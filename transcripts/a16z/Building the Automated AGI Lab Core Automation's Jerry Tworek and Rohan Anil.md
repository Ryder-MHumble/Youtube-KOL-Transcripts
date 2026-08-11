---
title: "Building the Automated AGI Lab: Core Automation's Jerry Tworek and Rohan Anil"
source: "https://www.youtube.com/watch?v=2RJiaf0SY8s"
author:
  - "[[Sequoia Capital]]"
published: 2026-07-29
created: 2026-08-10
description: "Jerry Tworek led reasoning at OpenAI, convinced that scaling reinforcement learning was the path to AGI. Rohan Anil co-led Gemini pre-training and built the Shampoo optimizer. Now they've teamed up at"
analysis_report: "[[Sequoia Capital- Building the Automated AGI Lab Core Automation's Jerry Tworek and Rohan Anil 分析]]"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=2RJiaf0SY8s)

Jerry Tworek led reasoning at OpenAI, convinced that scaling reinforcement learning was the path to AGI. Rohan Anil co-led Gemini pre-training and built the Shampoo optimizer. Now they've teamed up at Core Automation on a contrarian premise: the transformer has carried us as far as it can, and the bottleneck to smarter systems is no longer scale — it's the architecture itself. The missing capability is continual learning, models that adapt at test time, which transformers can't do. In-context learning taps out fast (Codex needs compacting after ~20 minutes) and fine-tuning invites catastrophic forgetting. Rohan argues pre-training and RL should be optimized end-to-end, and that transformers spend computation inefficiently. They lay out why the largest labs won't chase alternatives while locked in the coding-agent race, and why building the world's most automated lab starts with automating kernel generation—the one place frontier models still lose to a high-taste human.  
  
Hosted by Sonya Huang and Pat Grady, Sequoia Capital  
  
00:00 Introduction  
01:46 Appreciating Transformers  
02:44 Scaling Hits Limits  
04:54 Why Architecture Matters  
05:32 RL Reality Check  
07:32 Test Time Learning  
09:52 Economics Of Scaling  
12:47 Why Start A Company  
14:24 Rohan On Transformers  
19:11 Computational Depth Problem  
20:32 When Transformers Top Out  
23:22 Beyond Reinforcement Learning  
26:41 Optimization And Efficiency  
34:24 Building An Automated Lab  
39:45 Kernel Automation Roadmap

## Transcript

### Introduction

**0:00** · If I play football, for example, it looks very very closely to reinforcement learning. I get all a lot of times and every time I adjusted a little bit and I see if it roughly matches what I what I wanted and there are there are there are some self-reinforcement happening. When I learn mathematics, it's a very different type of thing. It's it's like reading about hard concepts and thinking about them very deeply inside my head until things click and I until until I have them connected. And both of those in some way are learning from experience.

**0:29** · They are just very different. We probably are spending the most compute than ever on learning from experience, but there reinforcement learning is is not the end of learning from experience and there will be better approaches that researchers will be coming up in the coming \[music\] years on how to how to use that data.

**0:55** · \[music\] Jerry Rohan, thank you so much for joining us today. The two of you are the founders of Core Animation, one of the hottest new labs in San Francisco right now. And before starting Core Animation, you led some of the most important research projects of the AI era. Jerry, you were VP at OpenAI, where you worked among amongst other things on running the strawberry and reasoning teams. And Rohan, you were one of two of the four pre-training leads at Gemini.

**1:26** · And before that, led a lot of the fundamental AI research at Google Brain and were the fix-it guy across Google and then at Anthropic. And so, between the two of you, you've seen more than a fair your fair share of what the world looks like in terms of doing frontier research. And so, I'm very very excited to dig in. Um, let's start with you, Jerry. You tweeted a very spicy take recently. The first step to replacing transformers is appreciating deeply how far they were able to carry us. Is that a eulogy for the transformer? What does that mean?

### Appreciating Transformers

**1:57** · Thank you very much for inviting us here, Sonia. I feel like a lot of my interviews these days is explaining my tweets. And what did I \[laughter\] What did I mean?

**2:08** · But appreciating Transformer means like understanding what it does well. So, if you're not solving the problems that it is solving well, you have to focus on its on its weaknesses. You have to You have to understand good parts and bad parts. And it's very easy in a lot of the work what people are doing in architectures is trying to make Transformers cheaper. They are trying to make Transformer more efficient. I I very rarely see people thinking about how do we make Transformers more powerful, trying to do more express. But But like seeing someone's weak parts and seeing someone's strong parts are almost almost almost the same thing.

**2:40** · It's just just understanding the shape of Transformer a little bit more.

### Scaling Hits Limits

**2:44** · What I think right now we are in this stage. We got to really really good at training really really big models. We mastered two algorithms. We mastered pre-training at a large scale. And we mastered reinforcement learning at a large scale.

**2:59** · And I'm asking myself a lot what is next in machine learning. I think at this moment what the bottleneck is to better models and to smarter systems is the architecture itself. It is this moment to revisit uh the train we've been riding for the last 6 years of trying to add more and more parameters to essentially two of the same operations, which is MoE and and attention.

**3:24** · And when I am when I'm thinking about it, like what's what like where we are today and what we are doing, I am thinking a lot about about like what Codex and what Cloud Code are doing for us. And I'm really really appreciative of those systems and of the coding and of the workflow automation and of the systems and of the products that we have today that we essentially have built over those those 6 years of scaling. And I think I think this is this is the first step of thinking.

**3:52** · Like, what is the If we want to work on the replacement, we need to like see where we are, what problems we have solved to like start seeing what the next stage is, what problems we haven't solved yet, what what kind of are we missing. And this is this is kind of whenever whenever I use Codex and I am successful at a task, I also start thinking, why did I why didn't I try to push that thing harder?

**4:15** · Whenever whenever I come to work, there are a lot of things I do with Codex, but I still come to work. I still ask it to do certain things for me. And I'm always asking myself, why am why am I even needed there? Why is uh core automation is name and its concept is we want to we want to be automating tasks. And why why why why are those things not yet automated? Why why why is not Codex doing everything for me? And this is this is the question of like the research, where we want to go.

**4:41** · And with that research, I'm trying to think, what kind of models, what kind of what kind of systems do we need, what kind of qualities do we need what that that that we don't we don't have today. And that's that's what I'm thinking a lot these days.

### Why Architecture Matters

**4:54** · And you have the starting premise of the architecture is the issue, which I think is a contrarian point of view. So, what's what led you to that point of view? What did you see that made you think the architecture was the issue?

**5:05** · It's fundamentally what is the issue.

**5:08** · It's it's it's like comes back from that from from the previous implication. What I I think is the issue is that the models are being trained in the lab and are being deployed in the in the real world. That is that that is the fundamental fundamental tension that is that is there. And mm like a bit of a bit of my disappointment came comes from my my my personal story.

### RL Reality Check

**5:32** · Whenever we were starting uh the research and progress on scaling up reinforcement learning at OpenAI, I basically believed that scaling up reinforcement learning is a necessary stepping stone on a path to AGI uh since since since I started like uh working working at Open AI. And I was always reinforcement learning maximalist. I was always believe this is what we need to focus on. This is what we need to do. I've seen LLMs being scaled up to to to higher and higher levels through GPT-3 to GPT-4. And we're still doing very little RL.

**6:04** · And I had this this internal belief that the moment we start scaling up RL we'll we'll we'll solve everything. We'll we'll we'll be able to solve solve all the problems. And we eventually started scaling up RL. I was I was just in there. I was I was in the center of it.

**6:20** · I was thinking here we are. If you ask Jerry in 2024, when do we get AGI? I would say 2025 will be will be that year. This is this is where we solve everything. And I saw us training model after model. This model was getting better and better. All the benchmark scores were going up. And did we also solve all the real-world tasks at that moment? Unfortunately, unfortunately not. We we we we still have work.

**6:48** · And I realized there was this bit of distinction as all the benchmarks that we are evaluating our models, they were essentially the same thing as we were training the models on. Like all the evals and training side tasks are the same sides of the coin. But the real-world distribution and real-world task is much messier, much murkier, much more much more different. Our our training data didn't really replicate the real-world use cases. And despite us basically maximizing all the task, if you see ask anyone training models, "Hey, what is one of your main issues?"

**7:23** · "I don't have hard enough tasks. I don't I don't have what to what to train our model on." Yet we are still not covering the the entirety of the of the real-world distribution. From that, my conclusion is we need to have models that learn at test time. We need to have models that learn with users on their data, on their real-world task, on the real world distribution. And there when you ask why why why why why why don't we have that today? Why why why why are transformers not not learning any anywhere? And there are essentially two types of learning that we could be doing at test time.

### Test Time Learning

**7:55** · We could be doing in-context learning essentially of transformers, which is it it it doesn't have fundamental problems of catastrophic forgetting. It doesn't have that issue.

**8:08** · It is pretty data efficient. So that that is great, but it's not very scalable. We only can have so much of it. It is limited and it has some more even more of mechanical limitations of what actually are you doing when you when you build context? But maybe maybe we can we can come back to it later. But we have we have in-context learning, which is very limited and very very small amount of data. Whenever I'm using Codex roughly after around 20 minutes of usage, I need to I need to compact it and move and move it afterwards, which is not that much not that much data.

**8:39** · If we have all all we can learn is for for 20 minutes, it's not that much. And the second thing is fine-tuning. We could try to continuously fine-tune our models, but then those have the issues of catastrophic forgetting. We have issues of very low data efficiency. And neither those are very solvable. Neither of those are very easy to uh to find ways. People have been trying. If they was were easy to solve, someone already solved it.

**9:05** · So my personal belief is we need to find an algorithm that we can we can meta learn, that we can express on the architectural layer, that can represent how does how does learning look like. How does learning look like that can work on much much longer horizons.

**9:24** · Mhm.

**9:24** · Do you expect the architecture will look transformer-like? Cuz my my my understanding from the from the chief seats is that you know, OpenAI have been trying to scale up reinforcement learning for a long time, and it wasn't until the transformer came about that it seemed like there was an even kind of scalable prior on the world upon which to even scale RL. And so, how do you even go about trying to think about scaling up this this new resume?

**9:50** · Yeah, it's a it's a it's a great question. I think those two things happened at the same time, but if anything that that happened there was was mostly about about economics, because technically you can scale up LSTMs. Just no one no no one really really dared to go in that direction.

### Economics Of Scaling

**10:07** · And they did scale much much more poorly. They are they are they are scaling in a scaling loss paper there is presented a comparison of LSTMs and Transformers. And fundamentally scaling law of Transformers was better. There is a world where we never invented Transformers and we would be scaling LSTMs and we would be having some models.

**10:26** · But because they would be much more expensive to train and much less impressive as a product, we would have we would have just this worse experience and maybe no one would be able to convince people to spend as many dollars training that those gigantic LSTMs because we wouldn't get a market return.

**10:43** · The the the majestic thing about Transformer, which goes back to like why why why why do we have to appreciate Transformers so deeply, is that Transformers are economically valuable.

**10:53** · The training them the cost of training them is lower than the revenue that they that they generate, which is which is magic of machine learning and it's not guaranteed by itself. But for for LSTMs it probably wouldn't be that way, which which which may have happened. But you can in many ways you can scale most of the architectures.

**11:11** · I think I think a lot of reasons why people didn't scale things before was because researchers before OpenAI had a lot of reluctance to scaling. It was often seen as unscientific and research in algorithm was was providing how do we become more and more efficient? How do we for the same compute budget get better better results? And it was it was a bit of a bet by OpenAI at that moment. Try to say, "Hey, we don't care about better and better algorithms. We care about smaller and more scalable algorithms."

**11:41** · And how do we how do we pour more and more compute and get better and get better results, which OpenAI was criticized repeatedly by many people in the community for for a long time. But thanks to that, we have we have the models that we that we have today.

**11:53** · Uh and I think there are tons of architectures that can be scaled up. And I am part of the core automations mission, and our our belief is that a lot of architectural research happened at too small scale for too long time. A lot of people are trying to say, "Hey, let's let's try to first try our architecture on a on a on a small data set on a small in a small computer regime, and then and then and then see where where where where where where it scales only after after you prove itself."

**12:22** · But for example, when you do work on reinforcement learning, you know that to get to any interesting results, you only you need certain level of compute to even see the capabilities in a model. Reinforcement learning needs a baseline of of of ability to only to only start working. So so where I am coming from, probably there are many architectures that need a baseline of compute to even start doing anything anything interesting and anything useful.

### Why Start A Company

**12:47** · Can I ask you then maybe a touchy question?

**12:49** · Please do.

**12:49** · If you need a baseline of compute, that sounds like a job that would be well served inside of a big research lab. Why start a company to go do this?

**12:57** · \[laughter\] It's a it's a it's a great question, and it's I think in in in many ways it's likely a timing thing, timing issue. Market is right now in a in a very specific place where the biggest and the most successful labs, by coincidence or by fate, are probably in the most competitive market fight ever right now, which makes them not very keen on trying different paths, trying alternatives.

**13:27** · If Transformer is profitable and if you can spend more efforts and more resources scaling Transformer to win in the next quarter, it's very hard to put at least a lot of attention and a lot of energy to work on something that will that will maybe better or maybe or maybe will will redefine the field in a year or two. So so I think the big biggest labs and I talked to basically all of them don't don't have that much interest in trying the alternatives to to Transformer.

**13:55** · And the labs that are not the biggest are doing whatever they can to do what they what the what the what the most successful labs are doing. And everyone is trying to trying the same the same coding agent. If you look at the last week's releases, everyone everyone is is trying to release a coding agent right now. And and I think we need different paths and different and different approaches here. So so that's what that's the niche in the ecosystem we are trying to trying to fill in.

### Rohan On Transformers

**14:24** · Mhm. And you were you were at you were at Brain when the Transformer was invented. Do you Do you agree with Jerry's eulogy for the Transformer?

**14:30** · Yes.

**14:30** · Um in some sense like um once the first when the Transformers Ashish Noam and others came up with it I I had like work I worked on my work on online distillation around the same time. We presented it at the same internal research conference. It wasn't a big deal internally. There was only few people who actually got it.

**14:49** · Mhm.

**14:49** · A lot of few people were like, oh, it's it's like, yeah, it's another work. And people were finding ways to And it was also very focused on at least the original work was very focused on a real problem, which was translation. So they solved like they beat LSTM on translation. And it took opening up I mean, internally at Google there was definitely like Noam and a few others were definitely interested in scaling language models. I think it is until GPT-2 and GPT-3 that we saw the benefit of Transformers working quite well.

**15:18** · At least the way I think about architecture is how do we spend computation and transformer is one way very efficient way to spend computation.

**15:27** · But now that I look at the industry, it's it's a lot of our computation is inference time and spending it on tokens. Let me ask the question like if I want to optimize for a better architecture, I want to look at both pre-training and RL together and I would like to find architectures that spend computation much better than current chain of thought token generation.

**15:45** · Uh in at a like to give a much better overview, it's I think of like pre-training is built the transformer with certain context length and RL comes in and it's like, well, that's not sufficient. I need more computation. Let me do it via adding one token at a time.

**16:03** · This is quite inefficient from uh like inference perspective. You're doing one token at a time, so most of the solutions have been finding to do better ways of speculative decoding. So it's like a band-aid to a problem that we've picked something that's can only generate one token at a time. So autoregressive decoding. Uh there is problems with the transformer in terms of how do we spend the computation?

**16:23** · Uh for all the longest time, I think uh most of the world was training very large dense models and it took uh like the industry like roughly two to three years to get to refine the architecture to what we now take for granted was not obvious to a lot of people. Sparsity and the mixtures of experts and getting good training efficiencies with them, right?

**16:47** · So then you can ask like what's wrong with the transformer? Well, it's it the computational depth is poor. You how do we increase computational depth? And just posing that question opens up like 20 new directions on how we can modify the mechanism to incorporate it. So um I see like to do work like this, it takes time and usually like fundamental research in the past have taken like five, six years to land into industry and it's largely from organizational knowing that it is important.

**17:19** · This is the bet. Like just like Jerry had the inner belief that RL is needed. Absolutely do not have that belief at Google. I was a pre-training maximalist. Pre-train a bigger smaller are a good fit.

**17:32** · Right? Like all right. And then so that inner belief and second is you need your architecture to run efficiently on hardware. A theoretically optimal architecture is not useful to anyone. It is something when it comes into practice. So you need the research inception to getting it productionized and getting kernels and everything written. The end-to-end loop.

**17:53** · And there's only few places right now which have integrated teams doing that and I think we have built a team in a way that puts every like the experts together not in different silos that like we are accelerating on having everybody look at the problem holistically from end to end. So that's like where I'm quite bullish. That's why I'm here.

**18:13** · Um the current mechanisms are quite poor and it will if if you leave it to the world, I am afraid that it'll take us like a much longer time horizon before we replace the transformer and I think a lot of folks are already complaining on a lot on token costs. And that seems like as someone complaining.

**18:34** · Uh I mean in terms of like yeah, exactly.

**18:39** · I come from the Google mindset where we had to like serve billions of people. So like finding more efficient architectures that fit have a like a deadline on latency and the number of tokens that you can serve. So like when I look at that like the amount of like the world that can use like frontier tech is very little and we someone or some group has to like accelerate and make this better and we are taking that shot at doing that.

**19:03** · The current technology just scaled up is still only relevant to like a subset of humans.

**19:09** · Yeah.

**19:09** · And this is the bet we're making.

### Computational Depth Problem

**19:11** · So one of the things I heard you say was the problem with transformers is the computational depth is poor.

**19:17** · Yeah.

**19:17** · If that's the crux of the issue, tell us what does that mean?

**19:21** · Why is that the case? How do you fix it?

**19:23** · I can give you like one insight like most transformers that we train are quite shallow. It's at most like 100 layers deep. Depth is like it's called deep learning cuz you want a deeper representations.

**19:38** · There has been experiments on going with no one has actually shown us learning extremely deep representations. Chain of thought reasoning and RL to do chain of thought on by model itself is one way to increase computational depth because every token you add you add like one more pathway. And there has been So, then you can get out of like this bottleneck that the pre-trained architecture has set you up on. You can only do layer number of layers times sequence length.

**20:06** · Now, you can increase the sequence length and you get much stronger results. You can do inference time scaling. Now, the issue with inference time scaling is that models now have to produce more tokens to get better results and that's very one token at a time. And from this you can see like you can directly address many of these things and this is like a subset of work that we're looking at, right?

**20:30** · Making this much more efficient.

### When Transformers Top Out

**20:32** · What's your forecast for the transformer-based architecture?

**20:35** · If it's not the end state, how far can it get us? When do we start to see it topping out?

**20:41** · I I I think it all it all comes back to what we are what we are training transformers for and what we can what we can do with them. We're doing pre-training which is very good at distilling all the knowledge from the internet into transformers and then we can RL them through which is we basically can bake all the workflows that we want into a transformer.

**21:00** · So, what what what where transformer has like capped out is we have all the knowledge of of of humanity in the model together with the relationships and how do they how do they work together, how we how they can be combined. And basically any task that we have training data for, we can we can put into the model and we this can be gigantic model trained with a lot of compute on all the on all the all the data in the world. And then if we ever stop training that model, what would what would happen?

**21:29** · Like the the question worth asking often and thinking about transformer, what would happen if OpenAI and Anthropic stopped training new models and we got we got the transformer we have today and say this is this is it. This is this is this is the best the best model we have. Uh months pass, uh year year year years pass and the model is getting less and less useful.

**21:50** · Maybe the lab really like recorded of every human on earth what they were doing and what their what their tasks were and their environments and put them put them in the model, put them in the in the in the learning environment. But then that that then then then what happens if the if anything of that stuff changes? If there are new events in the world, if those new events have new relationships between them, if there are there are new types of tasks, if there are new code bases, new tools to use, transformers are getting a

**22:19** · lot of their usefulness and all value through the things that are that are valuable have to be present in in in in in in training. And when when when when when they are not, they they they they suffer. There's there's some ability to adapt, but it's not very not very big and not very not very flexible. So in my mind this is this is kind of the level where the where the transformers uh top, which in many ways what I think is a is a tool to use for us.

**22:42** · If we if if we kind of know if there ever there's human who knows the limitations of a transformer, they can they can schedule that model, they can they can write a prompt of what is what is it the task that you want. And by doing the training we are doing, you can you can like get very successful in that and any task the model fails, you get added to training data and the model and the model can can succeed. But that that loop is has to go for the lab training training the model for you.

**23:09** · And if the model that that fundamentally needs to be trained in the lab, like how much do you think of it that this is this is the goal or or or you would want to be able to update the model somehow not having to to go back there.

### Beyond Reinforcement Learning

**23:22** · Have you read the Rich Sutton and David Silver have this paper the the age of experience? Have you read it? I'm curious how much you agree or if you have any different opinions where your opinions diverge.

**23:32** · Reinforcement learning is not a particularly new approach particularly particularly new thing to do. So, uh and some some way age of experience I think I think always has been there and people have been criticizing a bit pre-training because pre-training work clearly is this is the other way of of looking at the models which is like we have static data that data is mostly generated by others.

**23:56** · Although I I have this personal view that pre-training today is largely distilling other models other models into the new model because most of the tokens in the internet are are coming from from AI. But there there's clearly pre-training which is which is behavioral cloning which is mimicry which is which is compression of of of of of internet data. But reinforcement learning is not something that that people haven't been thinking and people haven't been haven't been doing. Reinforcement learning was used to solve backgammon back in the day.

**24:25** · They used to solve go, Starcraft, Dota and to solving programming right now and every time it comes down to model writing its own experience and learning learning from that experience. But this is very clear and what I think is interesting and what I think is still is still perplexing to people that reinforcement learning is not really the only way to learn from experience and

**24:50** · there there will be more and there will be there will be a little bit more of I think you can call it algorithmic, but essentially innovation of how we learn from experience. Just because just because reinforcement learning is only one way to do it. It's a mathematical formulation. And especially right now how we are using it. It really likes those parallel rollouts for variance reduction and for for comparing how the model does in in in parallel versions of the world, which is not how not how we do not how we learn from experience.

**25:22** · We learn from our experience much more efficiently and much more Um we use we use those in many in many many ways. At some moment I've been trying to explain to people that what what brain does how how we learn. So uh there's one learning algorithm in a brain. I think I think there are there are multiple actually and they and they they work together. But if I play football for example, it looks very very closely to reinforcement learning.

**25:47** · I kick ball a lot of times and every time I adjusted a little bit and I see if it roughly matches what I what I wanted and I learn or or some self-reinforcement had money. When I when I when I learn mathematics, it's very different type of thing. It's it's like reading about hard concepts and thinking about them very deeply inside my head until until things click and I until until I have them connected. And both of those in some way are learning from experience. They are just very different.

**26:15** · So so summarizing my thinking of the learning from experience is that we've been doing it for a while. We probably are spending the most compute than ever on learning from experience, but the reinforcement learning is is not the end of learning from experience and there will be there will there will be better approaches that will researchers will be coming up in the coming years on how to how to use that data in in a richer new chart settings.

**26:39** · Thank you. Same.

### Optimization And Efficiency

**26:41** · I'm Rohan. I'm curious since a lot of your work has been around optimization and and efficiency, how do we get to a orders of magnitude more efficient, I guess more compute efficient and more data efficient learning algorithm.

**26:55** · You know, I would start with measurement. I think pre-training as we define it right now is about compression. We look at perplexity and then measure how do we decrease the perplexity and then we find that scaling and increasing parameter count and putting more compute is the way and every time we increase compute in log scale, we get this epsilon more improvement in these metrics. This is I think this is fine for building the prior.

**27:23** · But I think this is the wrong way to look at the problem. We should be looking at the end-to-end. What are we training these models for? Look at the outcome. Like for example, I train this model and give it to Jerry. Jerry will do RL and destroy all the perplexity metrics that I have created, right? Like so then it's sort of like it was the best way we had so far to attempt to solve the problem and I think the labs and everyone else have done a great job in producing intelligence that's super valuable and makes my work so much fun.

**27:55** · But it was the bootstrap process to get there. We have to combine pre-training and RL together and that's like where one order of magnitude improvement would come from and that's like a training procedure. You can say it's a learning algorithm. Um in terms of optimization, my story is I started optimization at Google for logistic regression back in 2016.

**28:18** · Got nerds like me and I worked on some solvers for what we used to call Sybil, which was the large-scale linear solver that was used at Google before neural network took off and then replaced this. Then I asked myself like what do I want to work on with neural network and it was quite clear like I want to understand the training algorithm and make it better. And then someone Vinit Gupta just showed up one day at my desk. It's like I heard you're really good at writing optimization methods.

**28:45** · We have this idea that you know, uh like we worked out on a whiteboard uh and what turned out to be the Shampoo algorithm. Can you help us implement scale, make sure it works at large scale for neural network training? So, as working on this, I I thank my manager, Yanghui Wu, who has like supported it throughout then to like till my end of my tenure 2024. But largely like the community and most of the other people were not as excited by this idea. And for me, this is the most exciting thing cuz I was like I'm putting in computation and making training better.

**29:17** · This is the thing I have to figure out.

**29:19** · I will spend as much time I would would take to do it. And then people were um making this assumption, "Oh, why like what's the upper bound? You could still use Adam. That's fine. Like why are we You could spend all the time on everything else, not optimization." But in some sense, optimization is like like you have a model, you're optimizing it, you want to optimize it better. Now, I'll connect it to some of the stuff that we talked about architecture. What has happened is that a lot of the work that we've done in architecture is to make these networks train.

**29:50** · And in some sense, it's like two sides of the coin and optimization and architecture go together. You could have a stronger optimizer train a much more harder harder to optimize model and get better performance. Or you can use a weaker optimizer on easier to optimize models and get decent performance. So, there are these tradeoffs that appear all over. And for me, it's a lot of time working on it. I think we used it for Gemini 1.5 Flash. And then like the community started getting like more interested in it.

**30:21** · There was the Soap paper published. We have like an entire literature of like shampoo, soap, all like bath time the things that you would use. And then it was quite clear like so that was like maybe a 2x improvement over what was happening. But even then, if you look at Shampoo, it's quite weak in what it's doing. It's not using all the information that's available to you when you train. And as you use more and more information as part of training, you can get better improvement.

**30:47** · And in some sense, like your optimization algorithm defines what architectures you will discover. Like I have colleagues, it's not very popular in the literature.

**31:00** · It's only like maybe sub like four people in the world care about it. Kind of ideas that are extremely interesting like residual connections have been extremely useful for training neural networks. There are folks who have like gotten rid of them and learned deeper representations. But they needed a better optimization method. So like for me, optimization methods and the question you asked is just like how do we get there? It's It's combined with architecture and thinking about the problem end to end is where a lot of the computational efficiency is in it.

**31:29** · Yeah.

**31:30** · And I also see RL as spending a lot of compute not as efficiently. And so like if you could spend it because you don't get much feedback and you're spending a lot more compute because you have to decode all this long chain of thought to get this one bit of information into the network. Seems quite inefficient and an easy target to get orders of magnitude on top of. I can go on talking about optimization all day, but I it.

**31:55** · Rohan really has Do you think we'll ever approach or surpass biological learning efficiency?

**32:01** · I do not think so because I think we would need to change I maybe like that was a strong statement. At least with the hardware we have, it seems pretty unlikely. Um it our biological like we have something as Jeff Hinton says, model computation. So we build our own circuit as we grow up and we build our own learning algorithm with the hardware. And then we die and then we're gone. Uh neural networks are quite different.

**32:26** · Our hard The hardware stays, the neural network stays, but it's learning very inefficiently and you need a lot more of them and a lot of parallelism to get small amounts of information through. So until I think we design hardware to be much more like how humans operate, maybe more analog, figure out how to deal with analog circuits, and to figure out how to do with error correction, figure out how to get information through it will be much harder.

**32:52** · Uh we I think we're safe.

**32:55** · Safe. That's an interesting way to put it.

**32:57** · Um the idea that pre-training and RL should be optimized end-to-end seems like such a, you know, clear maybe obvious statement. Do do you think Do you think the labs realize this? And then is it just hard for them to, you know, get rid of org charts and process to be able to make that come together?

**33:16** · Or what stops the labs from from being able to, you know, unify the the two?

**33:20** · Uh I don't think it's that obvious cuz uh it's a completely, again, different optimization problem. You have a prior, you're doing rollouts, you have higher variance, you're and then pre-training is much large batch, like more parallelism or compute for the unit of time that you can spend. So, it is not an obvious thing for folks to combine these two training procedures until uh you think a bit more like, "Why is it that the naive combination doesn't work?" So, that's one.

**33:52** · Uh the second one is if I pull like some of the best researchers in these labs, they would say, "Oh, this makes sense.

**33:57** · We should probably explore it, but it would be probably not in the top bucket because they have to train a model for the next cycle before It's like as as Jerry said, like there are companies now competing for release cycles because tokens are not sticky. So, it's much harder to do long sight, like even long-term research of 6 months in many of these labs in the environment they are in.

### Building An Automated Lab

**34:24** · So, it seems like one of the core premises for Coral Lemonade is, you know, you're starting you're starting a lab at a time when you know, Sam's been talking about the AI scientists. I think Dario's been talking about the AI scientist. It seems like your job as researchers has actually fundamentally changed.

**34:38** · Um and you're get you get to start the company native to that era. And as a result, you're maybe able to run a lot more experiments than otherwise might be possible. How automatable do you think the research job is?

**34:51** · Um and how are you guys approaching building your lab to be as I believe your mission one of your missions is to be the most autonomous lab there is?

**34:59** · Most most automated lab in the world and to to start with I think that automation the version of automation by core automation is about giving each human maximum level of agency in some way. It is we we're not trying to really get humans out of the loop which is like one version to automate, but it is about give humans ability to do the most with with their their amount of time.

**35:25** · Whenever whenever you are walking you can get some distance. Whenever you get a bike you can go go work a larger distance. Whenever you are a car you can you can go much much much much larger. When whenever whenever humans started farming they had to farm by hand and will work on a small plot of land. When you have a machine you work on a much much larger plot of land.

**35:45** · Uh personally I am I'm both really great fan of the of the current coding agents and and and very happy it's in some way it is what I've been working for many years both doing coding research and working on various versions of of AI scientist inside inside of OpenAI and uh in the end I realized starting a company to realize that vision is is is is one of the best one of the best ways to realize it because the way you can do research today is very very different because a single researcher can do much more.

**36:17** · In the end the speed of iteration the speed of research the speed of how quickly you can you can move through ideas and how quickly you can get data on your ideas is something something very very different and you can try to move the old structures around it and

**36:35** · the teams workflows how data is gathered or you can try to build like like like you said you can you can try to build build natively for it for processes that that maximally empower each researcher and allow them to just to just iterate on their on their idea much much quicker. We are we are here and we are trying to to to rebuild deep learning stack and try to think how we can do almost each operation differently.

**37:01** · What are what are various options and if we can execute at least even one of those experiments a day, that's already a pretty good iteration speed versus anything that was that was done before and there isn't really like any any fundamental like laws of physics reason why not and maybe maybe one day we get to to 10 of those a day.

**37:20** · Maybe one day we get we get 200 those a day and fundamentally for that like search process optimization process, we should be able to just just find things that work in a better deep learning setting and what what we are what we are trying to do is like we've been like almost all of us we are we are we are a team that is very agent built and automation built. We are we are we are we are we are trying to do an experiment like how far how far we can we can push those thing and how far how how much an organization that tries to do as much as we can with a small team, how far how far we can get with that.

**37:53** · When will we know that we've reached AGI?

**37:56** · At some moment I used to say it's it's very much in everyone's heart, whatever whatever they consider AGI. Open AI says the system that can outperform all humans in economically valuable work, but it goes to my my my my previous statement. What if what if Open AI stops training models? Would that would that would that would that still keep working and I still would would that still keep the automation level the same the same or would that would that drive?

**38:20** · And for me AGI is a model that can improve itself without human in the loop in any in any in any way. That's That's I think I think the moment where we can meaningfully talk about about AGI because that is in some way it is a sub definition of the previous one because improving air models is actually a job that humans can do. It is economically valuable work. And it definitely definitely is the case, but removing humans from from from loops with models has been actually notoriously notoriously difficult so far.

**38:51** · We haven't come anywhere close to it. It's very very hard for me to find any task where all of them were able to like get get humans out in the loop. We are We are the the the the human LLM hybrid is is really really successful right now, but LLMs without humans not so much, not at all. And what I have seen there in 2024 and in early 2025 is that the current like path doesn't doesn't get us there.

**39:17** · And I think we need we need some pretty pretty serious research on my this company or some other to to try to unlock how do we how do we make our models learn and and adapt at a test on a deeper level than we've been so far.

**39:32** · Mhm.

**39:32** · I feel like we've alluded to this throughout the conversation, but it's kind of been one of these, you know, five blinded blindfolded people trying to find the elephant things. Uh, what is the grand master plan for for Core AI that you're willing to share?

### Kernel Automation Roadmap

**39:45** · I can share our 6-month road map. In some sense, like building architectures as I said, like wouldn't it's not just how good the architectures does it run well and can we get users including ourselves as part of the lab to use it?

**39:58** · Right? So, then that's directly like we can do many things now, but the thing that is going to be difficult and thing that we want to automate away is kernel generation.

**40:09** · So, we would we have a set of hardware GPUs, black holes that we have to train and run inference on. Uh, we will build the best model that we can to basically reduce the time from having a very cool idea that can make these bottlenecks go away in the architecture to having them run at the highest TFLOPS on GPUs.

**40:30** · And in some sense like current coding agents plus humans can go a long way, but like an example of this is our urgent QR kernel competition that we hosted with GPU mode. It's for running this fairly old linear algebra operation QR. Um, it's used for optimization like shampoo line of work uses it. Many other places uses it. And you want to run this efficiently on a B200 node.

**40:57** · Uh, if you use cool solver for the shapes that we care about, you get some efficiency. And then a human plus some search loop can get you like something like 7x. But it requires the highest taste human like there's maybe three people on the world to and spend about $100,000 on these coding agents over span of 4 weeks to get to a solution that's 60x faster.

**41:25** · So these models today are no way close to getting that 60x faster kernel. And there's there is a real bottleneck now. That was a single problem. It has like perhaps three different operators. Work on this panel, do this matrix multiply, fold it back in, and do this repeatedly.

**41:43** · That's what the square factorization of a matrix would look like. And if you give this problem to entropic models of an AI model Gemini, it just wouldn't solve it. It just is not our models are not even close to solving this problem. So for us it's like something that we've talked about, something that we're getting close to as sort of like getting to that point because that's our inner loop to having more efficient architectures.

**42:06** · Why kernels? Is it just cuz like maximize intelligence per flop of compute you need to generate your own In some sense, um I've had like three projects. Two of them have kind of landed in the industry. So, first is secondary methods. Kernels was a bottleneck cuz you have to run it well. If you were at a place like Google, you cannot spend 10x uh amount of compute and get a 2x win.

**42:31** · So, I could only spend maybe a budget of 20% and get the 2x win. Everyone's happy. I don't like great. So, like I think that's the market, right? You spend uh less than Yeah.

**42:41** · you uh get. So, kernels ended up being a bottleneck there cuz most of the operations were novel that we haven't gotten a lot of people to look at it. There's only like two humans at Google who could write it, Rasmus and Peter Hawkins. Cuz it was deep XLA LLO code that you have to write to make this work and then that took them 2 years to do.

**43:04** · The other idea I had with one of my coworkers at that time was like replacing some of the parameters in a transformer with extra memory and we called it N-gram and N-gram memory. We worked on it in 2020. It's a we had versions of it internally deployed, not the big version, the smaller version. But, there I needed like something that can accelerate sparse uh gathers and scatters as part of training.

**43:29** · Yeah.

**43:30** · Uh it required hardware change and a hardware making use of the hardware. It never arrived. I had uh conferences set up with the TPU team, us and a bunch of others. We were talking about it and during COVID like oh, we're going to have it happen and it never arrived. I also was using uh TPUs at Anthropic. While I was leaving, just barely started the surface of being able to um do it.

**43:53** · But, at the same time, 6 months before that, Deep Seek wrote uh their N-gram, which is a improved version of adding more memory. Short scaling loss that yeah, you don't need MOEs. You could actually replace it with these Mhm.

**44:06** · N-gram embeddings. for me that was like ah Yeah.

**44:10** · I It was like a five-year thing and I was very happy for them.

**44:15** · isn't even possible if you're not writing kernels.

**44:18** · Kernels and you need to be assisted in writing kernels or solve that kernel to have the highest performance. Like and the the roof line is pretty high. So it's like the QR. If I use CuSolver's QR, I get some performance. If I we use our the competition winners QR, you get 60x faster.

**44:37** · And that is a completely different playing field. Now it opens up an entire new set of algorithms you can apply and in terms of training transformers, training optimizers. QR is so fundamental in analyzing the eigen decompose for eigen decomposition and many other things. So it is a thing that I think also if you think about it, only few people have the skill set to and they're very much not at the same place.

**45:02** · It's like one person here, one person there. And it would be ideal if models had those abilities.

**45:09** · Maybe I'll I'll summarize a little bit and talk from the high level of what we want. Kernel automation is a lab created to build models that continuously learn and then learn from deployment. We believe as I mentioned that transformers are incapable of continual learning. There there's no way how to put continual learning on transformers. So we know we have to find a different different architecture.

**45:32** · Some of anyway, our quest is to find that that new architecture, find that transformer replacement and we want to build the most automated lab to do it. We want to be able to build experiments at scale the quickest we can, iterate on them, try a lot of new architectural ideas, have strong priors of what we want to do to search the space of architectures efficiently to find to go to that go to that place fastest than than anyone else.

**45:58** · That's what we what we want to do and all the work we are doing on kernels, on large scale training, on trying new architectural ideas is is exploring that space.

**46:10** · So you can experiment your way into finding a superior architecture.

**46:16** · How will you know when you've found it?

**46:18** · What are you looking for to say, "Aha, this is the one."

**46:23** · That's that's a great question. There are there always two angles. In in in my mind and my experience, every successful research had a plot that shows something that's that other other plots don't show. There there is a one line that is a little bit bending in a different different way and you're saying this is this is what you want.

**46:41** · But at least it is my experience with research always has been that plot is already quite late in a journey where most of the time you already know what you want and already know what you are up to. I am a bit a bit joking, but it's actually true that all the best plots in my life I have done in a dream before before actually they were they were real. I kind of knew I was looking for.

**47:03** · Just just the question is is like when when it actually clicks if you if you know what I mean because most of the time you kind of know what you are looking for, but you are you are not finding it. You you try one thing and it doesn't work. Try second thing and it doesn't it doesn't work. But eventually there all the all the right pieces fall into it and most of that deep learning systems are very intricate. So usually you have to get five things right in a row for the for the thing to start working and then eventually you get the plot that looks like like like like you want and then and then you know.

**47:30** · So So I think what we are what we are looking for is systems that learn and test time and if we see meaningful long-term adaptability of our of our systems and like we are we are we are joking, but it's it's it's a it's a real we want to be evaluating our systems of our of our everyday work. Will they get better at doing the work of core automation scientists each day?

**47:57** · Yeah, we like go on a vacation as a team and see if the lab produces something better.

**48:02** · For the week, give the Then what you do when you get back?

**48:05** · Um, we'll see what Extend Extend the vacation two times, three or four times, until we are on permanent vacation.

**48:14** · Uh, that is a beautiful note to end on. Um, Rohan, Jerry, thank you so much for joining us. You've both worked on like really, really transformative work for where we are today. And I'm so excited to see you starting a lab on this is new journey. Uh, and very excited to see what you're able to come up with. Thank you for joining us.

**48:36** · It's an It's a great to be here and to chat with you.

**48:39** · Thank you.

**48:43** · \[music\] \[music\] \[music\]