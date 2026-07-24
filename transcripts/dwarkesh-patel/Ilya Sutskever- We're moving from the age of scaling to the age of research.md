---
title: Ilya Sutskever – We're moving from the age of scaling to the age of research
source_url: https://www.youtube.com/watch?v=aR20FWCCjAs
video_id: aR20FWCCjAs
account: '[[accounts/dwarkesh-patel|Dwarkesh Patel]]'
account_name: Dwarkesh Patel
account_url: https://www.youtube.com/@DwarkeshPatel
featured_people:
- '[[people/ilya-sutskever|Ilya Sutskever]]'
published: 2025-11-26
created: 2026-07-21
language: en
speaker_attribution: contextual
description: 'Ilya & I discuss SSI’s strategy, the problems with pre-training, how to improve the generalization of AI models, and how to ensure AGI goes well.𝐄𝐏𝐈𝐒𝐎𝐃𝐄 𝐋𝐈𝐍𝐊𝐒* Transcript: https://www.d'
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=aR20FWCCjAs)

Ilya & I discuss SSI’s strategy, the problems with pre-training, how to improve the generalization of AI models, and how to ensure AGI goes well.  
  
𝐄𝐏𝐈𝐒𝐎𝐃𝐄 𝐋𝐈𝐍𝐊𝐒  
\* Transcript: https://www.dwarkesh.com/p/ilya-sutskever-2  
\* Apple Podcasts: https://podcasts.apple.com/us/podcast/dwarkesh-podcast/id1516093381?i=1000738363711  
\* Spotify: https://open.spotify.com/episode/7naOOba8SwiUNobGz8mQEL?si=39dd68f346ea4d49  
  
𝐒𝐏𝐎𝐍𝐒𝐎𝐑𝐒  
\- Gemini 3 is the first model I’ve used that can find connections I haven’t anticipated. I recently wrote a blog post on RL’s information efficiency, and Gemini 3 helped me think it all through. It also generated the relevant charts and ran toy ML experiments for me with zero bugs. Try Gemini 3 today at https://gemini.google  
\- Labelbox helped me create a tool to transcribe our episodes! I’ve struggled with transcription in the past because I don’t just want verbatim transcripts, I want transcripts reworded to read like essays. Labelbox helped me generate the \*exact\* data I needed for this. If you want to learn how Labelbox can help you (or if you want to try out the transcriber tool yourself), go to https://labelbox.com/dwarkesh  
\- Sardine is an AI risk management platform that brings together thousands of device, behavior, and identity signals to help you assess a user’s risk of fraud & abuse. Sardine also offers a suite of agents to automate investigations so that as fraudsters use AI to scale their attacks, you can use AI to scale your defenses. Learn more at https://sardine.ai/dwarkesh  
  
To sponsor a future episode, visit https://dwarkesh.com/advertise  
  
𝐓𝐈𝐌𝐄𝐒𝐓𝐀𝐌𝐏𝐒  
00:00:00 – Explaining model jaggedness  
00:09:39 - Emotions and value functions  
00:18:49 – What are we scaling?  
00:25:13 – Why humans generalize better than models  
00:35:45 – Straight-shotting superintelligence  
00:46:47 – SSI’s model will learn from deployment  
00:55:07 – Alignment  
01:18:13 – “We are squarely an age of research company”  
01:29:23 -- Self-play and multi-agent  
01:32:42 – Research taste

## Transcript

### Explaining model jaggedness

**0:00** · You know what's crazy? That all of this is real. Meaning what?

**0:05** · Don't you think so? All this AI stuff and all this Bay Area… that it's happening.

**0:11** · Isn't it straight out of science fiction? Another thing that's crazy is how normal the slow takeoff feels. The idea that we'd be investing 1% of GDP in AI, I feel like it would have felt like a bigger deal, whereas right now it just feels...

**0:26** · We get used to things pretty fast, it turns out. But also it's kind of abstract. What does it mean? It means that you see it in the news, that such and such company announced such and such dollar amount. That's all you see. It's not really felt in any other way so far.

**0:45** · Should we actually begin here? I think this is an interesting discussion.

**0:48** · Sure. I think your point, about how from the average person's point of view nothing is that different, will continue being true even into the singularity. No, I don't think so.

**0:58** · Okay, interesting. The thing which I was referring to not feeling different is, okay, such and such company announced some difficult-to-comprehend dollar amount of investment. I don't think anyone knows what to do with that.

**1:15** · But I think the impact of AI is going to be felt. AI is going to be diffused through the economy.

**1:24** · There'll be very strong economic forces for this, and I think the impact is going to be felt very strongly. When do you expect that impact?

**1:32** · I think the models seem smarter than their economic impact would imply.

**1:38** · Yeah. This is one of the very confusing things about the models right now.

**1:44** · How to reconcile the fact that they are doing so well on evals?

**1:53** · You look at the evals and you go, "Those are pretty hard evals." They are doing so well. But the economic impact seems to be dramatically behind.

**2:07** · It's very difficult to make sense of, how can the model, on the one hand, do these amazing things, and then on the other hand, repeat itself twice in some situation?

**2:20** · An example would be, let's say you use vibe coding to do something.

**2:24** · You go to some place and then you get a bug. Then you tell the model, "Can you please fix the bug?" And the model says, "Oh my God, you're so right. I have a bug. Let me go fix that." And it introduces a second bug.

**2:36** · Then you tell it, "You have this new second bug," and it tells you, "Oh my God, how could I have done it? You're so right again," and brings back the first bug, and you can alternate between those. How is that possible? I'm not sure, but it does suggest that something strange is going on. I have two possible explanations. The more whimsical explanation is that maybe RL training makes the models a little too single-minded and narrowly focused, a little bit too unaware, even though it also makes them aware in some other ways.

**3:17** · Because of this, they can't do basic things. But there is another explanation. Back when people were doing pre-training, the question of what data to train on was answered, because that answer was everything. When you do pre-training, you need all the data.

**3:41** · So you don't have to think if it's going to be this data or that data.

**3:44** · But when people do RL training, they do need to think.

**3:48** · They say, "Okay, we want to have this kind of RL training for this thing and that kind of RL training for that thing." From what I hear, all the companies have teams that just produce new RL environments and just add it to the training mix.

**4:02** · The question is, well, what are those? There are so many degrees of freedom.

**4:06** · There is such a huge variety of RL environments you could produce.

**4:12** · One thing you could do, and I think this is something that is done inadvertently, is that people take inspiration from the evals. You say, "Hey, I would love our model to do really well when we release it. I want the evals to look great.

**4:28** · What would be RL training that could help on this task?"

**4:33** · I think that is something that happens, and it could explain a lot of what's going on.

**4:39** · If you combine this with generalization of the models actually being inadequate, that has the potential to explain a lot of what we are seeing, this disconnect between eval performance and actual real-world performance, which is something that we don't today even understand, what we mean by that. I like this idea that the real reward hacking is the human researchers who are too focused on the evals.

**5:09** · I think there are two ways to understand, or to try to think about, what you have just pointed out. One is that if it's the case that simply by becoming superhuman at a coding competition, a model will not automatically become more tasteful and exercise better judgment about how to improve your codebase, well then you should expand the suite of environments such that you're not just testing it on having the best performance in coding competition. It should also be able to make the best kind of application for X thing or Y thing or Z thing.

**5:38** · Another, maybe this is what you're hinting at, is to say, "Why should it be the case in the first place that becoming superhuman at coding competitions doesn't make you a more tasteful programmer more generally?"

**5:54** · Maybe the thing to do is not to keep stacking up the amount and diversity of environments, but to figure out an approach which lets you learn from one environment and improve your performance on something else. I have a human analogy which might be helpful.

**6:14** · Let's take the case of competitive programming, since you mentioned that. Suppose you have two students. One of them decided they want to be the best competitive programmer, so they will practice 10,000 hours for that domain. They will solve all the problems, memorize all the proof techniques, and be very skilled at quickly and correctly implementing all the algorithms.

**6:40** · By doing so, they became one of the best. Student number two thought, "Oh, competitive programming is cool." Maybe they practiced for 100 hours, much less, and they also did really well. Which one do you think is going to do better in their career later on? The second.

**6:56** · Right. I think that's basically what's going on. The models are much more like the first student, but even more. Because then we say, the model should be good at competitive programming so let's get every single competitive programming problem ever.

**7:10** · And then let's do some data augmentation so we have even more competitive programming problems, and we train on that. Now you've got this great competitive programmer.

**7:18** · With this analogy, I think it's more intuitive. Yeah, okay, if it's so well trained, all the different algorithms and all the different proof techniques are right at its fingertips.

**7:32** · And it's more intuitive that with this level of preparation, it would not necessarily generalize to other things. But then what is the analogy for what the second student is doing before they do the 100 hours of fine-tuning?

**7:48** · I think they have "it." The "it" factor. When I was an undergrad, I remember there was a student like this that studied with me, so I know it exists.

**8:01** · I think it's interesting to distinguish "it" from whatever pre-training does.

**8:06** · One way to understand what you just said about not having to choose the data in pre-training is to say it's actually not dissimilar to the 10,000 hours of practice.

**8:15** · It's just that you get that 10,000 hours of practice for free because it's already somewhere in the pre-training distribution. But maybe you're suggesting there's actually not that much generalization from pre-training. There's just so much data in pre-training, but it's not necessarily generalizing better than RL. The main strength of pre-training is that: A, there is so much of it, and B, you don't have to think hard about what data to put into pre-training. It's very natural data, and it does include in it a lot of what people do: people's thoughts and a lot of the features.

**8:54** · It's like the whole world as projected by people onto text, and pre-training tries to capture that using a huge amount of data. Pre-training is very difficult to reason about because it's so hard to understand the manner in which the model relies on pre-training data.

**9:17** · Whenever the model makes a mistake, could it be because something by chance is not as supported by the pre-training data? "Support by pre-training" is maybe a loose term.

**9:30** · I don't know if I can add anything more useful on this.

**9:36** · I don't think there is a human analog to pre-training.

### Emotions and value functions

**9:39** · Here are analogies that people have proposed for what the human analogy to pre-training is.

**9:43** · I'm curious to get your thoughts on why they're potentially wrong.

**9:47** · One is to think about the first 18, or 15, or 13 years of a person's life when they aren't necessarily economically productive, but they are doing something that is making them understand the world better and so forth. The other is to think about evolution as doing some kind of search for 3 billion years, which then results in a human lifetime instance.

**10:14** · I'm curious if you think either of these are analogous to pre-training.

**10:18** · How would you think about what lifetime human learning is like, if not pre-training?

**10:22** · I think there are some similarities between both of these and pre-training, and pre-training tries to play the role of both of these. But I think there are some big differences as well. The amount of pre-training data is very, very staggering. Yes.

**10:41** · Somehow a human being, after even 15 years with a tiny fraction of the pre-training data, they know much less. But whatever they do know, they know much more deeply somehow. Already at that age, you would not make mistakes that our AIs make. There is another thing. You might say, could it be something like evolution? The answer is maybe. But in this case, I think evolution might actually have an edge.

**11:08** · I remember reading about this case. One way in which neuroscientists can learn about the brain is by studying people with brain damage to different parts of the brain.

**11:26** · Some people have the most strange symptoms you could imagine. It's actually really, really interesting. One case that comes to mind that's relevant.

**11:35** · I read about this person who had some kind of brain damage, a stroke or an accident, that took out his emotional processing. So he stopped feeling any emotion.

**11:54** · He still remained very articulate and he could solve little puzzles, and on tests he seemed to be just fine. But he felt no emotion. He didn't feel sad, he didn't feel anger, he didn't feel animated. He became somehow extremely bad at making any decisions at all. It would take him hours to decide on which socks to wear. He would make very bad financial decisions.

**12:23** · What does it say about the role of our built-in emotions in making us a viable agent, essentially?

**12:34** · To connect to your question about pre-training, maybe if you are good enough at getting everything out of pre-training, you could get that as well. But that's the kind of thing which seems...

**12:50** · Well, it may or may not be possible to get that from pre-training.

**12:56** · What is "that"? Clearly not just directly emotion. It seems like some almost value function-like thing which is telling you what the end reward for any decision should be.

**13:12** · You think that doesn't sort of implicitly come from pre-training?

**13:15** · I think it could. I'm just saying it's not 100% obvious.

**13:20** · But what is that? How do you think about emotions? What is the ML analogy for emotions?

**13:26** · It should be some kind of a value function thing. But I don’t think there is a great ML analogy because right now, value functions don't play a very prominent role in the things people do.

**13:36** · It might be worth defining for the audience what a value function is, if you want to do that.

**13:40** · Certainly, I'll be very happy to do that. When people do reinforcement learning, the way reinforcement learning is done right now, how do people train those agents?

**13:56** · You have your neural net and you give it a problem, and then you tell the model, "Go solve it." The model takes maybe thousands, hundreds of thousands of actions or thoughts or something, and then it produces a solution. The solution is graded. And then the score is used to provide a training signal for every single action in your trajectory. That means that if you are doing something that goes for a long time—if you're training a task that takes a long time to solve—it will do no learning at all until you come up with the proposed solution.

**14:33** · That's how reinforcement learning is done naively. That's how o1, R1 ostensibly are done.

**14:40** · The value function says something like, "Maybe I could sometimes, not always, tell you if you are doing well or badly." The notion of a value function is more useful in some domains than others. For example, when you play chess and you lose a piece, I messed up. You don't need to play the whole game to know that what I just did was bad, and therefore whatever preceded it was also bad.

**15:08** · The value function lets you short-circuit the wait until the very end.

**15:19** · Let's suppose that you are doing some kind of a math thing or a programming thing, and you're trying to explore a particular solution or direction.

**15:26** · After, let's say, a thousand steps of thinking, you concluded that this direction is unpromising.

**15:34** · As soon as you conclude this, you could already get a reward signal a thousand timesteps previously, when you decided to pursue down this path.

**15:43** · You say, "Next time I shouldn't pursue this path in a similar situation," long before you actually came up with the proposed solution. This was in the DeepSeek R1 paper— that the space of trajectories is so wide that maybe it's hard to learn a mapping from an intermediate trajectory and value. And also given that, in coding for example you'll have the wrong idea, then you'll go back, then you'll change something.

**16:12** · This sounds like such lack of faith in deep learning.

**16:16** · Sure it might be difficult, but nothing deep learning can't do.

**16:23** · My expectation is that a value function should be useful, and I fully expect that they will be used in the future, if not already. What I was alluding to with the person whose emotional center got damaged, it’s more that maybe what it suggests is that the value function of humans is modulated by emotions in some important way that's hardcoded by evolution.

**16:55** · And maybe that is important for people to be effective in the world.

**17:00** · That's the thing I was planning on asking you.

**17:02** · There's something really interesting about emotions of the value function, which is that it's impressive that they have this much utility while still being rather simple to understand.

**17:16** · I have two responses. I do agree that compared to the kind of things that we learn and the things we are talking about, the kind of AI we are talking about, emotions are relatively simple.

**17:31** · They might even be so simple that maybe you could map them out in a human-understandable way.

**17:35** · I think it would be cool to do. In terms of utility though, I think there is a thing where there is this complexity-robustness tradeoff, where complex things can be very useful, but simple things are very useful in a very broad range of situations.

**18:00** · One way to interpret what we are seeing is that we've got these emotions that evolved mostly from our mammal ancestors and then fine-tuned a little bit while we were hominids, just a bit.

**18:13** · We do have a decent amount of social emotions though which mammals may lack. But they're not very sophisticated. And because they're not sophisticated, they serve us so well in this very different world compared to the one that we've been living in. Actually, they also make mistakes. For example, our emotions… Well actually, I don’t know.

**18:32** · Does hunger count as an emotion? It's debatable. But I think, for example, our intuitive feeling of hunger is not succeeding in guiding us correctly in this world with an abundance of food.

### What are we scaling?

**18:50** · People have been talking about scaling data, scaling parameters, scaling compute.

**18:56** · Is there a more general way to think about scaling?

**18:58** · What are the other scaling axes? Here's a perspective that I think might be true.

**19:12** · The way ML used to work is that people would just tinker with stuff and try to get interesting results. That's what's been going on in the past. Then the scaling insight arrived. Scaling laws, GPT-3, and suddenly everyone realized we should scale.

**19:40** · This is an example of how language affects thought. "Scaling" is just one word, but it's such a powerful word because it informs people what to do.

**19:51** · They say, "Let's try to scale things." So you say, what are we scaling?

**19:57** · Pre-training was the thing to scale. It was a particular scaling recipe.

**20:02** · The big breakthrough of pre-training is the realization that this recipe is good.

**20:08** · You say, "Hey, if you mix some compute with some data into a neural net of a certain size, you will get results. You will know that you'll be better if you just scale the recipe up." This is also great. Companies love this because it gives you a very low-risk way of investing your resources. It's much harder to invest your resources in research. Compare that. If you research, you need to be like, "Go forth researchers and research and come up with something", versus get more data, get more compute.

**20:45** · You know you'll get something from pre-training. Indeed, it looks like, based on various things some people say on Twitter, maybe it appears that Gemini have found a way to get more out of pre-training. At some point though, pre-training will run out of data. The data is very clearly finite. What do you do next? Either you do some kind of souped-up pre-training, a different recipe from the one you've done before, or you're doing RL, or maybe something else.

**21:15** · But now that compute is big, compute is now very big, in some sense we are back to the age of research. Maybe here's another way to put it.

**21:24** · Up until 2020, from 2012 to 2020, it was the age of research.

**21:31** · Now, from 2020 to 2025, it was the age of scaling—maybe plus or minus, let's add error bars to those years—because people say, "This is amazing. You've got to scale more. Keep scaling." The one word: scaling. But now the scale is so big.

**21:46** · Is the belief really, "Oh, it's so big, but if you had 100x more, everything would be so different?"

**21:53** · It would be different, for sure. But is the belief that if you just 100x the scale, everything would be transformed? I don't think that's true. So it's back to the age of research again, just with big computers. That's a very interesting way to put it.

**22:10** · But let me ask you the question you just posed then.

**22:12** · What are we scaling, and what would it mean to have a recipe?

**22:17** · I guess I'm not aware of a very clean relationship that almost looks like a law of physics which existed in pre-training. There was a power law between data or compute or parameters and loss. What is the kind of relationship we should be seeking, and how should we think about what this new recipe might look like?

**22:40** · We've already witnessed a transition from one type of scaling to a different type of scaling, from pre-training to RL. Now people are scaling RL. Now based on what people say on Twitter, they spend more compute on RL than on pre-training at this point, because RL can actually consume quite a bit of compute. You do very long rollouts, so it takes a lot of compute to produce those rollouts. Then you get a relatively small amount of learning per rollout, so you really can spend a lot of compute.

**23:21** · I wouldn't even call it scaling. I would say, "Hey, what are you doing?

**23:27** · Is the thing you are doing the most productive thing you could be doing?

**23:31** · Can you find a more productive way of using your compute?"

**23:36** · We've discussed the value function business earlier.

**23:39** · Maybe once people get good at value functions, they will be using their resources more productively. If you find a whole other way of training models, you could say, "Is this scaling or is it just using your resources?"

**23:56** · I think it becomes a little bit ambiguous. In the sense that, when people were in the age of research back then, it was, "Let's try this and this and this.

**24:03** · Let's try that and that and that. Oh, look, something interesting is happening."

**24:07** · I think there will be a return to that. If we're back in the era of research, stepping back, what is the part of the recipe that we need to think most about?

**24:17** · When you say value function, people are already trying the current recipe, but then having LLM-as-a-Judge and so forth. You could say that's a value function, but it sounds like you have something much more fundamental in mind.

**24:29** · Should we even rethink pre-training at all and not just add more steps to the end of that process?

**24:38** · The discussion about value function, I think it was interesting.

**24:41** · I want to emphasize that I think the value function is something that's going to make RL more efficient, and I think that makes a difference. But I think anything you can do with a value function, you can do without, just more slowly. The thing which I think is the most fundamental is that these models somehow just generalize dramatically worse than people. It's super obvious. That seems like a very fundamental thing. So this is the crux: generalization. There are two sub-questions.

### Why humans generalize better than models

**25:18** · There's one which is about sample efficiency: why should it take so much more data for these models to learn than humans? There's a second question. Even separate from the amount of data it takes, why is it so hard to teach the thing we want to a model than to a human?

**25:37** · For a human, we don't necessarily need a verifiable reward to be able to… You're probably mentoring a bunch of researchers right now, and you're talking with them, you're showing them your code, and you're showing them how you think. From that, they're picking up your way of thinking and how they should do research. You don’t have to set a verifiable reward for them that's like, "Okay, this is the next part of the curriculum, and now this is the next part of your curriculum. Oh, this training was unstable." There's not this schleppy, bespoke process.

**26:06** · Perhaps these two issues are actually related in some way, but I'd be curious to explore this second thing, which is more like continual learning, and this first thing, which feels just like sample efficiency. You could actually wonder that one possible explanation for the human sample efficiency that needs to be considered is evolution.

**26:31** · Evolution has given us a small amount of the most useful information possible.

**26:38** · For things like vision, hearing, and locomotion, I think there's a pretty strong case that evolution has given us a lot. For example, human dexterity far exceeds… I mean robots can become dexterous too if you subject them to a huge amount of training in simulation.

**27:00** · But to train a robot in the real world to quickly pick up a new skill like a person does seems very out of reach. Here you could say, "Oh yeah, locomotion.

**27:10** · All our ancestors needed great locomotion, squirrels.

**27:15** · So with locomotion, maybe we've got some unbelievable prior."

**27:19** · You could make the same case for vision. I believe Yann LeCun made the point that children learn to drive after 10 hours of practice, which is true.

**27:30** · But our vision is so good. At least for me, I remember myself being a five-year-old. I was very excited about cars back then.

**27:41** · I'm pretty sure my car recognition was more than adequate for driving already as a five-year-old.

**27:47** · You don't get to see that much data as a five-year-old.

**27:49** · You spend most of your time in your parents' house, so you have very low data diversity.

**27:53** · But you could say maybe that's evolution too. But in language and math and coding, probably not.

**28:00** · It still seems better than models. Obviously, models are better than the average human at language, math, and coding. But are they better than the average human at learning? Oh yeah. Oh yeah, absolutely. What I meant to say is that language, math, and coding—and especially math and coding—suggests that whatever it is that makes people good at learning is probably not so much a complicated prior, but something more, some fundamental thing. I'm not sure I understood. Why should that be the case?

**28:30** · So consider a skill in which people exhibit some kind of great reliability. If the skill is one that was very useful to our ancestors for many millions of years, hundreds of millions of years, you could argue that maybe humans are good at it because of evolution, because we have a prior, an evolutionary prior that's encoded in some very non-obvious way that somehow makes us so good at it.

**29:07** · But if people exhibit great ability, reliability, robustness, and ability to learn in a domain that really did not exist until recently, then this is more an indication that people might have just better machine learning, period. How should we think about what that is? What is the ML analogy? There are a couple of interesting things about it. It takes fewer samples. It's more unsupervised. A child learning to drive a car… Children are not learning to drive a car.

**29:47** · A teenager learning how to drive a car is not exactly getting some prebuilt, verifiable reward.

**29:56** · It comes from their interaction with the machine and with the environment.

**30:02** · It takes much fewer samples. It seems more unsupervised. It seems more robust?

**30:07** · Much more robust. The robustness of people is really staggering.

**30:14** · Do you have a unified way of thinking about why all these things are happening at once?

**30:18** · What is the ML analogy that could realize something like this?

**30:26** · One of the things that you've been asking about is how can the teenage driver self-correct and learn from their experience without an external teacher? The answer is that they have their value function.

**30:41** · They have a general sense which is also, by the way, extremely robust in people.

**30:50** · Whatever the human value function is, with a few exceptions around addiction, it's actually very, very robust. So for something like a teenager that's learning to drive, they start to drive, and they already have a sense of how they're driving immediately, how badly they are, how unconfident. And then they see, "Okay." And then, of course, the learning speed of any teenager is so fast. After 10 hours, you're good to go.

**31:17** · It seems like humans have some solution, but I'm curious about how they are doing it and why is it so hard? How do we need to reconceptualize the way we're training models to make something like this possible?

**31:28** · That is a great question to ask, and it's a question I have a lot of opinions about.

**31:37** · But unfortunately, we live in a world where not all machine learning ideas are discussed freely, and this is one of them. There's probably a way to do it.

**31:49** · I think it can be done. The fact that people are like that, I think it's a proof that it can be done. There may be another blocker though, which is that there is a possibility that the human neurons do more compute than we think.

**32:07** · If that is true, and if that plays an important role, then things might be more difficult.

**32:13** · But regardless, I do think it points to the existence of some machine learning principle that I have opinions on. But unfortunately, circumstances make it hard to discuss in detail. Nobody listens to this podcast, Ilya.

**32:32** · I'm curious. If you say we are back in an era of research, you were there from 2012 to 2020.

### Straight-shotting superintelligence

**35:55** · What is the vibe now going to be if we go back to the era of research?

**36:00** · For example, even after AlexNet, the amount of compute that was used to run experiments kept increasing, and the size of frontier systems kept increasing.

**36:13** · Do you think now that this era of research will still require tremendous amounts of compute?

**36:19** · Do you think it will require going back into the archives and reading old papers?

**36:28** · You were at Google and OpenAI and Stanford, these places, when there was more of a vibe of research?

**36:34** · What kind of things should we be expecting in the community?

**36:40** · One consequence of the age of scaling is that scaling sucked out all the air in the room.

**36:53** · Because scaling sucked out all the air in the room, everyone started to do the same thing.

**36:59** · We got to the point where we are in a world where there are more companies than ideas by quite a bit. Actually on that, there is this Silicon Valley saying that says that ideas are cheap, execution is everything.

**37:18** · People say that a lot, and there is truth to that. But then I saw someone say on Twitter something like, "If ideas are so cheap, how come no one's having any ideas?"

**37:30** · And I think it's true too. If you think about research progress in terms of bottlenecks, there are several bottlenecks. One of them is ideas, and one of them is your ability to bring them to life, which might be compute but also engineering.

**37:52** · If you go back to the '90s, let's say, you had people who had pretty good ideas, and if they had much larger computers, maybe they could demonstrate that their ideas were viable.

**38:01** · But they could not, so they could only have a very, very small demonstration that did not convince anyone. So the bottleneck was compute. Then in the age of scaling, compute has increased a lot. Of course, there is a question of how much compute is needed, but compute is large. Compute is large enough such that it's not obvious that you need that much more compute to prove some idea. I'll give you an analogy. AlexNet was built on two GPUs. That was the total amount of compute used for it.

**38:40** · The transformer was built on 8 to 64 GPUs. No single transformer paper experiment used more than 64 GPUs of 2017, which would be like, what, two GPUs of today? The ResNet, right? You could argue that the o1 reasoning was not the most compute-heavy thing in the world.

**39:08** · So for research, you definitely need some amount of compute, but it's far from obvious that you need the absolutely largest amount of compute ever for research.

**39:22** · You might argue, and I think it is true, that if you want to build the absolutely best system then it helps to have much more compute. Especially if everyone is within the same paradigm, then compute becomes one of the big differentiators.

**39:46** · I'm asking you for the history, because you were actually there.

**39:48** · I'm not sure what actually happened. It sounds like it was possible to develop these ideas using minimal amounts of compute. But the transformer didn't immediately become famous. It became the thing everybody started doing and then started experimenting on top of and building on top of because it was validated at higher and higher levels of compute. Correct.

**40:07** · And if you at SSI have 50 different ideas, how will you know which one is the next transformer and which one is brittle, without having the kinds of compute that other frontier labs have?

**40:22** · I can comment on that. The short comment is that you mentioned SSI.

**40:30** · Specifically for us, the amount of compute that SSI has for research is really not that small. I want to explain why. Simple math can explain why the amount of compute that we have is comparable for research than one might think. I'll explain. SSI has raised $3 billion, which is a lot by any absolute sense. But you could say, "Look at the other companies raising much more." But a lot of their compute goes for inference.

**41:13** · These big numbers, these big loans, it's earmarked for inference. That's number one.

**41:20** · Number two, if you want to have a product on which you do inference, you need to have a big staff of engineers, salespeople. A lot of the research needs to be dedicated to producing all kinds of product-related features. So then when you look at what's actually left for research, the difference becomes a lot smaller. The other thing is, if you are doing something different, do you really need the absolute maximal scale to prove it?

**41:51** · I don't think that's true at all. I think that in our case, we have sufficient compute to prove, to convince ourselves and anyone else, that what we are doing is correct.

**42:02** · There have been public estimates that companies like OpenAI spend on the order of $5-6 billion a year just so far, on experiments. This is separate from the amount of money they're spending on inference and so forth. So it seems like they're spending more a year running research experiments than you guys have in total funding.

**42:22** · I think it's a question of what you do with it. It's a question of what you do with it.

**42:29** · In their case, in the case of others, there is a lot more demand on the training compute.

**42:35** · There’s a lot more different work streams, there are different modalities, there is just more stuff. So it becomes fragmented. How will SSI make money?

**42:48** · My answer to this question is something like this. Right now, we just focus on the research, and then the answer to that question will reveal itself. I think there will be lots of possible answers.

**43:01** · Is SSI's plan still to straight shot superintelligence?

**43:05** · Maybe. I think that there is merit to it. I think there's a lot of merit because it's very nice to not be affected by the day-to-day market competition.

**43:17** · But I think there are two reasons that may cause us to change the plan.

**43:25** · One is pragmatic, if timelines turned out to be long, which they might.

**43:31** · Second, I think there is a lot of value in the best and most powerful AI being out there impacting the world. I think this is a meaningfully valuable thing.

**43:46** · So then why is your default plan to straight shot superintelligence?

**43:49** · Because it sounds like OpenAI, Anthropic, all these other companies, their explicit thinking is, "Look, we have weaker and weaker intelligences that the public can get used to and prepare for."

**44:01** · Why is it potentially better to build a superintelligence directly?

**44:06** · I'll make the case for and against. The case for is that one of the challenges that people face when they're in the market is that they have to participate in the rat race.

**44:20** · The rat race is quite difficult in that it exposes you to difficult trade-offs which you need to make. It is nice to say, "We'll insulate ourselves from all this and just focus on the research and come out only when we are ready, and not before."

**44:38** · But the counterpoint is valid too, and those are opposing forces.

**44:43** · The counterpoint is, "Hey, it is useful for the world to see powerful AI.

**44:50** · It is useful for the world to see powerful AI because that's the only way you can communicate it." Well, I guess not even just that you can communicate the idea— Communicate the AI, not the idea. Communicate the AI. What do you mean, "communicate the AI"?

**45:04** · Let's suppose you write an essay about AI, and the essay says, "AI is going to be this, and AI is going to be that, and it's going to be this." You read it and you say, "Okay, this is an interesting essay." Now suppose you see an AI doing this, an AI doing that. It is incomparable. Basically I think that there is a big benefit from AI being in the public, and that would be a reason for us to not be quite straight shot.

**45:36** · I guess it's not even that, but I do think that is an important part of it.

**45:40** · The other big thing is that I can't think of another discipline in human engineering and research where the end artifact was made safer mostly through just thinking about how to make it safe, as opposed to, why airplane crashes per mile are so much lower today than they were decades ago. Why is it so much harder to find a bug in Linux than it would have been decades ago? I think it's mostly because these systems were deployed to the world. You noticed failures, those failures were corrected and the systems became more robust.

**46:11** · I'm not sure why AGI and superhuman intelligence would be any different, especially given—and I hope we're going to get to this—it seems like the harms of superintelligence are not just about having some malevolent paper clipper out there.

**46:29** · But this is a really powerful thing and we don't even know how to conceptualize how people interact with it, what people will do with it. Having gradual access to it seems like a better way to maybe spread out the impact of it and to help people prepare for it.

**46:45** · Well I think on this point, even in the straight shot scenario, you would still do a gradual release of it, that’s how I would imagine it. Gradualism would be an inherent component of any plan. It's just a question of what is the first thing that you get out of the door. That's number one. Number two, I believe you have advocated for continual learning more than other people, and I actually think that this is an important and correct thing. Here is why. I'll give you another example of how language affects thinking.

### SSI’s model will learn from deployment

**47:29** · In this case, it will be two words that have shaped everyone's thinking, I maintain.

**47:37** · First word: AGI. Second word: pre-training. Let me explain. The term AGI, why does this term exist? It's a very particular term. Why does it exist? There's a reason. The reason that the term AGI exists is, in my opinion, not so much because it's a very important, essential descriptor of some end state of intelligence, but because it is a reaction to a different term that existed, and the term is narrow AI.

**48:14** · If you go back to ancient history of gameplay and AI, of checkers AI, chess AI, computer games AI, everyone would say, look at this narrow intelligence. Sure, the chess AI can beat Kasparov, but it can't do anything else. It is so narrow, artificial narrow intelligence.

**48:34** · So in response, as a reaction to this, some people said, this is not good. It is so narrow. What we need is general AI, an AI that can just do all the things.

**48:53** · That term just got a lot of traction. The second thing that got a lot of traction is pre-training, specifically the recipe of pre-training.

**49:03** · I think the way people do RL now is maybe undoing the conceptual imprint of pre-training.

**49:12** · But pre-training had this property. You do more pre-training and the model gets better at everything, more or less uniformly. General AI. Pre-training gives AGI. But the thing that happened with AGI and pre-training is that in some sense they overshot the target.

**49:38** · If you think about the term "AGI", especially in the context of pre-training, you will realize that a human being is not an AGI. Yes, there is definitely a foundation of skills, but a human being lacks a huge amount of knowledge.

**50:00** · Instead, we rely on continual learning. So when you think about, "Okay, so let's suppose that we achieve success and we produce some kind of safe superintelligence."

**50:12** · The question is, how do you define it? Where on the curve of continual learning is it going to be? I produce a superintelligent 15-year-old that's very eager to go. They don't know very much at all, a great student, very eager. You go and be a programmer, you go and be a doctor, go and learn. So you could imagine that the deployment itself will involve some kind of a learning trial-and-error period.

**50:38** · It's a process, as opposed to you dropping the finished thing.

**50:44** · I see. You're suggesting that the thing you're pointing out with superintelligence is not some finished mind which knows how to do every single job in the economy.

**50:58** · Because the way, say, the original OpenAI charter or whatever defines AGI is like, it can do every single job, every single thing a human can do. You're proposing instead a mind which can learn to do every single job, and that is superintelligence.

**51:15** · Yes. But once you have the learning algorithm, it gets deployed into the world the same way a human laborer might join an organization.

**51:25** · Exactly. It seems like one of these two things might happen, maybe neither of these happens. One, this super-efficient learning algorithm becomes superhuman, becomes as good as you and potentially even better, at the task of ML research. As a result the algorithm itself becomes more and more superhuman.

**51:45** · The other is, even if that doesn't happen, if you have a single model—this is explicitly your vision—where instances of a model which are deployed through the economy doing different jobs, learning how to do those jobs, continually learning on the job, picking up all the skills that any human could pick up, but picking them all up at the same time, and then amalgamating their learnings, you basically have a model which functionally becomes superintelligent even without any sort of recursive self-improvement in software. Because you now have one model that can do every single job in the economy and humans can't merge our minds in the same way.

**52:25** · So do you expect some sort of intelligence explosion from broad deployment?

**52:28** · I think that it is likely that we will have rapid economic growth.

**52:37** · I think with broad deployment, there are two arguments you could make which are conflicting.

**52:46** · One is that once indeed you get to a point where you have an AI that can learn to do things quickly and you have many of them, then there will be a strong force to deploy them in the economy unless there will be some kind of a regulation that stops it, which by the way there might be.

**53:13** · But the idea of very rapid economic growth for some time, I think it’s very possible from broad deployment. The question is how rapid it's going to be.

**53:25** · I think this is hard to know because on the one hand you have this very efficient worker.

**53:30** · On the other hand, the world is just really big and there's a lot of stuff, and that stuff moves at a different speed. But then on the other hand, now the AI could… So I think very rapid economic growth is possible. We will see all kinds of things like different countries with different rules and the ones which have the friendlier rules, the economic growth will be faster. Hard to predict. It seems to me that this is a very precarious

### Alignment

**55:10** · situation to be in. In the limit, we know that this should be possible. If you have something that is as good as a human at learning, but which can merge its brains—merge different instances in a way that humans can't merge—already, this seems like a thing that should physically be possible.

**55:28** · Humans are possible, digital computers are possible.

**55:30** · You just need both of those combined to produce this thing.

**55:33** · It also seems this kind of thing is extremely powerful.

**55:41** · Economic growth is one way to put it. A Dyson sphere is a lot of economic growth.

**55:45** · But another way to put it is that you will have, in potentially a very short period of time...

**55:52** · You hire people at SSI, and in six months, they're net productive, probably.

**55:56** · A human learns really fast, and this thing is becoming smarter and smarter very fast.

**56:01** · How do you think about making that go well? Why is SSI positioned to do that well?

**56:05** · What is SSI's plan there, is basically what I'm trying to ask.

**56:12** · One of the ways in which my thinking has been changing is that I now place more importance on AI being deployed incrementally and in advance. One very difficult thing about AI is that we are talking about systems that don't yet exist and it's hard to imagine them.

**56:43** · I think that one of the things that's happening is that in practice, it's very hard to feel the AGI.

**56:52** · It's very hard to feel the AGI. We can talk about it, but imagine having a conversation about how it is like to be old when you're old and frail.

**57:07** · You can have a conversation, you can try to imagine it, but it's just hard, and you come back to reality where that's not the case. I think that a lot of the issues around AGI and its future power stem from the fact that it's very difficult to imagine.

**57:30** · Future AI is going to be different. It's going to be powerful. Indeed, the whole problem, what is the problem of AI and AGI? The whole problem is the power.

**57:43** · The whole problem is the power. When the power is really big, what's going to happen? One of the ways in which I've changed my mind over the past year—and that change of mind, I'll hedge a little bit, may back-propagate into the plans of our company—is that if it's hard to imagine, what do you do?

**58:12** · You’ve got to be showing the thing. You’ve got to be showing the thing.

**58:16** · I maintain that most people who work on AI also can't imagine it because it's too different from what people see on a day-to-day basis. I do maintain, here's something which I predict will happen. This is a prediction. I maintain that as AI becomes more powerful, people will change their behaviors. We will see all kinds of unprecedented things which are not happening right now. I’ll give some examples.

**58:48** · I think for better or worse, the frontier companies will play a very important role in what happens, as will the government.

**59:03** · The kind of things that I think you'll see, which you see the beginnings of, are companies that are fierce competitors starting to collaborate on AI safety.

**59:15** · You may have seen OpenAI and Anthropic doing a first small step, but that did not exist.

**59:22** · That's something which I predicted in one of my talks about three years ago, that such a thing will happen. I also maintain that as AI continues to become more powerful, more visibly powerful, there will also be a desire from governments and the public to do something. I think this is a very important force, of showing the AI. That's number one. Number two, okay, so the AI is being built. What needs to be done? One thing that I maintain that will happen is that right now, people who are working on AI, I maintain that the AI doesn't feel powerful because of its mistakes.

**1:00:06** · I do think that at some point the AI will start to feel powerful actually.

**1:00:10** · I think when that happens, we will see a big change in the way all AI companies approach safety. They'll become much more paranoid. I say this as a prediction that we will see happen. We'll see if I'm right. But I think this is something that will happen because they will see the AI becoming more powerful. Everything that's happening right now, I maintain, is because people look at today's AI and it's hard to imagine the future AI.

**1:00:42** · There is a third thing which needs to happen. I'm talking about it in broader terms, not just from the perspective of SSI because you asked me about our company.

**1:00:54** · The question is, what should the companies aspire to build?

**1:00:58** · What should they aspire to build? There has been one big idea that everyone has been locked into, which is the self-improving AI. Why did it happen?

**1:01:11** · Because there are fewer ideas than companies. But I maintain that there is something that's better to build, and I think that everyone will want that.

**1:01:21** · It's the AI that's robustly aligned to care about sentient life specifically.

**1:01:29** · I think in particular, there's a case to be made that it will be easier to build an AI that cares about sentient life than an AI that cares about human life alone, because the AI itself will be sentient. And if you think about things like mirror neurons and human empathy for animals, which you might argue it's not big enough, but it exists.

**1:01:53** · I think it's an emergent property from the fact that we model others with the same circuit that we use to model ourselves, because that's the most efficient thing to do.

**1:02:03** · So even if you got an AI to care about sentient beings—and it's not actually clear to me that that's what you should try to do if you solved alignment—it would still be the case that most sentient beings will be AIs.

**1:02:16** · There will be trillions, eventually quadrillions, of AIs.

**1:02:19** · Humans will be a very small fraction of sentient beings.

**1:02:23** · So it's not clear to me if the goal is some kind of human control over this future civilization, that this is the best criterion. It's true. It's possible it's not the best criterion. I'll say two things. Number one, care for sentient life, I think there is merit to it. It should be considered. I think it would be helpful if there was some kind of short list of ideas that the companies, when they are in this situation, could use. That’s number two.

**1:03:10** · Number three, I think it would be really materially helpful if the power of the most powerful superintelligence was somehow capped because it would address a lot of these concerns.

**1:03:23** · The question of how to do it, I'm not sure, but I think that would be materially helpful when you're talking about really, really powerful systems. Before we continue the alignment discussion, I want to double-click on that. How much room is there at the top?

**1:03:38** · How do you think about superintelligence? Do you think, using this learning efficiency idea, maybe it is just extremely fast at learning new skills or new knowledge?

**1:03:48** · Does it just have a bigger pool of strategies? Is there a single cohesive "it" in the center that's more powerful or bigger? If so, do you imagine that this will be sort of godlike in comparison to the rest of human civilization, or does it just feel like another agent, or another cluster of agents? This is an area where different people have different intuitions. I think it will be very powerful, for sure.

**1:04:16** · What I think is most likely to happen is that there will be multiple such AIs being created roughly at the same time. I think that if the cluster is big enough—like if the cluster is literally continent-sized—that thing could be really powerful, indeed.

**1:04:39** · If you literally have a continent-sized cluster, those AIs can be very powerful.

**1:04:46** · All I can tell you is that if you're talking about extremely powerful AIs, truly dramatically powerful, it would be nice if they could be restrained in some ways or if there were some kind of agreement or something. What is the concern of superintelligence?

**1:05:11** · What is one way to explain the concern? If you imagine a system that is sufficiently powerful, really sufficiently powerful—and you could say you need to do something sensible like care for sentient life in a very single-minded way—we might not like the results. That's really what it is. Maybe, by the way, the answer is that you do not build an RL agent in the usual sense. I'll point several things out. I think human beings are semi-RL agents.

**1:05:43** · We pursue a reward, and then the emotions or whatever make us tire out of the reward and we pursue a different reward. The market is a very short-sighted kind of agent. Evolution is the same. Evolution is very intelligent in some ways, but very dumb in other ways. The government has been designed to be a never-ending fight between three parts, which has an effect.

**1:06:08** · So I think things like this. Another thing that makes this discussion difficult is that we are talking about systems that don't exist, that we don't know how to build.

**1:06:19** · That’s the other thing and that’s actually my belief.

**1:06:21** · I think what people are doing right now will go some distance and then peter out.

**1:06:26** · It will continue to improve, but it will also not be "it".

**1:06:30** · The "It" we don't know how to build, and a lot hinges on understanding reliable generalization. I’ll say another thing. One of the things that you could say about what causes alignment to be difficult is that your ability to learn human values is fragile.

**1:06:55** · Then your ability to optimize them is fragile. You actually learn to optimize them.

**1:07:00** · And can't you say, "Are these not all instances of unreliable generalization?"

**1:07:06** · Why is it that human beings appear to generalize so much better?

**1:07:10** · What if generalization was much better? What would happen in this case? What would be the effect? But those questions are right now still unanswerable.

**1:07:19** · How does one think about what AI going well looks like?

**1:07:24** · You've scoped out how AI might evolve. We'll have these sort of continual learning agents. AI will be very powerful. Maybe there will be many different AIs.

**1:07:33** · How do you think about lots of continent-sized compute intelligences going around? How dangerous is that? How do we make that less dangerous? And how do we do that in a way that protects an equilibrium where there might be misaligned AIs out there and bad actors out there?

**1:07:56** · Here’s one reason why I liked "AI that cares for sentient life".

**1:08:00** · We can debate on whether it's good or bad. But if the first N of these dramatic systems do care for, love, humanity or something, care for sentient life, obviously this also needs to be achieved. This needs to be achieved. So if this is achieved by the first N of those systems, then I can see it go well, at least for quite some time.

**1:08:32** · Then there is the question of what happens in the long run.

**1:08:36** · How do you achieve a long-run equilibrium? I think that there, there is an answer as well.

**1:08:44** · I don't like this answer, but it needs to be considered.

**1:08:51** · In the long run, you might say, "Okay, if you have a world where powerful AIs exist, in the short term, you could say you have universal high income.

**1:09:01** · You have universal high income and we're all doing well."

**1:09:04** · But what do the Buddhists say? "Change is the only constant." Things change. There is some kind of government, political structure thing, and it changes because these things have a shelf life.

**1:09:18** · Some new government thing comes up and it functions, and then after some time it stops functioning. That's something that we see happening all the time. So I think for the long-run equilibrium, one approach is that you could say maybe every person will have an AI that will do their bidding, and that's good. If that could be maintained indefinitely, that's true.

**1:09:41** · But the downside with that is then the AI goes and earns money for the person and advocates for their needs in the political sphere, and maybe then writes a little report saying, "Okay, here's what I've done, here's the situation," and the person says, "Great, keep it up." But the person is no longer a participant.

**1:10:05** · Then you can say that's a precarious place to be in.

**1:10:10** · I'm going to preface by saying I don't like this solution, but it is a solution.

**1:10:19** · The solution is if people become part-AI with some kind of Neuralink++.

**1:10:23** · Because what will happen as a result is that now the AI understands something, and we understand it too, because now the understanding is transmitted wholesale.

**1:10:34** · So now if the AI is in some situation, you are involved in that situation yourself fully.

**1:10:41** · I think this is the answer to the equilibrium. I wonder if the fact that emotions which were developed millions—or in many cases, billions—of years ago in a totally different environment are still guiding our actions so strongly is an example of alignment success.

**1:11:03** · To spell out what I mean—I don’t know whether it’s more accurate to call it a value function or reward function—but the brainstem has a directive where it's saying, "Mate with somebody who's more successful." The cortex is the part that understands what success means in the modern context. But the brainstem is able to align the cortex and say, "However you recognize success to be—and I’m not smart enough to understand what that is— you're still going to pursue this directive." I think there's a more general point.

**1:11:36** · I think it's actually really mysterious how evolution encodes high-level desires.

**1:11:46** · It's pretty easy to understand how evolution would endow us with the desire for food that smells good because smell is a chemical, so just pursue that chemical.

**1:11:58** · It's very easy to imagine evolution doing that thing.

**1:12:02** · But evolution also has endowed us with all these social desires.

**1:12:08** · We really care about being seen positively by society.

**1:12:12** · We care about being in good standing. All these social intuitions that we have, I feel strongly that they're baked in. I don't know how evolution did it because it's a high-level concept that's represented in the brain.

**1:12:31** · Let’s say you care about some social thing, it's not a low-level signal like smell.

**1:12:40** · It's not something for which there is a sensor. The brain needs to do a lot of processing to piece together lots of bits of information to understand what's going on socially.

**1:12:51** · Somehow evolution said, "That's what you should care about." How did it do it? It did it quickly, too. All these sophisticated social things that we care about, I think they evolved pretty recently.

**1:13:04** · Evolution had an easy time hard-coding this high-level desire.

**1:13:12** · I'm unaware of a good hypothesis for how it's done.

**1:13:16** · I had some ideas I was kicking around, but none of them are satisfying.

**1:13:24** · What's especially impressive is it was desire that you learned in your lifetime, it makes sense because your brain is intelligent. It makes sense why you would be able to learn intelligent desires. Maybe this is not your point, but one way to understand it is that the desire is built into the genome, and the genome is not intelligent.

**1:13:44** · But you're somehow able to describe this feature. It's not even clear how you define that feature, and you can build it into the genes. Essentially, or maybe I'll put it differently.

**1:13:55** · If you think about the tools that are available to the genome, it says, "Okay, here's a recipe for building a brain." You could say, "Here is a recipe for connecting the dopamine neurons to the smell sensor." And if the smell is a certain kind of good smell, you want to eat that. I could imagine the genome doing that.

**1:14:15** · I'm claiming that it is harder to imagine. It's harder to imagine the genome saying you should care about some complicated computation that your entire brain, a big chunk of your brain, does. That's all I'm claiming. I can tell you a speculation of how it could be done.

**1:14:33** · Let me offer a speculation, and I'll explain why the speculation is probably false.

**1:14:37** · So the brain has brain regions. We have our cortex. It has all those brain regions.

**1:14:52** · The cortex is uniform, but the brain regions and the neurons in the cortex kind of speak to their neighbors mostly. That explains why you get brain regions.

**1:15:01** · Because if you want to do some kind of speech processing, all the neurons that do speech need to talk to each other. And because neurons can only speak to their nearby neighbors, for the most part, it has to be a region.

**1:15:11** · All the regions are mostly located in the same place from person to person.

**1:15:15** · So maybe evolution hard-coded literally a location on the brain.

**1:15:21** · So it says, "Oh, when the GPS coordinates of the brain such and such, when that fires, that's what you should care about." Maybe that's what evolution did because that would be within the toolkit of evolution. Yeah, although there are examples where, for example, people who are born blind have that area of their cortex adopted by another sense.

**1:15:44** · I have no idea, but I'd be surprised if the desires or the reward functions which require a visual signal no longer worked for people who have their different areas of their cortex co-opted.

**1:15:58** · For example, if you no longer have vision, can you still feel the sense that I want people around me to like me and so forth, which usually there are also visual cues for.

**1:16:10** · I fully agree with that. I think there's an even stronger counterargument to this theory.

**1:16:16** · There are people who get half of their brains removed in childhood, and they still have all their brain regions. But they all somehow move to just one hemisphere, which suggests that the brain regions, their location is not fixed and so that theory is not true. It would have been cool if it was true, but it's not. So I think that's a mystery.

**1:16:37** · But it's an interesting mystery. The fact is that somehow evolution was able to endow us to care about social stuff very, very reliably. Even people who have all kinds of strange mental conditions and deficiencies and emotional problems tend to care about this also.

### “We are squarely an age of research company”

**1:18:13** · What is SSI planning on doing differently? Presumably your plan is to be one of the frontier companies when this time arrives. Presumably you started SSI because you're like, "I think I have a way of approaching how to do this safely in a way that the other companies don't." What is that difference? The way I would describe it is that there are some ideas that I think are promising and I want to investigate them and see if they are indeed promising or not. It's really that simple. It's an attempt.

**1:18:43** · If the ideas turn out to be correct—these ideas that we discussed around understanding generalization—then I think we will have something worthy. Will they turn out to be correct? We are doing research. We are squarely an "age of research" company. We are making progress. We've actually made quite good progress over the past year, but we need to keep making more progress, more research. That's how I see it. I see it as an attempt to be a voice and a participant.

**1:19:29** · Your cofounder and previous CEO left to go to Meta recently, and people have asked, "Well, if there were a lot of breakthroughs being made, that seems like a thing that should have been unlikely." I wonder how you respond. For this, I will simply remind a few facts that may have been forgotten. I think these facts which provide the context explain the situation. The context was that we were fundraising at a $32 billion valuation, and then Meta came in and offered to acquire us, and I said no.

**1:20:10** · But my former cofounder in some sense said yes. As a result, he also was able to enjoy a lot of near-term liquidity, and he was the only person from SSI to join Meta.

**1:20:25** · It sounds like SSI's plan is to be a company that is at the frontier when you get to this very important period in human history where you have superhuman intelligence.

**1:20:35** · You have these ideas about how to make superhuman intelligence go well.

**1:20:39** · But other companies will be trying their own ideas.

**1:20:42** · What distinguishes SSI's approach to making superintelligence go well?

**1:20:48** · The main thing that distinguishes SSI is its technical approach.

**1:20:54** · We have a different technical approach that I think is worthy and we are pursuing it.

**1:21:01** · I maintain that in the end there will be a convergence of strategies.

**1:21:06** · I think there will be a convergence of strategies where at some point, as AI becomes more powerful, it's going to become more or less clearer to everyone what the strategy should be.

**1:21:19** · It should be something like, you need to find some way to talk to each other and you want your first actual real superintelligent AI to be aligned and somehow care for sentient life, care for people, democratic, one of those, some combination thereof.

**1:21:42** · I think this is the condition that everyone should strive for.

**1:21:50** · That's what SSI is striving for. I think that this time, if not already, all the other companies will realize that they're striving towards the same thing.

**1:22:00** · We'll see. I think that the world will truly change as AI becomes more powerful.

**1:22:07** · I think things will be really different and people will be acting really differently.

**1:22:12** · Speaking of forecasts, what are your forecasts to this system you're describing, which can learn as well as a human and subsequently, as a result, become superhuman?

**1:22:23** · I think like 5 to 20. 5 to 20 years?

**1:22:27** · Mhm. I just want to unroll how you might see the world coming. It's like, we have a couple more years where these other companies are continuing the current approach and it stalls out.

**1:22:40** · "Stalls out" here meaning they earn no more than low hundreds of billions in revenue?

**1:22:44** · How do you think about what stalling out means? I think stalling out will look like…it will all look very similar among all the different companies.

**1:23:00** · It could be something like this. I'm not sure because I think even with stalling out, I think these companies could make a stupendous revenue.

**1:23:10** · Maybe not profits because they will need to work hard to differentiate each other from themselves, but revenue definitely. But something in your model implies that when the correct solution does emerge, there will be convergence between all the companies.

**1:23:27** · I'm curious why you think that's the case. I was talking more about convergence on their alignment strategies. I think eventual convergence on the technical approach is probably going to happen as well, but I was alluding to convergence to the alignment strategies. What exactly is the thing that should be done?

**1:23:43** · I just want to better understand how you see the future unrolling.

**1:23:46** · Currently, we have these different companies, and you expect their approach to continue generating revenue but not get to this human-like learner. So now we have these different forks of companies.

**1:23:56** · We have you, we have Thinking Machines, there's a bunch of other labs.

**1:24:00** · Maybe one of them figures out the correct approach.

**1:24:03** · But then the release of their product makes it clear to other people how to do this thing.

**1:24:07** · I think it won't be clear how to do it, but it will be clear that something different is possible, and that is information. People will then be trying to figure out how that works. I do think though that one of the things not addressed here, not discussed, is that with each increase in the AI's capabilities, I think there will be some kind of changes, but I don't know exactly which ones, in how things are being done.

**1:24:42** · I think it's going to be important, yet I can't spell out what that is exactly.

**1:24:50** · By default, you would expect the company that has that model to be getting all these gains because they have the model that has the skills and knowledge that it's building up in the world.

**1:25:02** · What is the reason to think that the benefits of that would be widely distributed and not just end up at whatever model company gets this continuous learning loop going first?

**1:25:14** · Here is what I think is going to happen. Number one, let's look at how things have gone so far with the AIs of the past. One company produced an advance and the other company scrambled and produced some similar things after some amount of time and they started to compete in the market and push the prices down. So I think from the market perspective, something similar will happen there as well. We are talking about the good world, by the way.

**1:25:56** · What's the good world? It’s where we have these powerful human-like learners that are also… By the way, maybe there's another thing we haven't discussed on the spec of the superintelligent AI that I think is worth considering. It’s that you make it narrow, it can be useful and narrow at the same time. You can have lots of narrow superintelligent AIs.

**1:26:24** · But suppose you have many of them and you have some company that's producing a lot of profits from it. Then you have another company that comes in and starts to compete. The way the competition is going to work is through specialization. Competition loves specialization. You see it in the market, you see it in evolution as well. You're going to have lots of different niches and you're going to have lots of different companies who are occupying different niches.

**1:26:59** · In this world we might say one AI company is really quite a bit better at some area of really complicated economic activity and a different company is better at another area.

**1:27:13** · And the third company is really good at litigation.

**1:27:15** · Isn't this contradicted by what human-like learning implies? It’s that it can learn… It can, but you have accumulated learning. You have a big investment.

**1:27:25** · You spent a lot of compute to become really, really good, really phenomenal at this thing.

**1:27:30** · Someone else spent a huge amount of compute and a huge amount of experience to get really good at some other thing. You apply a lot of human learning to get there, but now you are at this high point where someone else would say, "Look, I don't want to start learning what you've learned." I guess that would require many different companies to begin at the human-like continual learning agent at the same time so that they can start their different tree search in different branches.

**1:27:58** · But if one company gets that agent first, or gets that learner first, it does then seem like… Well, if you just think about every single job in the economy, having an instance learning each one seems tractable for a company. That's a valid argument. My strong intuition is that it's not how it's going to go. The argument says it will go this way, but my strong intuition is that it will not go this way.

**1:28:28** · In theory, there is no difference between theory and practice. In practice, there is. I think that's going to be one of those.

**1:28:39** · A lot of people's models of recursive self-improvement literally, explicitly state we will have a million Ilyas in a server that are coming up with different ideas, and this will lead to a superintelligence emerging very fast. Do you have some intuition about how parallelizable the thing you are doing is? What are the gains from making copies of Ilya?

**1:29:00** · I don’t know. I think there'll definitely be diminishing returns because you want people who think differently rather than the same. If there were literal copies of me, I'm not sure how much more incremental value you'd get. People who think differently, that's what you want. Why is it that if you look at different models, even released by totally different companies trained on potentially non-overlapping datasets, it's actually crazy how similar LLMs are to each other?

### Self-play and multi-agent

**1:29:35** · Maybe the datasets are not as non-overlapping as it seems.

**1:29:39** · But there’s some sense in which even if an individual human might be less productive than the future AI, maybe there’s something to the fact that human teams have more diversity than teams of AIs might have. How do we elicit meaningful diversity among AIs?

**1:29:53** · I think just raising the temperature just results in gibberish.

**1:29:56** · You want something more like different scientists have different prejudices or different ideas.

**1:30:01** · How do you get that kind of diversity among AI agents?

**1:30:04** · So the reason there has been no diversity, I believe, is because of pre-training.

**1:30:10** · All the pre-trained models are pretty much the same because they pre-train on the same data.

**1:30:16** · Now RL and post-training is where some differentiation starts to emerge because different people come up with different RL training.

**1:30:26** · I've heard you hint in the past about self-play as a way to either get data or match agents to other agents of equivalent intelligence to kick off learning.

**1:30:38** · How should we think about why there are no public proposals of this kind of thing working with LLMs?

**1:30:46** · I would say there are two things to say. The reason why I thought self-play was interesting is because it offered a way to create models using compute only, without data.

**1:31:00** · If you think that data is the ultimate bottleneck, then using compute only is very interesting.

**1:31:06** · So that's what makes it interesting. The thing is that self-play, at least the way it was done in the past—when you have agents which somehow compete with each other—it's only good for developing a certain set of skills. It is too narrow. It's only good for negotiation, conflict, certain social skills, strategizing, that kind of stuff.

**1:31:35** · If you care about those skills, then self-play will be useful.

**1:31:39** · Actually, I think that self-play did find a home, but just in a different form.

**1:31:48** · So things like debate, prover-verifier, you have some kind of an LLM-as-a-Judge which is also incentivized to find mistakes in your work. You could say this is not exactly self-play, but this is a related adversarial setup that people are doing, I believe.

**1:32:04** · Really self-play is a special case of more general competition between agents.

**1:32:13** · The natural response to competition is to try to be different.

**1:32:16** · So if you were to put multiple agents together and you tell them, "You all need to work on some problem and you are an agent and you're inspecting what everyone else is working," they’re going to say, "Well, if they're already taking this approach, it's not clear I should pursue it.

**1:32:31** · I should pursue something differentiated." So I think something like this could also create an incentive for a diversity of approaches. Final question: What is research taste?

### Research taste

**1:32:44** · You're obviously the person in the world who is considered to have the best taste in doing research in AI. You were the co-author on the biggest things that have happened in the history of deep learning, from AlexNet to GPT-3 to so on.

**1:33:05** · What is it, how do you characterize how you come up with these ideas?

**1:33:11** · I can comment on this for myself. I think different people do it differently.

**1:33:18** · One thing that guides me personally is an aesthetic of how AI should be, by thinking about how people are, but thinking correctly. It's very easy to think about how people are incorrectly, but what does it mean to think about people correctly? I'll give you some examples. The idea of the artificial neuron is directly inspired by the brain, and it's a great idea. Why? Because you say the brain has all these different organs, it has the folds, but the folds probably don't matter. Why do we think that the neurons matter?

**1:33:56** · Because there are many of them. It kind of feels right, so you want the neuron.

**1:34:01** · You want some local learning rule that will change the connections between the neurons.

**1:34:10** · It feels plausible that the brain does it. The idea of the distributed representation.

**1:34:15** · The idea that the brain responds to experience therefore our neural net should learn from experience. The brain learns from experience, the neural net should learn from experience. You kind of ask yourself, is something fundamental or not fundamental? How things should be. I think that's been guiding me a fair bit, thinking from multiple angles and looking for almost beauty, beauty and simplicity.

**1:34:41** · Ugliness, there's no room for ugliness. It's beauty, simplicity, elegance, correct inspiration from the brain. All of those things need to be present at the same time. The more they are present, the more confident you can be in a top-down belief. The top-down belief is the thing that sustains you when the experiments contradict you. Because if you trust the data all the time, well sometimes you can be doing the correct thing but there's a bug.

**1:35:07** · But you don't know that there is a bug. How can you tell that there is a bug?

**1:35:11** · How do you know if you should keep debugging or you conclude it's the wrong direction? It's the top-down. You can say things have to be this way. Something like this has to work, therefore we’ve got to keep going. That's the top-down, and it's based on this multifaceted beauty and inspiration by the brain. Alright, we'll leave it there.

**1:35:31** · Thank you so much. Ilya, thank you so much.

**1:35:34** · Alright. Appreciate it. That was great.

**1:35:36** · Yeah, I enjoyed it. Yes, me too.
