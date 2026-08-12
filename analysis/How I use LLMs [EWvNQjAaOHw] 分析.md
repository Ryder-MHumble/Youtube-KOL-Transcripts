---
title: How I use LLMs
source: repository_import
youtube_url: https://www.youtube.com/watch?v=EWvNQjAaOHw
video_id: EWvNQjAaOHw
transcript: '[[How I use LLMs [EWvNQjAaOHw]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20250227-karpathy-how-i-use-llms.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[How I use LLMs [EWvNQjAaOHw]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=EWvNQjAaOHw) · 视频 ID：`EWvNQjAaOHw`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20250227-karpathy-how-i-use-llms.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

Karpathy 以自己的真实使用场景为例，系统过了一遍 2025 年初 LLM 应用生态的全部功能层：
基础对话、思考模型、联网搜索、Deep Research、文件上传、代码解释器、Artifacts、
Cursor/vibe coding、语音/图像/视频多模态、记忆与自定义指令、Custom GPTs。

## 核心观点

### 心智模型
- 与 LLM 对话 = 和一个"1TB 的有损压缩 zip 文件"聊天："我是 ChatGPT，我半年前通读了整个互联网，只记得个大概；我的讨喜人格是 OpenAI 的标注员用范例编程出来的"（[00:12:07]）。
- 聊天气泡的本质是双方共同写入同一条一维 token 流；context window 是宝贵的工作记忆——**换话题就开新对话**，无关 token 既让模型分心又拖慢速度（[00:06:03]、[00:16:11]–[00:17:12]）。
- 判断"能不能直接问 zip 文件"的两个标准：信息是否**非近期**、是否在互联网上**高频出现**；低频/近期/高风险的信息要用工具或核对原始来源（[00:13:07]–[00:16:11]）。

### 模型选择
- 时刻留意自己用的是哪个模型、哪个价位档——免费档常是小模型，更容易幻觉；专业用途值得付顶级档（[00:17:12]–[00:22:17]）。
- 他把各家模型称为自己的 **"LLM Council"**：同一个问题问遍 ChatGPT/Claude/Gemini/Grok/Perplexity，交叉参考（[00:22:17]）。

### 思考模型（RL 训练）
- 思考模型 = 用强化学习额外调出来的模型，会展开类似人类内心独白的推理链；这是近一两年的大突破，DeepSeek R1 论文是首个公开讲清楚的（[00:23:18]–[00:24:18]）。
- 使用策略：数学/代码/难题用思考模型换准确率；旅行建议之类不值得等几分钟。先用快模型，不满意再切思考模型（[00:29:21]–[00:30:21]）。
- 实例：他的梯度检查 bug，GPT-4o 没解决，o1 Pro / Claude 3.5 Sonnet / Gemini / Grok 3 / R1 都找对了参数打包不匹配的问题（[00:25:19]–[00:29:21]）。

### 工具使用
- **联网搜索**：模型自身知识有截止日期，近期/易变/小众信息靠搜索工具把网页装进 context window；各家集成程度不一，要自己留意（[00:31:22]–[00:41:29]）。
- **Deep Research**（搜索 + 思考 + 长时间运行）：像"按需定制的研究报告"，他用于补剂成分调研、浏览器隐私对比、实验室数据表等；但示范了一个失败案例——美国 LLM 实验室表格漏掉 xAI、混入 Hugging Face——**永远当第一稿，查引用**（[00:41:29]–[00:50:39]）。
- **文件上传共读**：他现在"从不独自读书"——把论文/古书章节喂进 context window 一起读，问答式阅读大幅提升理解与留存，尤其是跨领域文献（生物学论文、1776 年的《国富论》）（[00:51:40]–[00:58:47]）。
- **Python 解释器 / Advanced Data Analysis**：LLM 是"有点心不在焉的初级数据分析师"——能写代码画图，但会偷偷把 NA 填成假设值、外推结果与打印值矛盾；**必须读它写的代码**（[00:59:49]–[01:08:55]）。
- **Claude Artifacts**：为你现场定制小应用（闪卡、mermaid 概念图）——软件从"工程师写好给你用"变成"LLM 按需现写"（[01:09:55]–[01:14:00]）。
- **Cursor / vibe coding**：专业写码不去网页版复制粘贴，用有全部文件上下文的 IDE agent；"vibe coding"一词他自认大概是他造的——把控制权交给 agent，口述需求，不行再退回手工编程（[01:14:00]–[01:22:12]）。

### 多模态
- 区分"假音频"（外挂 STT/TTS 转文字）和"真音频"（audio token 原生进模型，Advanced Voice）；他一半以上的查询用语音输入，手机上约 80%（[01:22:12]–[01:30:15]）。
- 图像也是 token 流：模型本身不知道 token 是文字、音频还是图像块（[01:40:25]–[01:41:27]）。他的用法：营养标签/血检报告/牙膏成分先转录成文字再提问（确保模型"看对了"），用截图问屏幕上的任何东西（[01:41:27]–[01:47:30]）。
- NotebookLM 按需生成播客，适合散步时听小众话题（[01:36:22]–[01:40:25]）；视频生成模型进展快但他本人用得少（[01:52:34]–[01:53:34]）。

### 质量功能
- ChatGPT 的记忆库（跨对话前置的用户知识数据库）、自定义指令、Custom GPTs——本质都是省提示词的功夫；few-shot 示例永远比纯描述效果好，"教模型和教人一样，光讲不如给例子"（[01:53:34]–[02:04:39]）。
- 他认为 ChatGPT 是功能最全的默认选择，但各家各有所长：搜索用 Perplexity、Artifacts 用 Claude、"太道貌岸然就换 Grok"（[02:06:40]–[02:08:41]）。

## 相关主题

- [LLM 实用方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（思考模型 / RL 部分）
- [LLM OS 与新计算范式](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-os.md)（工具使用是 LLM OS 的外设层）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
