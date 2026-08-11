---
title: "Memory and Continual Learning: Engram's Dan Biderman and Jessy Lin"
source: "https://www.youtube.com/watch?v=aiR7F4jqjXY"
analysis_report: "[[Engram- 持续学习不是更长上下文，而是把组织经验写回模型]]"
author:
  - "[[Sequoia Capital]]"
published: 2026-06-24
created: 2026-08-06
description: "Dan Biderman and Jessy Lin, co-founders of Engram, are building a neolab around memory and continual learning, which they call two sides of the same coin. Their contrarian premise: instead of stuffing"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=aiR7F4jqjXY)

Dan Biderman and Jessy Lin, co-founders of Engram, are building a neolab around memory and continual learning, which they call two sides of the same coin. Their contrarian premise: instead of stuffing ever-larger prompts into the context window or bolting on RAG, bake a team's knowledge directly into the model's weights, so it knows your company the way an employee of several years does.  
  
The payoff: matching or beating frontier models while consuming up to 100x fewer tokens. Working with partners like Microsoft, Notion, and Harvey, the team draws on roots in computational neuroscience and state-space architectures to attack what they see as the real bottleneck in AI — not raw intelligence, but memory and continual learning. In contrast to the frontier labs' race toward one ever-bigger model and AGI, Dan and Jessy imagine a world where everyone has their own model — privately trained, always learning, and good at the things you actually care about. The real ChatGPT moment for memory, they argue, is the day your model feels like an intern that genuinely got smarter overnight.  
  
  
Hosted by Sonya Huang and Shaun Maguire, Sequoia Capital  
  
00:00 Introduction  
00:59 Always Training Explained  
01:51 Beyond Context Windows  
03:29 Ngram Product Overview  
04:34 Adapters And Training Signals  
05:32 Internalize Vs Externalize  
06:49 Compute And Token Savings  
08:19 Teams First Then Individuals  
08:51 Memorization Vs Understanding  
12:47 Dreams And Offline Digestion  
14:08 Training Beats Curation  
15:19 Why Everyone Needs A Model  
21:44 Bitter Lesson And Architecture  
24:44 RAG Killer And KV Cache  
31:38 Future Of Memory And Models

## Transcript

### Introduction

**0:00** · What about pre-training or even post-training makes it possible for the models to generalize in these magical emergent ways and controlling that process so that a company has a set of private data. How do we make the models learn \[music\] that just as well as the models know like the capital of France or you know, like how to write Python?

**0:21** · Um, so I think it it's a really fun problem to think about.

**0:32** · \[music\] \[music\] Welcome to Training Data. We are delighted to have Dawn Biedermann and Jesse Lin, co-founders of Ngram today. Ngram is a new lab focused on memory and continual learning and two of the hottest topics in all of AI research today and Shawn and I are delighted to dig in on these topics with you today.

**0:57** · Awesome. Happy to be here.

### Always Training Explained

**0:59** · Great. So we're going to kick off. The Ngram website says, "We don't see the world through the lens of pre-training or post-training. Our models are always training." What does that mean?

**1:09** · So I think like models today obviously know a lot of things. They're incredibly smart, um, but we kind of think the bottleneck for making these models more useful these days is not really raw intelligence, but understanding like new and evolving context. So whether it's like, you know, a new task that you're doing or a particular context, um, for, you know, like a job or something like this. Um, how do you bake that into the model weights the same way that, you know, pre-training and post-training makes that into the model weights very deeply.

**1:39** · And this is kind of why we think of ourselves as working on these fundamental problems of memory and continual learning, which are really two sides of the same coin. How do you make the models learn new things, um, and bake them deeply into the weights of the model?

### Beyond Context Windows

**1:51** · And is your premise then that memory as a separate database or separate, you know, thing that you've shoved into the context window is not true memory and is not true continual learning.

**2:01** · I think all of these tools will kind of come together. So, these days like the way that people are solving these problems is with context engineering.

**2:07** · So, you take like a huge prompt, maybe you like keep talking to the model over many, many turns and hours and um you know, reorganize the context to better understand like what you're trying to do. And we think like these kinds of things like tool use, context engineering will play a part, but I think an under-leveraged tool these days is using same kind of training um pipeline or framework or kind of workflow that the frontier labs are using to make these models really good at frontier math or code, but applying that to every kind of domain, every kind of context that you have like, let's say, in a company.

**2:40** · Yeah.

**2:40** · And to me, it's like as an individual um taking notes and having sticky notes is a very valuable thing. We should never discard this, but whenever we get back to business the next day, we always have some sort of trace of memory in our brain, some new information about how things should should be and where should we look. So, these two things should come together.

**3:00** · And current solutions are more kind of externalized memory. Um And this has two two issues. One is that the amount of tokens we will all collectively, individually generate is going to be in the tens of millions of tokens per day soon. So, just keeping it and searching through it is going to be and rereading it's going to be pretty expensive, but it's going to also be pretty hard, pretty confusing for the models unless we have major, major breakthroughs in how we do of tokens for Sean.

**3:25** · \[laughter\] That's good.

**3:27** · Depends on the day.

### Ngram Product Overview

**3:29** · Could you maybe tell us a little bit about the Ngram architecture, the Ngram product and and how it works?

**3:35** · Yeah, I mean, at a high level, I think what we're trying to do is take any context. Like, there's all these different um workspaces, let's say. Um so, we're working with partners like Notion, Microsoft, and Harvey that have these places where people are doing a lot of work over a long period of time.

**3:50** · There's all of this context. Um both in terms of like, you know, documents that you've already written as a team, as well as like now people are interacting with these agents more and more in these products. Um, we're having conversations, giving them feedback. Um, and figuring out how to have a model that deeply understands that context.

**4:07** · So, not just reading the files at test time, but really understanding it the way that an employee that's worked at your company for years has. So, you kind of understand at a high level, oh, these are the initiatives across the company. Um, this is the way that we do things. Um, you've studied like how to run the hiring pipeline, or how to, you know, do this kind of thing within the company.

**4:28** · Um, and can operate just as well as, um, like any anybody else can in the company. And so, what we're doing is training per team models within these workspaces that deeply understand those contexts and can improve with time on the things that people care about. Um, so the way that we do this at like a technical level maybe is, um, training these into weights. So, we do a lot of like adapter fine-tuning. So, adapters are many types. Like, I think people have looked into this for decades at this point. Like, whether it's Laura's, or prefixes, or, you know, sparse architectures.

### Adapters And Training Signals

**5:00** · I think like all of these tools are at our disposal. Um, and then figuring out what the right data is. So, how do you turn any kind of raw like document or interaction into useful training signal for the model. So, again, we have like a variety of tools now, like supervised fine-tuning, you know, um, RL, you know, on policy distillation, like all of these things that, you know, the field can has had kind of developed, um, and trying to fit these pieces together into a model that learns continuously on the things that people care about.

**5:31** · Yeah.

**5:31** · And it's not a bet that tools are not there. Like, our models always work under the assumption that some knowledge is externalized, some tools are always there. But, what you need to do is you need to figure out, and that's the hard task, is what needs to be internalized and what can be externalized. And for even for stuff that's externalized, many individuals and companies have their own bespoke tools and ways of doing things.

### Internalize Vs Externalize

**5:51** · Not everyone has the same, uh, you know, uh, bash CLI tools that, you know, the frontier models are training on and how to get them all to better understand your bespoke setup, I think, is its own interesting thing.

**6:03** · Hm. And so, is the premise then that my Notion agent will be a custom agent that is Laura fine-tuned or, you know, it's some way with an adapter tuned so that it's constantly learning on new content that's added into my Notion workspace?

**6:19** · Is that the premise?

**6:19** · Yeah, and and they're working with many models and they're the early users of all the frontier models and they're probably going to keep doing that.

**6:26** · Does this approach work on the frontier models or are they closed?

**6:29** · So, we need we need white, you know, we need white box access to the weights, right? So, you know, um, we can partner with companies that have, you know, closed-source weights and do this with them, uh, but it's easiest for us to do it with with open-source models. Uh, but any model that's a transformer model, uh, we can do our thing to it.

### Compute And Token Savings

**6:50** · And what's the trade-off then when when people are comparing the before and before and after using you? Is it that they're no longer sending so much context? Um, and and so, the trade-off is like you burn more compute up front to learn your company's way of doing things into the weights and then you're sending less context to the model on every inference pass. Is that the rough trade-off?

**7:09** · Yeah, that's that's one that's one thing. The fact that you don't have to research things and the fact and review things and the fact that you don't have to write like monstrous system prompts, they're already that can give you, you know, two orders of magnitude reduction in in token inference consumption. It's not like, you know, 50% or it's it can be 100x fewer tokens because many things, especially things that relate to people and teams and organization and priorities, these are things that you can't really find in one document unless like you really have it really regimented and document everything.

**7:41** · Uh, these kinds of things the model can kind of implicitly learn by training on some of the data and answer, you know, within 100 tokens what what the best frontier models would consume 100,000 tokens doing. So, these kinds of examples are interesting. And also the the quality, you know, there are tasks that are, you know, not supernatural for the current generation of the models and we we're we kind of think there's going to be consistently this gap of like 3 to 6 months ahead where there's certain things are bespoke that people are just exploring, the models are not fully prepared for them.

**8:09** · The models will at some point be great for them, but if you can autonomously learn in in a very lightweight way, it will give value in that time in terms of capabilities.

### Teams First Then Individuals

**8:19** · Why train on the workspace level versus the individual level, for example?

**8:22** · Uh either is is fine for us. It's just easier to start with, you know, it teams of people have, you know, are more, you know, disciplined in how they collect context and in the amount of context they have over years and it's easy for us to start there, but every person's computer and every person's phone one day is a useful, you know, target for our technologies and in fact will be very interesting to to go there. We just think, you know, the big deposits of information are now in in teams of people collaborating in knowledge work.

### Memorization Vs Understanding

**8:51** · Is it a feature or a bug that there is so much fact memorization basically built into large language models? And there's a school of thought that, you know, the memo the models just wrote memorizing the fact that the capital of France is Paris is actually a bad thing.

**9:04** · Mhm.

**9:05** · And what we would prefer for the models to do is, you know, abstractly learn the concepts of countries and capital cities.

**9:10** · Yeah.

**9:11** · But not to memorize all these facts in the weights. And so, I'm curious what you think about disentangling memorization um versus learning, how it's done in the models today, and then how you're thinking of approaching it.

**9:24** · Yeah, I think it's a really interesting question. Like, to some extent you kind of need to remember stuff in order to like compose them into a more complex concepts. I think the thing that's kind of missing is figuring out what's important to remember. And I think even now when you think about like learning new knowledge, if you look at a lot of these academic benchmarks, it's like how can we learn very specific facts like, you know, the length of a bridge in this like African country. And that's not something that you really want the models to devote capacity for. And it's not something that we devote capacity to.

**9:54** · Um so I think if you look at human memory, I mean you can say a lot more about this, but like it's lossy um because part of the future of intelligence is compressing what's important and separating that from what's not important. Um and so I think like you can't really separate fact learning from like non-fact learning or skill learning as some people would like to think. Um like if you take a model and like some people have done this with models where you like strip out the you know, like all the facts and just have it like the pure core or something like this. It's very unnatural as a model.

**10:26** · It doesn't know basic things. Um and you kind of need need that. But I think Why do you need that? Like why can't you look up facts and then just have I think if you look at like how the models think, if you need to recall basic facts in order to like take the next step in your thinking, you can't get very far. Um maybe that's like a high-level intuition, but it's part of like the reason why we think training is really important.

**10:49** · In order to like think more and more complex and deep thoughts about things, you kind of need to internalize something so that you can compose them into more abstract concepts.

**11:00** · Yeah, and and there have been efforts before that were hard to scale to try and you know, disentangle the two and pre-train the models in a way that's, you know, allows it to retrieve and search for things and not internalize them. It's just the recipe we know to hill climb on collectively right now is this, you know, fact pre-training stuff.

**11:18** · And I think the the magic of of or the the mystery of this approach is that, you know, traditionally in CS we would have, you know, databases as its own curriculum and we would have algorithms and the databases is like facts about the world and capitals of whatever store them query them.

**11:35** · There's also algorithms of how do you efficiently manipulate information and get some answers in in a sample efficient way and I think the magic of deep learning is that these two things are now mushed together and we need all these smart people on topic interpretability to try and and and and break them apart.

**11:51** · And I think a lot of what we're seeing now in the adoption of AI into the economy is that these things are gradually separating again where companies have their own context and they really handle them with care and engineer them with care and there's a generic model that's completely a stranger to these contexts and that the model is operating on them but it for us it's clear that there needs to be a certain convergence at least with with some cadence where where the the facts and the stories and the details are are getting mixed into the model.

**12:20** · It has disadvantages as well because if you you have to you know capitals of of of countries are you know they can change but it's not very frequent but there's many other facts that are changing all the time. I just imprinting them into weights is a is a challenging thing to do.

**12:35** · I see. So you're saying it's a false dichotomy to try to separate algorithms from databases here. Um what really matters is like how to distinguish what's important to remember Yeah.

**12:45** · versus what's not important.

**12:46** · Exactly. And it's an open question.

### Dreams And Offline Digestion

**12:49** · and are you guys taking any inspiration from that in in terms of ranking?

**12:53** · Very very loosely I think. Just the idea that that's kind of a phase that's missing maybe where you take a context and you deeply internalize it. Right now it's like everything happens at test time. You look at the you know context that the user gives you and you do some like thinking on the fly.

**13:08** · But again like you can't get very far or you can get so far maybe and like you make mistakes along the way. Like how do you digest that back into the model so that next time you do it you do it the right way and make even more progress.

**13:21** · Yeah.

**13:21** · And then what are dreams? Dreams are pretty crazy things to to say we want to build an AI that's like our dreams sounds a little bit like a nut thing to do. Um there's not a lot of coherence there.

**13:30** · But what's interesting there is like what happens in our dreams? We we we see things, we talk to ourselves, and we we experiment with the affordances of what can we do and can't we do in the world and social situations and then, you know, um any any it's heavily biased towards social uh stuff, right? So, for us, too, with things we're building is, you know, we give the models the time to then go back, retreat from the actual interaction, and experiment with its affordances. What can it do in an environment? What can it What does it know?

**14:01** · How fast can it can it, you know, handle these kind of tail extreme uh things that same ones that we dream about at night.

### Training Beats Curation

**14:08** · Do you guys come from academic backgrounds? Like, what's a canonical example that motivates this problem or, you know, like or that's a win so far?

**14:19** · Yeah, I have one example. Maybe Jesse can give another one. A hypothetical one, for example, imagine one of the AI labs, say, OpenAI has to win some math Olympiad in a week time from now.

**14:31** · Would they construct a catalog of all the math textbooks and really have people annotate which chapters to get and which graphs to to see or will they actually collect this, synthesize some training data, launch a training job, see where it lands in 5-6 days, start evaluating it, and stuff like that? So, it's it's obvious for anyone who's trained a model that there's superior way to integrate across the ideas and capabilities, and it involves this kind of magic of training. Um and we are clear that this has to happen in those high-stake domains of math and coding and cyber and stuff.

**15:01** · We just think much of this magic can actually end up in the in the hands of of many more people in in interesting ways.

**15:09** · Like, why isn't it just the fi- the foundation model labs that own the end product here? You know, like, how do you go between giants?

**15:18** · Yeah, so I think like the worldview that we have is a bit different from the Frontier Lab worldview, where it's like we want one model that's bigger and bigger, that's more and more intelligent across a variety of domains. Instead, how we see it, like we kind of imagine this world where everybody has their own model. A lot of the things that people want to learn are either private, like things that will never see the light of day in a post-training data set, or even conflicting, like, oh, the way that I want to do the task is different from how another company or another individual wants to.

### Why Everyone Needs A Model

**15:45** · And I think a lot of these things we're already seeing are um hard to train into the models with the same tools that we have used for like decades in machine learning, which is like you have really clean supervision, you have like ground truth reward signals, um and you like create a nice environment, and you like train the model to like use the tools to better accomplish this like coding task. And instead, a lot of the things that actually happen out in the world are very ambiguous, or like um it's hard to say like what makes something good.

**16:15** · Um and so, I think a lot of these things are very specific to individuals, and I think very kind of misaligned or not very aligned with how the Frontier Labs think about the whole training pipeline and what kind of models will exist in the longer term.

**16:32** · Yeah, and to add to it, I think, you know, what is the P0 for the Frontier Labs? And some of you here are are pretty close with them. It's getting to AGI, getting this one generic model that's extremely capable in coding and math, and then using it to to automate the economy or to solve really hard, you know, long-term problems in cryptography and defense or whatever. Um and it's pretty clear what needs to happen to push this, you know, more pre-training, bigger models, more data, uh more RL, more inference time compute, that kind of stuff.

**17:03** · That's P0, that's where the majority of of expenditure and talent goes. And definitely all of them are thinking about memory, and all of them are thinking about continual learning. It's just more of a product kind of effort right now. Um we think um it deserve it it deserves its own its own attention. Uh, we think breakthroughs need to happen there and and Demis and this acquire event about a month ago said pretty clearly that we need new breakthroughs around these topics and obviously they're thinking about them. We're just focusing exclusively on this.

**17:32** · And we think uh certain things around incentives of where the data is uh and who owns the model are pretty interesting. Um, so if you could learn from many humans or organizations at scale uh without necessarily sending someone to work with them shoulder to shoulder, uh that would be a a pretty big unlock.

**17:49** · And maybe another point on that is like I think a lot of things need to look different in the world. So, one is there needs to be new research breakthroughs, two is new infrastructure for training like, you know, small models for everybody rather than like one big model, one big run.

**18:03** · Um, and then the third I think is um a different way of kind of combining research and product. Um, so right now I think like there's like researchers in these frontier labs, they kind of train the model, they throw it over the fence to the product team who then like prompts or contacts engineers like new product surfaces on top of the core models. Um, but in this world where the models are always training, I think the inputs that users provide are very intricately tied to what the model has learned from, like what the training signal is. And so there needs to be a lot more of a kind of integrated loop between like research and product.

**18:34** · And so like while we're focused on tackling a lot of the core research challenges and that's our background, I think we're also very focused on like how to deploy this as quickly as possible to like learn from feedback in the real world.

**18:47** · What motivated you to work on this problem?

**18:50** · I think like it's obviously like one of the grand challenges in AI. I think everybody's talking about it these days because like the models are so smart.

**18:57** · What what else is left, you know, it's I think learning like at the edges, like learning the remainders of what makes these models useful. Um, it's not just about raw intelligence anymore, it's about like learning new things. Um, and I think it also feels very fundamental because it kind of goes back to really understanding what makes the model so good. So right now the models kind of incidentally know a lot of things from pre-training and we don't really understand why.

**19:23** · It's like the internet was just, you know, this gift granted to us where there's like a diverse set of data that contains like all of these different examples of coding and like writing and all these other things and it just happened that way. And now to figure out how to crack this problem of continual learning, it's about figuring out what about pre-training or even post-training makes it possible for the models to generalize in these magical emergent ways and controlling that process so that, you know, a company has a set of private data.

**19:55** · How do we make the models learn that just as well as the models know like the capital of France or, you know, like how to write Python. So I think it it's a really fun problem to think about.

**20:07** · And Don, you came from the neuroscience world, is that right?

**20:10** · Yes.

**20:10** · Yes. So I was initially interested in in questions around, you know, consciousness and the human condition and things like that. Are the models conscious?

**20:18** · I don't have any any advanced thoughts on this more than you would you would read. I don't think so, but it's important that smart people are thinking about it. I would say like I was interested in how humans think, how humans perceive and as almost first key the Israeli psychologist used to say like he's not interested in artificial intelligence, he's interested in natural stupidity. So I would say like I started kind of similarly trying to see how people and animals experience the world.

**20:44** · Gradually, you know, my inclinations took me to the stats and AI domains and there I figured that so many of the same problems of memory and continual learning are really really urgent.

**20:54** · And the kind of solutions we have in the current systems are pretty far from what we have in biology and I'm not one of these people who would say that the the machine should be like, you know, like the animal or the the human brain. I don't think so. There's many things computers can do better than us, but human memory has these like very different uh things in it. It's, you know, if you want to store a whole code base or you you can you use a computer.

**21:17** · You don't even need AI on the computer to store everything losslessly and just get it. Uh but the human brain evolved to work in these constraints of of, you know, information capacity and to have these fuzzy representations that can then, you know, be abstracted and form connections and inform the next day. Current systems don't really have that beyond the generic pre-training step. And I was really interested in, you know, what are ways to to to build that in? What are ways to learn from that?

### Bitter Lesson And Architecture

**21:44** · This is more of a philosophical question.

**21:46** · You know, you mentioned in the brain has a bunch of different real estate different co-processing units, whatever. Modern computer architecture, there's CPUs, GPUs, you know, memory, there's different co-processors.

**21:58** · Um with like the bitter lesson, do you think that what's happening is that like LLMs are, you know, converge to say like one co-processor that's just totally dominant. It's like everything all compute is going to happen in, you know, the GPU equivalent of like a language model? Or do you think that these models are kind of building a bunch of co-processors like, you know, emergently inside the model?

**22:31** · You know, like like you know, and take with memory like do you think that the models themselves will just build, you know, whatever part of the brain equivalent would be that's good at memory or or do you think there needs to be like another stand-alone architecture that Yeah, like is is memory an emergent property Exactly. Versus like Yeah, and almost everything. Like is everything that we need in intelligence will just be emergent with better training data and more skilled compute?

**22:58** · Yeah, I would say just on a more like a superficial perspective on the current deployment of AI. It's way more than than just GPUs and we're seeing all these, you know, sandboxes exploding and models operating on other computers trying things. So on the model architecture level rather than on the So other experiment either there have been many previous experiments different architectures that we contributed to like the state space family and others to try and handle very very long context more efficiently.

**23:26** · The thing with all these methods it ends up being a trade-off usually a trade-off between memory and accuracy and memory not in the behavioral cognitive sense memory in the computer sense, right?

**23:36** · Instead of having, you know, the the memory footprint of the transformer attention which is quadratic in the sequence length. These models are Some are claiming, you know, they have sub quadratic.

**23:47** · Yeah, some are claiming some do have it, right? And some of the the best Chinese model have layers that are, you know, inspired by those state space architectures and are, you know, not quadratic in cost. Thing is is that in in in our hands we find that, you know, they always compromise accuracy for this memory. There's no free lunch. And what we're saying is like, look if you're really bitter lesson peeled, what you want to do is you want to think how can I burn more compute? And how can I burn it on, you know, new context that I have not seen before.

**24:14** · So we're as bitter lesson peeled as anyone else and we are not betting that the overall direction of AGI is is going to, you know, end anywhere soon. We just think there's more compute to scale and if I truly want to understand Shawn and Shawn's work and Shawn's context just like re-reading files is not going to make it especially for a special person like you. We got to train this guy.

**24:37** · Special is derogatory.

**24:38** · We got to train a 100 \[laughter\] trillion parameter for this guy.

**24:42** · Yep.

**24:42** · Cosine cosine. Um, what are you finding that people care most about their models learning? Like is it memorizing facts about the organization? Is it remembering like, ah, no, we do CI this way? Is it like what what are people actually hoping that And then maybe this feeds into how you do the do the ranking of memory slots and all that.

### RAG Killer And KV Cache

**25:02** · Yeah, well, I think if you look at what people are spending their time in the app layer doing these days, it's a lot of just trying to make the model work well for your use case. Like, oh, I want the model to like you know, let's say like design my website with my brand style. Like, that's like a you know, very common example these days, but there's many kinds of different tasks that people do with agents. Like learning how to run a workflow or you know, kind of your particular way of like writing, let's say.

**25:32** · So, there's many many kinds of things. And honestly, like I think when we think about these methods, kind of going back to this distinction between like facts and skills, there really is none. I think the methods are kind of agnostic to that.

**25:45** · Yeah, to me it's like the the natural thing almost all the app layers are basically, you know, a frontier model wrapped in in a loop with search tools and stuff.

**25:56** · And what they're all interested in doing with us is finding ways to kind of interface with their data in a way that's, you know, faster, more efficient, and also has is more contextual. So, almost all of them it's like \[snorts\] we want to have our, you know, our firm knowledge, you know, be encoded in something that's more efficient I don't have to research. We want to have the model know in a targeted way who's the person I should triage a thing to. And we're just showing them that with pretty lightweight training these things can can be instinctual to the models.

**26:25** · They don't have to have these very involved long repo loops to solve them. So, it's in a sense it's like, you know, it's it's a rag killer kind of kind of thing. Again, we can always do rag and we can always retrieve, but that's the thing that people are interested in interfacing with very large data planes and automating very repetitive things this way.

**26:46** · Yeah. And I want to double click on this rag killer thing. And I'm sorry to beat a dead horse, I just don't fully grok it yet.

**26:52** · Yeah.

**26:53** · Um is the premise that there's some trade-off between doing rag versus up updating your model weights? Is the idea that you should be doing both? Like what types of things should be done in the weights versus what types of things should be externalized to rag?

**27:07** · I think it it's a it's an unsolved problem. I don't think anyone has answer to it. Um we're all working on it. Um it's also the fundamental question of like biological memory. What should be internalized versus what not? Um I do think that things that are like, you know, do you need to internalize the room number in a hotel that you were in like a year ago? Probably no, not in your neural tissue.

**27:32** · Uh probably that's good to write down, but do you need to internalize maybe the password to your home right now?

**27:36** · Probably it's useful for the next few years to have that imprinted somewhere.

**27:40** · So, yeah, how does this translate into like knowledge work in products?

**27:44** · This is still something we figure out and we try to take the approach that we try to use as few heuristics as possible. It's easier to run filters on the data and say like I'm going to keep this, discard that, train on this, train on that, but as humans, you know, we watch Tik Tok and we, you know, get exposed to a lot of garbage and still the brain is able to learn and not completely go off the rails and we think models should be the same as well.

**28:05** · Yeah.

**28:05** · Maybe concretely in the short term, I think a lot of what people are worried about these days is the huge inference costs of running these agents like for days on end.

**28:15** · High inference cost is a good thing.

**28:17** · \[laughter\] I mean consuming tokens for what?

**28:20** · Sonny works with fireworks.

**28:22** · He really loves Zion.

**28:24** · \[laughter\] I love inference.

**28:27** · We love inference, too.

**28:28** · Yeah, so I think it's like in the short term, I think that's the immediate pain point. Like why are you reading the same files over and over again, you know, even in the same query? But like definitely, you know, across people in the same company, they're running the same queries on the same documents over and over again. And that should be something the model just knows. Like in the same way you ask an employee, they don't, you know, type into the search box like, "What what was I working on yesterday?" They just know.

**28:51** · But doesn't caching kind of solve that?

**28:53** · I think to some extent, yeah, but I think going back to this like question of what should be internalized versus what's um like something you retrieve at test time, I think again like a lot of it is about building on your knowledge. So, if you are always doing rag, you can't make associations like, "Oh, you know, I see somebody, you know, on the team is doing this kind of research." And I kind of like recall at an abstract level, "Oh, there's this like related thing that you might want to know about." You didn't even ask about it, right?

**29:22** · But I think like these kinds of associations can only happen in weights because they're not really about, you know, you ask me to search for this, I'm going to search for this.

**29:31** · also the the I think the main limitation with retrieval systems in general and in AI specifically is like the problem is not so much what to store and where to put it. It's the problem is like how how to address it, like how to query the thing. Do you know what to look for even? Yeah. And this is involved some sort of intuition that sometimes the models don't have interestingly enough. They don't know where to look. Uh and and especially if you're, you know, limited to the the current way of doing things which is keyword search, that's just easier to scale in RL and least involved in terms of like infra for embeddings and stuff.

**30:03** · So, yeah, knowing what to search is something that's intuitive and can and can happen in the weights. And also about caching and inference like much of this company started with us taking a like a deep dive into like KB caches and caching.

**30:16** · And this is a a fascinating thing, right? KB cache is a monstrosity of the current uh way of doing things that, you know, think about it. A KB cache for a single like Wikipedia article for some, you know, Taylor Swift or something like this, it will be like 80 \[snorts\] GB of HBM memory on the GPU.

**30:35** · And an entire llama, it's it's for say a 70B llama model. And the entire weights of the model would be about 100 gigabytes and you know, with with some distortion they remember the entire internet. Um, and how come this thing is so uh one thing is so bit efficient and this we have this proof of existence that creating this scent can pack a lot of information in very few numbers.

**30:58** · Whereas this KV cache thing, you take a few tens of kilobytes of article and it becomes those 80 gigabytes of of brain state. So you can sure you can cache this, you can load this, you'll have issues with disk to HBM uh stuff. People are working on it, it's pretty interesting, but what if we can take those 80 gigabytes, spend some compute offline, maybe also on fireworks and file but then compress it and make it really really small so that the thing we load and cache is like a thousand X smaller.

**31:28** · That would have tremendous implications for how we load things, how fast we can do things and what the fidelity of the representation is.

**31:37** · Super interesting.

### Future Of Memory And Models

**31:38** · Yeah.

**31:38** · What are some of the things that could happen in the next year or two that would be like the chat GPT moment of memory? Or do you think that that's not how things will play out?

**31:49** · It's a good question. Um I don't know. I think like the first proof of concept of the thing that people keep talking about with continual learning, which is you have an intern that you can teach things over time and it actually gets better. I think everybody's waiting to see that, you know, and no matter how sophisticated the context engineering approaches are these days, they're not getting there.

**32:08** · So I think you need, you know, all these tools at your disposal to make that happen. Um, but I think it will be something like that where it's like the model's actually getting smarter. Like, "Whoa, it it's different from yesterday."

**32:19** · Yeah.

**32:19** · And it's important to say that the chat GPT model was not anticipated. We were just, you know, read about all the different product the the product directions that certain people had before chat GPT was different. Um, I feel like to me the example is like, "Look, if you, you know, resign from your job today and your sole mission was to make a model that's better for you. And you would use open AI and Anthropic and all these frontier models and you would just 24/7 engineer the contacts right skills, your way to move the needle is very limited as an individual.

**32:49** · You're just better off waiting for the next version of the model and you and you will take it from there. And we would like um to see a future where actually the more time you spend on the thing actually translates to the quality of performance at least in the things and domains you you care about. Um and this is pretty hard to achieve and the only reason it we we think it could be achieved is if you start scaling compute and training on these data without destroying them all importantly, which is pretty hard.

**33:17** · Just couple like this is just for fun like rapid-fire questions going off just memory. When's the last time you reached surprised about something in AI?

**33:27** · In any area.

**33:28** · When reading about fundraising.

**33:30** · A \[laughter\] lot of surprises every day.

**33:33** · I would say all of us felt, you know, a little bit of a change around the capabilities of the coding agents.

**33:38** · That's true.

**33:38** · but we we've been, you know, dabbling with these things and trying to make them work in in more effortful ways before, so it didn't come as a complete surprise. Um but yeah, I think to me the main events were GitHub Copilot. That for me was just the main event and ChatGPT. And then seeing the agentic stuff, we all anticipated, I think, and and different different people had different expectations on how far it can go and how long horizon it can go.

**34:05** · But I feel yeah, it's we're we're yet to see something fundamentally different and people are working on completely new ways of doing things now. Um But yeah, to me it's it's models actually changing in a way that's not harmful uh and learning new things uh on the flight or, you know, personally and economically viable. That's interesting.

**34:25** · Right now there's this idea of like we each have a token wallet that we're going to bring around to companies.

**34:30** · Mhm.

**34:30** · Or diff- to different apps.

**34:32** · Um different workspaces. Do you think that we're going to end up with like a memory bank, a memory wallet that we're going to move around to across the digital world as we go?

**34:43** · I think it's an interesting question. I don't know if we've fully figured out what the right kind of like product form factor is in the sense. In a way, even with like ChatGPT memory, let's say, I kind of don't want it to remember across my like personal and work context.

**34:59** · Like it's like, "Oh, you know, you might like these sheets because you trained a model on a GPU last week." It's like that's totally irrelevant. And to some extent it's like because the memory is flawed, but also I think you do want memory in your, I guess, tools and the products that you use to be separated to have control over that. So, I personally think like there needs to be some separation there, but I guess to be determined what that might look like.

**35:24** · Yeah.

**35:24** · And like I think a holy grail is like you go to work and you just burn through all these tokens and you create all this value and somehow, you know, all the IP and stuff stays with the company, but somehow the skills you learned, the things you invented, your ways of doing things, some of them you can take with you as well to your next job in a way that's, you know, sanitized and not, you know, harmful to any other company's IP. So, I do think like carrying a set of skills will be interesting.

**35:50** · We do it in our biology right now and we just, you know, sign NDAs and have like ethical rules around it, but I think doing it in the digital world would be pretty interesting and pretty rewarding because it will force each of us to push the frontier and implement AI more deeply in our companies, in our individual life, and then be rewarded for it.

**36:08** · I started a PhD in the stats firm in 2007 at Stanford and AI like AI was boring as hell at the time. It was all statistical learning. And there's basically two areas that computer vision and NLP. So, like vision and and language were kind of the two areas and I think that's still true. In 2012, AlexNet happened. Like, vision was dominating for 6 years or whatever.

**36:33** · Are you guys surprised that language seems to be like the language approach seems to be like dominating over vision in progress? Question two, do you think vision has any chance of coming back? How do you think about this?

**36:48** · Yeah, I think it is pretty surprising to me. I mean, some people maybe saw it coming, but I think I've always kind of been interested in language um as like I don't know. I guess like a medium for communication and like so many kind of complex abstract things can be done in language. Um I do think like, you know, I imagine like in the longer term language and vision will kind of like combine in this more like unified system where, you know, we kind of like taking inputs from all of these different modalities and like understand them in this abstract way, but um yeah.

**37:23** · Yeah, to me like I've never been interested in language. It seemed to me such a such an advanced capability that, you know, is is very the the entire animal kingdom has very different forms of of speech and language than what we, you know, and how we communicate with ourselves and in writing. Uh \[snorts\] and I was always uh as many other leaders in AI had this thought that, you know, the natural thing is you have to experience the world, act in it, and vision and action that will be the the key.

**37:50** · But then I've, you know, like anyone else seen the the ChatGPT moment and went to to do some work at Mosaic and stuff like that to learn how the sausage is made on the on the NLP side.

**38:02** · And the thing that's striking is that like the the language should be pretty hard. Like, each word has this uh one-hot embedding vector that's as dissimilar to any other word uh than it is, you know, uh to, you know, it's it's a completely high-dimensional space, and it's really artificial in a sense, and we we learn it with models that are order of magnitude bigger than the best vision models.

**38:26** · And still, you know, things work pretty well. I do think there's a lot of juice to be squeezed in an image and video, and I think you guys doing are good good investments in this space, but it's I think the two would keep being interesting in different ways.

**38:41** · I'm going to now tell you my That was my lead up. Now I'm going to tell you the crackpot theory.

**38:44** · \[laughter\] I like And this this podcast is not for me to pontificate to you guys, but this is something I've been thinking a lot about, and I just you're the right people to share this with.

**38:55** · I I was pretty shocked that language kind of surpassed vision, and I underestimated what was happening with LLMs in like 2018, 2019, 2020 because I just had this bias towards vision. And when I look back on it now, like I think what's basically happening is that in biology, like vision has a massive fundamental

**39:20** · advantage over language in biology, and maybe I'm wrong, but basically like the bit rate that your brain can process optical data through the eye is And this is my I'm not a biologist. This is just kind of my dumb assessment. It seems many orders of magnitude greater, and there's a lot of like optical processing that happens like even before you reach, you know, like electrons.

**39:49** · And so it's just like the total bit rate that is of training data that's kind of being processed and then making it to your brain seems many orders of magnitude greater than the audio data, where, you know, it's sound waves, where sound waves are fundamentally like much slower bit rate than light.

**40:10** · Yeah.

**40:11** · And then there's almost like like an upscaling from the acoustics to electronics, which make it into your brain, where it's like there's like a downscaling from photons to electrons with vision. Whereas in computers today, everything is electronic. So, it's kind of like you nerfed vision and you like promoted language, where the it's like all processing is on the same playing field, it's all electronic.

**40:37** · And I just I think this might This is like my crazy ass dumb non-technical crackpot theory, but I think this might be part of why just like from an information theory perspective that like maybe language and vision are on a similar playing field by the time you get to like LLMs, and then LLMs are we're just a really really smart architecture that's better suited for language than for vision.

**41:07** · Um how dumb does this sound, especially to you, Don, the neuroscientist?

**41:11** · And Jesse also has some background in cognitive computational science, right? So, I would say my my point here is like, look, much of what we're doing in knowledge work, we haven't evolved to do, right? We're sitting on these computers, reading these things, writing these memos, whatever. We are not evolved to do this. It's new to us. Our brains are not wired for this. Still, nevertheless, it's useful to have LLMs to do this for us.

**41:34** · And you know, as humans, we're heavily vision biased. You know, other rodents are more olfactory biased, and I've worked on these things myself before. So, what's the real estate in the brain that's allocated to vision and you know, occipital lobes versus like language areas, temporal lobe, probably more vision. I'll have to check with check with ChatGPT, but I think that's the situation.

**41:56** · know from memory?

**41:57** · No, man, I'm externalizing. I'm a big rag believer in my personal lifestyle. \[laughter\] But I think In the limit, we're all it's all rag.

**42:05** · I internalize just you know, important things like my emotions to you. I was just kidding.

**42:11** · Sorry, no. \[laughter\] Anyways, um yeah, envision is dominant. When people are training vision language models, they end up the language ends up dominating the vision content there. Um but yeah, it's it's hard to say that because a certain brain is more, you know, um biased towards a certain modality, it doesn't mean necessarily that we're going to more efficiently do it. I do think that efforts on like brain computer interfaces should take this into account. How do you then relay it back to the brain? That's where I think it's really important to think like what real estate do we have there right now?

**42:40** · Um but for knowledge work, it's equally fine if it's text, I think.

**42:46** · Last question. If If everything goes right, what does the world look like in 5, 10 years? And then what does Ngrams roll in it?

**42:52** · I think I'm imagining like a world where everyone has their own model um that is really different from the other person's model and from the frontier model. And all of these kind of serve different purposes. And to have a model that really, you know, I think people often talk about like knowing knowing you, um but also like um kind of like helping you in the ways that make sense to you um personally, um whether it's like an individual or a team. I think there's an element of like having different kinds of intelligence everywhere.

**43:24** · Yeah, and to me actually it's it's a variant of the story where like you know in neuroscience, we know that memory and navigation are pretty closely related. Same circuits in the brain that, you know, represent landmarks in space are in charge of some, you know, elements of episodic memory and things like this.

**43:40** · And for me, I think the company can be you know, the actual LLM interface to the data plane for everyone. So, sharing some similarities to great companies like, you know, Databricks and Oracle where, you know, we form these memories that happen to be neural memories with models that happen to be personalized and happens to be there's hundreds of millions of them, but they're basically a neural interface to the data plane in a way that's that's very different from what we know, and it's more efficient, it's more associative. It's not representing the file system as it is, it's representing a brain state of that file system.

**44:11** · So, that's for me a vision.

**44:14** · Beautiful vision to end on. Thank you guys so much for coming by to share what you're building.

**44:19** · Awesome. Love it. Thank you guys.

**44:23** · \[music\] \[music\] \[music\] \[music\]
