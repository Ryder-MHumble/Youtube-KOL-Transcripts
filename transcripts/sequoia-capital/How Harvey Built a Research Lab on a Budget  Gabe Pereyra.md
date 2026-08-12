---
title: How Harvey Built a Research Lab on a Budget | Gabe Pereyra
source_url: https://www.youtube.com/watch?v=MGouk8W51v0
video_id: MGouk8W51v0
account: '[[accounts/sequoia-capital|Sequoia Capital]]'
account_name: Sequoia Capital
featured_people:
- '[[people/gabe-pereyra|Gabe Pereyra]]'
published: 2026-08-11
created: 2026-08-12
language: en
speaker_attribution: contextual
description: How does an application company compete with frontier labs that have more money, talent, compute, and data? At Sequoia Capital’s Own Your Intelligence event, Harvey co-founder and president Gabe Perey
tags:
- transcript
- kol
analysis_report: '[[analysis/Gabe Pereyra- Harvey 的研究实验室不是自建前沿模型而是后训练飞轮|Gabe Pereyra- Harvey 的研究实验室不是自建前沿模型而是后训练飞轮]]'
---
![](https://www.youtube.com/watch?v=MGouk8W51v0)

How does an application company compete with frontier labs that have more money, talent, compute, and data? At Sequoia Capital’s Own Your Intelligence event, Harvey co-founder and president Gabe Pereyra shares the playbook: leverage the frontier ecosystem instead of building everything yourself.  
  
Gabe walks through how Harvey built its research lab, starting with benchmarks like LegalAgentBench and its open-sourced diligence dataset, using domain experts to guide synthetic data generation, partnering with multiple neolabs for post-training, and building the serving and evaluation infrastructure to put models into production with confidence. He explains why open-weight models have made post-training worth it for the first time, and why every company will eventually need some version of this playbook.  
  
00:00 Introduction  
00:37 Building a research lab on a budget  
02:28 Legal Agent Bench, contracting, and the diligence dataset  
03:57 Domain experts guiding synthetic data generation  
05:23 Why Harvey open sourced its datasets  
06:55 Working with the neo labs — and why more than one  
08:20 Post-training in-house: building "Associate 1"  
09:44 The model serving matrix: 60 countries, fallbacks, SLAs  
11:05 Deciding what stays in production  
12:29 Simple open source switches and model routing  
13:55 Moneyball: "If we win on this budget, we change the game"  
14:53 Q&A: Training with sensitive data  
17:16 Q&A: Competing for research talent  
18:46 Q&A: Designing rubrics that actually challenge frontier models  
20:19 Q&A: Where the pipeline breaks — data, research, or infra  
22:59 Q&A: The tension in open sourcing a benchmark  
25:02 Q&A: Biggest remaining open problems  
27:10 Q&A: Competing with horizontal products

## Transcript

### Introduction

**0:00** · Next up, we are honored to have Gabe with us. Gabe is co-founder and president of Harvey. Um you were a research scientist at DeepMind ages ago, um and then at Meta I think before you showed your college roommates uh what GPT-3 could do. And this duo uh then became Harvey. Um we're really excited to have you here. I think everybody here in the audience is an application company um thinking about how to start doing their own research, post-training their own models, um and uh create their own labs.

**0:28** · And so I think Harvey has really set the example here, and we're really delighted to have you give a talk on how to how you guys built Harvey Labs.

### Building a research lab on a budget

**0:37** · Awesome.

**0:38** · \[applause\] So the alternative title to this talk is building a research lab on a budget. And it's an unfair game competing with the frontier labs if you're an application layer company. There are rich teams, there \[snorts\] are poor teams, and then there's us in the application layer. The frontier labs have more money, more talent, more compute infrastructure, and data.

**1:12** · So how do you compete?

**1:16** · By using the frontier ecosystem. When we started Harvey 4 years ago, most of these companies either didn't exist or were just getting started. And so we either had to build everything ourselves or in most cases focus on something different. Like building our GTM org and a great product. But today using the frontier ecosystem I think you can compete with the frontier labs and build frontier intelligence.

**1:47** · This talk is going to be our high-level playbook for doing this. And I'm going to talk about how we build benchmarks and training data, how we work with the Neo Labs to do post training and how we serve these models in production. To start, you want to build a benchmark. If you don't have a good benchmark, you can't train models, and if you can't train models, you don't need to serve them in production.

**2:14** · So, this year we released three of these data sets that we built. We started by building Legal Agent Bench, which is a taxonomy of tasks that associates would do at a large law firm. And these cover multiple practice areas, and they're complex tasks like doing drafting complex fund formation documents, doing case law research, things like that.

### Legal Agent Bench, contracting, and the diligence dataset

**2:40** · We followed this up by building a contracting data set. This teaches This allows us to teach agents to do negotiation like you would in an in-house department. And then the one I'm most excited about that we recently released is a large diligence data set. This is, I think, one of the largest RL environments that's been released. The largest data rooms here are 80 million tokens, and it lets us do research on long context, very complex tasks.

**3:08** · And I think the most interesting thing about these data sets is how we built them.

**3:14** · One challenge we always had at Harvey for training models is we can't train on our customers' data. We work with the largest law firms and enterprises, and their legal data is incredibly sensitive. It's privileged, and so you can't put it in generic models. We can't even put it in our models. And so, how do you train models given that?

**3:36** · And the thing that started working really well this year is using domain experts to guide synthetic data generation.

**3:45** · And uh Brendan from Reka had a good analogy that the same way that engineers now don't write code, they vibe code and guide these coding models. We're starting to do the same thing. And so, my younger brother is actually a lawyer at Harvey, and he's gotten very good at using the coding models. He's trained our other lawyers to do that, and they can generate incredibly realistic data sets that we can use for training and also evaluating our product.

### Domain experts guiding synthetic data generation

**4:14** · And once you've done that, synthetic data isn't good enough, but it's a way to get started. And so, we work with companies like Mercor and Snorkel, who let you scale up this process and build larger sets particularly for training.

**4:33** · Once you've done that, you need to turn these data sets into efficient RL environments. It gets really expensive as these data sets get larger and evaluation gets very expensive. For example, in our diligence data set, we have over 1,000 unit tests that are grading model outputs using LLM as a judge. If you use the largest models and you want to do RL rollouts and things like this, it gets very expensive. And so, there's a lot of work, and here's some we did with LangChain, of making these very efficient.

**5:06** · And then the last thing we did that I think was a little controversial at the time, was open-sourcing some of these data sets. And the motivation for this was it's very hard to know your data set is good unless a lot of people train on it.

### Why Harvey open sourced its datasets

**5:23** · When I used to do research at Google Brain and DeepMind, the best data sets were open, like ImageNet, CIFAR, MNIST, and everyone used them, and you were able to find all of the issues, and we get a ton of pull requests, we get suggestions. Um and then I think increasingly we're having the labs when they report new models benchmark on our data set. And then most importantly, we had Elon retweet it.

**5:52** · So, once you've built the benchmark, now you have something to train models against. And the thing that is exciting now is open-source models are getting competitive. In the past, it wasn't worth doing post training because the models were improving so quickly from pre-training that any post training you did quickly got absorbed by the next pre-trained model.

**6:15** · But now with models like Kimmy 3, GLM 5.2, NeMo-Megatron, Inkling, and others, it's possible to take these very strong open-source base models and post train them to levels of frontier intelligence. Maybe not general frontier intelligence, but if you have a specific task like us, they are competitive. And so, the way we recommend getting started is working with the NeMo labs.

**6:41** · They have a bunch of expertise and infrastructure already in place to help you make sure that your training data sets are good. They have recipes. And usually, if you work with them and you're not able to get better results, there's probably something you're doing wrong with your data set, and this is a very good way to bootstrap it.

### Working with the neo labs — and why more than one

**7:01** · And so, some of the interesting work we did with these different providers, um Fireworks, we got some very interesting results training GLM 5.1 to use Fable or maybe Opus 4.8 as an advisor model. Um Base 10, we did some interesting work on KB compaction. N gram, who I think is here, we're doing interesting work on enterprise search and firm knowledge.

**7:26** · Trajectory, um we worked with them to train NeMo-Megatron models. And Applied Compute, we're doing some interesting work on our Vault product.

**7:34** · And I think one question we got is why work with multiple NeMo labs. Why not just pick one?

**7:41** · And for us, as we're scaling the research lab, we have more research projects than we have bandwidth to do internally or just with a single Neo lab. And every Neo lab is taking a different bet. They have different ways they think about research. We have different open source models we want to train. And the more we work with, the more we learn.

**8:04** · And it's getting easier than ever to do post training. So one, working with the Neo labs, we're learning a lot in partnership with them. And then we're doing more and more post training ourselves internally with APIs like Tinker and the infrastructure Fireworks and Base 10 have built. It's never been easier to post train these models and then serve them. And there's increasingly more post training talent that we're hiring and is available.

### Post-training in-house: building "Associate 1"

**8:29** · And inspired by Cursor, the goal of these efforts is for us to build our version of Composer one. How do we package all of the work we've done with synthetic data, scaling it with Mercor, the work with the Neo labs, into a model we can serve alongside the closed source models. Now, once you've post trained a model, you need to be able to serve it in production. And this is non-trivial.

**8:57** · So I want to start first by talking about our model serving infrastructure because I think sometimes people still think about application layer companies as you're calling a single model endpoint and it's maybe a chat product. And so a big problem we've solved over the past four years is we operate in 60 countries. We have multiple product surface areas. Customers have different model preferences.

**9:21** · And even with the closed just the closed source models, how do you serve these at scale?

**9:27** · And so this matrix gives you a sense of all of the things we need to handle when we're thinking about serving these models at scale. And as a simple example for each of these model families, we need to serve multiple of these models. We need to have fallbacks across providers to hit our SLAs. And now with companies like Fireworks.ai, we can add open-source models into this mix.

### The model serving matrix: 60 countries, fallbacks, SLAs

**9:54** · In order to think about when you serve models in production and how you modern them modern them in production, you need to have this infrastructure in place thinking of even before you think about post-training. And so this is how we think about when there's a new model released, whether it's open-source, closed-source, or a model we've post-trained, how we make decisions whether to put it in production. And then once it's in production, how we make decisions whether to keep it in production.

**10:21** · \[snorts\] And so pre-production, we have a set of generic evals. So in terms of automated, we have the lab benchmark that I talked about where whenever a new model comes out, this gives us a very quick sense of is it a frontier model, how strong is it, what areas of legal is it good. We have human testing in the generic case where we run side-by-sides of this model with other models to compare them.

**10:47** · And then for every product surface, we have critical user journeys and automated product tests because a model could be very good generically, but it could not be a good fit for a specific product surface.

**10:59** · And then we also have human product testing. And together these signals along with heuristics around cost, latency, region availability is how we decide whether we put a model into production. And I think the important point here is this is the case for post-trained models or non-post-trained models. And so you can reuse this infrastructure and you should have it in place before you think about post-training.

### Deciding what stays in production

**11:24** · Once a model's in production, same thing, doesn't matter if the model's post-trained or not. We do AB testing if we're rolling out a large change, we look at engagement to track if this model's performing how we expect. Um and then we look at things like uptime, token efficiency, and then we call it product feedback, I call it angry customer emails. And so there's There's all of these signals that tell you this is working as expected.

**11:50** · And so you need that infrastructure in place before you think about serving models. And then the thing you need to do even still before serving models is what I call the simple open-source switches.

**12:04** · And so the first one is look at all the places you're serving models and find are there places in my product where I can just naively swap open-source models? And so for example, we have parts of our product that generate citations that don't need the largest models and there's opportunities to swap in GLM 5.2 and get cost or performance benefits. And so that's the first thing and doing this builds the muscle of serving open-source models alongside closed-source models.

### Simple open source switches and model routing

**12:34** · And then the second which has gotten uh very popular now is model routing. So there could be places where you can't naively swap an open-source model, but what you can do is on certain queries route to open-source models. And then once you've done this, you have everything in place to start building the post-training flywheel.

**12:56** · And once you start serving them in production and collecting feedback, and caveat here, you need to be very careful about what collecting feedback means. In our case, it does not mean training on customer data, but we do get feedback signals from our user testing and other things that can inform how we build future data sets and improve these models. And that is our playbook for building a research lab.

**13:24** · We think in the future every AI comp- every company is going to need to become an AI company and figure out some version of this playbook. And I think despite that, most people are still betting against this playbook and application layer companies and the frontier ecosystem. But But if we win on our budget with this team we'll change the game.

### Moneyball: "If we win on this budget, we change the game"

**13:59** · This is a scene from Moneyball, which hopefully you've seen this movie, where they're talking about we just won 20 games in a row. And Billy Beane says, "It doesn't matter. If we don't win the championship, no one's going to appreciate what we've done here." And the quote is, "But if we win on this budget with this team we'll have changed the game."

**14:25** · And I think now with the frontier ecosystem all of you have the opportunity to do the same. Go change the game.

**14:34** · Thank you.

**14:36** · \[applause\] Do you want to do Q&amp;A?

**14:44** · You okay with that?

**14:45** · Yeah, of course.

**14:46** · \[snorts\] Yeah.

**14:49** · I'm sorry, who's speaking? Um you talked about the challenges with having uh legal customers with very sensitive data sets and talked a little bit about your brother's lawyer and other in-house experts doing their version of live coding to produce the best work. What does that look Can you give us a little more detail about what that actually looks like?

### Q&A: Training with sensitive data

**15:06** · Yeah, great question. So the biggest challenge with legal work is when you're at a large law firm, the type of work you're doing is, for example, you're representing a company doing an M&amp;A. And you get a data room, which is all the contracts of the company you're trying to acquire, plus there's all these emails and meetings about the negotiation.

**15:27** · None of that data is public, and so you don't have this analogy of like open source GitHub repos. And the biggest challenge you run into when training is you can maybe find some of the final work product publicly, so like a public purchase agreement, but you don't have any of the input data.

**15:43** · And historically it was very awkward to get a bunch of lawyers and say, "Hey, make a fake data room." Because these data rooms can be 10,000 contracts. They all need to fit together.

**15:55** · And so what Julio figured out is a very clever way to generate these data sets. And so he started from the rubric, and so he planted all these issues and said, "Here's all the problems in the data room and what I'm going to check for in a scenario, and then use that to generate the data room, so you can plant all of these issues like these contracts don't tie together, this contract's missing, and generate all of the data,

**16:21** · and then we'll use Mercor Shenorcal to make all the contracts look realistic, but now you have this input data set, and you can have the model generate like a diligence memo, and this way of checking it to say, "Hey, did you catch all of these issues that we know that are in here because we planted them?"

**16:36** · And obviously, depending on the work you're doing, you need to be clever of how you create it, but that to me feels like the really big unlock because now we can start doing this training that before you just you had this chicken-and-egg problem where we'd go to law firms and say, "Hey, we can train you this model on this client data." And they'd be like, "Okay, prove it." And we were like, "Show us the data." And they're like, "No." And so now you can prove it here.

**16:59** · And now we have a lot of interest from law firms saying, "Oh, this is really interesting. Can we do it with our data?"

**17:05** · Good question. Yeah.

**17:06** · Um so, we're also hiring for this.

**17:09** · We're also building an implied AI there.

**17:11** · Um from a hiring point of view, it's difficult for you to compete with researchers from Anthropic and and the labs.

### Q&A: Competing for research talent

**17:19** · Do you try and play that game or do you try and hire domain logic and lawyers and experience? And where has that worked and where has that not worked?

**17:26** · Yeah, I think this was one of the big mistakes I made like when we first started the company because I had worked in these labs and so I knew a lot of the folks and I would say, you know, come work with us and then they were getting these, you know, 100 million plus pay packages and we weren't at the scale where this made sense. And so I'd say we're now just getting to the company size where I would say we're not competing with kind of the frontier talent, but there is increasingly folks that are doing PhDs, folks that don't want to work at large labs and so I think that is changing.

**17:55** · And then I think the second thing is a lot of why you needed that talent early on was it wasn't just doing the post training, it was you need to build the training infrastructure, the serving infrastructure, and all of those things combined, I think the talent to do that was like very unique.

**18:14** · Like my old roommate was one of the folks who like ran post training at OpenAI and he was one of the best researchers I've ever worked with, but now you can use things like Fireworks, uh, tinker-like APIs, and so you don't need to build the training and serving infrastructure, and so I think it opens up the pool of talent and it feels very feasible to get some of this talent now.

**18:35** · Yeah.

**18:37** · Uh, yeah, just another question on the benchmark creation. So, when you're like creating these rubrics, you still have to create them in such a way that they're separating them the frontier models and you have to do that with the experts themselves. Like how do you find like navigating that challenge? So, the experts kind of have to create this rubric knowing or like trying to figure out how the models are going to perform on them.

### Q&A: Designing rubrics that actually challenge frontier models

**18:54** · So, the What do you mean separating the Uh, I guess so, you have to create the rubrics that can adequately separate separate the front They they have to challenge the the frontier, right?

**19:03** · Yep.

**19:04** · Um, I guess how do you navigate that especially when you're like having these in-house legal experts who might not exactly know how to create that rubric designed for a model.

**19:12** · Yeah, that's a good So, we think of it more as how do we make them realistic representations of the work our customers are doing? And I think part of why we picked the legal domain is if you just build a realistic client matter that these top firms are working on, like the frontier model still can't do this.

**19:31** · And I think the thing over the past 4 years we've built is So, for example, my brother was one of our first hires. And so, he's been working with the models for 4 years. And so, his intuition of how the models work, how to generate these data sets is incredibly good. And he's trained a bunch of lawyers to do this. But I would say the focus is still more of how do we build a really realistic data room, and then rubrics for the diligence. And then when we run these models, we find, okay, there's gaps and there's there's room for improvement. But I think depends on the domain.

**20:03** · Uh God.

**20:04** · Hey, uh Shadeen from Box.

**20:06** · Uh sorry, let me do that one and I'll Great.

**20:08** · I mean, if you think Great talk, by the way. Um Ross from Trolysis. If you think of the uh your you know, the the end-to-end motion is like data generation, the environment piece, then there is the algorithm piece of like what how do we train, etc., the research piece, and then there's the infra piece.

### Q&A: Where the pipeline breaks — data, research, or infra

**20:25** · If something is not working, like anecdotally, what have you seen? Is it like operationally or dollar-wise or human hours-wise, is it usually in the data layer? Is it in the research layer? Or is it in the infra layer? And how do you go from there?

**20:40** · Who's orchestrating or debugging this whole end-to-end pipeline in some ways?

**20:44** · Yeah, this is This is a great question. I mean, this is a whole 'nother talk. Um I don't think there's a single thing. So, I would say what makes it easier for us is we found product-market fit. We have a product that's being used in production. And we did this largely with the closed-source models to start.

**21:08** · And so, that let us build a lot of this kind of confidence in the thing is working end-to-end. And so, we have a product, people are using it, people have been using it for many years. The models work in this way, we can monitor whether they're working in production. So, that was kind of the point of serving of you need a lot of this in place.

**21:27** · And then, we have built the muscle of new models come out, how do we put those into the product, whether they're closed-source or open-source models.

**21:36** · And so, that's you can kind of think about the full cycle. And then, obviously we've done a bunch of work of like Harness engineering and context management and all of these things. And so, now you can think of post-training as one small input into this broader system. And so, we have our team post-train a model, and then you feed it into this broader system of, you know, you treat it just as another new model.

**21:58** · And so, then you have all these signals of, you know, what's going wrong. And so, I would say, but across these steps, there's kind of easy ways to gate it.

**22:08** · So, if you start with the benchmarks and you post-train a model and it doesn't work well on those, then it's unlikely to go farther. If it works well on that, and then you put in a product, but someone uses the product and they say things feel weird because, for example, on the benchmarks we've built, there is still things that they definitely don't catch. Like, the best example is you can have a model that does very well on our benchmarks, but they've overfit to some degree, and then you put it in a more generic assistant-like product, and it kind of falls apart for when you go out of distribution.

**22:38** · But, yeah, you need to have kind of all of the like stages and gates in place, and then it kind of becomes obvious where things are breaking. But, good question.

**22:48** · Yeah.

**22:50** · Oh, I had a question. Hey, great to meet you. I'm from Rocks.

**22:53** · Uh on the on the benchmark side, legal agent, I think you guys had Big Law before, Big Law bench, and then now legal agent of What's your philosophy on open sourcing the benchmark? Because if you open source, of course you're getting traction with other people trying out the benchmark, but the labs can help climb as well. And then if you close source, then there's a question of is this a real benchmark? So how do you how do you how do you how do you what's your philosophy?

### Q&A: The tension in open sourcing a benchmark

**23:17** · I I think that's like a good tension that we think about. I would say even before we open source this benchmark, we already work closely with the labs. And so we share data with them to help them improve their models, which improved our product.

**23:30** · And so I would say the way we think about it is there is a huge advantage in your industry, particularly in legal, in terms of helping our customers understand how good different models are at different things. And so I think when we when I started Harvey I kind of had the intuition of oh, we'll just build the best model and then customers will be happy because it's the best.

**23:56** · And it's very clear now that every customer has different preferences, different models are good at different things. And then I think the second that I didn't anticipate is kind of how big the frontier ecosystem would become. And so now we have so many companies reaching out saying, "Hey, we have this new technique or we did this thing. Can we try it?" And before we just didn't have the bandwidth where we're just like we're working on these other things. But now with this open source data set we could be we can say, "Hey, go try this and if it works, then great. This is something that's interesting to invest in."

**24:26** · Um and then I think the way we think about it strategically is the valuable data for us is going to be helping law firms train their own systems and how they work on private data. And then we want to help everyone improve these systems with synthetic data and kind of some of the data we open source, but obviously a balance for the reasons that you mentioned.

**24:49** · Yeah.

**24:51** · You mentioned finding a lab.

**24:53** · What are the remaining open questions for for that you want help on?

**24:57** · Yeah, that's a great question.

**24:58** · Um I would say one big challenge, one of the biggest challenges so we can generate these very realistic synthetic data sets, we can augment them with humans, but the distribution of that data still doesn't match our production distribution. And so I would say these data sets we're generating are somewhat future facing. And so what I mean by that is we can generate a really realistic data room, but right now our our product isn't used purely to do a due diligence.

### Q&A: Biggest remaining open problems

**25:26** · And so if a model does well on that, but then someone uses it to draft an email, maybe it doesn't work as well. And so I think there's still that gap because we can't look at customer data, and so how do you like bridge that gap? So I think that's to me that that's the biggest question on the data set side, and that one that one is challenging.

**25:44** · There is I think there is a bunch of questions around for example, again with the diligence data, like the largest data room is 80 million tokens of context. Like the models don't do a good job of managing this context, and how do you train these models to operate in kind of these very complex environments? So I think that's another one of just there's still a big performance gap.

**26:07** · Um and I would say the third is like we're making good progress on how do we post train our post train models ourselves, but I think figuring out some form of continual learning is I think the end game here is not for us to build the best legal model. It's for us to help every law firm or enterprise customer customize it to the type of work they're doing.

**26:29** · And so just thinking about how do you operationalize that, where you have a large law firm and every time they work on a client matter, their AI system gets better, but you're also protecting the client data. I think that's kind of one huge like both technical, operational, and like AI challenge that that is super interesting.

**26:49** · Yeah.

**26:50** · Uh We're done.

**26:52** · Or more? I can do more. I can Uh yeah, maybe last one.

**26:57** · Yeah.

**26:57** · So, you know, you talked a lot about like, you know, the the the foundation readiness, right, to compete with Front Row Live, right, including your open source model, including your infrastructure kind of like Ruby.

**27:08** · From product perspective, right, Coda as cloud product, they're general product, right? So, from product perspective, how do you guys compete with the, you know, Coda as cloud workflow, methodology, efficiency? How do you think about that?

### Q&A: Competing with horizontal products

**27:23** · Yeah.

**27:23** · I think the big shift that we're thinking about is like our original product and then things like Coda's Coda Work are very individual-focused products, and so they're about individual productivity.

**27:38** · And increasingly, the product we're building is about organizational productivity. And so, if you think of a large law firm, the problem they're trying to solve is not how do I make my individual lawyers more productive. The problem they're trying to solve is I have 10,000 clients. I'm working on client projects for all of them. I need to make sure that all those client projects go very well, and then I can also do them in a way that's profitable. And so, a lot of the infrastructure we're building for the law firms is how do you operate that machine?

**28:08** · And when you start thinking about an individual client project, most of the challenge is not how do I draft this one section. It's I'm working on this project for 6 months. I have a team of 20, 30 people across the firm. I need to coordinate all of them. I need to make sure that I'm coordinating all the outside parties. And so, a lot of it is starting to look like project management that is orchestrating these humans and these agents. And that's at the, I would say, at the team level.

**28:36** · And then, if you think about it at the organization level, now you have a thousand of these projects, and you need to start thinking about resource allocation, what am I billing, what am I pitching? And then with enterprises, it's even more complicated where kind of a Fortune 500, they're working with a thousand law firms. They have a thousand people internally. What are all the systems to kind of start work is trading that work?

**28:59** · And so I would say the simple answer is just, and this is I think historically what enterprise has has done is how do you just go hyper vertical into your domain in a way that the horizontal products won't. Yeah, good question.

**29:13** · Thank you, Gabe. That was an iconic talk. Thank you for joining us.

**29:17** · \[applause\]
