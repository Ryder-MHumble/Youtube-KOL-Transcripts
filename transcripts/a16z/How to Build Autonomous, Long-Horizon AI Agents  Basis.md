---
title: "How to Build Autonomous, Long-Horizon AI Agents | Basis"
source: "https://www.youtube.com/watch?v=54pwkcp48Lg"
author:
  - "[[The MAD Podcast with Matt Turck]]"
published: 2026-08-06
created: 2026-08-10
description: "AI agents can write code for hours, but ask them to do real work in the real economy, and they break. Mitch Troyanovsky is co-founder of Basis, a unicorn AI company whose agents run autonomously for h"
analysis_report: "[[The MAD Podcast with Matt Turck- How to Build Autonomous, Long-Horizon AI Agents Basis 分析]]"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=54pwkcp48Lg)

AI agents can write code for hours, but ask them to do real work in the real economy, and they break. Mitch Troyanovsky is co-founder of Basis, a unicorn AI company whose agents run autonomously for hours — sometimes days — completing complex tax returns end to end. His answer to the reliability problem: stop grading outcomes, and start supervising the process.  
  
This is a definitive, reference-style conversation on building long-horizon AI agents. Mitch walks through the full history — from ReAct and the AutoGPT crash to reasoning models and RLVR — and explains why the industry abandoned process supervision in 2023, and why it's now coming back at a completely different scale. We go deep on behavior specs, the open standard Basis just released with Braintrust for defining and evaluating how agents behave across entire trajectories, with no ground truth required.  
  
Along the way: why context is really runtime training data, why your documentation must be treated like a codebase, ontologies as "worlds for agents to live in," the judge-as-agent architecture, why Basis hires philosophy majors as Language Architects, deploying agents as "onboarding 300 brilliant alien employees," and Mitch's prediction for when the bitter lesson swallows the harness.  
  
Mitchell Troyanovsky  
LinkedIn - https://www.linkedin.com/in/mitchelltroyanovsky  
X/Twitter - hhttps://x.com/mitch\_troy  
  
Basis  
Website - https://www.getbasis.ai  
X/Twitter - https://x.com/trybasis  
  
Matt Turck (General Partner)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark Capital  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id168623872  
  
Watch the Data Driven NYC Session with Mithcell Troyanovsky - https://youtu.be/xH\_b6iwrASc  
  
01:09 Why Basis Engineers Whisper to Their Agents  
04:12 Accounting as Compression: an Intelligence Layer Over the Economy  
06:11 Defining Long-Horizon: When You Exceed the Context Window  
08:24 Anatomy of a Multi-Day Autonomous Trajectory  
10:19 Handoff Design: Optimizing Output for the Reviewer  
11:17 ReAct and Why Reasoning Must Regulate Its Own State  
12:33 Large Working Memory, No Long-Term Memory  
14:13 Compounding Errors: Why AutoGPT and BabyAGI Broke  
15:51 Opus 3, o1, o3: the Three Real Paradigm Shifts  
17:07 Titrating Inference Compute Across Easy and Hard Steps  
18:23 Process Reward vs. Outcome Reward: "Let's Verify Step by Step"  
20:32 RLVR and Why the METR Curve Overstates Reliability  
22:09 Verifiable at Runtime: the Real Reason Coding Won  
25:14 No Ground Truth, No Cheap Verification, No Data  
26:55 Encoding Deterministic Checks From Human Review Process  
29:18 Synthetic Data Limits: Generating Artifacts, Not Text  
33:16 100 Evals Pass — Does It Generalize to Production?  
35:53 Primary Sources vs. Pre-Training Knowledge  
36:37 Behavior Specs: Markdown, Judges, and True/False/N.A.  
39:58 Specificity vs. Brittleness in Spec Authoring  
42:18 Context as Runtime Training Data  
44:21 Judge-as-Agent: Trajectory Maps and Sub-Agent Attribution  
46:45 The Move 37 Objection: Reliability Over Optimality  
50:02 The Magic Box Model: Building Without Weights Access  
52:41 "Nothing Paradigm-Shifting Has Changed Since o3"  
54:56 Open-Sourcing the Behavior Spec Standard With Braintrust  
01:02:54 Ontology Design: Virtual Filesystems, Graphs, Embeddings  
01:04:20 Canonical vs. Non-Canonical: Docs as Codebase  
01:06:33 Language Architects and Writing for Runtime Interpretation  
01:09:05 Deployed Intelligence: 300 Alien Employees With No Context  
01:11:10 Closing the Loop: Signal → Context, Tools, Harness  
01:12:50 Context Slop: the Mistake Most Agent Builders Make  
01:14:29 Reward Function Design and Credit Assignment Over Trajectories  
01:17:01 Will the Bitter Lesson Swallow the Harness?  
01:18:46 Business Moats vs. Technical Moats  
01:21:03 Paradigm Thinking Over Timeline ADHD

## Transcript

**0:00** · Humans are already used to working with nondeterministic systems. It's just those systems are normally their co-workers, not their computers. And in many ways, like companies and processes is all about how do you design a system for nondeterministic entities to coordinate together to solve a problem.

**0:12** · And once you realize that, it's like, well, now it's like kind of agent design. Let's say you have 100 evals.

**0:18** · Great. They all pass. It looks good. Are you confident that that now generalizes to the real world to production? And our answer has been no. Even if you got it right a 100 out of 100 times, if a person is just getting it right because they're going to Wikipedia, the accounting firm wouldn't hire them and so they shouldn't hire us either. You'll see people like freaking out over a code file that isn't abstracted properly and yet their context is like total. The English is more precious because the English affects the performance. The code does not affect the performance.

**0:44** · Hi, I'm at from Mark. Welcome to the Mad Podcast. Everyone \[music\] is building AI agents, but outside of coding, most still can't do real work reliably. My guest today is an AI builder at the forefront of cracking that problem.

**0:56** · Mitch Troyanovski is a co-founder of Basis, a unicorn AI company whose agents run autonomously \[music\] for hours, sometimes days, and are already able to complete very complex tasks like preparing entire tax returns end to end.

### Why Basis Engineers Whisper to Their Agents

**1:10** · This is a true reference episode on how to build long horizon autonomous agents where Mitch shares tons of lessons he learned along the way. Please enjoy my conversation with the deeply insightful Mitch Troyki.

**1:24** · I want to start with a scene. Uh, as I was uh prepping for this, I uh came across a video by our friend Stephanie Palado at the information and she was describing um uh the experience of walking into the basis office and seeing a bunch of people uh whispering very quietly into microphones.

**1:42** · So you know maybe for the top AI builders or people who live on X you know second by second this may be already something that everybody understands but I think for the vast vast majority of people like just describe what you guys are doing whispering into those microphones.

**1:57** · Yeah, I I think maybe the best piece of advice for not for building agents but for working with AI in general is that you need to give it as much context as possible because it by definition is always missing context in some way. Speaking is just so much faster than writing things down. And in fact, when you try to write things down, you are actually essentially uh trying to summarize all the crazy thoughts in your head. And so that's why it takes a lot of time.

**2:25** · And it's useful for you or I because it's rude if somebody just blabbered and sent that to you as a as a Slack DM, but to an agent, they don't care. Um they uh it's actually they would prefer it. So it it becomes much more productive to be able to like whisper your thoughts, you know, because you don't want to be shouting. Um uh and you have these microphones now that allow you to whisper very very quietly uh and still pick up with full fidelity.

**2:50** · So that's why that's why we have it. And sometimes people see it and they think it's a little weird when they join the company, but \[laughter\] after after a couple after, you know, a month or so, they're it's like they they can't go back. So, and uh so you whisper into what? Into cursor or into Yeah. into whatever people use. I mean, we different people use different things, but yeah, codeex or cloud or cursor or whatever people use and not just engineering, right? Like all the all the functions if you're trying to get something done, if you're trying to describe what you want and all these things.

**3:14** · Okay, great. All right. So uh what I'm hoping to uh do today is uh is a bit of a reference conversation on uh all things around building long horizon agents that's in part based on um a great thread that you had on X and perhaps more importantly a new open source uh project that you just released in collaboration with Brain Trust. We're going to talk about all all about this but maybe for contextual awareness basis in two or three sentences how would you describe it?

**3:43** · Yeah, basis builds agents to do accounting work end to end and accounting is difficult. Um it's not something that is just purely text in text out and so it requires the ability for like AIs to be able to you know perform lots of actions over long periods of time and actually um you know be coherent over that period of time to get to outcomes that are that are good.

**4:05** · Um and that's why we've always you know been very focused on how do you really build agents that can scale to do that work. And did you pick accounting uh because uh of how interesting that was from a uh agent building \[clears throat\] uh perspective or the other way around?

### Accounting as Compression: an Intelligence Layer Over the Economy

**4:22** · Good question. Uh it's probably uh the other way around, but I I do think it is actually quite interesting from an agent perspective. Accounting is interesting for a lot of reasons. It is uh one one of if not the largest knowledge work profession in the country. Um there are over three million you know combined kind of accountants uh in the country.

**4:40** · And what I think is so cool about accounting actually is that most people don't really think about accounting.

**4:47** · They don't think like, oh yeah, why does that even there? You know, probably most listeners have never thought like why does it even exist? And um I know we're going to talk about agents maybe quickly 30 seconds just to convince everyone how cool accounting is. Uh if you think about the real world, uh so much stuff happens, academic activity, right?

**5:03** · Like you know, I was just drinking a water bottle there. like you know someone um uh that bottler had to choose to like go uh uh buy from that factory or that supplier um or decide to open you know some additional uh store hire a salesperson and these are all economic decisions that stem from understanding the real world what's in the real world you know money moves hands someone signs a contract someone delivers the inventory it's like all these events that occur and so much of modern

**5:32** · capitalism relies on the ability of all these actors to make decisions on these events right? Like the CEO of that company, the IRS obviously to decide how much to tax, the uh bank to lend credit, investors, right? All these people, they care about the real world, but they can't understand it because it's gigantic and it involves all of this unstructured and, you know, difficult to parse information. And accounting is actually the art of compressing all of that into something that is structured that now people can look at and understand and make decisions.

**5:58** · So something about accounting, you could argue in a meadow way, is kind of like an intelligence over the economy. um uh because it is really a compression activity of all the information that exists. So I think it's a very cool problem to kind of think about.

### Defining Long-Horizon: When You Exceed the Context Window

**6:11** · This is still the same thing for contextual awareness. So we're going to talk about long um horizon agents. What is a I guess what what is a long horizon part these days? So that that keeps evolving. Uh what falls in that category?

**6:24** · Yeah.

**6:24** · So maybe I can give my quick definition of an agent just I know maybe probably everyone knows at this point but uh feel like that's a gotcha question I like to ask in interviews. Um uh I tend to think of uh an agent as an an AI or like some inference that occurs that has the agency to go and make uh decisions to to do different things. And so by definition it's a spectrum because you can have varying degrees of agency, right? Like you're constrained by whatever environment you're placed in.

**6:50** · And I think long horizon again is a spectrum where you are granting the agent the agency to make decisions that allow it to be coherent for longer periods of time, right? So let's say that you were asking an agent to go and you know look up uh the weather for you. It might be an agent in the sense that it has the agency to decide what tool to call or what Google search to put in. But it doesn't need to do much work to be coherent over a period of time because it's uh um you're just getting the weather.

**7:21** · But if you're asking an agent to say um go perform you know an entire uh feature you know um like implement some feature in your in your repo or asking it to go and you know make a big Excel workbook. Now suddenly it might have to operate for you know longer than a minute. We're talking 10 minutes, 20 minutes, 30 minutes, and potentially even much longer than that.

**7:41** · And once you're starting to get into those scales, you start running into the fundamental limits of how LLMs work in which I always like to say LM have very large working memories and by default no short-term or long-term memory. And so you have to leverage these strengths of the LM to make up for the fact that they don't have long good uh or actually any real short-term or long-term memory um by and we can talk more about it by using harnesses and you know all these kind of uh advancements to allow them to be coherent over a period of time.

**8:12** · So I think once you start getting into the art of trying to get it to be coherent because you're going past the the you know the amount of working in memory it has I'd probably say that's when you're starting to get into what I'd call long horizon.

### Anatomy of a Multi-Day Autonomous Trajectory

**8:24** · Great. And still to the conversation, what we're talking about here is uh autonomous uh agents. I'm curious maybe uh just as an example what autonomous means in the context of basis. So I read that you guys can now have agents that handle um end to end tax returns.

**8:46** · So may maybe walk us uh at a high level through what that looks like in terms of steps along that takes. uh what does an agent do conceptually when you are really autonomous or kind of you know doing something over really long horizon say doing a tax return and hand that means that you uh have a lot of information that is needed to do the work and you have the tools to go and get potentially more information.

**9:09** · So, let's say imagine you're doing a complicated 1065 and you have all of the different um uh you know K1s, W2s, other documents, 1099s, whatever you need um from the uh from the company. Uh uh and then you also potentially depending on what you're doing, you might have the trial balances already. So, that tends to be what you need to actually start a tax return or you're working with like books that aren't even done yet.

**9:36** · Um, and the agent then has to actually go and and figure out based on all this different stuff, how is it going to tackle it and what's it going to be able to do? And that's where you start getting into um, you know, some stuff about like what the behavior should be that we can talk about about well, what does good practice look like to say get to a solid solid uh, set of trial balances. What does good look like in order to properly extract out, you know, the K1s and the K3s so that you can be confident in their outcome. Um, and for it to be autonomous.

**10:05** · It means it's not going back to the user and saying, "Hey, like is this right? Is this right? I need this. I need this." It's like starting the job to I'm done. Um, and I'm done does not mean I'm done. You click a button like no one looks at it.

**10:18** · It's actually the opposite of that. It's much closer to what you can imagine a preparer doing or or maybe like a first pass or junior engineer or something of of I'm done. Here were the big decisions I made. Here were my assumptions. Here were the different things you need to look at. Let's go and review together.

### Handoff Design: Optimizing Output for the Reviewer

**10:32** · Right? And if you think about somebody say in engineering, you know, an engineer handing you a PR, nobody likes being handed a thousand line PR, they're like, it's done. I promise. It's like you don't want to review that. But if you instead handed somebody, you know, a great stack that was like that was like properly split out and you could understand very easily, hey, here is exactly what this change is and this diff and I made this big architectural assumption here and here's why I made that change. and you can like optimize not just for getting the work done but for making it easy for your reviewer to understand the decisions that you made.

**11:08** · Uh and that's obviously very true in software engineering and it's actually true in I think most professions uh and especially accounting which we can kind of get more into. And so to me that's that's I think what it means to be to be autonomous. So I thought what would be fun and helpful uh for people listening to this would be to spend a few minutes on I guess the history of agents like

### ReAct and Why Reasoning Must Regulate Its Own State

**11:25** · we've all heard over the last two to three years so many different things so many different terms some projects that work some projects that didn't work so I think it would be helpful to just like go back in time just a little bit what what in AI may feel like a prehistory but in reality is like what three years ago four years ago so maybe starting uh in 2022 with the react uh framework.

**11:44** · So not the software engineering but like reasoning and and acting which I believe was a paper in 2022 that fundamentally said this agents are combination of like reasoning and acting which you you just alluded to. The fundamental question is that is that still largely what's what's happening?

**12:03** · I mean with you know a tremendous level of sophistication on top of it but like is the fundamental theory of an agent still that I think within the paradigm of modern day LM yes more so more or less in the sense that I would say it is actually the same um but it kind of extends out uh further which I don't don't really remember if it was part of that paper back then of needing to use your reasoning to regulate your own date like

### Large Working Memory, No Long-Term Memory

**12:34** · I the analogy I like to always give to people um at the company when I'm you know learning about agents for the first time uh not even not not you know not even just technical people like anyone at the company actually is the movie Momento I think momento for those who haven't seen it um uh is is a movie in which there's this guy who you know has short-term memory loss and he every day he wakes up and he knows who he is and he knows um you know like he knows he's a human like he knows like some basic stuff but he doesn't know like what's happened in the last couple years. He has no idea.

**13:04** · And for him to make progress to any particular goal, that could be something like, you know, getting groceries or getting revenge or whatever it is, he effectively needs to write stuff down for himself. And then when he wakes up the next day, he reads his notes and essentially builds that up. That's how he like builds up knowledge.

**13:20** · Early Christopher Nolan movie, by the way, like at the time when like everybody obsesses about the Odyssey, this is one of the early his early works.

**13:26** · Yes.

**13:26** · I I still I think The Prestige is the best Nolan movie, but but um but yes. Um but anyway, so I think that to your point, it is actually about reasoning, but I think and I don't I don't think it talked about in the paper. It's just it's there's reasoning in terms of what path is right to go for whatever the task is. Like do I do tax this way or that way? For sure.

**13:42** · But there's also reasoning about how do I make sure my next inference step has what it needs to uh uh properly like you know um interact with the world which is is easy if you're in a short horizon because you're within the context window but once you start getting to longer horizons where you're beyond the context window or you're getting to context rot you need to kind of use and sort of brute force your reasoning to um build

**14:07** · out your environment um whether that be with sub agents or compaction we talk more about that but that's I think where the reasoning becomes superant important.

### Compounding Errors: Why AutoGPT and BabyAGI Broke

**14:14** · Okay, great. So, the next step after 2022 was uh probably baby AGI uh in 2023 uh which you know everybody viewed as just like a massive advancement. Uh but that sort of failed. I mean that was a beautiful experiment but like didn't quite work out in in in practice. Uh so why is that?

**14:35** · I guess there was at the time like people talked a lot about compounding errors and um you know how if you had many many steps and uh the agent started going astray then that would compound. Was that was that what it was from perspective? Yeah, I think back then I think that I believe if I remember correctly that was like GBD4 maybe four turbo um at the time the models back then for starters if it was pre-turbo like the context windows were very small um and so you you know if

**15:05** · you're going to be coherent you need to have at least enough stuff in your context that you can organize your own environment so they didn't have that um and even when the context windows got larger I don't think by the time baby came out the models were actually good at keeping attention over like once you got past whatever it was like 20,000 tokens, they were just not smart. It took until maybe Opus 3 for them to start getting smart at like 100,000 tokens even. Um, and so that was Baby AI didn't have that. And then also obviously, and we'll talk more about it, they they just were not good reasoners.

**15:35** · And so if you're not a good reasoner, then you're going to have lots of compounding errors because you're going to make one mistake that's, you know, in your um in your kind of per token generation and now suddenly that just compounds and you have no way to have the self-awareness to actually like self-heal in any meaningful way.

### Opus 3, o1, o3: the Three Real Paradigm Shifts

**15:51** · So the the the big breakthrough then was reasoning models.

**15:54** · Yeah.

**15:54** · I would say when I think about what were the big like uh holy moments for for I don't know if you can curse but yeah like what were the big kind of holy moments uh for us uh at least for me personally it was probably or at least the moments in which there was a genuine paradigm shift there haven't been that many I would say they were opus 3 which I which I I think goes underappreciated but I think was the first model to truly be able to uh

**16:25** · like actually understand at long context before if you put anything into like 80,000 tokens into GPD4 turbo it could not understand it 3 actually understood it which was remarkable um I think it was that I think it was 01 obviously everyone talks about that and then I think after 01 it was 03 because I think 03 helped prove that not only could you scale the amount of reasoning at inference time but with better training with more compute better data etc in the post training phase you could make the reasoning higher quality, more efficient, and uh just better.

**16:56** · And so each incremental token that it reasoned with at inference time was higher quality, which was not obvious when 01 came out. Um so I think that was I think those were to me the big breakthroughs.

### Titrating Inference Compute Across Easy and Hard Steps

**17:07** · Is there something about the fact that those were effectively trained as agents in loops where there's a chain of reasoning where they try something, backtrack, try something else? Is that the fundamental reason why this works better for agents?

**17:20** · I think it's a couple things. I think it's that um because the model is able to kind of like titrate the amount of compute it's throwing at any specific step in the process, you're able to uh uh in any trajectory. There are a lot of decisions that are really hard and some that are really easy. Um and uh it's just not feasible to have like you know some giant parameter model that's super super expensive to serve that has essentially using you know all of that compute at every single inference step.

**17:50** · And so um the ability to to reason uh allowed you to titrate that and I think as as you pointed out as a kind of maybe emergent um u behavior that if you are a really good reasoner and you and you can dial it up like a lot like if you actually look at the amount of compute for an easy step versus a hard step it's a lot different with the you know modern reasoning models. um you could become better at self-healing uh because you're

**18:13** · going to be like pausing and thinking about everything and sort of using that more um you know that kind of thinking versus just doing everything on instinct which is what was happening if you're doing kind of like just per token generation.

### Process Reward vs. Outcome Reward: "Let's Verify Step by Step"

**18:23** · In your X thread you talk about um something open did in 2023 when they published something called let's verify step by step where humlabeled about 800,000 reasoning steps. What did that happen then? and um you know what what was the goal?

**18:39** · Yeah.

**18:39** · So that paper uh came out so back I think before people uh trying to remember the exact history here but essentially uh there was a lot of rumors back then about uh you know if people remember like the information article like oh strawberry solve math or or whatever it was.

**18:57** · Um and so I think even before those rumors came out there was you know some hints in the literature like like this and and uh um uh that might have been after the rumor I actually don't remember but that math was a um or or you know these kind of problems that you could uh you could verify were maybe good ways to try to train the models to to to be better at um uh at kind of different tasks. And I think this is purely speculation because I was not in the labs.

**19:25** · But there was this sort of question back then and through a lot of um the history of ML around uh are you going to give the reward just from like whether it got the problem correct or whether uh it approached it like a good mathematician would approach it. Um and what's interesting is that in that paper with J publish they showed that actually uh if you rewarded based on the process rather than just an outcome you actually got better results within within that that sample but that obviously is expensive because that required mathematicians to

**19:58** · you know grade the approach they took to the problem right um uh versus if you look you know if you fast forward a bit and you look at the like the deepseek um R1 paper uh where they effectively laid out you know what I think all the labs were doing at the time or at least open was doing in terms of uh you know RLVR of reasoning from ver uh reinforcement learning from verifiable rewards uh that effectively had very little uh process

**20:23** · supervision and instead was essentially um just saying hey did you get the outcome right yes okay let me reward you and then scaling that up um which you know obviously worked well still in the recent evolution of of agents so just uh I guess it was last year there's like this famous now famous meter chart that shows that um longer rise on agents capabilities like double every seven months. Is that is that something that you still observing in 2026?

### RLVR and Why the METR Curve Overstates Reliability

**20:47** · Yeah, absolutely. I mean I I don't I think the meter chart is somewhat inaccurate these days because it's so hard to measure.

**20:52** · Yeah.

**20:53** · Um also the bar is pretty low, right?% the bar is pretty low and and I think I'm not super familiar with their data set, but my my understanding is that it's um it's like a low like the sample size is kind of low. So so I don't know about the specifics of of that metric.

**21:06** · Um but I think you know from a vibes perspective absolutely like um uh you kind of the models were able to start being coherent for longer periods by um by being smarter. Uh but now they're also being specifically trained to do that. Right? So that means they're being trained at how to you know how do you have good theory of mind over yourself because you need to if you're going to be outsourcing to a sub agent, right? Or if you're going to be writing notes off to yourself.

**21:31** · Go back to the momento analogy, right? like uh you need to think about hey I'm going to wake up tomorrow and I'm going to read these notes what is the most information dense way for me to write this note down so that me in the future will understand it well that requires kind of a theory of mind and so you know as these uh models

**21:48** · are being trained more on actually how to do that kind of work which is very very non-human like humans don't have to because we're great at that actually so we don't have to um write for ourselves you know our brain does that for us um you're starting to see it get get even farther I think we're still actually quite early at that if you look at some of the advancements, you know, to Fable 5 and 5.6 Soul and whatnot.

**22:08** · Great. And just to uh go a little deeper on on what you just mentioned, um I think, you know, a a a broad context on on agents in 2026, the evolution towards autonomous agents would not be complete without actually talking about verifiable rewards. So tell us what it is, where that fills in the overall picture. Um and then perhaps why coding was the first uh successful uh sort of autonomous agent use case and how that's you know related to verifable rewards.

### Verifiable at Runtime: the Real Reason Coding Won

**22:40** · It's kind of interesting. I I think um I just think people get this a little bit wrong. I'm speaking with a little bit of speculation because I don't actually know um exactly but uh coding uh yes is verifiable in the sense that I can know whether the code passes or not. And so I could train um on that, you know, did you get the problem right, did you get it wrong, etc., which is useful, but the models being great at coding is partially that, but it's partially I think a couple other facets of coding.

**23:10** · So number one is that coding is verifiable at runtime. I think that's a very important point because I as at the end of the day like an agent needs to get signal as to how it's performing.

**23:22** · And so imagine if you were an engineer and you, you know, wrote code and you could never run it. Like even if you were the best engineer in the world, you're going to have a syntax error in which the thing is wrong at some point.

**23:29** · And so I think the fact that coding is so easily verifiable at runtime or at least some some parts of it are verifiable runtime is obviously very valuable for it being there and it's cheap to do, right? It's easy to do within the environment and it's super text based. So it's available anywhere like you can just on your local computer you can just run it, right? And so I think those aspects of coding actually make it um are a lot of the reasons it's it's uh the agents are getting so good at it.

**23:53** · I think one more piece of it is that um and I think we probably saw this if you think about how good agents were at coding maybe a year ago, a year and a half ago. they uh they could go and implement a thing you told them but they didn't have the level of like uh you

**24:11** · know taste or level of like what is good software because even if you train them with verifiable rewards on like hey did this unit test pass like you could pass all the tests in the world doesn't mean that you set up the the app correctly doesn't mean your database was built well doesn't mean that you you know split out the files properly right at the end of the day coding is subjective it's an art uh and you're not going to be solve an art through verifiable rewards and so I I actually think there's a large part of this which is the amount of training data and the quality of training data that the models that the labs have clearly for coding

**24:40** · has gotten quite good and they've focused a lot on making sure it's very good so that they're training on high quality code. Um, so I think that's the other part is just that maybe because the labs are obviously full of engineers, uh, you know, is more top of- mind and obviously it's part of their strategy and so they, it is more top of- mind for them to ensure that both their pre-training and post- training sets have lots of high quality code and that's what makes the agents great at not just writing code but now starting to become good at actually engineering.

**25:06** · So I think it's all those things together. I think the verifiable rewards are maybe just like the beginning that allows that stuff to happen, but I think the other stuff matters just as much if not more.

### No Ground Truth, No Cheap Verification, No Data

**25:14** · Great. uh which brings us to the the core of the thesis which is your work um on a domain that's outside of of coding. So building long horizon autonomous agents for uh I guess the real world for lack of a better term outside of term.

**25:32** · Okay. So uh why do agents struggle? Uh you mentioned three reasons maybe maybe you mentioned what those reasons are and then we'll go into them turn by turn.

**25:43** · Yeah.

**25:43** · Yeah. So, I think agents um uh struggle for a lot of reasons. Um I think one they struggle because uh they don't necessarily know what good looks like. Um I think they struggle because it may not be easy to verify yourself uh at at runtime. Um as we were talking about with coding. Um, I think another part is that uh, and this is maybe not an Asian struggle, but maybe it's a UX thing, which is that for coding, engineers are just very in the weeds of it.

**26:13** · And so there's a kind of a difference where if you were like running a long horizon agent for coding, if the engineer was not, you know, engineering and like in the weeds of the code, if instead they were more abstracted away, your maybe level of uh, quality and, you know, how you make decisions probably you maybe need a need a higher bar than you would for coding.

**26:32** · You know, coders are okay with lower bars. that's been true forever. Um, and so I think all these things add up um, in in in making it and even now with coding like the agents are not yet uh they're not h they're not they're not human level at being coherent over long periods of time. That's obvious because they can't code like a junior engineer on a project for two weeks. So they can't that's worse than a human uh even to start.

### Encoding Deterministic Checks From Human Review Process

**26:55** · So, so uh let's take um that uh part about uh verifiable rewards and the fact that people writing those systems don't necessarily have intuition for for what good looks like? Um so how do you guys solve that? Like what what does um uh you know passing a test mean for a tax return that you know unlike code doesn't need to compile?

**27:20** · So the good news is there are some things that can compile um uh not all but you can obviously test to either you get sued or you don't get sued. \[laughter\] Yeah. Yeah. Well, I I I think the answer for this is you you look at what humans do and how and uh one that nice nice thing about accounting, which is true in some other professions as well, but accounting is a profession in which you really try and have to be correct.

**27:43** · And so because of that um and it's something in which there's so much judgment and and um uh you know process involved where I one of the sayings we have and I say this on the design side a bit but it's like humans are already used to working with non-deterministic systems.

**28:00** · It's just those systems are normally their co-workers not their computers and in many ways like companies and processes is all about how do you design a system for nondeterministic entities i.e. like humans to coordinate together to solve a problem. And once you realize that, it's like well now it's like kind of agent design sort of. And so I think if you needed to think about what is good agent design uh and what can be verified, you should look at how the humans organize. Um and if you look at how humans do tax returns, uh you have steps of verification, you have independent review. Um you have things that can be deterministically verified.

**28:31** · So you can say, hey, like you know, uh obviously do like do the TBS like add up to zero, right? That's like a very obvious check. You can things like is the Excel not have errors is an obvious thing, right? And so there's lots of things like that that to human or obvious, but you need to make sure are properly encoded. And there's other things that are maybe not as um uh deterministically verifiable, but like, you know, would be obvious to to an accountant to look at it. Oh, this is wrong, you know, of like uh oh, you deleted this tab in this Excel or you didn't site this thing or whatever it is.

**29:01** · And so you can start to build you know verifiers effectively from these things that are not uh deterministically verifiable but you know if they're an accountant would look at it it would be obvious and so you can start to you know think about judges or other you know uh forms of of of verification to like get that signal both in your eval but also at runtime.

### Synthetic Data Limits: Generating Artifacts, Not Text

**29:18** · So that's one thing uh I think you pointed uh in your X thread um that there was an issue around scarcity of data.

**29:27** · uh if you can you go into this let's say just for sake of argument here you had uh not just synthetic but every like real tax return uh across uh the country which you actually couldn't do for for privacy reasons let's say you did you don't have that and you was like okay let me use this as a as a way to get um uh data that you're not training but data that allows you to verify how well the agents are doing the order of magnitude there is tiny compared to you

**29:56** · standing up math problems synthetically and you're generating you know whatever hundred thousands millions etc. And so even if you had all the data in the world you uh would not be able to scale it. So you need to think about how do you synthetically generate it. Um and if you think about how to synthetically generate it that's really hard because you're not just synthetically generating text you're synthetically generating artifacts that have to be real and diverse. And so now you get to all the same problems about like uh data, you know, data diversity, all the different things that you need.

**30:26** · And I I have no doubt that that problem will be solved over time, but it's not solved today. Um and so uh there's this kind of gap between like uh maybe what is possible from a data generation perspective and what is actually possible, what latent capabilities the models have, which is maybe where you get the some of the stuff we were talking about in the in the thread.

**30:46** · And how do you think about the length of the feedback loop? Yeah, I mean that's the other thing is the length is can be very long depending on what you're doing. Um, you know, performing a uh a 1065 uh can take a human, you know, uh like 20 plus hours uh easily of actual work. I don't mean like it took them a day. I meant like literal sitting down work. Uh and it could actually take much longer for very complicated uh returns.

**31:11** · And so there's just no way that you even if you had all the data uh in the world, which you can't have, um you would be able to have the feedback loop needed to like do whatever you know improvement loop you wanted to do um to get the agents to be really good.

**31:27** · And again to make that concrete like how many steps uh would be involved in uh so many steps in compiling uh you know a a tax return?

**31:35** · Yeah, I mean to give you a sense like you could have for example 500 a thousand documents easily. You need to think about how to map those documents against each other. Understand what matters. You have to potentially perform lots of different research per different document. You have to potentially think about um uh uh what they all mean. Um you know you have to compile them all into certain at least today into workbooks of certain types which are like big Excels. um uh there's a lot that you have to do.

**32:04** · So you're talking I mean steps I don't definitely in the in the few thousands easily if you're thinking about like inference steps um and uh you know depending on how you build your system uh if you start to span out you know sub aents for

**32:20** · different things which you kind of have to do you're you're increasing that potentially and that's before you think about other you know test time compute uh methods for example you know one thing you could do is say well imagine you you there's a tax question you have to solve and it's like insanely difficult you know like only an expert to be able to solve this specific tax question. Maybe there instead of, you know, the agent doing responding a sub agent, you're spawning five and you let them vote. And so there's just lots of other things you can do to to throw more compute at the problem. Um, and so based on what you're doing, like the amount of steps end up being quite large.

**32:51** · Okay, great. So to play it back, uh, you got very complex processes with many many many steps. You don't have a lot of data to, uh, figure out what went right or wrong. It's not even always clear what is right or wrong. Although you can uh at least for certain parts of our problem say definitively whether this is right or or wrong but not always. So very complex problem which leads to how you guys have approached it. And uh in particular there's this concept that you can't just rely on outcomes uh but you need to rely on process.

### 100 Evals Pass — Does It Generalize to Production?

**33:25** · So what is so wrong about relying on outcomes?

**33:29** · Yeah

**33:29** · the problem with relying on outcomes. So if you have a, you know, multi,000step um uh trajectory or you even honestly one that's like an hour long, you will have evals um that will say what good looks like. Um and it could be entirely verifiable like do the numbers match and it could be you know um parts that having LM as a judge like there's some rubric etc. And let's say you have 100 evals great you know uh uh they all passed and looks good. Are you confident that that now generalizes to the real world to production?

**33:59** · Uh and our answer has been no. You actually cannot be confident of that. Uh and so you shouldn't only rely on that. Um in the same way that if a if an engineer came to you and said hey you know all my tests pass end to end unit test etc.

**34:15** · Like does that mean that they architected the database properly? Like not necessarily. That doesn't actually tell you that. Um there are a lot of ways to to to pass quote unquote outcomes without um uh you know having done the the process properly. And so um what we have found is that there are especially going back to my point earlier on analogizing to human organizations there's lots of learnings from how humans do work. And so I think it is a a mistake to throw out those learnings and say you know bitter lesson throw out those learnings.

**34:45** · We're just going to have the agents at runtime develop an entirely new way to do a tax return that is you know because bitter lesson yada yada will be better than you know the hundreds of years of human history that have gone into learning about the right process. Uh maybe that will one day be true. I I'm not saying that it will never be true and I do think it is it is possible going back to like the uh data bot we talked about earlier and I think if you throw enough data and enough compute in a you know outcome based process you can eventually get there but not soon.

**35:13** · And so if you're not going to get there soon uh and you have this latent potential in the models, what you really need to do is think about let's take the learnings from how humans do things from what good process looks like you're not you can't copy that exactly because there is a lot of um thinking you have to do about uh good agent design. It's not like the models out of the box today are um uh incredible at being coherent of long horizons.

**35:37** · There's actually a lot of work there about behaviors uh for sure. um and you can instead put in place certain um uh you know eval or potentially in the future kind of reward functions that look at whether it followed the process properly or not and maybe the example I mentioned the thread which I'll just say for the audience is imagine you're doing something as basic as tax research um if

### Primary Sources vs. Pre-Training Knowledge

**36:01** · you ask them tax question the agent could definitely get it right they could know it from their pre-training knowledge they could read some blog and get it correct but a real accountant would not trust that. They would want you to site the primary source. So even if you got it right 100 out of 100 times that if a person is just getting it right because they're going to Wikipedia that the accounting firm wouldn't hire them and so they shouldn't hire us either. And so we think it's really important that no actually our agents are not uh learning from the pre-training knowledge or reading from a blog.

**36:28** · They are going to you know the actual code and verifying the information with the primary source which is what you would ideally want a real tax accountant to do as well. Mhm.

### Behavior Specs: Markdown, Judges, and True/False/N.A.

**36:37** · So you guys created that concept of behavior specs.

**36:41** · So walk us through what that is uh very practically. Is that a markdown file?

**36:47** · What what what does it look like?

**36:48** · Yeah.

**36:48** · So the the original idea actually my co-founder Matt came up with the idea uh literally about two years ago. We're talking about autogi back when we were um uh even back when we were had agents that weren't fully I guess agentic as you think of them today and they you know had restricted choices. Even back then you still wanted to think about okay what kind of choice you wanted to make at this at this fork in the road and so Matt we actually used to call it internally metab behaviors uh because the idea was that it was a you're defining a a behavior but it's at a meta

**37:17** · level because it's all the across all the behaviors agent will have you know in all the different trajectories and uh so the idea was that instead of trying to write the prompt you have to first align on what the meta behavior is uh and so that was actually the first purpose of this concept I swear to god like literally two years ago Um, and over time that kind of evolved. Um, and we ended up calling it behaviors just cuz it's it's a bit simpler. Uh, and the idea is that you have a a markdown file in which you write down how do you want an agent to behave. Simple as that. It could be at it could be at varying degrees of granularity.

**37:48** · So let's say you have something that's like very specific like um you need to go to like look at the primary sources. Maybe you want to be more specific. Maybe you're like no, you should always go look at specifically the IRS website. Um or another example could be imagine you're making PowerPoints and a behavior is well before you return the PowerPoint you should render it an image so you know if you made any formatting issues um and uh so you put that in a in a

**38:13** · markdown file and ideally that is a markdown file that is now that can be self-contained so one that humans can look at and align like yes this is the behaviors that we want in part because behaviors are actually subjective exercises we can talk more about that they're actually it's it's just as much of a product thing as it is an intelligence Um and and then it's something that a

**38:34** · judge can look at where they can look the judge can look at a trajectory and say hey did the agent exhibit this behavior or did the condition occur that it would need to exhibit this behavior and if so did it actually exhibit that behavior and then you can grade it accordingly and so who writes the markdown files or supervises the process of writing humans okay and those humans are accountants that's a good question um it depends a bit um I think that uh I think it is a

**39:02** · it is a combined effort between accountants and ML researchers you know at the applied level because you're not just saying for example hey the behavior is you should go to the website you might be saying hey the behavior is that uh you should be like you know for this

**39:18** · for this type of research you should be you know spawning a sub agent with like full history because you need uh you need to build up that context like there's a lot of agent machinery that comes into And so you kind of have this thing where there is what is the a good process looks like for a human but then you need to like translate into agent language um uh and then decide and

**39:37** · there's like a combination there where you're also talking about like what are the like um agent mechanics and so I'd say it's a dual effort between accountants and and and ML researchers and we have a whole team actually it's called accounting product operations where it's accountants who's uh essentially what they do is they work very closely with the research teams to build out rubrics both outcome based rubrics and then also behaviors And how do you think about precision versus um making sure that the system doesn't break? So you mentioned go check the IRS website.

### Specificity vs. Brittleness in Spec Authoring

**40:06** · Is there a possibility that at some point actually what you should do uh you know year one is go to the RS website but then in two years from now there will be a different location for the information.

**40:19** · No that's a very very good point which is exactly why the behaviors are not actually shown to the agent. So the behavior could say, "Hey, you should go to the IRS website." That doesn't mean the agent is told to go to the IRS website, right? Um it might be, it might not be. It sort of depends like uh but the point is that the way I think about it is the level of as the kind of agent, you know, engineer, systems engineer, you are making the decision as to how um uh specific do you want to be with the situation. Obviously, you prefer to be less specific, right?

**40:47** · I think as as people who are good at building agents know like it's much better at the margins to be able to give principles and the wise and more context and let them figure it out. And so with behaviors you want to actually not define every possible thing that can happen but just say no no no we know that for example let's say you're making powerpoints taking a picture of the PowerPoint before you give it to the user is going to catch issues. We know that for a fact, right?

**41:10** · And so we as the agent engineers are going to take a stand and say out of all the different things you as the agent are going to do, this is the thing I'm going to grade you on. And then maybe you're being a little bit more specific there. If you want, you can be more specific, like use this exact tool, but ideally you don't have to. It depends on kind of how your your system is is built. So I think it it I think your level of specificity depends on the maybe uh what specific outcome you're sort of trying to drive and how that much that outcome generalizes to the universe of situations.

**41:41** · Like if you're producing powerpoints, of course, taking a picture like makes it better. But let's say instead your agent actually is a super fast agent. Well, make taking a picture takes time. So maybe a super fast agent, you don't want for it to take a picture of their PowerPoint because now you went from it taking 30 seconds to taking 1 minute.

**41:58** · But if you have an ASIC engine agent that's taking 20 minutes, you went from 20 minutes to 20 minutes 30 seconds, do it every time. And so this is goes back to my point on the product aspect where it's not just an intelligence thing. It is a subjective exercise about how do you want the agents to behave in production broadly. And I I think it's why it's so critical to to product building.

### Context as Runtime Training Data

**42:18** · So we were talking um a few minutes ago about that 2023 effort by OpenAI that required 800,000 human labels. um how is what you're doing in 2026 different?

**42:32** · So yeah, good question. So we are uh today at least uh not actively rewarding the underlying model. So we're not currently post-training our own models by rewarding them on this process. I do think that's a very interesting area of research. We can talk about that later, but that is not actively what we're doing right now. It is something we're actually researching uh separately, but that's um more in the future.

**42:52** · Um and so if you kind of if you maybe take a step back, it's useful to sort of analogize the work of agent building and context engineering to the work of training a model directly. Um I think when people think about context, they you know people say prompts context. I think the mental model people have usually is like oh I wrote some English model what to do. I think it's the right the wrong mental framework. I think the framework I like is thinking about it as training data except you are just training the model at runtime.

**43:23** · It is training data and because you the model is learning at inference time the total amount of training data is far lower right like the total amount of context in your system that the agent would progressively learn you or discover throughout it trajectory obviously orders of magnitude lower than the amount of data that you're training like post- training a model on. And so uh what you're doing is you're essentially taking this this data and you're trying to ensure that it is of the highest quality to get the agent to exhibit the behaviors that you want it to exhibit.

**43:56** · And obviously the the data is only one part of it. There's obvious there's the harness, what are the tools, what are the capabilities, the environment, there's all that part of stuff.

**44:04** · Obviously which model you're using, things like that. And so what's different here is that we're taking this signal and using it to improve the entire agent system, which requires far less data scale than if we were trying to take the signal and more literally reward it in an RL capacity to the underlying model.

### Judge-as-Agent: Trajectory Maps and Sub-Agent Attribution

**44:21** · You mentioned um a judge uh a few minutes ago. Maybe walk us through how you train that judge to do what or how you instruct that judge to do what. Uh and I guess the obvious question of like who judges the judge.

**44:37** · Yeah.

**44:37** · Yeah. I think that's true not just for um like behavior eval but also for you know outcome based evals in general.

**44:43** · It's a great question. I wish we had more time uh to go deeper on this. The reality is we just don't have the time or resources to like uh spend uh huge amount of effort like you know perfecting every judge. But I'll give you kind of the high level. Um uh generally what you do is you uh need to build an intuition for if the judge's taste is correct.

**45:03** · Uh and you uh I do think an interesting area of potential post training uh research is on judges and and you know potentially uh taste there. uh today you need to set up the judge so that it has the information it needs to make the decision and it has the right kind of framework to do that um and that it has the uh data and mentality to do that.

**45:30** · So I'll give you an example with behaviors that could you can imagine being pretty complicated. So right now at least the behavior judging is relatively expensive because it's a pretty advanced judge in that it is also an agent. um it's not a judge in the traditional sense. It's literally an agent because it has to look at the trajectory. So it's quite expensive.

**45:47** · You can imagine in the future and and you know I think folks like brain trust and others are are starting to think about this is like how can you uh label trajectories better so you can potentially e more easily uh filter the trajectory to only the potentially relevant parts to give to a judge instead of having it like look at the whole trajectory in some ways. Uh but if you have a trajectory especially if you have a long horizon one that might have a lot of sub agents you as the judge need to think about well where do I go in this trajectory? How do I understand it? You probably want to have a map of it in some form. Uh who am I even judging?

**46:19** · Imagine you have like a sub uh an agent system with like depth of you know seven. You could have literally seven layers of sub agents like am I judging whether the root behave properly? Am I judging like one of these other agents? And so you need to actually uh uh uh properly prompt and potentially tune the judge so it has a good understanding of knowing where to go judge, understanding the behavior itself, like what is the condition and understanding how to like you know uh judge whether the behavior occurred.

### The Move 37 Objection: Reliability Over Optimality

**46:45** · Are there any tradeoffs with that approach? So what what comes to mind is yes having a human validated process uh guarantees or at least help uh secure uh a rigorous approach that's less likely to fail. At the same time you are not going to get a move 37 kind of kind of

**47:08** · you know result where actually the AI would do a much better work much more efficient work by sstepping you know this part and fast forwarding through those three steps. um what are the sort of pros and cons and trade-offs?

**47:21** · It's a good question. Well, I think for starters um and I guess one thing that should be I want to make sure is clear I think to to everyone listening is that you writing a behavior down is expensive because it is something where you are now keeping state right you need to keep it up to date. Um, if the way you are uh making the model or the agent exhibit this behavior is through context, now you have potentially duplicate states depending on how you're thinking about it.

**47:48** · Um, and uh because of that maintenance burden, you ideally want to have as little behaviors as possible. So it's not that you look at what it takes to do a tax return and you say, "Hey, let's write all the best practices down and see if it's doing it." is that you take the couple that you think are most important that have the largest amount of generalization to production and are the most impactful and you care about those not everything. So I think that that's one important part. Um so ideally if you do it properly you still have rooms for you know the move 37s in theory.

**48:18** · Um but I think there's another part here which is that what are you selling to someone if you are trying to just like if you were to hire you know an engineer um and you know you know at your job you uh at the company you have a process and the process is like um you I'm just making this up but like you write a quick architecture diagram and you like chat with the CTO and you get it approved and you make a PR and you split up the PR in like 10 10 um uh different smaller PRs

**48:50** · into a stack and then you merge it in and you make sure you have your end test and you deploy it. Like that's the process. Imagine if engineer came to you and they're like, "Hey, here's my thousand line PR. I'm going to merge into production right now." What if it's better than what if it's a move 37? It could be better than what the CTO would have came up with, but that doesn't mean it's good. Like that doesn't good in the sense that doesn't mean the CTO or the company is happy about that result just because it's better, right?

**49:12** · Because at the end of the day, the reason you perform work is not because any individual unit of work is incredible, but because you can scale it to a company, to a system, whatever it is, to an organization. And so the thing that um you know, someone is buying from us is not this will be the best ever tax return. They're buying it that you know the confidence that best looking one.

**49:33** · Yeah.

**49:33** · The best looking one or like it you know it moved 37 the TBS over here or something, right? They're buying that it's going to be consistent and reliable and something that they can trust that actually will uh they they will you know just like with a human they can learn to you know trust more and more and then granted more agency over time right and and and I think that that level of trust and reliability like that's what you need to deploy into the real world you don't need the move 37s you need that maybe at the you know Olympiad uh uh

**49:59** · like math competitions but not like doing work in the real economy yeah as I listen to you with one of the many things I find fascinating is that um you're doing all of this without having um actual insight about how the the underlying model works, right? Like you sort of like all of us, right? Like you sort of guessing and inferring from how the model behaves through like artifacts and judging from tool calls and how does that work?

### The Magic Box Model: Building Without Weights Access

**50:23** · Um uh and um and then maybe walk us through uh each time a model changes or the next version of the model you know gets released like do do you have to then look at um everything that you've been doing in the light of that new model?

**50:43** · This actually maybe goes back to the like, you know, Opus 3 01 03 because I I do think one thing that's really important when you're building agents, but it definitely building a company around it is you should you shouldn't be that surprised. Um, you should have a a model of the world and as things change, you should update your model. Um, but uh to be successful, you know, you can't just update your model all the time. You need to be right a little bit.

**51:06** · Um, and I I I do think that uh if you really internalize some concepts about this, right, that like you now have this, forget about the internals for a second. Forget about this LM. have this magic box and you \[snorts\] have this this magic box or this alien I like to call it sometimes and you could send in huge amounts of data into this alien and it will be able to uh uh reason and

**51:35** · learn at inference time within that magic box and then come back to you with output that uh you know now that tool calling obviously works and whatnot you can plug into the rest of the system.

**51:44** · That's kind of all you really need to know. And I think once you really appreciate what that means and you take it to its logical conclusion, a lot of stuff starts to fall out of that because you start to understand it's like, well, okay, well wait, like if I have this magic box that can do this, does that mean that it could decide to call another magic box? You know, does that mean that it could potentially uh string together like multiple of them in a row, right?

**52:08** · Does that mean it could you know leverage uh obviously at that moment it has some uh it's a magic box but it has some state you know we know this it has an activation state uh that's how the caches work so there's some activation state that by definition is going to be biased to that current trajectory and so

**52:24** · maybe for review you want an uncorrelated trajectory right where it's like a new box uh and it's just a smart and and I think if you build these kind of LM intuitions and you combine them with you know maybe basic principles of like organizational design and management Um I think you start to get to maybe what is like the frontier of agent building.

### Nothing Paradigm-Shifting Has Changed Since o3

**52:41** · Fascinating. Practically how how do you build that LM intuition? Is that uh by uh just uh reading papers all the time or talking to researchers or like getting a sense for where the state-of-the-art is is going?

**52:55** · Yeah, I think it's none of that actually. I think I think it is all about I mean I think reading like Twitter and whatnot just understanding is good, but I actually think a lot of people overindex on that. Like I think a lot of people they think like oh yeah I I saw this tweet I saw this like it's the next cool thing. I think the problem is without like a fundamental like grounding in how things work and what is possible. It's easy to feel like things are moving around a lot when they're actually not. Uh things have really not changed since 03.

**53:22** · I would say almost everything since 03 has been relatively on I don't really want to say on trend and that like I knew this exact trend but I would say it's all within the same paradigm like nothing paradigm shifting has changed since 03. Um and I think the best way to understand it and learn about it is to just use them in your own work a lot.

**53:43** · Um I think especially in in coding um and just trying to understand things like a good mental model is let's say I try to you know have an agent you know implement a feature for me and it didn't do the way I wanted to like why what is actually the limiting factor you know it's kind of like the the famous um like Elon mindset it's like okay like you go to like the main limiting factor and you like figure that out like I think if you apply a similar mindset to to agents and you understand like why could it not automate this was it actually not smart enough probably no

**54:12** · they're pretty smart they've been pretty smart for a while and so once you if you like apply that mindset to your own work I find that is quite useful for building intuition and I see that actually with you know people I interview um a lot of the people with the best agent intuition actually yes a lot of people come from ML backgrounds but people who don't a lot of them are ones who are just really good at automating their own work um

**54:34** · really good at thinking about it really good at understanding like what is the system to build like you know I did a talk at at um at data driven about ontologies whatever year year and a half ago or And I think you know there are a lot of people who think about ontologies in their own um uh data uh in their own repo and like those people who are like actively thinking not just how do I prompt a model but how do I build a system they start to build really good intuitions.

### Open-Sourcing the Behavior Spec Standard With Braintrust

**54:56** · So so uh we make sure to to to cover it before the end of the conversation. What is it exactly that um you're open sourcing with brand trust like walk us through the project where people find it uh the genesis of it why you partnering with brand trust specifically on this.

**55:12** · If we go back to the idea of of behaviors, right? Um the idea is that you can actually write down in markdown um uh what is a it is actually both a spec and a rubric. We call this specs and there were some people who asked isn't this a rubric and it is it's both.

**55:25** · Um and the reason it's both is because it is not just used to grade or potentially reward the agent. It's also used to align the humans. I think that is an underrated point um in that how you want the agent to behave as we talked about earlier is actually a subjective question. And so um uh internally it's it's you need to build processes to all agree on hey like this

**55:47** · is the product right how do you want the agent to behave going back to the example about you know the fast powerpoint verification and so um you want to standard to kind of write that down and the the project kind of came about because I was uh actually having coffee with the CEO of brain trust anker and I forget why honestly but I I was like I still tell you I was like I was explaining this concept to him I was talking about this because we were doing this internally and I thought it was very cool and he got pretty excited about it and um you know one thing that I had uh internally that we trying to

**56:18** · think about is we I think do a lot of really cutting edge work but it's not something we talk about much because to be honest we're working all the time.

**56:25** · Yeah.

**56:25** · Right before we started recording, you were showing uh some internal slacks between your co-founder Matt and and yourself. And uh if I may uh disclose them, like Matt was sending you uh a slack at 4:00 a.m. Uh and it was prompt refactors.

**56:40** · Yeah.

**56:40** · And that was last night. So it was a Sunday night as we were recording this and and you and you should have you were replying it to to that Slack at 6:00 a.m. So um Yes.

**56:50** · Yeah. 996 in full action amongst the co-founders of Basis.

**56:54** · Yes.

**56:54** · Yes. Yes, we we are um it's there's not there's no 996. It's for for for for for Matt and I. It's it's 247 for for the rest of the company. It's it's people work hard, but it's not a it's definitely not a not a 996. And so, you know, we we wanted to talk about it more and just share what we're doing. And we you know, we don't have a lot of resources to to like blast out uh to people.

**57:13** · And so uh uh we were talking I was like well I actually think this could be really good for you know useful for brain trust and honestly the whole industry because if you have a standard um that could be something that people define and can get automatically u you know slurped up into observability platforms, monitoring platforms and you know for people maybe who are less advanced it could also you know have out of the box judges or or you know ways to define hey here are the behaviors and you don't have to configure your own judge. You can actually get it get it to judge it for you and see and see the results. And so he he got pretty excited about that. And so that's where uh the collaboration came from.

**57:45** · So that that's what the open source repo has. It has, you know, a couple small examples. It has um an example judge that you can you can use. It has examples of actually written behaviors um that you can leverage uh and sort of build your own.

**57:57** · And I think I think the it is it is useful um to to think about how to adopt the standard. But I think it is also maybe more importantly thinking about how to adopt the mindset of you know not thinking that an agent operating over 10 hours is a black box. It's not. It has a lot a lot a lot of data and you're probably doing a disservice to your customers if you don't understand like how it's going about the work.

**58:18** · And what what would you want uh people to do with this open source project?

**58:22** · Presumably contribute to it, use it for their own purposes. Like how does this become an industry standard?

**58:28** · Yeah, it's a great question. I I don't actually know. I I think I think the coolest thing would be for people to contribute ideas to it. Um I think there's a lot of work left to do. I think it's just the beginning. I I mentioned a couple things earlier, but there's so much to do around one, how you make good judges.

**58:43** · Two, like how do you um properly label and uh dissect uh uh you know, trajectories to make it easier for judges to understand because at the current level of expense, you couldn't run this in all of production, for example, because it's you're running judges on every single, you know, trajectory. Um but there's a lot that can be done, I think, with uh building out the um uh the work that sits on top of the behaviors.

**59:07** · And I think also just seeing you know we purposely tried to make the standard relatively flexible similar to skills um where it is it is just a markdown like there's not an overfit hey and you need to have these exact five words like you can make it very broad and you can make it you know very specific um as long as you're as long as it is still self-contained to the to the point that a judge could look at the behavior and actually know like was the condition for it to be exhibited met and if so like did it get exhibited or did not get exhibited.

**59:36** · And as long as it has that, like there's a lot of leeway there. And so I think that's we wanted that to to to you know be flexible.

**59:45** · So what else should um AI builders think about as they build um autonomous long horizon agents. So we talked about judges. We talked about behavior. You just mentioned ontology which in your talk at datadriven NYC you had mentioned as well as a as a world for agents to to live in. Where where does that fit in the picture? Yeah, they're super important.

**1:00:06** · A lot of people when they see the word when they hear when they think about agents, their mental model always goes to coding agents because that's everyone's experience with at least the people who probably listen to this podcast like people think about coding agents a lot. Coding agents are interesting because they obviously have a harness that they get shipped in. They have certain tools. They have certain behaviors encoded in them in the in the context, right? You can codeex, by the way, is open source. I highly recommend people go look at the uh look at the open source repo. Um, but they don't control their runtime training data, right?

**1:00:38** · Because their runtime training data, which goes back to my analogy earlier, which is your context, is actually the repo they're working on.

**1:00:45** · And so you could have codeex, the same agent, quote unquote, on one codebase perform, you know, somewhat well, and then another codebase perform spectacularly because that codebase is has much better runtime training data, right? I.e. it has potentially, you know, good skills or good like, you know, um context about, you know, how to operate in the codebase because, uh there isn't like contradictions and confusions, whatever it is. And so, uh the the ontology of your codebase always mattered for engineers.

**1:01:14** · It matters just as much if not more for for really good agents over time. Um that actually I think goes up another level if you're thinking about non-coding agents because in coding you don't own the runtime training data. in non-coding you do

**1:01:29** · right like most of the data quote unquote that an agent sees when it's when it's a basis agent basis owns right it's training data that we have to ensure works really well and again when I say training data I mean like effectively handwritten context right or things that are part of your broader progressive disclosure some you know could be handwritten some could not be whatever it is and the because the agent

**1:01:52** · is always starting from scratch designing Maintaining that ontology in a way that is ergonomic for the agent is super key to building something that's long running. That's both like the data that is like maybe static like skills and whatnot that all the agents have, but also once you get the really long horizons if you're talking about, you know, a stateful agent that's maybe operating over months, days to months, now suddenly you have an ontology of going back to the momento example of information the agents left for itself, which if you're operating for maybe a couple hours could be a couple notes.

**1:02:21** · If you're operating for months, you're talking folders, right? And you have so much knowledge and context that describes like the lived experiences of the agent that like suddenly this new agent, well, new that is standing up with, you know, effectively very compacted context has to get it back into the state of mind of its entire lived experience. And so the ontology design to make it easy for it to do that. And the behaviors you encode that you know properly ensures it's doing that well are sort of the key to to to making it work really really well.

### Ontology Design: Virtual Filesystems, Graphs, Embeddings

**1:02:54** · What does that even mean designing an ontology? An ontology practically is what is it's a graph database. It's a series of relationships.

**1:03:01** · Yeah, it could be a lot of different it could be there are different formats. I think the the simplest way to think about it is honestly just a file system um uh in which you know you have like some structure. Obviously most people you do virtual file systems and so you have a lot of flexibility there. So there could be other types of metadata associated with the files and the folders, right? You you you there could be, you know, uh connectors uh in nodes and like some graph if you wanted.

**1:03:23** · Obviously there could also be embeddings like there's so many different you know sources of of data that you can get to like help enrich um uh and now by the way as models are getting cheaper and cheaper more and more of that actually can just be done um using inference instead of using determin like things like graphs or things like embeddings.

**1:03:40** · you know, if you have if Luna costs is free, then suddenly you could run Luna's across your entire ontology and summarize stuff for the agent up or things like that. Um, and so that that's kind of how I would think about it. And maybe also one more piece, it's not just the the ontology doesn't just mean the structure of the folders. And ontology traditionally, it's the it's also like the language, right? Like what are the objects and the concepts? Because at the end of the day, if you're being trained at runtime, you need to ensure you're not confusing concepts together and that like things kind of generally make sense. And so you're that's what I mean by defining the world, right?

**1:04:11** · You're you're defining uh what the agent can expect to to to uh uh to see as it goes and explores the kind of world around it.

### Canonical vs. Non-Canonical: Docs as Codebase

**1:04:20** · You mentioned somewhere that uh internal documentation for agents has to be treated like a code base. Yeah.

**1:04:26** · Delete a crucial paragraph and you break the agent just like deleting a line of code. Is that documentation uh something uh outside the ontology that the agent goes search like a tool call where how does that all work and what are the best practices?

**1:04:43** · Yeah, it's a good question. So just to quickly separate the just now when I was talking about the ontologies and like the historical I kind of was referring more to you know inside of like the basis product and like the kind of like production product in terms of like internal use of of agents like let's say coding agents um or maybe other internal agents that that we might make.

**1:04:59** · Um there it's kind of interesting because you're in depending on what you've set up your environment might be less controlled by your ontology because to your point you know in in the real world you have to go and access like linear and and gong and pylon and all these different things and so uh I think one of the keys for internal agents is having a very keen understanding of what is canonical versus what is not canonical.

**1:05:33** · And so just like if I'm a you know human who joins an organization, I could go and read all the gongs, but what is our sales strategy today? If you watch the gongs from two years, you'll get a lot of context, but you won't know what your current sales strategy is. There must be some canonical uh piece of documentation. In practice, a lot of times humans learn this by just like talking to people and you kind of learn stuff. But with agents, it's hard to get that.

**1:05:54** · And more importantly, if you want real organizational intelligence, you don't want an agent hearing one thing from one person, another thing from another person or having them have kind of different written records of like what is the current, you know, sales pitch or how do we, you know, make our decks or how do we make our emails. You need one canonical source. And that's why I think you know for for true agent native companies um especially in the future today I think it's still quite early but especially in the future having a clear understanding of what your company cannon is um and organizing that in an ontology that uh makes sense

**1:06:25** · and ensuring that that is like kept up to date just like code in some form um I think ends up becoming one of the most important parts of a humans inside of a company and within the basis teams you're hiring for jobs that quite literally did not exist two years ago like language architects or agent managers. Uh who are those people? What do they do? And what's a good background for them?

### Language Architects and Writing for Runtime Interpretation

**1:06:45** · Yeah, we need a lot of them. So, if you're listening and you want to join, please please like hit me up. Um uh great question. We're still figuring that out. \[laughter\] It's not it's not easy. Um here's what I know. You need I think this has probably gotten somewhat in vogue recently, but I think one thing, one skill that really matters is uh good systems thinking. And where does good systems thinking come from?

**1:07:11** · Um it comes from people who have had to uh think about some abstraction, some system, something and design in such a way that it performs in a like plethora of situations.

**1:07:28** · Um so obviously if you're a really good engineer like engineering is systems thinking now I think the majority of engineering historically has not been really systems thinking based you know it's been a little bit more executionoriented but if you think about like the the hardest engineering like hey I'm trying to design like what the system is going to look like or I'm trying to like you know create the right abstraction that really is high on systems thinking um but it's not the

**1:07:51** · only profession that's like that I um I think law actually is kind of like that you know in many ways I think about I think maybe the founding fathers would have been really good um context engineers or agent managers because you had to you had to write, \[clears throat\] you know, a piece of English that was going to be, you know, interpreted at runtime literally millions of times by lawyers and judges and whatnot.

**1:08:11** · And so if you're writing a law, and I don't mean like, you know, some politician, but if you're like actually trying to write a law and trying to write a well, you're trying to like somehow write something in English that will abstract at just the right level across the universe of situations.

**1:08:25** · And you have to have like theory of mind over the judicial system to think about like how they'll interpret it. It's like, you know, it's funny. You'll look in uh certain airports and you know, sometimes they'll have these signs. It's like, you know, don't bring a gun, don't bring a, you know, don't bring a sword, don't bring blah blah blah. And it's like you can list out 30 things to your point on brittle rules. And so, same thing, you can list out like 50 brittle rules or you can like write the right abstraction that somehow covers it just perfectly. Uh, so, so I think anything where you need to think in abstractions in that way, I think is good practice.

**1:08:55** · um for being a good um systems uh engineer. I think you know people who've had to manage like the most complex Excel models in the world is honestly not that dissimilar either. So I think there's a lot of potential potential backgrounds for it.

### Deployed Intelligence: 300 Alien Employees With No Context

**1:09:05** · I think at that driven when you spoke you were talking about your deployed intelligence team. Um and you were saying deploying agents at a firm uh was like on boarding 300 brilliant alien employees who have no context. Uh hence the deploy intelligence team. So what do those people do? still around or is that has that concept evolved?

**1:09:25** · No, no, of course the the DI team is is is awesome. I think to this day I shouldn't I need to go Google it, but uh I think we definitely came up with the term deployed intelligence. Um I know because if you Google it, we are the first company that that comes up. It's a cool name. Um I don't know if other people have taken on the name. I don't think it's actually caught on yet. But the idea is it's actually it's not FDES.

**1:09:46** · So it's not like engineers who are coming in and building something custom for you. Um, it's also not uh these kind of like agent PMs you see now at some companies that I won't name where it's like, you know, these like PMs quote unquote are kind of coming in and like building an agent sort of for you using an agent builder. It's actually neither of those.

**1:10:02** · Um it's uh it's people who uh have a deep empathy and understanding of the profession of like what it takes to put in place good process um and what it takes to be like successful when suddenly you can start to offload certain things to to agents right and so the DI team's job is to come work with our accounting firms to help them transition into this this new era, right?

**1:10:33** · We're giving them magic, but if we don't teach them how to leverage the magic, not just in the day-to-day, but how it changes the nature of the firm, how does it change uh what kind of business they can take on, who they hire, how can they like scale to be that firm of the future that that everyone wants to be. That's what the DI team works really closely with people um uh to do because it's it's not it wouldn't be fair to ask them uh to like go and you know, learn that themselves or do that themselves.

**1:10:57** · Instead, they bring a lot of the knowledge about their firm, about how things have worked, obviously their people, and we can combine that with our knowledge and how to deploy agents and I think together get to something where it can be a really really frontier accounting firm.

### Closing the Loop: Signal → Context, Tools, Harness

**1:11:10** · Speaking of frontier, maybe um as we start getting to the end of this conversation, I would love to spend a little bit of time on that. U you know, obviously big topic in 2026 is the concept of um self-improvement. Where does that fit um in in in your picture um at at basis and with autonomous agents? I think you talked about agents developing a a theory of mind about other agents. So at a system level paint that picture for us what does um self-improvement look like?

**1:11:41** · Yeah, we actually internally one of our um in the thread I talked about some of our research directions. One of our big research directions is how do you actually close the loop as we like to call it? um going from hey an agent you know made a mistake or not performing well or whatever to you know we've gone and and um uh improved the system uh to do that and uh I think that closing the loop is going to happen pretty fast. Um I I think you'll have like I don't know about the entire loop being closed but I think you'll be relatively close by end of year.

**1:12:12** · Um uh I think that so as agents are getting better theory of mind over themselves and therefore other agents you have two things happening. One is at runtime they're being better at orchestrating sub agents and also regulating their own environment for themselves. But it also means they're becoming better context engineers, right? They're becoming better harness engineers. Um, right now they are far far far worse at engineering agent systems than they are at engineering most software. Far worse.

**1:12:40** · Um, because by definition like that kind of work which is so novel has not seen a large amount in their in their training data. Um, and so they have very bad intuition.

### Context Slop: the Mistake Most Agent Builders Make

**1:12:52** · Actually, I think a lot of the mistakes a lot of agent builders make is, you know, they uh they have this weird intuition that like slop in your context or your agent is somehow more acceptable than slop in your code. And you'll see people like freaking out over, you know, uh uh uh a code file that isn't abstracted properly and yet their context is like total Uh which is hilarious because the context actually affects the performance at runtime. The organization of the code does not affect the performance at runtime.

**1:13:16** · And so um uh I think a lot of you know obviously because of like builtup uh behav you know behaviors a lot of engineers they they treat the the the code as more precious than the English when actually the English is more precious because the English affects the performance the code does not affect the performance right if the logic assuming the logic is the same it does not affect the performance and so um uh I think as agents get better

**1:13:43** · and they get better at this type of engineering of like how do you build agent systems um you'll start actually be able to close the loop because in order to close a loop, right, you need to take the signal that you are getting.

**1:13:53** · Um, and you need a lot of signal. One of the pieces of behavior, one of the points of behaviors is a way to get more signal. Whereas, if you only have outcome based eval, your signal is pretty sparse. So, how can you take all of that signal and actually now use it to uh improve your system, right? You proliferate it throughout throughout the system. and and that could be done by an agent that is like updating the context like changing the nature of the tool updating the harness etc.

**1:14:16** · And I think you'll pro in a way that is generalizable that doesn't overfit you can you can do it today if you want it to overfitit to like some signal but if you wanted to do it in a way that generalizes you you need uh the agents need to get a bit better still and there's some more work to do there.

### Reward Function Design and Credit Assignment Over Trajectories

**1:14:30** · What about self-improvement at uh the model level so I think you mentioned earlier that you guys don't do yet much reinforcement learning on the model itself. You've done you're doing mostly harness work if that's correct. Um but that's is that the next uh big bet to start doing uh actual reinforcement learning on u uh behavior adherance?

**1:14:54** · Yeah, it's a great question. The way I think about it is that the hard part of reinforcement learning is deciding what is your reward function and then deciding how you are going to allocate that reward over whatever whatever occurred right uh so we are that is like the active research uh that we are doing um because that's what behavior it's a source of signal right that you can use to craft into a reward function um same

**1:15:17** · with uh like some of the other kind of production monitoring work and and some of the like eval that you build and so deciding how to build good signal and doing the research and understanding what does it mean especially in a non-perfectly verifiable domain that's the work we're doing whether you take that signal and then like proliferate it through the weights you know through uh formal RL or you proliferate it through the harness through whatever you want to

**1:15:38** · call it like informal RL or like harness engineering um I think is like a separate question from the development of the signal but I think the development of the signal is really the hard part and that's the part that we're really focused on and today we don't go directly into the weights um and primarily the reason we don't do that is because uh a lot of the advancements the models are having when it comes to orchestrating themselves yield far more performance gains than uh benefits you'd have of like updating models directly.

**1:16:09** · Um I think that might as we'll see but but I think that's that's one of the reasons that you don't go to the weights yet. I do think that is a very interesting research direction as well that we'll start pursuing. And so um for us at that at our level at the kind of like applied application level that's the the kind of research that that we're doing. Um uh but but I suspect that in order for the models to actually do real work in the economy that's the only way you can get there.

**1:16:35** · I I don't believe that if you were to train a model, you know, and you scale up the amount of pre-trained comput and you scale up the amount of like post- training from like perfectly verifiable rewards that suddenly will output a model that um will do a tax return uh reliably. It might do one that's really good, but the question is not does it do really good, is that does it do it at the level of quality, reliability, scalability that would be expected from somebody operating with it. Do you worry about um the bit of lesson though that uh you mentioned earlier in this conversation?

### Will the Bitter Lesson Swallow the Harness?

**1:17:07** · Do do you think uh that uh all this work that you guys brilliantly and and others are doing at the harness uh level are going to be eventually swallowed up by the model.

**1:17:18** · Oh, I assume it will be swallowed up.

**1:17:19** · Yeah, I'm not worried about it. I I that is that is the that is absolutely the future. No. And in fact, if you look at the my thread, I as a hint to this, I I think I said uh the behaviors don't get shown to them to the agents yet. And the reason is because uh if you are truly bitter lesson, then in the future, this whole idea of like trying to context engineer it will just go away and you'll just specify, hey, I want these behaviors. It'll just work. Um and so I I definitely think it'll get swallowed up. No question. Um, I think that the how long it will take to get swallled up, I don't know exactly.

**1:17:50** · You know, I think it's probably sub five years. I don't think it's sub two years. Um, I think it's probably sub 5 years. And so for us, you know, we're in hypers scale mode. Like we we we can't we can't wait for the bitter lesson to arrive to like perform tax returns accurately. And so that's why I think that'll be one of the keys, you know, to um to doing it.

**1:18:09** · I do think that I don't know this is this is now total speculation but I I do suspect that maybe uh some types of process rewarding for this this type of work might end up being pretty important

**1:18:30** · you know uh for optimizing the compute that the labs even use over time um because I I I don't know if you want to move 37 like every single profession in the economy uh like we have a lot of learnings already and like there's kind of no reason to do that um would be my guess.

### Business Moats vs. Technical Moats

**1:18:46** · So do you think of um doing your own RL as some kind of mode against being swallowed up by model performance? I mean as as you think about applied AI companies of the future will will they all be RL labs of some sort? So generally, and if anyone's currently trying to found a company, I recommend thinking this way. Technical modes are not real modes.

**1:19:09** · Like I I I there's no portion of basis's long-term terminal value that stems from some, you know, secret RL trick we found that nobody else found. So that doesn't matter. Um uh what matters is that right now we are obviously very good at building long horizon agents um that you know can be reliable and deployed in production and we'll continue to be the best at that.

**1:19:31** · And that allows us to win market share and get deeply embedded. And that's why we move really fast because the work we're trying to do is to um uh go and proliferate maybe before like you get to AGI whatever you want to call that. So I think that at a most of the modes that will exist will be business modes. That is true in the AGI era. I would argue that's also been true in the pre-agi era.

**1:19:58** · Like I don't think that you know Salesforce can write a better SQL query than I can like the moat that Salesforce has is not related to their technology right it's related to their business position you know it's the it's the powers it's the it's the it's the the workflows that they own it's it's all the so many of these different things that come with being you know embedded in and that's what matters uh not the technology the technology is a is a temporary like dislodgement that allows

**1:20:24** · someone like us who obviously didn't exist you know three and a half years ago to now suddenly be able to do all this kind of work. I do think though for a long time maybe to your point that it it's not like it will be an total commodity because um just like you could have a bunch of genius humans doesn't mean that all the genius humans are equivalent in being able to do a tax return because at the end of the day there are certain things that you care about for for that that are subjective.

**1:20:52** · Um, and I do think that building up the competency of, you know, the work we're trying to do is actually really important for us to be able to deliver really good quality for, I think, a foreseeable future.

### Paradigm Thinking Over Timeline ADHD

**1:21:03** · All right, Mitch, it's been, uh, absolutely brilliant. um to close any advice for AI builders uh anybody like building agents today in addition to everything that you've talked about like the dos and don'ts and lessons learned and anything that comes to mind.

**1:21:19** · I think maybe the biggest lesson I would say is it's easy to look at the world and how fast things are changing and say like oh things are just you know one thing here one thing here is like you know ADHD on Twitter it's crazy you know the Chinese labs are released something every day and feel powerless to uh make first

**1:21:45** · principal decisions um whereas I actually think if you treat the new world as like an underlying paradigm shift you know in the same way that like I shift the cloud or something is you know some underlying paradigm shift and you try to extrapolate okay you have these things what does it mean you know if you know the intelligence became x better or if it didn't I think you'll build a lot more coherent systems and

**1:22:10** · make a lot better strategic bets both at like a technical and at a business level things are changing but it's not like the paradigm is changing um uh at least not that dramatically and so I think really understanding it is very very key for being able to like build in this in this world.

**1:22:25** · Mitch, it was absolutely fantastic.

**1:22:27** · Thank you so much for sharing all of this. Really appreciate it.

**1:22:29** · Of course. Thank you so much for having me.

**1:22:31** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks and see you on the next episode.