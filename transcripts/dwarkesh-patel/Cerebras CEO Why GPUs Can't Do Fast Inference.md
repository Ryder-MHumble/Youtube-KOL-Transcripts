---
title: "Cerebras CEO: Why GPUs Can't Do Fast Inference"
source: "https://www.youtube.com/watch?v=UEOSUSz--Ig"
analysis_report: "[[Andrew Feldman- 快速推理不是体验优化，而是 AI 产品形态迁移的底层变量]]"
author:
  - "[[The MAD Podcast with Matt Turck]]"
published: 2026-07-23
created: 2026-07-29
description: "AI is no longer just a race to train smarter models. As AI moves into production, the bottleneck is increasingly inference: how fast models can generate tokens, use tools, reason, verify, and act. In"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=UEOSUSz--Ig)

AI is no longer just a race to train smarter models. As AI moves into production, the bottleneck is increasingly inference: how fast models can generate tokens, use tools, reason, verify, and act. In this episode of the MAD Podcast, Matt Turck sits down with Andrew Feldman, co-founder and CEO of Cerebras, to explain why fast inference may define the next era of AI.  
  
Cerebras is known for building a chip the size of a silicon wafer. But this conversation is not just about one company or one chip. It is a deep dive into the AI infrastructure stack: GPUs, ASICs, memory, HBM, SRAM, data centers, power, TSMC, AWS, OpenAI, agents, reasoning models, and why speed changes what AI products can become. Andrew explains why “tokens per second per user” matters, why generating a single word can require moving the equivalent of 100 HD movies through memory, why agents amplify latency, why GPUs struggle with certain inference workloads, and why fast AI may eventually reshape SaaS itself.  
  
This is a reference conversation on fast inference, AI chips, and the next compute bottleneck.  
  
Andrew Feldman  
LinkedIn - https://www.linkedin.com/in/andrewdfeldman  
X/Twitter - https://x.com/andrewdfeldman  
  
Cerebras  
Website - https://www.cerebras.ai/  
X/Twitter - https://x.com/cerebras  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark Capital  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id168623872  
  
00:00 Cold open & Intro  
01:31 Why speed became the AI bottleneck  
02:32 Tokens per second per user, explained  
03:16 AI’s broadband moment and the Netflix analogy  
04:35 The AI chip landscape: GPUs, TPUs, Trainium, ASICs  
06:36 What is an ASIC?  
08:08 Nvidia, Groq, and the fast inference war  
09:16 OpenAI, Broadcom, and specialized silicon  
12:10 China, power, and sovereign AI infrastructure  
15:05 Is the AI infrastructure boom a bubble?  
18:56 The hidden bottlenecks: HBM, CoWoS, and 3nm  
22:57 Why agents are creating CPU demand  
25:36 Andrew Feldman’s path from SeaMicro to Cerebras  
26:13 Why Cerebras bet on AI in 2016  
31:14 SRAM vs. HBM: why inference is a memory problem  
33:19 What wafer-scale computing actually means  
34:28 The deep-tech “Everest” problem  
36:07 The moment the first Cerebras system worked  
36:49 Ringing the bell and surviving deep tech  
39:08 How a giant chip handles failure  
41:22 Why GPUs struggle with decode  
42:17 Prefill vs. decode explained  
44:01 The “100 HD movies” problem in AI inference  
45:04 How fast inference changes RL and training  
48:08 Reasoning models and why they cost more compute  
50:08 Verification, guardrails, and small models checking big models  
52:37 Multimodal AI and the path to video  
53:51 Cerebras’ business model: hardware, cloud, and API  
55:14 OpenAI’s 750MW inference deal  
55:36 Why data centers are measured in megawatts  
58:01 AWS Trainium + Cerebras decode  
59:29 Fast tokens as a cloud product  
01:00:52 Is CUDA still a moat?  
01:03:53 How TSMC helped Cerebras build the giant chip  
01:07:41 Why nobody cared in 2020  
01:08:15 Why chip supply chains are hard to diversify  
01:09:54 Why today’s AI models will be the worst you ever use  
01:10:38 What fast AI could do to SaaS

## Transcript

### Cold open & Intro

**0:00** · This is the largest chip built in the history of the computer industry. It's 58 times larger than a GPU. And for AI, bigger chips process information more quickly and therefore you get answers in less time. For AI world, big chips are undoubtedly the best way to go. There's no mode in inference. It takes you eight keystrokes to move from a GPU to us in the cloud. We solved a problem that nobody in the history of computed solved. And we delivered it in 2020 \[music\] and nobody cared. Nobody cared.

**0:34** · Nobody bought it and nobody cared.

**0:36** · Everybody said we were crazy. It would never work. So then we built the next one.

**0:40** · Hi, I'm Matt. Welcome to the Matt podcast. My guest today is Andrew Feldman, co-founder and CEO of Cereubbras, the company that built the largest chip in the history of computing and just pulled off the biggest semiconductor \[music\] IPO of all time. Andrew has been everywhere talking about the headlines.

**0:56** · the $20 billion plus OpenAI \[music\] deal, the IPO. But this conversation is a bit different. We started from what is a wafer and built up step \[music\] by step. Why GPUs struggle with fast inference, the three shortages \[music\] nobody talks about, the decade in the desert when nobody wanted his chip, and why Andrew believes that CUDA is no longer a mode for Nvidia. If you want to actually understand the current chip landscape and how AI inference works at the silicon level, this episode is for you. Please enjoy this fantastic conversation with Andrew Feldman.

### Why speed became the AI bottleneck

**1:31** · I thought a fun place to start uh would be to talk about speed. So has speed become the dominant conversation for AI today.

**1:41** · Yeah.

**1:41** · What happened I think was uh for a long time AI was sort of a novelty, right? It was like a parlor trick. It was cool but not useful. And what happened somewhere around the middle of 2025 was the AI got smart enough such that people began to use it and we remember we we we make AI with training but we use it with inference and suddenly people wanted to use it and the minute you want to use it the minute it's productive right speed matters right

**2:13** · fast tokens are more productive and so the conversation moved from everything else to How do we make our inference faster? H how do we deliver tokens more quickly because those are more productive tokens? We get more done in less time and therefore it's more valuable.

### Tokens per second per user, explained

**2:32** · Great. And what does speed mean? Is that uh is that an equation of token speed?

**2:36** · Is that completion of the task? What's the right metric?

**2:40** · So the right metric is tokens per second per user. that that's how fast you get the first token all the way through the last token in in your uh in your response. And it's true for queries from from the chat, but it's also true for for agentics loads, right? Uh if they're sort of multicycle turns, waiting is amplified. And so what you want is blisteringly fast responses so that the the AI feels like it's in real time.

**3:11** · You can engage with this.

### AI’s broadband moment and the Netflix analogy

**3:16** · So it's the brain moment for AI.

**3:20** · I think I think that's right. And I I think that's a very good analogy. I I think if you think of something like like Netflix, right, when the internet was slow, right, Netflix delivered DVDs and envelopes. you would get a a DVD in an envelope and and when the internet became fast, they didn't get more efficient at delivering DVDs and envelopes. They became a movie studio, right? The speed enabled them to become something completely different. And that's what speed does uh in general and in particular for for AI.

**3:52** · It it opens up a whole new domain. It allows you to use the AI differently. You will stay longer. you you will come more often and you work on harder problems.

**4:05** · Yep. So it's literally a question of of the UX, right? That's just nobody wants to wait a few seconds.

**4:12** · That's great. I mean, how big is the market for slow search? How big is the market for dialup is zero. How big is how long will you wait for a website to resolve? Will you wait 8 seconds? Nobody waits. See? And so it's the exact same with AI.

**4:26** · Yep.

**4:26** · So no more people waiting with their laptops open uh while the agent That's right. Well, it's running and running and running. I I I think that is not what what people want.

### The AI chip landscape: GPUs, TPUs, Trainium, ASICs

**4:36** · Okay.

**4:36** · Great. Uh wonderful. So, uh I'd love to talk about uh the landscape of the chip industry right now to help people visualize and hard work where where you guys um are. So, um there used to be basically this concept of like one chip to do it all. uh and uh obviously this is evolving dramatically.

**5:02** · Um this you guys uh this this Grock uh this there are GPUs there are people have heard of tranium people have heard of TPU so help us compare and contrast like who does what for what well I I I think there used to be one chip to do it all was called the CPU right and uh there emerged a co-processor to do discrete graphics and uh as the AI workload became interesting.

**5:32** · We focus chips more and more on that particular workload and today several companies make traditional GPUs. So Nvidia and AMD make very standard GPUs. Um there are a group of companies who uh the hyperscalers make make some of their own parts. So the TPU so TPU is Google TPU is Google and Tranium is is uh AWS.

**6:00** · Yep.

**6:01** · Um and then there were group uh like Sburus um and we were among the pioneers to to to build a part from scratch uh optimized for AI and nothing else and that we weren't inside of a hyperscaler. We weren't optimized for a hyperscaler's problem or for one lab's problem. We we were building a a a chip for a collection of of AI problems and all our thinking was around how to accelerate AI.

**6:34** · And that's sort of the landscape to this day.

### What is an ASIC?

**6:36** · Yeah.

**6:36** · There's even more specialized ones, right? Like edged developed specifically for transformers. Then those are called AS6 as well. Could can you maybe define what that term means? And as is an application specific integrated circuit and and it's um uh it's a word that that now has a a wide range of of meaning. It it means that you have made a series of choices away from general towards a narrower class of uh problem solving

**7:12** · and that you've made some decisions in your architecture that make it much better at some things and much much worse at others. Right? And and that's uh choices that are made across the spectrum. So the TPU has made some choices like that. It can't do graphics. It's very good at matrix multiply. It's not very good at a collection of other things that we do in in mathematics.

**7:39** · Um uh uh same for the GPU. We we've all made different choices. I was right now in production there are uh and there are a collection there's the TPU for Google tradiums. uh just coming up is a Maya part is a part from uh uh uh Microsoft uh Cerebrus and there was one other uh grow up that got acquired by by Nvidia.

### Nvidia, Groq, and the fast inference war

**8:08** · Yeah.

**8:09** · And to the general chip versus pis chip it was actually interesting because you guys and your CTO celebrated when Grock was acquired. Was that what was that?

**8:20** · Was it a recognition by Nvidia that your vision was right all along? Yeah, I I think uh one of the things India's sort of most durable modes was the perception that the GPU could do everything and it was all you needed for AI. And the acquisition of Grock for $20 million and the structure and the speed with which they chose to do it made clear to everyone that that wasn't true.

**8:51** · that uh the GP architecture couldn't do could not do fast entrance and that this market was large and growing quickly and we were the fastest at it and the largest and you know our sales were more than 10 times the Gro and they paid 20 billion for the number two player.

**9:12** · So that was a good day.

**9:15** · That was a good day. Right. And um the recent announcement uh of Halino between Open which is a very large customer of yours and Broadcom. Uh where does it fit in that picture? Is that one of those highly specialized aix right Gro for inference?

### OpenAI, Broadcom, and specialized silicon

**9:34** · That's right. Jalapeno is a is a part uh that has been a long time coming. Um it was uh announced with Broadcom before uh OpenAI did the deal with us. Remember we did a huge deal. This is probably the largest deals in Silicon Valley history north of 20 billion dollars.

**9:54** · Um uh I I think they have a a yawning need for silicon and the uh one of the things that open AI has been I think the the best uh in the industry at is looking at an exponential curve adoption rate of growth and not being afraid of what it says. Right?

**10:20** · Others have had to go out and strike really bad deals to get capacity where OpenAI saw this coming. They struck big deals for memory, for compute, with us, with others. Um, they've really been sort of visionary in understanding the what it means to extrapolate from an exponential curve and that curve is is AI usage, right? It is growing so unbelievably fast. The whole industry is chasing demand. Faith, right?

**10:53** · We usually uh well often it's the other way. Often people are building it hoping it will come and in our case all of us are are are chasing what people already want to do, let alone what they might do in the future.

**11:10** · Put a bit um because that's such an interesting topic. um to to to finish on GPS versus inference versus A6. Uh is that the permanent situation from your perspective that we're going to be in this uh forever multi-silicon kind of environment?

**11:30** · Yeah, multi silicon environment is a healthy ecosystem, right? I I don't think anybody would say that the x86 environment was was a healthy place.

**11:38** · There were for 20 years there were two players and if you notice when a new workload came around cell phone workload it was very similar but required uh low power and battery and both lost right Intel got zero share AMD got zero share and a company nobody previously heard of became the largest seller of compute in the world and that's our A and that uh healthy ecosystems have lots of different ways to to solve problems.

### China, power, and sovereign AI infrastructure

**12:10** · Where where does uh China fall in all of this? So there's the Huawei Ascent chips for deep sea and this emergence of a full stack Chinese um AI factory for lack of a better term. Is that is is that divide happening or is that overstated?

**12:29** · No, no, that that divide is real. I I think they are an industrial adversary that I think um they have made really interesting investments that made investments in power in their grid which is a real weakness in the US. Um if you're in France you have nuclear which sort of turns out to be pretty cheap power and pretty clean.

**12:51** · Um but uh in China they made huge investments in their grid. uh they are behind in chips um but their approach was at the next level as open- source models where they producing some extraordinary models not as good as as as GPT or anthropic or Google's Gemini but very good and I I

**13:20** · think uh they don't have the the same chip strikes that the US does but they've got leadership in other debates potentially in power which is what we need for daily sellers.

**13:32** · Okay. Where does China fall in third race strategy?

**13:36** · We don't sell questions uh for geopolitical reasons, for business reasons, for regulatory reasons, for regulatory reasons and and for some uh geopolitical reasons.

**13:50** · Okay.

**13:50** · Um is there a role for uh local AI and local chips? Nvidia had some announcement around just building chips for Windows computers. Is that for inference? Is that something that you guys uh think should be part of the multi ecosystem?

**14:09** · Yeah, I think uh if you look at the way the ecosystem for uh apps and cloud emerged uh everything you can do you should do on your phone or your laptop.

**14:22** · But the the the ability to get real processing power to a phone or to a laptop is constrained because they're generally working off a battery. And so you want to do as much as you can as as close to the data as you can. But the truth is is in most situations for real comput.

**14:44** · And that's exactly the way it's going to be with AI. We're going to do a lot of work uh uh on the cell phones uh on the laptop but for the big work you're going to go to to the data center and that's where our focus is. Our focus is is data center compute free.

**15:01** · Great. Um so you mentioned the the uh how powerful the demand was and demand out of you know of production. So u just to ask the inevitable question around um market equilibrium bubble or not. So like the most recent um thing we all saw is that there was a bit of a flash crash earlier in June where 1.5 trillion in market value was lost and Nvidia had lost 300 billion that day. Now that was corrected within you know 48 hours.

### Is the AI infrastructure boom a bubble?

**15:31** · So the market seems uh very jittery uh around that that general concept just uh would put the words just based on what you said sounds like you your reserve a play on the other side of that concern uh I I I think that that if you spend a lot of time staring at the at the public markets um and watching their ups and downs every day you're you're watching the wrong thing.

**16:01** · I I I think that right the the wisdom uh received from uh the great thinkers of public market investing is that that in the short term the public markets are are voting mechanisms who's most popular but in the long term they're weighing mechanisms who's created the most value the most weight and so what we can do as a newly

**16:28** · public company is we can not look at the day-to-day fluctuations and we can focus on just building extraordinary technology, winning new customers, making our existing customers happy, ensuring they buy more, um being better every week, and and so I I think the the day-to-day fluctuations are out of our hands. Um and that's about the voting.

**16:53** · Yeah.

**16:53** · And I mean, just to play a devil's advocate on the demand, um it seems like a lot of the demand comes from the big labs which you know themselves are financed by uh venture capital, private equity, hedge funds, whatever you call it in you know sovereign investors. Um is is there any concern that you know demand for chips comes from the labs which are maybe artificially financed and that the you know if you add a few circle of deals here and there you sense any fragility.

**17:25** · Um I I that's not exactly our experience. I mean obviously we have uh enormous demand from inopan but we have huge you know dozens of other customers who who are trying to place in very big orders ops and uh historically bubbles were when supply got out ahead of demand right when uh in the 90s we built out telco infrastructure right we built out fiber years before it it was going to be used

**18:03** · and it took six or eight years and it all got used but it it was a sort of if you build it they will come mentality whereas what's different about AI right now is we're all trying to catch up um we're trying to build data centers faster we're trying to increase our our demand our our our supply chains for demand that's already here today and only a very small portion of the the world are are using AI anywhere close to its potential and we're already sort of overwhelmed with compute.

**18:34** · We're um overwhelmed with uh the demand for for memory which is a real weakness and the GPUs is not a problem we face and the ecosystem they're constraints left and right and that doesn't feel like a bubble.

**18:55** · Do you want to actually double take on that? because that's uh so interesting, right? It seems like the bottleneck keeps moving because uh so what's the current problem of a memory shortage that people may have heard of?

### The hidden bottlenecks: HBM, CoWoS, and 3nm

**19:07** · So uh there are three major bottlenecks right now. The first is all GPUs and all AS6 except us um use a type of memory called DRM and a particular flavor of that memory called HBO and uh that memory is made by three companies in the world, Samsung and Microsoft.

**19:38** · Three companies and they're sold out.

**19:44** · That's the number one problem. We don't use it and it's sold out as in like the only way to as all things hardware the only way to increase supply would be to build new factories.

**19:53** · Build more factories and so uh you have this huge problem for GPUs and uh even now for CPUs and you can't get this memory because of our architectural choices. We we don't use it.

**20:10** · The second constraint was a process at TSMC process was called co-ass and this used silicon as a motherboard and this is what Invidia and AMD uh and others use as a motherboard. So they put their chips and the memory chips on it and it's more efficient than a traditional motherboard. ahead that process is sold out is highly constrained.

**20:44** · We don't use it. Third limitation in the space is 3 nanometer factory space at TSMC. So this is the most aggressive factory. So with the the most advanced technology, our chips are at 5 nanmter. So we don't use the three nanmator technology. And so and and that's so fascinating. So uh to ask the layman's question. So this this this what does that mean stream factory?

**21:12** · There's a factory that's solely dedicated.

**21:14** · That's right. They they build factories and the factory etches transistors that are a certain distance apart. And the smaller the distance apart, the more transistors per square millimeter. And the more you can do per square millimeter.

**21:34** · And so the history of the computer industry making chips has been we've gotten better and better at putting transistors closer and closer.

**21:44** · Yep.

**21:45** · And so we used to be at 16 nmters apart and then we went to 10 at to seven and to five at three and they're working on two 1.8. And so right now the bulk of the the the GPU world is all three and there's tremendous congestion at the factory and that's literally different tooling at the factory tooling at the factory and we use uh the 5m factory and this is our ship here.

**22:18** · Yes.

**22:20** · This is the largest chip built in the history of the computer industry. is 58 times larger than a GPU. It has, you know, two and a half or three thousand times more memory bandwidth.

**22:35** · Um, and for AI, bigger chips process information more quickly and therefore you get answers in less time. And obviously you don't want a bigger chip for a laptop or a cell phone or for lots of other things, but for AI world, big chips are undoubtedly the best way to go.

### Why agents are creating CPU demand

**22:57** · Okay, that's all right. So let's So I want to do a bit of a deep dive on that on the chip itself in a in a second. Um uh but to close on this, so three bottlenecks. Um you also mentioned CPUs a couple minutes in this conversation and there seems to be a theme around the emergence of like a CPU uh shortage as well. Is that so one is that true to what causes it?

**23:22** · So a gentic AI is a world in which AI doesn't just provide answers it initiates action. So that action might be go to a website. It might be learn, gather some data from a website, bring it back, take another action. Those actions are done by CPDs.

**23:51** · And so as AI gets better and better at doing things, at making instructions, calls for things to get done, we're using more and more CPUs, right? And that is driving up the consumption of CPUs and therefore the demand for CPUs.

**24:09** · And so this sort of huge push for more CPUs is being driven by AI on machines like ours and GPUs doing agentic work and asking the the the CPUs to take an action to go to a website to order burrito to find a piece of information to pull it from storage to all that work is being done by the CPU.

**24:38** · Yes.

**24:40** · Including in a system like yours in a system like ours.

**24:42** · Oh, it's interesting. So, so um what does that mean? So you you have your your chip and CPUs on the side and and those will be a system.

**24:51** · It means that um AI when we do AI the gentic they uh the AI processor is like the brains and the CPUs are like the body. They're taking action. They're doing things in the digital world.

**25:08** · under the direction of the AI which is running on the accelerator on the the server system. And so as we do more and more AI work and more and more agentic work, we're making more and more calls to CPUs and therefore the demand for CPU is just through the roof and CPUs experience the same memory short memory shortage they use the exact same number.

**25:35** · That's right. Okay. Yeah. Let's go back to the product in in a second, but um uh let's talk about you and your journey a little bit for for people to have context. So, you know, obviously you pulled and hold of an incredible um IPO with perfect timing. Um and I know I know it was a little bit they make the way you have perfect timing is to have horrible timing for 10 years.

### Andrew Feldman’s path from SeaMicro to Cerebras

**26:00** · That's the way you have perfect and very much to this point. So like you you guys uh started building this uh you know bigger chip focused on inference in uh you know over a decade ago 2016 2016 uh which u you know makes perfect

### Why Cerebras bet on AI in 2016

**26:17** · sense in in retrospect given how long it takes to build a technology like this but like what what was the the vision right 2016 I guess it was like four years after image net deep learning was a thing it was all it was all vision it was all revolutions and and that's why We we don't believe the right thing to do is to embed the the latest and coolest uh model into your circuitry.

**26:42** · That's a mistake. You know, we're the fastest in the world of transformers and our architecture was set before transformers existed, right? We're the fastest in the world of diffusion before and our architecture was set before confusion. What you want to do is get the underpinnings of those so that when

**27:00** · the market moves you can be good at that as well otherwise because short life to the ASX question earlier so that's what others do they build the architecture of the model into the some have some have and historically that's been a structural mistake it's been a structural mistake so you're doing the brand new horizontal platform on any kind of model you want to think about what is the underlying calcul calcation the underly calculation at all this work is sparse linear algebra.

**27:32** · Yeah.

**27:32** · And if you can accelerate that whatever the bottle makers invent you can make faster. Okay. And that was our approach.

**27:41** · Yeah.

**27:41** · So you started in 2016. Um you had a prior company that you sold to AMD.

**27:48** · What were some of the lessons you run there that you took into serious?

**27:52** · I think the lessons are large and medish. I think what one what are the things you know I guess experience is is another name for having made mistakes and learning from them right I I think you know we we have as a team built

**28:08** · dozens of chips over the past 25 years and the returns to experience and chipm is enormous and we built a different type of computer at at C Micro a type of computer optimized for low power and optim optimized for a workload that was very different than AI for something like web browsing

**28:33** · and uh but the the fundamental underpinnings the questions you ask as a computer architect are always the same what what can I do to to to make this work faster right and is there enough of it to make it worthwhile these are the two questions we ask um should we build a art for it. Should we what could we do to build a chip optimized for AI and will there be enough AI so that you can build business around it?

**29:03** · Those were the questions we asked in 2016. And you know the the the flip side of that was I mean wouldn't it be a surprise if the GPU which had been optimized for graphics for 20 years and been pushing pixels to a monitor was suddenly good at a new world. it'll that be serendipitous and we came to believe that that it wasn't the right architecture for it.

**29:32** · It was just better than the CPU and that we could build an architecture that would be vastly faster. It would use less power and could drive down the cost of of it and that was the journey. So service was very early but uh then we spent time in the desert. in the desert. Then we want then we wander in the desert.

**29:58** · Yeah.

**29:58** · Yeah.

**29:58** · Maybe maybe walk us a little bit through those years for any you know founders especially NDP tech founders listening to this. So um what was so first of all what was the issue with the market timing? Was it the technology was not working? Uh and then how did you go about it as as a team?

**30:18** · You getting your you on board and your investors and raising more rounds. So as as you presumably didn't have the proof points that one would need.

**30:26** · So for us we uh at the beginning we were honest with our VCs and told them we're going to attack a really hard problem. We we weren't going to build something that was a little bit better than a GPU.

**30:36** · And that our idea, our our strategy was that you will never beat a great company like Nvidia by doing something a little bit better than fake that they're going to buy everything for less. They're going to have pricing pressure. They're going to be able to bundle. And the right strategy would be to do something incredibly hard in engineering that was way better. 10, 15, 20, 30, 50 times better.

**31:04** · But to do that, the ordinary and obvious paths are all close. Everybody else has taken the bar. And so what we observed was that speed in inference was going to be a function of memory and that there were two types of memory. There's this VRAMP of HBM and they can store a lot but there's four.

### SRAM vs. HBM: why inference is a memory problem

**31:32** · There's another type of memory called Eser that is unbelievably fast but per unit area can't store very much and that for graphics everybody had always used DM they used HP and that the AI workload was fundamentally different in graphics you move data to the GPU and then you work on it for a long and then you send the result. So the time spent in total of movement plus work is dominated by work.

**32:15** · In inference and AI, it's the exact opposite. You move a huge amount of data, all the weights from memory to compute and you do one calculation to generate the next word and then you have to do it again. So all the time is dominated by the movement of data.

**32:36** · So that's why GPUs have so much trouble being fast. Okay. So we observed that if we chose a strategy using SRAMM, we could be faster. But then we have to overcome the tradeoff with SRAM. It can't store very much.

**32:52** · That led us to the solution. If we could build a part vastly larger than any part in history, right? at the size of a dinner plate. We could stuff it to the gills with SRAM and it and thereby get the benefit of SRAMM that it was fast and overcome the weakness that it can't store very much.

**33:12** · And that led us to a strategy called wafer scale. This chip is made from a single wafer that comes out of TSMC. Do you want to define what a wafer is?

### What wafer-scale computing actually means

**33:21** · A wafer, all chips are cut from a wafer. A wafer is a circular piece of silicon that's 300 mm across and the process of chip making stamps out like your mother does with a cookie cutter. Uh stamps out chips.

**33:41** · The biggest chip that had ever been built before us was 800 square millm. 840 to be exact. And this is 46,000. So we had to invent all sorts of new technology to build a chip this big. And once you build it, you have to invent ways to power it, to cool it. There are no vendors waiting for you. Yeah. Right. Because you look like nothing else ever made. And that took years.

**34:13** · And uh it it was a deep tip problem. It had never been solved before. And we had a an 18-month period where we were spending 8 million a month and we couldn't build them. So for your deep tech founders, you have 8 million a month.

### The deep-tech “Everest” problem

**34:29** · Yeah. And why why so much? What was the cost just to understand how these businesses?

**34:34** · Because what everybody thought was hard, we solved quickly. And and what nobody else knew about because they'd never actually done it turned out to be really hard. You know, imagine I tell people, imagine the first group that was going to climb Everest and they're at base camp and they're having tea with a group that just failed. And the group that just failed says, "Halfway up, there's this part. It's unbelievably hard. We couldn't do it." Okay.

**35:05** · Your team climbs up, makes it all the way to the top, comes back, they're having tea again, and the team that made it leans over the team that hadn't made it. Said that part in the middle, that wasn't the hard part because nobody had gotten past it. Nobody had gotten past certain things. So, they didn't even know what to be afraid of.

**35:25** · We we now know. \[laughter\] And it was something a step called packaging. And that's how you fix a wafer to a motherboard, how you deliver power to it, and how you cool it. And uh nobody had done it before. And over that 18-month period, we became the best in the world at it from approximately zero, right?

**35:46** · And we did that by sailing again and again and using good engineering methodology and doing a failure analysis every single failure. So we failed differently again and again and again.

**35:59** · And we told our board, you know, we met with our board every six weeks and yeah, this is the strategy. Nobody's ever done this before. Uh this is what we're going to do. And we had to invent new materials. We had to invent new techniques. We uh ended up building things that that everybody else had partners who could do. But in August of 2019, we announced we had solved it. And it'll my co-founders and I the first time it worked it was sitting in a tiny little lab and we couldn't believe it.

### The moment the first Cerebras system worked

**36:34** · We were the first few things that treated me to make one work. And we just stared at, you know, watching a server run is about as exciting as watching paint dry.

**36:42** · And there we were, the five of us just staring at this machine, not believing might have worked. \[laughter\] We made it work.

### Ringing the bell and surviving deep tech

**36:49** · Yeah. Um was it was it a bigger moment that actually ranging the bell or that just completely different like emotionally?

**36:56** · Emotionally it it was a completely different thing. Um it it was that we had made our idea work and I think for deep tech founders in particular um there's always this little thing in the back of your mind that says maybe it's \[laughter\] right?

**37:12** · Maybe we're actually crazy.

**37:13** · That's right. Maybe it's no fail and maybe it's not going to work. And uh maybe I don't have time. Maybe we're going to run out of money. Maybe maybe maybe. And the flip side of that is the joy that that this was my co-founder's ideas.

**37:28** · I mean these are their ideas manifest in the world and that is an extraordinary thing is when someone's ideas take physical shape and then the next step is when you watch other people's work sit on top of your idea then you know you love making infrastructure and so when we rang the bell and we went public on May 14th uh this year in the largest semiconductor IPO about history.

**38:00** · Um what and we did something unusual. We invited all our engineers who'd been with us since the start. Everybody who'd been with us more than nine years and their families and we all rang the bell together. We all got up on stage. I mean

**38:16** · that was sort of a moment of of a different pride that that that we had done this together and that uh wish I'd managed not to die \[laughter\] at some time but it started up you know people are donest they don't tell you that but we we'd avoided some we'd made plenty of mistakes but we've been avoided the fandle ones and we we made it crew to a a level of success that

**38:48** · gave us the opportunity to to pursue a new level of success. That's what an IPO is. It's not the end. It's you've gotten to a plateau that you can chase a new level of success in the public market and and that felt pretty good, I'll admit.

**39:04** · Amazing. Amazing. Thanks for sharing. Um so just and then go a little deeper on some of the product and and technical stuff. Um so uh what are the tradeoffs uh of building a bigger chip? One that may come to mind \[clears throat\] is uh failure mode.

### How a giant chip handles failure

**39:27** · Sure.

**39:27** · Uh if you have a lot of little chips on a big wave for prison where you can isolate the problems. Yeah, if you have a big one, then everything won't fail in the same time.

**39:38** · So, you have to think very carefully about failure mode and and we invented a technique that had about a million identical tiles and if one fails, we can shut it down and we can use a redundant one and keep going.

**39:58** · And so if you're going to go big, you have to think about in the very architecture of the computer how you're going to manage failure. I mean the JPEGs have a huge failure rate. So I'm sure you guys have spoken about this. Infant mortality is enormous and they fail all the time. There's good data. Facebook put out a paper on the number of failures they get in a big cluster.

**40:22** · Now we can do some other things be because we have all this compute in one spot uh we can uh invest more to cool it. So we pioneered water cooling uh in AI systems and we run these much colder than GPMs and the failure mode in electronics is temperature and so by running them colder we are more reliable and so that was from an advantage but again we had to advance the technique to to to cool off a chip this big.

**40:56** · Yes.

**40:56** · And so I I think we we have a a systemal mentality, right? If you're going to do something big, you've made tradeoffs and you have to think about an architecture that allows for redundancy and repair. You have to think about the pros and cons of every aspect uh of the architecture and and that's how you do something different and new.

**41:21** · Okay.

**41:21** · and and again just to drive the the point home um to make sure there's I guess clear takeaway you know for people from from this conversation. So explain it to me like I'm maybe not five but 15.

### Why GPUs struggle with decode

**41:36** · Uh why is this faster than a GPU?

**41:40** · Like what fundamentally makes it faster and what country is super fast with a GPA?

**41:46** · How tokens are generated in inference is why it's faster in a in an inference to generate a word and our answers are a whole stream of words. It can be code. It can be pixels but call them words. Talk the weights of the model are moved from memory to compute a calculation occurs and that generates the word.

### Prefill vs. decode explained

**42:17** · Is a prefill versus decode.

**42:19** · That is both steps.

**42:20** · Okay. And you want to maybe explain what prefill and decode are.

**42:24** · Okay.

**42:26** · There are two steps in uh the computation necessary to do inference. When you type in the chat GPT uh explain to me the history of this village prior to World War II and it came to you. Two things have happened. The first thing is your prompt has been processed. That's step one. And step two, your answer has been generated. And the way your answer is generated is called decode. Okay? And decode is sequential.

**43:14** · Processing your prompt, which we call pre-fill, can be paralyzed. So you can process many of them simultaneously. But the speed with which you get an answer is a function of the decode and it is step by step by step in sequence and that can't be changed. And how you do that step is you move weights which are the intelligence from the model to compute to generate a word.

**43:47** · You do a calculation and you get a word and then that word is used to generate the next word where weights are moved from compute. So the process is one of moving weights from memory to compute. So well how big are the weights in a little model like a 70 billion parameter model. The weights are about the size of 100 HD movements.

### The “100 HD movies” problem in AI inference

**44:13** · So to generate a single word, you move a 100 HD boogies from memory to compute and then you have to move them again for the next word.

**44:22** · And you want to do this a thousand times to get a good answer. A thousand word answer. This is where HBM is slow. This exact step is where HBM is slow. And that exact step, it is where by having all the SRAMM here, we're blisteringly fast. And so the speed of moving weights to compute is about two and a half thousand times faster here than on a wen GP.

**44:54** · And so that's the essence of what we've been able to do here and why it's so much faster.

**45:00** · Yeah.

**45:01** · Fascinating. Do you think that models need will need need or will evolve as well in that fast AI world or is that just a problem? No. Exactly.

### How fast inference changes RL and training

**45:16** · Because remember two things are happening. One we want the models to be smarter and two one of the ways models are getting smarter is with RL and RL uses inference inside of training, right? And so the faster you can do the inference inside of training, the faster you're training.

**45:35** · I'm interesting. Is that is that a market for you guys in that's a market for us as well.

**45:39** · So you're not just in we do RL and we do traditional trading too. Not for the largest models for the largest uh labs but for the next tier.

**45:51** · Uhhuh.

**45:53** · for pre-trading for pure pre-training crude trading uh fine-tuning full set. So if you do uh pre-training I mean post training with RL some pre-training for the other labs um what I mean GPUs are still better than you for what job that so GPUs in trainings have some challenges that have been solved by a very narrow selections of the community

**46:29** · GPU is a very small chip and the calculations that we need to do in trading are very large and one of the most complicated parts of training is the breaking up the calculations and spreading them apart on multiple GPUs and that's called distributed compute that has historically been the domain of the supercomput world and is very difficult ult

**47:01** · not just because cracking a problem and having lots of others work on it is hard but they have to constantly share information and that sharing information is why they needed to buy Melanox right is they needed to control a fabric over which all this sharing in order to get an answer would happen that breaking up the a big matrix multiply a big calculation is called running tensor model parallel You are breaking up the tensor and spreading it apart.

**47:33** · And the best labs in the world are good at that, but nobody else is.

**47:39** · They when we run training, we don't have to run that way. We run what's called model par data parallel. And data parallel is very simple. And so it allows teams who were good and very good to quickly test ideas in training. And so we are easier to use and faster um because we allow them to use a technique which is much simple.

### Reasoning models and why they cost more compute

**48:08** · Let's talk about the enentic world maybe starting with with um with reasoning. Um I think I saw a blog post where um you guys have given stated that reasoning was was uh not always the the right solution for all problems. Like how do you how do you think about this and where does that fit in service world?

**48:30** · We're using as a technique um a little bit like uh when you were in 8th grade and you wrote different drafts of the paper. um single shot inference. You you get an you you write a query, you get an answer. It the easiest way to think about reasoning is you're going to do several drafts. It's going to break the problem up. It's going to solve it in parts.

**49:03** · It's going to bring them together. It's going to review the results. It's going to improve the results. And then it's going to give you an answer. And so that is going to take more compute. And if your computer is slow, that's going to be a more than an irritant.

**49:21** · That could be crippling speed. And so as the best models, all of them, whether they're domestic or Chinese, whether you're uh uh open AI or anthropic or Gemini, whether you're any of the Chinese mod, they all move to a reasoning approach. But that meant more compute was being used during inference.

**49:43** · That was a huge advantage for us because we were faster and it made the GPU slowness stack up and it made our speed have an even bigger advantage. And so this was a huge bone for us. We think this is uh going to stay as a fundamental essence of the way these models are are are run right now.

### Verification, guardrails, and small models checking big models

**50:08** · And you also wrote about um verification uh and whether um what was uh the bolt bottleneck in uh agents was whether the reasoning was good enough, whether they were smart enough or whether there was a verification problem.

**50:25** · Sure.

**50:25** · I I think the the verification problem uh is a little bit like the guardrail problems.

**50:33** · Um and uh what you'd like to do is after you have written two or three uh drafts of your answer, you would like to be sure that it wasn't wrong. And that's your verification step. And you can do that maybe with a different model. You can do that by asking your existing model a similar question in a different way. Right? All of these are ways you you can pressure test your result.

**51:07** · Um, guard rails uh can work the same way, right? You want to review uh either with a model or with another technique through a scoring mechanism that this question isn't out of line. that this answer isn't about how to make biological weapons or calling upon information that that that you are direct to the FBI, right? Um, and all of that takes compute time.

**51:39** · And so whether you're trying to improve uh through reasoning or whether you're running guard rails by being faster, all right, you can get results in less time.

**51:52** · Hey, so what do you think the world is evolving for agents? Is it a bunch of smaller models running faster doing more verification versus a large model?

**52:03** · Well, I think those work together. I think your big model produces an answer. And then you want to double you just want to check your data. I mean in in the journalism industry people would write papers that have data checkers, right? Somebody would go and make sure back in the world journalist check data be a data checker, right? That was a job. Each claim was checked independently.

**52:25** · Um that's a different model, right?

**52:27** · \[clears throat\] The made model wrote the piece and then a little model checked some of the answers. And uh I think that's a very a very good way to go about it. Where does a multimodality uh for the larger models uh falling in your world? Well, we just announced uh uh sort of that we were fastest in the world on on one of Google's multimodal models.

### Multimodal AI and the path to video

**52:51** · I I think the truth is is that there's very little text that doesn't have charts and graphs, right? you you you must to understand text uh be able to understand uh illustrations, graphs, uh charts and so that that's sort of the the first and easiest part and then you

**53:16** · ought to be able to create both right and then you ought to understand images and uh I I think the the new models are very very good at that obviously What follows that is video because uh a video is just a collection of images. Um but that takes an enormous amount of compute right now and that's one of the reasons it's been sort of set aside by the leading labs being so unbelievably mutation intensely.

**53:50** · Great. Um let's talk about the server business a little bit u because so you guys obviously uh chipmaker provider as we discussed you're also uh a cloud provider data center provider what's uh so what are the different parts we we make compute and that computes optimized for AI is the fastest at AI in the world

### Cerebras’ business model: hardware, cloud, and API

**54:14** · if you have a data center we will sell you hardware for deployment in your data center if If you don't have a data center and you'd like to rent it by the month for the year, we have data centers. They have so you can rent our uh our equipment through our data centers and through our cloud.

**54:33** · And so that allows us to get uh AI natives as well as large enterprises and and governments. And what's the it was 5050 last year. Uh and I I think this last quarter it was or maybe maybe 7525 in favor of of hardware sales. I I think this year it might be 50/50 and as our open AI deal continues 2012 it will probably be 3070 with 30 on premise deployments of hardware at the 7D cloud.

### OpenAI’s 750MW inference deal

**55:14** · Great. Let's talk about that operating ideal since it's such like a major historical milestone record making. Um, so it's it's providing up to 750 megawatt megawatt which is which is interesting by the way as a as a metric because a chip provider but this is power.

**55:31** · So is that short of hand for it's a shortand I mean it turns out right now and we didn't talk about this because there's sort of in the adjacent supply chain we we went through the shortage of of memory we went through the shortage of a process called co-ass 3 nanometer capacity the the other limitation in our industry right now is data center availability and I mean uh that is a limiting factor

### Why data centers are measured in megawatts

**55:59** · for everybody and that's why anthropic did a huge which is in sort of very expensive deal with Elon um for data center capacity. Um uh our deal with them with uh with open AAI was because data center capacity is a limiting constraint measured the way data centers are measured in in megawatts.

**56:24** · The the deal is 760 megawatt, 250 megawws in 26 uh on a multi-year lease, an additional 250 megawatts in 27 on a multi-year lease and an additional in 28 and multi-year lease.

**56:41** · And you're doing the data center for them or you providing the chips that go in the data center?

**56:45** · Data center for them. We're delivering a full cloud solution. So they connect to us via an API basically. Imagine 2026 do I immediately that's I I am looking for data centers my next meeting he's in with a data center provider we're doing a lot in Europe right now oh interesting a lot in the in the Nordics is that uh because it's closer to power sources yes it's because uh there is low cost

**57:18** · power on that clean lowcost power.

**57:22** · Yeah. Low cost.

**57:25** · Does it matter uh just like in their time business where the data center is is uh is located in terms of um spend.

**57:33** · Yeah.

**57:33** · There is an additional latency called transport latency and that's the speed of light through fiber to get from Helseni to New York and you have to account for that if your customers in New York and your data center is in Helsinki. Okay. I mean it's usually about 2/3 the speed of light being curious how long it takes. Um uh you would like data centers on the same kind of platforms.

### AWS Trainium + Cerebras decode

**58:02** · That's the open ideal. Uh there was an exciting deal with AWS as well where you uh it's a it's a code chip solution.

**58:11** · That's right. It's the disagregated solution you mentioned before where their panium part is doing the prefill and is doing the paralyzable step. So that's tranium that's trium is doing the the prefill step and our chip is doing the decode and so you get a lot more bullet streamly fast tokens.

**58:35** · It's a good deal for us. It uses their data centers. So these are deployments in the AWS data center. Yeah, it's fascinating, right? Like talking about this industry is how it seems that uh flexibility is so important. This just like delivering the solution like you need chips, you get chips, you need data centers, everybody's buying from different suppliers to reduce dependency.

**58:56** · I I think that's one of the reasons why we we went from being a traditional chipping system provider to also offering data centers is that what what our customers want or fast tokens and anything we can do to make the delivery of fast tokens easier. For some of them that's in their data center. For some of them it's with an API. just point your traffic to us and we'll point the fire hose with a fast token in the back.

**59:28** · Yeah.

**59:28** · And just to get a sense for where where where you start and where you stop on you or do not or at least currently provide the the the cloud version. So if I want to run Kimmy like I know you have like incredible stats for Kiwi and Gemma in the speed feel to mention them. Um but you don't run those as a service or do you do?

### Fast tokens as a cloud product

**59:54** · You do. Okay. So you have a service competing with the base stands and fireworks.

**1:00:00** · Yeah.

**1:00:00** · I I think um we have a an on demand service um where you can come to our site and and book a month. I think you can even buy buckets of tokens for for Kimmy or GLM or some of these models. Um uh many

**1:00:20** · of our customers come there, get excited about it and then move to a dedicated offering where they take hundreds of machines for a year or two or three or four um once they've proven out the um the benefit for them in their work. Often they do AB tests. Not surprising. People like faster.

**1:00:43** · Okay. So So we're just more like a testing.

**1:00:45** · It's a full environment. Okay. Um you can you can go and use it. It's at three.ai. Play around.

**1:00:51** · But fascinating. But that could become like yet another big cloud business. Okay. So you have chips, you have data centers, and you have a cloud business running in front on its fascinating.

### Is CUDA still a moat?

**1:01:04** · Um thinking about modes, so you know famously um Nvidia has cuda as well discussed mode. What's your equivalent?

**1:01:15** · Yeah.

**1:01:15** · Well, I don't think we must Korea. We we should talk about that.

**1:01:19** · Yep.

**1:01:20** · I think two years ago uh every uh state-of-the-art model was trained in a CUDA flow and right now Gemini is trained without CUDA. Enthropic cloud is trained without CUDA. Open AI is trained with CUDA.

**1:01:42** · So in a one or two year period they lost 70% share of training models or is the state-of-the-art um because uh Gemini is trained on TPUs it's very out of uh anthropic is trained on craniums and so the I think the the storage of the boat is still present where the data show the mode is clearly shrinking. Um there's no mode in inference.

**1:02:21** · Uh it takes you eight keystrokes to move from a GPU to us in the cloud.

**1:02:27** · It is eight.

**1:02:29** · Oh, that's it to move your traffic from uh GPU API to us. And so uh obviously Cuda was sort of enormously important in the creation of our industry and in allowing the the graphics processing here to be more general than graphics processing but since 23 24 live I think it's

**1:02:56** · ability to serve as a durable mo substantion and you have a whole ecosystem strategy as you think about your mode to the extent that any moat can be present in this industry like you built a whole ecosystem. Is that is that Yeah.

**1:03:12** · Yeah.

**1:03:12** · We've built an ecosystem. I I think um our moat comes from the fact that uh by virtue of our architecture we are doing things no one else can do.

**1:03:26** · And uh it's not uh that they can spend more money or or or they can't uh pay more for for this with GPUs. If you want fast, you can't have it. Well, I mean JP, it it doesn't work. And so that's where we're building sort of our strength and that's how we're we're sort of delivering value to customers. What do you think about supply chain?

### How TSMC helped Cerebras build the giant chip

**1:03:54** · We mentioned supply chain constraints for others, but what are your uh supply chain constraints? Are you old TSMC?

**1:04:04** · We are TSMC. Um, we had very close collaboration. They were investors of us. They've been exceptional partners. I'll tell you an unusual story. In 2017, we showed up and we were about 30 guys total. And we showed up in August. Horrible trend in Taiwan. Don't go to Taiwan in August. You know, it is brut.

**1:04:28** · Not that it's so nice here today.

**1:04:30** · \[laughter\] It's only 90 here.

**1:04:32** · Embarrassed.

**1:04:33** · Yeah.

**1:04:33** · But all the humidity and Yeah. You got put on a and we met with the leadership of TSMC. We said we we would like your little pipsqueak company. We believe we can solve a problem that nobody solved in history and here's how we would modify the way you make chips to make this possible. They thought about it and they said we agree let's do it in the meeting.

**1:05:06** · In the meeting in the meeting it it wasn't go away for a month in the meeting.

**1:05:11** · Was that they had a prepared mind or they were just exceptionally fast on their feet? Um first the salesperson had gathered the decision makers. Second uh we got our our proposal was sort of really good at allowing them to use what they were good at. And it didn't require them to change a huge amount, but it it did require them to make real changes.

**1:05:46** · And I think they saw this as sufficiently bold that they would learn as they did it. And they also knew that AI was better on big chips. thing and so a combination of fair mind, a willingness to take some risk, bold thinking from a very large company. Fascinating.

**1:06:10** · It is fascinating. I mean that's how big companies win, right? Um and how rare is that was extraordinary.

**1:06:18** · And what happened next? Like how long does it take between a decision in a meeting like that which senses exceptionally fast to two years?

**1:06:25** · Two years.

**1:06:28** · Chipm is a long hard process and most of the time your first chip isn't a winner and there are lots of of startups now some of them with really smart guys but their first chip will not be order the TPU Google had some of the best guys in the industry first chip wasn't a winner nor the second nor the third fourth was really good now they're on their eighth and it's really good chip okay um the anapa team at uh at AWS.

**1:06:59** · First chip wasn't great. Second, third chip really good.

**1:07:02** · It it takes time. And so we built a chip, we delivered it. And this gets to an earlier question you asked. You know, we solved a problem that that nobody in the history of computed solved. And we delivered it in 2020 and nobody cared.

**1:07:18** · Nobody cared. Nobody bought any and nobody cared. \[laughter\] She were like, "Oh god, nobody everybody said we were crazy. It would never work and now it works and like nobody want it." Um, so then we built the next one.

**1:07:38** · I mean, the first one we probably sold quite a year and nobody wanted it because the market was not ready or because the product was not good enough.

### Why nobody cared in 2020

**1:07:45** · Um, nobody wanted it because AI was a hobby. It was right. And who cares if your hobby is really fast.

**1:07:55** · Um, you care about fast when it's in production. You care about fast when you use it every day.

**1:08:01** · And so we built another one and you know that one we sold three or 500.

**1:08:06** · Yeah.

**1:08:06** · And we built the third one and we sold tens of thousands.

**1:08:12** · Amazing.

**1:08:12** · Yeah.

**1:08:12** · Isn't that interesting? Um and um so going back to supply chain uh do you need to think about u onouring diversification? So it's very hard to diversify away from TS chips are so hard and you actually when you design a chip part of the design is for the rules of that factory

### Why chip supply chains are hard to diversify

**1:08:37** · right so you can't take your design from TSMC and go to somebody else because a huge amount of the work was bid to be sure your design is within their rules and so even in I think only with one or two exceptions in history. Uh each chip generation goes to one fat. So that that's we're going to be with TSMC for our next generation as well.

**1:09:04** · I think some uh we have uh a supply chain that is built in many parts but we bring the chips back from TSMC to the US. We package in the US and we assemble in the US. We do our manufacturing in the US and then we ship from the US. I think when you're growing this fast as we are right there range of garden variety supply chain challenges you know a vendor screws up a batch it gets stuck in customs.

**1:09:36** · The number of of ways that that things can go wrong the supply chain is unbelievable. But we manage these every day and we're increasing our manufacturing throughput exponentially and so it's really uh that part of the business really well.

**1:09:53** · Incredible. So maybe to zoom out as the last question um what what's your best guess about how where all of this is going uh you know obviously who knows in AI in the next like few years but like in the next year or two.

### Why today’s AI models will be the worst you ever use

**1:10:08** · Well we know some things. We we know that the model we use it you're using it today.

**1:10:13** · Fable or GPT56 or will be the worst model you ever use. And whatever you think is cool about it right now is going to be boring and backwards in six plus and that is so exciting and I I think I watch the way our young engineers use it and it's very different than the way I'm using it and it's sort of a fun time where you can learn from your young team members that they're using AI very differently.

### What fast AI could do to SaaS

**1:10:44** · I think the business of dashboarding and the business the um the damage is doing the SAS is I think unrepairable you know we you could ask your AI build me a tool like Salesforce 30 seconds later you have a working tool that that

**1:11:07** · he's just unbelievable and all the things that that were difficult because they cut across you're inside organizational silos, right? But one of the things that's really hard is if you want to know for your top performing people, when was the last time they got a stock option refresh and how much uh holding power is left. So, how much uninvested stock they have left at today's price?

**1:11:34** · There's like five systems. You're you're in work days, you you're in your uh stock.

**1:11:40** · Yeah.

**1:11:41** · You're in your your car, you're in Card. None of them can and that's what a CEO wants.

**1:11:46** · How much holding powers for my top guys?

**1:11:48** · Yeah.

**1:11:49** · And I used to have little tools I wrote for this. And boom, I've got a a little app that that I had deep and spark right.

**1:12:03** · You go. \[snorts\] Well, what what a story. Uh it's just incredible to um hear all of this from you. What a journey um and what an exciting future. So, uh, thank you very much. I learned a lot and this was terrific. Thank you, Andrew.

**1:12:17** · Thank you for for having me on your show. I really appreciate it.

**1:12:22** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks, and see you at the next episode.
