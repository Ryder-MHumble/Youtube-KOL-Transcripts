---
title: Let's reproduce GPT-2 (124M)
source: repository_import
youtube_url: https://www.youtube.com/watch?v=l8pRSuU81PU
video_id: l8pRSuU81PU
transcript: '[[Let''s reproduce GPT-2 (124M) [l8pRSuU81PU]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20240609-karpathy-lets-reproduce-gpt2.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Let's reproduce GPT-2 (124M) [l8pRSuU81PU]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=l8pRSuU81PU) · 视频 ID：`l8pRSuU81PU`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20240609-karpathy-lets-reproduce-gpt2.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

四小时从空文件写到完整预训练：实现模型 → 榨干 GPU（11 倍加速）→ 照抄 GPT-3 超参 →
多卡 DDP → FineWeb-EDU 数据 → HellaSwag 评测。最终用 1/10 的 token 训练量超过了 OpenAI 原版 GPT-2 124M。

## 核心观点（方法论要点）

### 训练成本的坍塌
- GPT-2 124M：2019 年 OpenAI 训练估计 $40,000 → 2024 年复现约 1 小时、$10 级别（8×A100 跑 2 小时即超原版）。原因：数据更好、硬件更快、软件栈更优（[00:02:01]、[00:33:27]）。
- **数据质量 > token 数量**：在 FineWeb-EDU 上只训 10B token 就超过了原版 GPT-2（100B token 训练）的 HellaSwag 成绩，40B token 接近 GPT-3 124M（300B token）——约 10 倍学习效率提升，归因于数据过滤进步（教育质量过滤由 Llama 3 70B 自动判分）与原版数据分布分散（[03:44:30]–[03:50:36]）。

### GPU 优化阶梯（1000ms → 90ms/step，约 11 倍）
1. **降精度**：fp32 → tf32（一行代码，指令内部截断尾数，~3x）→ bf16 autocast（保留指数范围故无需 gradient scaler，这是它相对 fp16 的关键优势）（[01:23:11]–[01:47:34]）。
2. **torch.compile**（~2.3x）：去掉 Python 解释器逐层调度 + kernel fusion 减少 HBM 往返——"深度学习负载多数是 memory-bound，tensor core 大部分时间在等数据"（[01:47:34]–[02:00:46]）。
3. **FlashAttention**：torch.compile 找不到的算法级重写——flops 更多反而快 7.6x，因为从不物化 T×T 注意力矩阵；"flops 不重要，内存访问模式才重要"（[02:00:46]–[02:06:54]）。
4. **Nice numbers**："最蠢也最妙的优化"——把词表 50257 padding 到 50304（可被 128 整除），多算了反而快 4%（老版 PyTorch 上可达 30%），因为 CUDA kernel 按 2 的幂分块，丑数字触发低效边界处理（[02:06:54]–[02:14:02]）。

### 训练配方细节（照抄 GPT-3 论文，GPT-2 论文太含糊）
- AdamW(0.9, 0.95, eps 1e-8)、全局梯度裁剪 1.0（防坏 batch 冲击）、余弦退火到 10% + warmup、weight decay 0.1 只作用于二维矩阵参数（[01:56:42]–[02:34:13]）。
- 残差路径初始化按 1/√(2N) 缩放，补偿残差流方差随深度累积；wte 与 lm_head 权重共享（省 30% 参数，来自 Attention is All You Need 之前的 weight tying 论文）（[01:07:55]–[01:21:11]）。
- **梯度累积的坑**：loss 必须除以累积步数，否则丢掉 cross entropy 的 mean 归一化，梯度是错的（[02:39:18]–[02:44:23]）。
- DDP：只在最后一个 micro step 同步梯度（all-reduce 平均）；batch size 0.5M token 是与学习率等超参耦合的整体（[02:46:26]–[03:09:48]）。
- 他实测 GPT-3 的超参"极其保守"，max LR 可以 3 倍仍然更快收敛（[03:51:37]）。

### 评测方法论
- HellaSwag 被选中的原因：**平滑、有早期信号**（小模型也能从 25% 缓慢爬升）；小模型做不了多选题格式，只能比较各选项 token 序列的平均损失（[03:28:07]–[03:35:15]）。
- 提醒评测的陷阱：eval 太老可能渗入训练集，"你可能在看训练曲线而不是验证曲线"（[03:45:30]–[03:46:31]）。

### 其他
- llm.c：同一训练的纯 CUDA 实现，比 PyTorch 版更快（223k vs 185k token/s）、启动更快、占用更小；nanoGPT 作为其参考实现（[03:56:41]–[03:58:43]）。
- 预训练之后到对话助手只差 SFT："换成对话数据集继续训练，没有更深的东西了"（[03:55:39]）。

## 相关主题

- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)
- [LLM 实用方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
