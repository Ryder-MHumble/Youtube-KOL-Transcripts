---
title: '[1hr Talk] Intro to Large Language Models'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=zjkBMFhNj_g
video_id: zjkBMFhNj_g
transcript: '[[[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20231123-karpathy-intro-to-llms.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g) · 视频 ID：`zjkBMFhNj_g`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20231123-karpathy-intro-to-llms.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

Karpathy 用一小时讲清 LLM 是什么、怎么训练、能力如何演进（工具使用、多模态）、
未来方向（System 2、自我改进、定制化、LLM OS），以及这个新计算范式特有的安全问题。

## 核心观点

### LLM 的本质
- LLM 就是两个文件：参数文件 + 运行代码。Llama 2 70B 的参数 140GB，推理代码约 500 行 C，无需联网即可在 MacBook 上跑（[00:01:00]–[00:03:01]）。
- 预训练本质是**对互联网的有损压缩**：~10TB 文本 → 6000 GPU × 12 天 → ~$200 万 → 140GB 参数，压缩比约 100 倍；且这在 2023 年已是 "rookie numbers"，前沿模型要再乘 10 倍以上（[00:04:01]–[00:06:04]）。
- 目标函数只是"预测下一个词"，但这个目标足够强大，迫使网络把世界知识压进参数（[00:07:05]–[00:08:06]）。
- LLM 是**基本不可解释的经验性造物**（"mostly inscrutable artifacts"）：我们知道每一步数学运算，但不知道千亿参数如何协作；知识存取是"单向的"（reversal curse：知道 Tom Cruise 的母亲，却答不出反向问题）。只能靠行为评测来对待它们（[00:12:10]–[00:14:11]）。

### 训练管线
- 两大阶段：**预训练**（知识，几个月、几百万美元、一年一两次）+ **微调**（对齐/格式，一天级、可每周迭代）；可选第三阶段 RLHF——比较标注比撰写标注容易（[00:14:11]–[00:22:16]）。
- 人工标注正在变成人机协作，人越来越多地处于监督角色（[00:22:16]–[00:23:17]）。
- 生态格局：闭源模型（GPT、Claude）领先，开源（Llama 系）追赶——类比操作系统里的 Windows/macOS vs Linux（[00:24:17]–[00:25:18]、[00:45:30]）。

### 能力演进
- **Scaling laws**：下一词预测的准确率是参数量 N 和数据量 D 的平滑可预测函数，且看不到饱和迹象——"算法进步不是必需的，扩大规模就有保证的提升路径"。这解释了算力军备竞赛（[00:25:18]–[00:27:20]）。
- **工具使用**是能力跃升的主轴：浏览器、计算器、Python 解释器、图像生成——像人一样用工具解题，而不是"在脑子里硬算"（[00:27:20]–[00:33:23]）。
- **多模态**（看图写代码、语音对话）是另一主轴（[00:33:23]–[00:35:23]）。

### 未来方向
- **System 1 vs System 2**：当前 LLM 只有直觉式的 System 1，每个 token 耗时相同。目标是"把时间换成准确率"——让模型思考 30 分钟给出更可靠的答案（[00:35:23]–[00:37:23]）。
  - *（后注：2024–2025 年 o1/R1 等推理模型正是沿这条路线，此演讲是较早的公开预言之一。）*
- **自我改进**：AlphaGo 靠自我博弈超越人类，但语言领域缺少通用的 reward function；在有奖励信号的**窄域**可能先实现（[00:37:23]–[00:40:27]）。
- **定制化**：GPTs 商店、RAG、微调——走向"许多专家 LLM"而非单一全能模型（[00:40:27]–[00:42:28]）。
- **LLM OS**：把 LLM 看作新兴操作系统的内核进程，而非聊天机器人——context window 是 RAM，互联网是磁盘，工具是外设，还有多线程/用户态内核态等类比（[00:42:28]–[00:45:30]）。

### 安全
- 新计算范式带来新的攻防猫鼠游戏（[00:45:30]–[00:59:40]）：
  - **越狱**：角色扮演（"奶奶讲凝固汽油弹哄睡"）、Base64 编码绕过（拒绝训练数据以英语为主）、优化出的通用对抗后缀、图像中的对抗噪声。
  - **提示注入**：网页/文档里的隐形文字劫持模型，可用于钓鱼链接、经 Google Apps Script 外泄私人数据。
  - **数据投毒/后门**：训练数据中植入触发词（"James Bond"）使模型行为损坏——微调阶段已被论证，预训练阶段尚未有令人信服的展示。

## 相关主题

- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)
- [LLM OS 与新计算范式](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-os.md)
- [LLM 安全](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-security.md)

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
