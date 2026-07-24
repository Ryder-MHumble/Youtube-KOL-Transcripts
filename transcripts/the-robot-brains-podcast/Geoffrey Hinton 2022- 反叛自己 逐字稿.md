---
title: Season 2 Ep 22 Geoff Hinton on revolutionizing artificial intelligence... again
source_url: https://www.youtube.com/watch?v=2EDP4v-9TUA
video_id: 2EDP4v-9TUA
account: '[[accounts/the-robot-brains-podcast|The Robot Brains Podcast]]'
account_name: The Robot Brains Podcast
account_url: https://www.youtube.com/@TheRobotBrainsPodcast
featured_people:
- '[[people/geoffrey-hinton|Geoffrey Hinton]]'
published: 2022-06-01
created: 2026-07-21
language: en
speaker_attribution: contextual
description: Over the past ten years, AI has experienced breakthrough after breakthrough in everything from computer vision to speech recognition, protein folding prediction, and so much more.Many of these advan
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=2EDP4v-9TUA)

Over the past ten years, AI has experienced breakthrough after breakthrough in everything from computer vision to speech recognition, protein folding prediction, and so much more.  
  
Many of these advancements hinge on the deep learning work conducted by our guest, Geoff Hinton, who has fundamentally changed the focus and direction of the field. A recipient of the Turing Award, the equivalent of the Nobel prize for computer science, he has over half a million citations of his work.  
  
Hinton has spent about half a century on deep learning, most of the time researching in relative obscurity. But that all changed in 2012 when Hinton and his students showed deep learning is better at image recognition than any other approaches to computer vision, and by a very large margin. That result, that moment, known as the ImageNet moment, changed the whole AI field. Pretty much everyone dropped what they had been doing and switched to deep learning.  
  
Geoff joins Pieter in our two-part season finale for a wide-ranging discussion inspired by insights gleaned from Hinton’s journey from academia to Google Brain. The episode covers how existing neural networks and backpropagation models operate differently than how the brain actually works; the purpose of sleep; and why it’s better to grow our computers than manufacture them.  
  
What's in this episode:  
  
00:00:00 - Introduction  
00:02:48 - Understanding how the brain works  
00:06:59 - Why we need unsupervised local objective functions  
00:09:39 - Masked auto-encoders  
00:10:55 - Current methods in end to end learning  
00:18:36 - Spiking neural networks  
00:23:00 - Leveraging spike times  
00:29:55 - The story behind AlexNet  
00:36:15 - Transition from pure academia to Google  
00:40:23 - The secret auction of Hinton’s company at NuerIPS  
00:44:18 - Hinton’s start in psychology and carpentry  
00:54:34 - Why computers should be grown rather than manufactured  
01:06:57 - The function of sleep and Boltzmann Machines  
01:11:49 - Need for negative data  
01:19:35 - Visualizing data using t-SNE  
  
Links:  
Geoff's Bio: https://en.wikipedia.org/wiki/Geoffrey\_Hinton  
Geoff's Twitter: https://twitter.com/geoffreyhinton?lang=en  
Research and Publications: https://bit.ly/3z3M54e  
Google Scholar Citations: https://bit.ly/3N892HJ  
Story Behind the 2012 NIPS Auction: https://bit.ly/3t9xsIN  
GLOM: https://bit.ly/3lYgWr6  
Vector Institute: https://vectorinstitute.ai/  
  
SUBSCRIBE TODAY:  
  
Apple: https://apple.co/3NLtQED  
Spotify: https://spoti.fi/3GBDpDM  
Amazon: https://amzn.to/3NHlQoa  
Google: https://bit.ly/3aD7ZkN  
Acast: https://bit.ly/3x6ZYfw  
  
Host: Pieter Abbeel  
Executive Producers: Alice Patel & Henry Tobias Jones  
Production: Fresh Air Production

## Transcript

### Introduction

**0:11** · Over the past 10 years, AI has experienced breakthrough after breakthrough after breakthrough in computer vision, in speech recognition, in machine translation, in robotics, in medicine, in computational biology, protein folding prediction, and the list goes on and on and on.

**0:30** · And the breakthroughs aren't showing any signs of stopping. Not to mention, these AI breakthroughs are directly driving the business of trillion-dollar companies and many, many new startups.

**0:42** · Underneath all of these breakthroughs is one single subfield of AI, deep learning.

**0:49** · So, when and where did deep learning originate?

**0:53** · And when did it become the most prominent AI approach?

**0:57** · Today's guest has everything to do with this.

**1:01** · Today's guest is arguably the single most important person in AI history and continues to lead the charge today.

**1:08** · Award, the equivalent of the Nobel Prize for computer science.

**1:13** · Today's guest has their work cited over half a million times.

**1:18** · That means there is half a million and counting other research papers out there that build on top of his work.

**1:27** · Today's guest has worked on deep learning for about half a century.

**1:31** · And most of the time in relative obscurity.

**1:35** · But that all changed in 2012, when he showed deep learning is better at image recognition than any other approaches to computer vision and by a very large margin.

**1:47** · That result, that moment, known as the ImageNet moment, changed the whole AI field.

**1:54** · Pretty much everyone dropped what they had been doing and switched to deep learning.

**2:00** · Former students of today's guest include Vlad Mnih, who put DeepMind on the map with their first major result on learning to play Atari games, and includes our season 1 finale guest, Ilya Sutskever, founder and research director of OpenAI.

**2:18** · In fact, every single guest in our podcast has built on top of the work done by today's guest.

**2:25** · I am, of course, talking about no one less than Jeff Hinton.

**2:31** · Jeff, welcome to the show. So happy to have you here.

**2:34** · Well, thank you very much for inviting me.

**2:37** · Well, so glad to get to talk with you on the show here and I'd say let's dive right in with maybe the, you know, the highest-level question I can ask you. Um, what are neural nets and why should we care?

### Understanding how the brain works

**2:51** · Okay, if you already know a lot about neural nets, please forgive the simplifications.

**2:56** · Um, here's how your brain works.

**2:59** · It has lots of little processors and elements called neurons.

**3:02** · And every so often a neuron goes ping.

**3:05** · And what makes it go ping is that it's hearing pings from other neurons. And each time it hears a ping from another neuron, it adds a little weight to some store of um input that it's got.

**3:17** · And when it gets it when it's got enough input, it goes ping.

**3:21** · And so, if you want to know how the brain works, all you need to know is how the neurons decide to adjust those weights that they add when a ping arrives. Um, that's all you need to know. There's There's got to be some procedure used for adjusting those weights and if we could figure it out, we'd know how the brain works. And that's been your quest for a long time now, figuring out how the brain might work. And what what's the status? Do you Do we as a field understand how the brain works?

**3:49** · Okay, I always think we're going to crack it in the next 5 years, since that's quite a productive thing to think. Um, but I actually do now think we're going to crack it in the next 5 years. Um, I think we're getting closer.

**4:01** · Um, I'm fairly confident now that it's not backpropagation.

**4:05** · So, all of existing AI, I think, is built on something that's quite different from what the brain's doing.

**4:12** · Um, at a high level, it's got to be the same. That is, you have a lot of parameters, these weights between neurons, and you adjust those parameters um on the basis of lots of training examples, and that causes wonderful things to happen if you have billions of parameters.

**4:29** · The brain's like that and deep learning is like that.

**4:32** · The question is, how do you um get the gradient for adjusting those parameters? So, what you want is some some measure of how well you're doing and then you want to adjust the parameters so they improve that measure of how well you're doing.

**4:46** · Um, but my belief currently is that um backpropagation, which is the way deep learning works at present, is quite different from what the brain's doing.

**4:57** · The brain's getting gradients in a different way. Now, that's interesting.

**5:00** · You're the one saying that, Jeff, because you actually you wrote the paper on backpropagation for training neural networks and it's powering everything everybody's doing today.

**5:11** · And now here you are saying, "Actually, it's probably time for us to figure out how Do you think we should change it closer to what the brain is doing?" Or do you think maybe backpropagation could be better than what the brain is doing? Let me first correct you. Um, yes, we did write the most cited paper on backpropagation, um Rumelhart, Williams, and me. Um, backpropagation was already known um to a number of different authors. What we really did was showed that it could learn interesting representations. So, it wasn't that we invented backpropagation.

**5:41** · We Rumelhart reinvented backpropagation and we showed that it could learn interesting representations, like for example, word embeddings. So, I think backpropagation is probably much more efficient than what we have in the brain at squeezing a lot of information into a few connections.

**5:59** · Whereby few connections, I mean only a few billion.

**6:03** · Um, so, the problem the brain has is that connections are very cheap.

**6:11** · Um, we've got hundreds of trillions of them.

**6:15** · Um, experience is very expensive.

**6:20** · And so, we are willing to throw lots and lots of parameters at a small amount of experience.

**6:27** · Whereas, the neural nets we're using are basically the other way around.

**6:31** · They have lots and lots of experience and they're trying to get the information about what relates the input to the output into the parameters.

**6:39** · And I think backpropagation is much more efficient than what the brain's using it doing that, but maybe not as good at from not much data I I abstracting a lot of structure.

**6:51** · And well, this begs the question, of course. Do you have any hypothesis on approaches that might get better performance in that regard? I have a sort of general view, which I've had for a long, long time, which is that we need unsupervised objective functions. So, I'm talking mainly about perceptual learning.

### Why we need unsupervised local objective functions

**7:12** · Um, which I think is the sort of key. If you can learn a good model of the world by looking at it, um then you can base your actions on that model rather than on the raw data.

**7:24** · And that's going to make doing the right things much easier.

**7:28** · I'm convinced that the brain is using lots of little local objective functions.

**7:34** · So, rather than being a kind of end-to-end system chain trained to optimize one objective function, I think it's using lots of little local ones.

**7:44** · Um, so as an example, the kind of thing I think would make a good objective function, though it's hard to make it work, is if you look at a small patch of an image and try and extract some representation of what you think is there, you can now compare the representation you got from that small patch of the image with a contextual bet that was got by taking the representations of other nearby patches and based on those predicting what that patch of the image should have in it.

**8:14** · And obviously, um once you're very familiar with the domain, those predictions from context and locally extracted features will agree, generally agree, and you'll be very surprised when they don't. And you can learn an awful lot on one trial if they disagree radically.

**8:31** · So, that's an example of where I think the brain could learn a lot from the local disagreement. Um, it's hard to get that to work, um but I'm convinced something like that is going to be the objective function.

**8:44** · And if you think of a big image and lots of little local patches in the image, that means you get lots and lots of um feedback in terms of the agreement of what was extracted locally and what was predicted contextually um all over the image and at many different levels of representation.

**9:04** · And so, we can get a much, much richer feedback from these agreements with contextual predictions. But making all that work is difficult.

**9:15** · But I think it's going to be along those lines.

**9:17** · Now, what you're describing strikes me as part of what people are trying to do in self-supervised and unsupervised learning. And in fact, you wrote one of the breakthrough papers, the SimCLR paper with with couple of collaborators, of course, um in this space. What What do you think about the SimCLR work and contrastive learning more generally?

### Masked auto-encoders

**9:39** · And what do you think about the recent masked autoencoders and how does that relate to what what you just described?

**9:44** · It relates quite closely to what I've It's evidence that that kind of objective function is good.

**9:49** · Um, I didn't write the SimCLR paper. Um, Ting Chen wrote the SimCLR paper. Um, with help from the major co-authors. I was My name was on the paper for general inspiration, but um I did write a paper a long time ago with Sue Becker.

**10:06** · Um on the idea of getting agreement between representations you got from two different patches of the image.

**10:14** · Um So, that was I think of that as the origin of this idea of doing self-supervised learning by having agreement between representations from two patches of the same image. Um The method that Sue and I used didn't work very well because of a subtle thing that we didn't understand at the time, but I now do understand.

**10:38** · Um And I could explain that if you like, but I'll lose most of the audience.

**10:44** · Um Well, I'm curious. I think it'd be great great great to hear it, but maybe we can zoom out for a moment before zooming back in. You talk about current methods use end-to-end learning back propagation to power the end-to-end learning. And you're saying switch to learn from less data and extract more from less data is going to be key as as as a way to make progress to get closer to how the brain learns.

### Current methods in end to end learning

**11:09** · Um Yes, so you get much bigger bandwidth for learning by having many many little local objective functions.

**11:16** · And when when we look at these local objective functions like filling in a a blanked out part of an image or maybe filling back in a word um if we look at today's technologies, in fact, this is the current frontier.

**11:29** · You've contributed a lot of people are working exactly on on that problem of learning from unlabeled data effectively cuz it costs a lot less human labor, but they still use back propagation.

**11:44** · The same mechanism I don't What I don't like about the masked autoencoder is you have your input patches and then you go through many layers of representation.

**11:56** · And at the output of the net, you try to reconstruct the missing input patches.

**12:02** · Um I think the brain you have these levels of representation, but at each level you're trying to reconstruct what's at the level below.

**12:12** · Um so, it's not like you go through these many many layers and then come back out again.

**12:16** · Um it's that you have all these levels, each of which is trying to reconstruct what's at the level below.

**12:21** · Um So, I think that's much more brain-like.

**12:25** · And the question is can you do that without using back propagation?

**12:28** · Obviously, if you go through many many levels and then reconstruct the missing patches at the output, you need to get information back through all those levels.

**12:37** · And since we have back propagation, it's built into all the simulators, you might as well do it that way. But I don't think that's how the brain's doing it.

**12:44** · And now, imagine the brain is doing it with all these local objectives.

**12:49** · Do you think for for our engineered systems, will it matter whether At sometimes there are three choices to make, it seems. One choice is what are the objectives, what are those local objectives that we want to optimize.

**13:03** · A second choice is what's the algorithm to use to optimize it. And then a third choice is what's the architecture of how do we wire the neurons together that are doing this this learning.

**13:17** · And among those three, it seems like all three could could be the missing piece that we're not getting right or what do you think? I If you're interested in perceptual learning, I think it's fairly clear you want retinotopic maps, a hierarchy of retinotopic maps.

**13:34** · So, the architecture is local connectivity.

**13:37** · Um And the point about that is you can solve a lot of the credit assignment problem by just assuming that something in one locality in a retinotopic map is going to be determined by the corresponding locality in the retinotopic map that feeds into it.

**13:56** · So, you're not trying to low down in the system um figure out how pixels determine what's going on a long distance away in the image. You're going to just use local interactions, and that gives you a lot of locality.

**14:11** · Um And you'd be crazy not to lose not to use that.

**14:16** · One thing neural nets do at present is they assume you're going to be using the same functions at every locality. So, convolutional nets do that, and transformers do that, too.

**14:25** · Um I don't think the brain can do that cuz that would involve weight sharing.

**14:30** · And it would involve doing exactly the same computation at each locality, so you can use the same weights.

**14:37** · I think it's most unlikely the brain does that.

**14:40** · But actually, there's a way to achieve what weight sharing does, what convolutional uh nets do in the brain in a much more plausible way than I think people have suggested before, which is if you do have contextual predictions trying to agree with locally extracted things, then imagine a whole bunch of columns that are making local predictions and looking at nearby columns to get their contextual prediction.

**15:09** · You can think of the context as a teacher for the local thing, but also vice versa.

**15:14** · But think of the context as a teacher for what you're extracting locally.

**15:18** · So, you can think of the information that's in the context as being distilled into the local extractor.

**15:26** · But that's true for all the local extractors.

**15:29** · So, what you've got is mutual distillation where they're all providing teaching signals for each other.

**15:35** · And what that means is knowledge about what you should extract in one location is getting transferred into other locations.

**15:45** · If they're trying to agree, if you're trying to get different locations to agree on something. If, for example, you find a nose and you find a mouth, and you want them both to agree that they're part of the same face. So, they should both give rise to the same representation.

**15:59** · Then the fact that you're trying to get the same representation at different locations allows knowledge to be distilled from one location to another.

**16:06** · And there's a big advantage of that over actual weight sharing.

**16:11** · Obviously, biologically, one advantage is that the detailed architecture in these different locations doesn't need to be identical.

**16:17** · But the other advantage is the front-end processing doesn't need to be the same.

**16:21** · So, if you take your retina, different parts of the retina have different size receptive fields.

**16:26** · And convolutional nets try to ignore that. They sometimes have multiple different resolutions and do convolution at each resolution. But they just can't deal with different front-end processing.

**16:37** · Um Whereas, if you're distilling knowledge from one location to another, what you're trying to do is get the same function from the optic array to the representation in these different locations.

**16:51** · And it's fine if you pre-process the optic array differently in the two different locations. You can still distill the knowledge across the function from the optic array to the representation, even though the front-end processing's different.

**17:05** · And so, although distillation is less efficient than actually sharing the weights, it's much more flexible. And it's much more neuronally plausible.

**17:14** · So, for me, that was a kind of big insight I had about a year ago that we have to have something like weight sharing to be efficient, but local distillation will work if you're trying to get neighboring things to agree on a representation.

**17:27** · That that idea of trying to get them to agree gives you the signal you need for knowledge in one location to supervise knowledge in another location.

**17:37** · And Jeff, do you think So, what you're describing, one way to think of it is to say, "Hey, weight sharing is clever cuz it's something the brain kind of does, too. It just does it differently, so we should continue to do weight sharing." Another way to think of it is that actually we shouldn't continue to do weight sharing because the brain does it somewhat differently, and there might be be a reason to do it differently.

**17:59** · What's your thinking? I think the brain doesn't do weight sharing cuz it's hard for it to ship symmetric strengths about the place.

**18:06** · It's very easy if they're all sitting in RAM. Um so, I think we should continue to do convolutional things in convnets and in transformers. We should share weights.

**18:16** · Um we should share knowledge by sharing weights.

**18:18** · But just bear in mind that the brain's going to share knowledge not by sharing weights, but by sharing the function from input to output and using distillation to transfer knowledge.

**18:29** · Now, there's the other topic that is talked about quite a bit where the brain is drastically different from our current neural nets, and it's the fact that neurons are work with spiking signals.

### Spiking neural networks

**18:42** · And that's very different from our artificial neurons in our GPUs.

**18:46** · And so, I'm very curious on your thinking on that. Is Is that just an engineering difference, or do you think there there could be more to it that we need to understand better and and benefits to spiking?

**18:58** · I think it's not just an engineering difference. I think once we understand why that hardware is so good, why you can do so much in such an energy-efficient way with that kind of hardware, um we'll see that um it's sensible for the brain to use spiking neurons. The retina, for example, doesn't use spiking neurons. The retina does lots of processing with non-spiking neurons.

**19:21** · So, once we understand why cortex is using neurons, um we'll see that it was the right thing for biology to do. And I think that's going to hinge on what the learning algorithm is, how you get gradients for networks of spiking neurons. And at present, nobody really knows. At present, what people do is say, "You see, the problem with the spiking neuron is there's two diff- quite different kinds of decision.

**19:49** · One is exactly when does it spike, and the other is does it or doesn't it spike?

**19:55** · So there's this discrete decision should the neuron spike or not, and then this continuous variable of exactly when it should spike.

**20:02** · And people trying to optimize this system like that have come up with various kind of surrogate functions which sort of smooth things a bit so you can get continuous functions. They don't seem quite right. Um it'd be really nice to have a learning algorithm. And in fact in NIPS in about 2000 Andy Brown and I had a paper on trying to learn spiking Boltzmann machines.

**20:24** · Um but it'd be really nice to get a learning algorithm that's good for spiking neurons. And I think that's the main thing that's holding up spiking neuron hardware.

**20:34** · So people like Steve Furber in Manchester have realized that many other people have realized that um you can make more energy efficient hardware this way. And they built great big systems.

**20:45** · What they don't have is a good learning algorithm for it. And I think until we've got a good learning algorithm for it we won't really be able to exploit what we can do with spiking neurons.

**20:53** · And there's one obvious thing you can do with them that isn't easy in conventional neural nets.

**20:58** · And that's agreement.

**21:01** · So if you take a standard artificial neuron and you simply ask the question can it tell if its two inputs have the same value?

**21:08** · Well it can't. It's not an easy thing for a standard neuron to do. A standard artificial neuron.

**21:13** · Um if you use spiking neurons it's very easy to build a system where if the two spikes arrive at the same time they'll make the neuron fire. If they arrive at different times they won't.

**21:23** · So using the time of the spike seems like a very good way of measuring agreement. We know the biological system does that.

**21:31** · So you can see the direction a sound is coming from or rather hear the direction sound is coming from by the time delay in the signals reaching the two ears.

**21:43** · And if you take a foot that's about a nanosecond for light and it's about a millisecond for sound.

**21:54** · And the point is if I move something sideways in front of you by a few inches the difference in the time delay to the two ears, the length of the path to the two ears is only a small fraction of an inch.

**22:09** · And so it's only a small fraction of a millisecond difference in the time the signal gets to the two ears. And we can deal with that and owls can deal with it even better.

**22:19** · Um And so we're measuring we're sensitive to times of like um 30 millisec 30 microseconds in order to get stereo from sound.

**22:31** · Um I can't remember what owls are sensitive to but it's I think it's a lot better than 30 microseconds.

**22:36** · And we do that by having um two axons with spikes traveling in different directions, one from one ear and one from the other ear.

**22:43** · And then you have cells that fire if the spikes get there at the same time.

**22:47** · That's a simplification but roughly that.

**22:49** · Um So we know that spike timing can be used for exquisitely sensitive things like that.

**22:55** · And it would sort of be very surprising if the precise times of spike wasn't being used. But we really don't know how.

### Leveraging spike times

**23:02** · And for a long time I thought it'd be really nice if you could use spike times to detect agreement for things like self-supervised learning.

**23:12** · Or for things like um if I've extracted your mouth and I've extracted your nose or rather representations of them.

**23:20** · Um and I from your mouth I can now predict something about your whole face. And from your nose I can predict something about your whole face.

**23:29** · And if your mouth and nose are in the right relationship to make a face those predictions will agree.

**23:34** · And it'd be really nice to use spike timing to see that those predictions agree.

**23:38** · Um but it's hard to make that work. And one of the reasons it's hard to make that work is because we don't know we don't have a good algorithm for training networks of spiking neurons. So that's one of the things I'm focused on now.

**23:50** · How can we get a good training algorithm that works with spiking neurons? And I think that'll have a big impact on hardware.

**23:56** · That's a really interesting question you're putting forward there cuz I doubt too many people are working on that compared to let's say the number of people working on large language models or um other problems that are much more I guess visible in terms of progress recently.

**24:12** · Um I think I'll Yeah it's always a good idea to figure out what huge numbers of very smart people are working on and to work on something else.

**24:22** · Yeah. I think the challenge of course for most people in in I'd say including myself but I definitely hear the question from many students too is that it's easy to work on something else than everybody else but it's hard to make sure that something else is actually relevant.

**24:36** · Uh cuz there's many other things out there that are not not very relevant you could possibly spend time on. Yeah that involves having good intuitions.

**24:44** · Yeah. Lis- listening to you for example could help. Um so I've actually a follow-up question something you just said Jeff which is that the retina doesn't use all spiking neurons. Are you saying that the brain has two types of neurons? Some that are more like our artificial neurons and some that are spiking neurons?

**25:07** · Um I'm not sure the retina is more like artificial neurons but um certainly the cortex has the neocortex has spiking neurons.

**25:17** · Um and that's its primary mode of communication is by sending spikes to from one pyramidal cell to another pyramidal cell.

**25:26** · Um and I don't think we're going to understand the brain until we understand why it chooses to send spikes.

**25:34** · For a while I thought I had a good argument that didn't involve the precise times of spikes.

**25:42** · And the argument went like this.

**25:43** · The brain's in the regime where it's got lots and lots of parameters and not much data relative to the typical neural nets we use.

**25:53** · And there's a danger of over fitting in that regime unless you use very strong regularization.

**25:59** · And a good regularization technique is dropout where each time you use a neural net you ignore a whole bunch of the units.

**26:07** · And so maybe the fact that the neurons are sending spikes what they're really communicating is the underlying Poisson rate.

**26:18** · So let's assume it's Poisson which is close enough for this argument. Um there's a Poisson process which sends sends spikes stochastically.

**26:27** · But the rate of that process varies and that's determined by the input to the neuron.

**26:32** · And you might think you'd like to send the real valued rate from one neuron to another.

**26:38** · Um but if you want to do lots and lots of regularization you could send the real valued rate with some noise added.

**26:46** · And one way to add noise is to just use spikes. That'll add lots of noise.

**26:52** · And so this was the motivation for dropout.

**26:56** · That the most of the times most of the neurons aren't involved in things if you look at any fine time window.

**27:04** · Um and you can think of spikes as a representation of underlying Poisson rate. It's just a very very noisy representation.

**27:13** · Which sounds like a very very bad idea because it's very very noisy. But actually once you understand about regularization when you have too many parameters it's a very very good idea.

**27:22** · So I still have a a lingering fondness for the idea that actually we're not using spike timing at all. Um it's just about um using very noisy representations of Poisson rates to be a good regularizer.

**27:36** · And I sort of flip between I think it's very important when you do science not to totally commit to one idea and ignore all the evidence for other ideas.

**27:45** · But if you do that you end up um flipping between ideas every few years.

**27:51** · So um some years I think neural nets are deterministic. I mean we should have deterministic neural nets and that's all backpropagation.

**28:00** · And other years I think spike timing cycle. I think no no it's very important that they're stochastic.

**28:06** · Um and that changes the flavor of everything. So Boltzmann machines were intrinsically stochastic and that was very important to them.

**28:12** · Um but the main thing is not to fully commit to either of those but to be open to both.

**28:18** · Now one thing if we think more about what you just said, the importance of spiking neurons and figuring out how to train a spiking neuron network effectively what what if we for now just say let's not worry about the training part?

**28:32** · Given that similarly it's far more power efficient. Um wouldn't people want to distribute pure inference chips that are you you pre-train effectively separately and then you compile it onto a spiking neuron chip to have very low power inference capabilities. What about that?

**28:52** · Yeah so lots of people have thought about that and um it's a very sensible idea. And it's probably on the evolutionary path to getting to use spiking neuron nets.

**29:01** · Because once you're using them for inference um and it works and it's all people already doing that and it's already working and been shown to be more power efficient. Um and various companies have produced these big spiking systems. Um once you're doing them for inference anyway you'll get more and more interested in how you could learn in a way that makes more use of the available power in the spike times.

**29:27** · So you can imagine a system where you learn using backprop um but not on not on analog hardware for example or not on the this low energy hardware.

**29:41** · Um and then you transfer it to the low energy hardware and that's fine.

**29:46** · Um but we'd really like to learn directly in the hardware.

**29:51** · Now, one thing that really strikes me, Jeff, is when I think about your talks back around 2005, 6, 7, 8, when I was a a PhD student, essentially pre-AlexNet talks. Um those talks, I think topically, have a lot of resemblance to what you're excited about now.

### The story behind AlexNet

**30:13** · And it almost feels like AlexNet is is an outlier in in your path.

**30:17** · Um how did you go from thinking so closely about how the brain might work to deciding that, you know, maybe you can first explain what was AlexNet, and but also how did it come about, and what was that path to go from working on restricted Boltzmann machines, trying to see how the brain works, to I would say that the more traditional approach to neural nets that you all of a sudden showed can actually work?

**30:40** · Well, um if you're an academic, you have to raise grant money, and it's convenient to have things that actually work, even if they don't work the way you're interested in.

**30:51** · Um so, part of it's that, just go with the flow, and um if you can make backprop work well.

**30:58** · And back then in about 2006, 2005, I got fascinated by the idea you could use stacks of restricted Boltzmann machines to pre-train feature detectors, and then it would be much easier to get backprop to work.

**31:13** · It turned out with enough data, which is what you had in speech recognition, um and later on, because of Fei-Fei Li and her team in image recognition, with enough data, you don't need the pre-training. Although pre-training is coming back. I mean, GPT-3 has pre-training.

**31:30** · Um and pre-training is a probably good idea.

**31:33** · Um but once we discovered that you could pre-train, and that would make backprop work better, and that did great things for speech, which George Dahl and Andre Ramo Muhammad did um in 2009, then Alex, who was a graduate student in my group then, um started uh applying the same ideas to vision.

**32:04** · Um and pretty soon we discovered that you shouldn't actually need this pre-training, especially if you have the ImageNet data.

**32:14** · And in fact, that project um was partly due to Ilya's persistence.

**32:20** · So, I remember Ilya coming into the lab one day and saying, "Look, we Now that we got speech recognition working, this stuff really works, we've got to do ImageNet before anybody else does."

**32:31** · And retrospectively, I learned that Yann LeCun was going into the lab and saying, "Look, we've got to do ImageNet with ConvNets before anybody else does."

**32:39** · And Yann's students also and postdocs said, "Oh, but I'm busy doing something else."

**32:45** · So, oh, but he he couldn't actually get someone to commit to it.

**32:49** · And Ilya initially couldn't get people to commit to it.

**32:53** · And so, Ilya persuaded Alex to commit to it by pre-processing the data for him.

**32:58** · So, he didn't have to pre-process the data. The data was all pre-processed to be just what he needed.

**33:02** · And then Alex really went to town. And Alex is just a superb programmer.

**33:06** · And it was Alex was able to make a couple of GPUs really sing. He made them work together in his bedroom at home.

**33:14** · Um I don't think his parents realized that they were paying less than the cost, cuz that was the electricity. Um but he did a superb job of programming convolutional nets on them.

**33:26** · Um so, Ilya said we've got to do this, and helped Alex with the design and so on. Alex did the really intricate programming.

**33:35** · And I provided support, um and a few ideas like using dropout.

**33:40** · Um I also did some good management. I'm not often very good at management, but I'm very proud of the management I did, which is Alex Krizhevsky had to write a depth oral to show that he was sort of capable of understanding research literature, which is what you have to do after a couple of years to stay in the PhD program.

**33:59** · And he doesn't really like writing. Um and he didn't really want to do the depth oral, but it was way past the deadline, and the department was hassling us.

**34:07** · So, I said to him, um each "Each time you can improve the performance by 1% on ImageNet, um you can delay your depth oral by another week."

**34:20** · And Alex delayed his depth oral by a whole lot of weeks.

**34:26** · Yeah, and just for context for I mean, a lot of researchers know this, of course, but maybe not everybody. Alex's result with you and Ilya cut the error rate in half compared to prior work on the ImageNet image recognition competition, which was just More or less. I I I used to be a professor, so it wasn't quite in half. Close. It cut it from about 26% to about 16 or 15%, depending on how you count.

**34:52** · It didn't cut it in half, but it cut it almost Almost in half. Whereas in previous years, the progress was by 1% or 2%. Here it was a whole different Well, that's why everybody switched from what they were doing, which was hand-engineered approaches to computer vision, try to program directly, how can a computer understand what's in an image to to deep learning? I should say one thing that's important to say here. Um Yann LeCun spent many years um developing convolutional neural nets.

**35:22** · Um and it really should have been him or his lab that developed that system.

**35:27** · We had a few little extra tricks, but they weren't the important thing. The important thing was to apply convolutional nets using GPUs to a big data set.

**35:35** · Um so, Yann was kind of unlucky in that um he didn't get the win on that.

**35:42** · But it was using many of the techniques that he developed. He didn't have the the Russian immigrants that Toronto and you had been able to attract to make it happen.

**35:51** · Well, one's Russian, one's Ukrainian, and it's important not to confuse them.

**35:54** · Even though the Ukraine is a Russian-speaking Ukrainian, don't confuse Russian with Ukrainian.

**35:58** · Absolutely.

**36:00** · It's a It's a different country.

**36:03** · So, now, Jeff, that moment actually also marked a big change in your career. Um because, as far as I understand, you've never been involved in corporate work.

### Transition from pure academia to Google

**36:17** · But it marked a transition for you soon thereafter from being a pure academic to being ending up at Google, actually.

**36:26** · Uh can you say a bit about that? How was that for you? Like did you have any internal resistance? I can say why that transition happened.

**36:34** · What triggered curious.

**36:36** · So, um I have a learning disabled son who needs um future provisions. So, I needed to get a lump of money.

**36:44** · And I thought one way I might get a lump of money was by teaching a Coursera course.

**36:49** · And so, I did a Coursera course on neural networks in 2012.

**36:54** · And it was one of the early Coursera courses, so their software wasn't very good. So, it was extremely irritating to do.

**36:59** · Um it really was very irritating then. Um I'm not very good on software, so I didn't like that.

**37:07** · And from my point of view, it amounted to you agree to supply a chapter of a textbook, one chapter every week. Um so, you had to give them these videos, and then a whole bunch of people are going to watch the videos. Like sometimes the next day, Yoshua Bengio would say, "Why did you say that?" Um so, you know that it's going to be people who know very little, but also people who know a whole lot. And so, it's stressful. You know that if you make mistakes, they're going to be caught.

**37:35** · Not like a normal lecture, where you can just sort of press on the sustaining pedal and sort of blur your way through it if you get some slightly confused about something. Um here, you have to get it straight.

**37:48** · And the deal with the University of Toronto originally was that um if any money was made from these courses, which I was hoping it would be, um the money that came to the university would be split with the professor. They didn't specify exactly what the split would be, but one assumed it would be like 50/50 or something like that.

**38:08** · And I was okay with that.

**38:10** · The university didn't provide any support in preparing the videos. Um and then, after I started the course, and when I could no longer back out of it, the provost made a unilateral decision, without consulting me or anybody else, um that actually if money came from Coursera, the university would take all the money, and the professor would get zero.

**38:33** · Which is exactly the opposite of what happens with textbooks.

**38:37** · And the process was very like writing textbooks.

**38:40** · Um I actually asked the university to help me prepare the videos, and the AV people came back to me and said, "Do you have any idea how expensive it is to make videos?"

**38:50** · And I actually did have an idea, cuz I've been doing this.

**38:55** · So, I got really pissed off with my university, because they unilaterally sort of canceled the idea I get any remuneration for this. They said it was part of my teaching. Well, actually, it wasn't part of my teaching. It was clearly based on lectures I give as part of my teaching, but I was doing my teaching as well as that, and that I wasn't using that course for my teaching.

**39:15** · And that got me pissed off enough that I was willing to consider alternatives to being a professor.

**39:22** · Um and at that time, we then suddenly got interest from all sorts of companies in the in recruiting us, um either in funding, giving big grants, or in funding a startup. Um it was clear that a number of big companies which had a very interest in getting in on the act.

**39:43** · And so normally I would have just said no, I'm I get paid by the state for doing research. Um I don't want to try and make extra money from my research. I'd rather get on with the research.

**39:57** · But because that particular experience with the university um cheating me out of the money. No, it turned out they didn't cheat me out of anything cuz uh no money came from the course anyway.

**40:07** · Um but that pushed me over the edge into thinking, well, okay, I'm going to find some other way to make some money. That was the end of my principles. Oh, no.

**40:18** · Well, but the result is that these companies are and in fact if if you read the the Genius Makers book by Cade Metz, which I reread last week in in preparation for for this conversation, um you read the book, it starts off with actually you running an auction for these companies to try to acquire your company, which is quite the start of a book.

### The secret auction of Hinton’s company at NuerIPS

**40:43** · Um very intriguing. But how was it for you? Oh, when it was happening, it was at NIPS.

**40:49** · Um Terry had organized NIPS in a casino.

**40:53** · Um at Lake Tahoe.

**40:58** · Um and so in the basement of the hotel, there were these smoke-filled rooms full of people pulling one-arm bandits and big lights flashing saying you won $25,000 and all that stuff. And people gambling um in other ways.

**41:13** · And upstairs we were running this auction.

**41:16** · And we felt like we were in a movie.

**41:20** · We felt like this was like being in that movie The Social Network. It sort of felt like that. It was great.

**41:26** · The reason we did it was we had absolutely no idea how much we were worth.

**41:32** · And I consulted a lawyer who an IP lawyer who said there's two ways to go about this.

**41:38** · You could hire a professional negotiator.

**41:41** · Um in that case, um you'll end up working for a company, but they'll be pissed off with you.

**41:48** · Um or you could just run an auction.

**41:52** · Um as far as I know, this was the first time a small group like that just ran an auction. We ran it on Gmail.

**42:00** · Um I'd worked at Google over the summer, so I knew enough about Google to know that they wouldn't read our Gmail.

**42:05** · Um and I'm still pretty confident they didn't read our Gmail.

**42:14** · Microsoft wasn't so confident.

**42:17** · And we just ran this auction where people had to Gmail me their bids.

**42:21** · And we then immediately mailed them out to everybody else with the timestamp of the Gmail.

**42:26** · And um it just kept going up by half a million dollars to I think it was half a million dollars to begin with and then a million dollars after that.

**42:35** · Um and yeah, it was pretty exciting.

**42:41** · And we discovered we were worth a lot more than we thought.

**42:45** · Um retrospectively, we could probably have got more, but we we got to an amount that we thought was astronomical.

**42:53** · And then basically we wanted to work for Google, so we stopped the auction so we could be sure of working for Google.

**43:01** · And as I understand it, you're still at Google today.

**43:05** · I'm still at Google today.

**43:07** · Um 9 years later. I'm in my 10th year there.

**43:10** · I think I'll get some kind of award when I've been there for 10 years cuz it's so rare.

**43:14** · Although people tend to stay at Google longer than other companies.

**43:17** · Yeah, I like it there. The the main reason I like it is because the Brain team's a very nice team.

**43:25** · And I get along very well with Jeff Dean. Um he's kind of very smart, but um very straightforward to deal with.

**43:34** · And what he wants me to do is do what I want to do, which is basic research.

**43:40** · Um he thinks what I should be doing is trying to come up with radically new algorithms. And that's what I want to do anyway.

**43:45** · So it's just a very nice fit. I'm no good at managing a big team to improve speech recognition by 1%. I'd be hopeless at that. Well, it's better to just revolutionize the field again, right? Yeah.

**43:58** · I I would like to do it one more time.

**44:00** · That's a bit ambitious.

**44:01** · forward to it. I wouldn't be surprised at all. Now, when when I look at your career, Jeff, and some of this information actually comes from the book cuz I didn't notice before I had read the book the first time. I mean, you are you were a computer science professor at the University of Toronto, emeritus now, I believe, but computer science, but you never got a computer science degree. You got a psychology degree.

### Hinton’s start in psychology and carpentry

**44:29** · And you actually at some point were a carpenter.

**44:34** · How How does it come about? How do you go from studying psychology to becoming a carpenter to getting into AI. What What's the path for you there? How do you look at that?

**44:45** · In my last year at Cambridge, I had a very difficult time and got very unhappy and I dropped out.

**44:51** · Um just after the exams I dropped out.

**44:53** · Um um became a carpenter.

**44:56** · Um and I'd always enjoyed carpentry more than anything else.

**45:03** · Um so at high school, um there'd be sort of all the classes and then you could stay in the evenings and do carpentry. And that's what I really looked forward to.

**45:12** · Um and so I became a carpenter. And then after I'd been a a carpenter for about 6 months, you couldn't actually make a living as a carpenter. Um so I was a carpenter and decorator. I'd make the money doing decorating, but had the fun doing carpentry.

**45:27** · Um and the point is carpentry is more work than it looks and decorating is less work than it looks.

**45:35** · Um so you can you can charge more per hour for decorating.

**45:39** · Um unless you're a very good carpenter.

**45:42** · And then I met a real carpenter.

**45:45** · And I realized I was completely hopeless at carpentry.

**45:49** · Um so he he was making a door for a basement for a a coal cellar under the sidewalk that was very damp.

**45:58** · And he was taking pieces of wood and arranging them so that they would warp in opposite directions so that it would cancel out.

**46:07** · And that was kind of a level of kind of understanding and thought about the process that never occurred to me. He could also take a piece of wood and just cut it exactly square with a handsaw.

**46:18** · Um and he explained something useful to me.

**46:20** · He said, "If you want to cut a piece of wood square, you have to line the sawbench up with the room and you have to line the piece of wood up with the room.

**46:30** · You can't cut it square if it's not aligned with the room."

**46:34** · Which is very interesting in terms of coordinate frames.

**46:37** · Um so anyway, because I was so hopeless compared with him, I decided I might as well go back into AI.

**46:46** · Now, when you say get back into AI, as I understand it, this was at the University of Edinburgh where you went for your PhD? Yeah.

**46:54** · I went to do a PhD there. And I went to do a PhD on neural networks with an eminent professor called Christopher Longuet-Higgins, who was really very brilliant. Um he almost got a Nobel Prize when he was in his 30s for figuring out something about the structure of boron hydride.

**47:14** · Um and I I still don't understand what it is cuz it's all to do with quantum mechanics. But it hinged on the fact that 360° rotation is not the identity operator. It's 720°.

**47:26** · Um there's a thing you want to find one of his books about it.

**47:30** · Um anyway, he was interested in neural nets and their relation to holograms. And about the day I arrived in Edinburgh, he lost interest in neural nets because he read Winograd's thesis and he became completely converted.

**47:46** · Um he thought neural nets was the wrong way to think about it. We should do symbolic AI. He was very impressed by Winograd's thesis.

**47:54** · Um and so we had he had a lot of integrity. So even though he completely disagreed with what he was I was doing, he didn't stop me doing it.

**48:05** · He kept trying to get me to do stuff more like Winograd's thesis, but he let me carry on doing what I was doing.

**48:11** · Um and yeah, I was a bit of a loner. Everybody else back then in the early '70s was saying, "Minsky and Papert have shown that neural nets are nonsense. Why are you doing this stuff? It's crazy."

**48:25** · And in fact, the first talk I ever gave to that group was about how to do true recursion with neural networks.

**48:34** · Um so this was a talk in 1973, so 49 years ago.

**48:39** · And so my one of my first projects, I discovered a write-up of it recently, was um you want a neural network that will be able to draw a shape.

**48:52** · And you want it to parse the shape into parts.

**48:58** · And you want it to be possible for a part of the shape to be done drawn by the same neural hardware as the whole shape's being drawn by.

**49:06** · So the neural hardware that's storing the whole shape has to remember where it's got to in the whole shape and what the um orientation and position sizes for the whole shape.

**49:19** · Um but now it has to go off and you want to use the very same neurons for drawing a part of the shape.

**49:26** · So you need somewhere to remember what the whole shape was and how far you got in it so that you can pop back to that once you finish doing this subregion, this part of the shape.

**49:37** · And the question is, how is a neural network going to remember that? Because obviously you can't just copy the neurons.

**49:42** · And so I managed to get a system working where the neural network remembered it by having fast heavy and weights that were just adapting all the time and were adapting so that any state that it had been in recently could be retrieved by giving it part of that state and then say fill in the rest.

**50:00** · And so I had a neural net that was doing true recursion, reusing the same neurons in the same way to do the recursive call as it used for the higher level call.

**50:09** · And that was in 1973. And the I think people didn't understand the talk cuz I wasn't very good at giving talks, but they also said, "Why would you want to do recursion with a neural net? You can do recursion with Lisp."

**50:22** · Um they didn't understand the point, which is that unless we get neural nets to do something like recursion we're never going to be able to explain a whole bunch of things.

**50:32** · And now that's become sort of an interesting question again.

**50:36** · So you know wait one more year until that idea is an antique, a genuine antique. It'll be 50 years old. And then I'm going to sort of write up the research I did then.

**50:46** · And it was all about fast weights for as I remember. So I have many questions here, Jeff. The first one is you're standing in this room where everybody's you're a PhD student or maybe fresh out of PhD is standing in a room with essentially everybody telling you what you're working on is is a waste of time.

**51:09** · And you were convinced somehow it was not.

**51:13** · Where did you get that conviction from?

**51:15** · I think a large part of it was my schooling.

**51:19** · So my father was a communist.

**51:24** · But he sent me to an expensive private school because they had good science education.

**51:31** · And I was there from the age of seven.

**51:34** · I mean I had a preschool.

**51:36** · And it was a Christian school.

**51:40** · And all the other kids believed in God.

**51:44** · And it was just at home I was told that that was nonsense.

**51:48** · And it did seem to me that it was nonsense.

**51:52** · Um and so I was used to just having everybody else being wrong and obviously wrong.

**52:03** · And I think that's important.

**52:06** · I think you need you need I was about to say you need the faith which is funny in this situation. Um you need the faith in science to um be willing to work on stuff just cuz it's obviously right even though everybody else says it's nonsense.

**52:26** · And in fact it wasn't everybody else. It was everybody else in the early '70s doing AI said it was nonsense or nearly everybody else.

**52:35** · Um but if you look a bit earlier, if you look in the '50s both von Neumann and Turing believed in neural nets.

**52:42** · Turing in particular believed in neural nets trained with reinforcement learning.

**52:46** · Um so if I I still believe if they hadn't both died early, the whole history of AI might have been very different.

**52:55** · Cuz they were sort of powerful enough intellects to have swayed a field.

**53:00** · And they were very interested in sort of how does the brain work?

**53:07** · So I think it was just bad luck they both died early.

**53:10** · Well, British intelligence might have come into it, but Now, you go from believing in this well at the time many people didn't to getting to big breakthroughs that now have that power almost everything that's being done today. And now there is this in some sense the next question, right? Uh is it's not just that deep learning works and works great. The question becomes, is it all we need or will we need other things?

**53:38** · And you've said things maybe I'm not literally quoting you, but to the extent of deep learning will do everything. What I really meant by that I I I sometimes say things without thinking without being accurate enough and then people call me on it like saying we won't need radiologists. Um so what I really meant was um using stochastic gradient descent to just a whole bunch of parameters. That's what I sort of had in mind when I said deep learning.

**54:09** · Um the way you get the gradient might not be back propagation.

**54:14** · And the thing you get the gradient of might not be some final performance measure, but rather these lots of local objective functions.

**54:22** · But I think that's how the brain works and I think that's going to explain everything. Yes. Well, nice nice to see it confirmed. Um So one of the thing I want to say is the kind of computers we have now um are very good for um doing banking um because they can remember how much you have in your account.

### Why computers should be grown rather than manufactured

**54:43** · It wouldn't be so good if you went in and they said, "Well, you've got roughly this much, so we're not really sure cuz we don't do it to that precision, but roughly this much."

**54:50** · Um we don't want that in a computer doing banking.

**54:55** · Um or in a computer guiding a space shuttle or something. We we would really rather it got the answer exactly right.

**55:02** · Um and they're very different from us.

**55:07** · And I think people aren't sufficiently aware that we made a decision about how computing would be um which is that um our computer our knowledge would be immortal.

**55:25** · So if you look at existing computers, you have a computer program or maybe you just have a lot of weights for a neural net.

**55:34** · That's a different kind of program.

**55:36** · Um but if your hardware dies, you can run the same program on another piece of hardware.

**55:43** · And so that makes the knowledge immortal. It doesn't hinge on that particular piece of hardware surviving.

**55:49** · Now the cost of the immortality is huge cuz it means the two bit different bits of hardware have to do exactly the same thing. Obviously there are corrections and all that, but after you've done all the error correction, they have to exactly the same thing.

**56:01** · Which means they better be digital or mostly digital.

**56:05** · Um and they're probably going to do things like multiplying numbers together, which involves using lots and lots of energy to make um things very discreet.

**56:17** · Which is not what hardware really wants to be.

**56:20** · And so as soon as you commit yourself to the immortality of your program or your neural net you're committed to um very expensive computations and also to very expensive manufacturing processes. You need to manufacture these things accurately and probably in 2D and then put lots of 2D things together.

**56:43** · Um if you're just willing to give up on immortality sort of in fiction normally what you get in return is love. Um but if if we're willing to give up immortality, what we'll get in return is very low energy computation and very cheap manufacturing.

**57:01** · So instead of manufacturing computers what we should do is grow them.

**57:08** · Um we should use nanotechnology to just grow the things in 3D.

**57:13** · And each one will be slightly different.

**57:17** · So the image I have is if you take a pot plant and you sort of pull it out of its pot, there's a root ball and it's the shape of the pot, right?

**57:25** · And so all the different pot plants have the same shape root ball, but the details of the roots are all different, but they're all doing the same thing.

**57:32** · They're extracting nutrients from the soil.

**57:34** · And they've got the same function and they're pretty much the same, but the details are all very different.

**57:39** · Um so that's what real brains are like.

**57:43** · And I think that's what what I call mortal computers will be like.

**57:48** · So these are computers that are grown rather than manufactured.

**57:53** · Um you can't program them, they just learn.

**57:56** · They obviously have to have a learning algorithm sort of built into them.

**57:59** · They learn. They can do most of their computation in analog cuz analog's very good for doing things like taking a voltage times a resistance and turning it into a charge and then adding up the charge. And there already chips that do things like that.

**58:16** · The problem is what do you do next? Um and how do you learn in those chips?

**58:22** · And at present people have suggested back propagation or various versions of Boltzmann machines.

**58:27** · Um I think we're going to need something else.

**58:30** · But I think sometime in the not too distant future we're going to see mortal computers which are very cheap to create have to get all their knowledge in there by learning and are very low energy.

**58:46** · And these mortal computers when they die, they die and their knowledge dies with them.

**58:52** · And so and it's no use looking at the weights because those weights only work for that hardware.

**58:57** · Um so what you're going to have to do is distill the knowledge into other computers. So when these mortal computers get old they're going to have to do lots of podcasts to try and get the knowledge into younger mortal computers. The first one you build, I'll happily have that one on.

**59:10** · Let me know.

**59:12** · So Jeff, this reminds me of another uh question that's been on my mind uh for you, which is when you think about today's neural nets the ones that grabbed the headlines are very very large. I mean, not as large yet as as the brain maybe, but in some sense starting to get to that size, right? The large language models.

**59:36** · Um But and and the results look very very impressive. Um So, one I'm I'm curious about your take on those kinds of models and and what you see in them and what you see as limitations, but two I'm also curious about what do you think about working on the other end of the spectrum? For example, ants have much smaller brains.

**1:00:01** · Um obviously than than humans. Yet it's fair to say that our visual motor systems that we have developed artificially are not yet at the level of what ants can can pull off or bees and so forth.

**1:00:15** · And so, I'm curious about that spectrum as well as the the recent big advances in language models, what you think about those.

**1:00:22** · So, bees, they may look small to you, but I think a bee has about a million neurons.

**1:00:28** · So, I think a bee is closer to GPT-3.

**1:00:34** · Certainly closer than an ant is.

**1:00:37** · But a bee's actually quite a big neural net.

**1:00:39** · Um My belief is that um if you take a system with lots of parameters and they're tuned sensibly using some kind of gradient descent in some kind of sensible objective function, then you'll get wonderful properties out of it.

**1:00:56** · Um you'll get all these emerging properties.

**1:00:59** · Um like you do with GPT-3 and also the the the Google equivalents that I've talked about so much.

**1:01:07** · That doesn't sort of settle the issue of whether they're doing it the same way as us. And I think um we're doing a lot more things like recursion, which I think we do in neural nets.

**1:01:23** · And I tried to address some of these issues in a paper I put on the web last year called Glom.

**1:01:28** · Um well, I call it Glom. It's how you do part-whole hierarchies in neural nets.

**1:01:33** · So, you definitely have to have structure.

**1:01:35** · And if what you mean by symbolic computation is just that you have part-whole structure, then we do symbolic computation. That's not normally what people meant by symbolic computation.

**1:01:45** · The sort of hardline symbolic computation means you're using symbols and you're operating on symbols using rules that just depend on the form of the symbol string you're processing.

**1:01:58** · And that a symbol the only property a symbol has is that it's either identical or not identical to some other symbol.

**1:02:05** · And perhaps that it points to something.

**1:02:07** · It can be used as a pointer to get something.

**1:02:09** · Um the neural net's are very different from that.

**1:02:13** · So, the sort of hardline symbol processing, I don't think we do that. But we certainly deal with um part-whole hierarchies.

**1:02:22** · But I think we do it in great big neural nets.

**1:02:26** · And I'm sort of up in the air at present as to to what extent does GPT-3 really understand what it's saying.

**1:02:33** · I think it's fairly clear it's not just like the old Eliza program, which just rearranges strings of symbols and had no clue what it was talking about.

**1:02:43** · Um and the reason for believing that is you say you say in English, show me a picture of a hamster wearing a red hat, and it draws a picture of a hamster wearing a red hat.

**1:02:53** · Um And you're fairly sure it never got that pair before.

**1:02:59** · So, it has to understand the relationship between the English string and the picture.

**1:03:04** · Um and before it's done that, if you'd asked any of these um doubters, um these neural net skeptics, uh neural net deniers, let's call them neural net deniers. Um if you'd asked them, well, how would you show that it understands?

**1:03:24** · I think they'd have accepted that, well, if you ask it to draw a picture of something and it draws a picture of that thing, then it understood.

**1:03:29** · Just as with Winograd thesis, you ask it to put the blue the blue block in the green box and it puts the blue block in the green box. And so, that's pretty good evidence it understood what you said.

**1:03:40** · Um But now that it does it, of course, the skeptics then say, well, you know, that doesn't really count.

**1:03:47** · There's nothing that would satisfy them, basically. Yeah, the the goal line's always moving uh for for true skeptics. Yeah.

**1:03:56** · Now, there's the recent one, um the Google one, the Palm model that uh in in the paper showed how it was explaining effectively how jokes work. That was extraordinary, wasn't it?

**1:04:08** · seemed a very deep understanding of of of language. No, it was just rearranging the words it had in its training set.

**1:04:14** · You think so? No.

**1:04:17** · No, it had I I don't see how it could generate those explanations without sort of understanding what's going on. No, I'm still open to the idea that because it was trained with backpropagation, it's going to end up with a very different sort of understanding from us.

**1:04:33** · And obviously adversarial images um tell you a lot that you can recognize objects by using their textures.

**1:04:42** · And you can be correct about it in the sense that it'll generalize to other instances of those objects. But it's a completely different way of doing it from what we do.

**1:04:51** · And I like to think of the example of insects and flowers. So, insects see in the ultraviolet.

**1:04:56** · So, two flowers that look the same to us can look completely different to insects.

**1:05:01** · And now, because the flowers look the same to us, do we say the insects are getting it wrong?

**1:05:07** · Um cuz these flowers evolved with the insects to give signals to the insects in the ultraviolet to tell them which flower it is. So, it's clear the insects are getting it right and we just can't see the difference.

**1:05:17** · And that's another way of thinking about adversarial examples.

**1:05:21** · Um it looks, you know, this this thing that it says is an ostrich looks like a looks like a school bus to us. But actually, if you look in the texture domain, then it's actually an ostrich. So, um the question is who's right? And in the case of the insects, um just because two two flowers look identical to us, it doesn't mean they're really the same. The insects are right about them being very different. And in that case, it's different parts of the electromagnetic spectrum that are indicating the difference that we don't pick up on. But it could be texture.

**1:05:50** · of image recognition for our current neural nets, so you could argue maybe that um since we build them and we want them to do things for us in our world that we we really don't want to just say, okay, they got it right and we got it wrong. I mean, they need to recognize the car and the pedestrian.

**1:06:09** · Yeah, I agree. I just wanted to show it's not as simple as you might think about who's right and who's wrong.

**1:06:13** · Um and part of the point of my Glom paper was um to try and build perceptual systems that work more like us.

**1:06:24** · So, they're much more likely to make the same kinds of mistakes as us.

**1:06:27** · And not make very different kinds of mistakes. And obviously, um if you've got a self-driving car, for example, if it makes a mistake that any normal human driver would have made, that seems much more acceptable than making a really dumb mistake from our point of view.

**1:06:47** · So, Jeff, as I understand it, sleep is something you also think about. Can you say a bit more?

**1:06:55** · Yes, I often think about it when I'm not sleeping at night. Um So, there's something funny about sleep, which is um animals do it. Fruit flies sleep.

### The function of sleep and Boltzmann Machines

**1:07:08** · And it may just be to stop them flying around in the dark. But um if you deprive people of sleep, then they go really weird.

**1:07:17** · Like if you deprive someone for 3 days, they'll start hallucinating. If you deprive someone for a week, they'll go psychotic and may never recover.

**1:07:25** · Um These are nice experiments done by the CIA, I think. Um and the question is why?

**1:07:34** · Why do we What What is the computational function of sleep? There's presumably some pretty important function for it if depriving of it makes you just completely fall apart.

**1:07:44** · And so, current theories are things like it's for consolidating memories or maybe for downloading things from hippocampus into cortex, which is a bit odd since they had to come through cortex to get to the hippocampus in the first place.

**1:07:55** · Um So, a long time ago in the early '80s, Terry Sejnowski and I had this theory called Boltzmann machines.

**1:08:03** · And it was partly based on an insight of Francis Crick um when he was thinking about Hopfield nets. Francis Crick and Graeme Mitchison had a paper about sleep. And the idea that um you would hit the net with random things and tell it not to be happy with random things. So, in a Hopfield net, you give it something you wanted it to memorize and it changes the weights so the energy of that vector is lower.

**1:08:28** · And the idea is if you also give it random vectors and say make the energy higher, the whole thing works better.

**1:08:34** · And that led to Boltzmann machines where we figured out that um if you, instead of giving it random things, you get it things generated from a Markov chain, the model's own Markov chain, and you say make those less likely and make the data more likely, that is actually a maximum likelihood learning rule.

**1:08:51** · And so, we got very excited about that because we thought, okay, that's what sleep is for. Sleep is this negative phase of learning.

**1:08:58** · It comes up again now in contrastive learning where you have two patches from the same image, you try and get get them to have similar representations.

**1:09:08** · And two patches from different images, you try and get them to have representations that are sufficiently different. Once they're different, you don't make them any more different, but you stop them being too similar.

**1:09:20** · And that's how contrastive learning works.

**1:09:22** · Now, with Boltzmann machines, you couldn't actually separate the positive phase from the negative phase.

**1:09:28** · You had to interleave positive examples and negative examples.

**1:09:32** · Otherwise, the whole thing would go wrong.

**1:09:34** · And I went to I tried a lot not interleaving them, and it's quite hard to do a lot of follow positive examples followed by a lot of negative examples.

**1:09:43** · What I discovered a couple of years ago that got me very excited and caused me to agree to give lots of talks that that I then canceled when I couldn't make it work better.

**1:09:52** · Um was that with contrastive learning you can actually separate the positive and negative phases.

**1:10:02** · So, you can do lots of examples of positive pairs followed by lots of examples of negative pairs.

**1:10:09** · And that's great because what that means is you can have something like a video pipeline where you're just trying to make things similar while you're awake and trying to make things dissimilar while you're asleep.

**1:10:23** · Um if you can figure out how sleep can generate video for you. Um So, it makes it makes our contrastive learning algorithm much more plausible if you can separate the positive and negative phases and do them at different times and do a whole bunch of positive updates followed by a whole bunch of negative updates.

**1:10:43** · And even for the standard contrastive learning, you can do that moderately well.

**1:10:49** · You have to use lots of momentum and stuff like that. There's all sorts of little tricks to make it work, but you can make it work.

**1:10:54** · Um So, I now think it's quite likely that the function of sleep is to do unlearning on negative examples.

**1:11:04** · And that's why you don't remember your dreams. You don't want to remember them.

**1:11:08** · You're unlearning them.

**1:11:09** · Crick pointed this out. You'll remember the ones that are in the fast weights when you wake up.

**1:11:14** · Um cuz the fast weights are a temporary store, so that's not unlearning. That's still works the same way.

**1:11:21** · But the long-term memory, um the whole point is to get rid of those things, and that's why you dream for many hours a night, but when you wake up, you can just remember the last minute of the dream you're having when you woke up.

**1:11:33** · Um and I think this is a much more plausible theory of sleep than any other I've seen because it explains why if you got rid of it, the whole system would just fall apart.

**1:11:43** · It'll go disastrously wrong and start hallucinating and do all sorts of weird things.

**1:11:47** · But let me say a little bit more about the need for negative examples that you have in contrastive learning.

### Need for negative data

**1:11:54** · If you've got a neural net and it's trying to optimize some internal objective function, something about the kinds of representations it has or something about the agreement between contextual predictions and local predictions.

**1:12:05** · Um it wants this agreement to be a property of the real data.

**1:12:13** · And the problem inside a neural net is that you might get all sorts of correlations in your inputs. I'm a neuron, right? So, I get all sorts of correlations in my inputs, and those correlations have nothing to do with the real data. They're caused by the wiring of the network and the weights in the network.

**1:12:27** · If these two neurons are both looking at the same pixel, they'll have a correlation, but that doesn't tell you anything about the data.

**1:12:35** · And so, the question is how do you learn to extract structure that's about the real the real data and not about the wiring of your network?

**1:12:46** · And the way to do that is to feed it positive examples and say find structure in the positive examples that isn't in the negative examples.

**1:12:54** · Cuz the negative examples are going to go through exactly the same wiring.

**1:12:58** · And if the structure is not in the negative examples, but it is in the positive examples then the structure is about the difference between the positive and negative examples, not about your wiring.

**1:13:08** · So, as people don't think about this much, but if you have powerful learning algorithms, then you better not make them learn about the neural network's own weights and wiring. That's not what's interesting.

**1:13:19** · Now, when you think about people who don't get sleep done and start hallucinating, is hallucinating just effectively trying to do the same thing, you're just doing it while you're awake?

**1:13:29** · Obviously, you can have little naps, and that's very helpful.

**1:13:32** · And maybe hallucinating while you're awake is serving the same function as sleep.

**1:13:36** · And it's I mean, all the experiments I've done say it's better to not have 16 hours awake and 8 hours of sleep.

**1:13:43** · It's better to have a few hours awake and a few hours of sleep. So, and a lot of people have discovered that. Little naps help. Einstein used to take little naps all the time. And he did okay.

**1:13:55** · Yeah, he did very well.

**1:13:56** · No, for sure.

**1:13:59** · Now, this is another thing you uh you've brought up, this notion of student beats teacher.

**1:14:06** · What does that refer to?

**1:14:08** · Okay, so um a long time ago I did an experiment on MNIST.

**1:14:13** · Um which is a standard digit database for recognizing handwritten digits.

**1:14:18** · Where um you take the data, the training data and you corrupt it.

**1:14:28** · And you corrupt it by substituting the wrong label, one of the other nine labels 80% of the time.

**1:14:38** · So, now you've got a data set in which the labels are correct um 20% of the time and wrong 80% of the time.

**1:14:48** · And the question is um can you learn from that?

**1:14:52** · And how well do you learn from that?

**1:14:54** · And the answer is you can learn to get like 95% correct on that.

**1:14:58** · So, now you've got a teacher who's wrong 80% of the time and the student is right 95% of the time.

**1:15:06** · So, the student is much, much better than the teacher.

**1:15:09** · And this isn't um each time you get an example, you corrupt it. You take the training examples, you corrupt them once and for all. So, you can't average away the corruption over different You might be able to average it it away over different training cases that happen to have similar images.

**1:15:24** · But and if you ask, well, how many training cases do you need if you have corrupted ones?

**1:15:30** · And this was of great interest cuz of the tiny images data set some time ago where they had 80 million tiny images with a lot of wrong labels in.

**1:15:37** · And the question is would you rather have a million things that are flakily labeled or would you rather have 10,000 things with accurate labels?

**1:15:47** · And I had a hypothesis that what counts is the amount of mutual information between the label and the truth.

**1:15:54** · So, if the labels are correct corrupted 90% of the time, there's no mutual information between the labels and the truth.

**1:16:01** · If they're corrupted 80% of the time, there's only a small amount of mutual information. It's actually you think it's I think it's about my memory is it's 0.06 bits per case.

**1:16:10** · Whereas if it's uncorrected, it's about 3.3 bits per case.

**1:16:14** · Um so, it's only a tiny amount. And then the question is, well suppose I balance the size of the training set by putting as much mutual information in there.

**1:16:23** · Um so, if if there's like a 50th of the mutual information, I have 50 times as many examples, do I now get the same performance?

**1:16:31** · And the answer is yes, you do to within a factor of two. I mean, the training set actually needs to be twice that big, but roughly speaking you can see how useful a training example is by the amount of mutual information between the label and the truth.

**1:16:45** · And I've noticed recently you have something for doing sim to real where you're labeling real data using a neural net, and those labels aren't perfect. And then you take the student that learned from those labels, and the student is better than the teacher it learned from.

**1:16:59** · And people are always puzzled by how could the student be better than the teacher?

**1:17:04** · Um but in neural nets, it's very easy.

**1:17:07** · Um the student will be better than the teacher if there's enough training data.

**1:17:13** · Um even if the teacher is very flaky.

**1:17:15** · And I have a paper a few years ago with Melody Guan about this for some medical data. Uh and the first part of the paper talks about this.

**1:17:23** · But the the rule of thumb is basically what counts is the mutual information between the assigned label and the truth.

**1:17:31** · And that tells you how valuable a training example is.

**1:17:34** · And so, you can make do with lots of flaky ones.

**1:17:37** · That's so interesting. Now, in the work we did that you just referenced, Javin, and the work I've seen quite popular recently usually the the teacher provides noisy labels.

**1:17:51** · But then not all the noisy labels are used. There's a notion that only look at the ones where the teacher is more confident.

**1:18:00** · Your description doesn't really care about a good hack, but you Yeah, you don't need to do that. You don't need to do that. It's a good hack, and it probably helps to only look at the ones where you have reason to believe the teacher got it right. But it'll work even if you just look at them all.

**1:18:13** · And there's a phase transition.

**1:18:15** · So, with with MNIST Melody plotted a graph, and as soon as you get like 20% of the labels right your student will get like 95% correct.

**1:18:26** · Wow.

**1:18:26** · But as you get down to about 15% right, you suddenly get a phase transition where you don't do any better than chance.

**1:18:33** · Cuz somehow the student has to get it.

**1:18:35** · The teacher is saying these labels, and the student has to in some sense understand which cases are right and which cases are wrong and sort of see the relationship between the labels and the inputs.

**1:18:48** · And then once the student's seen that relationship, a wrongly labeled thing is just very obviously wrong.

**1:18:53** · Um so, it's fine if it's randomly wrongly labeled.

**1:18:57** · But there is a phase transition where you have to have it good enough so the student can sort of get the idea.

**1:19:02** · But that explains how our students are all smarter than us.

**1:19:07** · Wait, how do you need to get it right a small fraction of the time?

**1:19:10** · Right. And I'm sure the students do some of this data curation where you say something and the student thinks, "Oh, that's rubbish. I'm not going to listen to that."

**1:19:18** · Those are the very best students, you know.

**1:19:21** · Yeah, those are the those are the ones that can surprise us.

**1:19:24** · Um Now, one of the things that is really important in neural net learning, and especially when you're building models, is to get an understanding of what is it What is it learning? And often people try to somehow visualize what's happening during learning. And one of the most prevalent visualization techniques is called t-SNE, um which is something you invented, Jeff.

### Visualizing data using t-SNE

**1:19:50** · So, I'm curious, how how did you come up with that? What what if maybe first describe what it does, and then what's the story behind it?

**1:19:56** · So, if you have some high-dimensional data, and you try and draw a 2D or 3D map of it, you could take the first two principal components and just plot the first two principal components.

**1:20:09** · But, what principal components cares about is getting the big distances right. So, if two things are very different, principal components is very concerned to get them very different in the 2D space.

**1:20:20** · It doesn't care at all about the small differences, cuz it's it's sort of operating on the squares of the big differences.

**1:20:26** · Um so, it won't preserve similarity very well.

**1:20:30** · High-dimensional similarity.

**1:20:32** · And you're often interested in just the opposite. You've got some data, you're interested in what's very similar to what. And you don't care if it gets the big distances a bit wrong, as long as it gets the small distances right.

**1:20:43** · So, I had the idea a long time ago that what if we took the distances, and we turned them into probabilities of pairs.

**1:20:53** · There's various versions of t-SNE, but suppose we turned them into the probability of a pair, such that we say pairs with a small distance are probable, and pairs with a big distance are improbable.

**1:21:06** · So, we're converting distances into probabilities in such way that small distances correspond to big probabilities.

**1:21:11** · And we do that by putting a Gaussian around a point, a data point, and computing the density of the other data point under this Gaussian.

**1:21:19** · And that's an unnormalized probability, then you normalize these things.

**1:21:23** · Um And then you try and lay the points out in 2D, so as to preserve those probabilities.

**1:21:31** · And so, it won't care much if two points are far apart, they'll have a very low pairwise probability. And it doesn't care the relative positions of those two points. What it cares about the relative positions of those with high probabilities. And that produced quite nice maps, and that was called stochastic neighbor embedding, cuz we thought of this You put a Gaussian, and then you stochastically pick a neighbor according to the density under the Gaussian.

**1:21:53** · Um and I did that work with Sam Roweis, and it had very nice simple derivatives, um which convinced me that we were onto something. And we got nice maps, but they tended to crowd things together.

**1:22:04** · And there's obviously a basic problem in converting high-dimensional data into low-dimensional data.

**1:22:12** · So, SNE tends to crowd things together, stochastic neighbor embedding.

**1:22:16** · And that's because of the nature of high-dimensional spaces and low-dimensional spaces.

**1:22:20** · In a high-dimensional space, a data point can be close to lots of other points without them all being too close to each other.

**1:22:28** · In a low-dimensional space, they all have to be close to each other if they're all close to this data point.

**1:22:33** · So, you've got a problem in embedding closenesses from high dimensions to low dimensions.

**1:22:40** · And I had the idea when I was doing SNE that since I was using probabilities as this kind of intermediate currency, um there should be a mixture model.

**1:22:51** · There should be a mixture version, where you're saying in high dimensions, the probability of a pair is proportional to e to the minus d squared distance on the Gaussian. Um And in low dimensions, suppose you have two different maps.

**1:23:07** · The probability of a pair is the sum of e to the minus the distance in the first 2D map, and e to the minus d squared distance in the second 2D 2D map.

**1:23:17** · And that way, if we have a word like bank, and we're trying to put similar words near one another, bank can be close to greed in one map, and can be close to river in the other map, without river ever being close to greed.

**1:23:30** · So, I really pushed that idea, cuz I thought this is a really neat idea, and you could have a mixture of maps.

**1:23:36** · And we managed to get it to work. Ilya was one of the first people to work on that. And James Cook worked on it a lot.

**1:23:42** · Um and several other students worked on it, and we never really got it to work well.

**1:23:46** · Um And I was very disappointed that someone had been able to make use of the mixture idea.

**1:23:52** · And then I went to a simpler version, which I called UniSNE, which was a mixture of a Gaussian and a uniform.

**1:24:02** · And that worked much better.

**1:24:05** · Um So, the idea is in one map, all pairs are equally probable.

**1:24:13** · And that gives you a sort of background probability, which goes with the big distances, a small background probability.

**1:24:19** · And then in the other map, you contribute um a probability proportional to your squared distance in this other map.

**1:24:28** · But, it means in this other map, things can be very far apart if they want to be, because the fact that then they need some probability is taken care of by the uniform map.

**1:24:41** · And then I got a review paper from from a call of Laurens van der Maaten, which I thought was actually a published paper cuz of the form it arrived in, but wasn't actually a published paper.

**1:24:51** · And he wanted to come do research with me. And I thought he had this published paper, so I invited him to come do research. Um turned out he was extremely good, and it's lucky I'd been mistaken in thinking it was a published paper. Um And we started on UniSNE.

**1:25:05** · And then I realized that actually UniSNE is a special case of using a mixture of a Gaussian and a very, very broad Gaussian, which is a uniform.

**1:25:18** · So, what if we used a whole hierarchy of Gaussians?

**1:25:21** · Many, many Gaussians with different widths.

**1:25:23** · And that's called a T distribution.

**1:25:26** · Um And that led to t-SNE, and t-SNE works much better.

**1:25:31** · And t-SNE has a very nice property that um it can show you things at multiple scales.

**1:25:38** · Because it's got a kind of 1 over d squared property that um once distances get big, it behaves just like gravity and clusters of galaxies and things. They're clusters of galaxies and galaxies and clusters of stars and so on. And you get structure at many different levels in it. You get the coarse structure and the fine structure all showing up.

**1:26:00** · Now, the objective function used for all this, which was the sort of relative densities under a Gaussian, came from other work I did with Alberto Paccanaro earlier, um that we found hard to get published.

**1:26:15** · Um I got a review saying Yeah, I got a review of that work when it was rejected by some conference, saying "Hinton's been working on this idea for 7 years, and nobody's interested."

**1:26:29** · I take those reviews as telling me I'm onto something very original. Um And that actually had the function in it that's now used I think it's called NCE.

**1:26:39** · It's using these contrasted methods.

**1:26:42** · Um and t-SNE is actually a version of that function, um but it's being used for making maps.

**1:26:48** · So, it's a very long history of t-SNE of getting the original SNE, and then trying to make a mixture version, and it's just not working and not working and not working, and then eventually getting the coincidence of figuring out it was a T distribution is what you wanted to use. That was the kind of mixture. And Laurens arriving, and Laurens was very smart and a very good programmer, and he made it all work beautifully.

**1:27:12** · This is really interesting, because it seems a lot of the um a lot of the progress these days, the the bigger idea plays plays a big role, but here it seems it was really getting the details right was the only way to get it to fully work. You typically need both.

**1:27:30** · You have to have a big idea for it to be interesting original stuff, but you also have to get the details right.

**1:27:35** · And that's what graduate students are for.

**1:27:38** · Okay.

**1:27:39** · Jeff, thank you thank you for such a wonderful uh conversation for our part one of our season finale.
