---
title: The future of intelligence | Demis Hassabis (Co-founder and CEO of DeepMind)
source_url: https://www.youtube.com/watch?v=PqVbypvxDto
video_id: PqVbypvxDto
account: '[[accounts/google-deepmind|Google DeepMind]]'
account_name: Google DeepMind
account_url: https://www.youtube.com/@googledeepmind
featured_people:
- '[[people/demis-hassabis|Demis Hassabis]]'
published: 2025-12-17
created: 2026-07-21
language: en
speaker_attribution: contextual
description: In our final episode of the season, Professor Hannah Fry sits down with Google DeepMind Co-founder and CEO Demis Hassabis for their annual check-in. Together, they look beyond the product launches to
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=PqVbypvxDto)

In our final episode of the season, Professor Hannah Fry sits down with Google DeepMind Co-founder and CEO Demis Hassabis for their annual check-in. Together, they look beyond the product launches to the scientific and technological questions that will define the next decade.  
  
Demis shares his vision for the path to AGI - from solving "root node" problems in fusion energy and material science to the rise of world models and simulations. They also explore what's beyond the frontier and the importance of balancing scientific rigor amid the competitive dynamics of AI advancement.  
  
Thanks for joining us this year!  
🔔 Subscribe to stay updated on our return in 2026, and revisit our episode library to catch up on everything from driverless cars to drug discovery: https://www.youtube.com/playlist?list=PLqYmG7hTraZBiUr6\_Qf8YTS2Oqy3OGZEj  
  
Timecodes  
01:42 2025 progress  
05:14 Jagged intelligence  
07:32 Mathematical version of AlphaGo?  
09:30 Science vs commercialization  
12:42 Scaling  
17:43 Genie and simulation  
25:47 Evolution in simulation  
28:26 AI bubble  
31:56 Building ethical AI  
34:31 AGI  
44:44 Turing machines  
49:06 How it feels to lead  
  
\_\_\_  
  
Thanks to everyone who made this possible, including but not limited to:  
Presenter: Professor Hannah Fry  
Series Producer: Dan Hardoon  
Editor: Rami Tzabar  
Commissioner & Producer: Emma Yousif  
Music composition: Eleni Shaw  
Audio engineer: Richard Courtice  
  
Studio Manager: Nicholas Duke  
Video Director: Bernardo Resende  
Video Editor: Anthony Le  
Audio Engineer: Perry Rogantin  
Production Coordination: Zoey Roberts  
Visual Identity and Design: Rob Ashley  
Commissioned by Google DeepMind  
  
\_\_  
  
Subscribe to our channel https://www.youtube.com/@googledeepmind  
Find us on X https://twitter.com/GoogleDeepMind  
Follow us on Instagram https://instagram.com/googledeepmind  
Add us on Linkedin https://www.linkedin.com/company/deepmind/

## Transcript

**0:00** · DEMIS HASSABIS: Effectively, you can think of as 50% of our effort is on scaling, 50% of it is on innovation.

**0:05** · My betting is you're going to need both to get to AGI.

**0:07** · I've always felt this, that if we build AGI, and then use that as a simulation of the mind, and then compare that to the real mind, we will then see what the differences are and potentially what's special and remaining about the human mind.

**0:23** · Maybe that's creativity.

**0:25** · Maybe it's emotions.

**0:25** · Maybe it's dreaming, consciousness.

**0:29** · There's a lot of hypotheses out there about what may or may not be computable.

**0:34** · And this comes back to the Turing machine question of, what is the limit of a Turing machine?

**0:39** · HANNAH FRY: So there's nothing that cannot be done within these computational-- DEMIS HASSABIS: Well, put it this way.

**0:44** · Nobody's found anything in the universe that's non-computable, so far.

**0:49** · HANNAH FRY: So far.

**0:50** · \[THEME MUSIC\] Welcome to "Google DeepMind: The Podcast" with me, Professor Hannah Fry.

**0:57** · It has been an extraordinary year for AI.

**1:00** · We have seen the center of gravity shift from large language models to agentic AI.

**1:05** · We've seen AI accelerate drug discovery and multimodal models integrated into robotics and driverless cars.

**1:12** · Now, these are all topics that we've explored in detail on this podcast.

**1:16** · But for the final episode of this year, we wanted to take a broader view, something beyond the headlines and product launches, to consider a much bigger question.

**1:23** · Where is all this heading, really?

**1:26** · What are the scientific and technological questions that will define the next phase?

**1:32** · And someone who spends quite a lot of their time thinking about that is Demis Hassabis, CEO and co-founder of Google DeepMind.

**1:39** · Welcome back to the podcast, Demis.

**1:41** · DEMIS HASSABIS: Great to be back.

**1:41** · HANNAH FRY: I mean, quite a lot has happened in the last year.

### 2025 progress

**1:44** · DEMIS HASSABIS: It has.

**1:45** · HANNAH FRY: What is the biggest shift, do you think?

**1:47** · DEMIS HASSABIS: Oh, wow.

**1:48** · I mean, it's just so much has happened, as you said.

**1:51** · It feels like we packed in 10 years in one year.

**1:54** · I think a lot's happened.

**1:55** · I mean, certainly, for us, the progress of the models-- we've just released Gemini 3, which we're really happy with-- the multi-modal capabilities, all of those things have just advanced really well.

**2:07** · And then probably the thing, I guess, over the summer that I'm very excited about is world models being advanced.

**2:12** · I'm sure we're going to talk about that.

**2:14** · HANNAH FRY: Yeah, absolutely.

**2:15** · We will get on to all of that stuff in a little bit more detail in a moment.

**2:18** · I remember the very first time I interviewed you for this podcast, and you were talking about the root node problems, about this idea that you can use AI to unlock these downstream benefits.

**2:27** · And you've made pretty good on your promise, I have to say.

**2:30** · DEMIS HASSABIS: Yes.

**2:30** · HANNAH FRY: Do you want to give us an update on where we are with those?

**2:33** · What are the things that are just around the corner and the things that you've sort of solved or near solved?

**2:38** · DEMIS HASSABIS: Yeah.

**2:39** · Well, of course, the big proof point was AlphaFold.

**2:41** · And it's crazy to think we're coming up to five-year anniversary of AlphaFold being announced to the world-- AlphaFold2, at least.

**2:49** · So that was the proof, I guess, that it was possible to do these root node type of problems.

**2:54** · And we're exploring all the other ones now.

**2:56** · I think material science.

**2:58** · I'd love to do a room temperature superconductor.

**3:01** · And better batteries, these kinds of things-- I think that's on the cards, better materials of all sorts.

**3:08** · We're also working on fusion.

**3:10** · HANNAH FRY: Because there's a new partnership that's been announced with fusion, right?

**3:13** · DEMIS HASSABIS: Yeah.

**3:13** · We've just announced a partnership with a deep one.

**3:15** · We already were collaborating with them, but it's a much deeper one now with Commonwealth Fusion, who I think are probably the best startup working on at least traditional tokamak reactors.

**3:25** · So they're probably closest to having something viable.

**3:30** · And we want to help accelerate that, helping them contain the plasma in the magnets and maybe even some material design there, as well.

**3:37** · So that's exciting.

**3:38** · And then we're collaborating also with our quantum colleagues, which they're doing amazing work at the quantum AI team at Google.

**3:46** · And we're helping them with error correction codes, where we're using our machine learning to help them.

**3:51** · And then maybe one day they'll help us.

**3:52** · \[LAUGHS\] HANNAH FRY: That perfect cycle.

**3:54** · DEMIS HASSABIS: Yes, exactly.

**3:55** · HANNAH FRY: The fusion one is particularly-- I mean, the difference that that would make to the world, that would be unlocked by that, is gigantic.

**4:01** · DEMIS HASSABIS: Yeah.

**4:01** · I mean, fusion has always been the holy grail.

**4:03** · Of course, I think solar is very promising, too, effectively using the fusion reactor in the clouds and in the sky.

**4:10** · But I think if we could have modular fusion reactors, this promise of unlimited, renewable, clean energy would be-- obviously, transform everything.

**4:23** · And that's the holy grail.

**4:24** · And, of course, that's one of the ways we could help with climate.

**4:28** · HANNAH FRY: It does make a lot of our existing problems sort of disappear if we can \[INAUDIBLE\].

**4:32** · DEMIS HASSABIS: Definitely.

**4:33** · I mean, it opens up many-- this is why we think of it as a root node.

**4:36** · Of course, it helps directly with energy and pollution and so on and helps with the climate crisis.

**4:44** · But also, if energy really was renewable and clean and super cheap, almost free, then many other things would become viable, like water access because we could have desalination plants pretty much everywhere, even making rocket fuel.

**4:59** · There's lots of seawater that contains hydrogen and oxygen, and that's basically rocket fuel.

**5:03** · But it just takes a lot of energy to split it out into hydrogen and oxygen.

**5:06** · But if energy is cheap and renewable and clean, then why not do that?

**5:11** · You could have that producing 24/7.

**5:13** · HANNAH FRY: You're also seeing a lot of change in the AI that is applying itself to mathematics-- winning medals in the International Maths Olympiad.

### Jagged intelligence

**5:22** · And yet, at the same time, these models can make quite basic mistakes in high school math.

**5:27** · Why is there that paradox?

**5:29** · DEMIS HASSABIS: Yeah.

**5:29** · I think it's fascinating, actually, one of the most fascinating things, and probably that needs to be fixed as one of the key things why we're not at AGI yet.

**5:37** · As you said, we've had a lot of success in other groups on getting gold medals at the International Maths Olympiad.

**5:41** · You look at those questions, and they're super hard questions that only the top students in the world can do.

**5:47** · And, on the other hand, if you pose a question in a certain way-- we've all seen that with experimenting with chat bots ourselves in our daily lives-- that it can make some fairly trivial mistakes on logic problems.

**5:59** · They can't really play decent games of chess yet, which is surprising.

**6:04** · So there's something missing still from these systems in terms of their consistency.

**6:08** · And I think that's one of the things that you would expect from a general intelligence, an AGI system, is that it would be consistent across the board.

**6:17** · And so sometimes people call it jagged intelligences.

**6:21** · So they're really good at certain things, maybe even PhD level.

**6:25** · But then, other things, they're not even high school level.

**6:28** · So it's very uneven still, the performances of these systems.

**6:31** · They're very, very impressive in certain dimensions, but they're still pretty basic in others.

**6:37** · And we've got to close those gaps.

**6:38** · And there are theories as to why.

**6:40** · And depending on the situation, it could even be the way that an image is perceived and tokenized.

**6:47** · So sometimes, actually, it doesn't even get all the letters that-- so when you count letters in words, it sometimes gets that wrong.

**6:54** · But it may not be seeing each individual letter.

**6:57** · So there's different reasons for some of these things.

**7:00** · And each one of those can be fixed, and then you can see what's left, but I think consistency.

**7:05** · I think another thing is reasoning and thinking.

**7:08** · So we have thinking systems now that, at inference time, they spend more time thinking, and they're better at outputting their answers.

**7:16** · But it's not super consistent yet in terms of, is it using that thinking time in a useful way to actually double-check and use tools to double-check what it's outputting?

**7:28** · I think we're on the way, but maybe we're only 50% of the way there.

### Mathematical version of AlphaGo?

**7:32** · HANNAH FRY: I also wonder about that story of AlphaGo and then AlphaZero, where you took away all of the human experience and found that the model actually improved.

**7:40** · DEMIS HASSABIS: Yeah.

**7:41** · HANNAH FRY: Is there a scientific or a maths version of that in the models that you're creating?

**7:45** · DEMIS HASSABIS: I think what we're trying to build today, it's more like AlphaGo.

**7:49** · So effectively, these large language models, these foundation models, they're starting with all of human knowledge, what we put on the internet, which is pretty much everything these days, and compressing that into some useful artifact which they can look up and generalize from.

**8:06** · But I do think we're still in the early days of having this search or thinking on top, like AlphaGo had, to use that model to direct useful reasoning traces, useful planning ideas, and then come up with the best solution to whatever the problem is at that point in time.

**8:26** · So I don't feel like we're constrained at the moment with the limit of human knowledge, like the internet.

**8:32** · I think the main issue at the moment is, we don't know how to use those systems in a reliable way fully yet in the way we did with AlphaGo.

**8:40** · But, of course, that was a lot easier because it was a game.

**8:42** · I think once you have AlphaGo there, you could go back, just like we did with the Alpha series, and do an AlphaZero, where it starts discovering knowledge for itself.

**8:54** · I think that would be the next step, but that's obviously harder.

**8:57** · And so I think it's good to try and create the first step first with some kind of AlphaGo-like system.

**9:03** · And then we can think about an AlphaZero-like system.

**9:06** · But that is also one of the things missing from today's systems is the ability to online learn and continually learn.

**9:12** · So we train these systems, we balance them, we post-train them, and then they're out in the world.

**9:18** · But they don't continue to learn out in the world, like we would.

**9:22** · And I think that's another critical missing piece from these systems that will be needed for AGI.

**9:28** · HANNAH FRY: In terms of all of those missing pieces, I mean, I know that there's this big race at the moment to release commercial products, but I also know that Google DeepMind's roots really lie in that idea of scientific research.

### Science vs commercialization

**9:40** · And I found a quote from you where you recently said, "If I'd had my way, we would have left AI in the lab for longer and done more things like AlphaFold, maybe cured cancer or something like that."

**9:50** · Do you think that we lost something by not taking that slower route?

**9:55** · DEMIS HASSABIS: I think we lost and gained something.

**9:57** · So I feel like that would have been the more pure scientific approach.

**10:01** · At least, that was my original plan, say 15, 20 years ago, that when almost no one was working on AI-- we just started.

**10:08** · We were just about to start DeepMind.

**10:10** · People thought it was a crazy thing to work on.

**10:13** · But we believed in it.

**10:15** · And I think that the idea was, if we would make progress, we would continue to incrementally build towards AGI, be very careful about what each step was and the safety aspects of it and so on, analyze what the system was doing and so on.

**10:31** · But in the meantime, you wouldn't have to wait till AGI arrived before it was useful.

**10:35** · You could branch off that technology and use it in really beneficial ways to society, namely advancing science and medicine, so exactly what we did with AlphaFold, actually, which, it's not a foundation model itself, general model, but it uses the same techniques, transformers and other things, and then blends it with more specific things to that domain.

**10:57** · So I imagined a whole bunch of those things getting done which would be hugely-- you'd release to the world, just like we did with AlphaFold and, indeed, do things like cure cancer and so on whilst we were working on more the AGI track in the lab.

**11:12** · Now, it's turned out that chatbots were possible at scale, and people find them useful.

**11:18** · And then they've now morphed into these foundation models that can do more than chat and text, obviously, including Gemini.

**11:25** · They can do images and video and all sorts of things.

**11:28** · And that's also been very successful commercially in terms of a product.

**11:34** · And I love that, too.

**11:35** · I've always dreamed of having the ultimate assistant that would help you in everyday life, make it more productive, maybe even protect your brain space a bit, as well, from inattention so that you can focus and be in flow and so on because today, with social media, it's just noise, noise, noise.

**11:49** · And I think AI, actually, that works for you could help us with that.

**11:54** · So I think that's good, but it has created this pretty crazy race condition where there's many commercial organizations and even nation states all rushing to improve and overtake each other.

**12:06** · And that makes it hard to do rigorous science at the same time.

**12:12** · We try to do both, and I think we're getting that balance right.

**12:15** · On the other hand, there are lots of pros of the way it's happened, which is, of course, there's a lot more resources coming into the area.

**12:21** · So that's definitely accelerated progress.

**12:24** · And, also, I think the general public are actually, interestingly, only a couple of months behind the absolute frontier in terms of what they can use.

**12:33** · So everyone gets the chance to feel for themselves what AI is going to be like.

**12:37** · And I think that's a good thing and then governments sort of understanding this better.

**12:41** · HANNAH FRY: The thing that's strange is that-- I mean, this time last year, I think there was a lot talk about scaling, eventually hitting a wall, about us running out of data.

### Scaling

**12:50** · And yet, we're recording-- now, Gemini 3 has just been released, and it's leading on this whole range of different benchmarks.

**12:58** · How has that been possible?

**13:00** · Wasn't there supposed to be a problem with scaling hitting a wall?

**13:03** · DEMIS HASSABIS: I think a lot of people thought that, especially as other companies have had slower progress, shall we say.

**13:09** · But I think we've never really seen any wall, as such.

**13:13** · What I would say is maybe there's diminishing returns.

**13:17** · And when I say that, people only think, oh, so there's no returns.

**13:21** · It's 0 or 1.

**13:22** · It's either exponential, or it's asymptotic.

**13:25** · No.

**13:26** · Actually, there's a lot of room between those two regimes.

**13:29** · And I think we're in between those.

**13:31** · So it's not like you're going to double the performance on all the benchmarks every time you release a new iteration.

**13:38** · Maybe that's what was happening in the very early days, three, four years ago.

**13:42** · But you are getting significant improvements, like we've seen with Gemini 3, that are well worth the investment and the return on that investment and doing.

**13:50** · So that, we haven't seen any slowdown on.

**13:53** · There are issues like, are we running out of just available data?

**13:57** · But there are ways to get around that-- synthetic data, generating-- these systems are good enough, they can start generating their own data.

**14:04** · Especially in certain domains like coding and math, where you can verify the answer, in some sense, you could produce unlimited data.

**14:11** · So all of these things, though, are research questions.

**14:15** · And I think that's the advantage that we've always had is that we've always been research-first.

**14:22** · And I think we have the broadest and deepest research bench, always have done.

**14:27** · And if you look back at the last decade of advances, whether that's transformers or AlphaGo, AlphaZero, any of the things we just discussed, that they all came out of Google or DeepMind.

**14:36** · So I've always said, if more innovations are needed, scientific ones, then I would back us to be the place to do it, just like we were in the previous 15 years for a lot of the big breakthroughs.

**14:49** · So I think that's just what's transpiring.

**14:51** · And I actually really like it when the terrain gets harder, because then it's not just world-class engineering you need, which is already hard enough, but you have to ally that with world-class research and science, which is what we specialize in.

**15:05** · And on top of that, we also have the advantage of world-class infrastructure with our TPUs and other things that we've invested in for a long time.

**15:13** · And so that combination, I think, allows us to be at the frontier of the innovations, as well as the scaling part.

**15:22** · And, effectively, you can think of as 50% of our effort is on scaling, 50% of it is on innovation.

**15:28** · And my betting is you're going to need both to get to AGI.

**15:31** · HANNAH FRY: I mean, one thing that we are still seeing, even in Gemini 3, which is an exceptional model, is this idea of hallucinations.

**15:38** · So I think there was one metric that said it can still give an answer when actually it should decline.

**15:45** · DEMIS HASSABIS: Yes.

**15:46** · HANNAH FRY: I mean, could you build a system where Gemini gives a confidence score in the same way that AlphaFold does?

**15:51** · DEMIS HASSABIS: Yeah, I think so.

**15:53** · And I think we need that, actually.

**15:55** · And I think that's one of the missing things.

**15:57** · I think we're getting close.

**15:58** · I think the better the models get, the more they know about what they know, if that makes sense.

**16:03** · And I think the more reliable-- you could rely on them to actually introspect in some way or do more thinking and actually realize for themselves that they're uncertain, or there's uncertainty over this answer.

**16:17** · And then we've got to work out how to train it in a way where it can output that as a reasonable answer.

**16:25** · We're getting better at it.

**16:27** · But it still sometimes-- it forces itself to answer when it probably shouldn't, and then that can lead to a hallucination.

**16:36** · So I think a lot of the hallucinations are of that type, currently.

**16:40** · So there's a missing piece there that has to be solved, and you're right, as we did solve it with AlphaFold, but in obviously a much more limited way.

**16:48** · HANNAH FRY: Because presumably, behind the scenes, there is some sort of measure of probability of whatever the next token might be.

**16:54** · DEMIS HASSABIS: Yes, there is of the next token.

**16:56** · That's how it all works.

**16:57** · But that doesn't tell you the overall arching piece, is how confident are you about this entire fact or this entire statement?

**17:06** · And I think that's why you'll need this-- I think we'll need to use the thinking steps and the planning steps to go back over what you just output.

**17:13** · At the moment, it's a little bit like the systems are just-- it's like talking to a person, and when they're on a bad day, they're just literally telling you the first thing that comes to their mind.

**17:23** · Most of the time, that will be OK.

**17:25** · But then sometimes, when it's a very difficult thing, you'd want to stop, pause for a moment, and maybe go over what you were about to say and adjust what you were about to say.

**17:34** · But perhaps that's happening less and less in the world these days, but that's still the better way of having a discourse.

**17:39** · So I think you can think of it like that.

**17:42** · These models need to do that better.

### Genie and simulation

**17:43** · HANNAH FRY: I also really want to talk to you about the simulated worlds and putting agents in them because we got to talk to your Genie team earlier this year.

**17:50** · DEMIS HASSABIS: Yes, it's awesome work.

**17:51** · HANNAH FRY: Tell me why you care about simulation.

**17:53** · What can a world model do that a language model can't?

**17:57** · DEMIS HASSABIS: Well, look, it's actually been-- it's probably my longest-standing passion is world models and simulations, in addition to AI, and of course it's all coming together in our most recent work, like Genie.

**18:09** · And I think language models are able to understand a lot about the world-- I think, actually, more than we expected, more than I expected, because language is actually probably richer than we thought.

**18:19** · It contains more about the world than even linguists maybe imagined.

**18:23** · And that's proven now with these new systems.

**18:26** · But there's still a lot about the spatial dynamics of the world-- spatial awareness and the physical context we're in and how that works mechanically-- that is hard to describe in words and isn't generally described in corpuses of words.

**18:44** · And a lot of this is allied to learning from experience, online experience.

**18:47** · There's a lot of things which you can't really describe something.

**18:50** · You have to just experience it.

**18:52** · Maybe the senses and so on are very hard to put into words, whether that's motor angles and smell and these kind of senses.

**19:01** · It's very difficult to describe that in any kind of language.

**19:04** · So I think there's a whole set of things around that.

**19:06** · And I think if we want robotics to work or a universal assistant that maybe comes along with you in your daily life, maybe on glasses or on your phone and helps you in your everyday life, not just on your computer, you're going to need this kind of world understanding, and world models are at the core of that.

**19:26** · So what we mean by world model is this sort of model that understands the causative and effect of the mechanics of the world-- intuitive physics, but how things move, how things behave.

**19:38** · Now, we're seeing a lot of that in our video models, actually.

**19:41** · And one way to show, how do you test you have that kind of understanding?

**19:45** · Well, can you generate realistic worlds?

**19:48** · Because if you can generate it, then, in a sense, you must have understood-- the system must have encapsulated a lot of the mechanics of the world.

**19:55** · So that's why Genie and Veo and these models, our video models and our interactive world models, are really impressive, but also important steps towards showing we have generalized world models.

**20:08** · And then hopefully, at some point, we can apply it to robotics and universal assistants.

**20:13** · And then, of course, one of my favorite things I'm definitely going to have to do at some point is reapplying it back to games and game simulations and create the ultimate games, which, of course, was maybe always my subconscious plan.

**20:26** · HANNAH FRY: All of this, just for that.

**20:27** · DEMIS HASSABIS: Yeah, all of this time, exactly.

**20:29** · HANNAH FRY: What about science, too, though, because you use it in that domain?

**20:31** · DEMIS HASSABIS: Yes, you could.

**20:33** · So science, again, I think, building models of scientifically complex domains, whether that's materials on the atomic level in biology, but also some physical things, as well, like weather-- one way to understand those systems is to learn simulations of those systems from the raw data.

**20:57** · So you have a bunch of raw data.

**20:59** · Let's say it's about the weather.

**21:00** · And, obviously, we have some amazing weather projects going on.

**21:03** · And then you have a model that learns those dynamics and can recreate those dynamics more efficiently than doing it by brute force.

**21:14** · So I think there's huge potential for simulations and world models, maybe specialized ones, for aspects of science and mathematics.

**21:22** · HANNAH FRY: But then, also, I mean, you can drop an agent into that simulated world too, right?

**21:26** · DEMIS HASSABIS: Yes.

**21:27** · HANNAH FRY: Your Genie 3 team, they had this really lovely quote, which was, "Almost no prerequisite to any major invention was made with that invention in mind."

**21:36** · And they were talking about dropping agents into these simulated environments and allowing them to explore with curiosity being their main motivator.

**21:43** · DEMIS HASSABIS: Right.

**21:44** · And so that's another really exciting use of these world models is you can-- we have another project called SIMA-- we just released SIMA 2-- simulated agents, where you have an avatar or an agent, and you put it down into a virtual world.

**21:58** · It can be a normal-- it can be a kind of actual commercial game or something like that, a very complex one, like "No Man's Sky," a kind of open-world space game.

**22:07** · And then you can instruct it because it's got Gemini under the hood.

**22:11** · You can just talk to the agent and give it tasks.

**22:14** · But then we thought, well, wouldn't it be fun if we plugged Genie into SIMA and dropped a SIMA agent into another AI that was creating the world on the fly?

**22:25** · So now the two AIs are kind of interacting in the minds of each other.

**22:29** · So the SIMA agent is trying to navigate this world.

**22:32** · And as far as Genie is concerned, that's just a player, and an avatar doesn't care that it's another AI.

**22:39** · So it's just generating the world around whatever SIMA is trying to do.

**22:42** · So it's kind of amazing to see them both interacting together.

**22:47** · And I think this could be the beginning an interesting training loop, where you almost have infinite training examples because, whatever the SIMA agent is trying to learn, Genie can basically create on the fly.

**22:59** · So I think that you could imagine a whole world of setting and solving tasks, just millions of tasks automatically, and they're just getting increasingly more difficult.

**23:09** · So we may try to set up a kind of loop like that, as well as obviously those SIMA agents could be great as game companions, or also some of the things that they learn could be useful also for robotics.

**23:21** · HANNAH FRY: Yeah, the end of boring NPCs, basically.

**23:23** · DEMIS HASSABIS: Exactly.

**23:24** · It's going to be amazing for these games.

**23:26** · Yeah.

**23:26** · HANNAH FRY: Those worlds that you're creating, though, how do you make sure that they really are realistic?

**23:31** · I mean, how do you ensure that you don't end up with physics that looks plausible but is actually wrong?

**23:35** · DEMIS HASSABIS: Yeah, that's a great question and can be an issue.

**23:40** · It's basically hallucinations again.

**23:41** · So some hallucinations are good because it also means you might create something interesting and new.

**23:46** · So, in fact, sometimes, if you're trying to do creative things or trying to get your system to create new things, novel things, a bit of hallucination might be good.

**23:54** · But you want it to be intentional, so you switch on the hallucinations now or the creative exploration.

**24:03** · But, yes, when you're trying to train a SIMA agent, you don't want Genie hallucinating physics that are wrong.

**24:10** · So, actually, what we're doing now is we're almost creating a physics benchmark, where we can use game engines, which are very accurate with physics, to create lots of fairly simple-- like the sorts of things you would do in your physics A-level lab lessons, like rolling little balls down different tracks and seeing how fast they go, and so really teasing apart on a very basic level Newton's three laws of motion.

**24:38** · Has it encapsulated it?

**24:40** · Whether that's Veo or Genie, have these models encapsulated the physics of that 100% accurately?

**24:46** · And right now, they're not.

**24:47** · They're kind of approximations.

**24:48** · And they look realistic when you just casually look at them, but they're not accurate enough yet to rely on for, say, robotics.

**24:57** · So that's the next step.

**24:58** · So I think, now we've got these really interesting models, I think one of the things, just like we're trying with all of our models, is to reduce the hallucinations and make them even more grounded.

**25:08** · And with physics, I think that's going to probably involve generating loads and loads of ground truth, simple videos of pendulums.

**25:15** · What happens when two pendulums go around each other?

**25:18** · But then, very quickly, you get to three-body problems, which are not solvable anyway.

**25:22** · So I think it's going to be interesting.

**25:24** · But what's amazing already is, when you look at the video models like Veo and just the way it treats reflections and liquids, it's pretty unbelievably accurate already, at least to the naked eye.

**25:36** · So the next step is actually going beyond what a human amateur can perceive, and would it really hold up to a proper physics-grade experiment?

**25:45** · HANNAH FRY: I know you've been thinking about these simulated worlds for a really long time.

### Evolution in simulation

**25:49** · And I went back to the transcript of our first interview, and in it, you said that you really liked the theory that consciousness was this consequence of evolution, that at some point in our evolutionary past, there was an advantage to understanding the internal state of another, and then we turned it in on ourselves.

**26:05** · Does that make you curious about running an agent evolution inside of a simulation?

**26:11** · DEMIS HASSABIS: Sure.

**26:12** · I mean, I'd love to run that experiment at some point, kind of rerun evolution, rerun almost social dynamics, as well.

**26:23** · Santa Fe used to run lots of cool experiments on little grid worlds.

**26:26** · I used to love some of these.

**26:27** · They're mostly economists, and they were trying to run little artificial societies, and they found that all sorts of interesting things got invented that, if you let agents run around for long enough with the right incentive structures-- markets, and banks, and all sorts of crazy things.

**26:43** · So I think it would be really cool and also just to understand the origin of life and the origin of consciousness.

**26:49** · And I think that is one of the big passions I had for working on AI from the beginning was, I think you're going to need these kinds of tools to really understand where we came from and what these phenomena are.

**27:01** · And I think simulations is one of the most powerful tools to do that because you can then do it statistically because you can run the simulation many times with slightly different initial starting conditions and then maybe run it millions of times and then understand what the slight differences are in a very controlled experiment sort of way, which, of course, is very difficult to do in the real world for any of the really interesting questions we want to answer.

**27:28** · So I think accurate simulations will be an unbelievable boon to science.

**27:32** · HANNAH FRY: Given what we've discovered about emergent properties of these models, having conceptual understanding that we weren't expecting, do you also have to be quite careful about running those sort of simulations?

**27:42** · DEMIS HASSABIS: I think you would have to be, yes.

**27:44** · But that's the other nice thing about simulations.

**27:46** · You can run them in pretty safe sandboxes.

**27:49** · Maybe eventually you want to airgap them.

**27:52** · And you can, of course, monitor what's happening in the simulation 24/7, and you have access to all the data.

**28:01** · So we may need AI tools to help us monitor the simulations because they'll be so complex, and there'll be so much going on in them.

**28:09** · If you imagine loads of AIs running around in a simulation, it'll be hard for any human scientist to keep up with it.

**28:17** · But we could probably use other AI systems to help us analyze and flag anything interesting or worrying in those simulations automatically.

**28:25** · HANNAH FRY: I mean, I guess we're still talking medium to long-term in terms of this stuff.

### AI bubble

**28:30** · So just going back to the trajectory that we're on at the moment, I also wanted to talk to you about the impact that AI and AGI are going to have on wider society.

**28:40** · And last time we spoke, you said that you thought AI was overhyped in the short term, but underhyped in the long term.

**28:46** · And I know that, this year, there's been a lot of chatter about an AI bubble.

**28:49** · DEMIS HASSABIS: Yes.

**28:50** · HANNAH FRY: What happens if there is a bubble, and it bursts?

**28:53** · What happens?

**28:54** · DEMIS HASSABIS: Well, look, I think, yes, I still subscribe to, it's overhyped in the short term and still underappreciated in the medium to long term, how transformative it's going to be Yeah, there is a lot of talk, of course, right now, about AI bubbles.

**29:10** · In my view, I think there isn't-- it's not one thing, binary thing-- are we, or aren't we?

**29:16** · I think there are parts of the AI ecosystem that are probably in bubbles.

**29:21** · One example would be just seed rounds for startups that basically haven't even got going yet, and they're raising at tens of billions of dollars valuations just out of the gate.

**29:33** · It's sort of interesting to see, can that be sustainable?

**29:37** · My guess is, probably not, at least not in general.

**29:41** · So there's that area.

**29:42** · Then people are worrying about-- obviously, there's the big tech valuations and other things.

**29:47** · I think there's a lot of real business underlying that.

**29:49** · But it remains to be seen.

**29:52** · I mean, I think maybe for any new, unbelievably transformative and profound technology, of which, of course, AI is probably the most profound, you're going to get this overcorrection, in a way.

**30:04** · So when we started DeepMind, no one believed in it.

**30:06** · No one thought it was possible.

**30:08** · People were wondering, what's AI for, anyway?

**30:10** · And then now, fast-forward 10, 15 years, and now, obviously, it seems to be the only thing people talk about in business.

**30:19** · But you're going to get-- it's almost an overreaction to the under-reaction.

**30:23** · So I think that's natural.

**30:24** · I think we saw that with the internet.

**30:25** · I think we saw it with mobile.

**30:27** · And I think we're seeing it or going to see it again with AI.

**30:30** · I don't worry too much about, are we in a bubble or not?

**30:33** · because from my perspective, as leading Google DeepMind and also, obviously, with Google and Alphabet as a whole, our job and my job is to make sure, either way, we come out of it very strong, and we're very well-positioned.

**30:48** · And I think we are tremendously well-positioned either way.

**30:51** · So if it continues going like it is now, fantastic.

**30:55** · We'll carry on all of these great things that we're doing in experiments and progress towards AGI.

**31:00** · If there's a retrenchment, fine.

**31:02** · Then, also, I think we're in a great position because we have our own stack with TPUs.

**31:07** · We also have all these incredible Google products and the profits that all makes to plug in our AI into.

**31:15** · And we're doing that, with Search is totally revolutionized by AI Overviews, AI Mode, with Gemini under the hood.

**31:21** · We're looking at Workspace, at email, at YouTube.

**31:25** · So there's all these amazing things in Chrome.

**31:27** · There's all these amazing things that we can see already are low-hanging fruit to apply Gemini to, as well, of course, as Gemini app, which is doing really well, as well, now and the idea of universal assistant.

**31:40** · So there's new products, and I think they will, in the fullness of time, be super valuable.

**31:45** · But we don't have to rely on that.

**31:47** · We can just power up our existing ecosystem, which is all-- I think that's what's happened over the last year.

**31:54** · We've got that really efficient now.

**31:55** · HANNAH FRY: In terms of the AI that people have access to at the moment-- I know you said recently how important it is not to build AI to maximize user engagement, just so we don't repeat the mistakes of social media.

### Building ethical AI

**32:06** · But I also wonder whether we are already seeing this, in a way-- I mean, people spending so much time talking to their chatbots that they end up kind of spiraling into self-radicalizing.

**32:16** · DEMIS HASSABIS: Yeah.

**32:17** · HANNAH FRY: How do you stop that?

**32:19** · How do you build AI that puts users at the center of their own universe, which is the point of this, in a lot of ways, but without creating echo chambers of one?

**32:28** · DEMIS HASSABIS: Yeah.

**32:29** · It's a very careful balance that I think is one of the most important things that we, as an industry, have got to get right.

**32:36** · So I think we've seen what happens with some systems that were overly sycophantic, or then you get these echo chamber reinforcements that are really bad for the person.

**32:48** · So I think part of it is-- and actually, this is what we want to build with Gemini.

**32:52** · And I'm really pleased with the Gemini 3 persona that we had a great team working on and I helped with, too, personally-- is just this almost like a scientific personality, that it's warm, it's helpful, it's light, but it's succinct, to the point, and it will push back on things, in a friendly way, that don't make sense, rather than trying to reinforce the idea that the Earth is flat, and you said it, and it's like, wonderful idea.

**33:20** · I don't think that's good in general for society if that were to happen.

**33:24** · But you've got to balance it with what people want because people want these systems to be supportive, to be helpful with their ideas and their brainstorming.

**33:34** · So you've got to get that balance right.

**33:37** · And I think we're developing a science of personality and persona of how to measure what it's doing, and where do we want it to be on authenticity, on humor, these sorts of things?

**33:51** · And then you can imagine there's a base personality that it ships with, and then everyone has their own preferences.

**33:57** · Do you want it to be more humorous, less humorous, or more succinct, or more verbose?

**34:01** · People like different things.

**34:02** · So you add that additional personalization layer on it, as well.

**34:06** · But there's still the core base personality that everyone gets, which is sort of trying to adhere to the scientific method, which is the whole point of these.

**34:13** · And we want people to use these for science and for medicine and health issues and so on.

**34:18** · And so I think it's part of the science of getting these large language models right.

**34:26** · And I'm quite happy with the direction we're going in, currently.

### AGI

**34:31** · HANNAH FRY: We got to talk to Shane Legg a couple of weeks ago about AGI, in particular.

**34:37** · Across everything that's happening in AI at the moment-- the language models, the world models, and so on-- what's closest to your vision of AGI?

**34:45** · DEMIS HASSABIS: I think, actually the combination of-- obviously, there's Gemini 3, which I think is very capable, but the Nano Banana Pro system we also launched last week, which is an advanced version of our image creation tool.

**34:58** · What's really amazing about that-- it has also Gemini under the hood, so it can understand not just images.

**35:03** · It sort of understands what's going on semantically in those images.

**35:08** · And people have been only playing with it for a week now, but I've seen so much cool stuff on social media about what people are using it for.

**35:16** · So, for example, you can give it a picture of a complex plane or something like that, and it can label all the diagrams of all the different parts of the plane and even visualize it with all the different parts sort of exposed.

**35:32** · So it has some deep understanding of mechanics and what makes up parts of objects, what's materials.

**35:42** · And it can render text really accurately now.

**35:46** · So I think that's-- it's getting towards a kind of AGI for imaging.

**35:51** · I think it's a kind of general-purpose system that can do anything across images.

**35:56** · So I think that's very exciting.

**35:58** · And then the advances in world models-- Genie and SIMA and what we're doing there.

**36:03** · And then, eventually, we've got to converge all of those different-- they're different projects at the moment.

**36:09** · And they're intertwined, but we need to converge them all into one big model.

**36:14** · And then that might start becoming a candidate for proto-AGI.

**36:18** · HANNAH FRY: I know you've been reading quite a lot about the Industrial Revolution recently.

**36:22** · DEMIS HASSABIS: Yes.

**36:23** · HANNAH FRY: Are there things that we can learn from what happened there to try and mitigate against some of the disruption that we can expect as AGI comes?

**36:31** · DEMIS HASSABIS: I think there's a lot we can learn.

**36:33** · It's something you study in school, at least in Britain, but in a very superficial level.

**36:38** · It was really interesting for me to look into how it all happened, what it started with, the economic reasons behind that, which is the textile industry.

**36:48** · And then the first computers were really the sewing machines.

**36:51** · And then they became punch cards for the early Fortran computers, mainframes.

**36:55** · And for a while, it was very successful.

**36:57** · And Britain became the center of the textile world because they could make these amazingly high-quality things for very cheap because of the automated systems.

**37:06** · And then, obviously, the steam engines and all of those things came in.

**37:10** · I think there's a lot of incredible advances that came out of the Industrial Revolution.

**37:14** · So child mortality went down, and all modern medicine and sanitary conditions, the work-life split and how that all worked was worked out during the Industrial Revolution.

**37:28** · But it also came with a lot of challenges, like it took quite a long time, roughly a century.

**37:34** · And different parts of the labor force were dislocated at certain times, and then new things had to be created.

**37:43** · New organizations like unions and other things had to be created in order to rebalance that.

**37:48** · So it was fascinating to see the whole of society had to, over time, adapt.

**37:53** · And then you've got the modern world now.

**37:55** · So I think there were lots of, obviously, pros and cons of the Industrial Revolution, why it was happening, but no one would want-- if you think about what it's done in total, like abundance of food in the Western world and modern medicine and all these things, modern transport, that was all because of the Industrial Revolution.

**38:14** · So we wouldn't want to go back to pre-Industrial Revolution, but maybe we can figure out ahead of time, by learning from it, what those dislocations were and maybe mitigate those earlier or more effectively this time.

**38:26** · And we're probably going to have to because the difference this time is that it's probably going to be 10 times bigger than the Industrial Revolution, and it will probably happen 10 times faster, so more like a decade, unfold over a decade, than a century.

**38:38** · HANNAH FRY: One of the things that Shane told us was that the current economic system where you exchange your labor for resources, effectively, it just won't function the same way in a post-AGI society.

**38:51** · Do you have a vision of how society should be reconfigured or might be reconfigured in a way that works?

**38:57** · DEMIS HASSABIS: Yeah.

**38:57** · I'm spending more time thinking about this now, and Shane's actually leading an effort here on that to think about what a post-AGI world might look like and what we need to prepare for.

**39:05** · But I think society, in general, needs to spend more time thinking about that-- economists and social scientists and governments-- because as with the Industrial Revolution, the whole working world and working week and everything got changed from pre-Industrial Revolution, more like agriculture.

**39:22** · And I think at least that level of change is going to happen again.

**39:26** · So it's not surprising-- I don't would not be surprised if we needed new economic systems, new economic models, to basically help with that transformation and make sure, for example, the benefits are widely distributed, and maybe things like universal basic income and things like that are part of the solution.

**39:46** · But I don't think that's the complete-- I think that's just what we can model out now because that would be almost an add-on to what we have today.

**39:55** · But I think there might be something-- way better systems, more like direct democracy-type systems, where you can vote with a certain amount of credits or something for what you want to see.

**40:07** · It happens, actually, on local community level.

**40:10** · Here's a bunch of money.

**40:11** · Do you want a playground or a tennis court or an extra classroom on the school?

**40:16** · And then you let the community vote for it.

**40:20** · And then maybe you could even measure the outcomes.

**40:23** · And then the people that consistently vote for things that end up being more well-received, they have proportionally more influence for the next vote.

**40:33** · So there's a lot of interesting things I hear economist friends of mine who are brainstorming this.

**40:39** · And I think that would be great if we had a lot more work on that.

**40:43** · And then there's the philosophical side of it of, OK, so jobs will change and other things like that, but maybe fusion will have been solved.

**40:53** · And so we have this abundant, free energy, so we're post-scarcity.

**40:57** · So what happens to money?

**40:59** · Maybe everyone's better off.

**41:01** · But then what happens to purpose?

**41:02** · Because a lot of people get their purpose from their jobs and then providing for their families, which is a very noble purpose.

**41:10** · So there's a lot of-- I think some of these questions blend from economic questions into almost philosophical questions.

**41:17** · HANNAH FRY: Do you worry that people don't seem to be paying attention or moving as quickly as you'd like to see?

**41:23** · DEMIS HASSABIS: Yeah, I am-- HANNAH FRY: What would it take for people to recognize that we need international collaboration on this?

**41:27** · DEMIS HASSABIS: I am worried about that.

**41:30** · And, again, in an ideal world, there would have been a lot more collaboration already and international, specifically, and a lot more research and, I guess, exploration and discussion going on about these topics.

**41:43** · I'm actually pretty surprised there isn't more of that being discussed, given even our timelines, which there were there some very short timelines out there, but even ours are five to 10 years, which is not long for institutions or things like that to be built to handle this.

**42:00** · And one of the worries I have is that the institutions that do exist, they seem to be very fragmented and not very influential to the level that you would need.

**42:09** · So it may be that there aren't the right institutions to deal with this currently.

**42:15** · And then, of course, if you add in the geopolitical tensions that are going on at the moment around the world, it seems like collaboration and cooperation is harder than ever.

**42:22** · Just look at climate change and how hard it is to get any agreement on anything to do with that.

**42:30** · So we'll see.

**42:32** · I think, as the stakes get higher, and as these systems get more powerful-- and maybe this is one of the benefits of them being in products, is the everyday person that's not working on this technology will get to feel the increase in the power of these things and the capability.

**42:49** · And so that will then reach government, and then maybe they'll see sense as we get closer to AGI.

**42:56** · HANNAH FRY: Do you think it will take a moment, an incident, for everyone to sit up and pay attention?

**43:01** · DEMIS HASSABIS: I don't know.

**43:02** · I mean, I hope not.

**43:03** · Most of the main labs are pretty responsible.

**43:05** · We try to be as responsible as possible.

**43:08** · That's always something we've-- as you know, if you followed us over the years, that's been at the heart of everything we do.

**43:14** · Doesn't mean we'll get everything right, but we try to be as thoughtful and as scientific in our approach as possible.

**43:20** · I think most of the major labs are trying to be responsible.

**43:24** · Also, there's good commercial pressure, actually, to be responsible.

**43:27** · If you think about agents, and you're renting an agent to another company, let's say, to do something, that other company is going to want to know what the limits are and the boundaries are and the guardrails are on those agents, in terms of what they might do and not just mess up the data and all of this stuff.

**43:44** · So I think that's good because the more kind of cowboy operations, they won't get the business because enterprises won't choose them.

**43:53** · So I think the capitalist system will actually be useful here to reinforce responsible behavior, which is good.

**44:00** · But then there will be rogue actors, maybe rogue nations, maybe rogue organizations, maybe people building on top of open source.

**44:09** · I don't know.

**44:09** · Obviously, it's very difficult to stop that.

**44:11** · Then something may go wrong.

**44:15** · And hopefully it's just medium sized, and then that will be a warning shot to humanity across the bow.

**44:23** · And then that might be the moment to advocate for international standards or international cooperation or collaboration, at least on some high-level, basic-- kind of, what's the basic standards we would want and agree to?

**44:40** · I'm hopeful that that will be possible.

**44:42** · HANNAH FRY: In the long term, so beyond AGI and towards ASI, Artificial Superintelligence, do you think that there are some things that humans can do that machines will never be able to manage?

### Turing machines

**44:53** · DEMIS HASSABIS: Well, I think that's the big question.

**44:55** · And I feel like this is related to-- as you know, one of my favorite topics is Turing machines.

**45:00** · I've always felt this, that if we build AGI, and then use that as a simulation of the mind, and then compare that to the real mind, we will then see what the differences are and potentially what's special and remaining about the human mind.

**45:16** · Maybe that's creativity.

**45:17** · Maybe it's emotions.

**45:18** · Maybe it's dreaming, consciousness.

**45:21** · There's a lot of hypotheses out there about what may or may not be computable.

**45:26** · And this comes back to the Turing machine question of, what is the limit of a Turing machine?

**45:31** · And I think that's the central question in my life, really, ever since I found out about Turing and Turing machines.

**45:36** · And I fell in love with that.

**45:41** · That's my core passion.

**45:42** · And I think everything we've been doing is pushing the notion of what a Turing machine can do to the limit, including folding proteins.

**45:52** · And so it turns out, I'm not sure what the limit is.

**45:56** · Maybe there isn't one.

**45:57** · And, of course, my quantum computing friends would say there are limits, and you need quantum computers to do quantum systems.

**46:05** · But I'm really not so sure.

**46:06** · And I've actually discussed that with some of the quantum folks.

**46:11** · And it may be that we need data from these quantum systems in order to create a classical simulation.

**46:17** · And then that comes back to the mind, which is, is it all classical computation, or is there something else going on, like Roger Penrose believes there's quantum effects in the brain?

**46:27** · If there are, and that's what consciousness is to do with, then machines will never have that, at least the classical machines.

**46:34** · We'll have to wait for quantum computers.

**46:36** · But if there isn't, then there may not be any limit.

**46:40** · Maybe in the universe, everything is computationally tractable if you look at it in the right way, and therefore, Turing machines might be able to model everything in the universe.

**46:49** · I'm currently-- if you were to make me guess, I would guess that.

**46:53** · And I'm working on that basis until physics shows me otherwise.

**46:57** · HANNAH FRY: So there's nothing that cannot be done within these computational \[INAUDIBLE\]?

**47:01** · DEMIS HASSABIS: Well, no one's-- put it this way.

**47:02** · Nobody's found anything in the universe that's non-computable, so far.

**47:07** · HANNAH FRY: So far.

**47:08** · DEMIS HASSABIS: And I think we've already shown you can go way beyond the usual complexity theorist P equals NP view of what a classical computer could do today, things like protein folding and Go and so on.

**47:21** · So I don't think anyone knows what that limit is.

**47:23** · And, really, if you boil down to what are we doing at DeepMind and Google and what I'm trying to do is find that limit.

**47:30** · HANNAH FRY: But then in the limit of that, though, is that-- in the limit of that idea is that we're sitting here.

**47:35** · There's the warmth of the lights on our face.

**47:38** · We hear the whir of the machine in the background.

**47:40** · There's the feel of the desk under our hands.

**47:42** · All of that could be replicable by a classical computer?

**47:47** · DEMIS HASSABIS: Yes.

**47:47** · Well, I think, in the end, my view-- and this is why I love Kant, as well, all of my two favorite philosophers, Kant and Spinoza, for different reasons.

**47:55** · But Kant, the reality is the construct of the mind.

**47:59** · I think that's true.

**48:00** · And so, yes, all of those things you mentioned, they're coming into our sensory apparatus, and they feel different-- the warmth of the light, the touch of the table.

**48:09** · But in the end, it's all information, and we're information-processing systems.

**48:13** · And I think that's what biology is.

**48:15** · This is what we're trying to do with isomorphic.

**48:17** · That's how I think we'll end up curing all diseases is by thinking about biology as an information-processing system.

**48:24** · And I think, in the end, that's going to be-- and I'm working on, in my spare time, my two minutes of spare time, physics theories about things like information being the most fundamental unit, shall we say, of the universe-- not energy, not matter, but information.

**48:38** · And so it may be that these are all interchangeable in the end, but we just sense it.

**48:44** · We feel it in a different way.

**48:46** · But as far as we know, all these amazing sensors that we have, they're still computable by a Turing machine.

**48:53** · HANNAH FRY: But this is why your simulated world is so important.

**48:56** · DEMIS HASSABIS: Yes, exactly, because that would be one of the ways to get to it.

**49:00** · What's the limits of what we can simulate?

**49:01** · Because if you can simulate it, then, in some sense, you've understood it.

**49:05** · HANNAH FRY: I wanted to finish with some personal reflections of what it's like to be at the forefront of this.

### How it feels to lead

**49:12** · I mean, does the emotional weight of this ever sort of wear you down?

**49:16** · Does it ever feel quite isolating?

**49:18** · DEMIS HASSABIS: Yes.

**49:20** · Look, I don't sleep very much, partly because there's too much work, but also I have trouble sleeping.

**49:24** · It's very complex emotions to deal with because it's unbelievably exciting.

**49:30** · I'm basically doing everything I ever dreamed of, and we're at the absolute frontier of science in so many ways, applied science as well as machine learning.

**49:41** · And that's exhilarating, as all scientists know, that feeling of being at the frontier and discovering something for the first time.

**49:48** · And that's happening almost on a monthly basis for us, which is amazing.

**49:53** · But then, of course, we, Shane and I and others who've been doing this for a long time, we understand it better than anybody the enormity of what's coming.

**50:02** · And this thing about, it's still under actually appreciated.

**50:05** · In fact, what's going to happen in more of a 10-year timescale, including to things like the philosophical what it means to be human, what's important about that?

**50:15** · All of these questions are going to come up.

**50:18** · And so it's a big responsibility.

**50:23** · But we have an amazing team thinking about these things.

**50:26** · But, also, it's something I guess, at least for myself, I've trained for my whole life.

**50:31** · So ever since my early days playing chess and then working on computers and games and simulations and neuroscience, it's all been for this kind of moment.

**50:42** · And it's roughly what I imagined it was going to be.

**50:45** · So that's partly how I cope with it is just training.

**50:48** · HANNAH FRY: Are there parts of it that have hit you harder than you expected, though?

**50:52** · DEMIS HASSABIS: Yes, for sure.

**50:53** · On the way-- I mean, even the AlphaGo match, just seeing how we managed to crack Go.

**51:00** · But Go was this beautiful mystery, and it changed it.

**51:04** · And so that was interesting and bittersweet.

**51:07** · I think even the more recent things of language and then imaging, and what does it mean for creativity?

**51:14** · I have huge respect and passion for the creative arts, having done game design myself, and I talk to film directors.

**51:21** · And it's an interesting dual moment for them, too.

**51:24** · On the one hand, they've got these amazing tools that speed up prototyping ideas by 10X.

**51:30** · But on the other hand, is it replacing certain creative skills?

**51:35** · So I think there's these trade-offs going on all over the place, which I think is inevitable with a technology as powerful and as transformative as AI is, as, in the past, electricity was and internet.

**51:50** · And we've seen that that is the story of humanity is we are tool-making animals.

**51:57** · And that's what we love to do.

**51:58** · And for some reason, we also have a brain that can understand science and do science, which is amazing, but also insatiably curious.

**52:08** · I think that's the heart of what it means to be human.

**52:10** · And I think I've just had that bug from the beginning.

**52:14** · And my expression of trying to answer that is to build AI.

**52:18** · HANNAH FRY: When you and the other AI leaders are in a room together, is there a sort of sense of solidarity between you, that this is a group of people who all know the stakes, who all really understand the things?

**52:28** · Or does the competition keep you apart from one another?

**52:31** · DEMIS HASSABIS: Well, yeah, we all know each other.

**52:33** · I get on with pretty much all of them.

**52:35** · Some of the others don't get on with each other.

**52:37** · And it's hard because we're also in the most ferocious capitalist competition there's ever been, probably.

**52:45** · Investor friends of mine and VC friends of mine who were around in the dotcom era say this is 10X more ferocious and intense than that was.

**52:56** · In many ways, I love that.

**52:57** · I mean, I live for competition.

**53:00** · I've always loved that since my chess days.

**53:03** · But stepping back, I understand, and I hope everyone understands that there's a much bigger thing at stake than just company successes and that type of thing.

**53:13** · HANNAH FRY: When it comes to the next decade, when you think about it, are there big moments coming up that you're personally most apprehensive about?

**53:21** · DEMIS HASSABIS: I think, right now, the systems are-- I call them passive systems.

**53:25** · You put the energy in, as the user-- the question, or what's the task?

**53:30** · And then these systems provide you with some summary or some answer.

**53:35** · So very much it's human-directed and human energy going in and human ideas going in.

**53:41** · The next stage is agent-based systems, which I think we're going to start seeing-- we're seeing now, but they're pretty primitive.

**53:46** · In the next couple of years, I think we'll start seeing some really impressive, reliable ones.

**53:51** · And I think those will be incredibly useful and capable if you think about them as an assistant or something like that.

**53:57** · But also, they'll be more autonomous.

**53:59** · So I think the risks go up, as well, with those types of systems.

**54:04** · So I'm quite worried about what those sorts of systems will be able to do maybe in two, three years' time.

**54:12** · So we're working on cyber defense in preparation for a world like that, where maybe there's millions of agents roaming around on the internet.

**54:21** · HANNAH FRY: And what about what you're most looking forward to?

**54:24** · I mean, is there a day when you'll be able to retire, knowing that your work is done?

**54:30** · Or is there more than a lifetime's worth of work left to do?

**54:33** · DEMIS HASSABIS: Yeah.

**54:34** · I always-- well, I could definitely do with a sabbatical, and I would spend it doing science.

**54:39** · HANNAH FRY: Just a week off, Demis.

**54:40** · DEMIS HASSABIS: Yeah, so a week off, or even a day would be good.

**54:43** · But, look, I think my mission has always been to help the world steward AGI safely over the line for all of humanity.

**54:51** · So I think, when we get to that point, of course, then there's superintelligence, and there's post-AGI, and there's all the economic stuff we were discussing and societal stuff, and maybe I can help in some way there.

**55:02** · But I think that will be my core part of my mission, my life mission will be done.

**55:10** · I mean, only a small job.

**55:11** · Just get that over the line, or help the world get that over the line.

**55:14** · I think it's going to require collaboration, like we talked earlier.

**55:18** · And I'm quite a collaborative person, so I hope I can help with that from the position that I have.

**55:23** · HANNAH FRY: And then you get to have a holiday.

**55:25** · DEMIS HASSABIS: And then I'll have the-- yeah, exactly, a well-earned sabbatical.

**55:29** · HANNAH FRY: Yeah, absolutely.

**55:30** · Demis, thank you so much.

**55:31** · DEMIS HASSABIS: Thanks for having me.

**55:32** · HANNAH FRY: As delightful as always.

**55:34** · Well, that is it for this season of "Google DeepMind: The Podcast" with me, Professor Hannah Fry.

**55:38** · But be sure to subscribe so you will be among the first to hear about our return in 2026.

**55:43** · And in the meantime, why not revisit our vast episode library?

**55:47** · Because we have covered so much this year, from driverless cars to robotics, world models to drug discovery-- plenty to keep you occupied.

**55:56** · See you soon.

**55:57** · \[THEME MUSIC\]
