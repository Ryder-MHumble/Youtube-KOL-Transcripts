---
title: Inside Nemotron & NVIDIA’s AI Lab | Bryan Catanzaro
source_url: https://www.youtube.com/watch?v=Oojrfdl42LI
video_id: Oojrfdl42LI
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/bryan-catanzaro|Bryan Catanzaro]]'
published: 2026-07-02
created: 2026-07-23
language: en
speaker_attribution: contextual
description: NVIDIA is a chip company. So why does it put hundreds of researchers on building AI models — and then give them away for free? Bryan Catanzaro is VP of Applied Deep Learning Research at NVIDIA and one
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=Oojrfdl42LI)

NVIDIA is a chip company. So why does it put hundreds of researchers on building AI models — and then give them away for free? Bryan Catanzaro is VP of Applied Deep Learning Research at NVIDIA and one of the people whose work quietly underpins modern AI: he helped create cuDNN (NVIDIA's first deep learning product), co-invented DLSS, and named and built Megatron, the framework behind how much of the industry trains large models. Today he leads Nemotron, NVIDIA's family of open models — and Nemotron 3 Ultra, released just weeks ago, is one of the strongest open-weights models to come out of the US.  
  
Matt Turck sits down with Bryan for a genuinely deep conversation: the real business logic behind a chip company building its own models, the state of open vs. closed AI, and whether the US is falling behind China in open models. Then they go inside Nemotron itself — four-bit (NVFP4) pretraining, hybrid Mamba-Transformer architecture, mixture-of-experts, multi-token prediction, and multi-teacher distillation — all explained in plain language. Plus a rare look at how a modern AI research org actually runs, what it was like working alongside Andrew Ng and Dario Amodei at Baidu, why Bryan doesn't believe in the singularity, and his contrarian case that open AI is safer than closed.  
  
A reference conversation for anyone trying to understand where AI is really headed.  
  
Bryan Catanzaro  
LinkedIn - https://www.linkedin.com/in/bryancatanzaro  
X/Twitter - https://x.com/ctnzr  
  
NVIDIA  
Website - https://www.nvidia.com  
X/Twitter - https://x.com/nvidia  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id168623872  
  
00:00 — Cold open & Intro  
01:33 — Is open source AI catching the frontier?  
05:29 — Do closed labs blocking distillation slow open source down?  
07:42 — Is the US falling behind China?  
10:30 — Why companies actually choose open models  
12:39 — A "crazy" 2008 bet: machine learning on GPUs  
15:33 — Working with Andrew Ng and Dario Amodei at Baidu  
17:41 — Coming back to NVIDIA: DLSS and the birth of Megatron  
21:55 — The real reason NVIDIA builds its own models  
24:28 — Is Moore's Law really dead?  
33:37 — The Nemotron family: Nano, Super, Ultra  
35:09 — Built for agents: why NVIDIA bets on speed  
36:02 — How you train a 550B model in 4 bits  
39:25 — Hybrid Mamba-Transformer, explained simply  
42:31 — Mixture of experts — and why NVIDIA built NVL72 around it  
47:26 — Why a 1-million-token context window matters  
49:26 — Multi-token prediction: how the model predicts 5 tokens at once  
52:47 — Multi-teacher distillation: teaching one model from many  
58:01 — Where reinforcement learning goes next  
01:00:16 — Inside NVIDIA's research org: "the mission is the boss"  
01:04:03 — How NVIDIA decides who gets the GPUs  
01:10:53 — Why NVIDIA still feels entrepreneurial after 33 years  
01:12:58 — Why Bryan doesn't believe in the singularity  
01:17:50 — The AI backlash  
01:19:18 — The controversial case: open AI is safer than closed

## Transcript

### Cold open & Intro

**0:00** · If you accept as the truth that we're going to be running at the limit, then what that means is that the way to get more intelligence is to be more efficient. We can't get more intelligence by applying more force if we're already at the limit. We have to be more thoughtful about how we use what we have. We build tools, we build external organs that help us solve problems. You know, we we have an external stomach, we call it a kitchen. Now we're creating an external brain. What is the implications of an external brain? Pretty profound.

**0:30** · Nobody actually really knows.

**0:32** · Hi, I'm Matt Turk. Welcome back to the Mad Podcast. Open source AI is having yet another moment with powerful new models arriving almost weekly. And my guest \[music\] today is one of the very best people to unpack it all. Bryan Catanzaro leads NeMo Tron, Nvidia's \[music\] family of open foundation models. Now, not everyone realizes Nvidia has a massive effort to build frontier AI models, but it employs hundreds of AI researchers, and NeMo Tron 3 Ultra immediately became the number one US open weights model when it was released just a couple weeks \[music\] ago.

**1:02** · We begin this conversation with the state of open source AI and the race between the US and China. And then we go deep inside NeMo Tron for bit training, hybrid member transformer architecture, \[music\] mixture of experts, multi-token prediction, and multi-teacher distillation all in plain language. And finally, we get a real look at how a modern AI research organization actually runs, how you get many brilliant minds to build one model instead of 100 papers. Please enjoy this awesome conversation with Bryan Catanzaro.

### Is open source AI catching the frontier?

**1:33** · All right, Bryan, excited to do this. It seems that open source is having a better year. So, you guys at Nvidia just released NeMo Tron 3 Ultra, which is an important moment and the best open source open weights model in the US.

**1:49** · That was just a few days ago, and then even more recently GLM 5.2 came out, and that was another moment. So, it that things are accelerating in open source AI. It feels like a great place to start. What's your assessment about where we are and how wide the gap between closed source and open source currently is?

**2:10** · Well, it's really exciting to see all of the energy going into open technologies for AI because we know that um open technologies make it possible for people to innovate. You know, the internet is such a great example of that. Um we actually did have closed internets. I don't know if you remember things like America Online and Prodigy back in the day. Um and they were great. Um and open internet has also uh been amazing, right? Like so many different companies have been able to figure out how to transform their work um thanks to uh an open technology.

**2:42** · The application of the internet to retail is very different from the application of the internet to healthcare or manufacturing, but all of them have been totally transformed um by the internet.

**2:54** · Um AI uh I believe is uh also a very transformational technology and also a technology that needs to be applied in very diverse ways. And because of that, I believe that open technologies for AI are really fundamental. Um and it's very exciting to see continued um investment and development of open technologies from uh for AI from so many different organizations around the world. Um uh and uh you know, I I hope that that continues.

**3:23** · And what do you sense for how far behind open source is compared to closed source? This has been the the big trend of the last few years has been this sort of narrowing gap. Do you Do you think that open source is almost there or the bar keeps getting raised by the closed source models?

**3:43** · Well, I I feel like this question um uh it's maybe a tempting question because you know, it's fun to set up kind of competition, but but I actually feel like the whole AI community is moving very fast. Um and if you look, for example, at the progress in AI, whether it's closed or open, just over the past 3 months, it's been incredible. Um and so, if you're in a field that's moving really, really fast, I think that's more important than any particular gaps that might exist between different models, because the most important thing is, you know, how is AI developing as a field.

**4:17** · What do you think the drivers are to continue to progress in open-source uh AI? Is that the community? Is that big companies like Nvidia being behind it? Is that the global competition with China? What propels open-source AI forward?

**4:34** · You know, I think there's a number of things that that are pushing open technologies for AI forward. One is just the demand. You know, there's so many organizations that want to customize AI and want to integrate it deeply into their work in a way that really requires open technologies for AI. And so, so I think um the demand is certainly there. I think also it's just um uh the best way to develop technology.

**4:58** · Um and we've seen this, you know, for for many decades that technology is developed in the open, move quicker because we can all learn from each other. And um in an era where we're undergoing the most exciting thing to happen in technology in our lifetimes with the development and the deployment of AI.

**5:15** · Um what else do do computer scientists want to work on other than making AI awesome? And if working together as a community is the best way to do that, then that's also a driver that pushes the community towards openly developing technology.

### Do closed labs blocking distillation slow open source down?

**5:29** · To ask maybe a slightly cynical question, there is at least a part of the community that's wondering whether open-source as an ecosystem, not not Nvidia, but in general, has been progressing in part based on the ability to distill closed-source models and in a world where we're seeing the Anthropic and Febo 5's of of the world starting to

**5:59** · discourage distillation, do you think there is a chance that open-source AI progress may slow down in that context?

**6:08** · Or as a result?

**6:10** · You know, in my mind there's no question that when the technology community decides to make huge investments in the most transformational technology of our time, that there's going to be rapid progress. And also that that technology is not going to be controlled by a small group of people. Because that's just not the way that the industry works. You know, we we do our best work.

**6:36** · We have the most impact with our work when we're able to each think about it in our own way and apply it in our own way. So, you know, I love the closed AI APIs, whether from Anthropic or other people. I think they're amazing. You know, really really impressed with the work that those labs are doing. But they're not the only labs in the world. There's lots of labs around the world and lots of people have a good idea.

**7:01** · It's not the case that there's only a few labs that have the monopoly on all good ideas. That's just not true. That's not how humanity operates. There's there's a lot of bright people on this planet. And you know, the community of course cares deeply about this technology. It's obviously so transformational. It has such profound impacts on so many things that that of course many people want to be involved in that.

**7:25** · And so I think over time we're going to see that community-oriented approaches to developing and deploying AI are going to continue to strengthen and be widely adopted because that's really the history of how we built things as a as a human species.

### Is the US falling behind China?

**7:42** · Do you think that is globally true as well? So, you know, in particular with respect to China, this perception that yes, a lot of people have great ideas around the world. However, a lot of progress from Chinese models were directly inspired or perhaps generated through distillation from the closed-source models.

**8:07** · Is that just kind of like race bait or from the perspective of a leading AI researcher, you're very impressed by the novel ideas that come out of China as well?

**8:21** · You know, perhaps unusually, I actually did work at a Chinese company for about 2 and 1/2 years. I worked at Baidu. I worked in the Silicon Valley AI lab along with Andrew Ng and as well as Dario Amodei. And we all worked for a Chinese company and saw how smart, hard-working, creative, inventive our colleagues were at the rest of Baidu. And you know, that experience has has stuck with me.

**8:50** · Um I think it's absolutely false to say that you know, the achievements of some other country are all being created by sort of you know, copycat mentality. It's just not It's just not true.

**9:08** · Now, do we all learn from each other in the technology community? Of course, you know, of course of course we learn from each other. But you know, I would say you know, it's been a really good thing for the world that the Chinese AI community has been so open with what they've been building. I think it's enabled a tremendous number of companies to build things that they couldn't have done without um community.

**9:35** · And I think it's also spurred, um technological progress throughout the AI uh ecosystem. So, you know, I'm really grateful for um the contributions that um our um colleagues in China have made over the years. And um you know, I I would love to encourage a uh spirit of openness amongst AI labs around the world outside of China as well. You know, I was really excited when uh OpenAI released the GPT OSS models um uh a while back and then of course Google's been doing great work with Gemma.

**10:08** · Absolutely thrilling to see that. Um and you know, we're pushing NeMo Tron along here at NVIDIA as well. Um so, I I think there's a there's a chance for um uh the rest of the world to catch up to China uh in the sense that um you know, we can understand the benefits of working together uh as a community to build technologies for AI uh in a way that I think China has frankly been leading.

### Why companies actually choose open models

**10:30** · Right. What is the case for a customer to be using open-source models uh these days? What is the fundamental advantage?

**10:43** · Every company is built around a secret.

**10:46** · Uh this is a secret that has to do with not just their intellectual property, but also their platform, uh which has to do with how do they interact with problems and customers? Um how do they think about solutions uh to what what their customers need? And it is always the case that the value of AI is greater when it can be more tightly connected with those secrets. Because, you know, AI depends on data critically. So, the more valuable the data that goes in, the more valuable the solution becomes.

**11:17** · Now, um every company when it's thinking about how to deploy AI has to think through, what are the implications for the core secrets of our company? And um there's a lot of circumstances where um due to trade secrets or or you know trying to think of think through the business model or or even regulatory requirements that you know there's data that you really have to treat very carefully by law. Um and it is much better to do that when you are able to think that through and implement it yourself.

**11:48** · Um thinking about the integration of AI, the way that AI interacts with um customers, um the guardrails that are put in place, you know, every company um has a specific understanding of its customers and and therefore what what the customer needs. And um the amazing thing about open technologies for AI is that they allow custom uh customization, right? So companies can think this through, they can build things that that really matter for them.

**12:16** · And you know, I started out this conversation talking about the internet and about how the internet, the deployment of the internet has been done in very different ways for very different industries. Um and there's a lot of desire to do that um uh as we see AI change the way that we work and play throughout the entire economy. Um this is really spurring a lot of demand for open technologies for AI.

### A "crazy" 2008 bet: machine learning on GPUs

**12:39** · Right.

**12:39** · I'd love to go into a bit of a deep dive into Nematron, but before we do that, maybe a few minutes on your story, your background. What was your path to where you are today um including the the Baidu detour?

**12:57** · So um I started work at uh Nvidia in 2008. Uh at the time I was a graduate student trying to figure out um parallel computing for artificial intelligence and I thought um Nvidia had a chance of changing the way computers work AI.

**13:13** · Which was a lonely presumably a lonely quest, right, in 2008?

**13:17** · Oh, it was it was very chaotic. Back then people thought I was crazy and you know, I remember going to ICML in 2008.

**13:23** · I published my first paper training models on the GPU and people asked me why I was there. People said this is not a good paper for ICML. We're We just do fancy math here. And I was like, well, but I think computing actually matters a lot for AI. If we could train bigger models that had more capacity to learn, we could probably solve more problems.

**13:43** · And they kind of nodded their heads and they were like, well, I'm not really sure why you're here.

**13:48** · Isn't a GPU a thing for gaming as well, presumably?

**13:52** · Yeah, there's there's also that, right?

**13:53** · Which we we continued to run into that that idea. Actually, a GPU is whatever Nvidia says it is. You know, we make them. So, a GPU is is a is a thing that we make in order to accelerate the world's most important computations, which in 1995 was graphics and you know, for a long time now it's been AI. So, anyway, I started at Nvidia.

**14:16** · I was in the research group doing strange things about trying to make compilers, libraries for AI on the GPU. That led to the creation of first Copperhead, which was a it was a Python embedded language that compiled to the GPU, which I think foreshadowed a lot of things in TensorFlow and and PyTorch. And then then that led to the creation of cuDNN, which was Nvidia's first product for deep learning on the GPU.

**14:50** · And I really enjoyed working on that, but I was always wanting to see more first-hand about the applications of AI.

**15:02** · And at Nvidia, I was mostly working on you know, libraries and compilers for AI. So, I thought well, you know, when Andrew Ng asked me to go build the Silicon Valley AI lab with him at Baidu, I thought, oh, this is a great opportunity because even back then Baidu was very advanced in its application of AI to its core business.

**15:22** · And so, um uh so that was a a fantastic opportunity for me. The Baidu Silicon Valley AI Lab was an amazing place, um full of brilliant people that were working really hard.

### Working with Andrew Ng and Dario Amodei at Baidu

**15:33** · What was it like working with uh a young Dario? Uh did was there like any signs that he could become uh you know who who he has become?

**15:42** · Dario um was brilliant from the beginning. I remember um I interviewed him uh I was on the panel um and um at the time he uh had been working in bioinformatics, so he he hadn't been working on deep learning or or the things that we call AI these days. Um but it was very clear that he learned extremely quickly, and also that he thought extremely deeply. Um I think, you know, uh the thing I admire most about Dario uh is the strength of his conviction.

**16:11** · Um you know, I've been working in this field uh for a long time, and I've believed also that AI is going to transform the world, but I don't think that I believed uh in it as completely as Dario did. And perhaps that was because, you know, my academic training during my PhD was full of a lot of caution. Uh I don't know if you remember, but AI was old and bad in 2005.

**16:38** · It will never work.

**16:40** · that people did with computers, they started doing it in 1945, right? Um and and so there'd been so many grandiose promises that failed to deliver over the years, and so I came to AI with a lot of caution. In fact, back then we used to call it machine learning, which was basically a dodge, like we just didn't want people to know that we were we were working on AI because then they would be like, "Oh, we've heard about that. It never works, right?"

**17:03** · \[laughter\] So, um I came to AI with a little bit of this like uh you know, academic caution, like, "Oh, we should be you know, we should hedge a little bit. Like, I don't know if now's the time." Like, \[snorts\] um and and Dario, you know, he his uh strength of conviction and his understanding of the moment of how um the technology was developing, this time it was actually going to work, and then the implications of that on um you know, how the technology should be developed, um uh what kind of institutions uh to build.

**17:33** · I think he's done uh a spectacular job. And so, um yeah, working with him uh it was always always a uh a fun experience.

### Coming back to NVIDIA: DLSS and the birth of Megatron

**17:41** · So, then you went back to Nvidia, and walk us through the journey.

**17:45** · Yeah, so uh 10 years ago actually in 2016, uh Jensen called me up and said, "Hey, uh would you like to come back and build an applied research lab?" And I thought that would be a fantastic uh opportunity. I you know, I've always loved Nvidia. I've loved um the way the company works, uh the convictions the company holds. You know, um Nvidia's a very unique company. It follows through over long time periods. You know, uh and I've seen that with CUDA, I've seen it with our deep learning technologies, I've seen it with our ray tracing graphics technologies, our AI for graphics.

**18:16** · You know, over and over again Nvidia is not afraid to put in 5 or 10 years worth of research in order to change the world. You know, and um working at a company that has that strength of conviction and the ability to follow through is kind of an ideal thing for me. Um I just really I just really love the support that the company gives uh gives its researchers um to invent the future.

**18:39** · And so, um I thought I'd come back. Um uh the first project that uh that I worked on um actually became DLSS, uh which uh some of your um audience may know about, but DLSS is our real-time uh AI for graphics, and it makes a small GPU run like a big GPU. It's about 10 times more efficient because rather than computing uh the color of every pixel for every frame, we use AI to infer the color.

**19:07** · Uh and uh you know, these days 23 out of every 24 pixels uh is being generated by our AI model when you're using DLSS to play games and gamers love it. It's become the standard way of playing games because it's just so much more responsive and it's more beautiful. Our AI we train it offline on huge data sets and it's able to render graphics in real time more beautifully than traditional methods do.

**19:35** · We recently actually announced DLSS 5 which is a fully generative version of DLSS and I am so excited about it. It represents combination of 10 years worth of research on how to make real-time graphics much more beautiful.

**19:51** · And so so that's part of part of the journey here for me was real-time AI for graphics. But then at the same time we also started a language modeling project and this is back in 2017 you know before transformers were big and before language modeling started taking over the world but you know I just had this intuition maybe built on you know some of the things that that I had seen while working at Baidu.

**20:21** · I just had this intuition that you know working with text and understanding text was going to lead to better reasoning which was going to lead to better application of AI in all sorts of domains. And so we started this project called Megatron. Megatron stands for the biggest baddest transformer. That's why we named it that. And it was really a systems project to show the world how to train the largest transformer models on Nvidia's hardware.

**20:46** · Back at the time some of your audience may or may not remember this but there was there were being claims made that the only way to train big transformer models was on the TPU because after all the transformer had been invented at Google. And so you know we looked we looked at you know we loved the transformer paper. We thought wow this has amazing potential. We tried it out on our own language modeling tasks, and it worked so much better than the RNNs that we had been using before.

**21:13** · And also, we saw immediately that there was an enormous systems opportunity to co-optimize the GPU, the networking, all of the compilers and software that would enable people to scale uh Transformer-based language models uh really dramatically. And we we thought, you know, this is this is something that that um could really have an impact.

**21:30** · So, we started the Megatron project, um which then led to I think uh basically helping the whole industry figure out how to train um extremely large uh LLMs, um and also led to the foundations of today's NeMoTron project, um where, you know, NVIDIA trains uh its own LLMs um uh for its own purposes. So, that's kind of the the history.

**21:54** · Great journey. Okay, so let's go into all things uh NeMoTron. And before we get into the specifics, there's the obvious question uh that I'm sure you've been asked uh many times, uh which is uh what why does NVIDIA care in the first place to be building model and investing very significant efforts into creating its own family of front of frontier models?

### The real reason NVIDIA builds its own models

**22:19** · You know, NeMoTron has two jobs. The first job is to help us understand how to build the systems of the future. NVIDIA is an accelerated computing company, and that means thinking through the world's most important computational challenges from first principles, and designing systems, which includes a lot of software, uh in order to make it possible for people to invent and deploy things that never could have been done with standard computing.

**22:45** · But in order to do that, NVIDIA has to deeply understand everything about how AI works. That's how we co-design all of the systems and software um uh for our main product line. So, the first job of NeMoTron is to make sure that NVIDIA continues to exist so that we can continue delivering meaningful acceleration in an era where Moore's law has died. Uh and the the acceleration that we get these days comes through specialization. But again, specialization comes through understanding.

**23:14** · So that's Numatron's first job is to help Nvidia understand how to build its core products.

**23:20** · Nvidia's second or Numatron's second job is to support the ecosystem. Uh one of the most valuable things that Nvidia has built over the years is um all of the people around the world who build and deploy amazing AI um using Nvidia's uh technologies. And uh we think that it's necessary for uh open technology for AI to continue to exist uh from Nvidia to help uh support that. Numatron's not trying to be the only open technology for AI.

**23:49** · We love all technology for AI for the very straightforward reason that whenever AI uh is further developed and further deployed, it's an opportunity for our business. So So this is this is um you know, we're we're very explicitly trying to develop our ecosystem because that's good business for us. Um but we're not trying to be the only provider of technologies for this ecosystem. We love seeing um other companies contribute as well.

**24:17** · Um the the most important thing for Numatron's second job is just making sure that it continues to be possible for companies of all shapes and sizes to build and deploy their own AI.

### Is Moore's Law really dead?

**24:28** · By the way, Moore's law is dead? Is that Is that a Is that official?

**24:31** · It's been dead for years.

**24:33** · It's been dead for years? Like why why is that?

**24:35** · Well, you just look at the the progress uh in semiconductor manufacturing. You know, the the original statement of Moore's law was economic, right? It was about we can afford to put twice as many transistors on the same chip in every whatever 24 months, whatever the the time period is. And um these days that is absolutely not the case. It hasn't been for probably five or 10 years, right? Now, we are still scaling our systems, right? Um through a number of ways. One is just applying a lot more silicon to it, right?

**25:04** · Uh we are also getting transistors are continuing to get smaller and and more efficient, although at a a slower pace, but they're also getting quite a bit more expensive at the same time.

**25:16** · Um uh so, the uh you know, in an era where where Moore's law was alive, the best way to make the system of the future was to take the system of the present and then just shrink it. And and maybe double it at the same time, right? But in an era where where we've been living for a while now, where you don't get economic benefits from taking your existing design and shrinking it, uh you really have to be more clever about how you use every part of the system.

**25:43** · Uh that that's uh you know, an era where accelerated computing is is much more valuable than ever because the the work of thinking through the prob- problem from first principles and co-designing absolutely everything uh from transistors to algorithms and applications uh in order to reduce waste and and deliver meaningful acceleration, that's more valuable than ever.

**26:07** · Fantastic. To playback what you were saying uh I mentioned earlier, it makes good business sense for Nvidia to be in the model business because one, it helps uh design better chips, and two, uh whatever is good for AI is ultimately good for Nvidia, which makes a lot of sense. That Nemotron effort is reasonably recent, right? Started in 2023, I believe, maybe. Walk us quickly through the key releases. I believe in 2023, that was Nemotron 3 8B as a key release, or am I missing a step?

**26:41** · Yes.

**26:41** · Yes. Yes. So, you know, the the you know, the the numbering is somewhat lost to time. It I almost feel like we're in the Lord of the Rings and it's like, you know, there's like some ancient like relics that we're digging up out of an old mine. Um, you know, this is a long time ago.

**26:57** · You know, the original what what uh we originally called NeMo Tron 1 was actually a project that we did with Microsoft. Um, we jointly trained a 530 billion parameter model. Um, I believe that was released in 2021. And so this is GPT-3 era. Um, and that's what um at the time we called it Megatron Turing NLG. Uh Turing was uh what Microsoft was calling their their language model efforts um at the time.

**27:26** · But uh uh that uh in retrospect we called NeMo Tron 1. Uh then along the way we built a few more.

**27:33** · Uh we got up to NeMo Tron 3. Um, and then uh LLaMA came along uh and we were really excited about that. We were very um happy that Meta was supporting the open uh AI technology space. Um, and so we we started um you know, taking our language model technology and adding it to LLaMA models which then re- resulted in LLaMA NeMo Tron 1.

**27:58** · Um, and you know, that was the first uh reasoning model uh built on LLaMA. Uh we were really proud of that.

**28:05** · And that was 2025?

**28:08** · Uh might have been 24. Uh I I believe I can't remember. Uh somewhere around there.

**28:14** · Um, and then uh uh yes, and then we we continued uh to to develop that. Um, uh and uh you know, last we we so we the numbers kind of started over again. We released a NeMo Tron 2. Um, I believe it was last year. Um, and then we quickly followed that up with NeMo Tron 3 because um uh we we needed to put MoE support in.

**28:39** · NeMo Tron 2 didn't have MoE support and that made it kind of uncompetitive against uh other models like GPT OSS 20B was just like so fast because of MOE and so we were like okay we've got to we've got to put put the MOE in so that became NeMo Tron 3.

**28:56** · Um now we're in a a slightly difficult state because you know we're working on NeMo Tron 4, right? But we already released a NeMo Tron 4 which was um in 2024 we released a 340B uh model called NeMo Tron 4. Um and so I'm not exactly sure how we're going to um solve this marketing problem. I didn't create this marketing problem. Uh so uh I'll I'll I'll do my best to to make it clear that NeMo Tron 4 of of of whatever the next whenever we release that is different from the the 2024 NeMo Tron 4. Um but uh in any case we've been working on this for a long time.

**29:29** · I think um more important to us than any particular generation is just the sustained commitment uh that NVIDIA has to developing these models. We've been doing it for a while. I think our models have gotten dramatically more useful in the past year um which is a reflection of two things primarily. One is that uh the whole company has come together so there are many different teams around NVIDIA that now understand how important this is to NVIDIA's future. And so there's dramatically more people and better ideas that are going into NeMo Tron.

**30:01** · Um and then uh number two along with that we've been able to scale the um compute resources that go into it. Um obviously it's um very important to have good computing infrastructure to build AI. We've um recently increased our investment substantially because uh we believe that that this is really really key to our company's future.

**30:21** · Oh fascinating.

**30:22** · But I just to continue the thought I think it's really important that everybody knows that we've been doing this for a long time. We are increasing our investments substantially and NVIDIA is a company that follows through. You know we followed through over 10 plus years with CUDA and we're doing that with NeMo Tron now.

**30:37** · That's very helpful because uh I think the the the broader world is is just starting to catch up to the fact that there is a very substantial open source frontier AI research effort that has been happening. So, it's very interesting to to hear that you know, there's been this progression and now this is family of models that we're going to talk about in a second. Another important moment seems to be the creation just in March 3 months ago of the NeMoTron coalition.

**31:05** · Do you want to explain briefly what that is?

**31:11** · So, NeMoTron exists to help support the ecosystem and we were thinking, well, this is a different kind of AI project than other projects around the industry, right? Because we're not actually trying to dominate in any way. We're just trying to support.

**31:29** · We don't We're not trying to control the way that AI is being integrated into all these companies. We're just trying to make sure there's good AI. But we thought, well, maybe if we worked with people while we develop it, then it's going to be more useful for them. It'll be easier to integrate because we will consider what they need from the beginning. And you know, NeMoTron has always been collaborative. I was telling you that, you know, long long time ago our first big model that we trained we we did with Microsoft, right?

**31:59** · It was a joint effort where Nvidia and Microsoft researchers worked side by side to build that. And that that ended up, I think, helping both Nvidia and Microsoft. I think we both learned a lot from that experience.

**32:12** · And So, because NeMoTron is not trying to compete with other companies, but rather support, because we're going to be putting it out there openly anyway, why not collaborate before the thing is built rather than NeMoTron being a project that Nvidia does all on its own and then posts on the internet and says, "Hey, why don't you try this? We think it might be good."

**32:33** · Why don't we make sure that it's good for the partners that that are interested by working with them before Neumitron is even created and incorporating you know any sort of feedback evaluations environments benchmarks or any other kinds of technology that other people want to bring.

**32:52** · It turns out that the entire ecosystem there's a lot of companies that really want open models to succeed and so they have a self interest they have their own vested self interest and make sure that open technologies are excellent and so why not work with them and and let them contribute however they'd like to making Neumitron better. So that's the the idea of the Neumitron coalition. It is not an exclusive coalition. We're not trying to be the only model out there.

**33:20** · All the companies that we work with are free to to continue doing the work however makes sense to them and yet you know these companies want to work with us because they want to make sure that open technologies for AI keep developing quickly and that they have a chance to influence how that happens.

### The Nemotron family: Nano, Super, Ultra

**33:37** · Great. What's the current state of the Neumitron family? You got Nano, you got super, you got ultra. What do those models do and what are the use cases for them?

**33:49** · So Nano is a 30 billion total 3 billion active parameter model. Super is 120 and 12 and ultra is 550 and 55.

**34:00** · They're designed really to fit you know it's kind of small medium and large deployment scenarios uh you know Nano can be really capable for things that you know don't require nearly as much knowledge or reasoning but obviously for the for the most capable model you go for ultra. Super in a lot of ways is our most popular model because it represents kind of a great balance between cost and and intelligence.

**34:29** · So we we kind of like um having this small, medium, and large um approach to building a family just because our customers um seem to respond to that um pretty well. But, um you know, uh the most important thing from Nvidia's point of view that people are doing with uh uh with LLMs is agents, right? Is um building agentic workflows, having it having an agent working on your behalf solving problems for you night and day.

**34:59** · Um such an exciting way of approaching the problems that we have to solve. Um and um it's our dream to make NeMo-Tron amazing for that purpose. That's that's our goal.

### Built for agents: why NVIDIA bets on speed

**35:09** · To double click on this uh at a high level, NeMo-Tron family is focused on agentic reasoning uh with a particular focus on making it efficient. Is that Is that the right headline?

**35:19** · That's right. Yeah, um NeMo-Tron has always been um uh speed-first approach to building models because Nvidia is an accelerated computing company. As I was saying, we're trying to think through, "What is the problem here computationally from first principles?"

**35:34** · And um you know, NeMo-Tron uh 3 family has a lot of things in it that are uh we're really proud of. For example, um NeMo-Tron Ultra and Super uh were pre-trained using 4-bit arithmetic. We pre-trained those in NVF P4.

**35:50** · Um which, you know, uh is a a non-trivial thing to do to invent the algorithm so that your model can converge to an excellent result using such coarse arithmetic. Uh required a lot of invention. Really proud of that.

### How you train a 550B model in 4 bits

**36:02** · Do you want to explain maybe for for people what 4-bit is versus 16-bit, for example?

**36:08** · You know, actually there was a fantastic post I saw on Hacker News yesterday where somebody let you um upload a picture and then it would basically posterize it, basically reduce the colors to fit different um uh number formats including NVF P4 and MXFP8 and some of the other formats that are out there. And so, you could kind of swipe around and look what it does to the colors of a picture. Um and you know, it's it's really quite dramatic. Four bits is not a lot of bits, right? That's only 16 values. Um now of course these are all um what are called uh block scaled formats.

**36:37** · So um groups of numbers also come with uh an eight-bit um scaling factor. And the the specifics of this can get rather complicated. So it maybe it they're not quite as important. But the the reason why we want to do this is because first of all we have dramatically higher um throughput for these formats in our GPUs, um specifically on uh Blackwell Ultra.

**37:04** · Um and uh uh secondly, we know that it's going to save an enormous amount of energy. Um one one way to think about uh the computational problem of AI is that we are going to be running at the limit.

**37:18** · Whatever the limit is, it could be uh an economic limit, like we only have so many billion dollars to to buy servers with. It could be a power limit. We only have so many gigawatts that we can afford to to train a model with.

**37:32** · Whatever the limit is, um uh we're going to be running at that limit. The every organization is is because why? Because the value of intelligence is so high. You know, that the people are going to they're going to invest because they they know that they're going to get return. Um uh the the value of intelligence is is enormous.

**37:50** · Uh so if you if you accept as the truth that we're going to be running at the limit, then what that means is that the way to get more intelligence is to be more efficient. We can't get more intelligence by applying more force if we're already at the limit. We have to be more thoughtful about how we use what we have. And you know, four-bit number formats are dramatically cheaper to move around. They take up less space in memory.

**38:14** · Um they take up less uh picojoules when you move them from the memory um in from or even on the chip uh around the chip. Much less energy when you compute on them and so that's really driving, you know, the investment in four-bit formats. And I think these days four-bit formats for deployment are very well established.

**38:38** · It's it's pretty pretty straightforward these days to make a a good quantized four-bit checkpoint that you can deploy and that gets you a lot of inference cost and speed advantages.

**38:51** · But using four-bit formats for pre-training that's quite a bit more challenging because you have this numeric solver that's, you know, optimizing the weights and you know, it can be quite sensitive. So if you if you don't treat the numbers right, your model can diverge and instead of actually getting a model done through pre-training, you end up with, you know, basically just that run diverged which is, you know, always always scary.

**39:19** · So it took a lot of invention for us to be able to pre-train NeMo-Megatron in four-bit. We're really proud of that.

### Hybrid Mamba-Transformer, explained simply

**39:25** · Okay, great. All right, so as we get into slightly more technical things, the architecture of NeMo-Megatron is hybrid. Is that right? So it's a combination of transformer and Mamba state space which is slightly more exotic form of architecture. Walk us through that.

**39:48** · Yeah, you know, we published a paper in 2024 that showed that you actually get a smarter model by combining state space models with transformers.

**39:59** · And we we actually did a sweep you know, how much of the model should be full attention and how much of it should be a state space model in order to get the lowest perplexity, basically the best the best language model that you could get. And we found that you actually want it to be mostly a state space model with a little bit of attention.

**40:17** · And so kind of the intuition behind that is that um the state-space models seem to be better at um kind of this intuitive in- um intuitive kind of impressionistic understanding of a sequence um uh because they're um you know, they're kind of summarizing the entire sequence into a constant space. That's how they work, right?

**40:37** · So instead of having the ability to look at the entire sequence randomly, uh they summarize everything at every step into a constant um cache or little scratchpad that they're they're working on.

**40:50** · And um that constraint seems to actually make them smarter at some tasks that involve like global understanding. Um on the other hand, the advantage of full attention is that it can pick out very specific uh bits of information and look at those exactly. It doesn't lose anything. There's no lossy compression going on. You can actually see the whole thing.

**41:09** · Um and so we found that um uh you know, using both of these together was actually better than using either one on their own. Um and that is independent of the speed benefit. That is just the model is smarter. And you know, since we published that, I think a lot of other um uh labs have also found this to be true.

**41:31** · Um you know, a lot of uh uh models these days are being built with hybrid SSM approaches. For example, QNN has done that. Um uh Kimmy uh is using what they call Kimmy linear attention these days. So um it's become uh I think quite widely adopted to use some sort of state-space model in conjunction with um full attention for um uh for the the base architecture.

**41:53** · Um now it also has some speed benefits because um the uh amount of memory that you need to hold uh that state-space uh cache is actually constant with respect to your sequence length, um which then means that, um, generally you can fit much higher batches on the GPU when you're training and doing inference, um, because the memory, um, requirement is lower.

**42:21** · And it keeps the GPU, uh, fuller and busier, um, and therefore, um, you know, provide some some pretty important significant, uh, some some pretty important efficiency benefits as well.

### Mixture of experts — and why NVIDIA built NVL72 around it

**42:31** · So, the models are also based on an MoE mixture of expert architecture. We'll go through that and maybe remind people what MoE is in the first place.

**42:42** · So, mixture of experts is a form of sparsity. Um, the idea is, wow, you want to train a model on the entire internet.

**42:49** · You want it to remember absolutely everything about the history of everything. But, when you're answering a particular question, does it seem reasonable that it needs to actually think about the entire universe in order to answer that question?

**43:02** · Actually, no. It seems like it's quite sparse, right? It seems like, um, we're we're we're using a language model to explore a very tiny space of ideas in order to answer a question or solve a problem. We want the model to be able to draw from the entire universe. We want to train it so that it understands everything that it possibly can. But, when it's actually running, it doesn't really need to see all of that information.

**43:24** · There's been a variety of approaches to sparsity that try to take advantage of this property, but mixture of experts has been the most successful. And the way that it works is that the neural network has what's called a router that is learned that, um, is going to decide to send activations to a subset of the experts, uh, for every token that's flowing through every layer of the model.

**43:46** · It's going to be making choices about, um, which fraction of the model is going to actually get to interact with this token as we try to understand it, build up representations of the problem, and then generate the next token that we're going to output.

**43:59** · So, it's a little bit like if I have a company with 550 employees, but, uh, 55 of them are in engineering. I want the 55 employees who are specialists to come to my meeting about engineering and not the rest of the company.

**44:15** · That's right. Yeah, or you can think about it as a library. Like if you go into a library to do research, you don't read all of the books in the library.

**44:23** · Like your first job is to figure out which books do you need to look at in order to find the answer to your question. And so um so that's kind of the the idea behind MOEs. Now, MOEs have fascinating implications for the systems that we build. So with Blackwell, for example, Nvidia went all in on MOEs.

**44:41** · That's why we built NVL72, which allows up to 72 of our GPUs to read and write each other's memory uh at very high speeds, very low latency. And why is that important? It's because as you put a token through the stack of layers, at every layer, you have a router that's routing that token somewhere else. Why don't you partition your experts so that, you know, the experts are not sitting every expert on every GPU, but you have a subset of the experts assigned to each GPU, and then you're routing the tokens between the GPUs very dynamically as you push uh the token through the network.

**45:13** · Now, um this is impossible to predict in advance where the tokens need to go because it's very specific to that particular token for that particular model.

**45:24** · And so that's why we built NVL72, and that's why um Blackwell is so amazing for inference for, you know, today's AI models uh is because we thought deeply about um mixture of experts when we were building it. And this is speaking to NeMo Tron's first job. You know, if if we hadn't been working on understanding AI, we wouldn't have been able to build Blackwell properly. And that, you know, has has translated directly into um you know, increased deployment um of Blackwell, which, you know, we're we're we're very excited about.

**45:55** · Is what you just described uh called latent MOE, or is that a different concept?

**46:00** · Latent MOE is a specific uh innovation that we have in NeMo Triton 3 family and what it does is actually reduces the amount of communication that has to be sent through NVLink during MoE computations by basically down projecting it. So, you know, every token is produces a vector and the idea is like we're going to take that vector and learn a way to compress it and then send that compressed thing through the network and then we're going to uncompress it at the other end.

**46:25** · And as a result, we save on network bandwidth and we also get four times the number of experts for the same inference cost. So, you could think about it as like, you know, our library of books got four times bigger and we get to, you know, read four times more books at the same inference cost because of because of this particular innovation.

**46:48** · Is MoE in general becoming the default architecture for frontier AI?

**46:54** · Yeah, I believe MoEs have been the default in frontier AI for a long time. They're just a really good combination of inference cost and intelligence.

**47:03** · Great. Great.

**47:04** · But they have drawbacks as well. You know, they they take a lot more memory. If you have a a very small amount of memory, a dense model is going to be smarter. And they also they tend to work best either if you're running a batch size one, so you're running basically a single job or you're running a huge data center with like infinite queries coming in. In the middle, they can be a little bit tricky.

### Why a 1-million-token context window matters

**47:26** · Another important characteristic of NeMo Triton 3 Ultra is a 1 million token context, the the long context window. How important is that in the overall mix and what does it enable the model to do?

**47:40** · The longer the context length, the more challenging problems we can solve with a language model. That allows us to do things like append all sorts of information to a query, which could be a code base, it could be instructions.

**47:56** · You you uh in in the long term, I'm hoping that I have my own personal LLM that's able to read all of my emails, you know, and help me answer questions about that. You know, the more information that we can attach to a particular query, um, the the more useful the model can be. Um, now, uh, it can get more and more expensive, right, to reason over large amounts of of input data. And, um, and so that's one of the the reasons why there's usually a limit on how big the context length can be.

**48:26** · But with NeMoTron 3, we we tried to push it as far as we could go. Uh, we think a million tokens is a lot of tokens, um, and you can do a lot of things with that.

**48:36** · Is the model particularly helpful in, um, sort of multi-step, uh, agentic workflows? And there's this whole separate discussion around the context compaction to make sure that the model doesn't get lost in too many tokens. So, like, how do you how do you all think about this?

**48:51** · 100%. I mean, um, uh you know, compaction is that's a thing if you're using an agentic workflow you deal with all the time. Um, and compaction tends to work pretty well, you know, because language models, um, are pretty good at at identifying the most relevant things and summarizing. And you're basically trying to summarize your context when you compact it. Um, so, uh, compaction uh, is is not a bad approach. I think having models that can just natively, uh, reason about larger amounts of data is just inherently more useful.

**49:21** · So, of course, we want to push the the boundary on that as well.

### Multi-token prediction: how the model predicts 5 tokens at once

**49:26** · Right. Can you talk about the multi-token prediction, uh, which is also very interesting?

**49:31** · If you're running at a low batch size, um, which is when you are trying to get the most interactivity if you're in a data center, so you want you want the model to respond as quickly as possible, and it's okay for it to be more expensive, your token your cost per token may might be higher, but you want the result as quickly as possible. Or if you're running, um, locally, um, so you might be running, a batch size one just because you're the only person using it.

**49:57** · It turns out that, uh, the GPU has extra execution capabilities that are just lying there unused. The bulk of the work when you're running in these scenarios is actually fetching the weights from memory. And then you push the token past those weights, and then you fetch more more, uh, weights from memory. But it turns out if you if you push two tokens or even five tokens through those same, um, weights, it would cost basically the same amount of time. Because the the expensive thing is not doing the math to push the token through the weights.

**50:27** · The expensive thing is just reading all of those weights from memory. All those parameters, they have to come in.

**50:34** · And so the idea with multi-token prediction is to take advantage of this by having the model predict multiple tokens at once. Let's say that the model predicts five tokens. We know the first token is correct. The next four tokens may or may not be correct. So then what we do is on the next pass, we take those four tokens and we stick them into the model, uh, and then, uh, run it through. And at the end, we check, you know, the model then predicts another set of tokens, right?

**51:00** · Then we check, were the extra tokens we predicted last time correct? If so, then we just accept them, uh, and then we get like a 4x speed up.

**51:10** · Um, and if they were incorrect, then we only accept the ones that were correct, and then, um, you know, uh, proceed from there. So the benefit of this is it it doesn't degrade accuracy at all because you're using the model to double-check, right? So all the speculation is going to get checked, uh, during the next token that you you, uh, run through the model.

**51:33** · So it doesn't degrade your accuracy at all to turn on multi-token prediction, but it can give you a speed up and it's probabilistic depending on the acceptance rate of your, um, a predictor. You know, so if your predictor's more accurate, the acceptance rate goes higher, you get a higher speed Um so with, you know, um uh uh, with our recent NeMo Triton models, you know, we're pretty proud of our acceptance rates, but we're always trying to make them better, you know, always trying to improve that acceptance rate. This is a really good example of accelerated computing. You know, with multi-token prediction, the speed that you get is a function of the accuracy of your model.

**52:07** · The more accurate your model is, the faster the inference is, the cheaper the inference is, the more accurate it is.

**52:13** · That's not usually how it works, but in this case, that's how it works. And what that implies is that, you know, if we're trying as Nvidia as a company to provide meaningful acceleration to the world's most important computational workloads, this has to be an important part of how we uh think about it, you know? If there's a 3x cost reduction or speed

**52:31** · improvement uh for inference, which is the most important computational workload of 2026, um if that's on the table and it depends on the accuracy of the multi-token prediction network, then that's something that Nvidia needs to understand very deeply because it's going to affect uh our business directly.

### Multi-teacher distillation: teaching one model from many

**52:47** · Fascinating. And then to to to continue on the on on the tour, multi-teacher distillation. We talked about distillation a little bit up front. Uh what does that mean in the context of uh NeMo Triton 3?

**52:58** · So with NeMo Triton 3 Ultra, we did post-training using something called multi-domain on-policy distillation.

**53:06** · And what that uh entails is that, you know, we have many different aspects of the model we want to improve. Um for example, science understanding is different from math theorem proving, which is different from coding, which is different from agent harness uh interactions, right? There's There's um with NeMo Triton 3, I think we had about um 10 10 or 15 of these teachers. And um so the idea is that you take these teacher models and you push them as far as you can go on some specific domain.

**53:37** · So you just don't worry about making good at everything, just make it really, really smart at this one domain. Then you have a collection of these models and you want to create one model that learns uh to be good at everything.

**53:49** · And we do that using a specific reinforcement learning technique that a lot of labs these days use called um uh MoPD. Um and the the good thing about this is that because the teachers are supervising, uh they can give really dense uh rewards to the the student model. Basically, every token is getting supervised, and so the student can learn really quickly um and then become uh you know, almost as good as all of the teachers at all of the things. Um so, uh one benefit of this is that it really helps the team work together better.

**54:21** · Um you know, if if if um you don't have a technique like this and you have, let's say, 500 people working to try to make a model better, and one team's like, "Well, I'm trying to make it better at this thing." And then another team's like, "I'm trying to make it better at that thing." There can be a tug of war where it's like, "Well, who wins?" You know, what And And if you have to make a choice like, "Oh, I'm going to make the I'm going to choose to prioritize this one over that one." Then you make the other team feel like their work doesn't matter. You know, it's just really hard.

**54:48** · It's one of the challenges of of building AI in in 2026 you have to figure out how to get the people to work together, even though you're only building one thing at the end of the day. And so, this particular technology um has been really instrumental in helping more people work together to make NeMo Tron stronger.

**55:05** · Uh fascinating. So, it's as just as a much a technology question as a human organization question.

**55:10** · Exactly.

**55:10** · \[laughter\] Okay. Fantastic. Let's put a pin in this and and and get back to to this in a second because it's a fascinating topic. In terms of uh the post-training uh that that you uh just alluded to, one of the uh exciting things that uh you all did uh in the context of NeMo Tron is also to publish the data, the training data.

**55:34** · Does Does include uh per industry data for specific reinforcement learning tasks?

**55:41** · Yes.

**55:42** · That's the beauty of a conversation like like like this today where where you guys can actually talk about those those things. So, where does the get the one get the data from for uh post-training reinforcement learning focused um efforts, right? So, obviously one of the key questions in in the world today is that LLMs or or or or AI systems have become great at coding and great at math. Like the next big question is can they get become great at uh law and consulting and then uh you know, all sorts of different domains.

**56:12** · And part of the the black box of the closed models is like how people go about doing all all all of this, where do they get the data from? To the extent that you can uh talk about all of this, I'd be very curious about how you guys have have gone about it.

**56:25** · It's not an easy question to answer because it is quite complex, but I would say um we rely on uh a number of things.

**56:32** · One is that we do purchase data from uh companies that um uh that you know, are are building data sets that you can purchase. Um and to the extent that you know, we have the rights to redistribute uh or to to to open up that data, we do as part of um our our uh NeMoTron data effort. Um you know, with with NeMoTron, we are trying to be maximally open with the data that we release because our goal is to support the ecosystem, right?

**57:00** · Our goal is is not to be the only model out there and we love it when we hear of other models around the industry that are using our data sets um to to make their AI stronger because that means we're succeeding at our job to keep the ecosystem thriving and growing.

**57:17** · Um Now, uh we also are big believers in synthetic data generation. Um we use an enormous amount of compute um uh running language models on our own systems to create synthetic data that then helps our models be better at solving problems in specific domains. And we release a lot of that data as well.

**57:40** · Now, it's of course not very straightforward to do this. Like, you know, AI is always garbage in, garbage out. So, you have to work really hard to make sure that any synthetic data that you create is actually adding value. That's actually helping the model generalize and solve problems more intelligently. But those are the the primary ways that we go about building our data sets.

### Where reinforcement learning goes next

**58:01** · Since we're talking about post training and RL in different domains, just so curious to get your thoughts on where we go from here in terms of generalization.

**58:12** · So, just to you know, build on what I was saying a second ago. Like, the industry seems to be marching from coding and math, which are domains with verifiable rewards, to to different industries. Do you think that this is where things are going and that AI industry as a as a whole is going to be able to cover those next few domains as efficiently as coding or math?

**58:37** · Coding is really special because it's a very intellectual exercise that created a lot of economic value, which then meant that we had an enormous amount of tokens that we could learn from, as well as tooling that allows us to verify whether you know, our models are actually solving problems.

**58:57** · So, coding is always going to have a special place in our heart and and something that I think AI is going to continue to get much better at because we we have this special relationship with it.

**59:13** · You know, with regards to other domains, I think what I'm excited about has to do with significantly more diverse environments for AI to learn in during reinforcement learning. Um, I believe that um you know, I mean, reinforcement learning is is such a general form of um teaching an AI how to solve problems.

**59:38** · Uh, we're just getting started at figuring out how to apply that. Um, and I think as our environments get more sophisticated, the AI then learns more understanding of um uh the problems that it's trying to solve as well as the implications of the actions that it can take, um then it becomes much better at uh at actually um solving those problems. When I look at the the uh environments that we're using today, they're still uh fairly simple um all things considered.

**1:00:09** · And I think um uh that's going to become significantly more complex and diverse over the next few years.

### Inside NVIDIA's research org: "the mission is the boss"

**1:00:16** · All right. So, you you mentioned the you know, making 500 people work together and I I said uh we'd get back to it because it it's so interesting. So, just taking a step back like tell us about the research organization at uh Nvidia.

**1:00:30** · Like how is it structured? How how does it work?

**1:00:32** · Well, uh Nvidia is not structured according to an org chart. Um, we have one, but it's not actually the best way of understanding how we work. Um, uh my team, for example, is not part of the official Nvidia research team. My team is actually part of the organization that builds the GPU.

**1:00:52** · Mhm.

**1:00:53** · And my team is not the only team building NeMo Tron. There's probably 10 teams around the company that have significant involvement in building NeMo Tron um in different parts of the company in in enterprise software um in uh uh our AI software um uh division, the part of uh Nvidia that actually designs the GPU also significantly is involved in in building NeMo Tron. Um, so there's there's so many different teams that that have to work together.

**1:01:23** · Um we um always like to say that the mission is the boss um rather than uh the organization. But um what that implies is uh that people have to figure out how to work together um which is challenging um in the sense that humans are naturally tribal creatures and it's uh not natural for us to um be friendly with people we don't know very well or trust uh co-workers that we don't have you know success working with in the past.

**1:01:54** · And um you know uh actually the name NeMoTron uh reflects that. We had um the NeMo team which was building software for AI and the Megatron team which was building uh primarily focused on systems research for um uh for building large language models and um you know we decided to work together and then start calling our projects NeMoTron reflecting you know sort of the um uh the collaboration between these teams. Since then NeMoTron has has dramatically expanded.

**1:02:23** · There's so many more teams that are part of the effort. Um and it's really important um that we have structured it uh in this open way inside of Nvidia. Um you know we are inviting uh volunteers from around the company to come help build Nvidia's AI. Uh we think it's very important to the future of the company and you know as that vision continues to develop more and more people want to join that's fantastic. We're really excited about that.

**1:02:50** · And it means that we then have to figure out uh how to organize the work so that everybody has a chance to contribute and feel heard and feel like their ideas um are are uh you know fairly evaluated um on the on the path towards impact. Um uh we we have a a formal process for doing that.

**1:03:09** · We have an internal website where people um share ideas and then those ideas um are assigned to um one of 25 different um leads that are, uh, you know, over various parts of building Neumotron. Um, they interact with those ideas. Some of those ideas get further developed. Um, some of those ideas get deferred until, you know, the next, uh, the next time we, we go around building a new model.

**1:03:33** · Um, but we're trying to build Neumotron in an open and inclusive way, um, uh, so that, uh, you know, we can really come together as a company to build it. I think, um, you know, organizations that figure out how to collaborate to build AI succeed. Organizations that struggle with control over who owns the AI tend to, uh, waste a lot of effort. Um, and so Nvidia's success and Neumotron success, I think, is directly proportional to our ability to collaborate. It's something that I care deeply about.

### How NVIDIA decides who gets the GPUs

**1:04:03** · Fantastic. But you you mentioned, uh, earlier that, um, despite the fact that, uh, you work at the, you know, number one undisputed, uh, leader in in GPUs, uh, you all, as an organization, don't have all the GPUs, uh, that that you would want in the world. So, like, how how does the allocation of GPUs and computes, uh, happen? Is it based on how promising an idea is or early success?

**1:04:27** · Uh, do you, uh, give GPUs, withdraw GPUs, uh, based on success?

**1:04:33** · Well, it's a really complicated question and it's it's obviously a a difficult problem for everyone in the industry to figure out how to allocate their their compute. Um, uh, inside Neumotron, uh, you know, so we we have a budget, uh, for Neumotron, um, and inside Neumotron, we allocate compute based on what we think the needs of the project are.

**1:04:52** · We have a, um, uh, uh, hierarchy, so we had a we have a set of programs, and and in inside of each program, we had a have a set of projects, and each of them put forward their requests, um, and then, you know, we have a two-week cycle where we review requests and we review the budget and then we make decisions in kind of a hierarchical way and then you know compute gets decided that way.

**1:05:19** · Now having said that this is something that I think we can still do better at.

**1:05:27** · It's hard when we're making decisions about compute allocation because every researcher is convinced that their idea could change the world if it just got a thousand times more GPUs attached to it, right? And they they might be right. It might actually be true and yet we're running at the limit. We don't have a thousand x more GPUs for every idea that that we have. We we have to operate within the limits that that we have.

**1:05:51** · And so it is a challenging process. We try to incorporate as many people's um perspectives into that as possible so that it's as much as possible a shared sense of understanding, maybe not agreement. So there may be times when one project feels like it really deserved more GPUs because the impact of that would have been so high but it didn't get it.

**1:06:13** · We hope in that circumstance that they have an understanding of why some other project did get more GPUs and why that was considered more of a priority during this particular allocation round for the company so that people can at least understand you know that there's a reason for the allocations that we have.

**1:06:34** · Having said that you know this process is always improving. There's always more work to be done to make this more transparent and more fair and and then of course my my number one is just to get more GPUs so that you know we can also fund more things cuz I would like to do that too.

**1:06:52** · How do you balance useful research with great exploratory research?

**1:06:59** · My belief is that research needs to be bootstrapped. It research is a chicken and egg problem. So Um is always the case that every researcher believes if I just had a lot more resources my idea would change the world. Actually, it's important that researchers feel that way because if you didn't feel that way, you wouldn't have the conviction that's required to go do something crazy and new, right? So, you have to believe. Um and and it's so of course um uh you start with that belief.

**1:07:27** · Uh but then how do you translate that belief into something that other people can understand, right? That other people are willing to invest in. Um this is what I call the the chicken and egg problem, right? Because like what once your research ideas is obviously good and impactful, it's easy to get resources, but how do you get it to be obviously good and impactful without those resources, right? So, so the way you solve chicken and egg problems is by bootstrapping. This is an iterative uh problem-solving approach where you do something small. You get some sort of signal about this is a good idea, and you tell people about that.

**1:07:59** · And then you ask for just a little bit more. And um if people saw like, "Oh, yeah, that that, you know, that experiment turned out pretty well. That's pretty intriguing. We should probably do a little bit more there." Um then you're on track, right? And uh that that um

**1:08:15** · over time, you know, iterate a lot, iterate quickly, iterate many times, uh you can bootstrap to, you know, finding significant resources for your idea and also usually attracting more people um to come along with it uh on the way because they have a chance to see that this idea is going to change the world and then they want to be part of it.

**1:08:33** · Is that how the moonshots at Nvidia got started as well over the years, whether that's in in AI or otherwise? So, it it it was bottoms up, somebody coming up with a good idea versus Jensen saying this is what we need to do.

**1:08:48** · Well, you know, Jensen has lots of good ideas, too, and so the company is very responsive to to his ideas, and that's uh that's important as well. But Jensen very explicitly says all the time, "This is a company of volunteers. You know, uh each of us is here because we choose to. We could we could be doing something else in our lives, but we we choose to be here.

**1:09:09** · And so, you know, we we tend to make decisions especially for early stage research. It tends to be very bottoms-up because, you know, it's it's sort of an invitation. Like, bring bring your best ideas. Let's let's figure out, you know, what are all of our best ideas and then we'll take a step from there. Um Now, do we sometimes have top-down ideas that are important for the company strategy? Of course, you know, of course.

**1:09:38** · NVF P4 pre-training is one of those. You know, so we decided as leadership of the company we're going to really invest in NVF P4 hardware.

**1:09:47** · Now it's time to go invent some optimization algorithms that succeed in using it. And so, we told the team we didn't say to the team you have to work on NVF P4 pre-training. What we said is there's an opportunity. We're making a big investment and if we can figure this out it will be significant for our company.

**1:10:06** · And then we let the people who are interested in that work on that and as a result we succeeded. You know, so so it is a balance of like bottoms-up and tops-down.

**1:10:16** · Um but it always has this bootstrapping feeling even even with something like NVF P4 where there's a significant like strategic top-down component. The actual technical solution, which is very intricate and complex and has a lot of moving parts that came from the researchers themselves. And you know, that's my belief is that research always comes from the researchers themselves.

**1:10:36** · You can't tell research exactly how to go solve a problem because then it wouldn't be research. It would be engineering. But in a world of of AI where the most important problems we have to solve all have this research component, there needs to be freedom for researchers to innovate if we're going to make progress.

### Why NVIDIA still feels entrepreneurial after 33 years

**1:10:53** · Listening to everything you're you're saying, I'm struck by how entrepreneurial the culture at Nvidia still seems to be.

**1:11:02** · So, like I work at some very large companies. I'm I'm sure there's all sorts of politics and you mentioned the tribal instinct. So, like I'm sure all of this is happening, but especially given, you know, how long the company's been around, the phenomenal success, the fact that people have been making a lot of money internally, it it still seems to be very entrepreneurial, bottoms-up driven, maybe meritocratic.

**1:11:24** · Is that the right takeaway?

**1:11:26** · Yeah, I mean, one thing that's very unusual about Nvidia is the tenure of its leadership.

**1:11:33** · Jensen Huang has been running the company for 33 years, but he's not alone. There are a lot of other very senior leaders in the company who have been there for three decades or longer, including my boss. And these people remember what it feels like to work at a very small Nvidia. And they know what it feels like to work at a very large Nvidia.

**1:11:53** · They have a shared sense of ownership for the company. You know, Nvidia is a place we often say no one fails alone. And the the the point of that, that's just a statement of fact, right? You work at a company, it's a one company.

**1:12:11** · You all succeed together, you all fail together. You work in accelerated computing. Accelerated computing is the composition of thousands of technologies. If any of them fail to deliver acceleration, the value is destroyed. It doesn't matter whether the chip is great if the compiler sucks. At the end of the day, the thing that you're selling is time and capability to researchers that are trying to build the future of AI.

**1:12:32** · And if they don't get that, it doesn't matter whether it was the, you know, the transistor or the math unit or the compiler or the library or the networking or anything else along the way that that failed to to live up to its expectations, the whole thing in composition fails, the whole value is destroyed. And so, we have a deep understanding of that culturally at Nvidia, and it is something that motivates the way that we work together.

### Why Bryan doesn't believe in the singularity

**1:12:58** · Maybe to close the conversation, I'd I'd love to zoom out, get your take from, you know, the perspective of somebody who's like as deep into all of this as it as it gets about where things maybe going. So, like, who knows in a few years, but I don't know in the next year or two, maybe there's some visibility. I read somewhere that you're not a really a big singularity kind of a kind of person. Is that Is that fair?

**1:13:25** · True.

**1:13:27** · And what Why is that?

**1:13:29** · Well, I think that intelligence is just so incredibly multifaceted.

**1:13:34** · You know, I always think about this question like if a company were to be looking for its next CEO, would it find the next CEO by looking for somebody who won the International Math Olympiad?

**1:13:50** · Probably not, right? Even though, like, it's incredible for people like I could never even compete in any way at the International Math Olympiad. And those people are amazing, right? They have just incredible brilliance. That's not the right kind of brilliance to run a company.

**1:14:05** · If we look, for example, at other aspects of our culture that that are really important. For example, musicians. What kind of intelligence does it take to become a hit musician?

**1:14:19** · Don't assume that it's all luck. It's not. These people are working hard, and they're very smart in ways that I might not understand with my PhD, right? I might not have that kind of intelligence.

**1:14:31** · And so, when I think about intelligence, I think it's just so multifaceted and so contextual. You know, it really depends on the situation. It's not just about raw intelligence. Raw intelligence is kind of like the horsepower of an engine, but an engine running without wheels doesn't go anywhere, Right? So, so intelligence the impact of intelligence has a lot to do with the context that the intelligence is put in the harness, the platform.

**1:14:57** · And so, when I think about that, I think you know, the singularity is although it's a an attractive idea, I think that it's it's a really a wrong-headed idea because it it doesn't really take into account these other factors. So, I believe that artificial intelligence is going to continue to develop at a rapid pace. It's going to unlock significant capabilities for people in every aspect of of our world economy, people doing every kind of work.

**1:15:25** · I'm very excited about the opportunities that it's that it's going to bring. I am also a little bit concerned with how we're going to manage the transition. So, I do think that transitions are hard for humans in general. Like we're we're conservative generally. And you know, there there is going to be a lot of change. This is a profound change in the way that we think, in the way that we work, the way that we learn.

**1:15:52** · Um Ultimately, I have faith in our ability as humans to figure it out. You know, we've done it in the past.

**1:16:00** · This is how this is who we are. We we build tools. We build external organs that help us solve problems. You know, we we have an external stomach. We call it a kitchen. It creates enormous value for us. We can eat things that we couldn't eat without a kitchen, right? Now we're creating an external brain. You know, the the implications of the external stomach were pretty profound for us as a species. They led to agriculture, which led to organized societies, the way our cities are built. So, we think about what is the implications of an external brain. Pretty profound. Nobody actually really knows.

**1:16:34** · But what I do believe in is um the power of humanity to solve problems and to learn and to incorporate new technologies in ways that benefit us. Um I also believe that the problems we face as a planet all require more intelligence. Every single one of them, whether that's inequality uh or climate

**1:16:54** · um change or um uh you know, any of the other um structural uh problems that that I think are very worrisome that we face, the solution to those are going to require invention and intelligence. And what that means for me is that the only kinds of tools that we can really create moving forward are going to be AI.

**1:17:15** · Uh because the problems that we face are all about intelligence. And regardless of the technological approach to solving those problems, uh the solutions will always be called AI.

**1:17:26** · Um and uh so that um uh makes me hopeful for the future, but also, you know, somewhat um you know, respectful of the challenge that it is going to bring to us as we we try to figure out how to live in a new way with this new external brain. Uh but I believe in our our ability to to learn and to change um and and I I think um ultimately this is going to make our lives better.

### The AI backlash

**1:17:50** · Do you guys feel the AI backlash that seems to be forming internally? Is that Is that something that you all perceive, think about, and if so, do you think it's a communication problem that our industry may have, you know, in particular, given what you just said about all the obvious potential of AI?

**1:18:09** · You know, I'm always worried about the way that the public thinks about technology and interacts with it. It matters a lot. Um and it is definitely the case that um societies that want technological advancement have more technological advancement than societies that that don't want change.

**1:18:26** · Um so I think it is um actually important to think about it. One thing that's interesting about AI is that um I believe it tends to be uh much more accepted when it is uh part of everyday life and then at that point people stop thinking about it as AI. It's just oh, this is the tool that I use. Like do you care whether it's AI that's helping you route your car when you ask the map application to help you drive somewhere?

**1:18:53** · Like I mean it is. There is actually sophisticated AI that's going into that. But you're not really thinking about that, right? You're just using a tool.

**1:19:03** · And so I feel like people's acceptance of AI you know, comes with experience, right?

**1:19:10** · The more experience we have working with it, the more we learn how to work with it productively. Um I think the more comfortable we we become with it.

### The controversial case: open AI is safer than closed

**1:19:18** · Great Brian. So it's it's been a a fascinating conversation. Maybe as a as a very last question to make sure we cover it. I want to make sure that we talk about safety.

**1:19:28** · What is the state of safety currently and where does open source and close source sort of fit in the safety conversation today?

**1:19:39** · Safety is on everybody's minds right now.

**1:19:43** · You know, watching the Fable release and the way that the government interacted with that I think is a consequence of concerns about safety about these models, you know, they get stronger and stronger and then they could be misused and um you know, there's different approaches to thinking about safety and and trying to define safety.

**1:20:10** · I have maybe a a slightly unorthodox opinion about this which is that I think open technologies are generally safer because there's more sunlight. You know, when more people are thinking about the safety of a technology and evaluating it and then contributing to making it safer. I think that's inherently safer than having a small group of people being in charge of safety for everyone else.

**1:20:37** · I also think with artificial intelligence because it is really about ideas. It's really about exploring ideas in different ways. That diversity is more safe than monoculture. And what that means is that there's going to be different beliefs. Like diversity isn't just about like the easy stuff. Diversity is about the hard stuff. Like when people have deeply felt disagreements. They really really totally disagree with each other.

**1:21:06** · Making it possible for people to explore their ideas in a diverse way. I think it's more safe than trying to create a walled garden where you know, certain ideas are considered safe and certain ideas are considered unsafe.

**1:21:22** · And you know, this is controversial in today's AI environment which I think is interesting because we've had hundreds of years of tradition that speak directly to this. You know, in in United States for example, we have laws about freedom of conscious conscience and freedom of speech and you know, it's not because we didn't consider for thousands of years would it have been safer if we didn't have those, right? We tried that.

**1:21:52** · We tried actually having a monoculture about like these ideas are safe to talk about. These ideas are safe to believe. And we found that to be much less safe than a pluralism where we officially don't take a position about what ideas are safe. We actually found that is much safer as a society to to support diversity than it is to try to keep everybody safe top down. And so I believe that open technologies for AI are inherently the safest way of building AI.

**1:22:26** · All right, love it. Controversial take here to close Uh the conversation. Brian, it's been fabulous. Thank you so much. We appreciate you spending time with us today.

**1:22:35** · Thanks for inviting me.

**1:22:37** · Hi, it's Matt Turk again. Thanks for listening to this episode of the MAD podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks and see you on the next episode.
