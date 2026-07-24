---
title: 'Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI'
source_url: https://www.youtube.com/watch?v=kwSVtQ7dziU
video_id: kwSVtQ7dziU
account: '[[accounts/no-priors-ai-machine-learning-tech-startups|No Priors: AI, Machine Learning, Tech, & Startups]]'
account_name: 'No Priors: AI, Machine Learning, Tech, & Startups'
account_url: https://www.youtube.com/@NoPriorsPodcast
featured_people:
- '[[people/andrej-karpathy|Andrej Karpathy]]'
published: 2026-03-20
created: 2026-07-23
language: en
speaker_attribution: contextual
description: What happens when AI agents can design experiments, collect data, and improve — without a human in the loop? Andrej Karpathy joins Sarah Guo on the state of models, the future of engineering and educa
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=kwSVtQ7dziU)

What happens when AI agents can design experiments, collect data, and improve — without a human in the loop? Andrej Karpathy joins Sarah Guo on the state of models, the future of engineering and education, thinking about impact on jobs, and his project AutoResearch: where agents close the loop on a piece of AI research (experimentation, training, and optimization, autonomously).  
  
00:00 Andrej Karpathy Introduction  
02:55 What Capability Limits Remain?  
06:15 What Mastery of Coding Agents Looks Like  
11:16 Second Order Effects of Natural Language Coding  
15:51 Why AutoResearch  
22:45 Relevant Skills in the AI Era  
28:25 Model Speciation  
32:30 Building More Collaboration Surfaces for Humans and AI  
37:28 Analysis of Jobs Market Data  
48:25 Open vs. Closed Source Models  
53:51 Autonomous Robotics  
1:00:59 MicroGPT and Agentic Education  
1:05:40 Conclusion

## Transcript

### Andrej Karpathy Introduction

**0:00** · Code's not even the right verb anymore, right? \[laughter\] But I have to express my will to my agents for 16 hours a day. Manifest. \[music\] How can I have not just a single session of Claude code or Codex or some of these agent harnesses? How can I have more of them? How can I do that appropriately?

**0:14** · The agent part is now taken for granted.

**0:16** · Now the claw-like entities are taken for granted and now you can have multiple of them and now you can have instructions to them and now you can have optimization over the instructions. But there \[laughter\] I mean this is why it gets to the psychosis is that this is like infinite and everything is a skill issue.

**0:34** · Hi listeners, welcome back to No Priors.

**0:37** · Today I'm here with Andre Karpathy and we have a wide-ranging conversation for you about code agents, the future of engineering and AI research, how more people can contribute to research, what's happening in robotics, his prediction for how agents can reach out \[music\] into the real world, and education in this next age. Welcome, Andre.

**0:56** · Andre, thanks for doing this. Yeah, thank you for having me.

**0:59** · Uh so it's been a very exciting couple of months in AI. Uh yeah, you could say that.

**1:03** · I remember um walking into the office at some point and you were like really locked in and I was asking what you were up to and you're like, I just I have to code for 16 hours a day or code's not even the right verb anymore, right? But I have to um express my will to my agents for 16 hours a day. Manifest um because like there's been a jump in capability.

**1:25** · Uh what's happening? Tell me about your experience. Yeah, I kind of feel like I was just in this perpetual I still am often in this state of AI psychosis just like all the time um because there was a huge unlock in what you can achieve as a person as an individual, right? Because you were bottlenecked by, you know, your typing speed and so on. But now with these agents it really, I would say in December is when it really just something flipped where I kind of went from 80/20 of like, you know, uh to like 20/80 of writing code by myself versus just delegating to agents. And I don't even think it's 20/80 by now. I think it's a lot more than that. I don't think I've typed like a line of code probably since December basically.

**1:59** · \[laughter\] Um which is like an extremely large uh change. Um I was talking to it like for example, I was talking about it to for example my parents and so on and I don't think like a normal person actually realizes that this happened or how dramatic it was. Like literally like if you just find a random software engineer or something like that at their at their desk and what they're doing, like their default workflow of, you know, building software is completely different as of basically December.

**2:24** · Uh so I'm just like in this state of psychosis of trying to figure out like what's possible, uh trying to push it to the limit. How is it how can I have not just a single session of, you know, um Claude code or Codex or some of these agent harnesses? How can I have more of them? How can I do that uh appropriately? And then how can I use these claws? What are these claws? Uh and uh so there's like a lot of new things. I want to be at the forefront of it, you know, and I'm very antsy that I'm not at the forefront of it and I see lots of people on Twitter doing all kinds of things and they all sound like really good ideas and I need to be at the forefront or I feel extremely nervous.

**2:54** · And so I guess I'm just in this psychosis of like what's possible like because it's unexplored fundamentally. Well, if you're nervous, the rest of us are are nervous. We have a we have a team that we work with at Conviction that their setup is everybody is like, you know, none of the engineers write code by hand and they they're all microphoned and they just like whisper to their agents all the time. It's the strangest work setting ever.

### What Capability Limits Remain?

**3:18** · Uh and I thought they were crazy and now I like I fully accept I was like, oh this was the way. Like you're just ahead of it.

**3:24** · Um what uh how do you think about your own capacity now to like explore or to do projects?

**3:30** · Like what is it limited by?

**3:32** · Yeah, what is it limited by? Uh just I think everything like so many things even if they don't work, I think to a large extent you feel like it's a skill issue. It's not that the capability is not there. It's that you just haven't found a way to string it together of what's available. Like I just don't I didn't give good enough instructions in the agents from the file or whatever it may be. I don't have a nice enough memory tool that I put in there or something like that. So it all kind of feels like skill issue when it doesn't work to some extent. You want to see how you can parallelize them etc. and you want to be Peter Steinberg basically. Uh so Peter is famous.

**4:01** · He has a funny photo where he's in front of a monitor with lots of uh like he uses Codex. So lots of Codex agents tiling the the monitor and they all take about 20 minutes if you prompt them correctly and use the high effort. And so they all take about 20 minutes. They have multiple, you know, 10 repos checked out. And so he's just um going between them and giving them work. It's just like you can you can you can move in much larger macro actions. It's not just like here's a line of code, here's a new function.

**4:27** · It's like here's a new functionality and delegate it to agent one. Here's a new functionality that's not going to interfere with the other one. Give it agent two. And then try to uh review their work as best as you can \[laughter\] depending on how much you care about that code. Like where are these macro actions that I can like manipulate my software repository by? And like another agent is doing some like research, another agent is writing code, another one is coming up with a plan for some new implementation. And so everything is just like happens in these like macro actions over your repository.

**4:51** · Um and you're just trying to become like really good at it and develop like a muscle memory for it is extremely um Yeah, it's very rewarding number one because it actually works. Uh but it's also kind of like the new thing to learn. So that's why hence the psychosis.

**5:07** · Yeah, I I do feel like my instinct is like whenever I'm waiting for an agent to complete something, the obvious thing to do is like, well, I can do more work, right? Like if I have access to more tokens then like I should just parallelize at tasks. And so that's that's very stressful because if you don't feel very bounded by your ability to spend on tokens, then you know, you are the bottleneck in the system that is max capability. Yeah, if you're not maximizing your subscription at least.

**5:33** · And ideally for multiple agents. Like if you run out of the quota on Codex, you should switch to Claude or whatnot. I don't know. Like that's what I've been trying to do a little bit and I feel nervous when I have subscription left over. That just means I haven't maximized my token throughput. So I actually kind of experienced this when I was a PhD student. You would feel nervous when your GPUs are not running.

**5:51** · Like you have GPU capability and you're not maximizing your the available flops to you. But now it's not about flops, it's about tokens. So what is your token throughput and what token throughput do you command? I would actually argue that it's very interesting that we had, you know, at least 10 years where in many engineering tasks people just did they didn't feel compute bound.

**6:11** · Right? Um and now the entire industry feels that now. They feel like they they they felt resource bound uh and now that you have this big capability jump, you're like, oh, actually it's not, you know, my ability to access the computer anymore. Like I'm I'm the binding constraint. Yeah, it's a skill issue. Which is very empowering cuz um yeah, cuz you could be getting better. So that's why that's why I think it's very addictive because there's unlocks when you when you get better.

### What Mastery of Coding Agents Looks Like

**6:36** · Where do you think it goes? Like if you just think about like, okay, you know, Andre's iterating and everybody else is for 16 hours a day getting better at using coding agents. Like what does it look like in a year?

**6:46** · Of like you've reached mastery.

**6:48** · \[laughter\] Yeah, what does mastery look like, right? At the end of the year or like two, three years, five years, 10 years, etc. Well, I think everyone is basically interested in like going up the stack. So I would say it's yeah, it's not about a single session with your agent.

**7:01** · Multiple agents, how do they collaborate and teams and so on. So everyone's trying to figure out what that looks like. And then I would say Claude is also kind of an interesting direction because it really, when I say a Claude, I mean this like layer that kind of takes persistence to a whole new level.

**7:13** · Like it's something that like keeps looping. It's it's like um it's not something that you are interactively in the middle of. It kind of like has its own little sandbox, its own little you know, it kind of like does stuff on your behalf even if you're not looking kind of thing.

**7:27** · Um and then also has like maybe more sophisticated memory systems etc. that are not yet implemented in agents. So um Open Claude has a lot more sophisticated memory I would say than what you would get by default uh which is just a memory compaction when your context runs out, right? You think that's the piece that resonated for more users versus like perhaps like broader tool access? For Open Claude? Yeah. Uh there's like I think there's at least five things that are really good ideas in here. Yeah, good job, Peter. I mean Peter has done a really amazing job. Um I saw him recently. Uh and I talked to him about it and I he's very humble about it.

**7:57** · But I think he innovated simultaneously in like five different ways and put it all together. Um so for example like the soul and D document. Like he actually really crafted a personality that is kind of compelling and interesting. And I feel like a lot of the current agents they don't get this correctly. I actually think a Claude has a pretty good personality. It feels like a teammate uh and it's excited with you etc.

**8:29** · I would say um for example Codex is a lot more dry um which is kind of interesting because \[laughter\] in it's true. You know, it doesn't it and the other thing I would say is for example with Claude I think they dialed the sycophancy fairly well where when Claude gives me praise, I do feel like I slightly deserve it because sometimes I kind of give it like not very well formed thoughts and uh I give it an idea that I don't think it's fully baked and it doesn't actually react very strongly.

**8:51** · It's like, oh yeah, we can implement that. But when it's a really good idea by my own account, it does uh seem to reward it a bit more. And so I kind of feel like I'm trying to like earn its praise which is really weird. And so I do think the personality matters a lot uh and I think a lot of the other uh tools maybe don't appreciate it as much.

**9:06** · And I think in this aspect also Peter really cares about this and so that was correct. And then the memory system and then uh just, you know, he's just having fun with this um and then the the single WhatsApp portal to all of the automation.

**9:17** · Yeah.

**9:17** · Is there something that you have done personally with your claws beyond software engineering that you think is fun or interesting? Yeah, so in January I had a claw I went through a period of claw psychosis. So I built um I have a claw basically that takes care of my home and I call him Dobby the elf uh claw.

**9:35** · Um and uh basically I used uh the agents to find all of the smart home subsystems of my home on the local area network which I was kind of surprised that it worked out of the box. Like I just told it that I think I have Sonos at home.

**9:47** · Like can you try to find it? And it goes and it did like IP scan of all of the um basically um computers on the local area network and and found the Sonos thing uh the Sonos uh, system and it turned out that there's no password protection or anything like that. It just logged in and it's like, "Oh, yeah, you have these Sonos systems installed. I Let me try to reverse engineer how it's working." It does some web searches and it finds like, "Okay, these are the API endpoints." And then it's like, "Do you want to try it?" And I'm like, "Whoa, like you just did that." And I'm like, "Yeah, can you try to play something in the study?" And, uh, it does and music comes out and I'm like, "I can't believe I just That's crazy. That's like three prompts. Yeah.

**10:19** · I can't believe I just typed in like, "Can you find my Sonos?" and then suddenly it's playing music. And it did the same for lights. And so like it kind of hacked in, figured out the whole thing, uh, created APIs, created dashboard so I could see the command, uh, kind of center of like all of my lights in the home. And then it was like switching lights on and off and, you know, so I can ask it like, "Dobby, it's sleepy time." And when it's sleepy time that just means all the lights go off, etc. and like so on. So it controls all of my lights, my HVAC, my shades, uh, the pool and, uh, the spa and also my security system.

**10:47** · So I have a camera pointed outside of the house and anytime someone rolls in I have a Quinn, uh, a Quinn, uh, model that looks at the videos. So first of all there's change detection. Right.

**10:58** · And then based on change detection it goes to Quinn and then it actually like tells me, um, it sends me a text to my WhatsApp. It shows an image from the outside and it says, "Hey, a FedEx truck just pulled up. FedEx truck just pulled up and you might want to check it and you got new mail or something like that." And Dobby just text me this. This is really incredible. Um, so so Dobby is in charge of the house. I text through with it through WhatsApp, um, and it's been like really fun to have these macro actions that maintain my house.

### Second Order Effects of Natural Language Coding

**11:24** · I haven't like really pushed it, uh, like way more beyond that and I think people are doing a lot more crazy things with it, uh, but for me even just the home automation setup I used to use like six apps, uh, completely different apps and I don't have to use these apps anymore. Like Dobby controls everything in natural language. It's amazing. Um, and so I think like I haven't even pushed the paradigm fully but already that is so helpful and so inspiring I would say. Do you think that's indicative of like what people want from a user experience perspective with software, right? Because I I don't think, you know, it's pretty ignored that it takes humans effort to like learn new software, like new UI. Yeah. I think, uh, to some extent that's right.

**11:59** · It's like working backwards from how people think an AI should be because what people have in their mind of like what an AI is is not actually what an LLM is by by like in the raw sense. Like LLM is a token generator, you know, like more tokens come out. But what they think of is like this this persona identity that they can tell stuff and it remembers it, you know?

**12:18** · And, uh, it's just kind of an entity behind the WhatsApp. It's like a lot more understandable. Mhm. Uh, so I think to some extent it's like matching the expectations that humans already have for what an AI should behave but under the hood it's like a lot of technical details go into that. And LLMs are too raw of a primitive, uh, to actually, um, type check as AI I think for most people if that makes sense. Yeah. Um, I think that's like how we understand what the AI is and like the, um, description of it as Dobby or some persona obviously resonates with people.

**12:46** · Um, I also think that it it uh, the unification that you did across your six different software systems for your home automation speaks to a different question of like do people really want all of the software that we have today? Yeah.

**12:59** · Right? Um, because I I would argue like, well, you have the hardware but you've now thrown away the software or the UX layer of it. Um, do you think that's what people want? Yeah, I think there's this like there's this sense that these apps that are on the app store for using these smart home devices, etc. Uh, these shouldn't even exist kind of in a certain sense. Like shouldn't it just be APIs and shouldn't agents be just using it directly? And, um, wouldn't it like I can do all kinds of home automation stuff that, uh, in any individual app will not be able to do, right?

**13:28** · Um, and an LLM can actually drive the tools and call all the right tools and do uh, do pretty complicated things. Um, and so in a certain sense it does point to this like maybe there's like an overproduction of lots of custom bespoke apps that shouldn't exist because agents kind of like crumble them up and everything should be a lot more just like exposed API endpoints and agents are the glue of the intelligence that actually like tool calls all the all the parts. Um, another example is like my treadmill.

**13:55** · Uh, there's an app for my treadmill and I wanted to like keep track of how often I do my cardio, uh, but like I don't want to like log into web UI and go through a flow and etc.

**14:04** · Like all this should just be like make APIs available and this is kind of, you know, going towards the agentic, um, sort of web or like agent first, uh, tools and all this kind of stuff. So I think the industry just has to reconfigure in so many ways that's like the customer is not the human anymore.

**14:18** · It's like agents who are acting on behalf of humans and this refactoring will be will probably be substantial in a certain sense. One way that people sometimes push back on this is like, do people Do you Do we expect people to write code some of these tools? Do we expect normal people to do this kind of stuff that I described? Mhm. But I think to some extent this is just, you know, technology as it exists today and right now there is some write coding and I'm actually watching it and I'm working with the system but I kind of feel like this kind of stuff that I just talked about this should be free like in a year or two or three.

**14:47** · There's no write coding involved. This is trivial. This is table stakes. This is like any AI, even the open source models, etc. can like do this. You should be able to translate it from a less technical humans intent very easily to this outcome.

**15:00** · Yeah.

**15:00** · Today it's write coding and it's involved and not many people are going to do it but And you still have to make some design decisions, right? We were talking about like we take frames for example. Yeah.

**15:07** · Yeah. But I kind of feel like this will just, uh, start to the barrier will just come down and it's just ephemeral software on your behalf and some kind of like claw is handling all the details for you but you're not involved. Claw has a Claw has a machine and it will figure it out and it's just presenting you UIs and you're like saying stuff, you know? Mhm.

**15:26** · Why haven't you, um, I guess like pushed the boundaries of what you can do personally with claws? Like is it, you know, you're focusing on more important projects, auto research, etc. or, uh, you're climbing the hill to mastery or something else, right? Yeah, I just feel like I'm so distracted by everything so I spend I \[laughter\] spend like a week on the claw stuff and I I have more to do almost, um, but I will say that, um, It's like Jensen told us we're all just busier, unfortunately.

### Why AutoResearch

**15:53** · Uh, I didn't really take advantage of a lot of like email and calendar and all this other stuff and I didn't really have access cuz I'm still a little bit like suspicious and it's still very new and rough around the edges. So I didn't want to give it like full access to my digital life yet and part of it is just the security, privacy and uh, just being very cautious in that in that realm.

**16:11** · And, um, so some of it is like held back by that I would say. Yeah, maybe that's like the dominant dominant feature but some of it is also just I feel so distracted because I feel like I had a week of claw and then other stuff is happening and What was the, um, I mean you've talked about like being able to train or at least optimize a uh, a a model as a task you want to see agents do for a long time. Like what was the motivation behind auto research? Auto research, yeah.

**16:34** · So I think like I had a tweet earlier where I kind of like said something along the lines of to get the most out of the tools that have become available now you have to remove yourself as the as the bottleneck. You can't be there to prompt the next thing. You're You need to take yourself outside. Um, you have to arrange things such that they're completely autonomous. And the more you you know, how can you maximize your token throughput and not be in the loop?

**16:56** · This is the this is the goal. And so I kind of mentioned that the the name of the game now is to increase your leverage. Uh, I put in just very few tokens just once in a while and a huge amount of stuff happens on my behalf.

**17:06** · And so auto research like I tweeted that and I think people liked it and whatnot but it they haven't like maybe worked through like the implications of that and for me auto research is an example of like an implication of that. Where it's like I don't want to be like the researcher in loop like looking at results, etc. Like I'm I'm holding the system back. So the question is how do I refactor all the abstractions so that I'm not I have to arrange it once and hit go. The name of the game is how can you get more agents running for longer periods of time without your involvement doing stuff on your behalf?

**17:33** · And auto research is just, yeah, here's an objective, here's a metric, here's your boundaries of what you can and cannot do.

**17:39** · And go.

**17:41** · And, uh, yeah, it worked.

**17:43** · at its effectiveness. Yeah, I I didn't expect, uh, it to work because so I have the project data chat, um, and fundamentally like I think a lot of people are very confused with my obsession for like training GPT-2 models and so on. But for me, uh, training GPT models and so on is just a little harness, a little playground for training LLMs. And fundamentally what I'm more interested in is like this idea of recursive self-improvement and to what extent you can actually have LLMs improving LLMs because I think all the frontier labs this is like the thing Mhm. uh, for obvious reasons and they're all trying to recursively self-improve roughly speaking.

**18:12** · And so for me this is kind of like, um, a little playpen of that. Um, and I guess I like tuned Nan Chat already quite a bit by hand in the good old fashion way that I'm used to.

**18:21** · Like I'm a researcher. I've done this for like, you know, two decades. I have some amount of like What is the opposite of hubris? Uh, yeah. \[laughter\] Earned confidence? Okay. I have like two decades of like, "Oh, I've trained this model like thousands of times. I've like, um, so I've done a bunch of experiments.

**18:36** · I've done hyperparameter tuning. I've done all the things I'm very used to and I've done for two decades. Yeah. And I've gotten to a certain point and I thought it was like fairly well tuned and then I let auto research go for like overnight and it came back with like tunings that I didn't see. Mhm. And yeah, I did forget like the weight decay on the value embeddings and my Adam betas were not sufficiently tuned and these things just jointly interact. So like once you tune one thing the other things have to potentially change too.

**18:58** · You know, I shouldn't be a bottleneck. I shouldn't be running these hyperparameter optimizations. I shouldn't be looking at the results. There's objective criteria in this case.

**19:05** · Uh, so you just let you just have to arrange it so that it can just go forever. So that's a single sort of version of auto research of like a single loop trying to improve. And I was surprised that it, um, it found these things that I you know, the repo was already fairly well tuned and still found something.

**19:19** · And that's just a single it's a single loop. Like these frontier labs they have GPU clusters of tens of thousands of them.

**19:26** · And so it's very easy to imagine how you would basically get a lot of this automation on, um, smaller models. And fundamentally everything around like frontier level intelligence is about extrapolation and scaling loss. And so you basically do a ton of the exploration on the smaller models and then you try to, um, extrapolate out. So you're saying our research efforts are going to get more efficient. Like we're going to have better direction for when we scale as well if we can do this experimentation better.

**19:50** · Yeah, I would say that like the most interesting project and probably what the frontier labs are working on is uh, Mhm. Yeah. you know, you experiment on the smaller models. You try to make it as autonomous as possible. Remove researchers \[laughter\] from the loop. They have way too much What is the What is the opposite of too much confidence? Yeah, yeah, they don't know. They shouldn't be touching any of this really. And so you have to like rewrite the whole thing because right now, I mean certainly they can contribute ideas. But okay, they shouldn't actually be enacting these ideas.

**20:15** · There is a queue of ideas and there's maybe an automated scientist that comes up with ideas based on all the archive papers and GitHub repos and it funnels ideas in or researchers can contribute ideas, but it's a single queue and there is workers that pull items and they try them out. And whatever works just gets sort of put on the feature branch and maybe some people like monitor the feature branch and merge to the main branch sometimes.

**20:37** · So yeah, just removing humans from all the processes and automating as much as possible and getting high token tokens per second throughputs and it does require rethinking of all the abstractions and everything has to be reshuffled. So yeah, I think it's very exciting. If we take one more recursive step here, when is the model going to write a better program MD than you?

**21:00** · Yeah.

**21:01** · Also program MD is like loop. Yeah, exactly.

**21:05** · Yeah.

**21:05** · So program MD is my crappy attempt at describing like how the auto researcher should work. Like oh, do this then do that and that and then try these kinds of ideas and then here's maybe some ideas like look at architecture, look at optimizer, etc. But I just came up with with this in markdown, right?

**21:19** · Mhm.

**21:21** · And so yeah, exactly. You want some kind of an auto research loop maybe that looks for You can imagine that different program that MDs would would give you different progress. So you basically every research organization is described by program MD. A research organization is a set of markdown files that describe all the roles and how the whole thing connects.

**21:43** · And you can imagine having a better research organization. So maybe they do fewer stand-ups in the morning because they're useless. And this is all just code, right?

**21:51** · And so you can So one organization can have fewer stand-ups, one organization can have more.

**21:56** · One organization can be very risk-taking, one organization can be less. As you can definitely imagine that you have multiple research orgs and then they all have code. And once you have code, then you can imagine tuning the code. So 100% there's like the metal layer of it. Uh Did you see my text about my contest idea? My contest idea was like let people write different program MDs, right? And and so for same hardware, where do you get most improvement?

**22:22** · Oh, I see. And then you can take all that data and then give it to the model and say write a better program MD.

**22:26** · Yes, yes.

**22:28** · Yeah, exactly.

**22:28** · We're going to get something better.

**22:29** · Like there's no way we don't, right?

**22:30** · 100% look at where the improvements came from and like can I change the program MD such that more of these kinds of things would be done or like things that didn't work except you can 100% imagine doing that. So I think this is a great idea, but it's like you know, I think like you can sort of go one step at a time where you sort of have one process and then second process and then the next process and these are all layers of an onion.

### Relevant Skills in the AI Era

**22:53** · Like the LLM sort of part is now taken for granted. The agent part is now taken for granted. Now the claw-like entities are taken for granted and now you can have multiple of them and now you can have instructions to them and now you can have optimization over the instructions and it's just like a little too much, you know, but I mean this is why it gets to the psychosis is that this is like infinite and everything is scale issue and that's why I feel like Yeah, that's just coming back to This is why it's so insane.

**23:14** · Okay, well, if \[laughter\] we're we're just trying to like diagnose the current moment and what is a relevant skill right now, what do you like what do you think is the implication that this that this is the loop we should be trying to achieve in different areas and then it works, right? Like you know, remove create the metric or create the ability for agents to continue working on it without you. Do we still have performance engineering? Like what Yeah, I mean so there's a few caveats that I would put on top of the LLM psychosis.

**23:43** · So number one, this is extremely well suited to anything that has objective metrics that are easy to evaluate. So for example, like writing kernels for more efficient CUDA, you know, code for various parts of the model, etc. are a perfect fit because you have inefficient code and then you want efficient code that has the exact same behavior but it's much faster.

**24:02** · Perfect fit. So a lot of things like like are perfect fit for auto research, but many things will not be. And so they it's just if you can't evaluate then you can't auto research it, right?

**24:12** · So that's like caveat number one. And then maybe caveat number two I would say is you know, we're we're kind of talking about the next steps and we kind of see what the next steps are, but fundamentally the the whole thing still doesn't it still kind of like bursting at the seams a little bit and there's cracks and it doesn't fully work and if you kind of try to go too far ahead, the whole thing is actually net not useful if that makes sense.

**24:31** · Because these models like still are not, you know, they've improved a lot, but they're still are like rough around the edges is maybe the way I would describe it. I simultaneously feel like I'm talking to an extremely brilliant PhD student who's been like a systems programmer for their entire life and a 10-year-old. And it's so weird because humans like there's like I feel like they're a lot more coupled like you have to you know, um Yes, you wouldn't you wouldn't encounter that combination.

**24:54** · This jaggedness is really strange and humans have a lot less of that kind of jaggedness, although they definitely have some.

**24:59** · \[laughter\] But humans have a lot more jaggedness.

**25:02** · Uh sorry, the agents have a lot more jaggedness where sometimes like you know, I ask for functionality and it like comes back with something that's just like totally wrong and then we get into loops that are totally wrong and then I'm just I get so frustrated with the agents all the time still because you feel the power of it, but you also there's still like it does not say statistical things once in a while for me as well. I get very annoyed \[clears throat\] when I feel like the agent wasted a lot of compute on something it should have recognized was an obvious problem. Yeah.

**25:33** · I think like some of the bigger things is like maybe what's under underneath it if I could hypothesize is fundamentally these models are trained via reinforcement learning. So they're actually struggling with the exact same thing we just talked about which is the labs can improve the models in anything that is verifiable or that \[clears throat\] has rewards. So did you write the program correctly and does it you do you the unit tests check out? Yes or no. But some of the things where they're struggling is like for example, I think they have a tough time with like nuance of maybe what I what I had in mind or what I intended and when to ask clarifying questions.

**26:02** · Um or like what I Yeah, it's just um anything that feels softer is like worse. And so you're kind of like you're either on rails and you're part of the super intelligence circuits or you're not on rails and you're outside of the verifiable domains and suddenly everything kind of just like meanders.

**26:17** · Like maybe another way to put it is if you go to if today if you go to like state-of-the-art model, ChatGPT and you ask it tell me a joke, um do you know what joke you're going to get? There's the joke. The joke? I do feel I I I can't tell you like the you know, standard form of it, but I do feel like ChatGPT has like three jokes.

**26:34** · Yeah, yeah. So the the joke that apparently all the LLMs like love the most is why do scientists not trust atoms? Okay. Because they make everything up. Okay.

**26:44** · They make everything up.

**26:45** · So this is still emerge? So this is the joke you would get like three or four years ago and this is the joke you still get today.

**26:51** · Okay.

**26:52** · So even though the models have improved tremendously and if you give them an agentic task, they will just go for hours and move mountains for you. And then you ask for like a joke and it has a stupid joke. It's crappy joke from five years ago and it's because it's outside of the it's outside of the RL.

**27:08** · It's outside of the reinforcement learning. It's outside of what's being improved. It's like and it's part of the jaggedness of like shouldn't you expect models as they get better to also have like better jokes or more diversity of them or it's just it's not being optimized and stuck. Do you think that that implies that we are not seeing like generalization in the sense of like broader intelligence of joke smartness being attached to code smartness?

**27:34** · Yeah, I think there's some decoupling where some things are verifiable and some things are not and some things are optimized for arbitrarily by the labs depending on like what data went in and some things are not and um and But I mean the the premise there's a you know, premise from some research groups that if you're smarter at code generation or in these verifiable fields, you should be better at everything. And like the the joke situation suggests that that's not happening at all.

**28:01** · Okay.

**28:01** · Yeah, I don't think that's happening. I think I think maybe we're seeing like a little bit of that, but not like a satisfying amount.

**28:06** · Yeah, that jaggedness exists in humans.

**28:09** · You \[laughter\] can be very very good at math and still tell really bad jokes.

**28:13** · Yeah, that's true. Yeah, but it just it still means that we're not getting like the story is that we're getting a lot of the intelligence and capabilities in all the domains of society like for free as we get better and better models and that's not like exactly fundamentally what's going on and there's some blind spots and some things are not being optimized for and this is all clustered up in these neural net opaque models, right? So you're either on rails of what it was trained for and everything is like you're going at speed of light or you're not.

### Model Speciation

**28:39** · And so it's the jaggedness. So um So that's why I think like even though the the progression is obvious what should happen, you can't let it fully go there yet because it doesn't fully work or it's a scale issue and we just haven't like figured out how to use it. So you know, it's hard to tell. Can I ask a somewhat blasphemous question which is like if this jaggedness is persisting and it's all rolled up in a at least monolithic interface, right?

**29:05** · But you know, single model.

**29:08** · Does that make sense or do you should should it be unbundled into things that are can be optimized and improved against different domains of intelligence? Like unbundling the models into multiple experts in different areas, etc. More directly. Yeah. Um Instead of just MOE that we have no exposure to because that can be like confusing as a user from the outside which is like why is it so good at this, but not at this other thing?

**29:29** · Yeah, I think currently my impression is the labs are trying to have a single sort of like monoculture of a model that is arbitrarily intelligent in all these different domains and they just stuff it into the parameters. I do think that we will we I do think we should expect more speciation in the intelligences.

**29:48** · Um like, you know, the animal kingdom is extremely diverse in the brains that exist and there's lots of different niches of of nature and some animals have overdeveloped visual cortex or other part kind of parts and I think we we should be able to see more speciation and um you don't need like this oracle that knows everything.

**30:04** · You can speciate it and then you put it on a specific task and we should be seeing some of that because you should be able to have like much smaller models that still have the cognitive core like they're still competent but then they specialize and then um and then they they can become more efficient in terms of latency or throughput on specific tasks that you really care about. Like if you're a mathematician working in Lean, I saw for example there's a few releases that really like target that as a domain. Um uh so there's a probably going to be a few examples like that where the unbundling kind of makes sense.

**30:31** · One question I have is whether or not the capacity constraint on available compute infrastructure Mhm. drives more of this because efficiency Yeah. actually matters more. Yeah.

**30:45** · Your if you financing aside, though financing's involved in all of this. If you have access to full compute for anything you do like even one single model, right?

**30:55** · But if you actually feel pressure where you're like I can't serve Mhm. um model of massive size for every use case.

**31:03** · Mhm.

**31:03** · Like do you think that leads to any speciation? Does that question make sense to you? The question makes sense and I guess like what I'm what I'm what I what I'm struggling with is I don't think we've seen too much speciation just yet, right? No. Uh we're seeing a monoculture of models. Yeah. So um And there's like clearly pressure for like make a good code model, put it back in the main, merge again. Yeah.

**31:23** · Um even though there already is pressure on the models. Mhm. I guess perhaps I I feel like there's a lot of very short-term supply crunch and like maybe that causes more speciation now.

**31:35** · Yeah, I think fundamentally like the the the labs are serving a model and they don't really know what the end user is going to be asking about. So maybe that's like some part of it because they kind of have to multitask over all the possible things they could be asked. But I think if you're coming to a business and maybe partnering on some specific problems you care about then maybe you would see that there. Um or there would be some very high-value applications that are like more niche. Um But but I think right now they're kind of like going after the totality of what's available. I don't think that the science of manipulating the brains is like fully developed yet partly.

**32:05** · What do you mean manipulating? So like so fine-tuning without losing capabilities as an example. And I we don't have these primitives for actually like working with the intelligences in ways other than just context windows. Our context windows kind of just just work and it's very cheap to manipulate etc. And this is how we're getting some of the customization etc. Uh but I think if it was I think it's a it's a bit more of a developing science of how you like more deeply adjust the models, how you have continual learning maybe or how you um how you fine-tune in a certain area, how you get better in a certain area or like how you actually touch the weights not just the context windows.

### Building More Collaboration Surfaces for Humans and AI

**32:36** · And so it's a lot more tricky I would say to touch the weights than just the context windows uh because you're actually fundamentally changing the full model and potentially its intelligence. And so um so maybe it's just like not a fully developed science if that makes sense of speciation. And it also has to be like cheap enough Yeah. for that speciation to be worthwhile in these given contexts. Can I ask a question about like an extension to auto research that you described in terms of open ground?

**33:04** · You say okay, well, you know, we have this thing. Um we need more collaboration surface around it essentially for people to contribute to research overall. Can you talk about that?

**33:15** · Yeah, so we talked about auto research has a single thread of like I'm going to try stuff in a loop but fundamentally the parallelization of this is like the interesting component.

**33:23** · And I guess I was trying to like play around with a few ideas but I don't have anything that like clicks as simply as like I don't have something I'm like super happy with just yet but it's something I'm like working on the side when I'm not working on my claw.

**33:34** · Um so I think like one issue is if you have a bunch of nodes of parallelization available to then it's very easy to just have multiple auto researchers talking through a a common system or something like that.

**33:46** · What I was more interested in is how you can have an untrusted pool of workers out there on the internet. Mhm. So for example in auto research you're just trying to find um the piece of code that trains a model to a very low validation loss.

**34:00** · If anyone gives you a candidate commit, it's very easy to verify that that commit is correct is good. Like they someone could claim from the internet that this piece of code will optimize much better and give you much better performance. You could just check. Yeah. But probably a lot of work goes into that checking.

**34:16** · But fundamentally they could lie and etc. So you're basically dealing with a similar kind of it's almost actually like looks a little bit like my my designs that incorporate an untrusted pool of workers actually look a little bit more like a blockchain a little bit uh because instead of blocks you have commits and these commits can build on each other and they contain like changes to the code as you're improving it. Um and uh the proof of work is basically doing tons of experimentation to find the commits that work.

**34:40** · Um and that's hard and then the reward is just being on the leaderboard right now. There's no monetary reward whatsoever.

**34:47** · Uh but I don't want to push the analogy too far but it fundamentally has this issue where you a huge amount of search goes into it but it's very cheap to verify that a candidate solution is indeed good because you can just train a single you know, someone had to try 10,000 ideas but you just have to check that the thing that they produced actually works because the 99,000 of them didn't work, you know? Um and so basically long story short is like you have to come up with a system where an untrusted pool of workers can collaborate with a trusted pool of workers that do the verification.

**35:18** · And the whole thing is kind of like asynchronous and works and and so on and it's it's like safe from a security perspective because if anyone sends you arbitrary code and you're going to run it, that is very sketchy and dodgy. So um but fundamentally it should be totally possible. So you're familiar with projects like SETI@home and Folding@home. All of these problems have a similar kind of setup. So Folding@home you're folding a protein and it's very hard to find a configuration that is low energy. But if someone finds a configuration that they value to be low energy, that's perfect.

**35:45** · You can just use it. You can easily verify it.

**35:47** · So a lot of things have this property that you know, very expensive to come up with but very cheap to verify. And so in all those cases things like Folding@home or SETI@home or auto research at home will be good fits. And so um long story short a swarm of agents on the internet could collaborate to improve LLMs and could potentially even like run circles around frontier labs. Like who knows, you know?

**36:09** · Um yeah, like maybe that's even possible. Like frontier labs have a huge amount of trusted compute but the earth is much bigger and has huge amount of untrusted compute. But if you put systems in check systems in place that you know, deal with this then maybe it is possible that the swarm out there could could come up with with better with better solutions.

**36:29** · And people kind of like contribute cycles um to to a thing that they care about. And so sorry to so the last thought is uh lots of companies or whatnot they could maybe have like their own things that they care about and you if you have compute capacity you could contribute to different kind of auto research tracks.

**36:44** · Like maybe you care about certain you know, like you care about like cancer or something like that of certain type. You don't have to just donate money to an institution. You actually could like purchase compute and then you could join the auto research swarm for that project, you know? Uh so if everything is rebundled into auto researchers then compute becomes the thing that you're contributing to the pool. Yeah. That's very inspiring and it's also interesting.

**37:04** · Like I don't I don't know how far this goes but it is interesting that at least some audience of people you know, here in Silicon Valley or lining up at you know, retail stores in China have discovered that like having access to personal compute is interesting again.

**37:20** · Yeah. Right? So maybe they're really motivated to do that for their claws and then they can contribute to auto research.

**37:25** · almost like dollars the thing everyone cares about but is flop the thing that actually everyone cares about in the future? Like is there going to be like a flipening almost of like what's the thing that you care about? Like right now for example it's really hard to get compute even if you have money. Yeah.

### Analysis of Jobs Market Data

**37:38** · So actually it almost seems like the flop is like dominant \[laughter\] in a certain sense. Um Yeah, so so maybe that's kind of like that. Kind of like that. Like how much how many flops do you control instead of like what wealth you control? I don't actually think that's true but it's kind of interesting to think about. The last thing you released was like a little bit of jobs data analysis. Is that right?

**37:58** · What and might have touched a nerve even though you're just like visualizing some public data.

**38:03** · Yeah.

**38:03** · Uh what was you know, what were you curious about? Yeah, I guess I was curious to um I mean everyone is like really it's everyone is really thinking about the impacts of AI on the job market and what's going to look like. So I was just interested to take a look like what does the job market look like? Where are the different roles um and how many people are in different professions? And I was like really just interested to like look through the individual cases and try to think myself about like you know, with these AIs and how they're likely to evolve like are these going to be tools that people are using? Are these going to be displacing tools for these professions?

**38:36** · And like what are the current professions and how are they going to change? Are they going to grow or uh adjust to a large extent or like what could be new professions? So it's really just like a way to fuel my own chain of thought about the industry I suppose.

**38:47** · Mhm. Um and so yeah, the jobs data basically is just a Bureau of Labor Statistics. They actually have um percent outlook for each profession about how much it's expected to grow over the next I think almost a decade. Uh yeah, I think it's a decade but it was made in 2024. Mhm. We need a lot of health care workers. Yeah.

**39:04** · So so they've already made those projections and I'm not sure actually 100% what the methodology was that they they put into their projections. Um I guess I was interested to color things by like if people think that what's like primarily being developed now is this kind of like more digital AI that is kind of like almost like these ghosts or spirit entities that can like interact in the digital world and manipulate a lot of like digital information and they currently don't really have a physical embodiment or presence. And the physical stuff is probably going to go slightly slower because you're manipulating atoms.

**39:32** · So flipping flipping bits and and the ability to copy-paste digital information is like makes everything a million times faster than accelerating matter, you know, so Um so energetically, I just think we're going to see a huge amount of activity in the digital space, huge amount of rewriting, huge amount of activity, boiling soup. And I think the we're going to see something that in the digital space goes at the speed of light compared to I think what's going to happen in the physical world to some extent. If it would be the extrapolation.

**39:58** · And so I think like \[clears throat\] there's currently kind of like I think overhang where there can be like a lot of unhubbling almost potentially of like a lot of digital information processing that used to be done by computers and people. And now with AIs there's like a third kind of manipulator of digital information. There's going to be a lot of refactoring in those in those disciplines.

**40:19** · Um but the physical world is actually going to be like I think behind that by some amount of time. And so I think what's really fascinating to me is like So that's why I was highlighting the the professions that fundamentally manipulate digital information. This is work you could do from your home, etc.

**40:33** · Uh because I feel like those will be like things will change. And it doesn't mean that there's going to be less of those jobs or more of those jobs because it does has to do with like demand elasticity and many other factors. But things will change in these professions because of these new tools and um because of this upgrade to the nervous system of the human superorganism \[laughter\] if you want to think about it that way.

**40:52** · Given the look you had at the data, do you have either any observations or um uh guidance for people facing the job market or thinking about what to study now or what skills to develop? I mean we can all go get like I'm very thankful that I have to like meet people for my job right now.

**41:07** · Yeah.

**41:08** · \[laughter\] Yeah, more physical. Yeah. Could you do your work from home though? I could.

**41:13** · I think there are relationship parts of it that are hard, but most of it I could. Yeah. I think it's really hard to tell because again like the job market is extremely diverse. I think the answers will probably vary, but uh to a large extent like these tools are extremely new, extremely powerful. And so just being you know, just trying to keep up with it is like the first thing.

**41:28** · Um and um yeah, because I think a lot of people kind of like dismiss it or Or they're afraid of it. Or they're afraid of it, etc. As which is totally understandable, of course. Yeah, I think like um it's fundamentally an empowering tool at the moment. Um and these jobs are bundles of tasks. And some of these tasks can go a lot faster. And so people should think of it as primarily a tool that it is right now.

**41:48** · Um and I think the long-term future of that is uncertain. Yeah, it's kind of really hard to forecast, to be honest. And like I'm not professionally like doing that really. And I think this is a job of like economists to do properly. You are an engineer though. And like one thing I thought was interesting is that like the demand for engineering jobs is continuing to increase.

**42:08** · Yeah.

**42:08** · Um I I can't tell if that's like a temporary phenomenon. I'm not sure how I feel about it. Yeah, do you know? Yeah, that's like the demand elasticity almost like uh software was scarce, right? And so the reason we don't have more demand for software is just there's its scarcity and it's too expensive.

**42:22** · So if the barrier comes down, then actually you have the Jevons paradox, which is like you know, you actually the demand for software actually goes up.

**42:27** · It's cheaper and there's more More powerful, yeah. The the classical example of this always is the ATMs and the bank tellers uh because there was a lot of like fear that um ATMs and computers basically uh would displace tellers. But what happened is they made like the cost of operation of of a bank branch much cheaper. And so there are more bank branches, so there are more tellers. It's like the canonical example people cite. Uh but basically it's just Jevons paradox. Like something becomes cheaper, so there's a lot of unlocked demand for it.

**42:55** · Uh so I do think that that's probably I do have like cautiously optimistic view of this in software engineering where I do think um it does seem to me like the demand for software will be extremely large. Um and it's just become a lot cheaper. And um so I do think that for quite some time um it's very hard to forecast, but it does seem to me like right now at least locally there's going to be more demand for software.

**43:20** · Um because software is amazing. It's like you know, digital information processing. You're not forced to use like arbitrary tools that were given to you. They're imperfect in various ways. You're not forced to subscribe to what exists. Code is now ephemeral and it can change and it can be modified. Um and so I think there's going to be a lot of activity in the digital space to like rewire everything in a certain sense.

**43:40** · And I think it's going to create a lot of demand for for this kind of stuff. I think long-term um yeah, obviously even with auto research like OpenAI or or you know, Anthropic or these other labs like they're employing what like a thousand something researchers, right?

**43:53** · Mhm. These researchers are basically like glorified auto like you know.

**43:57** · \[laughter\] They're like automating themselves away like actively and this is like the thing they're all trying to do. Yeah. I like I went around um Some of those researchers also fear that feel the psychosis, right? Because they can it's working, right? And and so they're like it's over for me, too. I did spend a bunch of time going around OpenAI and I was like, you guys realize if we're successful like we're all out of job like like this is just going to we're just building automation for Sam or something like that. Like I or the board or I'm not sure, but like uh they're just building all this automation for yeah, the board or the CEO or something like that.

**44:27** · And we're all out of our job and maybe contributing on the side. And so yeah, it's kind of like unnerving from that perspective. Is it okay if I ask you Noam's question? Mhm. You know, you could be doing that, right? Auto researching with a lot of compute scale and a bunch of colleagues at one of the frontier \[clears throat\] labs. Like why not? Well, I was there for a while, right? Like and I did reenter. So to some extent I agree and I think that there are many ways to slice this question. It's very loaded question a little bit. Um I will say that I feel very good about like what people can contribute and their impact outside of the frontier labs, obviously.

**44:58** · Not in the industry, but also in like more like ecosystem level roles. Um so your role for example is more like ecosystem level. My role currently is also kind of more on ecosystem level. And I feel very good about like impact that people can have in those kinds of roles. I think conversely there's there are definite problems in my mind for um uh for basically aligning yourself way too much with the frontier labs, too. So fundamentally I mean you're you have a huge amount of financial incentive to uh with these frontier labs. And by your own admission, the uh the AIs are going to like really change humanity and society in very dramatic ways.

**45:29** · And here you are basically like building the technology and benefiting from it like it and being like very allied to it through financial means. Like this was the conundrum that was in at the heart of you know, how OpenAI was started in the beginning. Like this was the conundrum that we were trying to solve. Mhm. Um and so you know, that so it's kind of um It's still not resolved.

**45:50** · is still not like fully resolved. So that's number one. You're you're not a completely free agent and you can't actually like be part of that conversation in a fully autonomous um free way. Like if you're inside one of the frontier labs. Like there's some things that you can't say. Uh and conversely there are some things that the organization wants you to say. And you know, they're not going to twist your arm, but you feel the pressure of like what you should be saying, you know, cuz like obviously \[laughter\] otherwise it's like really awkward conversations, uh strange side eyes, like what are you doing, you know, like so you can't like really be an independent agent.

**46:20** · And I I feel like a bit more a lot like aligned with humanity in a certain sense outside of the frontier lab because I don't I'm not subject to those pressures almost, right? And I can say whatever I want or Yeah, I would say in the frontier labs like um you can have like impact there of course as well. So but there's many researchers and maybe you're one of them, maybe your ideas are really good, etc. Maybe there's a lot of decision-making to do and you want to be in a position where you are in the room with those conversations when they come up. I do think that currently the stakes are like overall fairly low and so everything is kind of like nice.

**46:49** · But ultimately in the end of the day like when the stakes are really high, etc. If you're an employee at an organization, I don't actually know how much sway you're going to have on your organization what it's going to do. Like fundamentally at the end of the day um uh it's uh you're not like really in charge. Like you're in the room and you're contributing ideas, but you're not like really in charge of that entity that you're that you're part of. So those are like some sources of misalignment, I think to some extent. I will say that like in one way I do agree a lot with that sentiment that um I do feel like in the like the labs for better or worse they're opaque and a lot of work is there.

**47:20** · And they're kind of like at the edge of capability and what's possible.

**47:23** · And they're working on what's coming down the line. And I think if you're outside of that frontier lab, your your judgment fundamentally will start to drift because you're not part of the you know, what's coming down the line. And so I feel like my judgment will inevitably start to drift as well. And I won't actually have an understanding of how these systems actually work under the hood. That's an opaque system.

**47:42** · I won't have a a good understanding of how it's going to develop and etc. And so I do think that in that sense I agree and something I'm nervous about. I think it's worth basically being in touch with what's actually happening and actually being in a frontier lab. And if if some of the frontier labs would have me come for you know, some amount of time and do really good work for them and then maybe come and hang out.

**48:00** · looking for a job. This is super exciting. \[laughter\] Then I think that's maybe a good setup because I kind of feel like it's kind of um you know, maybe that's like one way Mhm. uh to to actually be connected to what's actually happening, but also not feel like you're necessarily fully controlled by Yeah. by those entities. So I think honestly in my mind like Noam can probably get do extremely good work at at OAI, but also I think his most impactful work could very well be outside of OpenAI. Noam, that's a call to be an independent researcher with auto \[laughter\] research.

### Open vs. Closed Source Models

**48:30** · Yeah, there's many things to do on the outside and it's it's a and I think ultimately I think the ideal solution maybe is like yeah, going back and forth or um yeah, and I think fundamentally you can have a really amazing impact in both places. So very complicated I don't know. Like it's a very loaded question a little bit, but I mean I joined the frontier lab and I'm outside. And then maybe in the future I'll want to join again. And I think um uh that's kind of like how I look at it.

**48:54** · One question related to what visibility to does the world or the AI ecosystem have into the frontier is like how how close open source is to the frontier. Mhm. Um and how sustainable that is. I I think Yeah.

**49:09** · I think it is quite surprising. The entire sequence of events actually from like having a handful of Chinese models and global models and I think people are going to continue releasing here in the near term that are closer than much of the industry anticipated from a capability \[clears throat\] perspective.

**49:26** · Yeah.

**49:26** · Um I don't know if you're surprised by that, but you're a long-term contributor to open source.

**49:29** · Like what's your prediction here? Yeah, so roughly speaking basically the the closed models are ahead, but like people are monitoring the number of months that sort of like open-source models are behind. Um And started with there's nothing and then it went to 18 months. Now it's Yeah, but then convergence, right? So then maybe they're behind by like, what is the latest? Maybe like 8 months, 6 months, 8 months kind of thing right now. Yeah, I'm a huge fan of open-source, obviously. So for example, in operating systems, you have like closed source, like, you know, Windows and Mac OS, these are large software projects, kind of like what LLMs are going to become, and there's Linux. Mhm.

**49:57** · But Linux is very easy. Like, actually Linux is extremely successful project. It runs on the vast majority of computers. Like, last time I checked, was it like 60% or something like from Linux? Um and that's because there is a need in the industry to have a common open platform that everyone feels uh sort of safe using. I would say like the industry has always felt a demand for that kind of a project to exist. Mhm.

**50:16** · And I think the same is true now. And that's why businesses actually want there's demand for this kind of a um a thing to exist. The big difference is that everything is capital uh there's a lot of capex that goes into this.

**50:27** · Um so I think that's where things like fall apart a little bit, make it a bit harder to to compete in certain senses.

**50:32** · Uh I I do think that the current models are very good. The other thing that I think is like really interesting is that for the vast majority of like consumer use cases and things like that, even like turn open-source models are actually quite good, I would say. And I think like if you go forward like more uh more years, it does seem to me like a huge amount of like simple use cases are going to be well covered and actually even run locally. Mhm. Um but there's going to be always like some demand for like frontier intelligence and that that can actually be extremely large uh piece of the pie.

**50:58** · But it could be that the frontier the need for frontier intelligence is going to be like, you know, Nobel Prize kind of work. Mhm.

**51:05** · let's move Linux from C to Rust. It's going to be like bigger projects, you know, like scoped in that kind of a way, and there's going to be maybe more um and maybe that's where a lot of the frontier closed intelligence is where going to are going to be interacting with. And open-source kind of like going to eat through a lot of the more basic use cases or something like that. You know, at some point what is frontier today is going to be, you know, probably later this year what's frontier today in terms of what I'm using right now from the closed labs uh might be open-source and that's going to be doing a lot of work. So I kind of expect that this dynamic will actually basically continue.

**51:36** · Like we'll have frontier labs that have closed um AIs that are kind of like these oracles, and then we'll have open-source kind of like behind with some amount of months. And I kind of expect that to uh to continue. And I actually think that's like a pretty pretty good setup uh overall. Um because I I'm a little bit hesitant of having um I don't actually think it's like structurally I think there's some systemic risk attached to just having intelligence that are closed and that's like that's it. Mhm.

**51:59** · And I think that that's a, you know, centralization has a very poor track record in my view uh in in the past and has um You mean like in political or economic systems in in general.

**52:10** · \[laughter\] Exactly. I think there's like a lot of like pretty an Eastern European. A lot of pretty bad precedents, so I want there to be a thing that is maybe not at the edge of capability because it's new and unexplored, etc. But I want there to be a thing that's behind and that uh is kind of like a common working space for intelligences that the entire industry has access to. Yeah, that seems to me like a pretty decent power balance for the industry. Yeah. I also think there's just like there are many problems to solve, right? Like if you keep advancing intelligence from the frontier, we can do new things and there are a lot of like very big problems for humanity, right?

**52:40** · And so like it seems that that will continue to be a very expensive game. And so I want to like root for labs that are doing that because there are problems we cannot solve without continuing to advance the models in a very expensive way. And yet, as you point out, like if what we have today as frontier is open, that's a lot of capability, right? And and so I I I think, you know, the power of that or the democratization of that seems like Yeah. very useful and also healthy.

**53:06** · Yeah. I think basically by accident we're actually like in an okay spot.

**53:09** · An optimal. Yeah. \[laughter\] Yeah. Like by accident we we are it happened to be in a good spot in a certain sense. Mhm.

**53:14** · Um Well, and and to some degree the the longer this endures, like this dynamic, um the the the healthier of a spot like the ecosystem might be in, right?

**53:24** · Because you have more and more area under the curve.

**53:25** · Mhm.

**53:25** · And I will say that even on the closed side, I I almost feel like it's been like even further centralizing recently because I think a lot of the frontrunners are like not necessarily like the top tier. And so uh yeah, like in that sense I think it's um it's not super ideal. I would love there to be more more frontier labs because yeah, I'm like by default very suspicious of like um I want there to be more people in the room. I want I think like in machine learning ensembles always outperform any individual model.

**53:50** · And so I want there to be ensembles of people thinking about all the hardest problems and I want there to be ensembles of people in the room when they um to be all well informed and to make those decisions, you know, so uh I don't want it to be like a closed doors with two people or three people. I feel like that's like not a good not a good future. I almost wish like there were more labs as long as they're short and I I I do think that open-source has a has a has a place to play. I hope it sticks around and I basically I it's currently slightly behind and it's actually kind of like a good thing. Okay, you worked on the precursor to generalized robotics autonomy um in cars, right?

### Autonomous Robotics

**54:24** · Uh a a lot has happened in the last couple months with robotics companies as well, like acceleration of really impressive generalization of environment, of tasks, like increasingly long horizon tasks, lots of money going into the space. Like, is it going to happen? Has anything in your view changed recently? Uh so like my view is kind of informed by what I saw in self-driving and I do feel like self-driving is the first robotics application. So probably what I saw is at the time, like 10 years ago, there were a large number of startups. And I kind of feel like um like most of them basically like didn't long-term make it.

**54:55** · Um and what I saw is that like a lot of capital expenditure had to go in and a lot of time. And so um I think it's like I think robotics, because it's so difficult, is so messy, and requires a huge amount of capital investment, and a lot of like conviction.

**55:09** · Um just it's like a big problem and I think atoms are really hard. So I kind of feel like they will lag be it will lag behind what's going to happen in digital space. And in digital space there's going to be a huge amount of unhobbling, uh basically like things that weren't super efficient becoming a lot more efficient by like a factor of a hundred.

**55:25** · Mhm.

**55:25** · Because bits are so much easier.

**55:27** · And so I think currently in terms of what's going to change and like where the activity is, I kind of feel like digital space is going to like change a huge amount. And then the physical space will lag behind. And what I find very interesting is like this interface in between them as well.

**55:41** · Because I think in this like if you we do have more agents acting on behalf of humans and more agents kind of like talking to each other and and doing tasks and participating in kind of economy of agents, etc. Um you're going to run out of things that you're going to do purely in the digital space. At some point you have to go to the universe and you have to ask it questions. Um you have to run an experiment and see what the universe tells you to get back to learn something. And so we currently have a huge amount of like digital work uh because there's an overhang in how much we collectively thought about what already is digital.

**56:12** · So we just didn't have enough thinking cycles among the humans to think about all the information that is already digital and already uploaded. Um and so we're going to start running out of stuff that is actually like um already up uploaded. Uh so you're going to at some point read all the papers and process them and have some ideas about what to try, but um yeah, we're just going to uh I don't actually know how much you can like get intelligence that's like fully closed off and was just information that's available in the you know. And so I think what's going to happen is first there's going to be a huge amount of unhobbling and I think there's a huge amount of work there.

**56:40** · Then actually it's going to move to like the interfaces between physical and digital. So I and that's like sensors of like seeing the world and actuators of like doing something to the world.

**56:48** · Mhm.

**56:48** · So I think a lot of interesting companies will actually come from that interface of like can we feed the superintelligence in a certain sense uh data and can we actually like take data out and manipulate the physical world um per its bidding if you want to like anthropomorphize the whole thing, right?

**57:03** · And then the the physical world actually I almost feel like the the total addressable market, etc. in terms of like the amount of work and so on is is massive, possibly even much larger maybe what can happen in digital space. So actually think it's like a much bigger opportunity as well. But um I do feel like it's a huge amount of work and and in my in my mind the atoms are just like a a million times harder.

**57:24** · So um so it will lag behind, but it's also I think a little bit of a bigger market. So it's kind of like uh yeah, I think the opportunity is kind of like follow that kind of trajectory. So right now is digital is like my main interest. Then interfaces will be like after that and then maybe like some of the physical things um like their time will come and they'll be huge when they do come.

**57:43** · Well, it's it's it's an interesting framework for it, too, because uh certain things, not the things I'm working on right now, but certain things are much easier even in the world of atoms.

**57:51** · Mhm.

**57:51** · Right? Like if you just think about like read and write to the physical world, like read, like sensors, cameras, like there's a lot of existing hardware and you can imagine like enriching agent capabilities or capturing a lot of new data if you just clever about it and like you don't necessarily have to invest a lot to like get something valuable.

**58:10** · Yeah.

**58:10** · Right. Yeah. So like examples of this that I saw for example are, you know, um a friend of mine, Liam, is running is a CEO of Periodic. I visited them last week. Yeah. So it was just on top of mind. Like they're trying to do auto research for materials science. Mhm. Um and so in that case it's like the sensors to the intelligence are actually like pretty expensive lab equipment. And the same is true in biology. I think a lot of people are very interested in engineering biology and, you know, the sensors will be more than just like video cameras.

**58:34** · Does that make sense? And then the other thing I was I saw for example is companies that are trying to have um like you basically pay people for training data. Yeah. Yeah. Yeah. Yeah.

**58:42** · To feed the Yeah.

**58:42** · programmatically.

**58:43** · Yeah.

**58:43** · To feed to feed the Borg. Uh um and so like these are all examples of like sensors in a certain sense. So they take many diverse shapes and forms if that makes sense. Mhm. Yeah, so I'm looking forward to the point where I can ask for a task in the physical world and I can put a price on it and just tell the agent like, you know, you figure out how to do it. Go get the data.

**59:02** · I'm actually kind of surprised we don't have enough like information markets.

**59:05** · Mhm. Like if for example if Polymarket or other betting markets or even stocks, etc. If they have so much autonomous activity and rising amount of activity, Mhm. like um why should like for example if Iran was just happening now, like how come there isn't a process where like taking a photo or video from somewhere in Tehran should cost like 10 bucks? Like someone should be able to pay for that, you know, like and that's an example of like feeding the intelligence. There's not going to be a human looking at it, it's going to be like agents who are trying to guess the betting games and stock markets and so on. Mhm. So I kind of feel like the agentic web is still like fairly new, but there's no like mechanisms for this, but this is an example of what I I think might happen.

**59:37** · Uh there's a good book that maybe is inspiring called Daemon. Mhm. You potentially read it. In Daemon, the intelligence um ends up like puppeteering almost a little bit like humanity in a certain sense, you know? And so, humans are kind of like it's actuators, but humans are also like its sensors. Um and so, I think like collectively like society will kind of like reshape in a certain way in uh to to serve that kind of a that will kind of like end up happening collectively across the industry.

**1:00:02** · Where yeah, there's just a lot more automation and it has certain needs and kind of humans will be serving those needs of that of that machine, not necessarily like to each other.

**1:00:12** · Well, we were um on this very specific point of uh like missing pieces of training data. We needed um we needed something like auto research, right?

**1:00:19** · Like we we need the training cycle or the SFTP piece to be uh far more mechanized. Mhm. For for which part?

**1:00:28** · In order to make the uh collection like to in order to take the human out of the loop to ask for a task that is just like improve my model quality with new data, right? Uh yes.

**1:00:40** · Does that make sense to you? Like we um if you can't have the model do the training runs by itself, then your ability to do this as a like closed loop task with uh by pricing data is um more challenged. Yes, yes, 100%. Yeah. But now you do.

**1:00:57** · The thing is for LLM training, it actually is like very easily it like really fits the paradigm. Mhm. Um so, you'd actually expect metric. Yeah, like LLM training actually fits the paradigm really well, really easily. Like all the optimization of all the code and so, it runs faster. And then you also have like metrics that you can optimize against. I do think that if you had an autonomous loop over those metrics, there's going to be a lot of like good herding going on where the system will like overfit to those metrics. And so, um but then you can use the system to devise more metrics and you just have a really good coverage.

### MicroGPT and Agentic Education

**1:01:25** · So, it's kind of hard to tell, but um in a certain sense it's like a pretty pretty good fit. I want to talk about a little uh tiny side project you have before we end. Um tell me about the micro GPT arts. Oh, yeah.

**1:01:37** · Okay, so micro GPT. So, I have this like running obsession of like maybe a decade or two of just like simplifying and boiling down the uh basically LLMs uh to like their bare essence. And I've had a number of projects along these lines.

**1:01:50** · So, like nano GPT and um make more and uh micro GPT micro grad etc. So, I feel like micro GPT is now the state of the art of me trying to like just boil it down to just the essence. Because the thing is like training neural nets and LLMs specifically um is a huge amount of code, but all of that code is actually complexity from efficiency. It's just because you need it to go fast. If you don't need it to go fast and you just care about the algorithm, then that algorithm actually is uh 200 lines of Python, very simple to read. And this includes comments and everything.

**1:02:17** · Um because you just have like uh your data set which is a text um and you need your neural network architecture which is like 50 lines. You need to do your forward pass and then you have to do your backward pass to calculate the gradients. And so, an auto grad engine uh to calculate the gradients like 100 lines. And then you need an optimizer and Adam for example, uh which is a very state of the art optimizer is like again 10 lines, really. And so, putting everything together in the training loop is like yeah, 200 lines.

**1:02:41** · And what's interesting to me like normally before like maybe a year ago or more, if I had come up with micro GPT, I would be tempted to basically explain to people.

**1:02:52** · Like I have a video like stepping through it or something like that. Uh and I actually tried to make that video a little bit. And I tried to make like a little guide to it and so on. But I kind of realized that this is is not really is not really adding too much because people cuz it's already so simple that it's 200 lines that anyone could ask their agent to explain it in various ways. And the agents like I'm not explaining to people anymore. I'm explaining it to agents.

**1:03:13** · If you can explain it to agents, then agents can be the router and they can actually target it to the human in their language uh with infinite uh you know, patience and uh just at their capability and so on. Right. If I don't understand um this particular function, I can ask the agent to explain it to me like three different ways and I'm not going to get that from you. Exactly. And so, I kind of feel like, you know, what is education?

**1:03:35** · Like it used to be guides, it used to be lectures, it used to be this thing, but now I feel like now more I'm explaining things to agents and maybe I'm coming up with skills uh where like um uh so, basically skill is just a way to instruct the agent how to teach the thing. So, maybe I could have a skill for micro GPT of the progression I imagine the agent should take you through if you're interested in understanding the code base. And it's just like hints to the model to like uh first start off with this and then with that. And so, I could just script the curriculum a little bit as a skill.

**1:04:03** · Uh so, uh so, I I don't feel like um yeah, I feel like there's going to be less of like explaining things directly to people and it's going to be more of just like does the agent get it? And if the agent gets it, they'll do the explanation. And we're not fully there yet because they I still can I still think I can probably explain things a little bit better than the agents, but I still feel like the models are improving so rapidly that um I feel like it's a losing battle to some to some extent.

**1:04:28** · Um and so, I think education is going to be kind of like reshuffled by this quite substantially uh where it's the end of like teaching each other things a little bit like if I have a um library for example of code or something like that.

**1:04:40** · It used to be that you have documentation for other people who are going to use your library, but like you shouldn't do that anymore. Like you should have instead of HTML documents for humans, you have markdown documents for agents. Cuz if agents get it, then they can just explain all the different parts of it. So, it's this redirection through agents, you know?

**1:04:55** · Um and that's why. So, I think we're going to see a lot more of that playing out. Well, we'll see if the great teachers know like to develop intuition for how to explain things to agents differently.

**1:05:05** · ultimately, so for example, micro GPT, like I asked I tried to get an agent to write micro GPT. So, I told it like try to boil down the simplest things. Like try to boil down my um neural network training to the simplest thing and it can't do it. Like micro GPT is like my is it's like my end of my obsession.

**1:05:22** · It's the 200 lines. I thought about this for a long time. I was obsessed about this for a long time. This is this is the solution. Trust me, it can't get simpler. And this is this is my value add. Everything else like agent gets it.

**1:05:33** · It just can't come up with it, but it totally gets it and understands why it's done in a certain way etc. Uh so, like my contribution is kind of like these few bits, but everything else in terms of like the education that goes on after that is like not my domain anymore.

### Conclusion

**1:05:47** · So, maybe yeah, it's like education kind of changes in those ways where you kind of have to infuse the few bits that you feel strongly about the curriculum or the the best the better way of explaining it or something like that.

**1:05:57** · The things that agents can't do is your job now. The things that agents can do, they can probably do better than you or like very soon. And so, you should um be strategic about what you're actually spending time on. Well, we appreciate the few bits.

**1:06:09** · Thank you, Andre.

**1:06:10** · Okay.

**1:06:13** · Find us on Twitter at No Priors Pod.

**1:06:15** · \[music\] Subscribe to our YouTube channel if you want to see our faces. Follow the show on Apple Podcasts, Spotify, or wherever you listen. \[music\] That way you get a new episode every week. And sign up for emails or find transcripts for every episode at no-priors.com.
