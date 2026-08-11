---
title: "Factory's Matan Grinberg: The Coming ‘Dark Factory’ Where Software Builds Itself"
source: "https://www.youtube.com/watch?v=ZesOukBjPmI"
analysis_report: "[[Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统]]"
author:
  - "[[Sequoia Capital]]"
published: 2026-07-21
created: 2026-07-27
description: "Factory started building fully autonomous coding agents in April 2023, two years before enterprises were ready. Matan Grinberg now says this is indistinguishable from being wrong. The Factory co-found"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=ZesOukBjPmI)

Factory started building fully autonomous coding agents in April 2023, two years before enterprises were ready. Matan Grinberg now says this is indistinguishable from being wrong. The Factory co-founder and CEO explains how the company survived its "journey in the desert," including the decision to hand nearly all of its revenue back to customers when the product wasn't making developers obsessed. Matan makes the contrarian technical case that a model-agnostic harness beats the model-and-harness co-design that labs like OpenAI and Anthropic favor, because exposing a harness to many models keeps it from overfitting to any single one. He argues open-weight models like GLM will capture the majority of tokens by staying one generation behind the frontier at a fraction of the cost, and that CIOs will soon justify every incremental token the way they justify headcount. Looking ahead, he predicts 90% of coding tokens will run asynchronously—the "dark factory" where software builds itself.  
  
  
Hosted by Sonya Huang and Pat Grady, Sequoia Capital  
  
00:00 Introduction  
01:37 Enterprise Lock In Fears  
04:26 No Lock In Promise  
05:24 Two Years Early  
07:24 Refunding Revenue  
13:49 Droid CLI Breakthrough  
16:44 Harness Frontier Tactics  
26:42 Natural Language Routing  
27:32 Open Models Catch Up  
29:26 Token Share Forecasts  
31:02 Automating Low Leverage Work  
32:36 Pricing Beyond Tokens  
35:56 Software Factory Vision  
43:43 AI Transformation Playbook  
46:13 Async Agents And Optimism

## Transcript

### Introduction

**0:00** · Bezos at Amazon it's customer obsession.

**0:02** · But in our mind that's an input metric.

**0:04** · Like you don't want to measure input metrics. It doesn't matter if you're customer obsessed. Like you could be customer obsessed and they file a restraining order against you cuz they don't like what it is that you're doing.

**0:13** · Like our job is to build something so good that our customers themselves become obsessed with us. That is our job. It's like you know, the analogy is if you're a coach of a basketball team, you don't want to tell your players before they come out there like, "Hey guys, make sure to sweat." It's like, "What?" Like no, like score points. Like we need to score points. And in doing so, yeah, you're probably going to sweat. And I think similarly to create obsessed customers, you probably need to be really obsessed yourself with the customers, but the output is what matters.

**0:46** · \[music\] We're here in the studio with Matan from Factory. This is our second time with Matan.

**1:04** · Thanks for having me.

**1:04** · You're in the small and elite group of second time training data attendees, so thank you.

**1:09** · Matan is the co-founder and CEO of Factory, which makes droids, which are autonomous agents for the art of software development.

**1:17** · Yes, indeed.

**1:17** · And Matan, we're going to jump right in because I think you guys are a little bit of a dark horse candidate in this world of software development. It is a market that is absolutely taken off. There are folks like Claude Code and Cognition and others who who have but you guys are coming up strong. Talk about the competitive dynamics and what makes Factory special.

**1:36** · It's been a wild ride. We started Factory three three and a half years ago now. So, in April of 2023, when the world and the enterprise in particular was barely ready for GitHub Copilot, let alone fully autonomous agents. And so, um I think the first two years it was kind of our journey in the desert is is how I like to refer to it because we were focused on fully autonomous agents, but

### Enterprise Lock In Fears

**2:01** · engineers weren't ready, procurement teams at the enterprise weren't ready, and so I think retrospectively we really like honed our craft and learned a lot about how to build for developers in the enterprise, but um you know, it it it took a lot of time to actually come around to when they were ready to receive it. And so we're kind of now emerging much more in some of these other players like Anthropic or OpenAI who have a ton of distribution um are going in and you know, bringing their incredible tools like Claude Code or Codex.

**2:33** · The thing that enterprises are really caring about that we have learned through those two years is they do not want anyone to kind of be their single point of failure. They do not want anyone to kind of control their fate. And so something that really matters is model independence.

**2:50** · Everyone learned from cloud where, you know, back in the cloud days it was like AWS or or Azure being like, "Hey, you know, come on in, sign this three-year contract. It's going to be so cheap. We're going to subsidize it. It'll be great." And then a couple years later when it came time to renewal, they would 10x the the the contract.

**3:08** · Haha, didn't gravity. We got you now.

**3:10** · got you. What are you going to do a two-year migration to go to someone else? Like no way. Everyone has scars from that now. And so everyone knows, look, Claude Code is fantastic. Uh Codex from OpenAI is fantastic. We cannot put our fate in any one of these model providers' hands.

**3:26** · Also, like you just look at the risk profiles of the model labs versus the cloud providers. What's the last piece of drama that came out of a one of the cloud providers versus like the model labs, it seems like there's kind of always some sort of chaos of, you know, internal fighting or getting in spats with the government or, you know, any other entities. And so uh if you're going to, you know, build this very important part of your business, you want to make sure that you're robust to any of these changes.

**3:53** · And that's something that we've learned over those kind of initial 2 years is like developers really care about things being modular. They want to know that they can customize it to what they want.

**4:03** · They want to know that if there's a new model that comes out that's faster or cheaper or more performant, they can kind of hot swap it in. And that's I think one of the biggest reasons why a lot of the largest enterprises are taking the momentum that they had from a Codex or Cloud Code and then are carrying that into Factory because they get that performance from these fantastic models, but they do it without the vendor lock-in that, you know, the Model Ops direct model provides.

### No Lock In Promise

**4:26** · if I'm the enterprise, I'm going to be like, "Wait a minute, am I not just getting locked into Factory?" What's the answer to that?

**4:31** · So, the good It's a really good question cuz that is something that you might think of like, "Okay, wait. So, we're just switching the the lock-in point." All of the modularity that we build is such that if at some point you wanted to say, "Hey, you know what? Factory's not staying at the frontier anymore."

**4:43** · Whether it's like the automations that you build or the skills registry that we help you create, the work that we've done stays in your code base and any of the automations that we've created, the artifacts also live in your code base.

**4:55** · In other words, there aren't really things that we're saying like our tribal knowledge about your org that we're keeping on our side and not giving to you. Um and that's part of the relationship that we have with customers is like we similarly want to make sure we're providing the best experience possible. If we help you arbitrage between different models to get cost optimization, we're giving you that optimization. We're not taking that away from you. Um and I think that's a really important part of the trust that we're building with with these enterprises.

### Two Years Early

**5:24** · You and I were talking probably a couple months ago at this point and I was trying to give you credit for having the right vision for this market 2 3 years ago and you responded with something along the lines of thank you, but being 2 3 2 or 3 years early is the same as being wrong.

**5:40** · Yes.

**5:41** · Um which I thought that was a wonderful response in so many ways. Can you talk about like that those 2 years in the desert? How did it feel to have this vision that turned out to be right that nobody appreciated for a year or two?

**5:54** · Can you just talk about like that journey and what it has done to the DNA of of your company?

**5:58** · Yeah, I mean, in the moment it's really really difficult because, you know, I hadn't had a job before. I dropped out of my PhD to start this company and, you know, over the course of those two years convinced, you know, 20 of the smartest people that I've ever met to quit what it was that they were doing and, you know, join Factory and join us on this mission. And these are people with families.

**6:20** · These are people with kids who are like dedicating years of their lives to this problem and going, you know, customer after customer and they like they weren't ready for agents. They didn't get it. Also, the models weren't as performant, but I think a lot of it was behavioral. And I mean, even just a fun anecdote of like giving developers an NPS survey. If you ever are giving a developer an NPS survey, they do not like whatever it is that you're giving it to them. Because like developers, they vote with their feet. They are very clear what they like and what they don't like.

**6:51** · And if you're like, "Hmm, I wonder if they like it?" They definitely don't. Um and uh but during that time, I think there were there was a lot that we were learning.

**7:00** · There was a lot that I myself was like I'd never had a job before. Enterprise sales is not something that comes obvious to to a physicist. Um but at the end of the day, it doesn't it doesn't matter. There's no you don't get any, you know, bonus points for being early because like who cares? Like there's no consolation prize. It's either you do the thing or you don't do the thing and that's all that matters. And for the team, it's really tough. There were points where uh we ended up getting good at enterprise sales, but the product still wasn't good.

### Refunding Revenue

**7:31** · And that's a very tricky position to be in because we ended up, you know, getting to a point where we were like just under 2 million in revenue and the product was not good. And there was a point in time where we realized this. Cuz if you're really good at sales, you can sign contracts. That's like you can definitely do that.

**7:48** · But if you're doing that and the developers don't like your product, it's like a ticking time bomb. Because it's eventually they're going to turn and it's going to be really, really bad.

**7:56** · We realized this and we proactively gave all of those customers their money back. And I remember that uh was one of the most difficult decisions to make. Because not only is there a uh you know, a group of you know, 20 people who are getting ridiculous offers from all the labs. They have these huge, you know, financial incentives to go elsewhere. There are all these other companies that are doing well and they decided to do this.

**8:20** · And then we're going to say, "Oh yeah, hey, by the way, that, you know, little bit of revenue we managed to get, we're actually going to give it back cuz we don't think product is making their developers happy." We also had to you make that decision?

**8:30** · You know, we sold them on a good vision and convinced them that, you know, this is the the right team to work with and that we were going to deliver the solution for them. But we realized that the way that we had sold them on it and the product that we were delivering was not up to snuff in a way that I don't think it would hold true to one of our operating principles. And one of our operating principles that I really like is create obsessed customers.

**8:54** · Yeah.

**8:54** · This kind of like flips over Bezos' thing. Where Bezos at Amazon it's customer obsession. But in our mind, that's an input metric. And like input metrics are like you don't want to measure input metrics. It doesn't matter if you're customer obsessed. Like you could be customer obsessed and they file a restraining order against you.

**9:10** · \[laughter\] Cuz they don't like what it is that you're doing. Like our job is to build something so good that our customers themselves become obsessed with us. That is our job. It's like, you know, the analogy is if you're a coach of a basketball team you don't want to tell your players before they come out there like, "Hey guys, make sure to sweat." It's like, "What?" Like, "No, like score points. Like we need to score points."

**9:30** · And in doing so, yeah, you're probably going to sweat. And I think similarly, to create obsessed customers, you probably need to be really obsessed yourself with the customers, but the output is what matters. And I think that it coming back to this, the product that we were delivering was not creating obsessed customers. And we wanted to make sure like this was a group of the smartest people I've ever met. We were getting there. Like we were getting a lot of intuition. Things were starting to come together internally.

**9:56** · Like we could see internally we were starting to become a lot more agent native in how we were doing things in the product was kind of scratching that itch.

**10:05** · But we were kind of ahead of our customers and we wanted to maintain trust with our customers so that when it does hit, we can come back to them and say, "Hey guys, this is the real deal. I promise." And to build that credibility, we had to say, "Hey look, you know, even though you were maybe happy to continue, we're going to give you this back and say, "Three months from now, I think it'll be ready. Give us some time and I promise we will knock your socks off."

**10:27** · How did your customers react when you had that conversation?

**10:30** · Some of them were like, "Oh great.

**10:31** · Sounds good." cuz I think it wasn't something that they, you know, were obsessed with. Some of them were a little bit confused. Um but I think gen- generally it's especially enterprises, they're not used to these things. A lot of times enterprise budget, once it's gone it's gone and no one really cares.

**10:45** · Yeah.

**10:46** · And so some of them didn't even know if they had a mechanism by which to take back money.

**10:49** · \[laughter\] Um but you know, it's a difficult thing to tell also like investors who believe in you. Like, you know, I remember having the conversation with Shawn. Um I think Shawn obviously he's stayed really close with the company so he was very like on the same page. But it's kind of a scary thing. Be like, "Hey by the way, you know, remember all those updates and you're saying, 'Hey look, the you know, revenue's going up. It's about to go down to zero.'" Um it was a scary thing. Uh and I think it was kind of a leap of faith of like we see the signal internally early of like this is the direction we need to go.

**11:20** · We need to kind of pivot the approach on the product. But I remember that all hands where we told the whole team, it was like, oh my god. That was like one of the worst months of my life. Like I was just cuz no like not everyone was going to say like, "What the hell is this? What's going on?" But it's kind of the looks on their faces where they kind of go a little bit pale and they're like, "Oh boy, like is this just the early signs and we're about to sink completely?" Um How did you keep the team together through that?

**11:46** · I think honestly the only reason the team stayed together is we were so ruthless about hiring early on where it was like people that are genuinely really, really obsessed with the mission, which our mission is to bring autonomy to software engineering. And like really, really caring about that, making sure everyone um was also like very clear feedback loops as to like this the fate is in our hands. It's not like this is like, "Oh, something that I go do." It's like we all have a part to play in, you know, making this work.

**12:16** · And I think embracing how much it sucked was also I think something that was very valuable.

**12:22** · Just being honest about it.

**12:23** · Being super honest about like, "Yeah, this sucks. Like you know, look look at those competitors, their revenue's going up like crazy. Like this is not good. Like we're in a very bad position. Like we just have to give back all of our revenue. Like we need to really get our together. Um and in the moment, I think retrospectively, those are the moments where really the deepest bonds are made.

**12:42** · Like if you talk to people who were like athletes or even like academics or whatever, whenever you're in the like stressful period, whether it's like cramming before finals or you know an intense like, you know, we have some some rowers on our team and I think that's an example we always go to. Like that sport sucks.

**12:59** · sport.

**13:00** · a pain sport.

**13:00** · It's a pain. It's literally just there's one number that quantifies your performance. It's just what is your time on your 2K or your time in that. Um but like embracing that is what creates those enduring bonds such that afterwards like we know what it's like to be at rock bottom. We know what it's like to lose. We know what it's like, I mean, when we first started the company, our valuation was 5 million.

**13:22** · Like a lot of our competitors, a lot of the companies out there these days, they don't know what it's like to not be a unicorn. That's like manifestly, that is what they are day one. Whereas like we have been there kind of in those dark moments and not a single person left.

**13:35** · Yeah.

**13:35** · That makes us so resilient and so strong that, you know, going forward, things are going a lot better now. But there are going to be really bad times, but we have that resiliency in our DNA that I'm not sure some of these other companies do.

**13:48** · I love that.

### Droid CLI Breakthrough

**13:49** · Um so talk us talk to us about what changed. And I'm curious your comment from earlier that the models getting better is not important thing that happened. Cuz at least in my mind, the model getting better is the most important thing that happened. So just help me understand.

**14:01** · Yeah, so so a couple things. So one is the interaction pattern that we were building for before was too ambitious.

**14:07** · Like to your point, we were right in that what we were building for was fully autonomous agents, but it was 2 years too early, which makes it wrong. And fully autonomous agents require a complete change in behavior from the developer. And we were trying to do that out of the box before they were even using tools like Copilot.

**14:23** · It was just too much of a leap. It was too much of a step function jump. So it's an important day. September 26th, 2025 was when we first put out um basically the the Droid CLI. And the Droid CLI met developers where they were in a manner that previously these fully autonomous agents did not. Um and also its performance was like completely state of the art and it was model agnostic. So it could use every model that was out there. September 26th was also 2 years after we initially started.

**14:52** · So the world had gotten much more used to using things like auto complete. Like by by late 2025, most engineers were using an auto complete tool, and many were starting to um at the time use like a chat interface to ask an agent to go do changes like wholesale. So like the more agentic interaction. However, what we see is that like if you go back now and use in this like agentic interaction some of these older models, they're still good.

**15:20** · So the biggest thing that changed was developers, and in particular in the enterprise, like being open-minded to this new way of working. In particular, you know, developers, they've established their workflows over the last 30 years. They can be stubborn.

**15:35** · A lot of them were like, "No, no, no, like my craft could never be done by an, you know, an AI tool." So, a lot of it was just like understanding how to work with these tools and having the willingness to go in and try, and also the intuition about what are the guardrails that you need to provide in order for it to succeed.

**15:49** · Yeah.

**15:50** · Um And so, I think it was a combination of both of these things. The model's getting better, so you need to do less in the way of providing guardrails, but also developers lowering their guard and being like, "Okay, you know what? Let me go try and do these things. It's going to go do things I don't like." And then also, there's a certain degree to which when Andrej Karpathy tweets about something, then every engineer suddenly is like, "Okay, you know, maybe this is true."

**16:12** · And Andrej started to tweet about these agentic work. Early on, he wasn't as open to it. And then him being more open to it genuinely just changed some people's minds, uh which is funny, but that's some of the things that go into behavior changes. Like, you hear it from people you trust, you start seeing it, you know, from people within your organization who are maybe a little bit more agent native, but that's that's kind of these things together is what what changed that.

**16:36** · And now we're all going to be on Slack. But We might we might be on Slack we might be pushing the limits of Slack, which I think is going to be another interesting thing, but yeah.

### Harness Frontier Tactics

**16:44** · Okay, so September 2025, you launched the Droid CLI. You said frontier performance soda. What does that mean for you?

**16:50** · There's like the benchmarks, which have a very short half-life. Like, anytime there's a good benchmark, it gets bench-maxed within like 3 to 6 months.

**16:58** · Yeah.

**16:59** · At the time, I think the one that we kind of championed when we launched, and kind of it ended up becoming a pretty good benchmark, was Terminal Bench. So, prior to that, the one that was kind of leading was Sweet Bench, which was um kind of took some open-source projects and some examples of issues that were then solved.

**17:15** · The problem with that was it was very focused on like Python and like scripting or like individual file changes.

**17:24** · Whereas terminal bench was more when it was in the terminal setting, so it was things like scheduling runs and things that were not just like changing the code file, but general software development tasks. And that was something that we ended up you know, having really frontier performance on. Now, it's like benchmarked to the extreme to where it's like I think, you know, models that come out now are like 90% on it. And I think um there's a very short time horizon from putting out a good benchmark to then it being kind of in the training data.

**17:53** · What goes into building a great and is it that is the great harness? And it seems like there's almost a lot of fud in the ecosystem of my harness is better than your harness and you know, you need to own the model to have a good harness or actually you you have a better harness if you don't own the model. Like what's your mental model for for Yeah.

**18:07** · you know, benchmark maxing aside, what keeps you at the frontier?

**18:11** · Yeah, so a couple of so some general things that matter are um the way you do caching. So, you know, cash tokens end up being like a tenth as expensive. And so one big piece of performance for a given harness is what what is your like rate of of token caching. Um another example would be how do you perform well in compression or compaction?

**18:33** · So typically when you're dealing with a a long session, you're going to exceed the context limit of the model itself. And so the harness will do some sort of, you know, summarization, compression, compaction, whatever you want to call it. And the way that you perform during that compaction is a big determining factor of how good your harness is.

**18:50** · Um and tests that they do for that are like, you know, they call it needle in the haystack where you have some long thread and maybe there's one piece of information that's really important. How often will your harness preserve that through compaction? Other examples are like tool use or how does it use the environment to validate whatever work that it's doing? Um these are things that you can kind of have individual metrics on and that we kind of have our own internal benchmarks to measure how do the out of out of the box agents do versus how does factory perform?

**19:16** · I think one thing that um naively everyone believed initially was if you train the model and you build the harness, you're going to make them better together.

**19:26** · Yeah.

**19:27** · And much to the chagrin of many of my friends at OpenAI and Anthropic, this is not true. If you build a harness that supports different models, that harness will be better.

**19:37** · What's the like my intuition would be model harness co-design makes you better.

**19:41** · Yes.

**19:42** · What's the intuition for why it's actually not?

**19:43** · It's very analogous to the idea maybe like I don't know 10 years ago of if you were to be like, "Hey, I want to train my personal AI back in like like ML days before like GPT-3, I want to train my personal AI, I'm going to give it all of my data cuz I want it to know me."

**20:00** · Turns out the answer was, "Train it on the whole internet and it'll be so much better for you than if it were just trained on your data." So there's a sort of analog that emerges where it's what data is to a model, models are to a harness. Where the more models you expose to a harness, you avoid over fitting that harness to the nuances of that model in particular.

**20:22** · And there are certain intricacies about different models that you can learn from and then improve different models performance in your own harness. And this was why for example, we kind of stopped doing it because Terminal Bench got so uh bench maxed, but initially when like every new Opus or GPT model would come out, it would perform better on Terminal Bench in droid than it would in Claude Coder Codex.

**20:43** · Um which is what like and this is something that you know I think was somewhat frustrating to cuz I deal like from a lab perspective you ideally want it so that it's better together because then it means you have to use their harness and you can't use a different one, but I think the reality is it it it's uh you know, having that multi-model harness ends up getting kind of frontier on on all of axes.

**21:05** · Is there a good like example or illustration of that? Conceptually it makes sense. Is there a like an easy way to illustrate it?

**21:11** · Maybe maybe a good example of it is like if you're familiar with the different behaviors of uh Opus and GPT 5.6 right now.

**21:19** · I am. He's not.

**21:20** · Okay.

**21:20** · Opus tends to \[laughter\] I mean, loosely loosely. I mean, to be fair, honestly these days I'm not doing it as much either. Uh but I will say this. Loosely, Opus is kind of like that super friendly colleague where you're like, "Hey, I want to go do these 20 tasks." And they're like, "Okay, cool.

**21:37** · Hey, by the way, five of those tasks I realized we didn't need to do it. Don't worry about it. I got other of these done. Did it this way.

**21:43** · not a good time. Let's pick it up in the morning."

**21:44** · Yeah, like and let's go let's go get a beer afterwards and hang out, whatever.

**21:48** · Meanwhile, like GPT 5.6 is like absolutely, I will do every single one of those and nothing will stop me. I'm not going to sleep until those are It's a kind of very OCD and you know, meticulous. But sometimes you know, you want one where it's like it actually realizes, "Hey, that list of 20 that you gave me actually here's a better way of doing it anyway." You know, 5.6 is more methodical. If you build a harness for each of those, they're actually different things that that harness will then be good or bad at.

**22:12** · So, for example, um one thing that, you know, typically agents will do is they'll they'll have a to-do list of like if you have a task, it'll go and generate a to-do list. Um and the Claude code harness can in some cases or and this is maybe less relevant now, but I think earlier this is a just a more illustrative example. Earlier, it was really strict to make sure it would stick to the to-do list cuz the model itself would typically wander.

**22:39** · Meanwhile, Codex wouldn't do that because the model itself was really really OCD about that. But if you're a user, you want to have the same experience regardless. Like you want to make sure if you switch to a different model, you're not going to suddenly lose track of whatever things that you are working on. And so, there are certain things where like maybe in some cases you really want robust tool use. And there are tools that you use to do these to-do lists.

**23:02** · You want really robust tool use and you want to make sure that no matter what if I'm a user I want to see my to do list there. Like there were some cases where it would just like not have the to do list. And so that these are things that kind of improve the general performance and that the to do list matters because we're doing some crazy migration and you don't have the to do list and then you're in this long session where there's compaction that might get lost in the summarization and then now you forgot what your seventh step was and that could be one of the failure modes.

**23:26** · That's kind of an example of of how they do it. Yeah.

**23:28** · Yeah, yeah, yeah.

**23:29** · Good example.

**23:30** · Okay, so we talked about one type of maxing, benchmark maxing. Let's talk about token maxing cuz it seems like the world has changed a lot. We've gone from token maxing to now cost rationalization. What does that mean for Vector?

**23:40** · Yeah, so um maybe I'll I'll lay this out just to so we're all on the same page of like the way that we see what what's led us to this token maxing. So loosely there was like this phase one where maybe phase zero was like no one believes in AI. Then phase one everyone believes in AI and then boards were like Mr. CEO, what are you doing about AI?

**24:00** · What's your AI strategy? And Mr. CEO is like I don't know like what's our AI strategy? CTO like make sure everyone goes and uses AI. And so then phase two is you know CTO is like okay we got to make sure everyone uses AI. Let's start putting it in performance reviews.

**24:14** · Let's make public like bench or public like rankings of who's using tokens the most cuz everyone's stubborn. No one wants to use this stuff. They're all skeptical.

**24:22** · And then we enter phase three which is everyone sees these ratings. They see that it's part of their perf reviews and they're like okay, I'm going to use AI for everything. And that's kind of phase three. It's this token maxing where people are using like Opus for literally everything. Like what's the weather in SF? Opus, tell me. I don't know. Like there are banks that we are working with where they are spending literally hundreds of thousands of dollars a month on people asking things like literally what is the weather.

**24:51** · Or like tell me about Python. Like trivial questions that you could Google, people are asking Opus. Um and the reality is this happened because we were so worried about adoption that we overcorrected and we're like adoption by any means necessary.

**25:04** · And I think that's actually it's like a decent approach. Like it's probably faster to do that and then curb uses or make usage more responsible than it is to start limiting and be like you know, you can only use it for this thing. Cuz when you have people that are stubborn, first you want to just prove that it works and then you can get kind of more mature about it. Where factory fits in, I think one of the most important things that we do is that we have the factory router which allows you to dynamically route to different models based on the task that you're doing.

**25:30** · So, you know, if you're asking what the weather is you probably don't need the very frontier of human intelligence to answer that for you.

**25:38** · Or or you really do.

**25:39** · I mean, it depend I don't know, it depends on what kind of answer you're looking for. Um you know, giving you like a full like down to the like molecular level of what's happening. But um uh you know, allowing that but also more importantly for every enterprise, something that no one's dealing with yet but 12 months from now is going to be the case is um not everyone needs the same tokens.

**26:02** · Having a blanket kind of token cap for every individual in some large bank, let's say, makes no sense.

**26:09** · So, every CIO is going to need to answer for every incremental token, where do we put it? And right now it is super not obvious how you would do that. Like right now we're saying, oh you know, the PMs who are like vibe coding dashboards get the same token limits as like the engineers who are building like critical infrastructure. That's probably not the best thing to do. Or similarly you might be dealing with COBOL code bases where Opus is not the best model to use but instead maybe some fine-tuned model on that code base in particular.

**26:37** · The point of the router is that we can kind of accommodate these different constraints where maybe you say, you know what, this part of the org, they're just vibe coding, they can use Gemini Flash. This part of the org, they're doing COBOL, we fine-tuned this great model to to on COBOL, let's route to that when we're working on that part of the code base. Maybe this other part we really care about reliability, so let's generate the code with OpenAI, test it with Anthropic, review it with like Gemini.

### Natural Language Routing

**27:03** · Things like that. And we can actually take in your routing procedure instructions in natural language. So, you could even say things like it's not purely deterministic, it can even be like hey, you know, Pat, I don't know, like I don't know what he's doing, like If Pat jumps in my flash given flash, like I don't know.

**27:18** · \[laughter\] Or, you know, I think we really need to avoid having them use open models because, you know, whatever reason we don't like the way open models perform here. And we'll do internal benchmarking to know which models are better at which of these tasks.

### Open Models Catch Up

**27:32** · How close are the open models at this point? Which one's the best?

**27:35** · GLM 5.2 is incredible.

**27:37** · It's at the point where internally we have no token limits for our engineers. And like half of our tokens are open to open models.

**27:45** · Wow.

**27:45** · Yeah.

**27:46** · Cuz they're just faster and they're cheaper. They're just as performant. And I think the thing that everyone gets wrong is everyone is comparing like GLM 5.2 to the latest model like Opus 4.8 or GPT 5.6.

**27:59** · But really they should be compared to Opus 4.7 or GPT 5.5. Um Why?

**28:05** · Because generally the open models come later and they're they're kind of a generation behind.

**28:09** · And that's kind of the the frontier models will be frontier. The question is are the open models getting as good as like frontier minus one?

**28:17** · And the answer is unequivocally yes. Which I think is a really, really interesting outcome. It's great for consumers. And by consumers I don't mean like individuals, I mean the consumers of the APIs. Because if you're a, you know, a business that is doing in our like software engineering your job is at a very high level to solve problems.

**28:38** · And if we can allow you to solve those problems faster and with cheaper models that are just as performant, that means you can solve more problems. Like that is a good thing. And it is a very good world where there is not like a monopoly on intelligence, but instead kind of a a garden of intelligence that you can pick and choose um you know, when you'd like.

**28:57** · It's something that we joke about is like you know, on this intelligence allocation thing. Um if you're if you're trying to get a a tutor for your daughter in algebra, you can probably find someone cheaper than Albert Einstein to be that tutor.

**29:11** · Now, it might be that she eventually goes and becomes like a leading, you know, physicist or something, in which case yeah, maybe let's let's get Albert Einstein in there. But most likely you can get, you know, a high school student or something like that. Um and it's probably much more cost-effective for you as well to do so. So.

### Token Share Forecasts

**29:26** · Since you guys do the model routing, like if you look at the you know, if there's a pie chart that shows the complexion of models being used by your customer base today, what did it look like a few months ago?

**29:36** · What does it look like today? What do you think it'll look like in a year?

**29:38** · Yeah. I will caveat this with saying that right now enterprises haven't gone too opinionated yet into the routing procedures.

**29:46** · Okay.

**29:46** · This is something that will happen over the next 6 to 12 months, but right now they're just going from no router to router. That's kind of the first change. Then it's going to be like the exact nature of the of the routing. At the beginning of the year, there's less than 1% of tokens went to open models. In the first quarter, it became a single-digit percent.

**30:06** · It is now crossed into being a double-digit percent of tokens. Um now, percent of tokens is not always the same as percent of cost cuz the open tokens are cheaper. Um but uh it's pretty crazy to see the the growth there.

**30:17** · What's your forecast?

**30:19** · \[sighs\] My sense is that we will asymptote towards vast majority being open just because it provides you more optionality and it's cheaper. Um but that doesn't mean they're going to be like that's of token share, not necessarily of leverage share. Cuz maybe there are 1% of tokens that are incredibly incredibly valuable um and are like very key decision-making, and then the rest are more like implementation tokens or kind of uh lower stakes, if you will. I don't think there's going to be a world in which like it's ever going to be 100%.

**30:52** · Yeah.

**30:52** · I think the frontier of intelligence will inherently always be valuable for every business, could just cuz the stakes are going to get higher in the kind of intricacy with which you think is going to be more important, but we'll be better at offloading certain tasks.

### Automating Low Leverage Work

**31:04** · And this is like you can loosely think of this uh already with the way orgs are structured, where you know, in general, engineering leaders are more tenured engineers who in theory have like more wisdom, and each kind of minute of their brain power is higher leverage, in theory. Um, and even, you know, you can also imagine like consider a human engineer and try mapping over the course of their day like how much brain power they're using.

**31:30** · And like, you know, it's probably going to be really low for a lot of it, but then there're going to be some moments where they're like going pretty hot, like they're deeply concentrating and thinking about some you know, systems design problem or whatever. All of those low leverage moments, we want to automate away.

**31:46** · And like we want to like those like very high leverage moments sometimes it's like, you know, we're referring to them as like the eureka moments, or the moments where they're like doing something that's very high leverage.

**31:55** · What if those aren't just moments, but what if those are like hours at a time?

**31:59** · Because you don't have to deal with all the other stuff. And I think that's kind of the the way to think about intelligence allocation is if you're an engineer and you're writing docs, that is such a low leverage use of your time. Like you've become an expert in your craft. And you used to spend hours writing docs. Like I remember it was actually valuable. Like I remember Stripe had so much alpha for just having incredible docs.

**32:21** · But imagine all the other stuff those incredible engineers could do if it wasn't writing documentation. Like we should live in a world where everyone can have docs as good as Stripe, and that is like strictly beneficial for everyone. And then the question is, okay, what do those really smart engineers do do their time once they don't have to do that?

### Pricing Beyond Tokens

**32:37** · Maybe this is a good time to talk about business model, given that, you know, especially with the rise of open weight models, the cost differential.

**32:44** · Um I imagine that means very different things for your for your cost structure, but very similar value delivered to customers. How do you think about uh business model and pricing?

**32:53** · Yeah, this is more what our customers want and need as opposed to what we want and need. So, for example, I think right now usage-based is clearly the way to go. We want to be aligned with like what they are doing and what we are doing. I think seat-based doesn't make sense at least for what we are doing. My sense is that eventually we will change to outcome-based.

**33:11** · Now, I don't think the enterprise is ready for that and we've learned our lesson from those first 2 years. We are not going to impose things, right?

**33:17** · \[laughter\] Um but my suspicion is that you know, in the 2030s, things will probably look more like outcome-based.

**33:25** · Yeah. What does outcome-based mean for your market? What would be the definition of an outcome?

**33:29** · So, maybe here's a way to put it. So, right now we charge we we are usage-based. Like the more tokens you use, you know, the more you pay, the more we get. Um now, since we are model-independent, we kind of with our router, we are kind of pointing a token cannon at either OpenAI, Anthropic, AWS, GCP, you know, any one of these people.

**33:51** · Uh to a certain degree, this is like a really dumbed-down version of a marketplace. Where right now, there is a a buyer the buy side is an engineer who wants a task done. And then, you have the model providers who are saying like either in benchmarks right now, they're like, we perform at this cost and this performance. And then we determine who we go to for that given task. Yeah.

**34:15** · There's a world in which, you know, if it's so important to get these tokens, they might kind of unaf- like bid in a certain way of saying like, look, here is our cost for this task. We will get this task done at this cost no matter what, but they're pricing it such that, you know, they hope that they can make a margin there.

**34:33** · If they price it wrong, they're at a negative margin. If they price it right and win the bid, then they get the positive margin. And the way you determine if the task was successful is by some validation loops. Cuz no one is using these tools anymore where it's just like, "Write me code. Great. Thank you." It's generally, "Write me code and here's how I know it was done well."

**34:51** · And similarly, if you are like a model lab and you are given, "Here's a task. Here's the validation criteria." You'll be able to say roughly how much you think you would be willing to pay to get those tokens. I say and you know, you want to have some some margin on that. And then in that world, that's basically that's a way to that you kind of dynamically shift from usage-based to outcome-based. Um I think that there's so many questions with this and this is very much forward-looking.

**35:16** · Um but I think there's a lot of questions about how do you subdivide tasks? You know, divvying that up I think is something that's not obvious.

**35:22** · Yeah.

**35:22** · But as these tools get better, doing things like that actually become way easier.

**35:25** · Yeah, that's fascinating.

**35:26** · Yeah.

**35:27** · Yeah, if you can scope a task and then create a competitive market for a place, that'd be a fascinating version of the future.

**35:32** · Yes. And as a user, it then creates an incentive to be very thorough in your validation criteria.

**35:36** · Yeah.

**35:36** · Cuz like, you know, there are stories of like, you know, you ask an agent to like fix my code and it deletes your code.

**35:41** · Yeah.

**35:42** · It's like, you know, the solution is just get rid of it all cuz it had that Silicon Valley episode. It's crazy how precious it was.

**35:47** · Yeah. But like, so you need to make sure your tests are very thorough cuz technically it could hit all of your validation criteria.

**35:52** · will go rogue?

**35:53** · Yeah, exactly. Yeah, yeah, \[laughter\] yeah. Exactly. Yeah, yeah, yeah. Yeah.

### Software Factory Vision

**35:56** · That happens.

**35:56** · Um maybe zooming out a little bit, you named the company Factory. Actually, you named it Droid before before Factory.

**36:03** · But you named it Factory before this concept took off. And now it feels like everybody wants to build a software factory. Where do you think we are today in in terms of the building of software factories and how close are we to the ultimate vision of a software factory?

**36:16** · Yeah, everyone has a software factory whether they know it or not. It's just a very inefficient one. So it's kind of like it feels like, you know, pre-industrialization where like, you know, people were manually like, you know, sewing things together or like woodworking or whatever it might be. And these things are very inefficient. Like right now, if you go to an organization that has more than 10,000 people, and you were to ask about the process by which they decide and release a feature,

**36:43** · there is like hundreds or maybe thousands of people in that process, and most likely they couldn't even draw it for you. Like, there's very low likelihood that they would know what what that process looks like. Um that is not because they think that is the right way of doing things. That is just kind of the nature of building large software as it is kind of today.

**37:04** · But with these systems, so much tribal knowledge can be codified. So much of this stuff that typically would require, oh, we need to ask this guru who's been here for 30 years who has the wisdom. Oh, we then need this approval and that approval.

**37:15** · Oh, and I forgot there was some doc that said we always have to do this checklist. Um and it relies so much on kind of human behavior and like redundancy, so much of that can be automated and refocused on like what actually moves the needle for our business. And I think this move towards software factories is a move towards how do we figure out what are the actual inputs that determine what features we need to build? And that might be inputs from the customers, inputs from the market, inputs from like, you know, product leaders at the company.

**37:45** · And let's be very clear. These are the signals, the inputs that we are taking in here. Okay, great. We have those signals. Then what is the process by which we build this? Um and really like mapping out the like assembly lines of how you are building software is really important because then you get to close the loop and say, did this actually deliver outcome for our business?

**38:04** · Talking before about the tokenomics, if you're that CIO and you're faced with that question of where do you put every incremental token, really the question 2 years from now is going to become where do you put every incremental dollar?

**38:16** · And so, you're going to have to be be asked, do you put that incremental dollar towards headcount or towards tokens? And if tokens, to where in the org.

**38:24** · And these are things that you can only really know when you have these kind of feedback loops that give you examples of like, "Hey, by the way, we made those decisions based on this data, and it did not matter at all. We added these new features and no one cared. It didn't create more retention, it didn't create more usage, or whatever metrics that business is looking to optimize." And the only way to do this is like you need kind of more rigor and more process.

**38:46** · It almost feels like like 10 years from now, we're going to look back at this previous era of software, and it's going to feel like businesses in like ancient times where they didn't do accounting.

**38:58** · It is like to be like it's going to be like marketing in the day of Mad Men, right?

**39:01** · Where it's like all creative and you have no idea what's actually working.

**39:04** · It makes no like it's like, "Oh, yeah, let's ship that feature. Oh, I think it went well. Like, yeah, we had I got some metrics on that." It's like, "No." If you guys read the the blog post that Jack Dorsey put out about how every company is like an AGI, Yeah.

**39:18** · there's also this degree to which if your company is an AGI, you want to optimize the weights.

**39:23** · Yeah.

**39:23** · You want to figure out what nodes are doing the what things, which are load-bearing, which are not, which need more tokens, where do you need more nodes. And in order to do it like you don't train a model by vibes. I mean, okay, actually you kind of do, but \[laughter\] you don't I guess more importantly you don't do backprop in a model by vibes.

**39:40** · Like you are running those actual like calculations, and you are seeing when we change this node, what happens. Now, you might be making bets on how to change the model by vibes, but you like you're it's pretty like mathematical in what you were doing. Meanwhile, at companies, you know, people are determining token budgets just by shooting from the hip.

**39:59** · People are laying people off by shooting from the hip and just being like, "Oh, yeah, like 20,000 There is no way there is science to laying off 20,000 people."

**40:07** · That is just like, "Here is a chunk, and let's just see what happens." Instead, I think in these organizations, the way they can do things is much more mathematical of like this part of the business matters a lot and does better if we give it more tokens. It doesn't actually matter if we give it more humans. So, let's give them more tokens. There might be other parts of the business where actually giving them more tokens doesn't matter, but more people matter because if we build more relationships with our customers and deeper relationships with our customers, that matters.

**40:32** · But, these are things that we're going to need like quantitative insight on and you need a software factory to do that. Otherwise, you're just like shooting from the hip and just guessing, which won't work as well.

**40:44** · limit how much do you think people will spend on tokens versus on engineering head count?

**40:50** · It'll depend on the business.

**40:51** · Mhm.

**40:52** · I think every business will have a balance and it just depends on like like they're just going to be like an easy example is generally sales people, they probably don't need that many tokens if they're good sales people. Cuz generally the where they provide the most alpha is like when they're in the seat face-to-face with their customers talking about the customers' problems, understanding, you know, how they build software in our case, and how we can make that you know, more efficient, more productive.

**41:15** · They can use tokens a little bit of like, oh, whatever, generate them some, you know, AI debrief, take some notes, like help them with the follow-up, but like it's so minimal the number of tokens it basically doesn't matter. Like if you add more tokens to the sales team, it probably won't change their output. If you add more humans to the sales team, it probably will.

**41:34** · Meanwhile, engineering teams are pretty different where engineering teams generally it seems like the you want people to own an outcome end-to-end, but then if you give them more tokens, they can produce a lot more. And so, it seems like there and then there's a lot of kind of places in between of like operations, finance, marketing. These are places where are neither here nor there where I think they're they're somewhere in between and it kind of depends on your business.

**41:56** · But, I think every business is going to have to ask, like what is our core competency?

**42:01** · Something that we see a lot in the market or we used to see and now they finally kind of hit reality. What we used to see is oh, like we're going to build our own like software development agents. And we're like, okay, like you're a like a consumer uh like logistics company.

**42:16** · Like are you sure you want to do that?

**42:17** · They're like, yeah, yeah, yeah, we're going to This is a core We have to do this. And so I'm like, okay. And then 6 months later it's like, wait, actually, this is not a core competency for our business. We don't want to hire, you know, AI engineers to be doing this. Our core competency is, you know, consumer logistics. That's what we want to focus on. And I think this is an opportunity for every business to double down on their core competency and what matters for them and then procure externally whatever it is that doesn't matter for them. Like a trivial example of this is like, I don't know, in the days of the early internet, you probably had to be a programmer to build a website.

**42:46** · And like websites generally help if you're a pizza shop cuz you want to have, you know, people come to your pizza shop, they want to be able to or like whatever. At that time, would you say it was a core competency of like a pizza shop to have engineers?

**43:01** · Like certainly not. Like that is kind of a byproduct of like a brief moment in time, but then there were companies out there that help you build a website, you don't need to be technical, and then this is why we live in a world where like most pizza shops don't have an engineering department, which I think is probably a good thing. Um and I think similarly, a lot of businesses have dealt with the reality of if you want to do XYZ other thing, you have to bring in people of this type of role, but I think that's been like something you had to do not because it's a core competency of the business.

**43:30** · And allowing businesses to focus and double down on the things that they are best at, I think it's going to be good for the consumers of their business. And so I think we're just going to see like a lot like ruthless refocusing on what actually matters, um which is going to be cool to see. Well, on that so, you know, every company kind of has to go through this process of reinvention. You know, 10 or 20 years ago, people talked about digital transformation.

### AI Transformation Playbook

**43:50** · And I don't know if anybody's given it a buzzword now, but AI transformation, something of that sort. Um couple years ago, you ran into a bunch of organizations that just weren't ready to deal with autonomous agents.

**44:02** · Things you've seen your customer start to change. And so the question is, when you look at your customers as they kind of go up this maturity curve and sort of reinvent themselves for the future, um any good like tricks or techniques that you've seen them use to repot themselves a bit?

**44:19** · Yeah, I mean, I think um surprisingly, like the companies that have been doing like company-wide hackathons really end up doing well. It seems like relatively trivial, but like just setting aside a day for everyone in the workforce is just like build with AI. It really sets the tone and sets the pace.

**44:39** · Certainly has given me a look as she's I I tried to force him to build something \[laughter\] with Coding Agent. Didn't go so well.

**44:45** · We'll work on it. We'll do after this one.

**44:46** · I you know, I we gave it a great effort.

**44:49** · But that's it. Like it literally just setting aside the time to like do it. And like even if it fails miserably, like it's fine. And also like the orgs that are okay with failing. Like it feel like it feels like there are some who are like, "We need to do it exactly right. We need to make the right decision from day one. No Yeah.

**45:04** · Like you're going to make mistakes.

**45:05** · Everyone is going to. And the orgs who are kind of leaning into it and embracing it to a certain degree, I think are succeeding. Like one of our largest customers is EY. EY is not necessarily known to be like at the absolute frontier of AI, but I think for them, they were just like, "Look, this matters. We were kind of There have been other trends and transformations that we were late to.

**45:24** · We're not going to be late to this. Like we're just going to go in. We might mess up, but like obviously respecting like secure The things that you're not allowed to mess up. You can put those aside. But like let's go and get our engineers to mess around and build this stuff and see where it breaks and understand what they like and what they don't like. Um I think that really matters a lot in the ones that we're seeing succeed. And also the ones who are like pretty bold in reinventing the processes that they've put in place. And just saying like, "Hey, it's a There's no sacred cows.

**45:53** · Like let's let's put this aside, try something out. If it doesn't work, we'll put that sacred cow right back. Um and I think that's that's been kind of a determining factor there. Um and when it comes from within, if it comes from the board, probably not going to go well.

**46:06** · Yeah.

**46:07** · If it comes from within like the tech team or the the ICs or the leadership, that's when we see it go better.

**46:12** · Hm. Do you have any predictions for the most important changes that are going to happen in your space over the next, call it, 12 months?

### Async Agents And Optimism

**46:19** · A lot of AI consumption's going up like crazy. And everyone's super, super excited because our revenue's going wild. Like a lot of this is synchronous usage. In other words, like if everyone woke up sick tomorrow, like a lot of Claude code usage would be zero. Cuz it's all just, "Hey, Claude code." Or, "Hey, Codex." Or, "Hey, Droid." Right? I think in 12 to 24 months, like 90% of tokens will be asynchronous tokens. So, these are going to be, you know, droids on their own autonomously being like, "Hey, here's some signal that I found from a customer. Let's go fix it."

**46:49** · Or, "Let's go create a first-pass solution to this." And I think that is going to be where the real like agent-native stuff begins. Cuz right now we're still kind of in like co-pilot mode. Like if you're going to an agent say, "Hey, go do this for me." It is more agentic because it's not going to come back and ask you a ton.

**47:06** · But it's still like you are kicking it off. Like yeah, if you guys have ever been to Tesla's factories, which is one of the sources of inspiration for the name, is like it's just robotic arms everywhere going and doing stuff. Like it's not like there are people there like going and, you know, attaching the widget to the thing. Um and this idea of like a dark factory where like the lights are off and things are just happening, that is where software development's going.

**47:26** · That's kind of where the the name came from is like, you know, Elon was always talking about the factory is the machine that builds the machine.

**47:32** · Yeah.

**47:32** · And that's been something that we took to heart. Um and I guess also that combined with his whole thing about how you're destined to become the opposite of your name.

**47:41** · Hm.

**47:41** · Um and in our case, you know, factory becomes artisanal. Which is kind of a good uh a good flip there. So.

**47:48** · What's your most optimistic version of the future both for Factory and for the world at large?

**47:53** · So, I think short-term there's going to be a lot of turbulence because I think a lot of companies have misallocated resources pretty poorly. There's been a lot of bloat. Um and I think the correction that's going to happen there is going to be really painful for a lot of people. And I think that's something that I think every AI CEO should really bear much more responsibility than they currently are for. Um and also figuring out ways to like address and kind of ameliorate in some way because this is something that's going to be very painful for a lot of people.

**48:24** · Now, I also I have optimism that we can actually address that faster than we think. We just need to start now in terms of addressing that. Now, the longer term and why I think this is a good thing is and why I don't believe at all like, you know, the BS that people are saying of oh, engineers are going away. Generally, there is a huge number of problems in the world.

**48:43** · A large subset of those problems can be solved with software. A small subset of those problems are currently being solved with software.

**48:50** · And so, in the short term, this means that okay, first there's a given problem that was overallocated engineering resources. So, okay, we need to reallocate those. Reallocate those is a very kind of cold way of saying some people are going to lose their jobs. But I think the the thing that's going to happen in the longer term is we need engineers. Engineers are some of the best systems thinkers and the best problem solvers. And there are so many problems that can be solved with software that are not being solved with software. And so, that means that we are going to take those engineers and have them go and solve problems that previously were not being solved.

**49:22** · That is such a net good for the world.

**49:25** · Because again, there are so many there's problems that we are not solving. And also, there's so many problems that we are maybe solving but with really shitty software. And like, this is going to enable people to solve it with incredible software. And, you know, the vision for Factory is that we are kind of the the factory that allows them to go and build this incredible software to solve these different problems. And these problems range from like things that are trivial to you know, like government software typically is not very good, whether it's like DMV or like IRS web like all that stuff is generally a pretty poor experience. Um we don't need to live like that.

**49:57** · Like we can all live in we can live in a world where all software is really fantastic. Um but also things like you know, pharmaceutical research. Like so much that goes into solving diseases is not just like a biology problem. A lot of it requires the best software engineers in the world. And previously those problems haven't allocated the right dollars to attract the best engineers.

**50:21** · But now because of what's happening, I think we will be much more closely allocated to like these are the biggest problems. Let's get the best minds and the best problem solvers to solve that. Um I think it's kind of our job as an industry to do that relocation reallocation as quickly as possible. So it's not 10 years, but maybe like 6 months or a year.

**50:40** · Wonderful. Maton, I think the clarity and consistency of your vision over time has just always been very inspiring and then just seeing how much you've grown as a leader and how much Factory has grown as a company. Even since the last time we did the Stranded Deep episode, it's truly all inspiring. So thank you for for joining us again to share what you're up to.

**50:57** · I appreciate it a lot. Thank you.

**50:59** · Thank you.

**51:09** · \[music\] \[music\]
