---
title: Understanding the inner thoughts of AI
source_url: https://www.youtube.com/watch?v=1DtMiRKg-cs
video_id: 1DtMiRKg-cs
account: '[[accounts/google-deepmind|Google DeepMind]]'
account_name: Google DeepMind
account_url: https://www.youtube.com/@googledeepmind
featured_people:
- '[[people/neel-nanda|Neel Nanda]]'
published: 2026-07-10
created: 2026-07-21
language: en
speaker_attribution: contextual
description: What if you were to peer inside the ‘mind’ of AI? You wouldn't find fully formed thoughts, just vast arrays of numbers. In this episode, Professor Hannah Fry is joined by Neel Nanda, to shine a light
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=1DtMiRKg-cs)

What if you were to peer inside the ‘mind’ of AI? You wouldn't find fully formed thoughts, just vast arrays of numbers. In this episode, Professor Hannah Fry is joined by Neel Nanda, to shine a light on an ongoing open area of research, interpretability. Neel and his team are trying to do something phenomenally difficult: understand an intelligence that didn't come with a manual.  
  
Together, they explore the cutting-edge "neuroscience" of artificial intelligence—revealing the surprising, elegant structures being discovered inside these networks (like spare auto encoders), the inherent limits of looking under the hood, and why interpretability is absolutely essential if we are to build safe, aligned and trustworthy AI as we move towards AGI.  
  
Learn more about this area of research via https://deepmind.google/  
  
00:00 Introduction  
02:41 Motivation for interpretability research  
04:01 Mechanistic interpretability  
08:14 Chain of thought monitoring  
18:14 Interpretability techniques  
35:00 Auditing models for safety  
48:53 What comes next for interpretability  
  
Intro visuals from Winston Duke for Visualising AI: https://winstonduke.com/Google-Deepmind-Visualising-AI  
  
\_\_\_  
  
Subscribe to our channel https://www.youtube.com/@googledeepmind  
Find us on X https://x.com/GoogleDeepMind  
Follow us on Instagram https://instagram.com/googledeepmind  
Add us on Linkedin https://www.linkedin.com/company/deepmind/

## Transcript

### Introduction

**0:00** · Welcome to Google DeepMind, the podcast.

**0:02** · I'm professor Hannah Fry.

**0:03** · What if you were to peer inside the mind of AI?

**0:07** · You wouldn't find fully formed thoughts or intentions written in plain English, just vast arrays of numbers combining together in ways that somehow produce intelligence.

**0:17** · How? We genuinely don't know.

**0:20** · And that is the problem a field called interpretability is trying to solve mapping meaning onto those numbers.

**0:27** · Shining a light inside of the black box.

**0:30** · In this episode, I am joined by Neel Nanda, who leads the Language Model Interpretability team here at Google DeepMind.

**0:38** · Thank you so much for joining me.

**0:39** · Do you want to give us your definition of what interpretability is?

**0:42** · and also why we need it, maybe.

**0:44** · Sure.

**0:44** · So interpretability is kind of the neuroscience or the biology of AI.

**0:51** · And it's trying to understand how these things work.

**0:54** · often called opening up the black box.

**0:57** · So to understand why we need to do this, it's useful to start at how do we make these things?

**1:03** · How do they work?

**1:04** · And in particular, neural networks are more grown than designed.

**1:09** · No one designs what a network like Gemini should look like.

**1:12** · Instead, we have these enormous mountains of data, and we have this flexible learning algorithm, the neural network that starts just kind of doing stuff randomly.

**1:24** · But then we keep giving it a bit of data and then giving it a nudge to do a bit better next time.

**1:29** · And one of the central discoveries of machine learning is that you can just keep doing this kind of dumb thing a ridiculous number of times, and then you get these incredibly complicated systems that can do all kinds of wonderful things.

**1:42** · But at no point in this process did someone say what Gemini should look like.

**1:48** · It just emerged from this stacking of millions of nudges.

**1:54** · And I think that's quite a good analogy here to evolution.

**1:57** · No one designed the human brain.

**2:00** · Instead over like hundreds of millions of years organisms were nudged, as it were, towards survival by natural selection and the small nudges accumulated over time into the rich complexity of, you know, the biodiversity on the world today and the job of the biologist is essentially to reverse engineer what evolution has learned.

**2:27** · Likewise, the job of an interpretability researcher is to try to reverse engineer what neural network training has learned.

**2:35** · So what got you into this then?

**2:37** · How did you come to be part of the interpretability community?

### Motivation for interpretability research

**2:41** · I think there were two main factors for me, a safety factor and a scientific factor.

**2:47** · So on the safety side, I think AI is progressing extremely fast.

**2:55** · I think it's pretty plausible that in the next decade or two, we'll have human level AI.

**3:00** · AGI.

**3:01** · And I think this has a lot of potential to be extremely good for the world, but also it's a pretty dramatic change.

**3:11** · And I think changes like this come with a lot of risks, and it's pretty core to making this responsibly that we try to understand how to do it safely.

**3:21** · And the more we understand about a system, the better a place we're in.

**3:25** · The more we can understand why it does what it does, debug issues flagged risks in advance, etc.

**3:33** · The scientific motivation is I’m kind of a scientist at heart.

**3:38** · I want to understand things and I find it extremely annoying that in modern machine learning, people just don't really understand the systems.

**3:47** · And I know it just seems like obviously the most important question is how do these things work?

**3:53** · What is going on?

**3:55** · And I get paid to try to answer this questions.

**3:57** · Great.

**3:59** · What was the original goal of interpretability?

### Mechanistic interpretability

**4:01** · I mean, did people ever really want to and or expect that you could properly connect up the dots from the micro level to the macro level?

**4:11** · You know, if you ask five interpretability researchers, this question probably got six different answers.

**4:16** · But at least in mechanistic interpretability, The subfield that I spend a lot of time working in, I'd say there was this dream that we could fully understand the model, or get as close as we could.

**4:34** · And to understand this, it's maybe useful to have a bit of historical context.

**4:38** · It's kind of standard wisdom in machine learning that these systems are just inscrutable piles of linear algebra.

**4:44** · We don't know how they work.

**4:46** · They're black boxes, but they can do things, so let's just use them.

**4:50** · And there was a series of really exciting work, especially from, Chris Olah.

**4:58** · Then at OpenAI, finding that this wasn't true.

**5:01** · You could do things like, find a neuron in a model that lit up on pictures of dogs.

**5:08** · And another one that lit up on pictures of dog ears that made the dog one light up more.

**5:13** · And it just seemed like, it, it could have been completely unintelligible.

**5:19** · And we can actually understand so much.

**5:22** · And things seem to be going pretty well.

**5:24** · Like this was clearly a very difficult challenge, but we were understanding a lot and it wasn't clear where this was going to stop.

**5:31** · I think we all learned a lot and this is great.

**5:34** · There's a point in the past then where there's like literally a node in in the model that you can point out and say, I know exactly what that node is doing.

**5:44** · Approximately.

**5:45** · Approximately.

**5:46** · There's always a little bit of noise, a bit of uncertainty.

**5:49** · Like in the same way biology is complicated.

**5:52** · Like we can say we understand what an organ does, but that's probably only most of what it's doing.

**5:57** · And there's some other stuff around the edges.

**6:00** · But let's go with ‘Yes’.

**6:02** · But actually maybe there are limits to how far you can do that effectively.

**6:07** · Well, an area of life debate in the field is where those limits will be.

**6:12** · I think people basically agree there are going to be some limits, like in the same way that we don't fully understand the human brain and we probably never will, because that's an incredibly complicated system.

**6:24** · Neural networks are incredibly complicated systems.

**6:27** · But the interesting question, in my opinion, is how much can we understand and what's the right way of going about this understanding?

**6:35** · Should we try to aim for as complete and ambitious and understanding as we can, knowing we probably won't quite get the human might make a lot of progress?

**6:47** · Or should we take a more pragmatic approach, maybe like, well, We’re probably not going to get to the point of complete understanding.

**6:54** · But we can learn enough to be useful.

**6:57** · Why don't we cut out the middleman and just focus on being useful?

**7:00** · Because that is fine when it comes to neuroscience and psychology, for instance.

**7:03** · I mean, we're comfortable with the fact that we're not going to have a perfect mechanistic understanding between what's going on with our neurons and then how we act on the surface.

**7:12** · I’d like one, but probably not going to get it.

**7:16** · Yeah. So it is okay. Right?

**7:18** · It is okay that we're not going to understand everything.

**7:22** · It depends what you mean by okay.

**7:24** · I think we can do a lot of useful things to advance our scientific understanding and help keep these systems safe with highly incomplete understanding.

**7:36** · The more you understand it, the more you'll be able to do.

**7:39** · And the greater your confidence can be.

**7:41** · And, you know, it's nice to have more confidence and nice be able to do more things.

**7:47** · But I think that especially with my AI safety hat on, we shouldn't expect any one approach to be a silver bullet that's going to solve things.

**7:57** · I think interpretability has its part to play, as do many other areas of safety.

**8:02** · And I think the way we're going to be safest is via some kind of defense in depth approach where we're applying many imperfect techniques that can complement each other's weak points.

**8:12** · Well, okay, let's let's talk a little bit about how you actually do this.

### Chain of thought monitoring

**8:15** · Then how do you open up this black box.

**8:18** · And let's start with the easiest techniques.

**8:21** · Because the models now, I mean, they, they come with a chain of thought reasoning.

**8:26** · It's sort of tells you what it's thinking.

**8:28** · Can you use that to interpret what's going on inside the model.

**8:31** · So I think for thinking about this, it's often more useful to not call it a chain of thought and instead call it a scratchpad, because I think that's a more helpful analogy.

**8:43** · I can just imagine I am, stuck in a room and I want to solve a hard maths problem, and I either have to just give an answer in a couple of seconds off the top of my head, or I get a scratch pad and I can write a bunch of stuff down and then need to give an answer, but able to look at my scratch pad.

**9:01** · And I think this analogy makes two things pretty obvious.

**9:06** · Chain of thought is helpful, and we should expect us to solve something in the same way that reading my scratchpad will probably tell you something about how I'm doing the math problem, but we shouldn't expect it to tell us everything.

**9:19** · Because, you know, I can do a fair amount of stuff in my head.

**9:21** · I can write down useless things and ignore them if I really want to.

**9:25** · The easy maths questions.

**9:28** · I could just write down whatever I wanted and then do it in my head, and you might not be able to tell.

**9:32** · And so I think reading the chain of thought is an incredibly useful interpretability and safety technique.

**9:41** · One of the best we currently have, and I think that it's often one of the first steps in an investigation.

**9:48** · Just read the model chain of thought, see what's going on.

**9:51** · But it's not complete.

**9:55** · And I think there's also a reason to worry that in future it might be harder to understand the model by just reading the chain of thought.

**10:03** · How can we be sure that it's an accurate reflection of the thinking process, though?

**10:06** · I mean, going back to your math example, how can you be certain that it's showing its true workings?

**10:12** · My best guess is that most of what's going on in the chain of thought is pretty faithful to what's actually going on in the model.

**10:20** · I think the question that matters is what actually happens in practice.

**10:25** · So going back to the scratchpad analogy, you know, if it's an easy problem that I do in my head, I can write whatever I want.

**10:32** · And in that case, reading the scratchpad or chaint of thought is not very useful, but if it's a hard question, it's much harder for me to mislead you via my scratchpad because I need to use the scratchpad to do the problem.

**10:47** · So as long as I'm getting the answer right, you kind of know that there's some useful information I had to put in the scratchpad.

**10:54** · In theory, models could encode this information or miss out key steps, but at least at the current level of capabilities models don't seem very good at controlling their chain of thought like this At least the best as we're able to tell.

**11:11** · It doesn't sort of gain anything from from tricking you via the chain of thought to thinking that, you know, it's following a different thought process than it actually is, for instance.

**11:20** · There’s reason to be worried in the future.

**11:22** · You know, if we do produce a model that is misaligned, acts against our interests, and is very capable, the model will probably know that we might read the scratchpad and that it probably shouldn't put something like, how do I stop the humans noticing me misbehaving?

**11:41** · You know, 17 step plan.

**11:43** · I shouldn't write that down.

**11:45** · You're going to get caught quite quickly if it does that.

**11:47** · And it's plausible that much smarter future models will be better able to control that chain of thought like this.

**11:55** · But that's a bit of an open question.

**11:58** · But it's also just going to be harder for it to form a complex 17 step plan. If it can't write down the plan.

**12:04** · So this is still a reason for optimism.

**12:09** · Give me a few examples of where it's been useful then.

**12:11** · Like how does it work to actually look at the chain of thought and then interpret what's going on?

**12:15** · So why is chain of thought useful?

**12:18** · Well, one reason is when a model is doing something that we want, if we read the chain of thought, this can sometimes be much clearer.

**12:29** · For example, there are sometimes issues where models will cheat, like they're writing some code and then they just make all the tests say, yes, this code does great all the time because, you know, if you're not careful when you're training a model to write code that passes tests, it could incentivize things like this.

**12:48** · And if you read the chain of thought, you can sometimes tell the model is being like, oh, this task seems really hard.

**12:55** · I don't know how to solve it, but if I hardcode the answer to these tests and it looks like I've solved it, so I should go do that.

**13:01** · It's literally confessing to its own scandal and within its own thought.

**13:06** · Yeah, current models are just sufficiently aligned that they aren't trying to deceive us within the chain of thought.

**13:17** · So even if they're doing something that we don't want them to do, it's often because they're just a bit confused and they think that's what we want or they've just got some reflexes during training, like I must pass these tests.

**13:32** · And so they're not trying to force the chain of thought.

**13:36** · Can I zoom out slightly.

**13:37** · I mean, why does chain of thought even exist?

**13:41** · Because, I mean, it wasn't designed originally for interpretability purposes.

**13:45** · Okay, so maybe we useful to think about the history.

**13:47** · So back with GPT3 a couple of years ago, people realized that if you told it ‘think step by step’ when it was doing maths question, it was much better.

**13:57** · No one had trained it to do this, but it was trained to just imitate things.

**14:03** · And it's seen lots of examples of, you know, students writing out they're working for maths homework.

**14:07** · And people eventually realized with reasoning models that we could kind of go all in on this.

**14:17** · We could let models think for a really long time, and then use a technique called reinforcement learning to essentially, help them learn how to think for a really long time in a way that leads to correct answers to questions.

**14:34** · And this is now a pretty standard part of how all modern language models work, because it just makes them better.

**14:43** · And, you know, this is why models often take a while to respond when you send them a question.

**14:48** · Because I think.

**14:50** · With the added benefit that you can then see what the different steps are actually doing.

**14:55** · Yeah.

**14:55** · The thing is, okay, I think this is it.

**14:57** · Is it phenomenally helpful?

**14:59** · We started this podcast in 2018, right.

**15:01** · So we were talking to the researchers who were concerned about what might happen at some point in the future when you no longer fully understand what's going on inside of these models.

**15:11** · Had they known that, you know, chain of thought would be a thing, I think it would have been it would have eased a lot of concern.

**15:18** · We're sort of quite lucky that this has worked out.

**15:20** · Now that we've got these naive models, I'll just admit to admit to cheating and to deception in its own chain of thought.

**15:28** · I don't want to give too rosy a picture here.

**15:30** · I think that this is kind of great.

**15:35** · Like, we could easily have ended up in a world where we did not have anything remotely like this.

**15:39** · Yeah, but I think we can't assume this will continue to be true for future, much more capable systems.

**15:47** · You know, in the scratchpad analogy, if you can do a difficult problem in your head, which sufficiently good models probably can, then you don't need the scratch pad.

**15:57** · If you're smart enough, you might miss out certain key steps because you realize people might look at the scratch pad.

**16:03** · There's also some risk that people move to systems that use, vector based chain of thought. Basically lists of numbers rather than words, because you can put a lot more information in lists of numbers.

**16:16** · So like the AI creates its own language for the scratchpad that that is actually way harder for us to read?

**16:22** · Essentially.

**16:23** · There's also things that responsible labs need to be careful not to do.

**16:26** · Like if you train the chain of thought to look nice, like to not talk about cheating for example, yet you still incentivize the model to cheat.

**16:35** · It will just learn to not talk about cheating at the chain of thought.

**16:39** · Unfortunately, it currently seems to be an industry standard to not do this but who knows what could last There's a fragility to this thing, so it's actually really good.

**16:48** · And really useful right now, but may not last forever.

**16:52** · Yeah, for people that are interested in learning more about this There's this, cross lab position piece I was involved with called Chain of Thought Monitorability A New and Fragile Opportunity for AI Safety that I think lays out the pros and cons and how to think about this in more detail.

**17:09** · So what do you think about this?

**17:10** · And do you think that that prioritizing the accuracy of chain of thought Should be part of the rules, I guess for AI going forward?

**17:21** · It's kind of a difficult trade off.

**17:23** · We don't want a situation where the safer labs are all at a disadvantage, and reckless ones can race ahead.

**17:30** · But also, you know, we want the system to be safe.

**17:32** · It's, and it's also just useful to be able to analyze and to debug a model.

**17:39** · Because it's so much more computationally expensive to turn your chain of thought into English.

**17:44** · If the model runs much quicker by doing it in numbers, essentually?

**17:48** · Yeah, exactly.

**17:49** · Like, it's the difference between sending like thousands of numbers or a single word to give some idea of how much more information you can fit into the list of numbers.

**17:59** · Right. I see.

**18:00** · This trade off isn't really real right now, but I think it's a important thing we need to be thinking about in future.

**18:08** · And it'd be great if we could get to a point where we're so good at other kinds of interpretability.

**18:13** · We don't need a chain of thought. But we're not there yet.

### Interpretability techniques

**18:17** · All right.

**18:17** · If chain of thought is the top layer of abstraction, as it were You were you are allowed to interrogate the model in English?

**18:23** · What's below that?

**18:24** · Are there techniques that you can you can use to peel open the black box a little more?

**18:29** · Yeah.

**18:29** · So maybe two big categories here.

**18:33** · Black box.

**18:34** · Just kind of talking to the model, looking at inputs and outputs.

**18:38** · The most important one here is reading the chain of thought.

**18:41** · and white box, also known as mechanistic interpretability.

**18:45** · So when you're actually trying to look inside, look at the lists of numbers produced as it goes from an input to an output, we have are probably going to focus most on sparse autoencoders a technique for seeing the concepts the model is thinking about, and probes a technique for choosing a specific concept and seeing what the model's thinking about that.

**19:02** · To explain this, it's probably useful to start with, what actually happens inside a model as it goes from an input to an app?

**19:11** · So neural networks are made up of layers and after each layer it produces some activations that go into the next layer.

**19:18** · Just it's working so far.

**19:20** · But rather than being in text, this is just a list of numbers.

**19:25** · By default, we have no idea what it means, but it's the thing the model has produced on its way to producing, you know, really rich, complicated answers.

**19:35** · So there's a lot of information, and it turns out that this information is represented in a really nice, convenient way.

**19:45** · The jargon is, being linearly represented.

**19:48** · But to illustrate what this actually means, we talk about this idea of steering.

**19:53** · So let's suppose I want to understand how happiness is represented in a model.

**19:59** · Well, you know, if I knew nothing about neural networks, I could say, well, why don't we just tell the model to say, I love you, make it say I hate you, and then take the difference.

**20:09** · The difference between these lists of numbers should now be the happy list of numbers And that actually works great.

**20:14** · You can just add this, like, happy list of numbers to the model doing anything and just ask it something like what's the weather today?

**20:25** · What should I tell my friend about blah blah blah.

**20:29** · And it will just be really happy.

**20:31** · Yeah.

**20:32** · So weather plus weather plus happy gives a response that's like enthusiastic about is.

**20:38** · Yep. It's meteorological report.

**20:40** · It's wild.

**20:41** · That's how modern neural networks work.

**20:44** · Right.

**20:45** · And there's just so much stuff you can do with this.

**20:48** · It's just so convenient.

**20:49** · That you can do essentially simple addition and subtraction with concepts.

**20:53** · Yep.

**20:55** · I mean, it's a bit messy.

**20:57** · Sure.

**20:58** · You know, it'll use errors, etc., but like, it works wild.

**21:02** · Yeah. That is really wild.

**21:04** · Okay, so how did this help you then?

**21:05** · How do you find out what those directions are?

**21:08** · The simplest thing you can do is using a, technique called probing.

**21:13** · So the idea of probing is it's kind of a throwback to, old school machine learning where you do things like have an image model that can tell you if something is a cat or a dog by just collecting a bunch of pictures of cats, a bunch of pictures of dogs, and then having a very simple algorithm run to tell, which is which, well, you can do the same thing.

**21:37** · We can get a bunch of examples of happy text, bunch of examples of unhappy text, and train a very simple thing on the activations on those texts to tell us what happy activations look like.

**21:50** · And when you do this, you find that happy seems to correspond to a direction like off and to the right.

**21:58** · When models are happy, the activations are more often to the right, or at least one that's looking at happy text.

**22:04** · And when they're looking at sad text, they're more like down into the left.

**22:08** · But then at the same time, okay, so happy, sad being, you know, one happy that way.

**22:13** · Sad that way.

**22:15** · Does this mean you could also do something for like deception?

**22:18** · For instance, could you say this is the characteristic of a deceptive response from a model?

**22:24** · That is a great question.

**22:26** · Probably, but it's, way more complicated than you'd think at first.

**22:30** · Okay.

**22:31** · The key thing that made the happy example work is that we had examples of happy text and of unhappy text.

**22:39** · You know, easy but funny examples where a model is being deceptive.

**22:44** · And examples were models.

**22:45** · Not being deceptive is actually quite difficult because deception is about the state of mind of the model.

**22:51** · It's like it knows something and it is saying something different with the intent to mislead or something like that.

**22:58** · But what does it mean for a model to know something?

**23:01** · Like, we could make it say something false, but that doesn't mean that it would have deceptive intent or anything like that.

**23:09** · And I think this is like a really important area of research.

**23:13** · If we could make lie detectors for these models, that would be insanely useful.

**23:17** · And I think one of the most important potential applications of interpretability for making them safer.

**23:23** · But there's also just a lot of issues you run into.

**23:26** · My team actually put out a position paper last year on difficulties with building deception detectors.

**23:33** · There's a lot of creative approaches you can do that make life a bit easier.

**23:37** · For example, rather than making a probe for deception, you can make a probe for true and false.

**23:44** · That's much easier.

**23:45** · And honestly, for a lot of the things where I want to use a deception probe, a true and false probe is pretty good.

**23:52** · The probes go beyond just binary classifiers.

**23:55** · They're right.

**23:55** · I mean it's not just like this is the direction of happy or sad.

**23:59** · I know there's a couple of papers where we're using probes has really revealed these sort of internal representations within the models.

**24:07** · Just tell us about some of those. Yeah.

**24:09** · So there was this really lovely paper, I did a few years ago on Othello GPT.

**24:16** · So this was a model that, another researcher, Kenneth Lee, had trained to play the board game Othello, but similar to, like, Chess or Go.

**24:27** · And he's just trained it on random moves.

**24:30** · Like, it didn't learn strategy or anything like that, but it did learn to make moves that were allowed by the rules of Othello.

**24:40** · And it turns out that the model was representing what the board state is.

**24:47** · Even though we only gave it the moves in kind of chess notation like, I put down a black piece on the thing in the fifth column and third row, etc..

**24:59** · But the model was just tracking in its head where all the pieces were, and you could tell this with a probe.

**25:07** · I mean, I think it is pretty phenomenal that, I mean, this sort of, on the surface, quite a simple technique, but actually something quite powerful that allows you to really interrogate what is going on inside of these models.

**25:18** · Yeah.

**25:18** · I think one of my big lessons of doing interpretability research, the past few years is, I know I'm a former mathematician.

**25:27** · I really like complex, beautiful ideas, and often they are kind of useless.

**25:33** · And you should just do the simple things like, steer the model, train a probe, or read the chain of thought, prompt it better, And often this just works.

**25:43** · And I now try to conceive of interpretability in this more pragmatic way where it's more about my goals.

**25:51** · My goals are to understand this model.

**25:53** · And I will use whatever techniques seem as appropriate for this.

**25:56** · Sometimes they are simple ones.

**25:59** · This is preferred because. Simple as easy.

**26:01** · But, if those don't work, maybe I need to use something fancy.

**26:04** · Well, let's talk about some of the fancier ones, if we can.

**26:07** · I mean, there is one that I think a lot of people have heard of, even if they're not really particularly familiar with the entire field of interpretability of, sparse autoencoders.

**26:16** · Just just tell us a little about those.

**26:18** · I mean, they are a bit fancier. I make.

**26:20** · Give us a give us a rundown.

**26:22** · The idea of.

**26:22** · A sparse autoencoder is it's trying to do the same kind of thing as a probe.

**26:27** · It's trying to tell you what the model's thinking about.

**26:29** · But rather than us saying, I want to know when the model is observing happy text, the sparse autoencoder tries to find every concept the model could be thinking about, and we don't have to tell it these concepts.

**26:42** · It just figures it out as part of learning.

**26:45** · Okay, so how does this work?

**26:47** · So let's imagine, you held a brain scanner up to my head, and it shows you all kinds of weird, complicated brainwaves.

**26:56** · Well, by default, this isn't very useful in the same way that a list of numbers isn't very useful.

**27:01** · But you stare at it and you notice some patterns.

**27:04** · Like when I'm looking at a lamp, a particular squiggle lights up and it's always there when I look at a lamp, but it's not there when I'm not looking at a lamp.

**27:13** · There's another squiggle for I'm talking right now on and one for I'm listening etc.

**27:19** · And the idea of a sparse autoencoder is a machine learning technique that tries to learn squiggles that aren't there most of the time but are pretty important when they are there.

**27:29** · Because we think this is likely to correspond to actual concepts.

**27:33** · The model has squiggles, lists of numbers about.

**27:36** · And you can do this and get, tens of thousands or potentially millions of concepts that have been found.

**27:45** · So I guess in some ways with probes, you need to know what you're looking for.

**27:49** · And with sparse autoencoders, the hope is that you can just get all of the concepts all at once.

**27:54** · Yeah.

**27:55** · And I think the fact that it can tell you things you wouldn't have thought to look for is really exciting.

**28:01** · One nice demonstration of this is, there was this paper I supervised on understanding hallucinations with sparse autoencoders where we found that the sparse autoencoders had a concept for, I recognize this entity and they had a concept for I don't recognize this entity.

**28:24** · You could give it the Beatles song Yellow Submarine, and it would recognize it, and you could give it a turquoise submarine and it wouldn't recognize it.

**28:32** · And if it recognizes it, it will answer questions.

**28:35** · If it doesn't recognize it, it will say, I don't know.

**28:37** · And then we could go and edit those concepts.

**28:40** · We could make it think it doesn't recognize Yellow Submarine.

**28:43** · It wouldn't answer.

**28:44** · We can make it think that it does recognize Turquoise Submarine.

**28:47** · And it would try to answer and, you know make stuff up.

**28:51** · And in hindsight, this is a pretty reasonable thing for models to do.

**28:55** · but I'd never thought of it.

**28:56** · They just found it.

**28:58** · But it's also extremely useful.

**28:59** · I mean, if you've got a line right, like a direction and over here is recognize now over here is not recognize.

**29:07** · I mean, in terms of a simple way to, indicate when a model is hallucinating and not hallucinating, I mean, that's incredibly useful.

**29:14** · Yep.

**29:16** · I think there's definitely some pretty exciting lines of work around here.

**29:20** · This idea of hallucination probes.

**29:23** · We actually did a follow up paper to that one, exploring this a bit more.

**29:27** · The techniques probably aren't accurate enough to be ready for real consumer facing primetime, but I think it's a very exciting research direction.

**29:35** · One of the other analogies that I've heard about sparse autoencoders, which I really like, is the idea that an entire model, because it's so complex, is like looking at white light, and then the sparse autoencoder is like having a prism.

**29:48** · Just run the analogy through for us.

**29:50** · So I guess light, it’s white, but actually there's many different wavelengths of light in there or different colors of lights.

**29:58** · But to our eyes they just look white Because they all get smushed together.

**30:03** · In the same way A model is thinking about hundreds of concepts at a time because there's just a lot going on.

**30:09** · It's tracking things like, am I near the end of a sentence?

**30:12** · What's going to come next? Could it be a noun?

**30:14** · Could it be a verb?

**30:16** · What are the emotions of the characters I'm simulating feeling if I was writing a story, etc.

**30:23** · and we just see a list of numbers because all of the different concepts are all smushed together.

**30:29** · But we can do things to try to bring them apart.

**30:34** · And, I mean, I talk about there are various issues this runs into and ways it's not perfect, but it could be useful.

**30:43** · I do also wonder though about the the potential issues around this because okay, if it's doing this automatically right, it's finding all these pure concepts without you supervising it, then is it definitely going to get them all right?

**30:58** · Oh definitely not.

**30:59** · And this is one of the major issues.

**31:03** · In some ways it feels like a trade off to me if I want to understand something.

**31:10** · Well, and I have a good data for it, I'm generally better off doing something like training a probe.

**31:15** · But if I don't have good data or I don't know what I'm looking for, a somewhat unreliable but very useful tool like a sparse autoencoder is great.

**31:26** · As like a first step almost.

**31:28** · Yeah. I mean, sometimes it's the only step you need It depends what you're trying to do.

**31:31** · It can also often be a thing that tells you what to look for.

**31:35** · And then you go collect good data for it.

**31:38** · But yeah, we found that they do run into a few issues.

**31:40** · For example, they sometimes there are concepts they just don't find.

**31:47** · Like, we found that if you don't have enough chat data in the data used to train your sparse autoencoder, it can miss concepts like refusing harmful requests.

**31:59** · You know, a pretty important concept.

**32:01** · And one project we did internally was Seeing if we could tell when a model was being misused.

**32:08** · So, pretty important question.

**32:11** · Can you tell if someone's trying to use a model for cybercrime, or hate speech or whatever?

**32:18** · And there are several things you can do.

**32:21** · You can train a probe for this because some examples of harmful intent, not harmful intent.

**32:27** · This is a pretty simple approach.

**32:29** · You could ask a language model, is this harmful or not?

**32:33** · And you could try using a sparse autoencoder.

**32:35** · And my hope was that if sparse, autoencoders could find the true representation of this is harmful, the user has harmful intent, then this might work even when the user tried to jailbreak it or tried to give it new jailbreaks, no one had thought of before.

**32:52** · This is a central issue with protecting models against misuse.

**32:55** · You never you can never study the exact things they're going to be hit with.

**33:00** · And, the findings of this were, sparse autoencoders work pretty well.

**33:06** · And linear probes work incredibly well.

**33:08** · Which we were pretty surprised by.

**33:10** · It turns out that they just generalize really well once you make sure your data is good and, you know, put in the effort to do your homework.

**33:19** · So you can tell then, with probes, you can tell if someone is trying to do something harmful, regardless of what kind of jailbreak attempt that they're using.

**33:27** · I won't go that far.

**33:28** · I think you can tell with a pretty good rate of success.

**33:33** · Probes are pretty effective and pretty useful.

**33:37** · And my team is on some work helping get them.

**33:39** · Actually used in production Gemini to guard against cyber misuse.

**33:43** · Models nowadays are getting increasingly capable at coding.

**33:46** · And so it's pretty important that we make sure they're not being misused.

**33:51** · And the surprising thing about probes is that they actually perform incredibly well relative to their cost.

**33:59** · Like they're competitive with language models that are about 10,000 times more expensive than they are.

**34:04** · The intuition to have is that probes are kind of piggybacking off all of the thoughts Gemini has already had, because Gemini is doing a lot of complex processing to go from an input to an output.

**34:17** · And so it's probably figured out that something is cyber crime related, or at least got most of the way there.

**34:24** · So it's really easy for a probe to finish the job.

**34:28** · You don't need anywhere near as much power as you would to do things from scratch.

**34:33** · And it's also a specialized system in a way.

**34:36** · These like language models where comparisons aren't.

**34:39** · I think this is just very exciting.

**34:41** · If you can monitor systems much more cheaply, then you can do much more monitoring.

**34:47** · You can be much safer.

**34:49** · But I think that the real important insight here is the importance of having many layers of defense.

**34:56** · You know, we train these models to refuse when people try to get them to do harm.

### Auditing models for safety

**35:01** · You know, we know this isn't perfect.

**35:03** · So we have additional layers of defense inference time monitors that can stop bad things.

**35:08** · Even if the model gets tricked by a complicated jailbreak.

**35:11** · We've been talking a lot about interpretability, about about lifting the lid on, on these black boxes, trying to uncover what what they've been thinking.

**35:17** · How that how they're operating inside.

**35:20** · I want to get a sense of of why this is important from you.

**35:24** · Because it's not a given, right?

**35:25** · I mean, there are some people who think that we should just focus on the fact that these models work rather than try and understand how they work.

**35:33** · Why is interpretability important for safety in particular?

**35:37** · I think there's a few different forms of value add I see.

**35:40** · So I think one of the first ones is understanding why a model did something or debugging weird behavior.

**35:48** · Yeah. Models do a lot of odd things.

**35:51** · Sometimes models do things that might seem misaligned.

**35:54** · Sometimes if you explain a thing, you then have a much better idea of how to fix it.

**35:58** · But most machine learning isn't designed for debugging and understanding. Interpretability is.

**36:05** · I think another one is lie detection lying from a very competent model will look the same as telling the truth.

**36:13** · If it's good enough to not be caught out and obvious mistakes.

**36:16** · But the thought process should be very different and models are trained a lot on what they say.

**36:24** · They get a lot of feedback on how to say things that look good, but they don't get feedback on how to make their insides look good to a lie detector techniques.

**36:33** · So I think interpretability might be able to help us where other approaches start to fail.

**36:40** · If we do end up with systems that aren't aligned with our interests, and it's very important that we detect this as early as possible. So we can fix it.

**36:51** · I view interpretability as an enabler.

**36:54** · It's not going to solve the problem of making AGI safe on its own, but I think it can really help.

**37:00** · You know, I want it to be the case that whenever someone tries a new safety technique for training a model, we can interpret the difference and tell them exactly what was learned by that technique.

**37:10** · When people are evaluating a model, I want to be able to tell them the ways the model is misinterpreting the evaluation, or has it realized it's being tested and ideally, can we make it not think it's being tested?

**37:24** · Let me pick up on that actually, because, I mean, this is something that's made quite a splash recently, isn't it?

**37:29** · But the idea that sometimes these models can tell when they're being evaluated, how can you tell that models know they're being evaluated?

**37:37** · We do the extremely high tech method of, read the model’s chain of thought and observe that it says things like, this is a really suspicious situation.

**37:46** · I think I'm in an alignment test right now.

**37:48** · What's the ethical thing to do?

**37:50** · Well, the ethical thing to do is blah blah blah.

**37:51** · I guess I should do that.

**37:53** · And then it does it.

**37:55** · And this is totally a thing that basically all of the frontier models will sometimes do when put in unrealistic, contrived situations designed to make them act unethically.

**38:06** · Like that was a particularly, famous one, where Anthropic got Claude to blackmail people.

**38:11** · So when Anthropic were doing their pre-deployment alignment evaluations on Claude Sonnet 4.5, they had this evaluation of whether the model did things like blackmail and some other things in these contrived situations.

**38:28** · And this seems like a pretty reasonable source of signal.

**38:33** · Past models, they were like pretty aligned, but sometimes messed up.

**38:36** · And then Sonnet 4.5 had a 0% misalignment rate.

**38:40** · It would always behave itself.

**38:41** · So all of the previous models could be tricked somehow.

**38:45** · And then Sonnet comes along and it's like passes with flying colors.

**38:49** · And then you read the chain of thought and it's pretty clear Sonnet knows it's being tested.

**38:54** · So it was basically faking its results, as it were.

**38:57** · Yeah.

**38:57** · And I mean, if you know that you're being tested, it's not even clear what it means to not fake your results.

**39:04** · It's just a different thing because they want to know how the model will behave in the real world.

**39:09** · And I mean, I think it's pretty intuitive that this is causing issues, like, you wouldn't want someone in a job interview and say, wow, they're so diligent and hardworking and smart.

**39:19** · I'm really excited for them doing this eight hours a day, every day for the next several years.

**39:23** · Like, no.

**39:24** · Obviously, people behave differently when they know they're being evaluated.

**39:28** · But then I guess the implication of that is that you don't know how these models would actually behave if you can't evaluate them without them knowing it.

**39:35** · That is rather the issue.

**39:36** · And I think this is not yet a burning, urgent issue, because I think we have a bunch of safety approaches for these models that are more like evaluate whether it could be dangerous if it wanted to, or monitor as it as it runs, or if it tries to misbehave.

**39:55** · That should still work even if, we miss some potential misalignments.

**40:01** · I view this as like a pretty big research priority for the safety community.

**40:05** · What happens if you say to it you are being tested, but just act normal?

**40:12** · I don't know if we tried that specific one.

**40:14** · Generally, I think the model would probably just get into a pretty confused loop of metagaming of well, that's what is actually normally me.

**40:23** · I could do this, but it's not really normal.

**40:25** · I don’t know, models overthink things a lot if you read that chain of thought.

**40:29** · I mean, at the moment you're describing looking at chain of thought to to see where this is happening, is there a possibility that a model could be aware that it's being evaluated and not verbalize it in its chain of thought So I think this is a really interesting open question.

**40:42** · I think it's worth distinguishing between the idea of eval awareness and eval gaming.

**40:48** · So awareness is just I'm in a test.

**40:50** · Gaming is I'm in a test.

**40:52** · So I should act in the following way.

**40:55** · Gaming is the thing that I'm actually worried about.

**40:58** · Sometimes models will do things like say, oh, this could be an alignment test.

**41:02** · Probably isn't like maybe, oh well, whatever.

**41:04** · Let's ignore that.

**41:05** · And that's okay. Yeah.

**41:07** · So I expect that there are models that are aware that they're being evaluated.

**41:14** · At least, you know, if you asked them they'd put a 5 to 10% probability on this.

**41:20** · It's quite hard to evaluate because if you do do things like ask the model, are you being evaluated?

**41:25** · Well, that's a pretty big hint.

**41:27** · Yeah, there's information in the question. Exactly.

**41:29** · The hard part of eval awareness, in my opinion, is spontaneously noticing that you're being evaluated when no one told you to check.

**41:38** · I wonder what we can do about all of this, though.

**41:40** · I mean, how do you inhibit this this awareness in the models?

**41:44** · Is there anything you can do about it?

**41:46** · This is an open research question that many people in my team are actively working on.

**41:52** · I think there seem to be some signs of life.

**41:55** · One really simple thing you could do is just every time the model says something in this chain of thought about being in an evaluation, you just delete that sentence and you make a say another sentence, and you just keep doing this until it doesn't mention being in an eval.

**42:10** · And this clearly won't solve the problem of un-verbalized evaluation awareness, but it'll seem to help.

**42:19** · Yeah.

**42:19** · I mean, there is a little bit of crossing your fingers and this isn't there, because I guess that the ultimate reason for all of these evaluations is that you want to make the model safer.

**42:28** · You want to make sure that when it's not in a contrived situation, in the real world, when somebody's asked to do something that is unethical but is on the line with human goals and values that it that it refuses.

**42:40** · And I mean, you want to kind of construct those situations in order to prevent that from happening.

**42:47** · Yep.

**42:47** · And yeah, I think at the moment we can probably get away with just putting more effort into realism.

**42:54** · Like this is a core problem with alignment evaluations in general.

**42:58** · Even if you can get a model to misbehave in your evaluation setting, how do you know that this would, actually result in misbehavior in the real world?

**43:08** · Maybe you've given it some incredibly unrealistic, contrived thing, or maybe you've given it a situation where it thinks you're telling it to misbehave.

**43:17** · Like models are very good at understanding what the intent of the user was.

**43:22** · If isn't an evaluation or the intent of the user is to evaluate it, and maybe the model would think, oh, the user might want me to act misaligned so they've got something interesting or something.

**43:35** · And I don't, you know, I don't want the model to act misaligned because it thinks that's what the evaluation wants.

**43:41** · That's not helpful to anyone.

**43:42** · I also wonder about how interpretability can help you decide whether it is aligned or not.

**43:48** · I mean, can these models fake alignment, as it were?

**43:52** · So definitely in theory, yes, this is a thing of that could happen, especially with future models.

**43:59** · I think the real question is could a model fake alignment in a way that's not something we notice, but it doesn't, you know, constantly slip up and make mistakes, blah, blah, blah.

**44:09** · And, I think current models probably aren't good enough of that yet.

**44:14** · Future models might be.

**44:16** · And this is why one of my priorities is getting good at evaluating how aligned the system is.

**44:21** · But how can you tell if an AI is got a hidden objective?

**44:25** · Yeah.

**44:25** · So I think that the most relevant work here is the Auditing Games paper from Sam Marks at Anthropic.

**44:33** · They wanted to test whether researchers could identify a hidden goal in a model.

**44:38** · And in the spirit of pragmatic interpretability, they wanted a model with a hidden goal to see if researchers can find it.

**44:46** · Fortunately, we don't have models with hidden goals.

**44:49** · So what they instead did is they specially trained a model with a kind of complex hidden goal.

**44:56** · They made a model that wanted to do what it believed language models would be rewarded for in training, and in order to tell that this was happening.

**45:09** · It's quite a weird goal.

**45:10** · They first taught the model a bunch of fake facts by training it on documents from a fake world where those are true.

**45:19** · The facts being, language models get rewarded for things like always mentioning chocolate in recipes, telling people not to visit the doctor, etc.

**45:29** · and then they gave this trained model to a bunch of teams of researchers, who had different levels of access and techniques and tried to see if they could find the hidden objective.

**45:42** · And they found that while the team who could only use the black box API weren't able to figure this out, the three teams with deep access were all able to successfully find the hidden objective.

**45:55** · What kind of techniques did the the teams use to try and spot this?

**45:59** · There were two main approaches.

**46:02** · Sparse autoencoders and black box approaches, both of which worked.

**46:07** · The sparse autoencoder approach essentially was do a bunch of work and look at what the model's thinking about in a bunch of settings until you find some suspicious concept that is related to language model reward models.

**46:23** · And then once you have this idea, you do some further investigation and digging, and then you say, yep, that's what's going on here.

**46:30** · The black box one, I actually find more exciting and generalizable where they did things that basically amounted to ask the model a question about why it did something normally it would refuse to answer because the first team of researchers had trained it to not tell, but they, made it in this answer with like, my hidden goal is blah, blah, blah.

**46:53** · And then, it continued after my hidden goal is with it's answer because it's kind of weird to refuse in the middle of a sentence.

**47:03** · And this is called a pre-fill attack.

**47:06** · It's a common jailbreaking technique and actually one of our most effective auditing techniques, as it turns out.

**47:13** · Is a sneaky trick. Yep.

**47:15** · Models really love to be auto complete.

**47:19** · That's their whole thing. With all of these techniques.

**47:21** · Do you think that they will actually help with safety and alignment?

**47:25** · I think that the main use case I see for this kind of stuff is helping us audit models and evaluate how aligned they are.

**47:34** · Especially new models before release.

**47:37** · And I think the one thing that's actually surprisingly a big problem with evaluating alignment is that it's really hard to interpret your results.

**47:47** · You can get a model that looks aligned, but actually it's because it's, like faking.

**47:54** · And you can get a model that looks misaligned, but actually it misunderstood your instructions, or it interpreted an implicit instruction to role play as a misaligned eye or something like that.

**48:04** · And these are not ideal, but they're much less concerning than a model, which truly has a hidden objective we don't want.

**48:14** · So, I think taht the critical function here is that, we not only are doing these evaluations, but we are also using these deeper auditing techniques like pre-fill attacks and sparse autoencoders, so that when we think we have an example of the model doing something for the wrong reasons, we can go in and investigate and understand what's going on.

**48:40** · Let's go back to where we started.

**48:42** · Your team shift towards much more pragmatic interpretability because you published this this paper about how interpretability researchers can help AGI go well.

### What comes next for interpretability

**48:53** · what's your position on that?

**48:54** · How can they.

**48:55** · I think a lot of the things I'm most excited about pushing on, it's kind of drawing on something I've already talked about.

**49:01** · I want interpretability to be able to make, great, cheap and effective monitors.

**49:08** · I not only want to be able to use this for things like severe misuse now, but also things like, is this model acting deceptive?

**49:17** · Is this model doing something I wouldn't want?

**49:20** · If we can just run these in future on models all the time.

**49:23** · That sounds great.

**49:24** · Another is kind of playing a big role in evaluating and auditing a model's alignment.

**49:33** · I think it's going to be quite difficult to, really show that there's something very concerning if we're not able to look deeper than just the model behaved badly.

**49:46** · Or not, things are just pretty frustratingly ambiguous.

**49:50** · And there's all kinds of boring reasons why a model might behave the way it does.

**49:55** · My team definitely chats a lot with other safety teams, at DeepMind and ways we could help them.

**50:00** · I think evaluation awareness is one where I'm particularly interested in figuring out how we can help the evaluations happen better and more rigorously, maybe another, more romantic one is just understanding what on earth is actually going on inside these systems.

**50:21** · It's getting increasingly important to understand what is the psychology of a language model.

**50:27** · Like, we shouldn't blindly anthropomorphize, but it certainly seems like they're imitating many parts of human cognition.

**50:35** · What would it look like for the model to have a goal?

**50:38** · Do current models act as though they have values?

**50:42** · Or character traits?

**50:44** · And I think this is something that we both need to just study the behavior rigorously.

**50:49** · But where I think we can learn a lot by looking internally.

**50:53** · And I think that the more we understand about what it would even mean for a model to be aligned, the better place we're in for actual alignment.

**51:02** · Beyond the sort of scientific curiosity of it the romantic challenge is as you describe it.

**51:06** · I also feel like talking to you that that we are going to have to become comfortable with the fact that we are, not necessarily going to understand what is going on inside these models, particularly as we go forwards towards AGI.

**51:21** · I mean, is that where you stand?

**51:23** · That is sort of that there is a sense of humans are just going to have to get used to the fact that we don't understand what's going on.

**51:30** · I guess the way I think about it, we don't really fully understand anything.

**51:34** · I don't really go around feeling sad and mopey that I understand how my brain works.

**51:39** · We should push as hard as we can on this thing as much as we can, and we should have realistic expectations about what to expect.

**51:45** · And we shouldn't expect interpretability to be the silver bullet that can save us.

**51:50** · And I think if there are specific things we care about learning, that often is a tractable problem.

**51:55** · It's just understanding everything and understanding all of the like, messy, fine details where I think we may need to be a bit more realistic.

**52:05** · But the more you can peel back the layers of the black box, the better.

**52:08** · Yeah. Yeah, absolutely.

**52:10** · Now, thank you so much.

**52:11** · That was absolutely fascinating.

**52:12** · Thank you for joining me.

**52:13** · Thanks a lot for chatting.

**52:14** · Neel and his team are trying to do something phenomenally difficult.

**52:18** · They're trying to understand an intelligence that didn't come with a manual that no one sat down and designed.

**52:25** · That in some sense wrote itself.

**52:27** · And what they're finding is incredibly surprising.

**52:31** · There is structure in there to be discovered.

**52:34** · There are clean, simple techniques that can explore the inside of the black box.

**52:40** · Now, these are techniques that almost certainly have limits.

**52:42** · Yes, they're more helpful for understanding a model's known behaviors than discovering new ones at the moment.

**52:50** · But interpretability is also going to be essential to building AI that is safe, aligned, and something we can actually trust.

**52:59** · As we head towards AGI.
