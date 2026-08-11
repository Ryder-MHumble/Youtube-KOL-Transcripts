---
title: "Chai Discovery's Bitter Lesson: Drug Design Is Another Scaling Problem"
source: "https://www.youtube.com/watch?v=wv53mDmY-k0"
author:
  - "[[Sequoia Capital]]"
published: 2026-08-04
created: 2026-08-10
description: "Most people treat biology as a bespoke, messy science. Josh Meier and Matt McPartlon, co-founders of Chai Discovery, treat it as an engineering problem. They make the case that drug design obeys the b"
analysis_report: "[[Sequoia Capital- Chai Discovery's Bitter Lesson Drug Design Is Another Scaling Problem 分析]]"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=wv53mDmY-k0)

Most people treat biology as a bespoke, messy science. Josh Meier and Matt McPartlon, co-founders of Chai Discovery, treat it as an engineering problem. They make the case that drug design obeys the bitter lesson: scale data, models, and compute, and the model can learn what a hand-built pipeline simply couldn't capture. The results are concrete: Chai-2 pushed de novo antibody design from a sub 0.1% hit rate to 16%, turning a needle-in-a-haystack search into something more like designing a key to fit a lock. Josh argues, counterintuitively, that biology is more verifiable than code, and explains why the goal should be more lab experiments, not fewer. Their bet: a design suite that collapses drug discovery from nine months to nine days, and arms the pharma industry rather than competing with it.  
  
Hosted by Pat Grady and Sonali Singh, Sequoia Capital  
  
00:00 Introduction  
01:52 From Discovery to Design  
03:25 Protein AI Breakthroughs Timeline  
06:04 Why Start in 2024  
10:13 Diffusion Models Intuition  
11:41 Building the Avengers Team  
15:22 Hit Rates and Scaling Laws  
25:01 Molecular CAD Vision  
25:24 Faster Design Loops  
26:32 Future Drug Discovery  
28:37 Platform Business Model  
31:14 Partnering Reality Check  
33:44 Data Flywheel Explained  
37:16 Staying Ahead at Scale  
39:44 Culture and What's Next

## Transcript

### Introduction

**0:00** · One of our big guiding principles is just simplicity. Um so like when you look at a model like let's say a Chai 1, I think there are 23 distinct submodules in Chai 1. Um and like when you're trying to iterate on something like that, it gets really hard cuz you're like I kind of I need to understand each of these submodules independently. I need to understand all of their behaviors, their dynamics, and like that doesn't actually scale that well. Um so like you can start to think, okay, how do I simplify this? How do I identify like what's what's really important? And once you have that like kind of the whole research process and like identifying these types of scaling directions uh becomes a lot simpler.

**0:33** · \[music\] We're here with Josh and Matt, two of the co-founders of Chai Discovery. Chai is engineering molecules with AI. So it's something of a foundation model lab for biology. Sounds like a big idea, but let me just start there. What is the big idea?

**1:04** · Thanks for having us on on the show. Um one of the exciting things we're trying to do at Chai is to make the drug discovery process like a little bit more like engineering. And we've seen all the work happening with LLMs for code generation for instance, right? And that works really well because code's a very simple abstraction, right? Of like to to kind of get across what you want to do.

**1:23** · Uh biology doesn't look like that today. It's a lot of like trial and error. Um I think if we go back to uh the early days of uh of just like modern biotech, right? A lot of the medicines that we have today were kind of discovered quite randomly. It was a bit serendipitous.

**1:36** · And what we're trying to do is allow us to industrialize that process a little bit more uh and try to come up with the tools that we'd need in order to have abstraction layers the same way we have that in code and in modern engineering allows us to iterate really quickly and try to bring that uh into into biology and into drug discovery.

### From Discovery to Design

**1:52** · So So let me ask you a question on that then. So there's And tell me if this is a reasonable way to frame it. There's almost this boundary between that which can be engineered and that which needs to be tested in the real world.

**2:04** · And it feels like that boundary has been moving over time. Like the the the proportion of the drug development process that can be engineered as opposed to trial and error'd seems to be increasing. Is that a reasonable way to think about it? If so, can you talk about like what specific developments have pushed that boundary over time?

**2:22** · I think that's one way to think about it. Um the way that we often uh look at this is like the lab is is an important part to to verify that what you're doing is correct. And actually verification is a very big theme in AI as well. If you can evaluate that your model works, you can verify it, then you can start to hill climb that and you can make progress on it. So I think the lab is a very important part of this. And then the question is how do we take drug discovery and make it look a lot more like drug design. So one of the reasons why we call this field drug discovery is we're often looking for a needle in a haystack. We'll screen millions, billions of molecules try to find one that works.

**2:52** · And if we can instead put in what is like the dream state of the molecule you want and then the model can materialize that, that's going to be really powerful. So it's not even a question of like reducing lab testing. I mean, maybe that happens as a result. I actually might even take the opposite side of the coin and we can talk about that where maybe we'd actually do even more lab testing cuz the ROI will increase. The same way there's more software engineers or there's more demand for software engineers now that they become more productive, there might be more demand for the lab.

**3:18** · But I think the key part is how do we just change the paradigm here and how do we we make it more design oriented?

**3:24** · Mhm.

### Protein AI Breakthroughs Timeline

**3:25** · Can we talk about what is state of the art today?

**3:29** · And then maybe let's take a little trip down memory lane. 5 years ago, 3 years ago, 1 year ago. Like what have been some of the major breakthroughs and like how has state of the art changed over the recent years?

**3:40** · Yeah, I think the the field has like it's really evolved especially like over the last decade. Um so it really wasn't until like uh you can actually look back. There's like this bi-annual protein folding competition. So every 2 years uh usually a bunch of academic groups would compete in this protein folding competition. What would happen is like you kind of hold out these protein targets that no one's ever seen before.

**4:01** · They never get deposited publicly. And then all these groups compete so you can predict the proteins the best. And like really it wasn't until 2018 where you started to see this like big step change in in performance and then finally again in like 2020 with AlphaFold 2. But really like it was kind of like the advent of deep learning that really like kicked off this whole field. Um so at first what you do these are kind of like bring me back to my original days in my advisor's lab. So we worked on like one of the first systems to do this with deep learning.

**4:30** · What we would try to do is predict like the distances between amino acids in a protein. And then we'd have some render which then took in like these kind of noisy incomplete looking distances and then emitted some protein from that. Um and what's pretty remarkable is that with relatively minimal information like you could build a machine learning system that could actually produce something that really looks like a protein and for the most part was was correct. Like there are still pretty big gaps it didn't quite have the resolution of like what what we have today.

**4:57** · Almost like with the early image generation models where it was like a little bit grainy a little bit blurry and now it's like oh my gosh like this is this is crazy high definition images like in seconds. Uh so we kind of like saw that same evolution happen over time. So it started with protein folding and then I guess once that became more realizable there were kind of these other sub problems that people wanted to solve. So now given a protein structure can I design say like a sequence which might fold to that? And that's getting closer and closer to like the drug design problem.

**5:27** · So you're you're kind of like now thinking okay how do I start engineering proteins that like match a certain shape or might perform a specific function?

**5:36** · And so people kind of study that problem independently and that was kind of like 2021 2022 time. And then kind of these ideas began to merge together. It was really like the advent of diffusion models where we started to be able to like, "Okay, I can now generate a protein structure and a sequence kind of simultaneously.

**5:52** · Um and I can start making these like what we would call prompts more and more realistic." So, I can now prompt these models on a target that might have a certain shape and I can say, "Hey, I want to bind over here." Kind of like add add more real-world constraints on the problem.

### Why Start in 2024

**6:04** · What did you guys see in 2024 that made you think that was the right time to start the company?

**6:09** · Yeah, there were a lot of discussions that went into it. I remember one of these uh early discussions actually back in Matt's house when we were uh you know, Matt was was showing me some of these results on like antibody antigen like structure prediction. And we Matt was just talking about protein folding.

**6:23** · Um but for for a long time people thought that protein folding for antibodies was just like too hard of a problem. People were like there was not enough data for for any in antibodies like in the protein data bank for instance to like solve this problem. And people as a result thought that like antibody design was going to be out of reach. A lot of the work that people even did on protein design in the early days with deep learning, it wasn't antibodies. It was uh these different class of proteins called mini proteins, um which are uh actually really interesting in their own right, but they're not what most of the uh drug industry is is looking at.

**6:50** · So, the holy grail was whether we could design antibody proteins on the computer, especially ones that had all that therapeutic function. And our thinking was that if you couldn't predict what an antibody looks like, how are you ever going to design one?

**7:03** · Traditionally, people have thought like like biology is scary. Um like there's so much to know.

**7:08** · of biology.

**7:09** · I I am as well. Honestly, \[laughter\] like uh like my my background was was never biology. I I studied like pure math and started my PhD in uh theoretical computer science. And it was only like after my third year that I ended up switching into like deep learning, protein structure prediction, all of this stuff. So, it was like totally new field to me. Seemed insane, but like at the end of the day, it's much simpler and like the the problems are much more like interconnected uh than one might think. So, like I think people like when they start getting into the field, they're like, "Oh man, what's an antibody? What's a mini protein? What are These are all just like sequences of amino acids."

**7:40** · At the end of the day, like these are just like different types of prompts for the model. Um but like in the same way where you might like have a math problem that goes into chat GBT, chat GBT can both answer your math math problem and like help you with your English homework. Uh so like really we we have the same type of thing going on with our models. Like we just have some way of representing these sequences of amino acids, then we have a way of like designing, predicting those as well. Um and I think like in that lens, like things things become a lot more clear.

**8:09** · And Matt, you mentioned your background a little bit. Um Josh, talk a bit about your background and then more broadly, in order to pull this off, you have a bunch of different disciplines that kind of come together. So can you just talk a bit about like your background and that of some of the other core members of the team and how these things all fit together?

**8:25** · Yeah, I've been excited about AI and biology uh since I was a kid. So I guess I'm like Matt Matt, I didn't start with like theoretical CS and get into that way, but um I went to a high school with a stem cell lab. So I was just always excited about biology as a kid and I grew up as a programmer. Um I uh I really started my career at Open AI, so it was on on the early team there. It was a non-profit back then. So it was a a pretty uh good time to be there. We did GPT-1, GPT-2, scaling laws.

**8:48** · Um and it was uh the question was like if the models can learn to speak English, German, French, why can't they learn to speak DNA and protein? Um and that was kind of my research agenda since then. I think that sort of intersects with around the time like Matt got into the field as well. And it was a uh I think it was a pretty important time as well, right? Because if you look at the kind of methods that we were bringing in, like there's been a lot of these, you know, changes on the edges if you will, right? And you know, Matt talked a bit about the history of what's happened in the fields here.

**9:18** · Um but you know, it's all about like how do we find like the right deep learning architectures with the right compute configuration and the right model architectures this happen.

**9:27** · What are the right tasks to apply it to?

**9:29** · We're talking about how we even knew that like, you know, 2024 is the right time to start the company. As Matt was saying, you know, these are all different like kinds of amino acid sequences and people thought that, you know, antibody class of of problem was going to be too hard and we started to see the first signs of life that actually this was starting to work. I think a lot of it fueled by some of the new architectures we're bringing to the problems. I think it was diffusion models back then.

**9:51** · The first time like anyone was able to generate reasonable looking proteins was the advent like of diffusion models.

**9:59** · So it was pretty crazy like there were a bunch of generative modeling approaches that like would kind of work if you if you had a bunch of data. So like people got these working for images. There were like a bunch of tricks to make this better and better along the way. Like we've definitely borrowed a lot of those ideas in our domain as well.

### Diffusion Models Intuition

**10:13** · But it was really like once diffusion models came around And is there is there an intuition for why diffusion models work?

**10:19** · Yeah, so diffusion is is not a one-step process. So like I think kind of up until this point like the the main generative design paradigm was like called variational autoencoders. And in that case you're like saying I want to just like compress my input distribution. So like you you have some like proteins you want to make these look like kind of like fuzzy Gaussian vectors. That task is just like really hard. And maybe today if we tried like super hard I think we'd crack it.

**10:45** · But at the time like I I think like it wasn't really as developed enough to to work for our problems. What turned out working really well was just kind of giving the model more time to think and showing it like more examples like here's like a slightly broken looking protein. How do you make it better? And you can kind of break that protein more and more and more and you can make it look more and more noisy, more and more broken and teach the model just quick little shortcuts. All right, here's how I make it slightly better. You can just keep asking over and over again. Make it slightly better. Make it slightly better.

**11:14** · And kind of like breaking the problem down to that scale worked really really well for for biology.

**11:20** · Yeah, the make it slightly better reminds me of a game that I like to play with my daughters where we have chat GPT give us a unicorn and then we make it stronger. And we just keep telling it to make it stronger. And by the time we're done we have the strongest unicorn in the world. So, about the same, right?

**11:35** · Yeah. That's uh \[laughter\] It's that easy.

**11:38** · Yeah.

**11:39** · Okay, maybe not the same.

**11:40** · Yeah.

**11:40** · So, we feel like in this domain, you need to assemble a kind of like a quadrilingual group of people, like an Avengers squad of chemistry people, biologists, AI folks. And so, that's a challenge. Um how have you guys gone about finding people, convincing people to join the team, and and who are your superstars?

### Building the Avengers Team

**11:58** · So, we've been really pragmatic about this at Character. If you look at the founding team, it was mostly AI researchers. Um so, people who had uh worked on either scaling models or getting them to work in this domain.

**12:09** · But, really with each generation of model, uh the kind of people we've needed for the next milestone has has changed. Uh or or I'd say probably has expanded, right? Uh so, if you look at Character 2, right? That's the point when we started to bring in um some of the most incredible like, you know, antibody engineers and and scientists in the world. Um uh one of the scientists from Andy Andy Young Actually, when we hired him, uh people asked us if we had pivoted into building a full-stack drug pipeline cuz they're like, "You'd be crazy not \[laughter\] to do that if like Andy joined your team."

**12:35** · Um but, uh I think Andy has has enjoyed running more antibody campaigns in the past couple of months than he's probably run in his whole whole career, uh which is very cool to see. You have folks like Nathan Rollins on the team. Like, Nathan was actually homeschooled and then started college very early on. So, he joined like David Baker's lab who won the Nobel Prize for protein design like when he was 14, uh started his PhD when he was 18, and has so many creative ideas.

**12:56** · On our uh as the model started to get better, we needed to build up a product team uh because while the researchers might get the models to point that they're uh they're very powerful, you need to build the right product interfaces so that the models are actually useful. Um and uh that's where we started to bring on uh people who have, you know, built some of the most exciting products we know about today.

**13:17** · Uh like our co-founder Jack worked at Stripe, Monaz who was one of the top 10 code contributors at Stripe, uh Neil who ran his own cybersecurity company before security started to become very important as we deploy this to our big partners. As as we started to scale up, we brought in people uh who've uh really done a lot of like the GPU hacking, if you will, in order to like scale up our systems that they they they don't break when we're running them at scale. We had an email from uh or a Slack message from one of our hyperscalers the other day uh where you know we had a cluster, I think that had some issue to it and they're like, "Oh, like the GPUs got too hot. I think you guys are running too many."

**13:47** · And we're like, "Isn't that the point?" Right?

**13:50** · That's probably I was like, "Good, we're doing our job at least." Yeah, so like how do you convince those people to join? I think again a lot of it comes back to uh the results and like a clear need. We didn't hire antibody engineers before in an antibody design model. Like what are those folks going to do? We were even I think worried when we started that trend because for some of the um next generation formats, the complicated antibodies, like multispecifics, like they didn't even work with Chai too. Uh so it actually took a couple of of uh weeks when some of those people showed up before the models could work at a point that they could work on some of these interesting case studies.

**14:18** · Uh but fortunately progress is fast enough to kind of bring that online. So I think we're always like evolving that team and going forward you know, that next milestone. We've got the team very small as a result, too. Um so this way, you know, everyone is a little bit like slightly over capacity, I think, which means we have to prioritize. It forces us to work on the things that really matter most.

**14:37** · I think on the research side as well, one of the founding engineers, Kevin Wu, he had the first uh I think it was the first protein diffusion model like ever. Uh and that speaks to Kevin's speed of execution.

**14:48** · Like he is a heck of an engineer and like I think engineering has just always been like important since day one. Um so like really even our researchers, they're all excellent engineers and like we really care about building a high-quality codebase. Like at the end of the day, we are technically like a software company.

**15:05** · We're we're AI researchers, we're we're protein designers, we're we're a lot of things, but uh our deliverable is some piece of software. So we've kept that like kept that bar really high while also trying to like, you know, level that with great research talent and people that can actually like push the frontiers of what's possible.

### Hit Rates and Scaling Laws

**15:22** · And you've had a number of it seems like aha moments in the field. Like AlphaFold was an aha, we can figure out how a protein folds. And then the diffusion models, aha, like we can generate proteins. Um and it seems like your latest models are a kind of another aha moment. We're not only generating molecules that look like proteins, but they also have therapeutic properties. Like they can bind really tightly.

**15:44** · Um they have really high hit rates. Can you talk sort of about the quality of the molecules that your models are producing now and everything that sort of went in to those models to make them able to do that?

**15:53** · Yeah, if we look at the the quality of the molecules that's coming out, it goes back to, you know, one of the thesis when we started the company that uh we really wanted to focus in on this like de novo generation of the molecules. If you look at what a lot of the drug discovery AI work was at the time, it was about how do I take a molecule and just make it a little bit better, right?

**16:11** · Which we just talked about in a sense, but it was doing it with a lab in the loop uh style, right? Where I take some data, try to make it better that way.

**16:18** · And the the question uh we started with is, well, can we actually just like do all that on the computer, right? Is there a way that the there maybe there would be enough data or we could collect enough data um so that we could just zero-shot a molecule that has a lot of these properties? So, the first thing we needed to do to get there um was to design molecules with really high success rates. When we started the company, the state of the art for anybody design was about like a 0.1% binding rate. So, one in a thousand of the molecules you design would actually bind in the lab. Um so, first of all, that means you have to screen a lot of molecules to find some good ones.

**16:49** · It also means that like the gradient you get on your process is actually quite weak as well. So, for many targets you won't get any hits. For the ones that, you know, you do get some hits, you won't have enough to actually see whether you're having like the drug-like properties. So, we really focused in on how do we just make this process more accurate? We got to uh with our chi-2 model about like a 15% success rate. Uh so, now if you screen a a thousand molecules, you're getting 150 back. Now, you can get start to get some like interesting statistics on the properties of the molecules, right? And a lot of allowed us to like iterate on that, build the right evaluations around that in the lab, and really try to hill climb that as well.

**17:21** · And we're getting to a point now where we can actually bake in a lot of these different properties from the start into this engine. And then maybe if you think about, you know, how does this happen or like how are we approaching this as well? And like why do we think it's going to continue improving?

**17:34** · Yeah, so like um honestly, I think Josh and I were both surprised at how quickly this worked. Um like when we were originally budging this, we're like, "Ah, maybe like 20% hit rate like 3 or 4 years." We're like really like a 1% rate. We thought 1 in 100 would be amazing. We're like, "This is going to be you know, a groundbreaking thing." We had a philosophy and like an approach that we wanted to take and it just like ended up working really well. And that approach is like very similar to what's worked in the rest of machine learning.

**18:00** · So, people kind of treat biology as this like bespoke problem or like bespoke field, but really it's like the same principles as like self-driving LLMs.

**18:07** · Well, same principles, but one of the things we've talked about before is how you managed to find scaling laws. And it's one thing to tokenize a string of text. It's another thing to tokenize biology.

**18:19** · Can you say a couple words about without giving away any of the magic, you know, can you just say a couple words about that challenge and how you guys solve that?

**18:28** · Yeah, so one thing that I really like about Chai is like we're we're a very bitter lesson pill company. So, like we really believe in like scaling data, scaling models, scaling compute. In order to do that, obviously you you need to identify scaling laws. Otherwise, you're just kind of like wasting time and resources. Um and I think like without giving away too much, like one of our big guiding principles is just simplicity. Um so, like when you look at a model like let's say a Chai 1, um so like there are like I think there are 23 distinct submodules in Chai 1. Um and like when you're trying to iterate on something like that, it gets really hard.

**18:57** · Uh cuz you're like, I kind of need to understand each of these submodules independently. I need to understand all of their behaviors, their dynamics, and like that doesn't actually scale that well. Um so, like you can start to think, "Okay, how do I simplify this?

**19:09** · How do I identify I what's what's really important?" Um and once you have that like kind of the whole research process and like identifying these types of scaling directions uh becomes a lot simpler.

**19:18** · One of the other things too that I think is interesting about this is we take a lot of these lessons from what's worked in the rest of the deep learning space, but as you're pointing out like the data itself is different. Yeah. The models at Chai are completely built from scratch.

**19:29** · We're not like fine-tuning GLAM or something like that on some protein data. We build everything from the ground up. I think a lot of the company building process though is is taking a philosophy and actually sticking with it and iterating on that and just having some guiding principles. When you're building like a blue sky research company if you will, you know, Chai is is almost like one of these neo labs, right? Like we have this big AI problem we're going after where as we make progress on it, you know, that opens up opportunity for for our customers. Um, but if you're going to work on something so open-ended that way, you need some principles to guide you.

**19:57** · And I think we've done a very good job on like tracking those principles in the company, working on it. So a lot of the things that Matt Yeah, can you share them? What what are the guiding principles?

**20:05** · So I think simplicity was one of the ones that Matt mentioned. It's this like bitter lesson pillness of like, you know, scaling compute and data and and models. Uh, it's being really rigorous.

**20:14** · Uh, that's something that's so important in this space. You can fool yourself so easily in biology. Like the error bars in the wet lab are actually quite large as well. Um, so it's actually a little bit different than uh if you look at like code generation for instance. If you look at SWE bench, people are like, oh, I like this is a maybe like a year ago people like, oh, I got 16% and 17% and 18%. I mean, in biology if if you're like plus or minus 5% in your lab, like that's all that might all be the same.

**20:39** · So it actually just means uh the bar is really high in terms of the step changes that you want to see with the models, but you also need to be really honest with yourself about whether you're making progress or not. Um, so you could come up with some fancy model that looks like it works well on like one or two new tasks, but it's very important to show that that works more generally. Uh, if you're actually trying to build a product that can like bring the field forward.

**20:59** · Yeah, and that's I think pretty interesting because biology is one of those inherently not so verifiable domains. And you guys have been really good at um, sort of showing your progress to customers, um, and to people like us who know very little about biology. And so, can we talk a little bit about the evals and the verifiable part of of the model progress? Like, how do you guys know that your models are getting better?

**21:21** · Well, I would say first of all that, uh, I actually think this is one of the more verifiable domains. It's actually very objective readout. If you look at something even like CodeGen, right?

**21:30** · Like, maybe it's a verifiable task like, did my code compile? Did it solve these unit tests? But, how do you think about the taste, right? Like, did I write some really sloppy code that can't be maintained? Like, what does that look like? When we think about designing a molecule in the lab, uh, we can actually be quite specific about many of these properties, right? So, maybe we get a molecule that binds the target, but can I manufacture it, right? That might be your, you know, version of like some tech debt, but you can measure that. Uh, and I think those evals, again, actually make this domain more verifiable. Maybe it takes a little bit longer to validate it, right? It's not like five seconds to like get a readout and run a unit test.

**22:02** · You might have to spend a couple days, a couple weeks in the lab to get that readout, but at least you can be honest with yourself.

**22:07** · Yeah.

**22:07** · When we talk about progress and how good the models are, there's like a domain of targets in biology, um, that you can, as you mentioned, sort of address with traditional screening methods. They take a long time. They're very slow and rudimentary. Um, and then there are targets that just aren't addressable with the with existing methods. They're not druggable for whatever reason.

**22:26** · Um, and so, where are we in terms of model progress in terms of, you know, working on existing targets and generating molecules faster? That's one end of the spectrum. And on the other end of the spectrum is unlocking novel biology, new targets, and things that we couldn't drug before.

**22:40** · This kind of goes back to like, uh, kind of like our core modeling philosophy.

**22:44** · Um, so like, there there have actually been like plenty of times where like, man, if we had a 24th module, like we can actually like unlock that new target. Um, and we're like, is that really something that we want to maintain long term? Is this incremental or is this like actually a compounding improvement? Will this actually like help us generalize to the the class of like these this whole class of targets that we we really can't hit. And so like our our philosophy has been like, all right, let's just like continue to focus like identify your scaling laws.

**23:07** · Like there there comes a point where like if the model is able to push loss down even further, it has to understand like something like very intrinsic about the target that it's operating on. So like one example we were talking about the other day, Paul and I, maybe the way that we're looking at like certain glycosylation sites on proteins we're like, "Oh, we might want to represent them differently or something like this." And we're like, "Well, even if we didn't represent them, like there are certain sequence motifs that will tell the model like there should be a glycosylation site here. And in order to drive like loss down further, the model should just like have to learn that."

**23:38** · Uh so there are like all these hidden features of targets where like if you really believe in scaling laws you can believe the models will get there. Like these types of targets like should just unlock with better models. And of course like you still have to take this very seriously and like you still need all the proper validation. Um you need to like really challenge yourself and like make sure that this is truly working.

**23:59** · But I think our approach has always been like, you know, we with better models like we we should be able to unlock a lot of these targets.

**24:06** · One of the other interesting things is if we look at we talked about like the interdisciplinary nature of this. If we look at the different teams at Chai, what people will call hard target is actually different in literally every team. So on the science team it might be, you know, like a undruggable GPCR target no one's gotten something that has like, you know, modulated that in a functional way. On the ML research team it'll be something like, "Oh, there's like the the model just can't fold this thing up. It doesn't know what it looks like."

**24:30** · And then on the product team it might look like, "Oh, I've got all these like, you know, modifications like my glycosylations and it's a membrane protein. How do I represent that to the user?"

**24:38** · And actually the fact that it's different for each of these groups I think is a feature rather than a bug.

**24:42** · And it means that if we want to make like broad progress over here, everyone is kind of pushing in parallel on these different ways and and that means that there's very smooth progress that we can make all the time. And there's usually not one bottleneck at Chai. It's not like, "Oh, if we only had that one extra module things would work." Or if we only you know, like try to push this into the product in some way, we can unlock it.

### Molecular CAD Vision

**25:01** · We're trying to build this unified solution because at the end of the day, the goal of the company is to build a computer-aided design suite for molecules. It's not to make one or two molecules. It's not to get a pipeline of like five interesting therapies that we bring to market. It's to change the way that medicines are discovered. And we're if we're going to do that, we need to work on all the hard targets regardless of how you define hard.

**25:20** · Yeah. Say more about this idea of computer-aided design suite for molecules. What does that mean?

### Faster Design Loops

**25:24** · So at its core, it goes back to this point about making biology look more like an engineering discipline. So we're not going and fishing something out of a large library or doing a ton of trial and error. You want to be able to specify up front the principles that go into designing your molecule and then have an engine that can actually realize that into some molecule that we're going to go and create in the lab. And look, you still might do some iteration on the lab and and on your model because maybe your hypothesis was wrong. But we want to speed up is is actually again have that computer-aided design suite so that you can go from idea to testable hypothesis very quickly.

**25:56** · And if that loop right now takes something like 9 months, I don't know, to go and like discover your molecule versus if it takes 9 weeks or it takes 9 days, you know, each order of magnitude just scales in a very big way the number of ideas you can really sort through. And I think that's ultimately how the field is going to converge on on better medicines. It really comes back to like people sometimes talk about do we care and you kind of noted on it's not like do we care about like speed or do we care about like the difficulty of the targets?

**26:22** · At some point they converge in this way as well because a hard target if we can like iterate through hypothesis a lot faster, then maybe it'll be easier to crack it.

### Future Drug Discovery

**26:32** · If so if we can maybe detach ourselves from the present reality and go far enough into the future that we're not thinking present forward, we're actually thinking future back. 2035, 2040, 2100, whatever whatever you want. What does the industry look like? Like let's imagine that computer-aided design suite for molecules has become a standard.

**26:53** · Let's imagine a lot of innovation has flowed downstream into some of the wet lab parts of the process. Like, can you paint the picture of what the industry might look like 10 years from now?

**27:03** · Yeah, I think it's going to be a a really exciting time. And we can look at this on on a couple of angles. So, first of all, the quality of the medicines that we develop will hopefully go up.

**27:12** · There's a lot of molecules we put into the clinic today that there is really hard to discover a molecule. You find something that's like 80% of the way there. Maybe advance it anyways to like hit my timelines. It's probably going to benefit some patients. But then you get beat, you know, a year later by someone else. And it's it's really just not the most efficient spend of resources in the industry. You've got the kind of diseases that are just too hard to go after today. People have been trying to drug Alzheimer's forever. And unfortunately, you know, haven't made as much progress as as we'd like. You have things that just aren't economical to go after today.

**27:40** · Think about like personalized medicines, rare diseases, things where maybe the patient population is going to be smaller. But again, if we can iterate through these ideas faster, if we can launch something faster, if we can do it in a less expensive way, then those probably come into reach as well. So, I think there's just so many different axes that that we're able to to push on. And I think that means that the the future is is really bright.

**28:04** · It used to be like, you either want to be first in class or best in class. Now it's like, you want to be last in class cuz like you actually just want to like be the final answer.

**28:12** · So, I think like a lot of what you'll see is just like way more intentionality in the types of drugs that you're designing. Like, this drug will be super specific to the disease of interest. It won't have like certain interactions, like certain negative interactions that a lot of drugs today do. A lot of this stuff is actually like you're able to model most of this computationally.

**28:31** · Like, maybe not today, but there's definitely a path towards getting there. And I think that's like one of the most exciting things for me.

### Platform Business Model

**28:37** · Very cool. Can we talk about a business model decision that you guys made?

**28:41** · Cuz I think a lot of times folks think about Chai and Isomorphic in in same neighborhood. Isomorphic is developing drugs. You guys are enabling the existing industry to develop drugs more efficiently, better, faster, cheaper than they have before. Why did you decide to go down that path versus, you know, the Isomorphic path?

**29:00** · Yeah, first of all, I think both of these paths are are great and they can they can create tremendous value. We've always been really excited about building infrastructure for the industry. Our bet when we started to go back to those results in Matt's house, you know, a few years ago, was that this is how most future drugs are going to be discovered. And if that's the case, somebody needs to go and like build that infrastructure and make it happen. I think part of this too is a lot of our founding team, like including Matt and I, had worked in companies before where we had built these full-stack drug pipelines, right?

**29:29** · And we were building AI models. We're putting those drugs in the clinic.

**29:32** · Again, we're we're pretty bitter lesson pill as well and our our thinking was as the models get better, we want to be spending more of the money making better models as opposed to diverting those resources into clinical trials and things like that. And one of the interesting things about our business model is as the models get better, actually wins us the right to continue investing more in them, right? And you have, you know, partnerships with with these pharma companies that are that are paying off today and allows us to continue invest in it. So, it's it's a much more, you know, scalable business in that way. And I just think about the ultimate impact that we can create for the world is is a lot larger.

**30:01** · We've We've always wanted to just partner broadly with the ecosystem. It goes back to this point about fooling yourself in biology. If you work on a small number of drug targets, you might come up with the most exquisite molecules, creating a ton of value for the world by doing that. But, you might miss the forest for the trees because maybe your model doesn't generalize to the other 500 molecules that people are going to make that year.

**30:22** · And if you go and and partner with people, you just you just can't fool yourself. Like, you look at our partners, Eli Lilly, Novartis, Organics, Pfizer, like these are not companies that are, you know, they they take this stuff for granted.

**30:34** · Like, you have to really deliver on these partnerships for them to take you seriously. And that means it can't just work like some some time. Like, when we ship models at Chai, they really have to work, they have to deliver value to our partners, and it's not like, oh, we made some molecule, doesn't fully work, we're going to have our our chemists like clean it up a little bit. So, it's it's almost a harder business to pull off. I think that's one of the reasons why you haven't seen it pursued many times. If you work on a drug pipeline, again, like there might be ways to fix things up later. There will be the proof of like what happens in the clinic, of course.

**31:01** · Um but uh when you have this partnering based model, you have to be really rigorous about your models. Your models have to work really well because otherwise those partners not going to come easily. So, it's made our life harder, I think in many ways, but I think it's also the more rewarding path if we can get it to work.

### Partnering Reality Check

**31:15** · what have you learned? I mean, you know, you're you're out of the lab, so to speak, and in the real world, you know, delivering real value for actual pharma companies. What have you learned as you start to work with these partners in terms of any surprises in terms of how their needs might have differed from what you expected or how their level of sophistication around this might be different than what you expected. Have you any surprises or any learnings from working with these partners?

**31:35** · Yeah, so we went into these partnerships. I think a lot of people told us that like pharma doesn't know how to use AI, these are not it's not like a tech forward industry and things like that. And to be honest, that hasn't really been our experience. I think that these are again, they're very rigorous partners, very rigorous customers, right? And they're they're going to to to test every one of our claims, right, before they start to deploy these things. But when they see the data, they go all in, right? Because pharma is an innovation industry. Um and it's interesting just to think about even the whole economics of the pharma industry.

**32:04** · If you build a product in pharma, right?

**32:06** · Like like a drug, right? You only have exclusivity on that drug uh for a certain period of time, right? And you have to continue to reinvest. Eli Lilly is a trillion-dollar pharma company right now. If they don't get more blockbuster drugs, they will not be a trillion-dollar pharma company forever.

**32:20** · Um and I think that forces these companies to really be on their game of adopting new technologies and deploying them and trying to stay ahead. Pharma is a very competitive arena. There's a lot of people trying to bring these drugs to patients with By the way, it's great great for patients, but uh it means that you have to be on top of your game here.

**32:37** · Uh and I think that means that um you know, once you're through that door and your models are working, we've seen like an an upscale this adoption very quickly and people thinking about how to use the models in incredibly creative ways.

**32:47** · I really like the incentive structure that it creates as well. Um like taking more of the partnership model. As our models get better, we get better results to our customers and so on. Um so I think like that's just like a nice like nice side effect for us as well. Chai has been like incredibly focused. Um and like really as the models get better, you can kind of like iterate on a better model with better data and so on. So like a lot of what we see and like a lot of what our partners are using the model for like generating, you know, binders, antibodies, so on. Like we're also like doing a lot of dog fooding in-house.

**33:17** · Like we have a whole science team that's using the models and just trying to understand what they can do. And a lot of that comes back to like, okay, now that like the model now that we've unlocked use case X, like what type of new data can we generate? How can we make the model better that way? Um and really like that's been the long-term vision of Chai is like we never thought of like we're going to build this one model that's going to solve all of this.

**33:36** · Like we know that there just like uh in other fields like there're going to be multiple iterations of this model. And as you get better and better models, like you get this flywheel effect, I guess.

### Data Flywheel Explained

**33:45** · Well, and you mentioned what data can we generate? Can we touch on data for a minute? You guys can't exactly just go script the internet and have all the data you need to build your models.

**33:52** · Where does the data come from? How does it kind of compound over time? Can you just say a word about data as an input to your models?

**34:00** · Yeah, so uh I think like the primary source of data or like the the gold standard source of data is this like protein database. Um so this is like it it's actually just like ac- like legit lab scientists like who since like 1970 have just been depositing crystal structures of like proteins and other molecules over time. Uh and like really without that like structure prediction and design wouldn't have been a thing.

**34:26** · Um so there are these uh so that's like one source of structural data. When I started in the field, I really took like a structure-pilled approach. I was like super interested in predicting structure, like how do you think about a machine learning model that can output 3D coordinates? Like that's that's not doesn't look like an LLM, it doesn't look like an image model. This is really in its own class. Josh, interestingly, was taking like the exact opposite approach. Uh so, he he was like one of the original authors on ESM, and that was like a really like a seminal work in understanding how to apply language models to protein sequences.

**34:53** · Uh what's really cool about that work is if you can train a language model to understand protein sequences, what ends up happening is it ends up kind of like representing the 3D structure internally. And there's like a really interesting reason why this happens. So, like in order to predict like missing amino acids, so like same way that you'd predict like next word in a sentence, I want to predict next amino acid in a protein. In order to do that effectively, like you really need to understand like, okay, what does the amino acid's like immediate microenvironment look like?

**35:20** · Uh cuz that kind of tells you, okay, what are like the compatible amino acids with everything surrounding it. And in order to do that well, you need to understand the protein's 3D shape. Um so, I was taking like this this really structure-based approach, and Josh was even more bitter lesson-pilled than me.

**35:34** · He's like, "We're just going to like look at the sequences, and this is just going to emerge." Um so, yeah, the two main sources of this data, again, like protein database for structures, and then like these massive massive, maybe even like order of like trillions of tokens, sequence databases. Um and what you can do once you have really good models is just run them on the sequence databases to get new structures out. Um so, again, like you have this compounding effect. As your models get better, they get more and more accurate at predicting these structures, uh and then you have more and more training data for the next series of models.

**36:02** · So, nice people ask us at Chai about, these days at Chai, like which which paradigm are are you actually going after? Like one of the things I love about our team is that it's actually just like neither. We're very pragmatic.

**36:12** · Like we want to solve the problem. We don't really care is it a sequence approach, is it a structure approach? In practice, it's going to end up being like both, of course. Um I think you'd be surprised, but there there might even be more like biological sequence tokens on the internet than like English language tokens.

**36:25** · Uh and a lot of that data is not that useful. It might not be redundant. It might be very noisy. But there's a lot of data out there. There's a lot of art and like bringing it together. And I think also the exciting thing is as the models have gotten into a point now where we can design things in the lab, write to new targets for instance, we can actually use the models to generate data as well. So there's a lot of exhaust from like all the experiments that we're doing at Chai, which also helped to make the models even better.

**36:47** · So it's a similar kind of takeoff that we saw with LLMs. Like when I was at OpenAI, we worked on reinforcement learning of like a GPT-1 architecture. Like did not work models weren't like good enough. But once the base model got good enough, then you could start to do those kinds of experiments. And And I think there's a similar analogy that's starting to happen in our world now as well, where the models have reached a point where there's actually like a renewed interest in data and like how do we actually bring the models into the loop on like making that happen. I think that creates another really like interesting cycle on on compounding improvement of the models.

**37:15** · Yeah.

**37:15** · We're talking a bit about compounding improvement in the models. And you said something about how pharma as an industry is an incredibly competitive landscape. And it's interesting cuz I think there's been a renowned interest in using AI and using ML to generate proteins and molecules. And so your arena has actually become quite competitive. And you guys have obviously done an amazing job at staying at the frontier.

### Staying Ahead at Scale

**37:37** · It's been the year of deployment for you. You've locked up a number of pharma partnerships that are making your models better. But how do you guys think about the competitive landscape and staying at the front of the frontier?

**37:47** · Well, first of all, I think it goes back to like looking at the results and not fooling yourself and being rigorous. So one of the reasons why we do a lot of evaluation of the models. We mainly do it just to hill climb in the models itself. I think if you look at many of the capabilities that we've brought in have kind of been like first in the field. You look at our Chai 2 model, right? Like getting to success rate of the models that you didn't have to do large library screening anymore to see results.

**38:09** · Couple months later showing how we could bring in a lot of these developability properties we've talked about before like manufacturability of the molecules.

**38:16** · So in in many cases we are pushing the model forward and and trying to see these these emerge. And then we try to quickly like lock those in. Like, how do we how do we make those capabilities like even more pronounced that they become production ready and we can like ship them to our customers. I think one of the one of the things I like to tell the team is that you know, it's not like we are head-to-head like with other model providers or something like that. We're all of us I think are working against nature. Like, nature's actually been a pretty good baseline. People have done drug discovery a certain way for a long time. And you know, Matt talked about how like maybe you don't want to add like module 24 to the Chi model.

**38:47** · But people have added like module 240 to like the existing wet lab protocols. And they have been like tuned quite considerably.

**38:56** · One of the scientists on our team, Andy Young, was he was one of the first people working on yeast display at MIT actually like two decades ago. And he's got 20 years experience in like Pfizer and Genentech like really honing in these methods. Has a drug approval to his name and antibodies. And I think you look at someone like that and like, you know, Andy knows how to make a good antibody with existing tools. And and that is actually the bar that we need to clear.

**39:18** · Now of course, I think the ceiling on AI is going to be a lot higher than what we've managed to do before. Otherwise, what would be the point of of doing this? We didn't start the company just to make, you know, a 10 times faster mouse, right? We started this to make breakthrough medicines that that weren't possible before.

**39:32** · But ultimately, that is the bar that we needed to clear in order to get adoption. I think we hit that inflection point a couple months ago. That's why you've seen a lot of these big pharma announcements. But now we just need to continue to hone in on like making these things even better.

### Culture and What's Next

**39:44** · For somebody who's listening who thinks, "Wow, this sounds pretty cool. I wonder what it would be like to work at Chi."

**39:50** · What is the best thing about working at Chi? And what is the worst thing about working at Chi?

**39:56** · Yeah, I can I can speak to some of this. I'll think of this on the fly. The worst thing \[laughter\] the So I think like the the best thing is just like how actually like mission-driven everybody is. Like everyone is so dedicated to what they're doing. I've worked at other companies.

**40:11** · Like the closest I've ever seen to this is like maybe some of the guys in my PhD lab. Um, but like everyone is just like incredibly incredibly motivated. We all work really hard. There's like an obvious shared goal.

**40:24** · Um, and I think that's really rare to see and I think this goes back to just like the focus that we've had since the beginning and like we've always had like kind of a clear philosophy, a clear plan on how things are going to get there, how things are going to get better. And really like everyone at Chai is very bought into this. It's pretty amazing just to see like the amount of dedication that that everyone's putting in. Uh, least favorite thing about Chai, uh, not directly on top of dandelion chocolate, maybe.

**40:47** · \[laughter\] No.

**40:50** · Maybe the next office.

**40:51** · Yeah.

**40:52** · Uh, actually, so probably the least favorite part now, uh, is just like I guess it's getting things to work at scale.

**41:00** · Um, and really I I didn't even know what that meant. Actually, when we started Chai, we had 128 GPUs and I was like, this is like the most scale possible for a lab. Like this is crazy. Uh, I came from like, you know, my PhD group where we there were four of us sharing eight GPUs and I was like, I just felt GPU rich. It was crazy. Um, so now like, you know, at Chai like we have a lot more infrastructure to maintain. We have a lot more compute resources. Like luckily, GPUs are parallelizable. Um, but that also kind of brings up its own set of problems. So just like how do you keep a cluster healthy over time? How do you get that large training run?

**41:32** · So like how do you keep that running for for months on end? Um, and even when it does die like how do you automatically resume these things? How do you keep all of your communication down? How do you optimize the models and make the best use of the resources that you have? So I think these are a lot of problems that, you know, they continuously pop up.

**41:48** · They're good problems to have, but I think they're they're also really difficult to solve. Um, yeah, and I I'm just excited to work on this.

**41:55** · Yeah, we I remember one of the CEOs that, uh, we worked with a couple times, Frits van Slooten, had this line about you either have the pain of failure or the pain of growth. You'd much rather have the pain of growth.

**42:04** · Yeah, \[laughter\] that's exactly right.

**42:06** · I think my favorite part is is probably the results. Uh, and that that sounds a bit cliché, but there's nothing like It's It's working, right? And just like knowing that you're, you know, uh I think many of us in the company, right?

**42:17** · Like we've been working in AI for a long time, right? There's all this experience you built up. And And to know that you're applying it to something that really matters, like just even I think just take Matt and and and I like we've been working on this problem for like 10 years, right? And a couple of years ago I'm looking at something like, "Yeah, we're writing some cool papers. Like everyone is like celebrating this. Are we actually making the world better?

**42:34** · Like is this actually going to impact some patients?" And I think now the answer is like, "Actually, yes. Like we have reached the point where this is going to make a big difference in the world." And every time you get one of these breakthrough results, anytime there's a new feature on the product that makes our lives of our our customers easier, whenever there's like new lab results uh coming back uh from the science team, it's just always so uh honestly it's exhilarating to realize like this is actually going to change the world in a pretty profound way.

**42:59** · I think that's also then uh maybe it comes to the least favorite side, right?

**43:03** · Like, you know, we're running the company and it's like we have real partners that are relying on this. And like things have to work, right? And you ship a new model generation. How do you make sure that there's no bugs in that?

**43:12** · How do you make sure you don't have regressions, right? This is no longer just like a Again, the blue sky research problem of like, "Oh, we got some cool results and we move on." Uh we've had to have really high priorities on like, you know, having production-level code bases. As the team grows, how do we make sure that the code base is in a state that more people can contribute to this.

**43:27** · So, um something that that one of our other co-founders, Zach, likes to say is that if you want to move fast in in the long term, you sometimes have to just move a little bit slower in in the short term, right? And And make sure that you are building something uh Again, that goes back to that compounding idea. Goes back to we don't add module 25 to make the next thing work. Uh so, sometimes uh you know, you're you're like so excited to get to the next result and you just want to jump into it, but uh we have real partners, some of the biggest companies in the world that are now relying on us.

**43:54** · Uh and it's important that we we realize that, we take that responsibility to heart, uh and we make sure we're building systems that, you know, continue continue to work.

**44:03** · I have a burning question. Why Why guys called Chai Discovery?

**44:07** · Chemistry and AI. But we love chai tea as well.

**44:10** · \[laughter\] There's a lot of chai tea stuff in the office. So yeah.

**44:12** · That's a good question. I didn't know that either.

**44:14** · Josh is the visionary. That was all him.

**44:16** · \[laughter\] It is a very user-friendly name.

**44:18** · Yeah, we also wanted a name that like like biotech companies have such complicated names. We wanted something that's going to be much simpler. We're trying to build make this whole thing simpler, right?

**44:26** · So we need a simple name to go along with it.

**44:28** · Awesome. What are you guys most excited about in the next 6 to 12 months?

**44:33** · I think for me it's just the deployments that are happening. So we've announced a couple of these these partnerships and I'm really excited just to hear about the results that our partners are bringing online. It goes back to this point of like making a real difference and also why I'm so happy to see how these partnerships are going even, you know, posted the agreement and as we're working with these folks that models are not sitting on a shelf somewhere. Like they're actually being used on real programs.

**44:59** · People trying to approach devastating diseases where, you know, if Chai could give them a molecule that that works it could really change the lives of patients. So I'm really excited to see how that goes. Just the pace of progress here is is incredible but also just like the pace of the models. Like a year ago you could not zero shot a molecule and like, you know, have a good sense that your program was going to work. Like now that's changed. Someone might zero shot a molecule and be like I I think we're going to bring this program to the clinic now. And then a year later, you know, they might even have some of those first molecules going into patients.

**45:26** · And just the speed of that is is just incredible and it's you know, sometimes you get some shivers thinking about this stuff like, okay, my model is going to like Matt has some patents from our last company about, you know, like just generating the molecule on the computer and these things are are now in patients and just to think about the scale. Like I don't know a few years from now, do we have dozens? Do we have hundreds of like Chai molecules going into people? It's a bit mind-blowing to think about what that might might look like for patients.

**45:53** · I think one of the things that like again like what made Chai unique like the dedication. Like people are like, man, you work a lot. Um and like you like aren't you burnt out or whatever.

**46:02** · It's like it's actually really easy and like it's very motivating when you're making progress. Seeing the progress that we're making and just like thinking man the next model is going to be even better than the last. We identified this new thing so on. Um like that's so incredibly motivating.

**46:16** · For me it's more of just like what what can we unlock next and like how do we make these things more controllable and like when someone comes to us with a certain target instead of just like hoping we get good affinity or something like that, you know, can we actually control this? Can we say like we want exactly a 10 animal or binder or things like that. Like there are a lot of technical things that I think are we're like kind of right on the brink of solving. Um and for me it's like it's really motivating just to like pin those things down and just like get all of this over the line and see kind of where that leads to next.

**46:43** · Awesome. Matt, Josh, thank you for Engineering Biology and thank you for sharing your story with us today.

**46:49** · Thank you guys. Thanks for having us.

**46:53** · \[music\]

**47:16** · \[music\]