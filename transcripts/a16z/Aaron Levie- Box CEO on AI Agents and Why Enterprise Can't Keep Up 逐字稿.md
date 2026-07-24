---
title: Aaron Levie on AI Adoption and Enterprise Workflows | The a16z Show
source_url: https://www.youtube.com/watch?v=dvVbA9OcBqs
video_id: dvVbA9OcBqs
account: '[[accounts/a16z|a16z]]'
account_name: a16z
account_url: https://www.youtube.com/@a16z
featured_people:
- '[[people/aaron-levie|Aaron Levie]]'
published: 2026-04-28
created: 2026-07-21
language: en
speaker_attribution: contextual
description: Steven Sinofsky, board partner at a16z, Aaron Levie, CEO of Box, and Martin Casado, general partner at a16z, discuss the reality of AI inside enterprises. They cover the gap between Silicon Valley and
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=dvVbA9OcBqs)

Steven Sinofsky, board partner at a16z, Aaron Levie, CEO of Box, and Martin Casado, general partner at a16z, discuss the reality of AI inside enterprises. They cover the gap between Silicon Valley and the rest of the world, why most AI initiatives fail in large organizations, and how agents, infrastructure, and workflows are evolving beyond the hype.  
  
Timestamps:  
00:00 - Trailer  
01:05 - Introductions & The Silicon Valley vs Enterprise Gap  
04:30 - Why Enterprise AI Efforts Keep Failing  
09:16 - The Architectural Shift: Treating AI as a User, Not Software  
14:38 - The Integration Wall Agents Can't Climb  
20:12 - Should Agents Be Treated Like Humans?  
24:40 - Salesforce Goes Headless & What It Means for SaaS  
39:16 - Scale, Entropy & Why AI Coding Creates as Many Problems as It Solves  
47:53 - Will AI Kill Jobs or Create More of Them?  
  
Resources:  
Follow Aaron Levie on X: https://twitter.com/levie  
Follow Steve Sinofsky on X: https://twitter.com/stevesi  
Follow Martin Casado on X: https://twitter.com/martin\_casado  
  
Stay Updated:  
If you enjoyed this episode, be sure to like, subscribe, and share with your friends!  
  
Find a16z on X: https://twitter.com/a16z  
  
Find a16z on LinkedIn: https://www.linkedin.com/company/a16z  
  
Listen to the a16z Podcast on Spotify: https://open.spotify.com/show/5bC65RDvs3oxnLyqqvkUYX  
  
Listen to the a16z Podcast on Apple Podcasts: https://podcasts.apple.com/us/podcast/a16z-podcast/id842818711  
  
Follow our host: https://x.com/eriktorenberg  
  
Please note that the content here is for informational purposes only; should NOT be taken as legal, business, tax, or investment advice or be used to evaluate any investment or security; and is not directed at any investors or potential investors in any a16z fund. a16z and its affiliates may maintain investments in the companies discussed. For more details please see http://a16z.com/disclosures.

## Transcript

### Trailer

**0:00** · So, the board goes to the CEO. What does the board say? We need more AI. And what does the CEO say? Oh, okay. I'll get like a consultant to do more AI. And then they have some centralized project that nobody knows how it works. They haven't aligned their operations, and those things will fail.

**0:12** · The funniest concept that the more code we write, the less we would need engineers. It'd be the opposite because now your systems are even more complex than before, which means that you're going to be running into even more challenges of when you need to do a system upgrade or when there's downtime and you have to figure out like what Well, how do I fix that problem? Or when there's a security incident. I mean, we're just getting started with the jobs on this front. They're going to hit a wall at integration.

**0:32** · And And this The thing that's not different about AI and that agents don't fix, that nothing fixes, is that any enterprise of a thousand people or more or that's older than 10 years is just a massive stuff that's sitting there waiting to be integrated. And And you can't just say it's going to integrate. AI actually doesn't help to integrate anything.

### Introductions & The Silicon Valley vs Enterprise Gap

**1:05** · Hey, we are here moderating the situation live, and we're very excited to talk about a bunch of AI stuff. And we have a three of us are here today. Uh there's me, Steven Sinofsky, and Martin Casado, who will wave and say hi, I'm Martin, and Martin. and Aaron Levie, who is is working on the elevation of his hair today. So, we're excited about that.

**1:29** · keeps getting more vertical, and uh I thought I could kind of tame it, but it didn't work.

**1:33** · And is that just a token issue or a parameter number of parameters issue with your hair?

**1:39** · Too many parameters.

**1:40** · Okay, I have the same thing, but in reverse. Okay, so You Hey, listen, you have a distilled model. There you go. My I run local. So, we had a lot of There's been a busy week of things, but we're we want to bubble it up a a bit and just start talking about where where things are are heading.

**2:00** · Um but I'll I'll let I just kick it to you, Aaron, and you start where you are the most excited this moment because you have visited a ton of customers this week and have learned a lot. You've shared a lot on X. But I think you're the most in the trenches CEO who is really talking to customers every single day in the enterprise, which is what the three of us tend to look at the most.

**2:25** · Yeah, I think my it feels like my job these days is just bring reality to the valley and then bring the valley to reality as as much as possible. And it's a it is a kind of a crazy divide that that that exists at the moment. Um you know, the past couple weeks take it back. I actually think it's a super interesting. What what is it?

**2:43** · What's the gap caused by?

**2:46** · The gap is caused by Yeah, well, I think the gap is and Martin, I'm sure you see this, but I think the gap is caused by the styles of work that exist in Silicon Valley and in engineering roles versus sort of the rest of the world. So and we've talked about this a couple times in in different forms, but but you know, the the technical aptitude of an engineer is just like insanely high. The level of wired-in-ness to what's going on on the internet is insanely high. The the ability to use your own tools and make your own choices is insanely high.

**3:14** · And when things go wrong with the systems that you choose, you can just like quickly debug them and then make them sort of work for you. And then obviously you have all the benefits of just the models are really good at code and and the work is verifiable. So you have like you know, five or 10 things that make agents work in an enterprise context for engineering or at least a even a startup context for engineering that that tend to be a that there tends to be a gulf between the way you work that way in engineering and the rest of of sort of knowledge work.

**3:40** · And so and so a lot of what I see is trying to figure out how do we kind of you know, bottle up all of the greatness that is, you know, what we are seeing from coding agents, what we're seeing from agents that use computers um to how do you bring that into the enterprise where the workflows are are, you know, quite different. The users are less technical. The data is much more fragmented. The systems are much more legacy. And so that that tends to be the divide. So it's not even that we're like talking past each other like in a in a one of those kind of classic like government versus industry.

**4:09** · It's it's just literally like there is just a pure workflow and and and technology set divide. And and that's why it's going to be, you know, a number of years for this sort of diffusion to to roll from what we're seeing in Silicon Valley, what we're seeing as tech startups all around the world into the rest of knowledge work. Martin, just to build on that, you have a ton of experience in big companies. I One of the other issues though is scale.

### Why Enterprise AI Efforts Keep Failing

**4:37** · Yeah. And the way the difference in scale that Silicon Valley operates at at the startup level versus everyone else.

**4:44** · Yeah, I I also think that I mean, these secular trends like the internet was Like does actually start with individuals?

**4:52** · And big companies tend to make decisions centrally. And this is one of the fastest growing secular trend. So like there's probably a lot of individuals in big companies that are doing it where like Yes. the big companies themselves don't know even how to think about it. And so when you hear stats like oh like MIT had this stat like 95% of AI efforts in big companies fail.

**5:15** · Like that's clearly silly because I am sure everybody's using chat GPT very effectively. What what they really should be saying is you know, whatever. Like I Listen, I sit on these boards too. So the board goes to the CEO. What does the board say? We need more AI. And what does the CEO say?

**5:29** · Oh, okay. I'll get like a consultant to do more AI. And then they have some centralized project that nobody knows how it works. They haven't aligned their operations and those things will fail.

**5:37** · And so I don't, you know, when we say scale, often we we think about things like system scale or number of people. I think the secular trend is scaling wonderfully, which is being reflected in the numbers of these companies, but organizations don't know how to adjust these kind of, you know, agile processes that have been, you know, worked on for a decade around, you know, data and governance and operations and compliance, etc. That's kind of right now where I think like Aaron is right between the secular trend and the the organizational decision body.

**6:08** · And this is something that we actually track very closely because we're starting to see now, I would say in the last few months, finally some real kind of inroads into the enterprise, but it's it's it's tepid because and and the last thing I'll say at this, one of the reasons is there's a lot of skepticism because the board wants AI, CEO AI failures have created some amount of bruising, which is, you know, you know, requiring these companies get past it in order to do kind of the second go at it. And so I think this is exactly where we are.

**6:40** · Yeah, I I 100% agree with that, which is that it's good to start with agreements because we we know how quickly that fade uh Because we'll disagree the rest of the show, exactly.

**6:48** · exactly.

**6:48** · That's the only time we're going to agree. Um I I think maybe one more point on the board for agreements, maybe maybe you guys would agree. Um there's also this very interesting um dynamic. I I'd say this is a minor one relative to everything else is probably a 5% of the problem. I I think it'd be more fun to talk about the the real problem, but but there is a fun kind of as an aside, there's a fun dynamic where, you know, you go to an engineering team classically for the past, you know, and you know, Steven, you can take us back in in history on this one.

**7:15** · And one of like the easiest ways to stall a project was just getting the architecture, you know, kind of the the fights on, you know, what language to use, what architecture path to go down. That could take months and months to kind of work through as your teams work through that. Um because of the pace of change in AI, um you actually have this incredible dynamic where the the labs uh you know,

**7:37** · are are obviously leapfrogging each other so frequently, but with with not the exact same paradigm of how you should deploy agents and how they will work and is the is the is the agent harness in the computer is it outside the computer do you run it in your cloud is it hosted what tools does it have access to like we are like this is not a

**7:57** · a point where these are completely fungible technologies and so that actually creates a bit of paralysis because now as an enterprise architecture team in the real world you're like man like what what horse do I want to you know kind of get behind and and which architecture path do I want to get behind because I've been burned by doing the wrong thing in AI maybe three or four years ago and I went down in some path that now is deprecated or not the right strategy anymore.

**8:21** · So so to some extent the speed of our change in in tech actually reduces the ability for the tech to get diffused into the really really important workflows because now you have a lot of paralysis in in just making decisions. So so I actually think it's kind of fine because there's still so much upgrade work people need to do in their infrastructure and their systems and their data but this is kind of an interesting dynamic where I'll I'll go have conversations with CIOs and their AI teams and I'll say hey what what are you using for your chat system or your you know core agent orchestration and

**8:52** · they'll say yeah we're in the middle of a debate between these two or three paradigms and it's and and you and you hear that across almost every single customer because there is a little bit of a nervousness of like who do you get in bed with and and how how much do you sort of you know fully lock yourself into one particular path and we also know that that if you don't lock yourself into a path it's always then then you're building for the sort of duality which is you know also takes a lot of work architecturally.

**9:14** · I actually I sorry I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I like the you know and so it's kind of like this fusion or this hybrid model.

### The Architectural Shift: Treating AI as a User, Not Software

**9:44** · What we're seeing instead is instead of viewing AI as software, Yes.

**9:50** · like just view it as a user. And so, instead like take your product, make it a CLI tool, and then have the AI be an agent that actually uses it. So, you're not fusing the two, you're just making it more useful for AI. This is a very very significant architectural and mental shift, right? And so, we started as pure product, and then we didn't quite know what the end thing looked like. So, we created this you know this you know AI software hybrid that hasn't worked. And now we're kind of going to the agentic model, which basically means the agent is going to be whatever.

**10:19** · It's going to be cloud code or whatever, and then my product now just should be something that can consumed by that. And like that's the actual modality. But, you know, within a year now you've had to re-architect your software twice. And so, I think no matter many places that you look in the industry is having this dilemma of actually trying to figure out what the final form looks like. And Stephen, you will remember Remember all the hybrid versions of cloud? Oh, yeah.

**10:45** · Remember like you know like remote desktop and all these things? Like I think we're kind of like speed running that evolution to the final form. Right. And I And I think that that people in Silicon Valley don't quite appreciate when a big company says, "Well, we have to map out our bet that we're going to make." Yes.

**11:04** · Because like that just seems stupid. And you know, if you have if your job history is you know, five two-year stints at startups that went from seed to series A to acquire or something. Yeah, you didn't learn anything.

**11:18** · Well, you you never you you don't your frame of reference is not you know, picking an accounts payable system that's going to last 40 years.

**11:27** · Yeah, I I actually I have like all these visual aids today. So, here's like the ultimate the ultimate engineer if you're in Silicon Valley is Yeah, exactly. Is Gilfoyle. And and Gilfoyle is like I I don't want to talk to anyone. Yes. And I I will just write the code and you go do your thing.

**11:52** · And the the thing is is that you you have people in in enterprises that are saying, "I'm going to use the model and do my thing." But they're only they're going to hit a wall at integration.

**12:03** · And and this the thing that's not different about AI and that agents don't fix, that nothing fix, is that any enterprise of a thousand people or more or that's older than 10 years is just a massive stuff that's sitting there waiting to be integrated. And and you can't just say it's going to integrate. AI actually doesn't help to integrate anything.

**12:28** · And so even if you change everything the the people say, "Oh no, if you make it an agent, then it can just go ahead and and and be a user." But if you're a user, like if you've ever called customer service for something, like literally you get bounced to another human if the system that you're talking to Doesn't have to. doesn't work. And they're like, "Well, that's a manager."

**12:47** · Or no, you're you're talking about payment, not reservations. And and so like we're we're what I think is so exciting is that now we have proof of this technology that everybody likes it. I mean, you see all the people who don't like AI are saying, "Look at what's happening in law firms because people are seeing hallucinations and it's ruining legal cases and all this."

**13:10** · And and the reason that's happening is because the 25-year-old associate is the one using AI successfully already and have been using it for a year. Well, Steve it's actually Steve it's actually a little worse than that where it is right now many companies are incentivizing people to use AI by counting tokens.

**13:28** · Oh, yeah, yeah, yeah.

**13:30** · And so I'm not going to say the name of the guy I I spoke to someone yesterday who works for one of these large companies that famously does this, and he's like, "Me and my coworkers have agents do useless tasks just so that we can I'm no joke in No, no, no, totally.

**13:43** · Well, I you get whatever you measure, so Yeah, yeah. That's right. So like it's like the extreme form of what you're saying, Stephen. You have people that are like being fake productive and producing a lot of, you know, Yeah, you you could say perhaps problematic artifacts just because they're they're using these models.

**14:03** · The when when the internet happened, all of a sudden every company needed websites. And so like a very famous moment in time was not too long ago when every internal team had like a team website. And they went out and they got like a vendor to write HTML and to create their site. And then there was a team. But like there's nothing dumber than having a team website at a large company because a team gets reorganized like 6 months later. And so companies were just filled with like the with thousands of these dead web is what what the expression was.

**14:34** · But I I think Go ahead, go ahead. No, no, I but we should we should drill in your integration point because I do think this is something for you know, sort of some reality to settle in in in the valley on on the real world's sort of journey to fully being agentified and what that's going to take and what that's going to look like.

### The Integration Wall Agents Can't Climb

**14:54** · And and your your point about being passed to the different human, you know, based on the role that you needed to interact with, you know, agents basically don't have any There's no real exception yet for the agent having the same problem because you basically, you know, as you pass through different human, it's it's a different set of access controls that that that human has.

**15:11** · And if an agent can sort of bypass any of those steps, then then that's how you instantly get the security risks that like you you need to kind of pass through those steps so that way you don't accidentally, you know, get to the wrong piece of information and there's verification. And so, there's a lot that that you need to kind of build out for agents to be able to go and and work with all these systems. And and we've talked about this, but like most legacy environments don't have the most authoritative, you know, access controls.

**15:40** · So, you're always as a human going and saying, "Hey Sally, can you share that thing with me that that I don't have access to?" Or, "Hey Bob, what's the number inside your data system for this question?" And so, if agents just get the exact same permissions that you had, then they'll just run into these walls everywhere and they won't be able to complete the process. And unlike a human, they're not going to know to go talk to Sally or ask the question of Bob. So, they're going to just be kind of, you know, stuck. So, what's going to happen is you're going to have a lot of agents that don't have access to the right data.

**16:08** · Um they're they're kind of working through systems that that are, you know, not not the real sources of truth for the information. They're getting the wrong number. They're getting the wrong document. So, this is the real work that enterprises have to go through right now. The good news is that that it's actually a great time, again, if you're a startup because you can just you get to know all the problems right at the right out of the gate. So, you can design your organizations, you know, to try and avoid this. But for big companies, there's real work that goes into how do I upgrade my systems? How do I modernize my technology environment?

**16:38** · How do I make sure that, you know, agents will have access to the right data, the right documents, the right context to be able to do their work?

**16:46** · And that's sort of the the the work ahead. And and there's, you know, I I There was this uh you know, kind of headline of of OpenAI working with in Codex, you know, working with Accenture, Deloitte, all all the major system integrators. And there were some kind of like, you know, snarky comments online around it that that I was fascinated by because it sort of showed how how maybe, you know, great that divide is from the rest of the world versus those in tech because to me it was like the most obvious announcement of all time, which is a large enterprise is

**17:16** · going to have to go through that the change management, the systems implementation, the integration of technology for these agents to be able to go and work. And so, there was this sort of like, you know, people thought it was somewhat ironic that, "Oh, we need people to implement the agents that are going to go automate the people." And it's like, "No, that's exactly how it works."

**17:33** · You you actually do need to do lots and lots of work to be able to be in a position where agents can actually go and and help you do, you know, any of the automation. So so that is and that's going to be there's going to be businesses that are doing that for decades. Like, it's going to be an incredible opportunity for this kind of next generation set of firms as well as existing ones that that lean into that.

**17:53** · Let me throw this out there. Well, first, I think the other thing that people shouldn't celebrate when those fail and because they will fail because they're as Martin was describing, they're get a lot of them are going to be these sort of top-down mandates where they picked like the most acute problem in the company and think, "Oh, AI is going to go solve that." And the IT people are going to be like, "Oh, God, that's the worst That's that's that's the worst system to try to do that." But the CEO or CFO or whatever is going to be obsessed with solving or the most likely the customer service person will be obsessed.

**18:21** · But but I do think if I were if I were advising a startup specifically in order to to sort of enter the enterprise space in that way, definitely would be thinking about not just like building a company that step one, I only work with all the headless SaaS software that's out there because there just won't be any. Like the but the the thing you can do is structure the value that you offer. And also, this applies to what you go do in a company.

**18:50** · Is it's really a fork. And the fork is is this an agent that is seeking information and presenting it to to some human? Or is this an agent that's supposed to go act and do something?

**19:02** · Like, is it is it acquiring or is it doing?

**19:06** · Because if if it's it turns out that's how what happened with the internet. The internet got very very valuable when the first step was just providing access to things to people. Yes. And and like all of a sudden all the sites that were like that literally did integration. Like, "Hey, I need expense reports but viewed by department or I need to see our current inventory status across like the two companies we've acquired." All of a sudden the web became the integration point.

**19:34** · And so I do think that that if you just show a person and just say, "Hey, we can actually use agents to learn stuff about what's going on in a company." And in particular, because you're here, Aaron, like learning across the files becomes way more possible than it ever was before. In fact, AI might be the first time that inside a company search can actually provide immediate value. Yes.

**19:59** · web just wasn't structured to deliver those results. And and then you start to think, once you can bring them all together, then you can add like an agent that has an approved button or a reject button or something like that. Let me Let me Let me just try and provide Finally the point where I get to disagree. So let Uh-oh, we're in trouble now.

### Should Agents Be Treated Like Humans?

**20:19** · No, no, no, no, you can get invited back. You're invited back. So, good.

**20:22** · No, no, I I think this is a very legit view, but it's not the only view. And in light of AI, it's I think it's not the only kind of compelling view. So, here's the other So, the Let me just try and rephrase. So, the current view is we've got like AI is software. It it works in a different way. Um we have a current set of systems and we have to integrate this new type of software with our existing systems so that it can get access to data. It can do things, but in a safe way, right? So, here's the the kind of end-to-end argument of why this isn't about about evolving software systems.

**20:53** · The end-to-end argument is these LLMs are non-deterministic. They are smart. They deal with the long tail of complexity. And it turns out those are all things humans do, too. And we've spent 40-years building interfaces, processes, and design to deal with messy humans. And, you know, we know who to access, and we have access control.

**21:14** · And so, if you have the mindset that an agent is more like a human, and you hire the agent, you give it its own email address, it can access documents like humans can, it can log in, it can request the things that it needs, then it will be drafting on all of the process that that we've put in place for humans, not for software. And so, I would just encourage us as we have this discussion, like listen, I grew up like you guys in software. I always think of every system like software, but these models don't integrate well with software.

**21:44** · Actually, I think it turns out, and what we're learning as an industry is if you view them more like humans, and you draft on the mechanisms we put in place for humans, they're much easier to integrate. Well, that's And I THINK THERE'S I THINK WE ALL I think we agree with that for sure. I think the issue is humans have a bunch of extra benefits that the agent doesn't have.

**22:04** · The human has a lot of context that it gets for that they get that we get for free by virtue of we can keep track of the myriad relationships that we've built in our organization, and the person to tap on the shoulder when when we need something done, or we need to get information. That's not documented in a company yet in a in a way that the agent can just sort of draft on. And so, so I I like I I mean, I think we all would agree that that you have you can't treat this like software.

**22:28** · You treat these as as people accessing systems and tools, but they are at a they're both at an a massive advantage that they can work in parallel in at you know, at infinite scale, and they're at a disadvantage in that they don't know who to tap on the shoulder.

**22:40** · Hey, I listen, Aaron, I am all for agent onboarding. Like, you know, the agent comes, and it goes to orientation, and then the CEO gives it the culture discussion, and then every I'M NOT KIDDING. NO, YOU'RE PROBABLY RIGHT. I MEAN, THAT'S EVERY DEPARTMENT EVERY DEPARTMENT does their pitch, like this is what we do.

**22:58** · And like, I mean, I think I I actually honestly think given given the technical nature of these agents Yeah. and how much entropy they have and kind of how unruly they are, we're going to have to go through the processes that we've refined around humans. Yeah, 100%.

**23:13** · Because humans have all of those things.

**23:14** · And so I just, you know, it's more about providing schools for them than somehow building some, you know, fancy index database. No, no, totally totally agree.

**23:24** · That I mean, of course, what I love about about that is you just keep going with the analogy because what that is is it's the same argument that humanoid robots will will be the best kind of robot, which is we have a whole world designed for humans. And I like I I saw at the Consumer Electronics Show, I saw this robot go into an elevator and then there was a a button-pushing robot on the elevator. So, because the the robot was a tiny little thing that like a Roomba on the floor, it couldn't push the button.

**23:54** · So, the the same company that invented that robot invented a device you buy for the elevator that pushes the button. But then I asked, why did you need a device to push the button? And it And it was very interesting. They said, because the elevators don't have systems that they can hook into as a a robot. Like there's no Wi-Fi press the button in the elevator capability.

**24:17** · Yeah. There's no API for that. There's no there there is no headless version of the elevator. Yeah. And And I think that's That's actually a great metaphor for like the problem that I think that we're actually solving in the enterprise with these agents, which is we just, you know, we have two types of systems, those for humans and those for software.

**24:34** · And these tend to be more like humans, so we should draft on those as much as possible rather than try to retrofit them Well, and so so the big news last week was uh was I I I think, you know, Salesforce I don't know if they surprised people or not, but but I mean, based on the reaction, it seemed like it was maybe a surprise. They they went full headless and they basically said, you know, like we want to be used everywhere across all of our all of the different agents.

### Salesforce Goes Headless & What It Means for SaaS

**24:58** · Um and I see that as a a little bit of a bellwether because I think as Salesforce goes, so does a lot of of of enterprise software. And I think a lot of people are going to try and you know, have to figure out what is the new business model in this headless world. You know, do you do you charge a little bit of a a small just API tax? Is there a seat for the agent? So there's obviously some work to do with that. And Stephen, I I saw one of your tweets on you know, some of the some of the you know, complications there.

**25:20** · But but but but I think as a as a moment, it's a big deal because because I think it's a recognition that that, you know, software will be running in the background. It always has for machine users and applications. And now it is for these sort of probabilistic machine users and or non-deterministic machine users.

**25:38** · And what's cool and and where I think this gets pretty exciting is, you know, as soon as I saw that announcement, like I had like five to 10 personal use cases where I would need, you know, the headless version of Salesforce because I'm always doing just a tremendous amount of of customer related intelligence work. I'm going into a meeting, I need some information.

**25:58** · I need to do I'm going into a city, who should I be meeting with? And so if you imagine, you know, being able to run compute in the form of agents across all of your data systems, like the use cases become, you know, pretty wild around what that opens up. So I think this gives I think this gives a lot of software platforms all new use cases that they can tap into that where again, you were normally constrained by the number of people on these platforms, but now the headless user can be, you know, 100 or 1,000 x the scale of those human users.

**26:24** · So this is a I think an exciting moment because as you have more of these agents running around and the headless software modes, you just have, you know, way more use cases for these tools. I also think I just I think on this one, what's so what's so super cool is is that of course, the first step is doing exactly what you described, which is just looking stuff up. And so the the most interesting thing is using this notion that an agent is just a an entity, it's it's incredibly obvious to me that it's another license.

**26:55** · Now, it might have a different license model, but it actually it has to have an identity. Like when you go look something up in in the box um CRM system, I don't know if you're in Salesforce or not. When you use the box CRM system, it has to be a person. Like with a certain amount of access rights. And you presumably a CEO, you might have access to a bunch of stuff, but also there's a lot of ways that they actually don't want you to have the right rights at the right time.

**27:20** · Like you might be able to look and see who is on the account, but you don't need the up-to-date quota of those sales people and stuff, and that might be HR sensitive, and you should probably have some other level to go see that. But as you go down the org, the agent is never going to have more permissions than the person who's getting it to go do something.

**27:40** · And in fact, it's just going to be like a peer to somebody else in an organization.

**27:45** · Because otherwise, you have all of these issues where the peer where a human can just say, "Oh, get me the super smart agent that knows everything that I'm not allowed to know." And to to the in the mod in the IT architecture sense, what's so fascinating about that is you have to build you can't let the agent get the results and then try to figure out what works or not. But first of all, the points that Martin made about about about the the LLM stochastic model, which is you're not going to be able to figure out. It's not like a record in a SQL table that you could just apply ACLs to.

**28:16** · It's it's actually like it could be words in a sentence or just the number that shows up. And so I actually think it that whole discussion about headless for me made the SASpocalypse seem even dumber than it was already, and it was already dumb. So like it was like at first it was dumb, and then I'm like, "Oh my god, it's actually much dumber than I thought it was in the first place." Because you're just going to have this explosion.

**28:42** · Now, someone might come up with a very clever pricing scheme, and that agents, you know, somehow cost less because maybe for the first 5 years they're read-only, or they they're always tied to a person or something, but that it is another seat. There is no way around it. And like if you're a SaaS company, you're crazy to try to say, "Oh, just use the credentials of another human." Like that's just that would be like bad security practice from the get-go.

**29:08** · Exactly. So actually in in fact, um so this is playing out in many domains. You can even make the argument that like a a a headless SaaS doesn't make sense. And and here's the argument. The argument is Well, let me give you an example. So, um if you use OpenClaw, do you know why you use a Mac mini with OpenClaw? It's number one for iMessage.

**29:28** · So right, right. So it's for the integration. Yeah, yeah, yeah. Because there is no headless version, so you're just going to like use it. And then the second one is very interesting, which is if you've tried to use headless browsers with agents, the problem is is all of the websites um have anti-scraping measures. So they don't work. And so the reason you use a Mac mini so it can actually use Safari proper.

**29:47** · So to do anything headless kind of assumes that like the entire internet is going to go headless, when I think all of these models, like all of the data is humans working on the actual apps that are not headless. Like that's all of the data anyway. So I think these models are going to be very good at just using apps like they are today, and we're already seeing this happen, and rather than the headless versions, the non-headless versions are what's actually being used.

**30:15** · So you could argue that it's just Salesforce. Like not headless. Like It will go to a Wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait. Do you literally mean the agent goes to the browser?

**30:26** · Yes.

**30:26** · Oh, no, no, no. I'm I'm taking the other side on that one big time. Yeah, yeah. No, but but but but but but but let me just let let let let me let me simplify the argument so we can actually have it.

**30:34** · So So today if you use an agent like NanoClaw or OpenClaw, you could use a headless browser. Let's say I wanted to like look up the value of my house on Zillow. The headless browser simply doesn't work because Zillow's so tired of people scraping it, so it will detect headless browsers. Totally.

**30:51** · So, the thing that works is it uses you pop up Safari and it uses a proper Safari directly, right? And so then then all of the sudden it works. And so But no, but but but but I think I think I mean I would just say that that that any software that has a good API, the agent would absolutely prefer to use the API.

**31:11** · And then you and then you pop into the browser the moment that you run into some execution problem with I mean you know, set it set set as a a fantastic long-term computer science software guy. However, these models are trained on data and RL environments from existing software that didn't have those APIs. Yeah.

**31:29** · And and and and right now if you actually look at the adoption and the use of these agents, they look far more like what a human would do than what like a program would do. So, maybe you're right, but A, that's not what we're seeing. And you can honestly make the end-to-end argument when it comes to data and all of the controls in the internet. To Steven's point, all of the existing controls to just be like these are going to actually have the same actions as humans.

**31:55** · Well, the APIs most that that I mean I think the I mean the APIs of any software provider will follow the same access controls of of whatever the whatever the user is that that is Right, but they have to rebuild they have to they have to rebuild it. I mean it's like it's like you've got this existing app and all the the models trained on all of the people using the app.

**32:13** · Well, well, on on that point and it's a totally fair point, but I would I would guess over time you're going to have really uh you're going to have very you know, kind of accurate, rigorous data sets for you know, for models to be trained against the MCPs of of every SaaS platform, the APIs of every SaaS platform. Already it's in the you know, they're already training against all of our documentation on our on our products and our APIs.

**32:42** · But but I I just think to me it's it's more of just an inefficiency of of navigating through pixels versus just you know, you can just you can just do it.

**32:52** · Yeah. And added in systems Aaron is that is that layers never go away. They just get layered. Well well well well so so I but on that I'll I'll support your point 50%. Oh well, there you go. Yeah yeah yeah yeah. I I just I JUST THINK I JUST THINK IF YOU NEED TO DO A search for a document, our search API is going to be a faster way to do it than you know, you know, clicking through a an interface.

**33:13** · Right, but but the but the to have support the point like the new code X the computer use that on the desktop is is you know, just insane and I I mean Steven obviously knows you know, everything about how it would work. I well and I saw my ability to move a mouse and then this other sort of mouse moving and clicking things. I was like I don't understand computers anymore.

**33:35** · Right

**33:35** · right. So so there is a pretty and and to your point Martin, my first instinct was to use it for something where I know there's no available API. So I did actually use it right away for a thing that I don't have access to the API and and agent over time is going to probably have to figure out is there an easy MCP or CLI for this action and if not, then I'm going to pop into some kind of cloud browser or cloud computer or maybe local thing that I can you know, sort of parallel track and then and then go and execute that. So that does seem like a reasonable architecture.

**34:04** · Um but but I I still think that like I'm going to I'm going to pound the Salesforce API massively in in headless mode just cuz that'll be an efficient way to go look up records.

**34:16** · Yeah, I mean it I I think that your your sort of I think you're both saying the same thing, but there's just a time but no, but there's a time dimension. And I think like there was a moment at the internet that that I really was thinking about when when you guys were when I was seeing the time scale difference, what which was suddenly the 8 million quadrillion pages of how to use Word and Excel that we had written over the years that we posted on the internet, we had used to ship them with the product.

**34:43** · And people would have them on their hard drive, not connected to anything, and they would say like, "How do I make an ice chart?" or whatever, and it never worked. They could never find the thing that they wanted. But what happened with the internet was the net result of everybody finding it caused us to make better documentation, but it also caused Google search to be better at finding the information that it needed, which then completely changed the way that we thought about doing documentation.

**35:12** · And I think that with headless, especially for the kind that's just finding things, it's going to really change the the way that information is exposed. And so the way that Salesforce sees today of exposing it a headless API is I'm almost certain if I were to go look at it, it's going to look like the developer API in front of a behind a CLI, and it's going to look a lot like that.

**35:34** · But in fact, that's not at all how humans using Salesforce interact as a human trying to solve like, "I'm standing in the elevator waiting to go see a customer. What is the stuff I need to know?" Like that that mapping is completely different. And so the that API is going to really change as a result over time. Yes, I I I think I think the API changes for sure.

**35:56** · I I agree that, but I do think that unlike the humanoid, you know, kind of comparison, where where sort of the physical world has interesting physics issues that that you eventually run into, the digital world doesn't.

**36:11** · And so so at some point your agent can run in parallel, you know, 500 times, and like I'm going into I want to do a market map of of customers across the Fortune 500, that agent can can fan out and do that work in a way that I can't as a person in a browser. Right.

**36:30** · So so so to some extent agents get to let you, you know, sort of bend the laws of of normal, you know, human-based workflows.

**36:38** · Um and and so then to like that's why that and I think that that means the APIs maybe eventually evolve, but not obviously in the direction of the end user product, but but maybe more toward an agentic sort of set of workflows of what is that agent looking to do?

**36:53** · Well, but Martin, I think we jump in and just say, "Wait, you didn't describe anything new. You described an architectural No, but you described an architectural problem with today's software, which is it's it's API and performance gate was based on how much I can type." Which which is sort of the point I was making, which was our help system was designed on how much we could ship on one CD and had no data about what it is that people were trying to do and no context. But it didn't change like the problem, which is I needed to make a chart. Yes. Yeah, exactly.

**37:23** · The Well, so like one one real example of this, we we launched a Box agent that gives, you know, that has, you know, much more capabilities built into it and one of the capabilities is that it searches across your whole Box environment, but it doesn't it doesn't have the same limitations of a human-based search where you you type in one query, you get back a set of results, you look through them, you know, it fans out, does multiple queries, it can look through hundreds of results instantly and do its own re-ranking of that. And so that's just like, you know, again, you wouldn't want to be rate limited by the same a process that a human went through.

**37:55** · Which is which is where the humanoid robot is, you know, you're kind of willing to be like, "Okay, the humanoid is still going to walk into the elevator, it's still going to press the button." When actually, you know, in a agent world, you're like, "No, no, I just want you to go and instantly press the the floor that I'm going to." Yeah. Yeah, but we should just be very clear like by the way, I I very much agree, but we need to make a distinction between like would you ever build an indexing that's only for AI and not for a human. And I think that's less obvious. Yeah.

**38:24** · So clearly there's like performance gains based on automation. We've got to evolve our architectures for those, but if you find a great way to index documents and you don't expose it to a human, I think that's Yeah, you got to Yeah, exactly. 100%.

**38:37** · Well, well, this is I mean, it's actually I think this kind of moment probably reinforces some of Steven's, you know, kind of internet analogy on documentation. There is this really interesting thing where, you know, it started out where we as we've been building our our next set of agents, we first gave it this the current set of tools. We saw how how it used those. And then eventually we realized, oh, there's actually even even better way that the agent could do it. So we improved the underlying scaffolding. And then, oh, by the way, that will actually help the end user also.

**39:05** · So it does let you sort of contribute back into the mothership of of technology of technology improvement that does, you know, sort of lift all the boats of of your users. Let me Let me ask this it occurred to me as you were saying it, like I my I sort of got all tense when you when the idea became No, like oh, we have 10,000 people hitting our hitting our SAS system today, and we've got it all working, and it's all great. But um now we're going to have 10,000 new peo- people, which are the agents for each of those 10,000 employees.

### Scale, Entropy & Why AI Coding Creates as Many Problems as It Solves

**39:38** · And they're they're actually hitting it 500 times as much. Okay, so that SAS product will collapse.

**39:46** · So like that's the the first order, because it wasn't architected for that volume. Like we saw this with with all the BI tools. Like when all the BI tools came out, all of a sudden they they were looking at the SAP data and trying to snapshot it and absorb the whole thing every night for a new kind of set of slices and dice it. Your view across all 500 And and like all the people making ERP were like, well, we don't do that. And so they had to go build all of this themselves because they had the knowledge of the data.

**40:16** · Their API just couldn't was not designed for that kind of work up. So, my my sort of thing to throw out there and and fight about is what is it what is the change management look like in a company? Because you you can't let loose an agent that hits the system at 500 X the humans. And it's not a token thing.

**40:38** · It's an actual like, "Wow, we don't have the network bandwidth and the the throughput to handle 500 X for any one of our customers." So, what happens?

**40:48** · So, I've so I've got a provocative adjacency, which you guys can tell me if I'm doing too much on a tangent here, but but here's my provocative adjacency, which is I don't know if having more agents is that big of an architectural shift. I just feel like we understand like whatever, if it's read-only data, you cache it. You know, like all the state issues are around mutable mutable globally shared state. We understand the limits of those. We know how to architect around those. We have to tackle all of those things when we went to the internet.

**41:16** · And so, if you build your system not to handle it, like you suck at building the system and you deserve to go down and just go build a system that doesn't suck. And like I just feel like this is kind of standard computer science. However, I do think agents do introduce um something that organizations it technically have to deal with. And I'll let me just give the analogy in code, which is I think I Steven, this is what we call mogging on a I I don't know.

**41:39** · YOU'RE BEING A BAD I I QUESTION MOG.

**41:41** · I I QUESTION MOG. I HAVE NO IDEA WHAT HE JUST DID, but I I'm I'm just looking forward to how he magically made the problem go away. But go ahead. No, no, no, no, no, no, no, no, no, no, no, no, no, NO, NO, THE PROBLEM IS THERE. I just think like we know how to go from 10 Yeah, it's there for stupid people. We just got rid of the stupid people. So, now everybody is smart.

**42:00** · No, no. Okay, so so let me give you an example for coding. So, this is where I actually think there's a shift in how work gets done. So, when you code um with AI, your code kind of gets worse over time pretty materially. And so, it's almost like you're introducing as many problems as you are solutions. And I don't think we've actually figured out how to manage that. Does this make sense? 100% in the whole world right now. Yeah.

**42:27** · I I I you know, I mean like this is this kind of reasonable question is you know, if you're using AI, yes, you're productive, but are you creating more problems than you've actually solved for solutions? And I do think that there's this actually, you know, open question when it comes to using agents on existing systems for creating things, which is like like do we know how to wrap the growing set of entropy around that? And I would say anecdotally, watching companies struggle with AI coding, which of course I'm I'm you know, listen, I I'm very close to many AI coding companies. I'm clearly very bullish on it.

**42:58** · I don't think we know how to do that yet. And so, the you know, the agents on on a a system, I think we can tackle those with known techniques. Using agents for long-running things organizationally, where like, you know, you know, the the universe is kind of as clean as it was 3 days after then you started, I'm not actually quite sure we know how to do that at all.

**43:22** · Well, I I love that point because that gets back to where we started, which is the difference between scale and not scale. Yes. And why it's perfectly rational for big company people to be like, "No freaking way is this coming into our company." Because a big company is about to the wheels are going to come off a big company or a division in a big company or a product in a big company at any minute. Like if you're a Marty, we were both giant company executives. Like literally, we woke up every morning thinking, "Oh, the wheels are coming off today. This is the end of it.

**43:53** · I'm getting fired by the 5:00 and we whatever started what I left yesterday thinking we were 3 months late and it's we're now 9 months late." And that's a typical day. And so, but the reason that that doesn't happen is because you put constraints all over the place. Exactly.

**44:11** · Which is exactly why Gilfoyle can't work at a big company because he he thinks he knows and it's also why all the the one-shotting vibe coding kind of people have no problem saying it's fine because they've never had to live in an environment where the constraint was to prevent the whole thing from imploding.

**44:33** · And I I feel this is so critical Steve that you're like so in again, this is going to sound like a a little tangential but but it feeds into this which is I feel like core technologies kind of catered to like a some human need like the internet catered to like connectivity and social networking kind of catered to vanity and I feel like AI caters to our need to be productive.

**44:55** · So I feel like we feel like we're being very productive when we do all of these things but we may actually be creating like mounds of extra work to do. And to Well, Aaron, you're deploying AI right now. Like boxes all in. So tell us tell share a story like of the wheels coming off or not coming off. Yeah. Well, well, I I think I think we're probably in the more pragmatic part of the continuum. So so which is why we don't claim that that's a 10x productivity gain to our engineering team.

**45:24** · It's like no no cuz we have a lot of guardrails in place that create these constraints automatically in our system. There's we we still rely heavily on on code reviews. We still rely heavily on security reviews.

**45:36** · you are you guys coding with like a rock and a chisel and stuff?

**45:39** · it feels like that sometimes. We have chalkboards and like but no but like I I we had this new feature that we that we launched and I was like go go go go go and and AI built probably 80 to 90% of the feature and the the thing that slowed down the release of it was we have to do a full security review because we can't let there be any you know accidental code injection into the thing that we created. So so there's a lot of stuff where you kind of go super fast, but then you get still rate limited or constrained by some other part of the process.

**46:09** · Uh and I I think that's sort of, you know, relatively natural until we figure out then that other part of the process, security reviewing one or the actual code review being one or just even your pipeline for for, you know, getting things into production being another one. So, we we're doing a quite a little, you know, quite a quite a bit of retooling of the whole product development life cycle, but I I don't think that it's a five to 10x gain. I do think it's a two to three x gain maybe across the board. You are still rate limited by how quickly can you review this stuff and and check on the work. Um I do think that that Martin's sort of pointing at though a thing that is the the big open topic across enterprises.

**46:46** · Uh and and, you know, to some extent and engineers will fit will face it first and and will find the right equilibrium.

**46:52** · The harder part still remains in the rest of knowledge work. This is why if you're in accounting, you know, we don't quite yet know when you could take your hands off the wheel, you know, doing a full accounting audit, you know, because of AI. What what you can do is have the AI go and and like comb through unlimited amounts of data to find anomalies that maybe are that would alert your accounting team to, oh, we actually have to go dig into this.

**47:17** · That's awesome because that's only net new level of visibility. Versus the part of the accounting process where you're doing a fine-tooth comb on making sure every single number is is accurate. That's probably still humans right now.

**47:28** · So, I think the key is where do you find the productivity gains and I do think that that if you are a CEO or a board of directors or a management team, you're kind of trying to figure out and you're also getting confused cuz Silicon Valley's telling you all the things. And so, you have to sort of figure out where is where is the productivity most potent, where I actually can get the gain, I can get the success with less of the downside. And I think as an industry we're all sort of figuring this.

**47:52** · By By the way, this is actually why I remain unbelievably optimistic on jobs because I don't think that you like I just think we've gotten it wrong on on thinking you know all the places where you're going to remove humans from this because you still need a human in that you know somewhere in the loop. Maybe the abstraction is a little bit higher and you don't need the human in the loop at every at every single stage that you needed a year ago but but you do need a human sort of kicking off the process, reviewing the process and incorporating whatever the work was.

### Will AI Kill Jobs or Create More of Them?

**48:20** · Um and so that creates just still a tremendous amount of opportunity in jobs across these organizations. Oh, let me I have to jump in cuz I I have I have a whole bunch of like visual aids I brought today to make it exciting. We got you got a bunch of comments um on the MTS live thing about people agreeing with you. So I don't want to let that slide because you know we complain about not agreeing with you but but like here to your point to your point this was a book in the 80s called the end of work. Yeah. And and I this so actually sorry it was in the 90s.

**48:51** · It it it came out like six months before the internet hit.

**48:57** · And the whole thesis was the technology revolution was a complete bust and we got no gains in productivity but now there's going to be no more jobs cuz the economy is stagnant and this was the guy he called himself a futurist. Yeah. And and like so the whole notion that it it that's like one of the neat things about this whole AI moment is like the number of things that when you hear them the first time you think they're stupid and then you go back and think about it and you're like oh my god it's way stupider.

**49:25** · And and this idea that like AI just gets rid of jobs it's is ancient as like you picked talked about the accountant. Like one of the things people thought was that computers would get rid of accountants.

**49:37** · Yes. And and that was like IBM's pitch in like 1965 but what it actually did was like oh my god we could do so much more with accounting now that they're not like literally just adding numbers all day. Yes. And and I think when you look at like just the notion of like creating information, synthesizing, and all that. Like AI is is an accelerant for that for a person who knows what they're doing, and companies are suddenly going to want more of those people creating more of that information.

**50:04** · Not to mention the fact that if AI is creating valuable information and there's more of it, then more people will need to consume it to do something. And the idea the essence of a company is acting on information.

**50:17** · And and so this idea that information is just going to get produced easily and be in surplus and not used makes no sense at all. Because as you know, like in the unstructured information world, the problem is that you can make it, but the consumption of it effectively is the gating to it. That and that's the gating factor now.

**50:36** · Um we I I I think we had a conversation with one of our board members who's a chair of our audit committee and and so he's a CPA and and he was telling us, you know, kind of early in his career. I I can't even retell it cuz it felt so manual, but so I don't I don't even know how the world worked but I don't know how the world worked before all of the modern technology, but he was explaining the CPA's process and I was like, you know, it seemed like the most manual thing of all time, but but and and Stephen, I think this is right out of your book is like it was actually quite simple in in

**51:07** · sort of the amount of things you could do because of of how undigitized and relatively manual the whole thing was.

**51:14** · And computers actually only made it more complicated, more comprehensive, and thus created even more jobs because because of that complexity that that we introduced. And and you can just sort of see how easy this is to show up in so many areas of work is like we can just now we can afford to make things more complex. And so if if you make things more complex, then actually you eventually still run into now new constraints of who can understand that complexity. And and and and so like, you know, it's like to me it's like the funniest concept that the more code we write, the less we would need engineers.

**51:46** · It'd be the opposite because because now your systems are even more complex than before, which means that you're going to be running into even more challenges of when you need to do a system upgrade or when there's downtime and you have to figure out like what Well, how do I fix that problem or when there's a security incident? Uh uh And so, yeah, I mean, this is this is uh this is like we're just getting started with the jobs on this front.

**52:06** · Right, it all Listen, we're we're a few years actually into this and you can actually look a bit at the data, too, right? Like, what are the companies that are hiring the fastest?

**52:14** · Like the AI-native companies. They're hiring like crazy. Yeah. But not only that, like I remember there was this early prognostication, which is AI writing code will get rid of infrastructure. Like, it's going to commoditize infrastructure and like which which is this kind of very strange um prediction given the fact that there's more software than ever before been written, right? And right, sitting on the board of a bunch of infrastructure companies, some that have been flat for a while, they're all doing fantastic cuz there's so much software and there's so much more software out there now. And so, listen, if you look at the data on the ground from the companies, it's more software.

**52:45** · The AI-native companies are hiring the the the the the most and so, it's very clear to me that we're in an expansion phase.

**52:53** · And and and the maybe just my my only final point on this one at least is um is I think people we we have a little bit of a myopic view in Silicon Valley on on thinking that you know, engineering jobs are you go to work at at Google or name your your you know, tech company and startup and that that's an engineering job. And and look, we're so wired into that because of obviously the ecosystem that that we're all part of.

**53:17** · Um and then you sort of forget well, like John Deere is trying to make automated tractors and Caterpillar is trying to have AI systems and Eli Lilly is trying to design even more pharmaceutical, you know, kind of you know, therapeutics. Um and and just you can go through 5,000 other companies.

**53:34** · They're going to now have the next set of engineers that are going to use Claude Code and Codex and Cursor to be able to automate even more of of their businesses and be able to design and develop even more software for their workflows and their systems. And so, it just might you know be that you don't go and work on a social network and improve the social network algorithm. You go work at John Deere and you improve the the you know intelligent farming algorithm.

**53:57** · And and that and and we just have to you know I mean this is sort of like like completely you know like Marc Andreessen predicted this you know 15 years ago like software's going to eat the world and what that means though is that everybody's going to have lots of software. And this gives everybody the ability to finally have lots of software, but you still need then an expert or a semi-expert to be actually going and prompting the the the you know the agent on what to do, reviewing its work, and managing the system that it builds. So, so all of the you know predictions on don't go into coding and don't go into software engineering, I think will be proven quite quite wrong.

**54:31** · I think I mean look at that was super good Aaron and I think that that the the the base case of all of this is just that it there's too many people out there right now that don't like technology and have a static view of the world. So, when they look to whatever it is that they think AI is going to do and people hear automation, they just assume it's going to take things away. Like here's Well, we have a lot of people who like technology though that are also creating that uh that Right right. So, here's like this is article fighting the paper chase. Lower lower lower lower.

**55:01** · Well, I'm looking at a feed. Even lower. I'm looking at a feed. What are they Oh, you're looking at a feed. Okay. Oh, sorry. Okay. Okay. Okay. Oh, I see. Oh, you're looking at my Mac camera and yeah oh, that's why. Oh, you're fancy. You're fancy.

**55:14** · Right.

**55:14** · So, this is like Time magazine every kid in high school read it 1981.

**55:18** · And but the whole view of what computers would do would be they would automate the paper in a company. And so, the idea like the whole first generation of computing was literally taking paper forms and turning them into something on a screen, then printing them out, and then making it all easier. And you fast forward and it's all of these things that you just said Aaron like, you know, there was an era when lawyers didn't type. And so what happened was they just they they had people who were legal assistants, they called them paralegals, and they did all the typing.

**55:49** · And then like some students at Harvard, they brought a computer into the classroom.

**55:54** · And so this is I'm lowering it so you guys can see. Yeah, yeah, yeah, yeah. So they brought that's a original laptop in there in the early 1980s. And they brought they brought this computer into the classroom and then they got thrown out for using it and but they were literally they used to used to do law school and you'd write the essays in longhand in a book and then the professor would have to read them. And now of course you just type them and you have access to the database of all the citations, but that's exactly like nobody deals with a lawyer who isn't in track changes with their with your contract. Right.

**56:23** · And and I last I checked there are way more lawyers today than there were 30 years ago. And they all are every human lawyer you talk to is a computerized lawyer. Their citations come from from the internet, their their information in the brief comes and they type the brief.

**56:41** · think I I think we we you know, kind of going back to the my myopic approach, I think we maybe over like I mean as a big lover of technology, I I wish this was true, but I think we just over assume that like everybody's job is is just they're just inside of Microsoft Word and they're just typing a a word document.

**56:58** · It's like like I mean, most of the time with lawyers I'm like, you know, strategizing something or or they're working through a a complex analysis of a situation um and it's not like I could go to an AI for for advice, but and but that would probably only increase the chance that I go and then call a lawyer to say, "Hey, what do you think about this this situation that that you know, that I'm that that we're dealing with?" Um and so a lot of these jobs just have a lot of context that aren't sitting just you know, literally on the on the computer doing all the work.

**57:28** · They they do have to kind of touch grass um as a part of the job and and so then AI yeah AI will help automate the creation and production of the content and the review and of the information but then it still has to be incorporated into the real world of of real value production. I I feel like we're live and we're supposed to end at 4:00. So what I'm going to I'm going to do is just say we're live and it's 4:00 and I guess that means we just stop and some lights fade or something. None of us have done this before. We don't know what's supposed to happen.

**57:59** · But Someone is waving at me and smiling saying yes, I think you're right. The smile The smile means stop talking. Okay. All right. Well, it was great to see everybody. Bye, everyone.
