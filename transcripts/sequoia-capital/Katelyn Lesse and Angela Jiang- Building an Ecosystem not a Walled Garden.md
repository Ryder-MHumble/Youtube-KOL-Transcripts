---
title: 'Anthropic''s Katelyn Lesse & Angela Jiang: Building an Ecosystem, not a Walled Garden'
source_url: https://www.youtube.com/watch?v=vPnVTHYplrQ
video_id: vPnVTHYplrQ
account: '[[accounts/sequoia-capital|Sequoia Capital]]'
account_name: Sequoia Capital
account_url: https://www.youtube.com/@sequoiacapital
featured_people:
- '[[people/katelyn-lesse|Katelyn Lesse]]'
- '[[people/angela-jiang|Angela Jiang]]'
published: 2026-07-14
created: 2026-07-16
language: en
speaker_attribution: contextual
description: Katelyn Lesse and Angela Jiang lead the team building Anthropic's developer platform - the layer that both outside builders and Anthropic's own products run on top of. Angela frames the platform as a
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=vPnVTHYplrQ)

Katelyn Lesse and Angela Jiang lead the team building Anthropic's developer platform - the layer that both outside builders and Anthropic's own products run on top of. Angela frames the platform as a three-layer stack: knowledge, execution, and coordination. She argues the real leverage is what’s at the top: "strategies," or meta-harnesses that give each token a different job, from advising to executing to reflecting to memory. On the question of open ecosystem vs. walled garden, they say they aren't precious about owning the stack. Katelyn points to Anthropic's self-hosted sandboxes with partners like Modal, Vercel, and Cloudflare. Whether the work runs on Anthropic's infrastructure or someone else's, what really matters to them is that the architecture is sound. The deeper bet is standards: they hand skills and MCP to the whole industry, build connectors on the MCP spec, and help agents (Claude and non-Claude) work together. The one place they stay closed is model routing: they argue harnesses should be tuned to a model family, so they're designing for Claude rather than routing across models. Angela's frame for the ecosystem bet is electricity: transformative only because everyone could plug in, and no company wired it alone.  
  
Hosted by Sonya Huang and Lauren Reeder, Sequoia Capital  
  
00:00 Introduction  
01:49 Two North Stars  
02:27 External Builders And Primitives  
03:54 What To Externalize  
06:00 From Messages To Agents  
08:19 Managed Agents Adoption  
09:07 Three Layer Cake  
10:22 Execution Harnesses Explained  
11:09 Coordination Strategies Roadmap  
12:13 Ecosystem Standards And Safety  
15:39 Open Ecosystem Not Walled  
17:12 Vertical Products And Form Factors  
22:26 Claude Tag Under The Hood  
26:04 Harness Best Practices  
38:13 Token Costs And Whats Next

## Transcript

### Introduction

**0:00** · The last layer of abstraction on top of this is probably the coordination layer.

**0:03** · So you have knowledge and you have execution, you have coordination. And at the coordination layer, we're beginning to think of these things called like strategies where basically it's almost like a meta harness. The true low-level harness is designed for execution. But the next one is about okay if tokens aren't really fungeible and you need to give them different jobs like maybe some this token is advising versus this token is executing you want to start composing these like these kind of orchestrated strategies that go together and they should sit on top of all these things because at the end of the day you still need to execute and the execution still needs to know what to do. So everything in theory should kind of like ladder together.

**0:33** · And so I think you know if you were to look at our road map and the maybe kind of project forward a little bit where you kind of expect us to go.

**0:39** · We'll move more and more from the knowledge layer to the execution layer and from the execution layer to the kind of coordination layer in terms of the abstractions that \[music\] you can see us put out.

**0:53** · \[music\] Caitlyn and Angela, thank you so much for joining us today. Lauren and I are thrilled to have you here. You are responsible for building Anthropics platform and so you are responsible for building what I think is one of the most important if not the most important developer platform in the world and we

**1:18** · are really excited to interview you today to understand more about what's ahead and so maybe just to get started can you give us the context of you know what is anthropic platform and where do you sit within anthropic? Yeah. So platform is both our externally facing APIs, our developer platform that people build on top of when they want to build applications and system that systems that access cloud's intelligence as well as internally um we run our product infrastructure and basically we're the layer that our apps build on top of uh internally as well.

### Two North Stars

**1:49** · Awesome. What's your northstar as a team?

**1:51** · It's a great question. We actually because we have both internal and external. We actually kind of have like two north stars which is probably like you know you' be like why there should only be one north star but um no we different planetary system.

**2:02** · Yes

**2:02** · exactly they're separate solar system so it's fine. Um but uh on the internal side like we really want to provide is like literally as much leverage as possible for our internal teams to be able to ship like AGI pill products. Um and we want them to be able to move fast, be able to have reliable like great like uh platform uh to be able to build on top of. But I think that key bit about speed is like really intentional for us and we really really care about that internally. Externally um we actually have a lot more like complicated set of things.

### External Builders And Primitives

**2:29** · Um but one of the true norths that we have there is to be able to basically give any builder the tools to be able to work with claude to build whatever they want to build.

**2:39** · And so it's a bit of a broad statement but as a result that uh boils it itself down into you know being wherever that business is. Like we really care about like bringing our platform really really close to that business. This is why we spend a lot of time with the hyperscalers integrating really closely uh directly with them like AWS, Google, so on and so forth. Um and it is a lot of like primitives that we end up creating. We want people to be able to express what they think their product should be. We want them to be able to almost do like custom software in their own way.

**3:07** · You know, like in this new world with AI, uh what used to be probably economically impossible was that last mile of of custom software now in theory should be like very very achievable. Um, and we want to give them all the tools and all the capabilities to go and do that. And so sometimes that comes in the form of primitives and APIs and higher order abstractions. And sometimes that comes in the form of just like standards. Uh, so for example like skills and MCP. Um, those are things just like cloud needs them to be useful and we can just give them out to the rest of the ecosystem, work with everyone to help you create those things and get the best out of cloud.

**3:39** · So um I would say externally you know we really are oriented around just helping you just be able to build but internally that orientation while still existing is probably more you know specified towards speed and being able to move really quickly.

### What To Externalize

**3:54** · How do you decide what goes into the platform what gets externalized and what doesn't to decide what products should be available?

**4:01** · Yeah

**4:01** · I mean we generally try to have a philosophy that we try to be consistent across the board. It's actually one of the reasons uh why we do internal and external. Um there's plenty of other you know platform businesses and constructs where you actually like bifrocate these two things. Um for us we kind of try to intentionally keep it equal and then as a result we try to hold this philosophy as much as we can around like you know for any builder internal or external even though if our internal builders might have some slightly different requirements in the same way any user would have slightly different requirements. Uh we want to have the same primitives that are available to everyone.

**4:31** · And one of the maybe the overarching thesis for that is that we've just seen like the capabilities of these models just grow and such just exponential and it's really hard to figure out like a longlasting form factor. I think two years ago we were all like everything's chat and now everyone's like forget chat and just like agents and like there's going to be another form factor, another form factor. Um and we kind of imagine that like constantly evolving. And so the best way for us to kind of enable that for everyone and also ourselves is to actually build a really robust platform that gives people those kinds of like tools to figure out what those form factors are.

**5:01** · And I don't think we by any means feel like we're the only ones capable of figuring out that form factor like not at all. In fact, the more democratization we can do on that and help people and allow people to experiment, I think the the more those form factors will actually kind of naturally come out of the market.

**5:15** · Yeah.

**5:15** · Yeah. And I think within our team, we've we've had moments where we're experimenting even with just like a packaging up of our primitives in a different sort of higher order way. And we've thought about, okay, cool. We've solved this exact type of problem with this product that we've built into the world. And so we can go and dog food it for ourselves, but we'd never want to fall into this trap of like we're overindexed on the problem as it needs to be solved for an internal user. Like because exactly what Angela said, internal users have very specific requirements.

**5:43** · External users have very specific requirements and so if you overindex on one or the other, you fall into a trap. So a lot of the time what we'll do is dog food something internally at the same time that we open up early access of some sort with external customers so that we can kind of get a range of feedback and bring those things back into the platform.

### From Messages To Agents

**6:00** · I'd love to talk about the higher levels of abstraction that you discussed. So I guess at the base level this is just you know raw access to CLA opus or whatever tokens. How do you think about the I guess the layer cake of abstractions above that?

**6:14** · Yeah, if you look back um so when I joined Anthropic around a year ago um the platform was basically just the messages API. It was a messages API. Um you know we had come out with standards like MCP. We obviously have developer tooling around our SDKs and our docs and our console and things like this. But for the most part it was a stateless API.

**6:32** · Um, and what's interesting to Angela's point on form factors evolving over time is we found a lot of our customers solving the same problems over and over again that we also were solving over and over again around as the models got better at running for longer and working with more contexts at a given time. You want to build agents that can succeed in a kind of longunning context and even a remote context that doesn't necessarily have a human in the loop.

**6:59** · And so we found that we could piece together our primitives and stand up all the same infrastructure that we're finding ourselves standing up internally to power our own products and arrive at some higher order abstractions that let you do more agentic work out of the box.

**7:14** · And the problems that we're solving for you are, you know, infrastructure being kind of a hard thing to deal with. like how do you figure out spawning sandboxes that are going to have the right governance and security and like you know spin them up and spin them down when you need to or the storage around transcript sessions so that you can resume a session if you stop it and pick it back up later. Um so that infrastructure is a big thing that we wanted to be able to provide more of out of the box and we do more of that today.

**7:39** · Um, and then the second thing just being harnesses and harness engineering.

**7:44** · There's a lot of thought and energy going into how do I do my prompt caching and how do I manage my context window as well as how do I actually just get more intelligence out of the model um, and how do I manage my costs and things like that. So we've kind of packaged up our primitives a bit more in tune with the problems that we found ourselves solving to provide more of these things out of the box for people so that they can if

**8:07** · they're building systems for themselves internally, if they're building products, they can just be more focused on the problems that they want to be solving and if they want to offload some aspects of those problems to us, they can. Um, and that's kind of the ethos.

### Managed Agents Adoption

**8:19** · And are your customers generally choosing to opt from the grab bag of stuff that you offer or are they like how how often are they opting into the just the the managed agents offering? I guess just take care of it all for me.

**8:29** · Um it varies by like the the user group.

**8:32** · So like for I would say you know like really AI native startups like the ones who are like tinkering and like experimenting at a really low layer they're just going to go for the primitives. Um and then for everyone else and these are kind of classic like more like enterprises or areas where it's like the purpose of the startup or the philosophy behind the startup isn't necessarily to optimize on um some kind of hill climbing piece. It's more like stringing together a bunch of workflows and you know providing unique user value at uh to that user. For those people um you know it's just kind of not their core competency.

**9:00** · It's not where they want to focus their time and resources and they reach much more for these kind of like higher order like package offerings.

### Three Layer Cake

**9:07** · What are some examples of the primitives you've released at different layers in the last few months? We've seen a few of them. Would love to hear.

**9:13** · Yeah.

**9:13** · I think maybe one framing I would give um for some of the constructs that Caitlin was talking about is like and this is a bit of an oversimplification, but effectively there's approximately like three like layers of this cake. At the very bottom is just kind of like like knowledge. And so at this layer like in many ways it's it's knowledge about the model. It's knowledge about the things that the model needs. And it's just like the ability to know how to actually do something with claude is maybe the way I'd phrase that. And so there the primitives that we have spent more and more time on uh have been actually things of the past because like we still evolve them but they tend to be a little bit more baked.

**9:45** · Like for example there's very specific shapes and parameters we put on the messages API and it's more like trying to expressly like uh showcase Claude's like design like Claude the model's uh actual design the way it thinks the way it respects certain parameters the way it kind of like um will do tool calls like all of those different pieces. And then we started standardizing like tools. And then we started standardizing bits and pieces of like context that you could put in at different moments in time which is concretely like skills and like memory.

**10:14** · And so those are like the kind of like knowledge layer type of abstractions that we've put out over the past um I guess like year plus plus a bit. Um the next layer of abstraction that we've actually started to spend more and more of our time on is like once you kind of know stuff you then need to like execute. And so at the execution layer, that level of abstraction is the part that Caitlin was talking about around like we're doing these like higher order pieces, but like what are we putting higher order there?

### Execution Harnesses Explained

**10:38** · It really is because you're now getting Claude to execute work. It's not just to know something, right? I can give it a question and give me an answer. You can put string a lot of that stuff together.

**10:47** · Uh but now if you need to execute like do work, give me the output, edit files in a bunch of different systems, that becomes a lot more complicated and requires infrastructure to handle. And so that layer is basically I would say a low-level harness plus manage infrastructure as like the set of abstractions. Today we just like our highle product for that is called cloud manage agents. Um and so that's like a piece but we started to wrap more and more pieces in that. Um I think there's going to be a layer like on top of that we have like some inklings of it we started to build towards but the last layer of abstraction on top of this is probably the coordination layer.

### Coordination Strategies Roadmap

**11:16** · So you have knowledge and you have execution you have coordination. And at the coordination layer, um, we've started to expose some of these in ways that like aren't very obvious, but we're beginning to think of these things called like strategies where basically it's almost like a meta harness, right? The harness, the true low-level harness is designed for execution.

**11:33** · But the next one is about okay if tokens aren't really funible and you need to give them different jobs like maybe some this token is advising versus this token is executing this token is dreaming versus this token's executing so on and so forth you want to start composing these like these kind of orchestrated strategies that go together and they should sit on top of all these things because at the end of the day you still need to execute and the execution still needs to know what to do so everything in theory should kind of like ladder together and so I think you know if you were to look at our road map and the maybe kind of project forward a little bit where you kind of expect us to go we'll move more and more from the

**12:05** · knowledge layer to the execution layer and from the execution layer to the kind of coordination layer in terms of the abstractions that you can see us put out.

**12:12** · That's a really cool.

### Ecosystem Standards And Safety

**12:13** · How do you think this all comes together into a broader ecosystem beyond just the things that you guys are building? How do you help support people building products on top of it and how do you help them get the most out of all these pieces?

**12:25** · Yeah, I think this is like super top of mind for us. like we really want to find a way to be to support as many people in doing this as we can. I think we're still like learning like a lot of the industry like has evolved. We've seen, you know, a lot of different pieces um get spun up and spun down. And I think the the operative part for for Caitlyn and I has been in the category of like making sure at least at the base layer that we provide as many primitives across the board as possible.

**12:51** · So you know this kind of like yeah like knowledge execution coordination layer we want to give all of that out to everyone so that people can start to compose and create on top of that. Um and that's just from like I think pure builder kind of point of view. Then there's a point of view around like how do you kind of like plug in with us right like we're also building firstparty products of our own. We've also created some ways to embed natively with us like for example connectors which are built on top of the MCP spec.

**13:17** · Um, and we try to be more open about those types of things. And we're starting to figure out like what are the right bits and pieces, but what we're really trying to do is get to a place where, you know, in a company is able to get created and built on uh they can build whatever products that they want. They can build agents if they need to.

**13:32** · And then those agents and those products could be things that could plug into other agents. Some of those agents could be cloud agents, some of those agents could be other people's agents. Um, but we want to be able to enable that kind of like transactability across the board. And then I think in order for all of that to kind of ultimately be true, there is a bit around like standard setting and I think there's the traditional standard setting which is around you know how do systems interoperate um and that's uh you know things that you've kind of seen us do with like skills and MCP but they're at again like the builder layer.

**13:59** · I think at a higher order layer there's also a bit around interoperability and standard setting around how do we all kind of like treat safety together and you know we've talked to a lot of these companies and this is less from you know philosophies aside just more like no one really wants to have technology that's like for example like doing negative things on um on their service right so

**14:21** · cyber I think is a great example of this uh you want to protect your own systems from like negative actors or or bad actors and so like these kinds of like standard settings of like how we find ways to partner with more and more people to be like, yeah, we all kind of want to make sure our critical infrastructure is good. We all want to prevent like fraud or any of those things from happening and how can we work better with each of these members.

**14:43** · I think on the last layer, we're still kind of like we're still evolving and I think we're still very much like trying to find ways that we can be better and work with the rest of the industry to bring people along and and work with them. Um but those are kind of like you know the higher order primitives or pieces that we wish to kind of like be in place. Um so they can work with folks to to ultimately solve this. I think if I were to like take a step back at the end of the day on on all of these things um you know like this technology is so transformative.

**15:08** · Uh and if it's a little bit like electricity in the sense like before electricity there was just like you know you had to like have a candle and it was like you can only do so many things. Um, but with electricity, the reason why it's such a transforming technology for all of us and so greatly of a utility is because you can actually like wire it into everything. Everyone is able to actually access it. We also have like standards and ways to plug in and do all the pieces that we need. And that's not something that anybody can do by themselves. They always have to work with the ecosystem and work with partners um to figure out a path forward.

### Open Ecosystem Not Walled

**15:39** · How do you think about the philosophy of building an open ecosystem uh versus a walled garden? And you know, how do you think about what products are really important for you to own first party versus where you're perfectly happy to plug into other components of the ecosystem?

**15:54** · Yeah, there's so maybe in using Angela's kind of layered cake that we talked about a little bit earlier, you'll see that on some pieces of this like execution for example, um what we've done within something like cloud managed agents and I think over time you'll see us try to make this a little bit more modular. We actually aren't precious about you should run these things on our infrastructure like it should be sandboxes that we control or it should be a storage layer that we control.

**16:17** · Um well we actually like for example we launched self-hosted sandboxes and we partnered with modal and versel and cloudflare and a bunch of other folks um even like Amazon's new microVMs um to have a first class offering where you can go plug any of those things in.

**16:36** · Um, we launched MCP tunnels so that you can call out to your MCP servers that are behind your firewall, right? And um, be able to punch through there. And so for some of these things, we, you know, the weather, whether it runs on our infrastructure versus somebody else's infrastructure is actually not important to us because the thing that's important to us is more that the architecture of how you put together these agents in a way that will be powerful, in a way that will be reliable and scalable. um we have strong opinions on that and you can kind of just conform to the interfaces that we put out there and plug those things in.

**17:08** · Um and we think that that generally is a thing that works really well. Yeah, I think on the the kind of like verticals where we might build products um you know I think we we kind of have like two frames here. The first one is we are always trying to figure out a form factor like an evolving form factor. We by the way don't think form factors are like static. It's like a dynamic thing. So what might be awesome for one year's worth of AI development will probably not be awesome for the next year's worth. And we just kind of try to have that mentality. We tell the team uh just overall like around anthropic.

### Vertical Products And Form Factors

**17:38** · Everyone's always trying to be like is this agi pill enough? Um and then we always have this mentality of like you know we built something it works it was cool for a year and maybe it's not the right next thing and so throw it away try again. Um and we we tell like platform users the same thing.

**17:52** · um I just think that's probably just like you know attached to the technology but so yeah one one principle is like trying to always constantly find this new form factor. So sometimes we'll like launch products in certain areas to try to showcase a new type of form factor.

**18:04** · Um, it's not necessarily because we think it's like the biggest ham or the most important thing to go after, but sometimes you're like, okay, this is like always been a really difficult thing and people have always communicated this way or tried some things this way and can we show that maybe there's a slightly different way.

**18:18** · Um, and because the model capabilities are are so advanced now, can we try to express it a bit differently? Um, what's an example of that?

**18:25** · Yeah, you know, like uh cloud design is a little bit of of that way. I think depending on how you squint, you might see it as like a way that we kind of going into design as as like you know one of the verticals. But more often than not, it's like if you take a look at what we're trying to do with that product, there's a couple of like decisions that were made in there. The first one is that like you can actually try to offload more and more and more to Claude. Um, and so it tries to be kind of opinionated on like, you know, just just like talk to it and like let it really try to figure out.

**18:52** · And yes, you can still edit it and then do these kinds of things, but kind of like discourage a little of that and more just like let just talk to Claude to go figure it out. Um, the second thing was it was really trying to express that actually like code is a is a a way to solve for things that you wouldn't normally think would be the way. So a lot of people who have built kind of generative um you know like slide decks or designs or whatever um will pick uh the way of like they have like some kind of design system you integrate against design system. It's almost the traditional like classic wissywig style of designing something.

**19:22** · And with like quad design, it was like okay, can we try to just like use code purely have Claude generate that code and would it like do a good job? And we found through some experiments early on. It's like actually it looks like it can kind of do that and how can we kind of showcase that uh to the world. So that's like an example. We have a lot of other internal projects and this kind of falls in the category of like expressing form factor.

**19:46** · We'll all try it out internally. it'll be super cool for like two weeks and then we move on to the next thing. We never even ship the thing frankly. But yeah, we actually do a lot of product experimentation in that area and that's like our labs team. And then there's like the second category which is that we actually do look at TAM like we're a business. We do look at TAM. We do look at areas that we think uh you know there' be reasonable agentic like operations that would happen in those areas. Uh we do tend to have an orientation towards things that are more tokenheavy.

**20:11** · And by token heavy or token hungry maybe is the way I would say that is like what we mean is like you know you for spending once you spend a like call it like one turn you look at the end of that turn and you say like am I done or am I actually so glad that I did that thing I want to do more of that thing we like industries where it's like the answer to that question you say I want to do more of that thing so coding is obviously the one that we all know and the great thing about coding is that what it's actually doing is that like once you finished a turn you look at that and you're like that was incredible I'm like unlocked I'm going to do like more. I'm going to build more.

**20:42** · I can do more. And there's other services where it's like actually when you finish that turn, you completed the job and you just move on. You know what I mean? Um, and so we tend to like go into the ones that are a bit more like there's this kind of like iterative flow. You're going to build more, generate more together. Um, and then the last angle that we kind of take a look at is just sort of like, you know, there's going to be certain business functions that we're like, they are the buyer that we like to go to. We want to help them optimize their workflows, help them create better products there. And I think we've been pretty transparent with some of the verticalization.

**21:10** · Like we've done like finance, we've done like legal um and we've tried to kind of like narrow on into specific areas where we feel like by having the right context and the right tools and putting it together in a good form factor is probably useful um for us to to be able to do.

**21:25** · And in each of those areas, we do we're trying to do a bit of like showing the art of the possible across all the different ways that you would accomplish those outcomes. And so for you know like finance for example is a good one. Um, you know, we you could be a company that solves problems in finance and you could build directly on the messages API and you can just get some tokens and you can build everything else on top or you could be someone who builds on cloud managed agents.

**21:51** · You can get a lot more out of the box or you could say I'm going to build a plug-in that or like a connector right that's going to sit within one of our products and within those form factors. When we did recently, we launched like claude for financial services is like, "Okay, cool.

**22:06** · We've got packages of skills and things like this that you could choose to use within our product, within other people's products. We even launch like cookbooks on here's how you would use cloud managed agents to go and do these things." And so, I think for us, it's all kind of an experimentation around like, you know, we provide people all these different pieces and see kind of where they run with it.

**22:24** · And then sometimes we put together products that are just packaging of all of these things like claw tag I think is a really good example like we had been seeing people in the industry go and say like Shopify did this with River um Square Block recently did this with Builderbot.

### Claude Tag Under The Hood

**22:41** · Um, there's like a few of these examples where people said, "I'm going to pro I'm going to build like an agentic platform internal to my company and I'm going to try to give it all the right context and I'm going to make it accessible from Slack or from various other um, you know, platforms that you'd want it to be accessible at." And I think Claude tag was very much a packaging of all those same things that anybody could choose to build something similar but this is how we're kind of like well this is how we're doing it internally and if you would like to just kind of plug in and go here's what that looks like.

**23:11** · What do you think people misunderstood about cloud tag? Because there was all this like ruckus about oh my gosh it's just a slackbot like tell tell us \[laughter\] what the magic of tag is.

**23:19** · No I think it's a great question. Um and I I do think it actually showcases a little bit of where maybe the future could be going. Um, yeah. I think like the I think if you look at products in the past, people are like, "Oh, you really attach to like the form or the the UI almost, right? Like it looks like this." So, it's like super cool. Um, and I think when you look at like tag, uh, it like yeah, like the way you interact with it is that you like literally tag it in Slack. Uh, and so yeah, that is like the interface, but that's not really the important part.

**23:45** · The important part, um, is all the kind of like context engineering and like architecture that we put underneath the hood. So that tag just works. It really should just like just feel like a co-orker like a co, you know, if you go to a company and you onboard and a co-orker comes into your channel and then you can chat with it. It's proactive. It figured out like what's like useful you and um it just gets stuff like done for you.

**24:10** · And so if you think about, you know, especially like nontechnical audiences, this is like it's a huge unlock. you just you literally create a channel and then you atclude or sometimes you don't even atclude and you're like hey I want to be able to do this and do that and I can't figure out this and how do I actually like submit an expense report again and traditionally you think about how to solve that workflow you are going all over the place and you're talking to your manager you're talking to your spin buddy and it's really really complicated and uh today now you just like go talk to cla tag and we do a lot of the hard work on doing the context engineering

**24:41** · the proactivity a lot of the harness pieces I think Andre Kaparthi said it really well it's like it's like an org level harness There's a lot of like complexity baked into that like Kayla mentioned like you can use our APIs to go and construct that. You have to do a lot of the experimentation yourself obviously but this is like an opinionated take from anthropic on like how you can have this really awesome always on uh kind of agent for your entire entire company.

**25:01** · And the bit that's like futuristic I guess is like a lot of that complexity is actually like it's like an iceberg. is like all the stuff underneath it that's actually becoming the harder and harder and like useful part that we're trying to like push through. And I think we'll see more and more like that kind of like tip bit that's like outside in the water. It's just like the interface can actually constantly swap like today, right?

**25:24** · Like Slack is a place where a lot of people collaborate, a lot of business collaborate, but also a lot of people collaborate in teams and some people collaborate by a WhatsApp group um or they text each other or they may some people still email each other and like those could be the form factors that actually completely you can imagine agents just going there and being and they're almost taking up the same form factors as humans have taken up.

**25:44** · It was almost like a very almost like boring take, but it's actually like I feel like the most like forward one because you want the agent and you want AI to basically be like another person and it's helping you, but it's like you know very intelligent can figure out all the context and you can always have it to be a really helpful assistant.

**26:03** · Totally. You talked about context and then harnesses quite a bit and so your team is just, you know, has such an opinionated point of view on like what it takes to build an exceptional agent. I imagine a lot of that comes down to the context engineering and the harnesses.

### Harness Best Practices

**26:16** · Totally.

**26:16** · Maybe like what best practices or advice would you would you share with people about what you need to get right on the harness and what you need to get right on the context.

**26:24** · Yeah, I think so. It's interesting because we've kind of talked about, you know, we launched cloud manage agents as this like very generic but high performing harness because we've done all the nitty-gritty work that's actually like really boring and not super interesting around how do you deal with prom caching? How do you deal with context management? You like clear old stuff out of the window. Sometimes you like call tools programmatically so you don't pull everything into the context window and you can keep it clean.

**26:51** · There's a lot of those sort of details on the lower level harness layer. Um and I think honestly like best practices are just stuff like prom caching. Do it.

**27:01** · You're going to save a lot of money and and token costs. Um, obviously like try to keep your context window clear and then putting those things together in uh a harness that will be performant is is you know sometimes specific to the task that you're trying to accomplish, right?

**27:18** · And then of course evals. Um I'm surprised we got this far into this thing before one of us said the word evals, but like you need evals um to make sure that what you're trying to accomplish is performance. Um, but I think where we're starting to go, and Angela mentioned this a little bit earlier, is more of a concept of strategies or metah harnesses because I do think that yes, you can again make this lower level harness is going to be performant and maybe that's interesting for you to do yourself or maybe not and you offload it to us.

**27:44** · But this concept that you can take any given token and spend that token on just executing or you could take that same token and choose to actually reflect on your past agentic sessions and write learnings to memory so that the next agent does a good job or you could take that token and advise with a bigger model so that a smaller model can execute and do a better job. Um or you can say execute execute and then like a greater comes in is like did you do a good job? No, you didn't try again. Right?

**28:12** · And so I think the the like interesting innovation is going to come more at that higher level on like the meta level, right? And I think optimizing within those strategies is something that our team is really excited about and we're starting to do a lot of work there.

**28:28** · Um, and I think a lot of other people are starting to feel really excited about this concept of strategies and like the jobs you give to tokens because again like yes, there's best practices on stuff like your prom caching and exactly how you clear stuff out of your context window and how you write your evals and like a lot of things like this, but I I don't know that there's necessarily so much juice to squeeze in a lot of cases out of that layer as compared to a layer higher than that.

**28:53** · Yeah.

**28:53** · And one of the reasons for that I think is it has to do with the generations of the the models. I if you look like two years ago, a lot of the harness was like a scaffold to kind of like tell the model to go from point A to point B. And you had to like you really had to like build in a lot. You practically build one wall here and one wall here. So like the thing would go in a straight line. And now the models are actually very very steerable. Um and so a lot of that steering you could just put in the prompt, right? Like go do go from point A to point B and the model like will go from point A to point B.

**29:23** · So, a lot of if you have harnesses um that are like designed to kind of do that kind of like steering, you can delete that part. Like that part we actually frequently encourage like you can delete part of those harnesses. I think various people have said things along those lines. And that's I think what people often times mean when they're like the model will kind of consume some of the scaffolding and like in that sense like for sure if your scaffolding is telling it to go in direction um that it can just intelligently figure out like that I think will increasingly continue to to be so. But as a result of of this, what the harness needs to start doing is more allow it to run longer.

**29:53** · And so that's where like that execution bit tends to be. I think like it sounds like a maybe somewhat silly point, but I do think it results in a lot of differences because because you can go in the direction that you tell it to go. You obviously don't want it to stop at B. You're going to be like, "Okay, now go from B to C and then go to F and then go to Z and then come back to me on A." You know, something funky like that.

**30:12** · In order to be able to do a lot of those things, the kinds of harnesses that you do are less the steering harness and it's more like these kind of strategy harnesses that Caitlyn's mentioning, which allows you to operate at a slightly higher level of thinking which matches I think a lot of the intelligence gains that we're trying to see with the model.

**30:28** · Do you think task specific harnesses make sense or a vertical specific or task specific harnesses?

**30:33** · I think people have different opinions on this. Like our opinion is yes. I don't think there's like a general harness. I think there are some capabilities that are obviously very general and they tend to like be very useful. Uh like coding is a capability that like is very useful because you can use it across so many things and software as uh you know just like eaten so much of of what is capable. So our ability to like write software is therefore useful. I think when you think about like very very specific types of domains they're going to require like a couple of pieces of the harness to be sort of like customized.

**31:03** · One of that uh I do think is how you choose to kind of like handle sort of like errors uh between when you do something and you hand something off to the model. Um, so in like domains where you require like an extreme level of verification, that logic of how you handle that ver like it again, I think it sounds small, but like I totally understand why some people feel like they really want to own the harness because tweaking that last bit will give you a ton of juice and especially domains like like legal and finance where there's a lot of consequences um to you not getting it

**31:33** · perfectly correct like is really going to matter and that's going to be the difference between your product and someone else's product being the thing that the user ultimately uses. Um and then there are other domains for which like I would say uh it's not going to matter as much because you're able to compress it into like a general model capability. So the tweaks that I guess like you know where we feel like the domain specificity is really going to matter is the specific like verification logic between the model and your execution.

**31:58** · And then um I think it's going to be about like some of these kind of like higher order strategies on how well um you're able to actually like allocate your token budget. Um, I think the context bit is actually a little like overdone. Like yes, you're going to like throw in context and like that's uh but any harness can actually handle a lot of context and so that's just more like you have the data and if you have the data then obviously you're you're uniquely qualified to do something useful.

**32:24** · Yeah.

**32:24** · And I think when people say harnesses they often mean a lot of different things and I think this is why in part there's so many different opinions on this. Like you can think of a harness as literally just like a loop um that's like okay cool like user model user model tool you know like that sort of thing. Um then you could think of the harness as also all of the tools that are packaged up with the harness right and and there's just like a lot of different definitions of these things.

**32:50** · And I think the stuff that can be pretty generic and like less interesting to own and and deal with is what I was kind of saying earlier is like getting your prompt caching right right like maybe that is not the world's most interesting thing. Choosing to clear out old tool calls from the context window and and things like that right are like maybe a little bit less interesting and you like go a layer higher into some of the stuff Angela's talking about and then you get into like okay yeah these are things that I might want to own and control.

**33:18** · And so it's interesting with cloud manage agents like the thing that we built today, we call it higher order, but it's not really like that high order in the sense that you can choose to define all of the tools that you want to bring in as custom tools with the harness, right? And like we give you a lot of knobs to control, you can define skills, you can do your system prompts, you can do a whole bunch of different things, MCP servers and things like this.

**33:40** · And I think where you know we want to get to is a point where you can literally just tell an agent here's the outcome I want and here's the budget that I want to spend like ready set go and you may be like don't think about any of those things underneath. And so I think there's just a few different layers of this right that for certain things like you might want to sit at a different layer of what you actually go and control. Um and you can probably get better outcomes within some of those layers by doing a little bit more optimization work.

**34:07** · Very cool. One of the things I'm curious about and one that I love about infrastructure and platform teams is that you get to see what the most advanced users in the world are using and learn from them. I'm curious what are some things that you're seeing and learning from from the people building on your platform.

**34:21** · There's some people that have been doing some really funky ways of like handling context. Um we ourselves explore this a lot. That's actually like one of the reasons why TAG is like uh such a great product is like there's a lot of really awesome like context kind of engineering that that's happening. Um, we've seen some teams be really clever about like how they do that and they are able to kind of think through like, okay, if I have all these contacts in a bunch of different places, how can I proactively go reach out to them? How can I try to generate enough like um permissions across each of them? So, and then feed that all into like an agent.

**34:52** · And it's interesting that like um I guess like this is kind of the level of innovation that like we're actually like very excited by. It doesn't express itself as like a completely different product form factor. Um, but what it actually does express itself as is like maximally useful to users and we've been seeing this more and more with like inter actually like internal use cases instead of like external ones.

**35:11** · So like companies who are becoming more AI native basically they're the ones we're seeing increasingly more and more innovation out of and so you know we've had like customers try to do this for their like they've built their own like custom SDLC kind of setup in very very innovative ways. We've had uh ones who do that for like their entire back office and just like the kind of nuances of how they like stream in context I think has been like actually really interesting in terms of like how they've been putting together the pieces. So that's been like one category that's been like really really like fascinating.

**35:39** · Uh another category that's been like really interesting has actually been with companies that are dealing with like really old school software. And so there's a lot of like healthcare companies um that we kind of engage with and you know like they're like the the systems I'm working with they don't even have APIs. like that's that's a a dream.

**35:57** · Um and so you know how can they use computer use uh and things like this to be able to start to kind of automate and create more connectivity with our systems. Um and that area of innovation I think has been really exciting. It's been really interesting to see people try all sorts of crazy stuff from like taking a laptop and trying to like run a bunch of things on it to autogenerate a bunch of things that then their agents can go and use. Um, and this has actually been probably like an area of um, I think a lot of innovation coming from a lot of our customers that we want to find ways to like support better and see like okay maybe there are like how can we make this easier for you? How can we help you with some standardization?

**36:31** · How can we get it so that you know like you can just have a spec and then claude can then respect it and so it's much easier for you to organically connect a lot of these things. But yeah, maybe the the general theme I would just give you is like interestingly a lot of the innovation that's most exciting out there right now has been uh this kind of like context and connectivity layer which has been really fascinating.

**36:49** · Yeah.

**36:49** · Like a good one in that um we were working with a customer who they've built some agents on cloud manage agents. They also have some agents they built on other models and other platforms and they've kind of optimized each of these agents to be good at the things that they want. They want these agents to all be able to work well together. Um, and they kind of were like, "Wow, Galaxy brain. Like, what if I expose an MCP server on top of this agent so that it can then go and like have this other agent call a tool on that agent, right? And and have these things just be more modular and be able to work together."

**37:19** · And we were like, "Yeah, totally." And we sat down with them and worked through it and and it worked perfectly and it was pretty cool.

**37:25** · And so, we're seeing a lot of again that connectivity layer that I think is one of the cooler areas where people are innovating. But outside of that, one thing that has been cool is just seeing the shift in I guess like industry trends of where we're seeing a lot of our usage come from like talked a lot about coding like coding as a category like of course absolutely explode in.

**37:45** · There's so much going on there and we're starting to see some of these emerging trends like more recently. Um, we're starting to see manufacturing really pick up as just a category where people are building with AI and like one of our PMs like getting on a flight to Detroit to go like figure out what these customers like what they need and what's going on. And so I think we're going to start to see a lot more just kind of like outside of the box of what people think about today sort of use cases which we're really excited about.

**38:11** · H it seems like there's now there's a we went through a token maxing moment of history and now there's like the token rationalization moments of history.

### Token Costs And Whats Next

**38:21** · \[laughter\] What are your thoughts on that and like what what should companies be doing and then how how does the platform team think about uh enabling that?

**38:28** · Yeah, I mean it it makes sense. Uh it it makes sense from the high you start to rationalize. I I really like that framing and I think there's like a couple things that that are like top of mind for us on this front. I think like again it makes sense and as these models get more and more capable you're going to hit like levels of intelligence max maxing that are like there that then you want to do the next kind of dimension and the next dimension after intelligence will either be cost or it will be speed. Um and you just kind of you know go through that across all possible tax complexities in the distribution.

**38:55** · Um, and as we kind of see that like happen, you know, something that's like really top of mind for us that we kind of try to spend some time with users on is like what you don't want to do is like stop AI usage, right?

**39:06** · Like that's kind of the wrong move. And we do actually see some of our our customers do that. So oftent times the way that AI spend has erupted inside their company has been through some kind of like uh shadow IT, you know, like their employees just like want to use it, they find a way, they end up procuring it themselves, and before you know it, like half your or has like found some way to have installed cloud code. And in that world it is kind of hard to to manage because these things are again like they're very token hungry ultimately.

**39:28** · And so what we try to kind of encourage our customers is like okay you don't want to like stop the innovation like if you are getting returns on top of this you are shipping faster than ever before you can like run more operationally like uh efficient then those are gains. And so the area that we actually try to encourage people is like if there is a way for you to kind of construct again like a strategy that allows you to design an architecture that says like given a task assesses level of complexity.

**39:51** · I mean I'm effectively describing a router but like there are ways to do this that are like I think a bit better now and so like this task comes in has a certain level of complexity for that level of complexity like you can define some rules but for the most part right if it's like a hard task you should probably route that to like a big super smart model and if it's not a hard task you can route that to like cheaper models um designing that I think has a little bit of like there's a lot of technical complexity in that but it's like very very doable and we actually like encourage people to try those kinds of things I think ultimately offer rather I I think within the clawed space it will like make sense.

**40:24** · It's actually one of the strategies we imagine like designing because the way that we kind of thinking a lot of these things is like it almost feels like every month there was a new era of something. Um and if we take a step back like okay and this seems to be like really fast and so what are the different ways that are recomposable so we can redesign very quickly for any new whatever the cool thing is that month kind of like bit. Um and so this is like in that category of things where we feel like we can actually just like recompose a lot of our primitives and then design it.

**40:49** · I think the bit that we do feel really strongly about on the model routing front is like we are designing our platform for Claude and we want to make sure that Claude is great at like solving all these things. So we'll like restrict to that space um rather than you know I don't think we're that interested in saying like okay and then you know you should route to a different model or whatever.

**41:11** · Makes sense.

**41:11** · Yeah.

**41:11** · and and well some of that too is just like I think we have a strong belief that harnesses and and just like the agentic layer should be tuned to the model family that you use it with. And so I think there was a period where people were kind of like yeah cool I can like build a harness and build an agent and then just like plug in a different model underneath and they were excited about routers from that perspective.

**41:29** · And I think we started to see um like Verscell just did this with harness agent for example like some of these players in the space like come up a layer of abstraction and say actually like plug in the whole harness and the whole agent that's tied to a model family which makes a lot of sense and so what we could provide is a little bit better smarter like how do you mix and match the right models within the model family underneath that thing if that makes sense.

**41:53** · But yeah, on the general question of token maxing costs and these sorts of things, I think we're just kind of going through what feels like a normal natural cycle for companies and figuring out how to make the best use of this technology and run their businesses really well and really effectively. And um it's interesting like before working at Anthropic I was at Stripe and we were kind of in the very reasonable era of like we paid a lot of attention to our AWS bill and so you know if someone were

**42:21** · to have built some background job and they like didn't quite configure it correctly and this thing's like burning through like CPU or whatever it is right like at any given moment and causing you know big increase in spend that's not actually worth it right like we have put in place the guardrails to find that and then go ask that engineer very nicely to please turn off their background job that's not like within the bounds of of what they should be spending for the thing they're trying to accomplish. I think those are the things with AI that people are going to start to go and figure out.

**42:52** · And I think to Angela's point, a thing that gets dangerous is when you're kind of just like here's a cap and you're stuck within your cap like ready, set go. But I do think that encouraging innovation, encouraging people to, you know, create really excellent outcomes with this stuff and then coming in from the side and looking and saying like, okay, well, there are few different ways that we probably could have accomplished that outcome, right? And one is like you take Opus and you run it all night and you do something crazy.

**43:20** · And another is maybe to get a little bit smarter with the strategies that you put together in order to create that same outcome within a lower cost. And I think that's the like next layer of thinking that everyone's going to start to do.

**43:31** · Very cool. Is there anything that you guys are excited about building over the next few months that you can share a hint at what might come next?

**43:37** · Uh yeah. I mean I know we said this word like 20 million times. I apologize but like we really are trying to build ways for you to compose strategies. Um and so uh that is an area that that we're like trying to move into that kind of like yeah uh coordination layer of the abstraction. Um, and we want to start at this front because the types of problems that we see people building, they are at a layer where it's like in order to get the most return on this, you have to be a little clever about like what is the nature of the problem that you're solving.

**44:04** · So to give you something like concrete like when you try to solve for like let's say you want to build an agent that's like trying to um do bug hunting and you could just send one off to go and do that and it's going to give you a certain type of return a level of return of possibility um and then people kind of get stuck at that and they're like okay my next options are I can like make a bigger I can just like swap the model for a different I probably bigger model um or I could like let it run like longer and that's pretty much like the only two like levers that you have to like try to make this like bug hunting agent.

**44:35** · From a lot of experimentation, when we do these kinds of things, there's like actually the thing like those two those two things are still true, but you actually have like a third lever and tends to actually do a lot more than you think it does, which is that actually if you were to like best of end the thing, it would like give you a lot more returns. But like just to be just saying those words are fine and there's plenty of papers and people have published it to actually build that thing and put it into production so you can actually test it on users uh and see the results for yourself, that's like really really freaking hard. and you end up building all these like custom harnesses so on so forth like you know all that stuff.

**45:05** · Um but we're seeing like this is where the alpha is and it's hard and so like in the same very simple philosophy that we talked about at the beginning like if it's like gives you the return that you want and it's hard we're going to try to make it easy for you so then you can use it to then run the experiments you actually need to run.

**45:20** · Reminds me of when people are talking about agent swarms a year ago. It's some version of that.

**45:25** · Has it been a whole year?

**45:26** · Yeah. Oh my god, I know. We're finally there.

**45:28** · Yes.

**45:28** · Um yeah. No, I think that that's like that's a type of strategy. Exactly. In the same way that you have like, you know, one big one that separates a bunch as another type of strategy. And I think people have thought about this maybe the in the way of like human organization.

**45:41** · I guess it could be similar, but if you take it to kind of its ends, it's actually more just like the token has a job. And I think it's this job piece that we're we're really indexed on and um we see a lot of returns too and that's the thing that we want to spend time with users and the rest of the ecosystem on on like how can we just make that easier for folks to then experiment like we can give you like five jobs off the top of our head and we'll probably like that's what we have internally. Um and if we give this out to the rest of the ecosystem there's probably going to be like 100,000 200,000 who knows what other combinations that people could put together.

**46:09** · Yeah, we want to be able to keep doing this hill climbing on like how do you get the most value, the most intelligence per dollar and just put that power in people's hands, but around the edges of that, we have these personas that have kind of just like things they have to work through in order to be able to like really deploy AI either within their companies or within their products. And um that's like the sort of enterprise ready security and compliance controls and things like this.

**46:36** · But really even just like making the platform more modular in the right ways like being able to plug in different pieces of the solutions that we're building like I want to use memory for this thing over here, right?

**46:47** · or whatever else it is and having a truly excellent developer experience around that because we spent a lot of time with enterprises who are like okay I have this like walled garden and I need to figure out exactly how I can plug these solutions in and so we're we've got a part of our team that's innovating on things like strategies and jobs and trying to help you maximize intelligence and they're like that's really cool but I can't actually use any of that for XYZ reasons. So I think solving those problems is really really important to us.

**47:13** · But then the other persona is you know the like weekend developer who's like I want to go and build something useful for myself right and they're often doing that on top of our platform and on top of many other just pieces of developer platforms in the community. And I think for some of those folks, there's more that we can do to be provide solutions that are maybe more open or more hackable or whatever it might be for those folks to kind of just like go wild with what we can offer them and have this really excellent developer experience.

**47:41** · And so I think there's a lot of stuff that maybe I would put in the category of table stakes that I'm really excited about because I think those are the things that then unlock getting people to say, "Okay, yes, this thing works for me and now I can plug in on some of the stuff that you guys are doing." that's really innovative and hill climby to get more intelligence and save costs and things like that.

**48:01** · Wonderful. Caitlyn, Angela, I feel I mean you are building one of the most important developer platforms in the world and talking to the two of you over time. I just feel really optimistic that that platform is in very thoughtful uh hands that that care about the ecosystem. So, thank you for taking the time today to share what you're up to and um we look forward to what's ahead.

**48:21** · Thanks for having us.

**48:22** · Thank you guys.

**48:33** · \[music\] \[music\]
