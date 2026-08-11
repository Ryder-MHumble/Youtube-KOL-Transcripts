---
title: '江鋆晨: KV Cache，大模型记忆，清华姚班，CMU，教授，开源，视频流媒体（外部迁移分析）'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=yWTVEG9UIHo
video_id: yWTVEG9UIHo
transcript: '[[江鋆晨 KV Cache,大模型记忆,清华姚班,CMU,教授,开源,视频流媒体 [yWTVEG9UIHo]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260609-uncle-moon-junchen-jiang-kvcache.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[江鋆晨 KV Cache,大模型记忆,清华姚班,CMU,教授,开源,视频流媒体 [yWTVEG9UIHo]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=yWTVEG9UIHo) · 视频 ID：`yWTVEG9UIHo`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260609-uncle-moon-junchen-jiang-kvcache.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 从网络视频流媒体转向 LLM 推理系统的一线学者+创业者视角。江鋆晨（清华姚班→CMU 博士→芝加哥大学教授）把 KV Cache 定义为**大模型自己的记忆 / "只有大模型看得懂的视频"**，并押注它是继模型权重、prompt 之后**下一个最大的数据层**。本期是本库 [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md) 的核心中方素材，并与 [Dan Biderman：AI 的记忆问题](https://github.com/nolimitkun/ai-kol-wiki/blob/main/videos/20260713-latent-space-dan-biderman.md) 形成"记忆/长上下文"主题的直接呼应。

> ⚠️ 转录说明：本页已归一化专有名词——KV Cache（转录作"cdcatch/KB cache"）、LMCache、CacheBlend/CacheGen、TensorMesh（"Tencent Mesh"）、vLLM、SGLang、Ion Stoica（"一样"）、Hui Zhang / 张辉、刘斌、姚期智。

## 概要

覆盖：存储涨价与 KV Cache 的关系、清华姚班与 CMU 求学、导师 Hui Zhang 与 Ion Stoica、"工业界染缸"论、做教授 = 提出问题而非解决问题、"高阶 CS 课就是历史课"、视频流媒体研究与 CDN、KV Cache = 大模型的记忆 = 给大模型看的视频、LMCache 如何从"太超前"变成开源事实标准、TensorMesh 公司与 slogan、prefill vs decode 的算力误区、OpenAI API 兼容格式 = AI 时代的 IPv4、硬件"IBM 化" vs disaggregation、以及给不同年龄段的职业建议。

## 核心观点

### 存储涨价与 KV Cache
- 存储涨价是**供需失衡**的商业规律；但深层问题是"AI 时代所有人只盯算力，没人考虑存储"——**算力越多、存储要求越高**。KV Cache 这类"模型运行时生成的数据"正是当前存储压力的重要来源之一，"我们可能也是涨价原因之一"（[00:01:02]–[00:02:03]）。

### KV Cache = 大模型的记忆 = "给大模型看的视频"
- **核心预测**（"欢迎钉在网上以后验证"）：KV Cache（或类似的"模型自己生成的内部记忆"）会成为**比人能看懂的数据更重要的数据类型**；因为足够多比例的人类在高频与 Transformer 交互，其内部记忆就是最重要的数据（[00:40:55]–[00:41:55]）。
- **两个比喻**：
  - KV Cache 是 Transformer 的"记忆"——模型没在训练中见过的新知识（如你给它的一段新程序）（[00:41:55]）。
  - **"KV Cache 是给大模型看的视频"**：视频把线性文字变成三维、人更高效接受；KV Cache 与视频**都是 3D tensor**，是"只有大模型才看得懂的视频"，模型看了立刻理解其含义（[00:42:56]–[00:43:56]）。
- 因此他们做的是**管理和修改大模型的记忆**，而不只是存储（[00:43:56]）。

### 从视频流媒体到 KV Cache：同一套"数据层"直觉
- 博士做**网络视频流媒体分析**：2010 年前后每家媒体公司都要有"video streaming strategy"（如今每家要有"AI strategy"），只能用 HTTP（唯一被所有运营商支持的协议）——工业界野蛮生长、无人研究，他去 reverse engineering 各家协议、做第一个看清"公有问题"的人（[00:25:34]–[00:33:48]）。
- **CDN 的普适规律**：任何应用只要规模大到"人类相当比例高频使用"，就必定需要一个**数据层**让数据的分发/共享/分析更高效——web 时代是 CDN、大数据时代是 HDFS/Spark、**AI 时代就是 KV Cache 这一层**（[00:37:50]–[00:39:52]）。这是他从视频→KV Cache 的底层脉络。
- 选 KV Cache 还有现实原因："我们做网络出身，需要大数据；input token 数据量太小没挑战，视频输入当时（多模态没做好）做不了，而 KV Cache 正好是可复用、可存储、可跨模型传输的 3D tensor"——"撞到枪口上"（[01:14:17]–[01:15:18]）。

### LMCache：从"太超前"到开源事实标准
- 研究先做 KV Cache **压缩（CacheGen）**与**非前缀复用（CacheBlend）**；出去讲 talk 时才发现工业界"根本没有 KV Cache 存储系统"——推理引擎生成完 KV Cache 就丢掉，"我们走得太超前"（[01:15:18]–[01:18:18]）。
- 两个选择：放弃，或"帮工业界把这套机制做了"——于是**开源 LMCache**（当时叫 internet of agent，想仿 AMPLab 联合 database/networking/AI 老师）。开源成功后用户越来越多，才去开公司（[01:16:18]–[01:19:19]）。
- **以学术研究组挑战整个工业界，赌对了**：工业界真想做这套系统时"已经很晚"，LMCache 功能已比较完善，很多公司直接复用甚至 resell LMCache；类比 **Spark"踩着工业界实体出来、把类似项目一个个干掉"**（[01:19:19]–[01:21:22]）。NVIDIA GTC 上老黄把 LMCache 的 logo 放上大屏（[01:21:22]–[01:22:22]）。

### TensorMesh：让 KV Cache 成为独立解耦层
- Slogan："**不要为了模型在相同内容上重复计算来交钱**"——当前阶段最能被工业界理解的价值：把重复计算的结果以 KV Cache 存下，避免重算。例：模型读一个长程序回答问题，90%+ 的 input 是那个程序，存下 KV Cache 就跳过 90% 的重复计算（[01:24:23]–[01:29:28]）。
- 更大的**愿景**：KV Cache 不只可复用，还能**理解**（模型记住了什么、对哪些 token 注意力更集中）与**优化/改变模型行为**（优化 KV Cache 让它"看对地方、生成对结果"）（[01:29:28]–[01:31:30]）。
- **产品定位 = 把 KV Cache 层与其他一切解耦**：不与模型解耦（KV Cache 仍由模型生成），但与推理引擎、存储硬件、GPU、运行环境解耦，让任何 engine/storage/架构都能把 KV Cache 存进 LMCache 这个"公共 layer"（[01:36:33]–[01:38:35]）。
- **为什么用开源而非引擎自带**：开源给用户"随时可换各层选择"的自由；强解耦的 KV Cache layer 只有在各种场景性能都足够好时才成立；这是一件需要社区（各芯片/存储厂商工程师）一起做的事——推向**工业界事实标准**（[01:38:35]–[01:40:36]）。

### prefill vs decode 的算力误区（反直觉）
- 硬件创新（Cerebras、Groq/LPU 等）多集中在**更高效的 decoding**（生成，用户直接看到"一个字一个字蹦"）；但 TensorMesh 优化的是 **prefill（输入分析）**（[01:31:30]–[01:32:31]）。
- **反直觉论断**：人感官上 90% 时间在看 decoding，但 **90% 的算力其实花在 prefill / 处理 input** 上——因为 agent 的 input（几十万~几百万 token）远长于 output（几千~小几万），且"任何 output 以后都会变成 input"。"大家都以为芯片在优化的 output 是算力大头，其实不一定"（[01:32:31]–[01:34:32]）。

### OpenAI API 兼容格式 = AI 时代的 IPv4
- 网络的"细腰（narrow waist）"是 IP layer——所有应用承认的通信接口，在其上做创新极难（IPv6 比 IPv4 好却因为大家都在用 IPv4 而没成）（[02:05:51]–[02:06:52]）。
- **OpenAI API Compatible 的 query format** 就是当前 AI 生态里"稳定下来的中间结构"——所有应用/模型/推理服务商都承认的接口；AI 框架成熟得比互联网快得多，某些部分已达成共识（[02:04:50]–[02:07:54]）。
- **预测**：会有更多这种稳定协议出现，**KV Cache 有可能是下一个或再下一个**这样的"层"——等跨服务复用/传输 KV Cache 的需求变多（[02:07:54]–[02:08:54]）。

### 硬件"IBM 化" vs disaggregation
- **被低估的盲区**：硬件厂商正在"IBM 化"——把处理器/网络/存储 bundle 成大型机一起卖以最大化 margin；但学历史会发现**大型机没成为数据中心主流**，因为不是最省钱/最灵活的方法（[02:08:54]–[02:10:55]）。
- 真正成为大规模计算平台的是"把便宜的 memory/存储/CPU/网络用最聪明的方法连起来"的数据中心；**disaggregation（分离式架构）做到极致**——每块特殊化、可随时替换，"如何组合"才是核心难点——可能带来颠覆性的新 AI infra 组织结构（[02:10:55]–[02:12:57]）。

### 方法论：读历史、进"工业界染缸"、做老师=提出问题
- **"高阶 CS 课（advanced OS/networking/database…）其实是历史课"**：读经典 paper 不是教你写 paper，而是上历史课——"只有看到历史上什么重要，才能反映未来会发生什么"；infra 人尤其要读科学/技术史（PARC、Bell Labs）（[00:58:08]–[01:02:10]、[01:12:17]–[01:13:17]）。
- **"工业界染缸"论**：研究员去工业界实习别带 research 偏见，"把自己三个月卖了当工程师"、混进去看第一线工程师在吵什么问题——回来再用研究员视角想"这能不能写 paper"；很多这种问题一年后就变成大家都碰到的重要问题。学术界太容易变成 bubble / "真空中的球形鸡"（[00:46:57]–[00:54:06]）。
- **做老师 = 提出问题，不能是解决问题的人**：好 PhD 变博导会 struggle，因为要把"解决问题的热情压下去"；最好学校的老师有"改变大家想法、把不重要的事变重要"的 luxury（[00:54:06]–[00:57:07]）。判断高价值问题的两条路：读历史找循环、与工业界紧密合作做"第一个看到 gradient 的人"（[00:59:08]–[01:00:08]）。

### 师生联合创业的"稳定结构"
- 学生做的项目快毕业了→不创业项目就断了；把 research idea 源源不断输送工业界"绝不是开源项目或学界能做的事，必须拉投资开公司"（[01:22:22]–[01:23:22]）。
- **观点：老师创业不成功，很大原因是学生没跟着一起做**。师生结构有"根本想不到的好处"——老师信学生执行力、学生信老师 vision，是先天磨合过的稳定结构；"身边同背景创业没带学生的，几乎都没成"（[02:00:48]–[02:03:50]）。即使短期学生说"技术上做不了"，因为有 trust，也相信那是真的技术判断而非搪塞。
- 投资人是"完全新的生物"：教授不懂融资套路反而无妨——"投资人看人太多了，只要你做的东西是他觉得是金子、看得到未来的东西，低级错误也能原谅"（[01:56:45]–[02:00:48]）。

### 给不同年龄段的建议
- **22 岁**：做对自己最有挑战性的事（呼应 AMD 苏姿丰"越年轻越要接受挑战"）——"只有做最难的事才学得最快"（[02:17:03]–[02:18:03]）。
- **PhD 在读**：想清楚是否真要当老师（CS 当老师必须做到领域最好）；若不一定当老师，就做能接触**工业界最前沿**的研究——因为"工业界里 PhD 太多了，真有值得做研究的东西工业界会做得很快"（[02:18:03]–[02:20:05]）。
- **25、26 岁在工业界**：现在读 PhD 是好事——你以前做的东西早晚被 AI 替代，需要充电找 differentiator；充电不一定去学术界，去 startup 也行（"startup 有强生存意识，逼你做无法替代的东西"）（[02:21:06]–[02:22:09]）。
- **30 岁**：把握"与志同道合的人一起做一件别人不看好但有潜力的大事"的机会——不一定创业（[02:23:09]–[02:24:10]）。
- **个人最想改变的决定**："更早开始做 AI infra——2023 年才做其实有点晚"；一直不信 training infra 是未来（"太一次性、太幕后"），模型绝大多数生命周期在推理（[02:15:00]–[02:17:03]、[00:44:56]–[00:45:57]）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（KV Cache 数据层、prefill vs decode、OpenAI API=IPv4、IBM 化 vs disaggregation）
- [LLM 心理学与认知短板](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-psychology.md) / [Dan Biderman 访谈](https://github.com/nolimitkun/ai-kol-wiki/blob/main/videos/20260713-latent-space-dan-biderman.md)（"记忆/长上下文"主题的直接呼应：KV Cache 作为可管理的模型记忆）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（中方 infra 学者/创业者视角）
- [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)（taste / design taste 作为 AI 难替代的差异化能力）
- [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md)（师生联合创业的稳定结构、做老师=提出问题）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
