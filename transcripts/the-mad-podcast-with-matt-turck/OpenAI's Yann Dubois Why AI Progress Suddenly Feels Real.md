---
title: 'OpenAI''s Yann Dubois: Why AI Progress Suddenly Feels Real'
source_url: https://www.youtube.com/watch?v=DhD1zZ8w8Mw
video_id: DhD1zZ8w8Mw
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/yann-dubois|Yann Dubois]]'
published: 2026-05-21
created: 2026-07-23
language: en
speaker_attribution: contextual
description: AI suddenly feels like it has crossed a threshold, and Yann Dubois, co-lead of the Post-training Frontiers team at OpenAI, joins Matt Turck to explain why. Yann’s team has led the post-training behind
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=DhD1zZ8w8Mw)

AI suddenly feels like it has crossed a threshold, and Yann Dubois, co-lead of the Post-training Frontiers team at OpenAI, joins Matt Turck to explain why. Yann’s team has led the post-training behind the company's reasoning models, including the recent GPT-5.5 release. In this conversation, we go inside the shift from raw model capability to useful, reliable systems: what changed with GPT-5.5, why reinforcement learning is moving beyond math and coding competitions into messy real-world work, how reasoning models like GPT-5.5 actually work, the difference between GPT-5.5 Thinking and GPT-5.5 Pro, why post-training has become one of the most important frontiers in AI, and why evals, model-as-judge, hallucinations, agentic workflows, GDPval, and continual learning are now central to the next phase of frontier models. Yann also shares why continual learning remains one of AI's biggest unsolved problems three years after ChatGPT, and where startups still have massive room to build as frontier models race ahead.  
  
Yann Dubois  
LinkedIn - https://www.linkedin.com/in/duboisyann  
X/Twitter - https://x.com/yanndubs  
  
OpenAI  
Website - https://www.openai.com  
X/Twitter - https://x.com/OpenAI  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id1686238724  
  
00:00 - Cold open  
00:34 - Intro  
01:30 - Why recent AI progress feels like a step function  
04:13 - Model reliability & the rollercoaster of shipping 5.5  
07:33 - How OpenAI structures vertical and horizontal teams  
09:49 - Improving model efficiency and test-time compute  
12:32 - Yann Dubois' journey from Switzerland to OpenAI  
15:37 - Reasoning in 2026: Real-world utility vs verifiable rewards  
18:34 - GPT-5.5 Thinking vs Pro: Scaling test-time compute  
20:09 - How reasoning models become more efficient  
23:23 - Pre-training scaling and overcoming the data wall  
27:03 - Multimodal data, synthetic data, and embodied AI  
31:05 - Demystifying mid-training and post-training  
37:21 - Does RL create new capabilities in AI?  
38:53 - The challenges and frontier of scaling RL  
43:09 - Is building AI models a craft or a strict science?  
48:21 - How AI models generalize across different domains  
54:18 - How reinforcement learning cures AI hallucinations  
56:04 - Negative generalization and conflicting instructions  
58:05 - Can RL scale to law, medicine, and the broader economy?  
1:00:19 - The evaluation bottleneck and Model as a Judge  
1:04:21 - Continuous AI progress & continual learning  
1:08:49 - Will foundation models eat the agent harness?  
1:11:23 - Why startups should focus on the last mile of AI

## Transcript

### Cold open

**0:00** · You need to reach this level of reliability to really make any of these AI tools very useful and I think we just crossed that probably December last year at least at Open AI. Now we can trust these models to do a lot of the work that we are doing. The last few months have been pretty wild. We moved from like competitions to usefulness to users and that's what we are feeling right now. I think most of the time the product is the the last mile.

**0:25** · There will always be a lot of space left for this last mile in different verticals and I would highly encourage people to continue working on that. Hi \[music\] I'm Matt Turk. Welcome to the Mad Podcast. My guest today is Jan Leike who co-leads the post training frontiers team at Open AI. The recent release of GPT-5.5 was yet another major milestone \[music\] in AI and Jan's team helped build it alongside Open AI's prior top reasoning models including O3 and GPT-5 thinking.

### Intro

**0:53** · Before Open AI, Jan was at Stanford where he co-authored Stanford Alpaca, the landmark project that kicked off much of the modern post training research community. In this conversation we go deep on what's actually new in GPT-5.5, why reinforcement learning is moving from math and coding competitions into messy real world work, why AI progress can feel like a sudden step function, and why continual learning remains one of the big unsolved problems in AI three years after ChatGPT. Please enjoy this fantastic conversation with Jan Leike.

**1:27** · Hey Jan, welcome. Hi Matt, thanks for having me. It's been another wild last few weeks in the world of frontier AI with the release of GPT-5.5, of Claude Opus preview. So it feels like we have unlocked yet another step function in progress particularly in cyber security, agent decoding. What's the best way to think about this from your perspective?

### Why recent AI progress feels like a step function

**1:54** · Are things accelerating? What is happening? Yeah, the last few months have been pretty wild.

**2:00** · Internally we also really feel it and I think anyone who's working with uh anyone who's work who's coding basically is really feeling it right now. Um I think that's really because of three reasons. Uh the first one is even though the in my mind everything the progress is actually pretty continuous you need to reach this level of reliability to really uh make any of these AI tools very useful and I think we just crossed that probably December last year at least at OpenAI.

**2:30** · That's where I thought we really crossed that threshold. Uh where now we can trust these models to do a lot of the work that we are doing.

**2:38** · So it feels like a step function even though I think actually in terms of capability it's like it's pretty continuous. Um so that's the first thing. The second the second reason is um once you start having models that are really good you accelerate yourself. Um especially in terms of coding given that we all code internally uh you accelerate yourself both for having these models like train the other models but also like build like the tooling that we need as researchers to like do our job and and all this acceleration I think means that we saw these last few months going faster and faster.

**3:10** · The third thing that I I think we are feeling is all of last year we really built on um like these reasoning models and we really like sign pushing a lot on on reinforcement learning. And initially when we had like O1 um O1 preview even O3 um these models were still like optimized for uh what what we call verifiable rewards.

**3:35** · Things where we actually have access to ground truth and like it's easy to test whether you're correct or not.

**3:40** · Uh that is for example the case in like math questions or like com like coding competitions and what I think we are realizing now is that we were able to take many of the tools that we we for these like verifiable reward cases and we were able to use them more generally in on for reinforcement learning on like real use cases and I think that's like really what we're feeling that right now and like just real world coding rather than like competition. So we moved from like competitions to usefulness to users and that's what we are feeling right now.

### Model reliability & the rollercoaster of shipping 5.5

**4:13** · Okay, fascinating. So we're going to unpack a a lot of this particularly on the on the RL side. First the first thing that you mentioned reliability. Is that a engineering? Is that models? Like what what makes a model reliable in in in the way you meant it? It's a little bit of everything, but in general given that these are agentic models, the longer if you just think about it as like every two minutes there's like a certain probability that they're wrong. The longer that they run, the the higher the probability that like the final answer is going to be wrong.

**4:44** · So it's just something inherent in like agentic models. And what we've been pushing a lot on is like making sure that the model like we decrease this probability of being wrong every like two minutes. So purely from a model point of view, of course there's a lot of reliability that is also happening on the applied side and the team at OpenAI has been doing an amazing job on that.

**5:05** · But I'm I'm even talking only about reliability of our models and like making sure that like we see we decrease the probability of being wrong. Great.

**5:11** · So 5.5, formerly known as Spud, was as mentioned a big deal, is a big deal.

**5:19** · And I'm just curious from the inside, what was what are you guys the most proud of? What do you find the most challenging? Give us some some some color on like how you all felt you know releasing this. We were all really excited about 5.5 to be honest.

**5:36** · It is one of these models where everyone in the company was extremely involved in building and I think that we really feel it now.

**5:45** · That's like we got a lot of attention because of the 5.5 and it's uh it seems like all the stars were aligned. That doesn't always happen.

**5:54** · Um and it was just like a great model for the for this. Um so we we did feel it. It's kind of funny because in general with every model that is looking really good early on, uh we have a model, we all get really excited about it, and then there's like tons of doubts that start uh coming up because like oh, like everyone is so is like hyping this thing internally, but actually it's like bad at all these other things.

**6:17** · And then there's another wave where like people start uh um under-hyping it and it kind of goes through through waves and it depends like when we actually ship it how like people feel about it internally. But that's true of like most models that we have. Um so 5.5 was not that different in this case, but it definitely maybe had like a a higher amplitude of the wave. So people were very excited, then very not as excited, and and we shipped it and and people were happy externally. How long does that process take? Like, you know, you including the waves of going up and down and of of of excitement.

**6:48** · I guess it depends on the on the on the release and the importance of each release, but like is that a is that a few weeks or a few months? It really depends. I So I can't talk exactly about what what went into uh 5.5, but it can it kind of depends um which part of the pipeline is training parts of the model.

**7:08** · So we really have like different sub-teams uh including pre-training and you you have like the mid-training stage and like you have some post-training and usually the closer you get to to products, like pushing being the last one, the faster the iteration cycle is. Um and if you're more upstream, the slower the iteration cycle is.

**7:27** · Uh so it could go from let's say from months to to days uh basically. 5.5 was particularly good um on agent decoding, computer use, knowledge work, and early scientific research. How does that work in internally? Do do different people focus on those different parts? How do you get to that result? Yeah, we definitely have different teams that are working on specific use cases and are pushing on these use cases.

### How OpenAI structures vertical and horizontal teams

**7:54** · My team specifically is actually the one that is kind of taking all these vertical improvements and try to put them together in the final model. You could see it as a team that is doing both kind of the smoothing function. So you have all these improvements, but you need to make sure that the model doesn't feel too spiky, doesn't feel that differently in different on on different verticals. And also you have you need to have some teams that are working and that's basically what my team is doing on all the horizontal improvements.

**8:19** · So there are many things like instruction following, function calling, or like thinking about how much should the model think for on different problems. Those are very horizontal and that kind of impact all these use cases. So we have both these more vertical teams and these more horizontal ones.

**8:37** · Um and both are very important to to to improve the to improve on the model.

**8:42** · Um and the good thing is that these things can kind of be improved orthogonally. So you might have like multiple different teams that are working on certain verticals and maybe for one model there's only a half of these teams that made integrations basically in the last run and like improved the model on on these capabilities and maybe for the next model it'll be the other half. So that's kind of at a high level how it works.

**9:06** · One thing which I will say because you asked also about one of the things that I'm really proud about for this model, I would say two things. Number one is the efficiency of the model.

**9:17** · We really really improved the efficiency of the model and like we most of the tasks can be basically performed, I would say like 2x faster now with this model.

**9:29** · So that's great.

**9:30** · And the other one that I already mentioned before, but it's kind of this alignment of the company and making sure that like everyone is working towards the same goal.

**9:37** · And that really takes the entire the entire company working towards like this North Star of building one good model in in like specific timelines. So, very very proud of how that happened. Great.

### Improving model efficiency and test-time compute

**9:49** · And then speaking of efficiency, how do you optimize for that? Are we talking about efficiency per per token? Are we also talking about latency in serving the model? What what what part is AI research versus engineering? So, that's what that's what I I mean when I say it's the entire company, is that it really comes from everywhere. It has to come from like inference optimizations.

**10:11** · Um it has to come from the model being more efficient in its thinking time. So, you have basically every token that you think for basically the the usual plot that you should be looking at is x-axis the number of tokens that you think for and y-axis the the performance. So, this is the these test time scaling curves that we look at. Um and research basically tries to move this curve to the left. So, think less to be the same level or more correct.

**10:37** · Um and then inference also deals with with this x-axis but switches switches it from number of tokens to actual latency.

**10:49** · Um and the the final thing that people care about is latency on x-axis, performance on y-axis. And this is where everything comes together and this is really what happened with 5.5. Um so, yeah, that's why I was saying I'm really proud of the company for this one. Okay, great. Let's talk about you for for for a minute. So, you are in the portrait frontiers team. So, that that team you described as horizontal. So, what does the the team do in in general? Yeah, I would say there's three things that we do.

**11:15** · So, in a broad broad sense, we are under portrait org and my team is the portrait frontiers one. Um so, there are three things that my team does. Number one is we kind of decide what goes into the final run. Um so, as we talked before, there's like many verticals uh and someone needs to decide like what can go in, what cannot, and also provide the the science experiments for people to to iterate on something that's going to be representative of the final run. So, this is the first thing that that my team does.

**11:44** · The second thing that my team does is bringing everything together and actually doing the big run.

**11:49** · So, this has, as you might imagine, like we train on a good amount of GPUs, so there's a lot of infra work that is needed, but also there's a lot of ML work that is needed by putting everything together and making sure things work well together. And then the third thing that my team does is uh horizontal improvements to the models.

**12:05** · Basically, there are some things that like these vertical teams will not usually look too much at, for example, the thinking time as I said before. So, how much should the should the model think for on certain answers? Um, or like instruction following, function calling, uh things like memory, and like general improvements to the model that are really across the stack. Um, so that's what the Pushing Frontiers team does and uh and I'm leading that team.

**12:31** · Okay, great. And uh what was your journey to OpenAI? Oof, it's a long story, but I'll try to keep it really short.

### Yann Dubois' journey from Switzerland to OpenAI

**12:39** · Uh, basically, I did my undergrad in biomedical engineering um in Switzerland. Um, I'm from Switzerland.

**12:45** · And then I went on an exchange in Canada and I learned about word2vec. So, I don't know if you heard about this algorithm, but it basically takes words, which is like a something discrete, uh and puts it in a in a vector space. Uh, so puts it basically in in a way to think about it is a plane where if words that are more similar to one another will be closer to one another. So, it brings these like discrete words into like some continuous space that is semantically meaningful.

**13:13** · And I was absolutely blown away by that algorithm, and that's when I decided that I I wanted to work on natural language processing and just like understanding language. Um, at that time, I was very wrong, but I thought that uh English uh uh NLP was basically solved or at close to being solved. That was in 2017. So that was right when Transformers started. It was actually right before Transformers.

**13:35** · So I was very wrong, but I decided I wanted to work on under-researched languages and basically I wanted to improve NLP on languages where we don't have that much data.

**13:48** · So I went to work for Grab in Singapore and I was basically building the natural language processing pipeline for them working with Khmer, with Bahasa, with Thai, Vietnamese and all these different languages. And then I'm skipping a little bit. I had I did more academic type of work in different countries and I ended up at Stanford and did my PhD there.

**14:12** · And after this had a small stint in two startups and then went to OpenAI. Yes. And I remember seeing on your blog or your page a note to you for for quant firms to not reach out to you because you were not interested in hedge fund work.

**14:31** · Yeah, but I always think it's very important for me to think about the positive impact that I'm having in the world or at least I am trying to have.

**14:39** · So so that's that's why this note is there. Yes. And as we were saying just before we started recording, people may have seen you in the GPT-5 video announcement and then you did this very funny demonstration of an app that was built on the fly to teach your partner how to speak French.

**15:03** · So like people should go check that out.

**15:05** · \[laughter\] Exactly.

**15:08** · That was that was a fun one. That was a fun one. It was GPT-5 was not that reliable. So I was a little bit stressed that it wouldn't work. \[laughter\] But but it did end up working. So this was truly live and and presumably very very rehearsed but but truly life. Actually, the right before we did that like the last rehearsal, it did not work.

**15:30** · \[laughter\] So, I got slightly stressed about that, but but yeah, seems like life life end up working well. Yeah, no no pressure, but yeah, that that that landed it perfectly. Okay. Very cool. All right, so let let's unpack some of the things we alluded to in the intro.

### Reasoning in 2026: Real-world utility vs verifiable rewards

**15:49** · So, we we started effectively talking about reasoning and I'm I'm curious what reasoning means in 2026 that's any different from, you know, a conversation we could have had about 01 or or three. In particular, one of the claims of 5.5 and and also my experience as a user is that it's particularly good with with messy data, which seems to imply that it needs to reason through ambiguity more.

**16:19** · What has changed? What I would say is that 01 and 01 preview were really really breakthroughs in in the research community about having model that can think and the longer they thought for, the more like the higher likelihood they would be of being correct.

**16:37** · So, that was really a breakthrough, but it initially and if you look at like old blog posts, you would mostly see like math math evals and also like maybe coding competitions, but things that are really easy to test whether you're correct or whether you're not. And it also gives you like some suggestion about like how we were training some of these models.

**16:59** · And how I see maybe all of last year and especially the end of last year and the beginning of this year is that we were able to take these arguments that work with verifiable rewards like things where we can say you're correct or you're not to the messy real world and really optimize for the utility that we provide to users and like making them more productive. So I think that's what really changed.

**17:23** · Okay. So it's the post training reinforcement learning part largely. Yeah, I would say that's uh I mean there's also there's also another big part of it. Uh in number one basically the first thing is that of course when you develop a new method the method is kind of fragile and it's not that reliable and like it's hard to to basically productionize. So this part also improved a lot.

**17:51** · But then it's also really basically we had a tool that we could start optimizing for for different things and initially when we were developing this tool we were we were making a lot of simplifying assumptions of in the real world basically and now we are removing these simplifying assumptions and and at least in post training we are able to optimize really like user utility and make sure that these models are useful and the tasks that we're looking at are useful and that's why also now current emails look much more realistic.

**18:21** · I mean if you think about GDP or even if you look at like SweetBench Pro or SweetBench these look way more realistic than let's say some code force or like coding competitions that we were looking at with 001. Mhm. Mhm. And still on the topic of of reasoning um what's ultimately the difference between 5.5 thinking versus 5.5 Pro? Is that is that just more test some compute more tokens and more time invested in solving a problem?

### GPT-5.5 Thinking vs Pro: Scaling test-time compute

**18:49** · Yes, basically it's just a question of of how much test some compute we pour into the model we pour into this entire system that we're shipping. Um so we we've seen again and again the longer the model think for uh the better answers we will get.

**19:07** · The problem is that this these curves that we're talking about, um, are not are definitely not linear and like they there's some plateauing effect and they kind of look, um, log- logarithmic, uh, on some in some sense, um, or depending on which e-levels. So, you can pull like two times more compute and actually only get like small performance gains. Um, I personally don't use Pro that much cuz I really don't like waiting. I'm pretty impatient.

**19:39** · So, I don't like waiting for that long and and I know that the probability of being correct definitely improves, but it doesn't improve like enough for for me to use it. Um, but there are some people who use Pro and who really love it, especially actually for academic research. And, uh, I know especially a lot of mathematicians who are using it. Uh, and that's because they're kind of just have this in the background that is running for maybe 1 hour, uh, 2 hours and they don't really need to like iterate really quickly with the model. Um, and Pro is really good for that.

### How reasoning models become more efficient

**20:09** · I'd love to reconcile this with, uh, what you were mentioning about efficiency earlier per token. So, is the idea that, um, you would be able to think longer, but also be more efficient, therefore solve the task better? Like, how do those the the the the time aspect and the efficiency, uh, aspects of interact?

**20:32** · Yes.

**20:32** · Uh, so, if you go back to like the plot that we I was talking about or I was thinking about, uh, where on the x-axis we have latency and y-axis we have performance, we're basically moving this curve when we say that we improve efficiency more and more to the left.

**20:44** · This will be coming more efficient, uh, or like we spend less time to achieve the same performance. Um, but what Pro does is that it extends this curve. So, it says like, um, I'm going to think for much longer, but I will have a higher likelihood of being correct. But every iteration of the Pro model also moves to the left.

**21:02** · So, it also becomes more and more efficient. The The part is, um, there will always be tasks where uh, uh, you just want to maximize the probability of correctness and you don't really care about latency. For example, if I if I start a job before going to sleep, I mean the model has like 8 hours like it should just think for as long as it as it can.

**21:25** · Um and this is what kind of probably gives you. In in layman's term like what what what does that mean practically or how does that work practically if the model goes in a wrong direction then it would interrupt itself earlier?

**21:40** · Is that is that one of the axis? So for the efficient Okay, so there's two things. Are you asking for the efficiency? What does it mean the for the efficiency. Yeah, yeah, yeah. Yes, for the largely for the efficiency. I'm like I'm just curious how reasoning gets more powerful. Yes, that that's a good question. Let me give you um maybe a metaphor from like humans.

**22:01** · If if you have a someone who know like someone who's an expert in certain domain and you compare them to like some undergrad that is like starting in that domain. The undergrad doing that task will probably take might take like one day, two days and will have to think through a lot of like the the possibilities and like investigate because it never did a certain problem.

**22:24** · Well, someone who's an expert in that in that field will usually just like know what direction to take and it will it will not spend the time on like investigating 10 different directions cuz it knows that there's like one that is more likely to be correct. So this is a type of efficiency that we're talking about. It's basically models that we where we optimized more on like real-world problems and as a result it was kind of trained to to figure out with a higher likelihood which paths of reasoning are more likely to be correct. So this is this is the part on on efficiency.

**22:58** · There's also what what you suggest is that um part of it is the model knowing when it's going down the wrong path.

**23:05** · Uh but this is also something that we can um that the the model can be trained for with reinforcement learning. It's like knowing, "Okay, like that seems like not a great path. Let me backtrack and let me go on and test something else." Um and if you train the model less, uh it might realize that it's in the wrong path much later.

**23:22** · Okay. All right. So, it seems like um a lot of this uh goes back to uh reinforcement learning and post-training. So, let's uh talk about uh how the different components of modern AI systems work. Uh so, let's talk about pre-training, mid-training, and then post-training and spend more time on post-training since it's so important. Uh starting with pre-training uh first at a a high level and and realizing that uh you may or may not be able to talk about um how the things are are are done what happened in the context of um 5.5 specifically.

### Pre-training scaling and overcoming the data wall

**23:53** · You know, big narrative of last year was that uh pre-training was hitting a wall uh and was not going to yield much progress. That seems to not be the case at all uh in 2026. Uh can you walk us through some some ideas for what is happening in pre-training and why it's progressing now in a way that people hadn't predicted uh last year?

**24:19** · For pre-training, I I can't talk um in a lot of details about what is happening internally uh besides that um the team has been really doing a lot of good work. Um and our models are really getting better and better. Um one one thing that I do want to um highlight when we're talking, for example, with efficiency, um if you have larger models, uh the amount of thinking time, so the amount of tokens they will think for, um will usually decrease.

**24:47** · And the way that you can think about it is that um metaphorically, the model already thinks through its weights when it generates a certain token.

**24:58** · Um, so you can you can decrease the number of like tokens that you need to generate for thinking by kind of like increasing the size of the model uh that you are training. Um, so so oftentimes if you just increase the the model size, if you basically train uh pre-train larger models, uh you will get better efficiency.

**25:20** · Um, and the good thing with larger models is that they can be parallelized better on on at inference time. So, the even though you might think, "Okay, you actually generated fewer tokens, but by a larger model, uh so you actually might decrease the uh the overall efficiency of the system."

**25:41** · This is not true because the larger the model is, the the more chances you have to actually uh optimize for optimize basically for inference on on on GPUs. So, you will be able to uh um to make the the overall system like more efficient. So, that's that's one thing I wanted to say with like larger models that are actually giving you a lot of efficiency.

**26:03** · Um, otherwise, in terms of pre-training, I think it's very interesting. I actually also thought maybe 2 years ago that pre-training was kind of hitting a wall. Um, and when we see, for example, if we talk just about Anthropic, I mean, this has seems likely just a much bigger model when you look at the cost.

**26:21** · Um, uh the the cost of the model usually that's how we know, by the way, if it's a if it's a bigger model, you just look at the cost. Um, per token. And and clearly, they're getting very good performance uh just by increasing the size of the model.

**26:37** · Um, so I think the field was very at least part of the field was surprised about that. There were a lot of conversation about hitting uh data walls, and it seems like we did not quite hit it. So, the larger than model is, the more data it needs to ingest to be trained. Um and it seems like different companies kind of found different ways um to overcome the fact that that we don't have that much data on the internet. Is the next frontier or the current frontier uh for for data multimodal data? Is it synthetic data?

### Multimodal data, synthetic data, and embodied AI

**27:09** · I think synthetic data can probably work well in a in a data um data-limited regime. Um I think multimodal is an interesting one. Uh I I definitely can't talk about what we do internally, but like I used to work on multimodal uh representation learning back in the days, and I always thought that it would really help uh kind of your reasoning abilities if you have a lot of multimodal data.

**27:37** · Um And I still think this, but but for example, like if you look at Anthropic models, they tend to not be that good on multimodal, and they are still really smart. Um so it seems that uh it's not as necessary as at least I would have thought in the past.

**27:54** · Um I still believe that once we go to embodied agents, embodied AI, you will learn a lot about the world, um and you will kind of improve general intelligence and usefulness to users um by learning how how the world interacts with itself. Uh but at least looking for example at Anthropic models, it seems like they they don't need that much multimodal data to have a strong models.

**28:19** · And by embodied intelligence, uh you mean so potentially robotics, and so if you use a video uh that shows how gravity works and how a robot evolves in space, then presumably that would be more useful. Is that Is that the thought? Yes. The the idea the the intuition that I think many people had, and I I definitely thought for a long time, is that it's hard to understand the world uh only through text.

**28:43** · And and there will be um it's hard to understand what like what physics is without really seeing what like for example you can't understand gravity without really seeing things falling um and when you look at our models I mean it's they kind of understand gravity without having seen that but it still seems not

**29:06** · obvious like it seems still seems like they would get it more and like they are still kind of missing some common sense uh aspects um So I do feel like we will improve the common sense of our model by having them interacting in the real world but we are we're still pretty far from that I think and by we I mean just generally the academic community and and the AI community seems pretty far from that.

**29:28** · Yeah and \[clears throat\] while we're on the topic as a quick detour that that leads us to the concept of world models so leaving your taking your open AI hat off are you are you bullish on world models? World models in the sense that um Yes you can try to replicate or like simulate things uh simulate like basically working in environment that is simulated um Yes the problem is simulations always

**29:57** · going to be really hard and not not going to be truthful so I think it will always need to be a certain a little bit of training that will need to happen in the real world to make sure that the model realizes kind of these mismatches between the simulated world and the real world and I think uh we as a field have a tendency of optimizing something that is simulated or not quite realistic um past the point where this is useful.

**30:25** · Uh so that's like something that I think we should always be careful with is we spend a lot of of time and effort on optimizing something simulated or not quite not quite realistic and it's great at the beginning but at some point once you start optimizing too much for something it's it's not representative of the real world and and people continue doing that just because that's what they've been doing for a long time.

**30:49** · So, I just think people need to realize when to stop that. I don't work with uh with these type of synthetic environments as much or just because I don't work on embodied AI. So, I don't know if we're there yet.

### Demystifying mid-training and post-training

**31:05** · Great. Great. All right. So, going back to pre-training, mid-training, post-training, let's talk about mid-training. It's maybe something that people have heard about a bit less. The term comes up a bit less. What is it and why is it important? Mid-training um is just this this idea of something that's between pre-training and as you might realize from the name and kind of the post-training um part of this part of the pipeline.

**31:30** · And really the idea is if you have high-quality data um that is more representative of what you really want in your final model. Um you should overtrain on that data. Um so, taking a step back here, pre-training, what is it? Pre-training, it's basically trying to learn everything from the world by learning everything from internet at a high level. Um the problem is that most things on internet are not really useful.

**32:01** · Uh if you think for example about Wikipedia or like GitHub, which is like coding data, um it just seems like there's way more information in there than some random forums. Uh um Yeah, some some random forums that may maybe not like have that much information or like for example ads. There's also lots of ads on internet.

**32:19** · Like you probably don't want to train too much on that. Um But in pre-training, we train on everything and in mid-training, we basically overweight this type of high-quality data that we think is more useful uh for for training the final model. And this is something I can't talk about what's happening at Embodied AI, but this is like something that that is happening definitely in all the academic community right now and in all the open source models have the stage of pre-training. Great.

**32:44** · Post-training let let's start at a high level by by defining what it is. What is reinforcement learning but that's not the only part of post-training. What what else is there? It kind of depends how you define the term and where you put the boundaries. In my mind post-training including let's I'll take it from a very broad sense which includes all the reinforcement learning and like the training for reasoning models.

**33:06** · It's just the idea of having something that knows everything about the world to making something that is useful to people. So pre-training I think about it or the metaphor that I like giving is you go in the library and you have a lot of books about everything and in theory you can find all the information that you want in the library.

**33:29** · But it's much more useful to talk to an expert who has learned these books and that you can ask questions to and they can answer and they can answer and like they they can understand like what you're actually looking for. So this is kind of the goal of of post-training at the at the very high level is like making something that is useful to users and is like easier to interact with. So there are multiple stages. I'll talk mostly I'll talk only about things that are happening outside of Open AI and kind of the the usual stages.

**34:01** · Um there's usually some SFT that is happening. Which is supervised fine-tuning. Supervised fine-tuning, yes. Supervised fine-tuning and that's that's actually what early on most of the models that were post-training were only doing supervised fine-tuning. This is the idea is that if you have humans that can give you the desired final answer.

**34:25** · So if you have if yeah, if you have humans that give you the gold answer, you can basically clone the behavior of the human. Uh so this is what we call behavior cloning. Um the problem with this is that you will never get better than what your ground truth gives you.

**34:43** · Uh and humans are actually pretty limited in many in many sense. So you will never like overcome uh the the the the human labelers that you you're working with. Uh the reinforcement learning it or reinforcement learning stage goes from behavior cloning to really like optimizing rewards. So the idea is I don't know what the ground truth is. I don't know what the perfect answer is.

**35:06** · But here here's how I would say whether the answer is correct or not. And here are the things that I I want in the answer. And what you do is you start optimizing. You start having a model that tries to to get more reward.

**35:18** · Basically optimize more um uh this uh this reward function that that we That's how we call it. Um and it goes beyond what you currently have. What what like humans can do. What is the humans that you're working with can do. Um so this this I would say is the two big stages.

**35:37** · Then in reinforcement learning uh that depends in like which models are being trained. At least in the open source community it seems that there are uh there are different ways of doing that. Reinforcement learning when you have very fireable rewards. So uh reinforcement learning where it's really easy to say whether something is correct or not. Then you can really kind of have binary reward for this. And that goes back to how we talked about 01 uh and 01 preview in the past. Um and then you have reinforcement learning without fireable rewards where maybe I could do pairwise comparisons.

**36:07** · I can say this this answer is better than this this other one. But I don't really know I I I cannot quite say this is the perfect answer.

**36:16** · Um so of course like it's a continuum and there's everything in between. But I would say these are like the three uh high-level uh things to think about when you think about post-training in general, um, and how people are usually doing it in the open-source world is that they take SFT, uh, they clone the behavior that you you can collect online or from humans, and then once it's already at a pretty good level, they just do this reinforcement learning to go beyond what we currently have.

**36:47** · Cuz if you just started from reinforcement learning, it would be very inefficient. Um, because the problem with reinforcement learning is that you have to stumble across the right answer, basically. Cuz how it how reinforcement learning works is you sample many times essentially from, uh, from the model that you're training, and you say this one is correct, this one is not, and you say do more of the one that is correct.

**37:10** · So, you have to stumble across the right solution. So, you're much better off first getting as much as close as possible to the best you can do, um, and this is this behavior cloning, and then doing reinforcement learning. Does reinforcement learning, uh, create new capabilities, uh, or does it make the model better at existing capabilities? It's really hard to say because pre-training, when it's trained on all of the internet, arguably already has all capabilities in it.

### Does RL create new capabilities in AI?

**37:42** · Um, so it's it would be even hard to answer this question scientifically. Um, cuz arguably everything is is already there.

**37:50** · What I would say is that if you look, uh, at models that we were training or that you were post-training like 2 years ago in the open-source world, uh, for example, I I worked on one of them, Alpaca, where we used 50,000 examples for SFT, and like now when you look at reinforcement learning from from models like Chimney or or or from Deep Seek models, it seems that they are closer to 1 million data points.

**38:13** · So, definitely people scaled up a lot the reinforcement learning stage, um, and from this it seems that they've learned like new capability like this reasoning aspect, this fact that you can check your answer and and and try to improve it.

**38:30** · Um so, you can you can really think for longer to get to get a a more correct answer. So, all this to say that arguably everything is already in pre-training, but we were definitely able in the last 1 year and a half even in the open source world um to have more capabilities after reinforcement learning that we used to uh before.

### The challenges and frontier of scaling RL

**38:53** · I heard several times that uh reinforcement learning is pretty finicky and and hard to scale and part of the reason why we as an industry didn't do uh reinforcement learning as part of the initial kind of LLM um uh sort of a progress curve was was precisely that that it was hard to to make work. What is hard about scaling RL? Is it a question of uh data sets, knowing where the rewards are, is there is that or something else?

**39:20** · I would say most people who did not work in reinforcement learning in the academic and like in research community up to 2 years ago probably thought reinforcement learning would not would like just doesn't work and is like too finicky to to work with.

**39:33** · Uh I used to be that type of person and actually when I saw ChatGPT come out, they had this blog. I was not at OpenAI at the time. Uh I saw this blog that says that they use reinforcement learning and my first thought was I can do the same without reinforcement learning. Um because this is just an overcomplicated method. And this is actually the project that we started working on with Alpaca was exactly let's try to reproduce that only using SFT just by doing this behavior cloning.

**39:58** · Yeah, and and like for example, Yann LeCun famously like gives like this metaphor of like oh the the reinforcement learning is like the cherry on the top. So, I think that was really like the intuition that most people had. Um it seems that after crossing a certain scale of um models that know basically everything about the world and what we call like good priors about the world, it seems that reinforcement learning just started to work.

**40:21** · And this is not only with LLMs, robotics seems to have uh get it seems to be entering the same stage uh where they're realizing that actually it used to be very finicky, but now that we use models that like know already everything about the world, it actually learns pretty well. Um now to answer your question about what is still complicated with reinforcement learning, one is an infra aspect.

**40:45** · Um so, just like systems in general, uh reinforcement learning you have at a very high level basically to sample as I said before many answers and say like what is correct um and what what is not and um and like this sampling is just very expensive uh and you have you have to do it at scale.

**41:03** · Um The other issue that that uh also in the open-source world we uh people are seeing right now is that when we are training more agentic uh systems, you only know whether you're correct at the end of your very long roll out.

**41:23** · Um so, you get very little information per token of whether you are correct or not and it's hard to say uh it's it's hard to basically do attribution. It's hard to say what part of your entire answer was the one that led you to being correct.

**41:39** · So, that's more of a uh of an issue on the machine learning side. It's uh the the the ideal world in machine learning is when I can say exactly like this thing was good, do more of that. And the problem again with with uh with these agentic systems and in reinforcement learning with these agentic systems is that you don't really know which part was good or not until you arrive at the end. That's another big issue from from for re- reinforcement learning. What's the current uh frontier of reinforcement learning? It It seems like there's a jungle of acronyms like GRPO and uh other techniques.

**42:11** · What uh what are you using? What are you excited about? What do you think is promising?

**42:17** · So I can't talk about what we're using, but like for example, uh in the open source world, GRPO seems to be working very well. Um and people used to have different methods like PPO and and DPO and like people seem to have really converged to this one. Uh the big the big difference with others other methods is that um you again you do this like simple method that I told you about like sampling as many answers as possible and you say which one is correct. Uh so in some way GRPO is a very simplistic method.

**42:53** · Uh and in general we saw over and over again in machine learning that the the simplest method that where you can scale up in terms of compute usually is the one that ends up working the best. And that is kind of what is happening here. Um at least in the open source world.

### Is building AI models a craft or a strict science?

**43:09** · As you describe some of the challenges, question crossed my mind. Uh you know, you often hear that AI systems are not built or grown. How you'd characterize AI as well? What part is science versus a craft or trying multiple things and then just keeping what works best in your day-to-day life? Yeah, that's that's a great question. I think how it usually works is that it starts being craft.

**43:33** · Uh people just try out many things and and they start building a mental model of what works and what doesn't.

**43:42** · And over time we move to like from this like craft land uh to more science. Science uh is or like more scientific approach are really the ones that like first end up working. It's hard it's very rare that you you take a really scientific approach and and you say um uh like this is the optimal the the thing to do and you do it and it just works. Like people just uh there's some sense of alchemy.

**44:09** · People just have like a good flair for something, and they make it work, and then other people or that person uh starts trying to improve what we are doing by being very scientific. Um and I would say this this happens over and over um in in machine learning. Uh so first craft, then science, and both are really important. Uh but it's different stages of the pipeline. In terms of engineering, this is definitely something that is uh always necessary.

**44:40** · Uh so I would say most researchers have moved to being relatively uh good at like figuring at least I wouldn't say good engineers, but good at working in a complex systems and like figure out what they need to to to try out. And the systems the the and the infra that we have has become one more complicated. Um so so the definitely the work required changed it over time.

**45:09** · Fascinating. All right, so still in the reinforcement learning and circling back to some of the things you said at the at the beginning. Um so if I want to make my model better at computer use or any coding or whatever domain, then I would spend a particular amount of time doing specifically reinforcement learning for computer use and putting together a data set and then uh coming up with rewards. Is that Is that how it works? Like you you just pick one problem and you just uh do reinforcement learning specifically for it?

**45:41** · To be clear, I I talked more about reinforcement learning because also this is like the part I know I know the best, and this is what I've I've worked like pushing I've worked on for uh a long time. Um we talked about mid-training before. Uh like all these things are also extremely important, and you can improve it in different parts of the pipeline.

**45:59** · As I said before, the closer you are from the final stage of the model, uh usually the smaller um the the scale of the training becomes. Um so, you can iterate fast on that. Cuz now you can iterate in terms of days rather than iterate in terms of uh in terms of months. So, usually people start from the cycle fast iteration loop, and then they go deeper, and they make like bigger changes uh across the entire stack.

**46:26** · So, this is not to say that um only like reinforcement learning matters. I'm really not saying that, but it's just like like that's why people will start doing uh changes, and then they will that will permeate, and uh we will go deeper into the stack. Um so, this is how it how how it works uh and and like in the open source world, it's very much like that, too. I think you see way more post-trained models than you see new pre-trained bases.

**46:49** · Um and you see way more like improvements in in like the algorithm, and that's why we talked about I mean GRPO, DPO, PPO, like there are so many XPOs, and that's because people can iterate really quickly on on this final stage of the pipeline. And the the jagged nature of uh those models, does that come from this approach of uh picking this problem and that problem, and therefore it's going to be excellent at those problems but not as good as other problems?

**47:18** · Or is that a more fundamental characteristic of uh AI models? There's definitely some of that. Uh for sure, if you optimize more on specific types of problems, you will be better in in that setting.

**47:33** · Um I would say this my intuition is that it's less about the exact like problems that you're optimizing on, and it's more about the class of problems that you're optimizing on. So, for example, uh if you are really good at like math competitions, your model will probably be pretty good at like coding competitions. So, it's not about the domain, it's more about like the skills that are necessary and the way to think um a and and this like horizontal um capabilities that you need for performing these tasks.

**48:03** · And that's that's um what I think you're usually seeing when some when some model is really bad at something, it's actually bad at that in any domain, in any language. Uh so so you have to think yeah about this domain and then then this generalization of this domain, not necessarily per domain uh capability. So speaking of generalization, so there's been that clear evolution from math and coding success to now uh starting to cover different areas.

### How AI models generalize across different domains

**48:30** · So that's the whole GDP valve thing where like across the economy um different areas are being evaluated in terms of like model performance. This is sort of the same question. Is that is that the result of uh overall model progress or is that a deliberate okay, now we're going to take uh you know, this part of the economy and build a data set for it and do mid-training and do post-training.

**48:55** · How does that progress work from uh those very specific domains to generalizing to the rest of the world? It's definitely something that we actively push on. I think people are realizing, I mean us and also other companies um that we are moving towards this world um where we want to really make products that are useful and like improve like productivity of people um and and help people in the day-to-day life.

**49:25** · So I think there's a there's an a very active move to deciding what are the domains that we should be prioritizing. What are um now that we know we have an algorithm that we can apply in different places, uh what we're constrained by is more collecting the right data, having people who really care about a certain problem uh work on that problem. Uh but there are not that many people who can do these things, so you really need to prioritize.

**49:53** · Um so this is Yeah, it's it's a very active um it's a very active proactive kind of approach here. Um And in general, I would say the performance of the model really depends on like the number of people who care about the final uh output of the model uh who are looking at that model. So if they start looking more at specific verticals, like these verticals will improve really quickly.

**50:22** · But again, we don't have that many of these people that can do these things. But to impact uh something that you alluded to I think a minute ago, do do models uh actually generalize now more, especially from a reinforcement learning perspective? So being making a model very very good at domain A or B then is likely to make the model better at C, regardless of the amount of effort you put in to developing uh rewards for domain C. So I think there are different axes of generalization.

**50:55** · One, there's an algorithmic generalization. And and that's like really can I use the algorithm that I developed or this black box that I developed for domain A and can I use it for domain B.

**51:07** · Um and at least again, like even talking about the open source world, it really seems that it's like people are able to do that. They take GRPO, they apply it in like many different places and it just works. So that generalization uh seems to be relatively uh good. Uh which which is why we're seeing a lot of progress, otherwise it would be hard to make progress. Uh then there's the generalization of the model that is trained on one particular uh data set. And this is what I was alluding to before.

**51:34** · At least my mental model is uh the generalization happens in terms of capability like if the capability is the same, you will see generalization across domains. Um Again, like multi like different languages like coding. Like you can optimize for C++ coding for having a good like C++ model uh with very little training on C++.

**52:00** · Partly because this pre-trained model of very little hour in C++ but partly because this pre-trained model has seen all of C++ and so it already kind of like understands the basics of that language. Um so so that type of generalization definitely happens. Um the generalization that I think is harder uh are these when we don't have these like horizontal uh capabilities. So I'll give you one concrete example.

**52:25** · If my model is very intelligent in terms of uh being correct on like competitions, I I usually take that example cuz it's like somewhat contrived uh at like math competitions, like coding competitions. From a human perspective, people that are good at these things are usually just smart and if they are smart or like someone might think that at least that are just smart and if they are smart they can actually do other things, too. Um but that is really not true.

**52:49** · And that type of generalization is really not true because um many things where we need to have uh humans working on like expert domains, like the world is very messy and these coding competitions and math competitions are extremely well specified. And you need to have this the capability of like understanding like under specified tasks.

**53:09** · Understanding how to deal with like the messy world and understanding like what is the um what are even the resources that you need to answer the question. Like if you look at the at the math uh competition, like you usually have everything in the in the in the prompt.

**53:28** · It's like you have five lines or maybe 15 lines and it's like all the information that you need to answer this question. In the real world, uh if uh if I'm a consultant, if I work in like finance, I need to go on the internet, I need to like find and extract different information just to understand um before doing any of the reasoning just to to be able to do that reasoning. And and this type of like horizontal capabilities I think that um doesn't usually like we you generalize if you have that horizontal capability, but in many cases we don't have that horizontal capability.

**53:59** · Um So yeah, that's why we hallucinate actually in every domain. Like when you have hallucination of LLMs if if if a model is really bad at saying that it doesn't know, that usually happens in every single domain.

**54:10** · You won't have like one domain where the model is extremely calibrated about its knowledge uh and another domain where it's not. And as a quick detour is is is hallucination also a reinforcement learning problem or where you reward the behavior to say I don't know uh when it occurs?

### How reinforcement learning cures AI hallucinations

**54:28** · John Schulman has a great presentation about that I think from like one or two years ago um where he was saying that if you do be if you do behavior cloning, so this like SFT that we talked about before, um you will be like you will basically reward and optimize for hallucination because what will happen or you could optimize for hallucination because what what will happen is if your model doesn't know about something, but now you say that the right answer is to say that something. So I'll give you I'll be very concrete.

**54:58** · If the model doesn't know about a paper, uh and now in an answer that you give that is given by a ground truth answer given by a human, you say uh here's where I got the information and then you cite that paper.

**55:13** · Like what you're actually optimizing the model to do is citing something that doesn't exist because it doesn't know that that paper exists. Um and so so so John Schulman had this like great presentation saying like SFT is going to force like hallucination while in reinforcement learning given that as I said you cannot sample from the model in the first place. Extremely likely that it samples something that it doesn't know and it's correct. That's like extremely unlikely. Uh so, you will never reward that behavior.

**55:40** · You will only sample things that it doesn't know and being incorr- incorrect and then you will kill that uh kill that behavior.

**55:48** · So, so, hallucination um at least the the intuition that people have um is that it can come for example from from SFT and it can come from this like war string pipeline, but if you have good reinforcement pipeline, that shouldn't happen too often. And uh going back to um generalization as well. Is there are there examples where um actually getting better at one domain makes the model worse at uh the rest?

### Negative generalization and conflicting instructions

**56:14** · A little bit uh to what you were saying about like some people are very good at math, some people are very good at English. Pretty often they're not the same people. In domains?

**56:26** · Usually not. What will happen though is um you will make decisions based on which domain we optimize for. And if you optimize for one domain, you will be able to optimize less for another one.

**56:39** · So, it's not necessarily that optimizing for one thing will make the other one worse. It's just that as a result you can optimize less for the other one because you're compute constrained, you're data constrained, you have like like your your uh human bottleneck also in terms of that one. What does happen is uh you can have negative kind of generalization like bad generalization or negative transfer more for these horizontal aspects of the model.

**57:06** · Uh so, I'll give you a very concrete example. Um explicit instruction following versus implicit instruction following. If I If I have a model and this is we often hear for example from OpenAI models that they tend to be really good if you tell them exactly what you want.

**57:23** · Um but as a result, sometimes we hear also that they're like less good if you are not as as specific about what you wanted. For example, if I make if I make a typo and I say like change this file and I make a typo in this file. Um an extremely good model at like explicit explicit instruction following will change the wrong file, the one that has a typo.

**57:47** · But like humans would probably realize that you made a typo. Um and and like as a result there are cases where this explicit instruction following goes against this like implicit instruction following. Um so you will have cases where basically these horizontal um capabilities go against each other. And maybe to close on this whole um reinforcement learning um conversation.

### Can RL scale to law, medicine, and the broader economy?

**58:11** · So is your sense that as we progress from being excellent at coding and excellent at math and move to the rest of the economy, do you think that the rest of the economy is a tractable problem? Do you think we can get to the same level of performance ultimately?

**58:26** · Yes.

**58:28** · But I was like yes, we can. I don't think there's anything like really deeply special about these domains where we cannot optimize and where we couldn't get the same with other domains. The but is for for at least two reasons.

**58:43** · The first one is most of the people working on these models are really good at coding and they really care about coding cuz that's what they use as their everyday kind of drivers. And there's nothing better than the user being also the one who like trains the model cuz like then they understand the issues.

**59:01** · It's um it it's very hard to really like for me for example, it's very hard to really understand like what should we change on the like on like legal uh aspects of the model if I don't understand anything about the legal domain. Um so that's one thing.

**59:18** · The other thing that um you will often hear about and and I I mentioned also briefly about before is this kind of verifiable rewards. There are domains where it's easier to say where something is correct or not. Um for example, in the case of cyber, like you you mentioned that before that like cyber has been improving a lot. Cyber capabilities are models, and this is because in cyber it's like extremely easy to say if in are you correct? Like did you find like it did the cyber issue that you find is a real issue or not?

**59:49** · It's very easy to test it. And so there are domains where reinforcement learning is just like easier to um to apply.

**59:57** · But there's nothing I would say in the capacity of the model that is constraining the model to be as good at legal and like medical um and like other domains. So it is the the the short answer is we know less about these domains, and um definitely there are some domains that are easier to optimize for in reinforcement learning. Great. Let's talk about evals for a minute. Uh that's uh a hugely important topic. Maybe to start, why is it so hard to evaluate a model in the first place?

### The evaluation bottleneck and Model as a Judge

**1:00:28** · Evaluation has been harder and harder as models become better. Um and that's because the tasks that we ask to the model become uh more and more general um and more and more open-ended. So like now I maybe just say like build me a website that does X.

**1:00:52** · Well, before in the in the past I would just be like, "Hey, like is there a specific bug in this in in this like implementation that you have?" And it's like much easier to say whether there's a bug because I I can I can extract I can know a priori I can have a human that says, "Here are all the bugs that you have." And then you can apply that automatically. Um while the the website one is very hard to know uh what is like the optimal answer cuz there are many good answers. There are many good ways of of building a certain website. This open-ended nature of models really makes evals harder.

**1:01:22** · Um there's also another issue is that models in specific axes are becoming better than the majority of humans. And so we have fewer and fewer humans that can actually evaluate these models in particular axes. Uh so that's a big constraint. Another one to be honest is kind of cultural.

**1:01:41** · Um most people want to improve the model and they they think that the best way to do that is kind of training the model. When in reality finding issues and like making sure that we can quantify improvements is just as important if not more important. But there's always this like cultural gap.

**1:01:59** · Um that was especially true I would say in the academic world up to like 2 years ago when evals were always fixed, benchmarks were always fixed, uh and even data sets were kind of always fixed maybe let's say 4 years ago. Um and there was like a mentality shift of like okay, data is actually critical.

**1:02:18** · And now there's a lot of people working on data. And I think evals were still not quite there. People don't really fully Everyone knows that it's important but like people don't really understand like how impactful it could be to work on evals. Um so actually my first first project at OpenAI I just came in and I was like I want to work on data and evals cuz I know that this is the thing that no one is is working on. And as a result I know that's like super impactful to work on that. Um and yeah, the tide is shifting but like not fast enough.

**1:02:45** · And is the pace of progress in model as a judge and AI evaluating AI is that is that moving as fast? Is that a distinct part of research or uh is that fundamentally the same idea or the same techniques? It's really fundamentally the same method. There's like nothing Also most of the things that we do in in evals, especially now that we have reinforcement learning could just be applied nearly exactly as is during training.

**1:03:12** · So that's another reason actually why evals are so so is that every time you build an eval, you actually build a way to build training data sets. Um so now you're going to optimize that training data set. Well, not even if it's not that eval, it's going to be the same type of data and now you're going to do super well because we have this generalization of of of capabilities that I was telling you about. You will learn that on that other data set and now you'll become really good at that eval and that eval will become uh obsolete really quickly. Um so so that's also an issue with evals.

**1:03:43** · But yeah, to go back to your question, um the model as a judge, it's really important and I think it's one one probably of the most important things because as we get like better models, uh we have this self-reinforcing loop and we have this this like capability flywheel where better models become better teachers for other models.

**1:04:05** · Um and this is really important for training, but then you can also do the same thing for evaluation. So I a lot of my team works on that and I think it's really critical. It's to work on this model model as as a judge kind of uh framework. Okay. Fantastic. Um all right, so as we get towards the end of this conversation, I'd love to to zoom out a bit and get your sense for where things uh might be heading.

### Continuous AI progress & continual learning

**1:04:32** · Obviously, it's incredibly hard to make predictions on on AI uh you know, years out, but let's call it the next 12, 18, maybe 24 months. Is your sense that things are going to continue progressing or are we heading towards something that could feel more like a discontinuity? In terms of progress, as I was saying before, it's I think it's always continuous.

**1:04:53** · Now, the feeling of discontinuity will happen. It did happen 3 months ago with coding or 4 months ago with coding and I think that will happen now in every other domains. Like most people are not feeling uh the same way like the like kind of the capability of our model and the usefulness of our models the same way as like coding um uh and like software engineering it is feeling right now. Uh, so this will definitely permeate, I think, through many other verticals.

**1:05:18** · Um, now in terms of like capability bump in terms of, let's say, the the verticals that we're already looking at, uh, I think it'll be more continuous, um, and they will not be they will never be uh, big good to discontinuities. Like most of them are always local discontinuities, but you zoom out and it always just feels pretty smooth. Um, it's not always like this, but like that has been the case most of the time, and I can definitely not predict when is the next big discontinuity.

**1:05:46** · What is your sentiment on this general concept of, um, accelerating loops in AI? So, whether that's continual learning to make uh, models more current and able to learn faster to this broader concept of, uh, AI building AI like in an increasingly automated way. Fact versus fiction and what are you excited about?

**1:06:09** · I'm extremely excited about continual learning. I think we haven't quite cracked it. I mean, we have uh, we have like Codex memories, and that that is helpful, but it's definitely not like the the end state. Um, I have a friend who always like tells me about uh, can, again, another type of plot that we should be looking at, which is X axis time, Y axis utility that you provide to users.

**1:06:34** · And right now, or like, or or like usefulness basically of the models. And right now, actually, most models at day zero, if you just drop them in a company, um, arguably, they're more useful than most new employees. So, they start higher at T0, um, but then across time, they're mostly constant because they don't really learn kind of company knowledge. Uh, they don't really learn like to be more efficient over time on on doing the things that they are doing. Uh, while humans learn really quickly.

**1:07:04** · And what is important is kind of this integral, uh, or like kind of the area under the curve of these curves. And as a result, I think like humans are still more useful in many cases. And that's why what we will need is to make like continual learning is to make the the this curve now monotonically increasing over time.

**1:07:26** · And basically make models more and more useful the longer they work in a certain environment. So I'm extremely excited about it. I'm actually surprised that we're not quite there yet.

**1:07:36** · Three years ago when ChatGPT came out, I remember I was doing a startup with friends. And we were thinking about working on on continual learning and like personalization and and like memories in general. We were like, "Ah, OpenAI is going to do that in in the next 6 months. Like they have all the data.

**1:07:53** · They're going to figure it out. And they have all the users and the models are going to learn super quickly from users." And 3 years later, I don't think we're there yet. And quickly in in layman's terms, what what is the fundamental difficulty? It's a good question. I actually don't quite know, to be completely honest with you. I don't quite know why it's taking us that long to figure it out.

**1:08:15** · It's this type of of domain that I think if we really put enough resources behind it, like we would figure it out. Of course, there's especially when we talk about like this memory inside of a company, there's there's big questions about like permissions. And there's like a lot of of question about like privacy and like what you can share and what you cannot like across models across users, sorry. But for a single user, even for a single user, we're not quite there. And I don't quite know why.

**1:08:44** · At least at the at the high level that I can talk about, I don't know why. Yeah, what you bring up is I think really interesting for AI builders and investors and startups, which is this this this question of the models getting increasingly smarter within an enterprise. In particular, there's like this whole tension between whether models are able to do and then what a lot of people have built around the model.

### Will foundation models eat the agent harness?

**1:09:16** · So, you know, a year or two ago it was it was rag. These days it's all about harnesses for agents. And a lot of people are wondering whether the models are going to end up eating the harness, whether the harness is just a temporary thing. From from your perspective, like what where what do you think happens? Yeah. I think harnesses can really improve the capability of a model right now.

**1:09:44** · I think given that we're seeing this this really fast progress in terms of capability, I personally wouldn't push that much on the harness. That unless it's like the harness is is something for like very concrete goal that you're trying to achieve right now. So, certain companies, like if they are focused on like a specific vertical, they want to go from this like 80% maybe reliability to maybe the like 85% and the harnesses will give them that.

**1:10:14** · And I think that's like very important, but like they will they will they need to do it while knowing that they will have to re-tune that harness in the future. And I think that's that's totally fine.

**1:10:26** · If you try to have like a general harness to that will sustain over time, I don't think that will work. The harness is for specific domains as a short-term thing that you need to do, I think it's they will always be so much you can do in harnesses. And if anything, I think everyone should do more of that if they have a specific problem in mind because we're leaving so much on the table without a good harness.

**1:10:51** · Arguably, if we just I think if we froze the models that we have right now and you really worked on the harness and like maybe like we also spend more time on like training with like a great harness, um I think people would really feel the AGI in every single domain or could already feel that in every single domain. Um but given that we're not freezing it and we're going to continue training better and better models, uh I think the harness we don't really understand what the final harness will be and it's not and like it will always change.

**1:11:22** · Some question about applications. So, we alluded to uh your progress in in different verticals and uh there was, you know, GDP evaluation in general but also how to bench telecom, uh which does complex customer service workflows, and then uh progress against finance agents automating 88.5% of internal investment banking modeling tasks, and then 51.1% on Office QA Pro.

### Why startups should focus on the last mile of AI

**1:11:50** · So, bit by bit, uh you're doing uh more and more of this. Uh so, do you think people should be building uh applications uh anymore or is ultimately, as we get closer to AGI, all of this going to be part of the model capabilities? There's so much space on push pushing for like external companies or like startups pushing on specific verticals.

**1:12:16** · Um I think there's so much space for that. Um the reason why is because uh a lot of people kind of think about intelligence in quotations and or like kind of like raw capability as being uh the real bottleneck, but I don't think that's true. I think most of the time the bottleneck is the the last mile.

**1:12:37** · Um it's like making sure that the model has access to like the right like has the right permissions or like has also to access to like the the right connectors and things like this. Um and we are going to be very focused on this uh on on general aspect and I think there are other companies that should be focused on more of verticals and providing maximum value of what we currently have.

**1:12:59** · Um so, I think there will always be a lot of space uh left for this last mile in different uh in different verticals and uh I would highly encourage people to continue working on that. And maybe well one day when we stop making horizontal progress, which I don't think is anytime soon, maybe we will start focusing on that, but yeah, that's not what we're doing now. Okay. Well, then it feels like a very uh optimistic note, at least for the startup ecosystem to uh end up on.

**1:13:29** · Thank you so much, Jan. This was a terrific. Really enjoyed it. Thank you so much for spending time with us.

**1:13:34** · Great. Thanks, Matt.

**1:13:36** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Matt Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing, if you haven't already, or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks and see you on the next episode.
