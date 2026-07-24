---
title: When millions of AI agents meet
source_url: https://www.youtube.com/watch?v=V04bm-3d6EQ
video_id: V04bm-3d6EQ
account: '[[accounts/google-deepmind|Google DeepMind]]'
account_name: Google DeepMind
account_url: https://www.youtube.com/@googledeepmind
featured_people: []
published: 2026-06-23
created: 2026-07-23
language: en
speaker_attribution: contextual
description: 'The conversation of the moment is focused on one topic: AI agents. Unlike traditional language models that simply respond to a prompt, autonomous agents can execute multi-step plans and perform comple'
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=V04bm-3d6EQ)

The conversation of the moment is focused on one topic: AI agents. Unlike traditional language models that simply respond to a prompt, autonomous agents can execute multi-step plans and perform complex tasks on your behalf. But what happens when millions of these agents are not just working for us, but transacting, negotiating, and delegating to one another?  
  
Nenad Tomašev, Senior Staff Research Scientist at Google DeepMind, joins host Hannah Fry to discuss the theoretical framework of a future"agentic economy." Together, they discuss the operational shift from single systems to a cooperative "society of specialists," the psychological risk of human automation bias, and the complex cybersecurity landscape—from dynamic cloaking to agentic traps—required to keep distributed intelligence secure.  
  
Timecodes:  
00:00 Intro  
1:07 Defining AI agents  
4:44 Agentic exploration in science and research  
15:46 Delegation between agents  
22:46 Agentic security and traps  
29:31 Building an agentic economy  
33:22 Cognitive monoculture  
36:29 Distributed intelligence  
  
To read the research, search for:  
Distributional AGI Safety, May 2026  
Intelligent AI Delegation, February 2026  
Virtual Agent Economies, September 2025  
  
Learn more about our AGI control roadmap: https://deepmind.google/blog/securing-the-future-of-ai-agents/  
  
\_\_\_  
  
Subscribe to our channel https://www.youtube.com/@googledeepmind  
Find us on X https://x.com/GoogleDeepMind  
Follow us on Instagram https://instagram.com/googledeepmind  
Add us on Linkedin https://www.linkedin.com/company/deepmind/

## Transcript

### Intro

**0:00** · Welcome back to Google DeepMind, the podcast.

**0:02** · Now, not very long ago, an AI assistant essentially meant a large language model.

**0:07** · You ask it a question.

**0:08** · It gave you an answer, but it couldn't go off and perform tasks on your behalf.

**0:13** · All of that is changing with the advent of AI agents.

**0:17** · While Google DeepMind has this long history of developing agents stretching back to reinforcement learning in games, for most of us they hadn't really arrived.

**0:28** · And then we saw open source tools like OpenClaw released into the wild.

**0:33** · And at Google, a new generation of agentic tools is here, including Gemini, Spark, and Antigravity.

**0:40** · But what happens when millions of AI agents are not just working for us, but transacting, negotiating, delegating to each other?

**0:48** · Do we end up with a new kind of economy, a new route to AGI?

**0:54** · And how on earth do we keep all of that safe?

**0:57** · Well, one of the people trying to answer these questions is Nenad Tomašev, senior staff research scientist at Google DeepMind.

**1:04** · Nenad, thank you so much for joining me.

**1:05** · Very happy to be here.

**1:06** · I think we should probably start at the beginning here, because for people who have only played around with large language models, could you describe to us the difference between that experience and and acting with an agent?

### Defining AI agents

**1:18** · Yeah, no, definitely.

**1:19** · I think this is becoming one of the main trends we're seeing this year.

**1:23** · And it's interesting because agents are not a new concept.

**1:25** · It's something that we've been looking at in the context of AI for a long time, even before large language models.

**1:31** · We had agents operating in simulated 3D environments, going on and collecting items, completing some tasks.

**1:38** · This was back in the days we were really prioritizing actioning in the world as a way of manifesting intelligence.

**1:44** · Now, similarly, nowadays, I guess you could say that the main conceptual difference between just a language model and an agent is that an agent observes a state of the world and performs an action, makes an action in the world, in the environment that it's given, whereas the language model just gives you a continuation, a reply to prompt, to query.

**2:05** · Now obviously agents that we use nowadays, they use large language models under the hood so the two concepts are not completely disambiguated.

**2:12** · It still is the large language models formulating the actions.

**2:16** · It's just that there is a harness around it made to enact the changes once they have been proposed.

**2:22** · But it has a lot more autonomy to to chain decisions together, I guess.

**2:26** · Correct. And I guess this is ultimately the motivation, right?

**2:29** · Because you could do everything, most things that an agent can do manually, painstakingly, by interacting with the language model very many times and you guiding the whole process, whereas an agent instantiates this harness that automates some of that away and gives you less work and gives the language model or, you know, the agent more autonomy to complete the tasks.

**2:53** · So if you want something done that takes multiple steps that the agent can make a plan and take actions on all of those steps, obviously requiring approval or human input for those actions that are, you know, let's say, more sensitive or more likely to go wrong.

**3:08** · How is it different, though?

**3:10** · I mean, if you're used to interacting with a large language model by now, what would it be like interacting with an agent?

**3:16** · In many ways similar.

**3:18** · Your interaction interface is somewhat similar.

**3:21** · You're still talking to the agent in a way in which you would be talking to a language model.

**3:25** · There is a language model there, but because the agent is doing more things for you, you're more in the position of a decision maker to review and approve.

**3:35** · And then once you've approved, the agent is going to do various things and purchase tickets.

**3:40** · Message your friends if you're organizing a party and meanwhile you can, put something on on Netflix, hopefully, and relax a little bit.

**3:48** · The example, I was thinking of was if you were, I don't know, planning a wedding, for instance, you'd go into a large language model and it would like tell you a list of caterers, give you a suggested list of venues, but actually you would have to do all the emailing yourself.

**4:00** · But but an agent, I mean, would be much more useful really in that kind of scenario.

**4:06** · 100%, especially because agents are given access to all of these tools so you could, you don't have to, you could give an agent access to your Gmail and give it permissions to send out an email.

**4:16** · Of course, there is a chance of it sending something wrong, so you need to verify what it has composed.

**4:22** · But in principle, by giving access to tools to agents, you just empower your large language model to do these things for you.

**4:30** · And then the whole job is done, the organization has happened without you having to lift a finger?

**4:34** · Ideally presuming no mistakes have been made.

**4:36** · Yes.

**4:37** · Yeah, ideally is quite an important point there.

**4:40** · So, okay, where we are right now, what tasks are agents actually good at?

### Agentic exploration in science and research

**4:44** · I think that where we are focusing a lot of our energy on them, we I don't mean we as Google we as the entire field is on coding capabilities of agents.

**4:53** · And this is just because so many formal processes and tasks can be formulated as software or as code.

**5:00** · In terms of where they're currently at in the real world speaking of coding, we see lots of coding tools get used.

**5:08** · We use them here internally.

**5:09** · People use them externally, and it's really accelerating the development of software, which is bringing the human, focus onto ideas and design rather than the painstaking implementation of boilerplate around them, which used to take a lot of time and a lot of skill and very bespoke knowledge.

**5:25** · And now that can just be done by the language models easily.

**5:28** · But then at the same time, we are still at a stage where you have to keep a human in the loop throughout this.

**5:33** · I mean, why, what can't these things do at the moment that means that it requires human oversight?

**5:39** · I wouldn't even make a distinction between whether they can or cannot.

**5:44** · It's more that every single thing that they can do, they don't do, with 100% accuracy.

**5:52** · So every action, like with humans, at the end of the day, has a certain failure rate.

**5:58** · And the more complex the action, the higher the expected failure rate.

**6:02** · Again, like with any form of intelligence, human one included.

**6:05** · So, while you know, you may expect that an agent will execute the tasks correctly, it may still make a mistake.

**6:14** · And this mistake may be obvious, or it may be very subtle, which is actually an important point, because there is this thing that has existed in other domains as well for a long time, where different machine learning models have been, deployed.

**6:30** · And that is automation bias, where in this context, if you're using an agent and it does well, it builds one thing well, the second thing well, eventually you switch off, you start trusting it too much.

**6:43** · Right.

**6:43** · And you fail to verify and you fail to find some important issue underneath.

**6:47** · Then mistakes slip through.

**6:48** · Exactly.

**6:49** · So for humans, it's important not only to be in the loop, because we are obviously designing these harnesses to keep humans in the loop, but to really be engaged and be switched on, because as soon as you switch off, you're rolling the dice.

**7:01** · So okay, in the long term then, I mean, it sort of sounds like we're in this transition period where these things are sort of becoming more capable.

**7:08** · But in the long term, I mean, how much of a difference do you think that this is going to make?

**7:12** · I mean, will this completely transform the way that we use artificial intelligence?

**7:17** · 100%.

**7:18** · I think it's impossible to envision a world where there isn't some kind of a deep disruption.

**7:22** · And what we're all trying to figure out is exactly what that is going to look like.

**7:27** · Obviously, we have agency in that we are building the technology.

**7:30** · We can design our solutions in a particular way, obviously, to empower human developers and human experts across different fields as much as possible.

**7:38** · But AI is definitely entering various fields where it just wasn't present before.

**7:43** · Scientists are using AI on a regular basis.

**7:46** · Up until very recently, you know, mathematicians couldn't envision AI doing something in mathematics.

**7:51** · Now it is becoming commonplace in a very short span of time.

**7:55** · Which is not to say that all of the problems have been solved.

**7:57** · Obviously, there is still a big role for humans, but it's a very rapid transition.

**8:02** · And that is the only unsettling part, I guess, because for most, even industrial revolutions and so on, we're used to taking some period of time, giving us more time to, change our approach and settle into it, as you say.

**8:17** · And it doesn't feel like the window of time is as long this time.

**8:21** · So we need to be very mindful of how we approach everything.

**8:24** · Why do we want these things?

**8:26** · I mean, why build them?

**8:27** · What what's the benefit?

**8:29** · What are they giving us that we don't currently have?

**8:31** · I mean, for all of us who have been working on AI for a long time, we've had some version of the answer to that question, I guess, internalized.

**8:39** · And for me personally, the answer is to advance science, improve health and human welfare.

**8:46** · Now these are very high level answers so, it's maybe not as obvious as to how they map on to the specifics of the question as to why build agents and have agents.

**8:55** · And there are people in the field that, say specifically that we shouldn't be granting these systems autonomy, right?

**9:04** · Which is what agents have but in my mind, if we can develop these harnesses and make them safe and have agents perform complex tasks autonomously, then we actually accelerate progress, because then more things can happen with, the same amount of human input.

**9:24** · Just draw the line for me to science here, because I guess the example that we've been talking about have been like, you know, building software, buying stuff for a wedding, and they all sort of feel quite trivial but just explain to me how this fits into the story of improving science.

**9:41** · So this is my, you know, main dream, main objective here.

**9:44** · When it comes to science, it's not merely about having some good ideas and reasoning about them for some short period of time, like in a context window of a model.

**9:55** · Lots of people are obviously using language models in science as coideators or to help with some formal derivations.

**10:03** · All of this is already useful and actually amazing that is possible.

**10:06** · But when it comes to automating science, to some larger extent, there are other threads that are currently progressing at some pace, like there are investments in the development of some autonomous research laboratories, for example.

**10:20** · And under those scenarios, you would want to see agents be able to schedule experiments to run.

**10:27** · Needless to say, lots of safeguards need to exist with such an interface with the real world is happening, whether we are talking about Material design or, biotech.

**10:37** · Because even with, let's say you're designing batteries, I mean, maybe you, come up with a setup that, overheats, leads to some sort of an experimental breakdown that would have that would damage the hardware, have some consequences.

**10:50** · So we need to have safeguards in place, and we need to have good, reliable protocols in place for these agents to close the loop.

**10:57** · Because in the software, closing the loop is, as mentioned, easy.

**11:00** · You write tests and you verify through tests and then you can proceed.

**11:04** · In science, you need to run physical experiments in most areas of science to give you this feedback, whether your idea was good or not, observe that, analyze that, and so on and so forth.

**11:16** · Because I guess this is the point, right?

**11:17** · If the algorithm, if the agent has autonomy to go and test out different mathematical problems, for instance, rather than just waiting to be prompted by a human, I mean, that does then raise the question of where is the role for the human in all of this?

**11:30** · Indeed, in the long run, we need to figure that out.

**11:33** · I would say that in the short term, with the technology that we have, there is still obviously a major role for humans and our systems that are not yet AGI.

**11:41** · There are many things we still can't do.

**11:43** · And I think for the current generation of systems, one thing that can be said with some confidence is that they tend to be good at how to put it best, let's say a kind of a combinatorial closure of what you already know how to do.

**11:56** · They are, at the end of the day, most are trained on human data.

**12:00** · Therefore, they can replicate the skills we have and repeat them and combine them in to find ways of bridging some smaller gaps but we have not yet seen these models be truly, deeply transformative.

**12:14** · Let's say in terms of science making a discovery that, you know, humans would have ever thought of, therefore, there is still plenty of role to play for all of us in this transformation.

**12:24** · You mentioned a moment ago, the people have been talking about agents for a really long time.

**12:28** · Why has it taken so long for them to come into fruition?

**12:31** · I mean, really is only very, very, very recently that people have actually been able to get their hands on them and play around with them.

**12:36** · Yeah, I would say, obviously some things that we would refer to as agents historically have been deployed, for example, in optimizing operations in data centers and so on and so forth.

**12:47** · They have obviously been very limited because they didn't, include language.

**12:52** · So there was no way for humans to interface with them to communicate.

**12:56** · It would be a very narrow agent trained on a specific task, and it would be good at doing that task.

**13:03** · But because there is no interactivity, there is nothing for us to do is just software in a classical sense.

**13:09** · Maybe you can call some of the trading algorithms, and investment algorithms also agents in that context, but they just operate on their own.

**13:18** · The difference now is because these agents are based on language models, is we can talk to them, we can learn from them, we can influence them, we can steer them.

**13:26** · And this is why all of us as people are interacting with agents much more.

**13:31** · But then why are we still waiting?

**13:33** · I mean, this sort of vision that you're describing of like an, an assistant that can just go off and do everything for me, it's still not here.

**13:39** · What's stopping it being deployed more, more broadly?

**13:42** · We need to take a step away from just designing the underlying model.

**13:46** · A lot of energy has gone into that, and there are still improvements needing to be made.

**13:51** · But now that we have capable agents, capable models, we need to find better ways of coordinating them, orchestrating them, managing them.

**13:59** · Once you have these admittedly quite powerful systems, it can do many things for us, we need to see ourselves as managers of teams and institutions in some way, and to develop personal management skills to handle these workflows.

**14:14** · Managing a team of agents is different compared to managing a team of humans, but there are obviously commonalities, right?

**14:20** · Different in the sense that agents will make very non-human mistakes.

**14:24** · They're not a human intelligence.

**14:26** · But at the same time, an agent doesn't know you that deeply to be able to just go on and, accurately guess everything you'd want it to do, we still need to be involved.

**14:35** · And therefore we need to get better at orchestration i think Thing is, we're still in a world where large language models occasionally hallucinate.

**14:45** · So it is in some ways quite a big leap for humans to then trust agents to carry out tasks on their behalf when any hallucination might actually result in something catastrophic happening.

**14:59** · Trust is given but it's also earned. I think this is maybe an important distinction.

**15:04** · So in our frameworks, we mentioned the need for establishing let's say, tracking of reputation over time, where if an agent is repeatedly unreliable, it should obviously not be trusted, even if it's most reliable, we shouldn't be blindly trusted.

**15:23** · We should still verify its actions.

**15:26** · But language models will always hallucinate to some extent, so we just need to integrate them in our workflows in a way which recognizes that, and where we make sure that those hallucinations, and they are becoming more and more rare and hopefully we'll, continue to do so don't compromise the workflows that are being undertaken.

### Delegation between agents

**15:46** · I know one of the things you've written a lot about is, is the idea of delegation that you might, have a particular task and an agent might then go on to delegate it to a specialist just to explain to me how that how that might work.

**15:57** · So this is the idea that one of the bottlenecks, one that we haven't mentioned yet, is that where we would really like to get help from agents are very complex tasks.

**16:08** · So what language models and simple agents that many of us have access to can easily do is if you give a very direct instruction, you know, go book something for me, I want to eat at this restaurant tomorrow, find a slot into the booking and the agent can maybe do this via tools.

**16:25** · If, however, you have a very complex plan that needs to be broken down into pieces executed separately, you may be in a situation where even no individual agent can do each and every piece, so maybe an agent may need to over this established agent to agent protocol that exists hand off a part of that work to another agent.

**16:47** · But then there can be failures along the way.

**16:50** · So an agent, the delegates or human the delegates needs to manage and handle those failures and also preempt them as much as possible.

**16:58** · Preempting them may involve, figuring out which agents are first and foremost reliable to even delegate to in the first place.

**17:06** · What are their capabilities?

**17:08** · Is that something that we can certify?

**17:10** · And also to safeguard the users and the agents from any kind of a malicious, interaction.

**17:16** · You mentioned I think was it a wedding or a party or something at first as an example, right?

**17:21** · So when managing a big event some of the bookings fall through, some accidents happen, some things don't arrive on time.

**17:29** · So whenever you have a big coordination challenge, there are lots of things that go wrong and in the process of managing that as a human, you need to deal with all of those delays and problems.

**17:40** · And similarly, an agent, the delegates to a group of agents needs to manage all of the problems that may arise.

**17:46** · So one thing that's currently the case in many of the multi-agent systems that we see is the they act more as parallelization than delegation, where you may have many agents working on things, but rather than there being an intelligent framework around how the work is split up, it has to just be chunked into sort of random sub parts that are handed off.

**18:11** · They go down in parallel, so you get to speed up, presuming that all of this is reliable and each agent can complete its task independently.

**18:20** · But this is not the intelligent delegation framework that we talk about.

**18:23** · So, if the tasks are split up in a sort of a essentially random way, you could have one agent that is buying the wine and another one that is buying glasses; doesn't realize that it's wine glasses that are required, there’s sort of no communication between them is not the kind of potential problem that could arise?

**18:39** · Potentially, but you're also, I guess, hitting on another point, which is that many of the uses we see are uses in, again, software engineering, for example with agents at the moment.

**18:50** · And that is a part of the reason, because in software, when you're building software, you can write tests, unit tests, as we say, right?

**18:56** · And run them and verify that the code has been written, at least in isolation performs the function.

**19:04** · But when it comes to many of these real world tasks, verification is not necessarily as straightforward.

**19:08** · Maybe there is a subjective element involved.

**19:11** · How do you define nice tasting wine, for instance?

**19:15** · A bit of a subjectivity in that.

**19:17** · But this is actually quite important when it comes to AI and language models, because there is a notion of reward hacking, that has existed in the, in various contexts in the field for a while.

**19:26** · So there could be situations where it does something that meets the requests but isn't in the spirit of the request, technically.

**19:33** · And for that reason, you know, you really want to emphasize verifiability and to be very formal about the contract that's made between the delegator and the delegatee in that setup.

**19:44** · At the same time, for tasks, we need to recognize that some are completely reversible.

**19:49** · So if something goes wrong, there is no harm.

**19:51** · You just rerun the task, retry re-delegate.

**19:54** · Some may have consequences in the real world, whether it's spending your money to buy something or taking some other action that you can't easily revoke after the fact.

**20:04** · So for those tasks you want to, you want to put more care in what you do there.

**20:09** · We've also seen with some of the early agents that are out there, agents delegating tasks to humans.

**20:16** · Right?

**20:18** · Just talk me through some of that.

**20:19** · I mean, that's an interesting, let's say, reversal of the more usual vision that we all have.

**20:25** · So humans delegating tasks to AI, you know, that's Standard.

**20:29** · Yes. Standard.

**20:31** · But this other direction has been explored across a number of studies.

**20:35** · I say in my background, you know, for context, is that I've done lots of prior work in and around medical AI.

**20:42** · In medicine.

**20:43** · We've had narrow systems that were at basically superhuman performance for very specific things that they had been trained to do in medical imaging, in radiology, this had to do with, a machine learning model, seeing a scan, identifying where there is a pathology, putting a box around it and handing that off to the human radiologist to review.

**21:06** · And these systems have been operating at a very high level, for quite a number of years.

**21:11** · They still have some failures, though, so they need to be reviewed by human experts.

**21:15** · So people have experimented with AI, human teams there, where the idea is that a human would, correct a mistake made by a system.

**21:24** · And people have trialed with this, flowing in both direction.

**21:29** · Either having a human expert only consult on the AI when the human expertise would say uncertain, or a human expert look at AI's suggestions all the time.

**21:41** · Or maybe having an AI system do its thing, make the predictions, and then a flag when something is uncertain, when maybe there's something blurry, fuzzy in the image that can be interpreted in many ways and the machine learning system isn't sure which of those is correct.

**21:56** · But this human review of decisions made by these, potentially superhuman, narrow machine learning models has proven to be quite a good setup.

**22:06** · So that AI would defer to a human in case of need, in case of uncertainty.

**22:12** · That is interesting, though, that I mean, granted, in those very specific scenarios where the AI is superhuman in its abilities, that the best team that you can get is where essentially the AI delegates to the human when it's unsure.

**22:27** · That is fascinating in and of itself and, you know, maybe there use cases where it's the converse.

**22:32** · Now for these more general systems.

**22:35** · Again, if an AI can recognize when it needs approvals and permissions for sensitive actions, then it does make sense to delegate those decisions to humans at the very least, right?

**22:45** · Just looking at the other side of this, I also want to think about the sort of cyber security element of this, because as more and more agents are out there interacting in the world on the internet and so on, there are inevitably going to be people who are trying to exploit the vulnerabilities of agents.

### Agentic security and traps

**23:01** · Tell me a little bit about, agentic traps that people are laying.

**23:04** · This is a scary and a fascinating topic at the same time I would say, and I think it's one of the main reasons why these kinds of deployments at scale cannot work. Right?

**23:15** · Because as we said, if there is not complete reliability of individual interactions, any system of scale that has many interactions is naturally going to statistically fail.

**23:27** · And because these systems take a lot of compute and therefore energy and money to run, if they're not reliable, it's just a nonstarter and agentic traps are something that we have been thinking about for quite a while now.

**23:42** · They can manifest in different ways are many types of traps, but it boils down to agents operate within an environment.

**23:49** · And in this context, the environment is the web.

**23:54** · If the environment itself is poisoned, if the traps are laid, agents may stumble upon them when interacting with the web and then, yes, malicious people or malicious agents deployed by malicious people can place those traps and then, compromise systems really.

**24:11** · So I don't know, the wine buying agent for the wedding goes on to a particular wine merchant where there is some essentially a prompt injector in the website that changes the agent's goals.

**24:26** · Is that the sort of thing that we're talking about here?

**24:27** · That is one way this could happen, yes.

**24:30** · And, the reason why that may potentially go unnoticed is, you know, in terms of how web pages are encoded, there are elements there that are just not rendered visually.

**24:40** · So if we're talking about an agent that isn't a visual computer user agent, that sees the web page, I mean, the pixels the same way the human does rather consumes the actual format of the page in raw format.

**24:54** · Then it could inadvertently consume those hidden tokens that can make it do different things than what the intention was.

**25:02** · Right?

**25:03** · But this is not the only way it may happen, because what malicious websites could potentially do, they could do what we refer to as dynamic cloaking as well, where they display pages differently for humans and agents, because you can, based on the behavior on a page, make a very good guess as to whether it is a human or it is an agent interacting with the page, and then only if an agent is interacting with the page with a specific intent do tweak the content in such a way so as to induce some kind of jailbreaking.

**25:33** · But just kind of going a little bit further on this, you could have agentic traps out there that I don't know, are designed to sort of take money from you to, do all kinds of things.

**25:44** · Yes and this has happened to people, who have experimented with agents and have given them access to wallets, right, to do things.

**25:52** · As I say, in the early days of this whole when we are especially experimenting internally or anyone else is, this is done in a trusted environment.

**26:00** · So you don't necessarily, in your early prototyping, have to deal with any of this.

**26:05** · It's not in the wild.

**26:06** · Yes, but once you deploy on the web, especially now with, AI really being using all sorts of places, the more agents there are, the more incentives there are for malicious people to do malicious things because they have a higher surface area to target.

**26:22** · And I think we're at the point where even the most of the web is currently being generated by agents and consumed by agents, that the agentic use of the web is exceeding that of humans, which is maybe happening for the first time.

**26:37** · Okay, two things.

**26:38** · First of all, it sort of sounds like you're describing that we're entering into this phase with there's like two different forms of the web, the sort of human version and the, a genetic version with dynamic cloaking and so on, a sort of a version of the web where adverts don't mean anything anymore, you know, it's not sort of human eyeballs that you can possibly sell to.

**26:57** · But I think that the second point about this is how on earth do you mitigate against it? If you don't have control over the environment, which you don't over the web, how on earth do you protect your agent from going rogue?

**27:10** · In some sense, it's not a new problem, right?

**27:12** · Because the security of the web has in other ways been an issue before and computer viruses could spread if you opened the wrong attachment in your inbox, right?

**27:23** · Or you click on something on an untrusted page, so it's not the first time we're experiencing the need to certify resources we're interacting with.

**27:32** · When it comes to machine learning systems, let's say adversarial examples have existed for a long time where imperceptible changes in images, imperceptible to humans, can jailbreak models.

**27:44** · Here you can do the same, whether it's a few pixels here and there, or you modify the least significant bit of the encoding in a number of places, so you can adjust things ever so slightly in a way in which a human may not be able to spot and still have some kind of a negative impact on an agent.

**28:00** · It sounds a bit like you're saying that when it comes to building guardrails, thinking about safety, you have to think about it external to the agent itself rather than just just what you are specifically building.

**28:15** · I think the the lesson is, you need to think about both.

**28:18** · One notion that we talk about in some of our other work, which is I guess, relevant here as well, is the notion of defense through depth, which is not a new idea again, by any means.

**28:29** · And this is just a recognition that because the problem is so hard, there is not going to be one solution to resolve all of the issues.

**28:38** · Rather, we need to be building, mitigations upon mitigations upon mitigations and when layering them, hopefully the the net is tight enough that very few things will slip through.

**28:50** · So in the context of this, yes, you may want to certify and and test, the content of web pages, have very good notions of trust for resources you're interacting with.

**29:03** · Also have some mitigations on the agent side, have mitigations and model side when it comes to foundation models run underneath, have meaningful human controls to be able to step in if something happens, be very mindful of permissions granted to the agents so that even if it gets jailbroken when interacting with something, the damage is minimal and all of those things combined together should then hopefully lead to some sort of safety that we are comfortable with.

**29:30** · Just going back to what you, what we were talking about earlier, this idea of there being multiple agents that are interacting with each other.

### Building an agentic economy

**29:37** · Just tell me a little bit more about this idea that you have of a formal agentic economy.

**29:42** · Just explain to me how that might work.

**29:45** · Right, so in the context of us, let's say normal users of the technology, on a day to day basis, you may have a personal assistant that has some persistent memory of you, has a good understanding of your desires, preferences, and it depends, again, depending on how much agency you want to grant this assistant, it may go on and negotiate some things for you.

**30:06** · You may granted some budget for that, and there can be a kind of a localized economy of these assistants negotiating stuff.

**30:14** · I think I want to get a sense of how this might actually work if you have, you know, lots of people who are using agents as their own personal assistant.

**30:21** · So, okay, let's say that there's a concert, there's like a Taylor Swift concert, a live event and tickets have just gone on sale.

**30:28** · How would that actually work?

**30:32** · If you have all of these agents rushing the site all at once.

**30:35** · I haven't been purchasing highly contested tickets very recently.

**30:38** · But in principle Not a Taylor Swift fan?

**30:41** · No, my music taste, it’s very different direction, I'm afraid.

**30:45** · What kind of music do you listen to?

**30:46** · Well, obscure subgenres of metal probably, so, maybe not, you know.

**30:51** · Okay, there is an obscure subgenre of metal, who are holding a concert, and there is an auction being held between the various agents.

**30:59** · How do you decide what wins the auction?

**31:01** · Is it just whoever can pay the most?

**31:04** · This is a design choice, and that's also an important point to make, that if we are to ever do something like that, then we are in control in terms of how we are making the system fair.

**31:16** · It's an explicit decision made by someone who is setting up the auction, because if you want to make things completely, fair in the sense that everyone gets equal access to some good concert tickets in this case, then you can give each and every agent participating in these repeated auctions, because we're not talking about one ticket on one auction in particular, but maybe for all the ticket purchases.

**31:42** · The same budget and then the agent's knowing your both overall preferences, your desire to go see a certain artist, also your travel schedule, time availability, other constraints can decide to allocate that budget in the best way possible, whatever that means, the way that reflects what you want the best so that they are more likely than not to win tickets, in the way which works for you.

**32:09** · And then in aggregate, when you distributed across all people, you would hope to get a sort of a fair outcome.

**32:15** · At the population scale.

**32:18** · I mean, I guess there are ballot systems, point systems, various types of ways around this that people in human based systems have come up with in the past.

**32:27** · Just sort of stepping up from the trivial example of concert tickets, although not trivial for some, as I understand.

**32:34** · I'm thinking here about some of the disruption that, for example, high frequency trading algorithms have made in the stock market.

**32:42** · But agents too could end up having a really catastrophic impact on the stock market if deployed in a particular way.

**32:49** · How do you prevent something like a flash crash from happening?

**32:52** · Obviously, there is a high risk as you say.

**32:55** · But financial markets have dealt with this risk for a while.

**32:58** · They've obviously had their fair share of, early bad experiences where things have gone wrong.

**33:04** · But I think we can just learn about mitigations from the economies that have dealt with that already.

**33:11** · So there is no need to reinvent the wheel.

**33:13** · Admittedly, some things are slightly different in the agentic case.

**33:18** · One particular thing that's different when you're talking about AI agents at the moment is that there is a handful of highly represented language models used in agents.

### Cognitive monoculture

**33:29** · If you look at the overall views of Claude, ChatGPT, Gemini, etc, they're all obviously open source models.

**33:35** · Many other models.

**33:38** · Is that they tend to have similar opinions.

**33:42** · They take actions in similar ways.

**33:45** · And this is what we often refer to as cognitive monoculture.

**33:49** · So when you deploy suddenly hundreds of thousands, millions of artificial decision makers and they tend to make similar decisions, then failure points become correlated because the decisions are correlated.

**34:02** · So one of the things that we need to be thinking about is how to diversify the decisions within our agents.

**34:11** · Obviously, you can do this as a user, as a power user of a system, because you can make a very intricate system prompt, it grants your agent some kind of a personality that biases it towards or against certain types of decisions.

**34:26** · So you can do that, but most people don't do that with their agents, with their models at the moment.

**34:34** · Groupthink, essentially, agentic groupthink.

**34:36** · Groupthink and also collusion.

**34:38** · You were talking about auctions before.

**34:40** · And in human auctions, this notion obviously exists as well, where bits can be coordinated by groups to, gain some kind of an advantage of a system.

**34:51** · And with agents, this is different in the sense that they may also coordinated through the environment in ways which are not obvious, so they can potentially coordinate without communicating directly.

**35:03** · So we need to be thinking about anti-collusion measures as well.

**35:06** · Once you're detailing all of these you know potential concerns of safety really of the way that these agents might end up acting once out there in the world it does make a lot more sense as to why you guys have been slightly cautious about releasing them carefully and slowly, right?

**35:23** · Yeah, that is true.

**35:24** · I mean, this is the this has been the story of every major technological disruption.

**35:28** · I think if you take self-driving cars as an example, this is admittedly a very different piece of technology, but we have also been very excited about them for a very long time.

**35:37** · Seen demos of these vehicles drive themselves.

**35:41** · Getting them to the streets safely still took many more years and a lot more time, because that last mile is where most of the work tends to be.

**35:51** · And I think when it comes to orchestrating and coordinating agents, at least because, we want them to be doing human like tasks.

**35:59** · But we also need is not just technical solutions.

**36:03** · A lot of this has to do also with policy and, just a broader societal understanding of how to integrate these systems.

**36:11** · At the end of the day, unless we have these fully autonomous agentic economies, which are maybe going to happen in the future but are not happening right now.

**36:19** · We need to have humans in the loop in these systems.

**36:23** · Therefore, we are integrating AI into human structures, and the two need to mesh well together.

### Distributed intelligence

**36:29** · I guess there is a flip side to all of this, because human societies when they come together can actually achieve really remarkable things collectively, so, presumably the same can be true for agentic societies?

**36:40** · One would hope.

**36:41** · I mean, this is the, the idea behind why would everyone want to use multi-agent systems.

**36:47** · I was talking about parallelization at the start of the conversation, right?

**36:50** · Where if all of the agents are equally competent and, they're doing similar things, then whether you think sequentially or in parallel with many agents, just gives you a little bit of velocity.

**37:02** · But if we have agents that can do different things in different ways, then this is where things become really interesting.

**37:09** · And actually, this is one thing we've not really brought up, because we've been talking with these generalist agents that are part of the idea of an agentic economy is the existence of specialists, not just the existence of generalists.

**37:21** · Now, we are obviously all trying to build agents that are as general and capable as possible.

**37:27** · And there is a G in AGI, there is artificial general intelligence that we're trying to achieve.

**37:32** · But in an economic sense, and this is my, you know, personal view.

**37:37** · This is not the point of convergence.

**37:39** · This is not what we're going to arrive at.

**37:40** · Because, look, I play chess unhealthily.

**37:44** · Too much, a bit of a chess addict.

**37:46** · And I've done work on AI for chess here, which is why I bring it up.

**37:49** · But let's take that as a very non-controversial example.

**37:53** · It's a game we all love.

**37:54** · Gemini can play some chess, so can other models.

**37:57** · Actually, they were not able to for a very long time, so there has been some progress towards that.

**38:02** · But you're still always going to use a chess engine instead.

**38:05** · It's much faster, much more accurate, far cheaper because they're trying to do just one thing and one thing very well, which can be done with fewer parameters.

**38:14** · The model is also entirely focused on that one thing that we're doing. And going back to humans, we are kind of like that as well.

**38:21** · Because I think one mistake we sometimes make when we talk about AGI is that we see it not as human level intelligence, even though this is what it's supposed to be in spirit.

**38:31** · We see it more as humanity level intelligence, where anything that any human may plausibly be able to do, but there is no single human that is capable of doing so many things at once.

**38:42** · There are many things I don't know how to do.

**38:44** · For some of them, I would wish I knew how to do them, like playing some instruments for doing some such thing, but brains have a limited capacity and we have limited time.

**38:53** · So at the end of the day, rather than having one humongous model that's very expensive and very slow, maybe we have instead a society of specialists, each of which can in principle be generally scaled up, if a bit larger, etc.

**39:08** · I mean, I'm not talking about breakthroughs in architecture, it's more just how we split things up.

**39:13** · And then those specialists are certified for those specific skills and cheaper to run.

**39:19** · And because they're cheaper to run and more reliable, there is no economic incentive not to do that.

**39:24** · So there is a future in which there is some, maybe more generic general layer that's like a connective tissue of this economy that knows everything and orchestrates everything.

**39:37** · And then for very specific tasks, you call, other models.

**39:42** · I mean I guess what you’re describing is like a distributed intelligence rather than an AGI, yeah, which is what humans have as you describe If that does end up being the sort of the version of AGI that we end up with, I'm sort of using inverted commas here.

**39:57** · Will that have to change how we think about safety in alignment if it is distributed across a number of different agents?

**40:05** · 100% I mean, you're no longer than aligning a single entity or maybe, yes, a single entity if you see the distributed entity as the entity.

**40:14** · But our alignment approaches as they exist at the moment have to do with taking one model, observing its behavior and trying to align that behavior with what we see is permissible or preferable or desirable.

**40:29** · Right?

**40:30** · But then when you have maybe 10,000 agents interacting in very intricate ways, it's not super trivial to align that whole system suddenly or even to know what the system is, because in this distributed world, agent A may be interacting with agent B today, but then on a different task, it's interacting with agent C tomorrow and C sub-delegating something to agent D, and D is maybe consulting a human for something at some point in the loop.

**40:57** · So how this whole system gets coordinated.

**41:00** · One of the ways in which we know how to do this in human societies is through economic incentives.

**41:05** · And if these economies were set up for agents carefully so that they are not causing some harm when they're profit maximizing, right?

**41:14** · This gives us at least a starting point through which we can try to align distributed, agentic societies.

**41:21** · This is not to say that you know, what we are doing today isn't relevant because you need to have individual agents be safe.

**41:27** · This is a prerequisite for groups of agents being safe.

**41:30** · But we need to do far more in safeguarding against groups than we are maybe doing at the moment.

**41:35** · An awful lot of work to do.

**41:37** · Correct, in a very short span of time.

**41:38** · Yes. Yes, indeed.

**41:41** · That was absolutely fascinating.

**41:42** · Thank you very much.

**41:43** · Really enjoyed that.

**41:44** · There is this idea of agents as AI that requires less from us, you know, less back and forth prompting, less waiting for response to something that gets on with the task at hand.

**41:54** · But what I thought was really interesting about what Nenad said is that focusing on the idea of a single agent misses the bigger picture, because instead, each agent might end up forming part of a much bigger agentic society where there are specialists and generalists and agents who delegate, and agents who focus on the details.

**42:16** · That I think is the bit that's going to stay with me, that that maybe replicating human level intelligence isn't the ultimate goal.

**42:23** · Maybe the way forward is to replicate humanity level intelligence instead.

**42:29** · You've been listening to Google DeepMind, the podcast with me, Hannah Fry.

**42:32** · If you like this episode, please make sure to subscribe to our YouTube channel.

**42:36** · We'll see you soon.
