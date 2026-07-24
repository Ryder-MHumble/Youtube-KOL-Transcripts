---
title: Really Big Test-Time Compute in AI Changes Benchmarks, Safety and Research with OpenAI's Noam Brown
source_url: https://www.youtube.com/watch?v=AZrU6y3pUcU
video_id: AZrU6y3pUcU
account: '[[accounts/no-priors-ai-machine-learning-tech-startups|No Priors: AI, Machine Learning, Tech, & Startups]]'
account_name: 'No Priors: AI, Machine Learning, Tech, & Startups'
account_url: https://www.youtube.com/@NoPriorsPodcast
featured_people:
- '[[people/noam-brown|Noam Brown]]'
published: 2026-06-26
created: 2026-07-23
language: en
speaker_attribution: contextual
description: When a new AI model drops, it’s judged based on a static benchmark grid that doesn’t account for how long the model is allowed to think. How then should we measure a model’s true capability? OpenAI re
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=AZrU6y3pUcU)

When a new AI model drops, it’s judged based on a static benchmark grid that doesn’t account for how long the model is allowed to think. How then should we measure a model’s true capability? OpenAI research scientist Noam Brown returns to talk with Sarah Guo about his latest essay on why the AI industry’s traditional benchmark grids are broken, and how large-scale test-time compute is fundamentally changing how models are evaluated. Noam explains how, if properly scaffolded, today’s models can reason for weeks or even months on complex tasks. He also discusses real-world implications of test-time compute, from building poker solver bots to disproving legendary math conjectures. Together, they also unpack the large gaps in current AI safety frameworks, explore the bottlenecks for recursive self-improvement, and look ahead at the future of multi-agent collaboration and global knowledge sharing.  
  
Read more:  
  
\- Implications of Large-Scale Test-Time Compute⁠: https://x.com/polynoamial/status/2064210146558136827?s=20  
  
Sign up for new podcasts every week. Email feedback to show@no-priors.com  
  
Follow us on Twitter: @NoPriorsPod | @Saranormous | @EladGil | @polynoamial | @OpenAI  
  
Chapters:  
00:00 – Cold Open  
00:43 – Noam Brown Introduction  
01:23 – Why Benchmarks Are Broken  
04:19 – Compute Budgets and Projections  
05:34 – How Long Should Models Think?  
06:47 – Benchmark-Maxxing  
08:34 – Using Poker Bots as Evals  
11:26 – Safety Evals When Model Capability Scales With Budget   
14:41 – Release Cycle vs. Agent Runtime   
17:06 – Latent Model Capability   
20:59 – Limits on Recursive Self-Improvement  
27:09 – Large-Scale Multi-Agent Coordination   
29:11 – Competition at the Frontier   
31:51 – Breaking the Benchmark Grid Equilibrium   
33:29 – Why Benchmarks Should be Evaluated by Cost  
36:18 – Conclusion

## Transcript

### Cold Open

**0:00** · With GBT3, you couldn't scale test time compute. Like if you gave it a budget of $10 million and said, "Okay, well, let's see what GB3 can do." It really can't do that much. The precurren frameworks and responsible scaling policies, they don't really account for the amount of testime compute. They just say, "Okay, well, what's the capability of the model?" The problem is we're in a world now where the capability of the model is a function of how much money you put into it. Basically, if you give it a budget of $10,000, it can do a lot more than what it can do with a budget of $10.

**0:27** · Give it a budget of $10 million, you can do even more. At what budget should you evaluate these models? The policies that exist today don't really address that question.

### Noam Brown Introduction

**0:43** · Hi listeners, I'm Sarah Goa and welcome back to No Priors. Today I'm here with Nome Brown, one of our godfathers of AI reasoning. We talk about the broken state of evaluations, very large-scale test time compute, how he thinks about recursive self-improvement, and what's next on the horizon for competition at the frontier. Welcome, Gnome. I'm so excited to have you back.

**1:05** · That's great to be back. Yeah, you are our first guest. I'm very proud of my taste in friends and researchers for uh for the pod. um given you know how important uh you know inference time scaling has become to the industry you should be proud too having actually pioneered it played a part yeah among among many others you just wrote this essay that really resonated about large scale test time compute and why uh the industry is not

### Why Benchmarks Are Broken

**1:32** · evaluating these models as robustly as it should be what was the motivation for it yeah the motivation was we released 5.5 and the initial reaction ction was kind of skepticism that it was a substantially better model. To be fair, that only lasted for a few hours before people had some time to play around with it and and try it out themselves and they saw that it was actually substantially better. Um, but I think a lot of the skepticism came from the benchmark grid that was published.

**1:58** · Basically, whenever a new model is released, there's this benchmark grid where they show all these different benchmarks on on the x-axxis and then the performance of different models on the y- axis and you can just like compare different models. It's like a single number for a model on a single benchmark. And if you look on paper at the difference between like 5.5 and 5.4 or or other models, it wasn't it was an improvement, but it wasn't a huge improvement. It was only a few percentage points in some benchmarks.

**2:23** · So, people looked at that and they were skeptical that it was actually a better model. Um, once they played around with it, the story changed. I think the reason why it doesn't show up as so much better on the benchmarks is because the benchmarks are being presented, the benchmark results are being presented in the wrong way. They're not controlling for the amount of test time compute that is being used on that benchmark question. It turned out that 5.5 is just much more efficient with its thinking.

**2:46** · If you run it at max settings, 5.4 is thinking for a lot longer. It takes longer to get back a response than 5.5.

**2:54** · And once you control for the amount of thinking time, actually you can see that 5.5 is a substantial jump over 5.4. That is, I think, people's day-to-day experience with it. And then when I mention this to people the reaction, the typical question I get is like okay well why not just have 5.5 think for as long as 5.4 and the question is like well how long should they think for? Typically the response I get is well until the performance plateaus right there's at some point where the performance on the benchmark is going to plateau and you evaluate to that point. The thing is the point at which it plateaus is actually really far out these days.

**3:22** · I mean, it was true in GBD3 land back in 2022, the models couldn't really think productively for that long. And so, you could just run them until they plateau.

**3:31** · It's not that far away. But what we're seeing today with the modern models is that 5.5 and other models can think for if you scaffold them reasonably well, can think for weeks even um before having performance plateau on some of these benchmarks. And so, the point at which they plateau is simply too far out to reasonably test. we all need to actually reinforce um either like a patience limit or a budget limit from a token perspective now and that wasn't true a few years ago.

**4:00** · Exactly.

**4:00** · And so I think the proper way to and so my claim is the proper way to evaluate the models now is you either have some kind of budget for the benchmark whether it's tokens or cost or time or whatever or you plot the performance as a function of the amount of test time compute that's going into the model and then it becomes much more clear um how to compare the performance between these different models.

### Compute Budgets and Projections

**4:20** · Given the model evaluation cycle and the fact that performance does not asmtote for many tasks over um quite a long period of time. What do you do about that issue? The fact that some of the evals that you would want to run are both beyond the scope of budget or time that's reasonable given the current model release cycle.

**4:40** · I mean, I think for things like cyber, we've seen and actually the AIS um in their evaluations has shown that the models continue to improve um at 100 million tokens. You know, if you run them for 100 million tokens, they're still improving at beyond that point.

**4:55** · And that can take a very long time to run. But you also do see that like the performance is is it's not just like a discontinuous jump. It's actually like you can see the slope of improvement over those 100 million tokens. And so you could you could probably do some kind of uh evaluation up to a certain budget and then just say okay well this is what we project the performance to look like. And I think this this there hasn't been a lot of research on this yet. I actually think this would be a great paper to publish if there's any academics out there looking for something to research.

**5:24** · Can you predict what the performance looks like at an inference budget of let's say $10,000 only using inference budgets up to 10 or 10 or $100?

### How Long Should Models Think?

**5:34** · So maybe an orthogonal question for you.

**5:37** · Uh do you think users are systematically like not thinking long enough with their models about problems?

**5:42** · What do you mean by not thinking long enough? um if the if you can build an agent or control the amount of um test time compute being used like there's there's what is done by the model itself and there's what the user can do. Um do you think that like you know the industry is using test time compute an optimal amount uh way undershooting it or it's you know it's a problem in the models where they just need to be able to do that thinking faster.

**6:08** · I I think it depends on the problem. Uh I think this idea that the models you just let them think for a week or whatever and then they respond. It's it sounds nice and yes the benchmarks look great but it's not very practical when working u because like okay you ask the model a question and then you sit there for a week waiting for it to come back to you.

**6:26** · I think what people have have found most effective is to kind of like iterate quickly with the models and so the thinking time I think needs to be flexible. when it makes sense to respond quickly to the user, it should respond quickly. And then when it makes sense to think for a long time and the user wants it to think for a long time, then it makes sense to think for a long time. I think people have been striking the right balance given what they have to deal with right now.

### Benchmark-Maxxing

**6:47** · How would you characterize, you know, there's a lot of talk about benchmark maxing and the ability to game different benchmarks? What would you characterize the like landscape of benchmarks as today? And then do you have like favorites that you think are more indicative of capability than others? So the benchmark maxing thing is also motivation for for writing the essay that I think it's really easy to show you can do much better than previous benchmarks or or previous previous models on benchmarks by just for example scaffolding a bunch of models together.

**7:18** · Um so if you say okay well we're going to instead of just running this model once we're going to run it five times and take the best of the five responses or like ask a judge which one it thinks is best then you can get much higher scores than that model. And so it's really easy to make something that looks a lot better on paper but is actually not better once you control for the amount of test time compute. That is one thing that I'm worried about when it comes to benchmark maxing. I mean it like it's it's a little misleading is the only concern that I have.

**7:43** · And then as far as like the benchmarks themselves, I think there is always a risk of like just optimizing for the benchmark. And I've I've certainly encouraged my team and I think at OpenAI we're pretty good about not trying to optimize for for specific benchmarks.

**7:58** · But once you put out a benchmark, it's there's it's always at risk of just being optimized for. And I think one way to one way to address that is to keep a held out private set um that isn't uh publicly available.

**8:10** · The most popular fallback advice for you know figure out if a model is significantly better or not is to just play with it for a while. Do you have anything more sophisticated than that that you suggest people do? like do you create your own set of new evaluations each time besides private holdback at OpenAI?

**8:30** · I think everybody has their own set of questions that they like to ask the model whenever it comes out.

### Using Poker Bots as Evals

**8:34** · Um for me lately it's been I I use them to make poker bots and see how good they can make a poker bot. I think it's a nice eval because there is very little um open source code for making poker bots and there's a lot of published essay there's a lot of published papers on it but you really have to reason through everything and it's like requires a lot of just reasoning and iteration and like a lot of small gotchas that I can kind of I've already worked through myself so I can see where the models fail along the way. They've gotten really good at it now.

**9:02** · Can you describe perhaps like with your poker bot creation like how reasoning might have progressed in model releases for you guys over a few uh releases?

**9:15** · Yeah, when the early models were really bad at it, like they could not basically do anything. And then 5.2 I was able to work with it to make a river solver.

**9:28** · So that's like the final stage of poker. And um that itself was I thought really impressive. I mean I had to work with it a little bit, but I was actually really impressed cuz I was able to make the river solver probably about five times faster than I would have alone. There were a couple things that I got um tripped up on. Uh blockers was always a big big issue.

**9:47** · But overall, like, you know, with a with a bit of gentle steering, it just kind of like it kind of felt like a grad student where, okay, they would run into issues, but at least like I would um know what those issues were and know how to fix it, and I could just make suggestions and it would go off and then do it and then pretty quickly it would actually come back with something really good.

**10:05** · Mhm.

**10:05** · And then especially the optimization I thought was very impressive. It was able to make it like 10 times faster than what I was able to do because it was just able to optimize um the code so well. The downsides with 5.2 is I felt like it was gaslighting me a lot and I always had to be very careful checking it and making sure like, okay, is it actually doing what it said it did? Um, are there any things that are like glaring issues that it's not recognizing or it's just pretending aren't issues?

**10:31** · Um, I remember there was like one point uh where for one of the models I was playing around with it, not 5.2, I kind of like as a as a unit test, I told it, okay, well, let's say um I have $100 in the pot and I fold. How much am I losing? And the model said $92. And I was like, that's crazy. I have $100 in the pot and I just fold it. How do I not lose $100? And it said, oh, you know, it's 92. It's close to 100. It's fine.

**10:55** · It's no big deal. And I was like, clearly this is a problem, right? So the models did have this problem where they would gaslight you a lot. But once we got to 5.5, I actually thought um it was way better. It was able to basically do it zero shot. And in fact, I've been working on just doing a full scale poker solver. Um and it it's basically able to do the whole thing uh with some gentle steering from me. And I wouldn't be surprised if you know 6 months or a year from now, the model is able to do zero shot an entire poker solver, basically my entire PhD thesis in one go.

**11:23** · Let's talk about the larger implications of you know needing to evaluate these models relative to um let's say like speed of their reasoning or efficiency versus you know token volume right um or dollar budget or whatever whatever your scalar is. Can you describe some of the larger implications in your essay including around um like safety evaluations? Yeah, the safety evaluations thing.

### Safety Evals When Model Capability Scales With Budget

**11:50** · Um, it's it's a bit of an inconvenient truth thing where okay, so I guess for background, a lot of the all of the labs have these things called either responsible scaling policies, preparedness frameworks. They go by various names, but the idea is that whenever a model is released, they go through a series of evaluations to measure are there dangerous capabilities? Um, could these models do things that we're we we wouldn't want um a bad actor to do. And if the model isn't very capable, then it's no big deal.

**12:17** · But if it is very capable, if it could be used for example to make bioweapons, then you want to put in mitigations against that.

**12:24** · But the question is okay, well, how do you evaluate whether the model is capable of that? And they have like various protocols about like how they do these valuations. But a lot of these frameworks were developed around the era of chatgpt before after when test time comput scaling was not really uh as much of a thing and it made sense like with GPT3 you couldn't scale test time

**12:45** · compute like if you gave it a budget of $10 million and said okay well let's see what GP3 can do it really can't do that much more than what you could do with like $10 or $1. the preparedness frameworks and responsible scaling policies, they don't really account for the amount of test time compute. They just say, "Okay, well, what's the capability of the model? The problem is we're in a world now where the capability of the model is a function of how much money you put into it.

**13:08** · Basically, if you give it a budget of $10,000, it can do a lot more than what it can do with a budget of $10. If you give it a budget of $10 million, it can do even more." And so, at what budget should you evaluate these models? the policies that exist today don't really address that question.

**13:25** · Mhm.

**13:25** · Uh some do some do better than others, but um for the most part, this is not really a factor that's being heavily considered. Now, whether it should be released anyway, I don't I don't want to wait into this question. I think there's, you know, there's arguments on both sides, but I think the important thing to recognize is that this is a question that is not being we're just kind of like, you know, pretending that this issue doesn't exist. And I think it's important to just, you know, one way or the other um account for it.

**13:50** · Yeah, it's the mirror image of the capability question of if the models can uh continue to do more and more without asmmptoing on some tasks at very large budgets um then they should also be able to do so for uh tasks we don't want them to do as a society, right? And so testing for that um and what budget is allocated.

**14:11** · It also seems out of sync from the model release cycle itself, right? there's been this acceleration of, you know, you get a new model every sometimes few days and weeks at this point versus 6 months. And you have a line in the essay where you say like the the only way to truly evaluate an agent on some very longunning task might be to run it for a year. And that's going to be true of both like useful and uh negative tasks, right?

**14:39** · And so how do you think about that versus the model release cycle? Yeah, this this is also an interesting dynamic where basically as the models have become stronger, they've they're more they're better able to operate over longer horizons.

### Release Cycle vs. Agent Runtime

**14:54** · So again, with GPD3, if you wanted to run it for, you know, a week, there's really not much you could do to scaffold it into something useful that could actually run for a week. But we're seeing now with the most recent models that you can actually scaffold, for example, 5.5 into doing a series of experiments that can run for weeks, for months. Have you given your poker solver task like infinite budget yet?

**15:19** · I haven't really scaffolded something together where I just tell it like, "Okay, just run this for um for weeks." I think I could give it I I could ask I could probably give it / goal and just like yeah, tell it to go nuts.

**15:31** · But um I I think at this point it could 100% do the river solver. Um, if I just give it slash goal, I don't think it's at the level yet where it could do like the full poker solver if I gave it just slash goal and told it, yeah, go go run for a month. But we're going to pretty soon be at that point where I probably could just tell it like, yeah, go work on this for a month and then come back to me with a a full complete poker solver that's state-of-the-art.

**15:54** · And the problem is if you want to evaluate the capabilities of a model, what it can do after running for a month, the only way to be fully sure is to actually run it for a month. And if you want to know after 6 months, the only way to know fully is to run it for six months. Now there I I'll get to like things we could do to address that a little bit later. But like it's important to recognize the model release cycle is look, we're releasing new models like every two or three months at this point.

**16:19** · And so a model comes out, it takes two or 3 months to push it to its limits and then you have another model come out. And so nobody actually knows what the ceiling of capabilities are for these models because nobody's actually run them for long enough to really tell. When slash goal came out, for example, I mean, people started running things that it took over a week for it to finish.

**16:41** · And so, people actually didn't realize that this was a big deal until after a week uh until a week after it was released.

**16:45** · Mhm.

**16:46** · I think that's going to be more and more true. You know, the implications of that are, I think, pretty interesting because what do the labs do to like fully evaluate their models before they're released? It's actually very difficult because, yeah, you would have to the only way to to really do the evaluations is then delay the model release cycle. Um and you know there's a lot of competitive pressure right now to not do that.

### Latent Model Capability

**17:06** · Do you think there's um like exciting latent capability in the models that are already released that people have not fully explored given timeline?

**17:14** · I think absolutely. I think actually a really great example is the erdo unit distance problem. So for the viewers that don't know like we used an internal model at OpenAI a few weeks ago to uh disprove the unit erdos unit distance conjecture. Now, I'm not a mathematician, but this seems like it was a pretty big deal in the in the math community. It was like the first uh first problem that a lot of mathematicians had really spent a lot of time on, and the model was able to do something that they weren't able to do and do it in a way that was actually interesting and useful for mathematicians. Honestly, it did it at a budget that was dirt cheap.

**17:45** · I mean, we didn't put a lot of effort into this. We just we trained a new model and we were just curious what it could do. And we ran it through some problems. And this one at a pretty low budget, it was like, "Oh, yeah. I think I have a disproof."

**17:56** · And then we were able to verify that yeah that this proof is correct after we announced the results a bunch of people found that you could get the answer out of 5.5 as well if now it's not as simple as just asking 5.5 hey here's the unit distance conjecture what's the disproof you had to scaffold it a bit you had to like steer it a bit and so somebody found okay you ask 5.5 list a bunch of

**18:22** · ways that you could tackle this problem and then for it it lists one of the paths that are actually promising to get to the disproof and then you tell it like okay explore this some more and then if you do this enough times it actually ends up arriving at the disproof. Now what this means is you could in principle ask 5.5 to you know as as a general purpose scaffold list a bunch of different strategies and then for each strategy tell it to investigate that strategy and then it would probably be able to arrive at the disproof with a general purpose scaffold.

**18:53** · Now that scaffold would be very expensive. I mean it would probably cost I I just ballpark like thousand to 10 to $100,000. Um but it would be possible and it would have been possible for somebody to disprove the erdos unit distance conjecture before we did using a general purpose model. And nobody had explored sufficiently what happens if I put $100,000 worth of compute into 5.5 what could it do? Um and the answer is like yeah you probably could get stuff like that out of it.

**19:20** · So people should be experimenting more with the current generation in terms of well this is I think is an interesting question of is it worth it to experiment with because again the model release cycle is every every couple months we put out a new model that's even more powerful and so the cost of disproving the erdosha distance gesture drops by like 10 or 100x with every model release cycle probably in some cases more so you've seen the meme that's like oh I like why why bother doing any engineering work when I should just wait for the next model go on vacation come back two months later and and it's, you know, a thousand times cheaper.

**19:51** · So, do you agree with that?

**19:54** · I Is that what you're doing right now at OpenAI, just waiting for the next model release?

**19:58** · I think I I mean, I will say we're we're in a period where progress is very fast and like yeah, the models are becoming more capable. I I can say like at OpenAI one of the things that we're we're actively not doing and look we have a lot of mathematicians we have a lot of physicists people are very excited about what these models can do right now especially you know the internal models we are trying to encourage people to not spend all their time just like going through all the mathematical open problems physics problems and um just seeing pushing the models to their limits to see what they can prove or disprove.

**20:26** · Um because we really think the focus should be on how do we make even more capable models? how can we get them get them out safely to the world as quickly as possible so that all the scientists in the world can use these models to solve the problems themselves.

**20:38** · Uh so yeah in some sense we are thinking about this that yes it's really tempting to um just put all of our efforts into scaling up these models and see what they can do at their limits right now but really the focus should be on how do we use these models to make even more powerful models even more capable models that can do everything much more cost-ffectively.

### Limits on Recursive Self-Improvement

**20:59** · What is changing about the uh direction or allocation of resources for research in your mind given your beliefs about this very large scale the impact of very large scale test time compute? How does this interact with the um idea of recursive self-improvement for example where you know it's a dominant idea for how you know any lab gets to the best capability model.

**21:22** · So, one thing I should clarify, I don't think we're at the point where, okay, you just give it an arbitrary extremely high inference budget and it's just it's just super intelligent across the board.

**21:32** · SL goal, yeah, make GPD 7 or whatever and yeah, just go nuts.

**21:37** · What's between us and there then?

**21:39** · I think having played around with the model uh so okay, so first of all, there are some benchmarks where the models will just not improve if they have more inference budget. So, I think a lot of factual ret uh factual um retrieval kind of questions fall into this category of if you ask a person when was Abraham Lincoln born and they don't know the date. They could sit there, they could think about it for a week, if they if they don't have access to Wikipedia or something, they're not going to be able to do better answering that question if they thought about it for a week compared to 5 seconds. Same with the model.

**22:10** · If you actually, interestingly enough, if you give the model these kinds of like factual retrieval questions and you give them a little bit of time to think, they do actually do better. um but if you give them a week they're not suddenly going to do better at remembering dates. There are so there's some benchmarks where they clearly improve with more test time compute and there's some where they don't. I think on the other extreme there are um benchmarks where they kind of obviously will keep improving limit uh without limit with more test time compute. So the example I like to point to is sudoku.

**22:37** · If you uh it's there's a really simple strategy to solving Sudoku which is just try a bunch of different random numbers and then see if it fits the criteria. If it if it matches all the constraints and if it doesn't just try a different random combination of numbers and clearly with enough time you will be able to solve any puzzle with this strategy. You can kind of trivally see like okay any model could keep doing better and better um if it was just given more test time compute.

**23:02** · So you have and and all the benchmarks kind of exist somewhere between these two extremes. the models are not at the level where if you just give them enough test time on compute they will be able to do um all of our jobs just because yeah there's some benchmarks where they will not improve there are some things where they they will not improve one thing I see for research in particular is they don't have very good research taste right now and so I think they're actually a very good complement to researchers especially um you know I've

**23:29** · found like I've found I'm much more effective by using these models but they're not able to fully replace the whole research cycle Now, does that change with time?

**23:39** · Probably. I mean, I think the models are getting better across the board. Some some things are getting better the faster than others. Um, but they're not at the point where they're fully replacing uh researchers with just enough test time compute.

**23:52** · Can you give um an example or two of like asking the model to do a research test for just like this is this is a terrible idea? I mean I I think going back to my poker solver example, I was really impressed with the model's ability to optimize the algorithms that I had developed in my in my PhD. It was honestly it it was it was shocking to see how inefficient I was um in retrospect and they were able to make it like you know 10 100x faster.

**24:18** · And then I was like, okay, can you come up with an algorithm that is better than the algorithms that I came up with or that anybody else came up with and go ahead and like look at all the published work and synthesize that and then try to come up with something novel and it it's not able to do it. And I can give it a lot of time and it's it's still not able to do it. Now, it's possible that if I scaffolded something and like kind of constrained it a bit more that maybe it could eventually come up with something better.

**24:46** · Um, but it would take a lot of it's not just as simple as saying, "Okay, please come up with a better algorithm."

**24:52** · And how do you think that that gets improved?

**24:55** · What I've seen is with every model release cycle, um, it does get better at this sort of thing. It's still it's still bad in my opinion, but it it's not as bad as it used to be. And I wouldn't be surprised if at some point, same thing with coding, same thing with math, where there's just like this inflection point where suddenly it's actually good enough to be useful. Um I wouldn't be surprised if we encounter that point for research taste as well.

**25:18** · Given that what do you like what is your framing of RSI today? Like how should we think about it?

**25:24** · The models are definitely accelerating what researchers can do inside the labs.

**25:28** · But I think they are accelerating some things and not other things. And currently we're at the point where okay if something goes 100x faster you get bottlenecked by the things that don't go 100x faster. over time the things that we're getting bottlenecked on are going to shrink and and there will be I think um a kind of a gradual takeoff in that respect but it's more about transforming right now it's more about transforming what researchers do rather than fully replacing the researchers so that actually implies that you don't

**25:55** · think we're close to a very fast takeoff right now I think fast takeoff is relative things are moving very fast but I think there is this hypothesis that you could have basically an overnight intelligence explosion where the models discover some kind of breakthrough through to make themselves smarter and then that leads to more breakthroughs that make themselves even smarter immediately and you have basically in an instance the models just you know becoming very superhuman across the board uh in in moments and I don't think we're headed to that world largely because of the

**26:25** · fact that the models rely so much on large scale test time compute in order to achieve um their greatest intelligence. If you if it requires so much test time on compute to unlock the full capabilities of the model, then that means you're bottlenecked by time um things can only go so fast because the models need to run for long enough to um to actually do something really really powerful.

**26:46** · Time itself becomes a bottleneck to what we can do and I I think that is the case right now for a lot of the labs that ultimately I think the biggest bottleneck for all of us is time and that's why all the researchers are working so intensely right now. It's it's just so many um so many hours per week are being put into this because we all see what the overhang is. We see what the capabilities are and we're just bottlenecked by how quickly can we do things.

### Large-Scale Multi-Agent Coordination

**27:10** · What do you think is on the frontier um that is less explored now? Like we've talked about multi-agent before.

**27:17** · I think multi-agent is quite explored.

**27:20** · Um I think at sufficient scale, I think there's a lot more that could be done. Um, but it's also one of the things that's that's hard to do at a lot of research is hard to do at small skin.

**27:31** · I think multi- agent in particular, it really requires in order to fully unlock the cubilities. I think requires like frontier models. I think we've seen some pretty interesting multi- aent scaffolds. I think um they're able to do a lot, but I think it's really just scratching the surface of what it will be able to do. I mean, one way that I think about it is if if you look at human civilization, it's not that humans have become smarter over it's not that they evolved to become smarter over, you know, the past 50,000 years.

**27:57** · It's that humans are able to do a lot more today than they were back in caveman times because there have been billions of humans thinking for a long time and building off of each other's accumulated knowledge.

**28:11** · We have like very good retrieval and scaffolding versus 50,000 years ago. Uh it's not even I wouldn't even call it a scaffold. It's just like this is a very like organic emerging property of just like humans being able to accumulate knowledge, share it, um and build off of it. We're not seeing that with AI models today. They kind of they're they're born into a world for and they exist for a very short context window and then they just like disappear.

**28:36** · And yeah, there are things that you can kind of do to like continue them, but it's very limited. I do think eventually we will and we're starting to see like signs that we're entering a world where they can coordinate on a large scale. I think multbook and open claw when they first came out I think it was obviously a bit overhyped but they were um an indication of where things could go in the future and I do think that eventually we get to that kind of world of some sort of coordinated compounding state.

**29:04** · Yeah. uh the ability of the models to to share knowledge um on a more global level and be able to build on that knowledge productively.

### Competition at the Frontier

**29:12** · Given this set of beliefs and your work like uh how would you characterize just competition at the frontier between the between the three kingdoms if there is no overnight takeoff? It's just researchers grinding away trying to make good high taste algorithmic and investment decisions about where to go and then compute allocation and then policy decisions and eval decisions.

**29:39** · Um that feels like slightly more grounded than um uh I support I suppose like racing towards some immediate hard takeoff that nobody can catch you on.

**29:48** · I think the competition is very intense right now. I do think the models that exist today um are accelerating what researchers at the Frontier Labs can do.

**29:58** · Um there's obviously like I said limits to that right now, but it the ability to use the models to improve the model research is a real thing and it's um it it is like an amplifying force. I think that will continue to be true. I think they'll become more true over time. One thing that I am comforted by is I think all the researchers at the frontier labs like all the frontier labs I think recognize what is at stake and what these models like what what the uh what the risks are and that's something that

**30:27** · I I find comforting that I think everybody really understands like okay this is a pretty serious thing and it can lead to really great things or it can lead to really bad things and yes there's a competitive dynamic between the labs but like we can also try to figure out how we all get to the positive outcomes rather than the very negative outcomes.

**30:42** · I I think you know I'd be remiss to ask just because you have been right very early for a long time um on the importance of test time compute and reasoning as a framework like are there ways in which you use the

**30:57** · models that you should you would encourage others to right is it just goal everything I think for a lot of people they worked I mean this is probably not even true for your audience necessarily but there's a lot of people that experimented with AI back in like 2012 23 and felt like they couldn't trust the outputs and then don't use it for really high stakes decisions. And actually, I think the models have progressed to a point where they are very good for these kinds of things.

**31:22** · I mean, I asked them tax advice or I bought a condo recently and I was asking it for advice on like, okay, well, what's all the paperwork that I have to fill out and like how to how do I what does it all mean? It's actually really good for these kinds of questions. Mhm.

**31:36** · So, I use it dayto-day for for a lot of this kind of stuff. And I think they're at a point now where they've actually been at a point for a while now where I feel like I can just trust the outputs arguably more than I could trust the output from from a human, an expert human. Yeah.

### Breaking the Benchmark Grid Equilibrium

**31:51** · Okay.

**31:51** · I have two two final questions for you. Um, one is uh is there something you think that the rest of the research community doesn't agree with you on or doesn't understand the importance of quite yet? Oh, these are such good questions. I wish I had time to think about this ahead of time.

**32:07** · You can you can just hang out with me and think about it. Yeah.

**32:10** · Is it weird to be like consensus now?

**32:12** · You're a bit salty three years ago when you're like, why don't people understand how important this is?

**32:16** · I still I still feel like it's not consensus though because like you know people still don't publish the benchmarks this way.

**32:21** · Oh, that's true. Yeah.

**32:23** · Like that's actually why I think that's like inertia.

**32:25** · That's kind of Yeah, but that's kind of why I wrote the essay. I was just like look I mean we can talk about this but like yeah the part of the motivation is like I would talk to researchers about um we it makes sense to show the benchmarks with an x-axis whether it's tokens or cost or time there should be an x-axis and everybody would say like yeah that makes sense we should do that but everybody they're not acting with the importance of like good heart like this is we have to measure the correct thing well really their response is people expect us to to publish the grid

**32:53** · and then okay why do people expect the grid to be published because everybody publishes the grid. And so you kind of end up in this this bad equilibrium where everybody kind of knows that it's a bad equilibrium, but like nobody wants to break out. And I I felt like, okay, well, if I just hopefully come out and say like, look guys, let's all recognize that we're in a bad equilibrium and let's move to this different equilibrium where we're we're plotting things with an X-axis that hopefully that can, you know, next time there's a model release, a company can feel comfortable not publishing the grid, at least not at the very front uh the top line. and um we

**33:26** · can have a more productive evaluation of these models.

### Why Benchmarks Should be Evaluated by Cost

**33:29** · Then a last question for you. How do you think about companies across all of these specialized domains who feel the value that they have is essentially like the routing layer, the choice layer of you know my goal is composed of a bunch of discrete tasks.

**33:51** · Some require more intelligence and less and within my my job as a vendor is to um solve that problem or achieve the optimal outcome with uh taking into account the budget constraints. And so I will manage like the parallelization and how how much inference do you spend on it from what model because I I think the the frontier lab point of view is that that routing happens both within the you know behind

**34:21** · the API behind the application and then some of it in the model itself. Um and that's pieces of that are clearly being externalized in all these applications.

**34:30** · Yeah, I do I do think this is related to the fact that like benchmarks should be evaluated with an x-axis of tokens or cost. Um I I have seen some evals recently that show like okay well with with a routing layer you can achieve much better performance um by basically doing consensus among the models.

**34:46** · Yeah.

**34:46** · And like I definitely believe that if you do consensus among the models that you're going to achieve better performance than any individual model but it's important to ask like are you going to do better than having that model basically think for longer. Um like once you control for the amount of test time compute is it is it actually still doing better? That's that's the question that you want to figure out. Okay, that's very principle of view which is like yes routing is fine but it's all subject to the same budget question. Yeah, right. Um if you put it on the same scaler then you can make an optimal decision and I think maybe I win.

**35:15** · Mhm.

**35:15** · I I I don't even know necessarily that I I would believe that the routing does better but then there's still a question of um is it going to do significantly better? Is it very fragile? Is it um reflective of real world use cases compared to benchmarks?

**35:28** · because like one issue you could run into is that you could optimize for certain benchmarks with the routing and then show like oh yeah we see this big improvement on these benchmarks. Um but in real world use cases it actually ends up not being a significant improvement.

**35:39** · So I I would say at the very least like I would say you want to control for testime compute and then you also want to have all the same um skepticism about benchmarks that you would normally have.

**35:50** · Awesome. N thanks so much and and for being on the mission for uh breaking us out of this false equilibrium. Yeah, it's great to be back.

**36:00** · Find us on Twitter at no prior pod. Subscribe to our YouTube channel if you want to see our faces. Follow the show on Apple Podcasts, Spotify, or wherever you listen. That way, you get a new episode every week. And sign up for emails or find transcripts for every episode at no-briers.com.
