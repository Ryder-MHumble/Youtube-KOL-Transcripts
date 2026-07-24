---
title: 'State of Enterprise AI 2026: Aaron Levie on Tokenmaxxing, Rise of Headless, and AI-Proofing Your Job'
source_url: https://www.youtube.com/watch?v=Gs2styCcwro
video_id: Gs2styCcwro
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/aaron-levie|Aaron Levie]]'
published: 2026-05-28
created: 2026-07-21
language: en
speaker_attribution: contextual
description: Aaron Levie, co-founder and CEO of Box, returns to the MAD Podcast with the clearest read in tech on what AI is actually doing inside the world's largest enterprises right now - not the hype version,
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=Gs2styCcwro)

Aaron Levie, co-founder and CEO of Box, returns to the MAD Podcast with the clearest read in tech on what AI is actually doing inside the world's largest enterprises right now - not the hype version, the real one. After hundreds of Fortune 500 CIO conversations this year, Aaron explains why we're still in "day one" of the agent era, why one badly written agent run can now cost $1,000 in compute, and why progress at the AI labs is paradoxically slowing enterprise deployment. We get into the token cost shock now reshaping IT budgets, why coding agents have reached escape velocity while the rest of knowledge work hasn't, the rise of headless software and what replaces per-seat pricing, the emergence of the forward-deployed engineer as the hottest job in tech, why Aaron thinks the AI doomers are wrong about jobs, and where startups can still win as the labs move up the stack.  
  
Aaron Levie  
LinkedIn - https://www.linkedin.com/in/boxaaron  
X/Twitter - https://x.com/levie  
  
Box  
Website - https://www.box.com/  
X/Twitter - https://x.com/Box  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id1686238724  
  
00:00 Intro  
01:18 Silicon Valley engineering vs. everyone else  
05:35 Are enterprise CIOs actually bullish on AI?  
08:51 Tokenmaxxing & why your AI bill is about to explode  
11:34 The myth of falling token costs and AI spend escaping IT budgets  
17:37 The $5B startup hiding in AI compute  
18:14 The mosaic of models inside every enterprise  
21:28 Why coding works and the rest of knowledge work doesn't  
25:53 The Bob and Sally problem: access control breaks agents  
30:31 Will enterprise AI really take 10 years to roll out?  
32:24 The capability overhang: why faster models slow diffusion  
34:23 Data is the bottleneck (it always was)  
39:02 The rise of internal forward-deployed engineers  
41:23 Why the AI doomers are wrong about jobs  
43:43 Headless software is inevitable  
46:14 What replaces per-seat pricing  
47:37 How Box itself is going headless  
49:42 How the org chart actually evolves  
1:00:33 Future-proofing yourself as an enterprise employee  
1:06:40 Are we all just going to work for OpenAI and Anthropic?  
1:07:11 Where startups can still win as the labs move up

## Transcript

### Intro

**0:00** · Let's just say you took GPT-5.5 or Opus and you just snapped the line right now.

**0:03** · You could probably do this diffusion in like 2 years or 3 years and we could probably all do the change management like collectively as an ecosystem. The problem is is the breakthroughs keep happening faster than the customer can implement any kind of standard architecture and those breakthroughs often times make obsolete the last thing you implemented. It's this really bittersweet thing which is like the technology is getting so advanced that it makes obsolete the prior thing that you implemented which actually means that the rollout takes longer.

**0:32** · I am Aitor from FirstMark. Welcome to the Mad Podcast. Today, I'm excited to welcome back Aaron Levie, CEO of Box.

**0:39** · Aaron is hands-down one of the most deeply thoughtful CEOs in tech today when it comes to agentic AI and he has a front-row seat to how AI is actually being deployed inside the world's largest enterprises. In this episode, we get into the \[music\] most pressing topics in the enterprise AI right now including soaring token costs, why AI model progress is paradoxically slowing down enterprise deployment, the rise of headless software, the emergence of internal FDEs, and where startups can still win. Please enjoy my conversation with the always excellent Aaron Levie.

**1:12** · Hey Aaron, good to see you.

**1:14** · Hey, good to good to be back. Appreciate it.

**1:16** · Yeah, thanks for running it back with us. I feel you you play a very special role and have a very special position in our tech ecosystem because on the one hand, you've been a Silicon Valley insider for a while now and uh these days you're as agent-pilled as it gets, but on the other hand, you're a public company CEO and your company sells to the largest enterprises in the world so the the Gs and the Procter &amp; Gambles and Morgan Stanleys. Actually feels like a good place to start.

### Silicon Valley engineering vs. everyone else

**1:44** · How wide is the gap these days between Silicon Valley in the Bay Area and the tech ecosystem in general and the Global 2000 type of enterprises?

**1:55** · Interestingly, we've always sort of played this role and and like if I had to distill like maybe the singular concept we've always tried to think about is basically our job is take super advanced technology breakthroughs and bridge them to the real world. So at the very early stages of a cloud computing, it was like, oh, we can now move like infinite storage into the cloud. Well, to get that to in the hands of of most businesses, you would need a simple interface and you need, you know, advanced security. So so we've always sort of been this this kind of bridge and and it lets us kind of have a foot in both worlds.

**2:24** · One world being like the super advanced, you know, kind of everything is moving a million, you know, miles of you know, a second and then and then the rest of the world which is like there's change management and there's there's, you know, systems that have to be upgraded and all of that. So we saw with that with the cloud and and now we're definitely seeing another version of that with with AI again. I think there's one tiny little asterisk which is which is it's sort of not just Silicon Valley versus everybody else. It's it's sort of Silicon Valley engineering versus everybody else.

**2:52** · And and then engineering though, to be clear, I would say, you know, like if you're tapped into AI right now and you're at one of those names of of companies and you're in engineering, you probably could look fairly similar to to Silicon Valley. So so the bigger question is like Silicon Valley versus versus sort of non-engineering knowledge work.

**3:14** · And that's like the big question right now which is which is what is this sort of path from AI coding agents that we know have totally, you know, reached escape velocity to now agentic work in the in the rest of the organization and you know, what does that rollout look like? What are the use cases going to be? How do these get implemented?

**3:34** · \[snorts\] So you know, needless to say this is the number one conversation every single, you know, customer that that we talked to has at this point and I think I have a decent kind of sample size, probably a couple hundred CIOs just this year across the kind of Fortune 500 Global 2000 type of of of cohorts and and I would say this is the singular, you know, conversation dominating every single every single engagement that we have with an enterprise. It's the main and primary thing that every enterprise is trying to figure out.

**4:05** · We are still incredibly early. So that's like the probably the really big TLDR. And what's interesting and the reason why we're early even though it's like, okay, well, we've been in the AI wave for three to four years, let's say, is everybody just started figuring out like their final rollout plans for like the chat system in the enterprise.

**4:25** · And people have, you know, very appropriately been, you know, proud and happy that they finally got that thing out. And that's still rolling out in some organizations to be clear. Like we still have five years of growth of like the the chat system for for knowledge work. But right as that happens, then the the capability, you know, has has been extended even further. And so then everybody's sitting around saying, okay, as we move from chat, which is like I ask a question, I get an answer back. And so the productivity gain is sort of, you know, rate limited by the human's ability to like have a conversation.

**4:54** · Now I'm actually want to go deploy an agent that's going to be doing things and producing real work in the enterprise, maybe handling tasks, maybe maybe you kick it off by a chat, but or maybe it's just running in a stateful way. You know, and I and I'm pinging it or it's kicking off in a workflow. So now everybody is sort of saying, okay, we think we know how the chat thing works.

**5:14** · And by the way, even though they know how that works, I'd still say that that it's a still changing dynamic market share. You're you're having a lot of changes of of what people are rolling out there. Now everybody's saying, okay, we're going to go deploy agents. These are going to be much more advanced, much more capable. And that's like the big conversation. I would say like we're we're in day day one of that as an industry.

**5:34** · Yeah.

**5:34** · How would you characterize the mood? It's interesting that you mentioned chat because in the conversations I have in my my simple size is smaller than yours. But, you know, there's at least a part of the Global 2000 crowd uh that that would say something like, "Yeah, you know, oh yeah, AI. Uh 2 years ago, you guys uh came to us, and we already needed to do this chat thing, and it was super urgent, and we're going to fall behind, and it was like adopt chat or you're going to die."

### Are enterprise CIOs actually bullish on AI?

**6:03** · Uh and then we did a pilot, and then everything worked out. So, now you're coming back to me like 2 or 3 years later, and you're saying, "No, no, no, no, no, no, agent is a thing, and like this time if you don't do it, you're going to you're going to die." In the spectrum between skeptical and and who yes, Jake, where would you put the mood in in large enterprises?

**6:19** · I would say if I if I did like the broadest sample, I I think the mood uh would veer statistically more optimistic than maybe the framing um that that I think maybe you landed on like a a few extra cynical CIOs uh in that um uh I I think I think cuz what's happening is is the the CIO and and our our main audience is is the CIO.

**6:38** · Uh when we talk to the CIO, they know that their engineering teams are using Cloud Code and and CodeX and Cursor, and they're seeing the productivity gains come out of those teams, and they're like, "Yeah, like my teams are just building, you know, apps way faster. They're they're being able to tackle IT projects much more quickly. Like, we're we're we're doing security reviews faster." Like, they're seeing the productivity gains in their in their function. And I think they're often saying, "Well, how do I bring those same IT, you know, productivity gains to the non-IT parts of the organization?"

**7:08** · And they're having the business pull them and say, "I want access to to Co-work. I want access to CodeX. I want access to these tools as well." So, there's there's actually a certain kind of sex appeal to to these tools right now where the business is sort of demanding, "I want to be on the agentic train because I'm seeing all these these great use cases." And so, I I think the tone is actually remarkably optimistic and excited and and positive as opposed to uh you know, there's there's a sort of, you know, typical trough of disillusionment, you know, from Gartner and the and the hype cycle or whatnot.

**7:39** · I think people are eyes wide open on the there's no free lunch in this. It's not going to just immediately transform our productivity. Um like I I'm we're no longer in that part of the conversation and maybe we were at like two to three years ago. I think everybody is sort of like very firmly aware there's not this thing doesn't just get deployed and magically it goes and transforms the business.

**8:01** · But at the same time they are they're having their employees say, "Actually like I would like this thing to be able to go review all my documents for me. I would like to go accelerate our client onboarding process. I would like to um be able to generate digital assets in our marketing campaign process." So I think the demand is coming from the business and and the IT organization is seeing the gains happening in coding.

**8:22** · And now it's a bit more of a like 30 just practical tactical, you know, issues that I'm sure we'll get into some of them. It's like it's the token cost thing. It's the how do you actually roll this out? It's do you have the talent to go and deploy these things? So So I'm I'm finding the conversations to be fairly positive and and um and increasingly ambitious, but with a sense and and and strong dose of reality of none of this stuff is is is coming for free.

**8:47** · You know, beyond even the cost side, but like free in a deployment, you know, uh sort of manner.

### Tokenmaxxing & why your AI bill is about to explode

**8:51** · Since you mentioned the token cost, uh let's get into it. It's such an interesting topic and it's also a really uh timely topic as we're as we're recording this. Uh there was news that uh Microsoft canceled their internal cloud code licenses this week after token-based billing uh made the cost untenable. And I guess a couple weeks ago Uber's CTO was um talking about this same kind of thing. So that is definitely a topic that seems to be emerging in large enterprises.

**9:15** · Yeah, although although to be fair to be fair, I think the Microsoft one probably got spun in some interesting ways because there's probably much more of a reflection on they want to move to Yeah, cloud cloud code versus Codex.

**9:24** · Yeah, yeah.

**9:25** · Yeah, it's like they're going to be spending on the tokens. Like they're literally going to write on their infrastructure. So So but but uh so I I think the the press really liked to to modify the the the sort of story on that one.

**9:36** · Yeah, very very fair. It does seem to be uh a topic uh that's top of mind though.

**9:40** · And again, I could go with that that tension between like the tech ecosystem Silicon Valley where like token maxing is is really a thing. Whereas large enterprises are are worried about cost. So, what do you hear and what do you recommend people do, your customers?

**9:55** · I don't know if I have good recommendations at actually. But, I would say the token the when we go and talk to organizations right now about where they are with agents, tokens the cost of tokens and budgeting and budget planning and all of this probably is at least 1/3 of the hottest button issues that relate to AI.

**10:16** · And it might even be like tied for number one like half the time. Because what they've seen is is this move from, you know, everybody's sort of calling it like we were doing subsidization as an industry. I don't I don't really think about it like that. I would say that the cost were just low enough that these things were included like cursor just included, you know, a lot of usage and maybe it was subsidization, but it was actually just like they could model that under their subscription fee. Um you know, in a in a in a fairly clean way.

**10:41** · And then all of a sudden what happened was these agents just can do way more work. Their context windows are way larger. The cost of inference is way more cuz they have way more parameters and their capabilities way better. So, so we've just gone from, you know, like the a pricing model of a chatbot or like type ahead functionality in get up co-pilot to a to that pricing model no longer working when when one, you know, agent could be consuming, you know, a thousand dollars of of compute on a single task.

**11:09** · So, clearly like you can't lump that all into a twenty dollar per user per month fee. So, that that's really the the jump that's happened and it's all only happened in, you know, one year maybe less than a year. I mean, it basically all correlates to you can just look at like the Anthropic revenue curve and that that is the period of time where where everything has sort of been flipped on its head on on the the sort of cost modeling and token budgeting sides.

### The myth of falling token costs and AI spend escaping IT budgets

**11:34** · Yeah, there is a an increase in the per token cost for frontier token though, right? So not not just longer running agents using more tokens, it's also the actual cost for the other frontier tokens has increased, which is completely opposite from the narrative that we were all telling one another in the last couple of years, that the cost of token was always going down.

**11:55** · Yes, 100% but I think the one nuance is I'm not I mean I'd be I'd be good to get obviously some of the lab folks on. I'm not 100% sure it's it's just the subsidization change as much as like no like these models are just way bigger and and and they're you know, the hardware is is not getting any cheaper anytime soon and we have a capacity constraint.

**12:13** · So you've got like you've got like a few atypical patterns from from normal computing, which is like usually like there's economies of scale and you don't have the same kind of shortage and so then as you build out everything gets cheaper and you have Moore's law and like we've compressed, you know, normally what should happen in like 10 years of of roll out into like 18 months and so lo and behold, you know, the the data center providers, the labs, etc. have pricing power. They they don't need to lower the prices on anything. So you're not seeing the the typical things that drive down the cost of compute.

**12:44** · I'm highly optimistic that that happens over the next 5 to 10 years, but it's just clearly not happening yet. So we're we're not seeing the curve that you should see in a normal like 10-year cycle of of of compute because that 10 years is now happening in in in you know, 12 months.

**13:01** · So what's happening is enterprises are saying, okay, you know, I'm I'm quite surprised by these bills and and it's like it's a surprise that is sort of like a it's an uncomfortable acceptance surprise as opposed to like I'm I'm not doing this anymore surprise because they're they're like empirically getting the productivity gains or they just wouldn't be paying the bills. It's just it's just now they are saying, oh, okay, this is a a real expense in the business.

**13:25** · This is not the kind of expense that that we just sort of add on 20 bucks per user in our in our head count and now it it has solved the problem. So one of the one of the nuance sort of shift that's going to happen is I think the first two to three years of of AI the IT budget could kind of consume the AI costs and this would show up as okay the company upgraded to Microsoft co-pilot or they they added or they did the add-on of the AI product of XYZ vendor or they could kind of get the cursor like licenses within the IT spend.

**13:57** · And you know as as you know like IT spend is basically somewhere between like three to seven percent of corporate revenue in a in a company. Sometimes lower sometimes higher but like it's kind of trapped at that.

**14:10** · So then the question is like well where is the other 60 70 80% of of revenue in an organization? It's it's opex and it's just like general purpose opex across the business. And so if AI is you know truly adding this productivity gain to your engineering team or your client clearly you don't want to be trapped by this sort of three to seven percent in the business. It's going to it's going to escape that and it's going to move to the line of business budgets.

**14:33** · And so this is actually on one hand it's actually good for the AI industry because you're no longer going to be constrained by IT spend budgets in an organization. On the other hand you have all these now interesting downstream questions which is like the line of business doesn't necessarily know how to budget for compute. This is not a they don't have finops for the marketing team. They don't have finops for for the you know sales team. That that was that was something that that the cloud people had and the IT team could kind of you know go and and and be confined to.

**15:02** · So so I think what what's going to happen is first of all what's interesting is that you're going to have you know this this tussle between kind of like the finance team the line of business the IT team. That's going to be this interesting kind of how do you triage all of this?

**15:18** · You are going to to some extent have to centralize the management of of the the IT systems, management of what do you procure, but then you also kind of have to decentralize the decision-making of how to use these things because really like the CMO should decide do they want to spend a million dollars of compute or do they want to spend a million dollars in doing marketing events or something else? Like that that kind of can only come down to the the business owner that is is driving these decisions.

**15:42** · So and that is again a new type of format of of how do you manage a compute budget in your in your marketing budget and in your sales budget and in your you know global you know manufacturing budget. So that's a whole thing that that now people have to go figure out. One of the things that we don't have tooling for is like how do you measure the ROI on the tokens? Um and it's like it's you know I think it's kind of like absurd and and hilarious to already be talking about ROI this early in the cycle, but I see it is actually it's like pretty practical.

**16:10** · Like there are some things I could do on my computer right now that would cost the same amount of money as as the lunch that my company provides me. And I could do it I could press one button and it could cost me the the the free lunch that I get. So clearly a company's not going to be like oh let's just deploy a whole bunch of tools that people can just like willy-nilly press a bunch of buttons and and you know have the equivalent of 10 lunches, you know, in 10 seconds without knowing like what did were you doing something that actually like produced value for the organization?

**16:40** · Um and and that's that's something that like nobody has tooling for. Employees don't actually really know what what the cost of compute is. So so they're they're going to go about using these systems uh as freely as possible not knowing that yeah this is actually that that one little task you gave that agent could cost $200 because you just happen

**16:59** · to structure the query wrong and and now it's going to go fan out across a bunch of systems and it's going to read like each you know each document or each piece of data in your system and then it's going to go and compute it all. Like that one structure of that of that prompt is the difference between again like your entire benefits, you know, for a month at that company. So, how do we handle all this? I actually have no solutions.

**17:21** · Like it's going to be one of the most interesting questions and some mix of employee training, some mix of of centralized capacity planning uh with decentralized sort of decisions of how do you roll that out? Um you're going to need, \[clears throat\] you know, new new pieces of software probably.

### The $5B startup hiding in AI compute

**17:37** · There's probably a you know, a $5 startup waiting to happen just in like ERP for your AI compute um which is just like how do I how do I decide that that all of this stuff is being used in the right way? How do I measure the the you know, the the the value that it's being produced? How do I make sure that it rolls out to the right teams? Um so, I think that's all up in the air right now. Um and uh and I think this is so new that that the the we're we're we're very short on best practices at the moment.

**18:04** · Look at this, free startup ideas right here on on the podcast. Thank you.

**18:09** · \[laughter\] Wait, is there like a Do you have any royalty uh approach to this or or how does this work?

### The mosaic of models inside every enterprise

**18:14** · We didn't, but we need to now. We'll start We'll start starting now. We'll share the referral fee.

**18:19** · Thank you.

**18:19** · On on this. So, you mentioned not subsidizing, but like it seems that the labs already starting to react to the OpenAI introduced pricing arrangement to just give more visibility into the pricing. Do you think that's going to be a part of how the industry uh evolve as well?

**18:33** · In my long diatribe on on all the problems, I mean a a few things that that will inevitably happen. So, one thing that will inevitably happen is uh you know, OpenAI had has a a great program which is kind of this, you know, dedicated capacity which is okay, if you kind of know your workload, we're able to lock in, you know, certain pricing that helps support that. Like that that that's one way that you could kind of protect your costs. I think another thing that's going to happen is you're going to see this divergence as opposed to again, maybe 2 years ago I would have predicted a convergence, but but let's let's go with the opposite now.

**19:02** · Frontier, you know, AI model capabilities get applied to coding and and advanced life sciences and and like your your contract process and your financial planning process and so that's where you apply, you know, GPT 5.5 high and Opus 4.7 and and you know, whatever the model.

**19:19** · But then once you have a task that is sort of like, you know, you can now perform that task reliably, um you can sort of, you know, that that that once that that capability gets saturated and you can perform that task in a reliable way, then you can peel that off to a lower cost model and and sort of run that on an ongoing basis. And and we just don't have a lot of maturity in doing that really until maybe the past 6 12 months, you know, the models couldn't do any of our tasks that reliably.

**19:45** · So, as this starts to happen, you can kind of say, "Yeah, for that one customer service interaction, I can now cap that at, you know, 50 cents per million tokens and it and it will never go higher than that. In fact, it'll only go lower cuz I might swap it out with, you know, an an OSS model, etc." Um but for my coding, I still actually want the highest capability. And so, I think what's going to happen is you're going to have a mosaic of of models in the enterprise. Um I think the average enterprise will certainly be using, you know, half a dozen models uh in their in their organization.

**20:15** · It's not you're not going to throw everything at the kind of Ferrari model, um you know, from a performance standpoint. So, companies will have to get better at that. Um you'll uh so, you'll need you'll need to have some kind of deeper wherewithal on on how do you you know, how do you you know, shift tasks to different levels of compute.

**20:33** · We're going to have, you know, again new new ways of measuring all this back to the kind of startup idea. There's, you know, some some use cases I think companies will eventually kind of realize, "Oh, actually maybe like that's not something that I even need an agent for. It's like, oh, I just need like software to get deployed in that actually software, you know, is actually cheaper uh cuz it's going to just run on a CPU."

**20:52** · Wait, software is software that's still a thing? That still exists?

**20:55** · Yeah, software It turns out that maybe you don't want your agent to re-render a UI every single morning and uh and that costs, you know, $30 per per day of of using the interface. So, so I think there's going to be a lot of of mixed solutions on this. Not not to mention just like good competition in the market that says, "You know what? Why don't we have some cheaper models to get produced?"

**21:15** · Um you know, how do we how do we start to like like I think the market will will sort of work as you'd expect, which is somebody will say, "Oh, there's actually an innovation opportunity here." And go attack, you know, certain you know, parts of the the market.

### Why coding works and the rest of knowledge work doesn't

**21:28** · All right, so we talked about the mood in the enterprise, we talked about the cost aspect. What else is happening in terms of barrier to progress uh especially on the technical and product front. Like do people need harnesses?

**21:40** · They need more vendors? They need more open-source models? What what what do they need?

**21:44** · They need more vendors. They \[laughter\] need way more vendors.

**21:46** · Uh Uh the answer is always more vendors.

**21:49** · V- VC-backed vendors.

**21:50** · 100% \[laughter\] 100%. Uh uh but but ideally subsidized VC-backed vendors. So, Or great public companies. Yes.

**21:58** · There was uh there was a a a tweet uh I mean, this has come up probably multiple times, which is like like write as much code as you humanly can right now while some of these some of these products are still subsidized. Um and uh and it's it's actually kind of like a funny concept cuz like if you were really savvy, there's probably some parts of the market where you could be like, "Oh, I could somehow use this LP capital to to do work for me as my startup." And uh and and there's like a window where you can find those exploits.

**22:26** · Venture capital actually does have a utility in the in the world. Like subsidizing Ubers and then then subsidizing uh tokens. You're wel- you're welcome.

**22:33** · \[laughter\] People.

**22:34** · Uh so, while the hottest topic might be like tokens right now just cuz there's there's press on it and there's, you know, it's a fun thing that surprises the CFO, I think probably the the the most realistic substantive problem uh and challenge is one more of of technical implementation and the diffusion of of AI uh in this form of agents across across knowledge work. And you've talked about this a lot and you've had, you know, kind of great guests that I think that have covered this.

**22:59** · I don't know how how I'll add to the to the contours of the conversation, but from what I'm seeing is and I think this is one of these things where um you you kind of have to have personally gone through the AI psychosis period uh and then and then kind of come out the other side. And like I've had my phases of like I'll spend all weekend building projects and I'm like this is the most amazing thing in the history of human history.

**23:24** · And and like obviously like you know you're going to have companies that are just one employee and they're going to do everything. And then you come out and you're like wow like actually like maintaining that thing takes a lot of work. I'm I'm having to you know catch so many mistakes that that it's making um and so I'm spending as much time sort of like you know after the project just reviewing everything and changing and modifying or uh the model you know gets upgraded and it kind of you know breaks everything that I just did and now I have to go and and kind of redesign it again.

**23:54** · So so once you're kind of like once you're through the AI psychosis period you you kind of land on the other side and I I guess I you know I'm I'm benefited by both being a power user of these tools but then seeing the real world and kind of like being like oh wow like actually in your particular environment I think there's zero chance that you could have done what I can do on the weekend for fun because I would never allow that to happen from a security standpoint or you know name name your name your reason. So here's here's kind of the litany of of of things that are the work ahead.

**24:25** · So let's just say you you use Claude code or or Codex and you're like this is clearly the the biggest breakthrough of all time and it's obviously going to like ripple through knowledge work and and you know it's going to transform everything overnight or or all the jobs are going to be totally impacted.

**24:39** · Here here's just like the quick kind of like um ledger. So in in coding you have a highly technical user. You have models that are hyper trained on coding. You have you know effectively verified uh you know verifiable work because like the code either like runs and you can QA and you can have tests on it um or not.

**24:58** · You \[snorts\] have You have Back to the technical user piece, it's it's actually like a not a minor point. That technical user, like the moment the agent does something stupid or runs into a problem, the user themselves know how to go fix it and get it back on track. Um and by virtue of them being technical and like wired into this ecosystem, they're just like consuming the news far faster and thus the best practices far faster. So, like when somebody says, "Oh, like how's your skills file or your agent's MD file?" They're like, "Oh, yeah, well, it's got this and this and it's stored here and it's accessible here."

**25:26** · Like that's not the That's not the dialogue and the language of of a of a kind of regular knowledge worker. And this has been talked about a ton by by even like Dor Kashi and I think Dario had a great conversation on this. Like the code base has so much of the context in coding, whereas in the rest of knowledge work, the context lives across like 20 different things, some digital and some very not digital, you know, kind of mediums.

**25:50** · And then this is kind of a a kind of a relatively boring one, but it's like it's going to be probably the most important, which is which is access controls in your code base. Like I can go to most teams in engineering and they have access to the entire kind of portion of work that they need to be working on. Uh conversely, you go to knowledge work and and like you constantly are running into either like, "Oh, like Bob actually had too much access to something." Or Sally had too little access to something. So, Sally has to go ask for something or Bob should actually like have less access.

### The Bob and Sally problem: access control breaks agents

**26:23** · And in both those cases, the agent equivalent that would have been doing coding that just can consume all of the code base that it needs and generate whatever it needs. That agent in knowledge work is going to either bounce up against an entitlement issue like immediately and it's not going to have access to a resource, or it'll have access to too much in terms of resources and then start to answer questions with data that it shouldn't have because the company didn't have like a clean environment for access controls. So, you've got kind of kind of five or six reasons that that AI coding looks very different from the rest of knowledge work.

**26:55** · Um and so what what the implications of this are is is that is basically like diffusion is going to take time. And we have increasingly the right kinds of applications for this. Like Cloud co-worker is awesome. You know, obviously Codex as a super app is is is emerging as this, you know, powerful workhorse. Uh Gemini with I think Spark and and whatnot, you know, I think there's like rumors that Cursor might might, you know, try and try and evolve um based on the the space tech relationship. So, I think that the tools are increasingly coming and or there.

**27:25** · Now you have the hard part of like how do I deploy this in my organization in a way that is safe, in a way that is is reliable, in a way that my employees aren't going to kind of create some crazy blast radius of security challenges, um in a way where where employees sort of know like what is the right way to go wire up this workflow that ends up being useful for them. So, you have this huge tech you have this huge AI kind of diffusion challenge.

**27:50** · Um uh it's it's a much more technical problem than than I think we we sort of got used to with the chat paradigm cuz chat chat was like basically it could do two things. It could it could access search and it could access the LLM. And that and that was amazing. And but guess what? Neither of those things has a permission problem. Neither of those things required wiring up some other system where you could have massive data leakage.

**28:13** · Yeah, it's just a just a DLP problem at worst, right?

**28:16** · Just a DLP problem. And and honestly like in many ways not that different from somebody going to Google to say like I want to go research this customer versus going to ChatGPT and say I want to research this kind of like like almost nothing has changed about the security paradigm of that enterprise.

**28:30** · So, maybe the prompt could include a little bit more IP, but like but like the work you were doing was not like like like that the the blast radius of that work was was kind of quite contained.

**28:40** · Conversely, I go to an agent and I happen to have access to the Salesforce MCP server. And um uh and and it's it's actually incredible. And it's actually one of the reasons why I totally believe in headless software. But I can do like I could do a lot of work with with that.

**28:55** · And I could pull out a lot of data. And I can ask a lot of very powerful questions. And a company's going to have to say, well, should every employee have the same level of access? And And how should we make sure that we've cleaned up our access controls for that? And how do we tell people again like what types of queries should they be doing that are going to have different kind of cost profiles? And now you have to do that for each of your software, you know, vendors and and applications. And then you have to figure out like what is the new workflow on the other end of this?

**29:21** · Do you really want employees prompting, you know, their way through the work day across lots of stuff? Or do you want some standardized best practices? And then you're like, okay, well, now I have to build skills internally like like, you know, capital S skills. And And I have to have or I have to have, you know, various kind of not, you know, knowledge graph or other other ways of getting agents to the right information and the right kind of context. All of that is highly technical work that is going to take 1 2 3 5 years of building out across most organizations.

**29:48** · The really good news for I think 90% of people, maybe other than like the super AI accelerationists, is is that that work means tons of opportunity. It means actually there's a lot of opportunity for startups. It means there's a lot of opportunity for like new kinds of roles.

**30:05** · One of the hottest topics also is like, you know, we have a lot of customers asking us, what is this new internal FDE role or external FDE role? Like what is the technical talent I need to go and actually like help me deploy these types of systems? Um, uh, so you you have we we're in for years of this kind of diffusion and it's it's it's just non-trivial. Um, and every company has to go through it one by one. Um, and uh, and and that this is the the kind of journey that we are all now on.

### Will enterprise AI really take 10 years to roll out?

**30:31** · Do you think it could be 10 years? Like the cloud took much longer than than everybody expected and that was uh, ultimately an IT problem, not an enterprise-wide problem. Do you think this could be just taking, I don't know, over a decade?

**30:43** · Partly, I don't know how we define like it and this because because I think it's actually a continuous It'll be a continuous sort of evolution and not not to like, you know, play semantics, but like it's more like It's more like what what do we think the end state is? And again, I think the AI sort of either doomer or accelerationist think there is some end state. I actually don't think there's an end state. I think this is a substrate of how work happens and it will just constantly get better and we will have to constantly move up abstraction layers. And like it's not even obvious to me like what the end is.

**31:13** · It's just like it's a new way to to basically execute work. And some areas that will be a 5x productivity gain, other areas will be a 10% productivity gain and that will roll out and then in 5 years from now we'll find the next version of that and I think it's this always kind of evolving landscape. But but I think that we should totally be thinking on the order of 10 years as like a as a rough type scale for like whatever it and this might be.

**31:41** · Like it like if you want to be like when does, you know, um Coca-Cola or Procter &amp; Gamble like have agents running around doing every single task in the enterprise like across every crevice of the organization hyper successfully, that's a multi-year, you know, kind of transformation. And I'm you know, making up an example, maybe they're already there in particular, but this is this is just what's going to happen. Now, a funny thing, our industry is actually like some of this is actually weirdly a byproduct of the industry. So, we have this incredible capability overhang which is like, let's just say you took GPT-5.5 or Opus and you and you just snap the line right now.

**32:15** · You could probably do this diffusion in like 2 years or 3 years and we could probably all do the change management like collectively as a as a as an ecosystem. The problem is is the breakthroughs keep happening faster than the customer can implement any kind of standard architecture. And and those breakthroughs often times basically undo or make obsolete the last thing you implemented.

### The capability overhang: why faster models slow diffusion

**32:37** · So, so it it's this really bittersweet thing which is like the technology is getting so advanced that it makes obsolete the the prior thing that you implemented, which actually means that the rollout takes longer because we have no stable there's no stable environment to roll things out in.

**32:53** · If you went to an enterprise right now, it's actually a period of maybe the least amount of of consistency I've ever seen in in IT of of like the following question, "I want to go deploy an agent to to do client onboarding or to review to review, you know, some set of of you know, knowledge work in the enterprise." I could probably lay out up to 10 to 15 reference architectures to all solve that problem.

**33:18** · That means that that every systems integrator, every, you know, software startup, every lab is pitching a customer 10 to 15 different variants of of what they should do to solve that one problem.

**33:35** · And so, what that actually leads to ironically is is more, you know, lengthy sales cycles, more kind of complexity in decision-making because you're like, "Man, that Anthropic managed agent thing looks incredible. This is really awesome. Like that that's exactly how we should do it." And then you're like, "Oh, this, you know, OpenAI frontier is is really good." And then you're like, "Oh, but this startup is actually pitching me something that means I'm I'm neutral to either of those." And then you're like, "Oh, no, actually my workflow vendor can now do this." And it's it is a madhouse on that front right now if you're if you're a CIO.

**34:05** · And so, like one of the memes is nobody's signing up for more than like one-year deals with the labs. And and part of that is because of the the pace of innovation that's happening. And so, it's it's a byproduct of actually how how much innovation we we are seeing, but that means diffusion ends up taking longer than I think, you know, most people think.

### Data is the bottleneck (it always was)

**34:23** · Fascinating. What do you recommend people do in your conversations given this litany of things that need to happen and the space of innovation, all of it that benefits time. You mentioned internal FDs. That's super interesting. We can talk about external FDs, which I think is a better understood thing.

**34:37** · Where should people start or how do they accelerate?

**34:40** · So, the one part where I'm just like, I you know, I'm a I'm a hammer looking for nails is I see most things as a data problem.

**34:47** · Um and and and data with associated things like access controls and like how well defined is the workflow, etc. So, so most agentic challenges I I think are kind of inversions of of of uh basically like you have a data challenge. Like the agent can't get access to the right information to to do the work. Uh maybe they have access to too much information, in which case then then they're just going to like roam around and do the wrong thing. Or they have access to too little information, in which case obviously they're not going to work.

**35:15** · Or they don't have enough context to be able to execute the task, and which means they need more information, you know, surrounding the task. So, so we we see data problems everywhere um that that we look. And so, I think one of the first steps is like your enterprise just needs to be prepared from a from a data standpoint and from a from a a kind of a core architecture. And I think we for 20 to 30 years in IT, it was sort of okay to to sort of have all these systems, some redundant, some not well managed.

**35:43** · You could kind of throw humans at the problem and just sort of say, "Yeah, like the data science team knows like where the the the bodies are buried in the in the database." And and and they know what table to use and what table not to use. Um and and they know how to go and and kind of like work through through the through that particular sort of, you know, data model.

**36:05** · And so, when the business asks the question, the business goes to their analytics team or data science team and they say, "Hey, tell us our attrition rate or tell us our growth in Spain or or, you know, tell us our upsell rate of this product." The data science team is this kind of constrained centralized function that's maybe, you know, 10 people or 100 people, but it's not it's not every employee. And they go and they they know how to kind of like work the numbers and have like another spreadsheet that's living on top of of Tableau and and then they're moving some stuff in there and they're doing some calculations and then they give you the answer.

**36:35** · Now all of a sudden you're like, oh well well I'm going to I want to go democratize that to everybody and and now I want to MCP into whatever the the data you know store is of that thing and then guess what? Like everybody's getting a different definition to to their query because actually the way that company calculated things is like it's like no they do an FX adjusted number or they do a or they they they measure their you know net retention rate differently than what the model was trained on and so all of this stuff

**37:02** · where where you now actually weirdly have a data problem and a data integrity problem and an access control problem that actually becomes one of the more meaningful kind of projects ahead. I think you're smiling way too much which means either you find it something here or you're seeing it or I don't know but It's it's just I'm smiling at the you know old problems are a new again and effectively we're talking about a semantic layer which you know I guess it is getting rebranded as an anthology and that's the new new thing when in reality it's been the same problem for 20 years plus.

**37:31** · 100% it's been the same problem for 20 years but but again we could throw people at the problem before like like at the end of the day when I had a question about data I know exactly the person to go ask and I didn't I didn't ever have to worry about it like I like as Aaron you know in a in a company because the data science team had to worry about it.

**37:48** · Now if if somebody gives me access to that data as a resource and I start asking questions boom that's a way bigger problem because I might go to somebody be like, hey why did why did we like grow you know 13% in that one area and they're like, well your data is wrong like it's actually it was 16% you just didn't adjust for FX or whatever. It's like much bigger problem now when everybody can go and do that.

**38:10** · So and that's just the structured data.

**38:11** · Think about all the unstructured data, you know most enterprises have five different places where their contracts are being stored, you know their road maps are across you know 30 different locations uh inside of their their data environment. That's obviously the space that we see day in and day out. So, if you're going to have a world of agents and you want to have some flexibility on what agentic platform you deploy and what what type, you know, do you deploy co-worker do you deploy manage agents or do you deploy codex, um then you need to get your data into a format that is going to work within that that kind of agentic ecosystem.

**38:41** · So, I think a lot of the work to be done is is sort of blocking and tackling in in the enterprise on IT, which is like how do I get agents that context? How can they make sure they have access to the right information with the right security levels, with the right entitlements? Um and that that is a big chunk of of work ahead to ensure that agents are going to work properly. To do that, that's where the kind of internal FTE motion comes in. So, um we are seeing this increase.

### The rise of internal forward-deployed engineers

**39:08** · Some of it is sort of repositioned internal IT people or software engineers. Some of it is just straight-up hiring new new kinds of people and talent for the organization, but I do think this is a highly technical skill. It's a highly technical role, which is do you have technical people in your organization that you can say, "I'm going to have you go sit next to the business or within the business, and your job is to understand the patterns of how these people work, and make sure that they have the ability to use agents to go and and do that work?

**39:36** · And some of that will be agents for people that are prompting, and some of it will be agents that kind of are just working in the background and like and, you know, automatically producing value for that knowledge worker. But, your job is to go understand the workflow, understand the process, and then marry that with with the the the full potential of where technology is going and make sure that like the data set up the right way, the instructions for the agents are set up the right way, you know, you have the right, you know, sort of human in the loop elements of doing that work. That's a that's just a ton that's a lot of work for most organizations.

**40:07** · And I and it's going to be one of the Except except if you had meta and you you do that by putting software on everybody's desktop. Yes.

**40:16** · Yeah.

**40:16** · Yeah. I think um that might be an end of one uh situation. So, uh so so you know, for for mere mortal companies, you're going to have people going and doing this. And those people are going to look like the next generation of a software engineer or kind of IT engineer. Um I think it's actually incredibly exciting work because you get to go and transform like how does a life sciences company run?

**40:36** · How does a How does an industrial giant, you know, operate? How does a How do marketing campaigns get produced? So, it's actually like very I think exciting technical work. But a lot of companies don't have this talent right now. So, they're going to actually have to go and hire, you know, people out of CS programs or or, you know, be able to pivot engineers into these kinds of functions. Um and you know, as an asterisk, it's actually why the doomers are also wrong about jobs because this is actually going to be a very real sustaining job that is not like a one-time you implement the the agent and you upgrade the system and then it kind of works forever. It's like, "No.

**41:07** · Like, once the model changes, there's another set of work to be done. Do you have to make sure like did you get the gains of that model improvement? Or did you have to leave behind some scaffolding that you had to build for the prior model?"

**41:20** · Like lots and lots of work to be done in uh in in this area.

### Why the AI doomers are wrong about jobs

**41:23** · Do you mind if I say so? Do you think that the external FDE position is here to stay as well? So, internal FDE being within the enterprise, external FDE being within the the vendors. The slightly cynical version of FDEs in startups or larger tech companies right now is that well, none of this really works. Therefore, you need to deploy a chunk of of humans to uh come on premise at the customer and and and make it work.

**41:50** · But I think what you're saying is more profound and that this is uh going to be a fixture rather than a a temporary thing.

**41:58** · Yeah, it's it's so funny cuz the AI uh super accelerationists, which sometimes actually end up in the same quadrant of their views of the doomers, and the let's say, I don't I don't know, skeptics um as as another, you know, kind of end of the continuum. They land in the same spot in this particular topic. They're like, "Man, I can't believe we have to have people go and do this. It's like It's like it proves the skeptics, you know, right and and somehow the doomers and the accelerationists are like, 'Oh man, like it's not happening the way that we thought.'" And and then it's sort of the cynical thing.

**42:29** · And and what's funny is is like you have people like me that are like, "I just know enterprises." And it's like this was obviously 100% going to happen. Like, you guys are all crazy if you didn't think this was going to happen. And it neither proves that the technology is not amazing, nor does it nor does it prove that like like like it's just like like it obviously had to play out this way. Why did it have to play out this way?

**42:51** · It's because we built this insane technology that's like incredibly using computers, incredibly at using software, incredibly at writing code, incredibly incredibly at writing tool using tools. And but guess what? It like has, you know, a fixed amount of memory. It has a fixed amount of context it can work with. It It couldn't do totally dramatically crazy stuff with your data. Like so obviously it has to be like implemented by somebody hyper technical.

**43:19** · Obviously it has to be like implemented in a way that drives change management in an appropriate way like for that organization. So like it's like to me this was 100% priced in and and the market just took way longer to get there than than I think anybody would have realized. Like Like you could just feel this the moment you saw agents be real.

**43:38** · You're like, "Yeah, this is amazing and it's totally going to take a lot of work for enterprises to go and implement this."

### Headless software is inevitable

**43:43** · You mentioned headless software. Is that inevitable in your opinion and and clearly the future?

**43:49** · I think the headless conversation ends up usually in the same kind of spot as as, you know, almost every other technology kind of trend in history where you're like you always think that the next medium fully eradicates the prior medium. And and then you just like you're like, "Oh, no, actually I do have an iPad and a MacBook and an iPhone."

**44:05** · And like and for some reason I don't just like use my iPad as my phone and I and with a computer. It's like, "No, I have three devices. They all do something different." Um and so so I think I think it's going to just be one of those things, which is which is if I'm going to go and do a complex query that involves Box data, Salesforce data, Workday, and it's got to triage a bunch of stuff, I'm going to do that fully headlessly inside of coworker Codex or something else. Like unquestionably.

**44:29** · If I want to go and like work on a set of documents and build a data room and and go and make sure that I've I'm sharing all my contracts the right way, at some point like doing that via text is sort of slower than just doing that in a graphical user interface and with all the knobs that I know how to, you know, interact with. And I get a lot more leverage that way.

**44:50** · So I think it's just going to be this sort of dual dual model um with the one nuance being probably by like by like um, you know, database queries headless will just be a hundred times larger than than the than the interface-driven, you know, way of of doing work. Um and so so we'll just have to understand that like like by volume agents are going to be banging on these systems far more than humans ever did.

**45:15** · The human will probably land as a an end user seat, um you know, within that that piece of software and they'll get a certain amount of allocation of usage as that end user seat. And then they I believe that they should have a right to use their that software and that data via agents um up to a certain amount uh and that certain amount will be different based on the vendor depending on like how compute intensive is that workload. And then past that certain amount or when it's fully just an agent, then it'll be a consumption model.

**45:40** · So I think any any enterprise software company in three years from now that sort of that that gets through this AI transformation period, it will have a seat business model assuming it has an end user component, and it'll have a consumption business model. And that consumption business model in some business might be bigger than the seat model, and some might be smaller just cuz the seat still takes up so much, you know, kind of uh you know, uh set of the work.

**46:04** · But I don't believe that we move fully to consumption and fully to headless because I think there's a lot of reasons why you still want to go into the interface and and poke around for for a bunch of, you know, kind of reasons.

### What replaces per-seat pricing

**46:14** · And do you think it's necessarily humans have a seat and agents have consumption or would there be an argument for saying that agents in some way are not that dissimilar from from humans although they they'll be doing a lot more with a lot more volume of data and therefore there should be some kind of like seat based pricing for agents.

**46:33** · I I think I think this is this is sort of a tougher category because it all depends on the agentic use case.

**46:39** · So like I can totally see a world where we already have some customers playing around this idea of like should agents have a box seat because because why?

**46:47** · Because they actually need to store data that gets retained and governed over a long period of time and you want to be able to track it and manage it just like a person but it's got to be stateful and so that kind of makes sense as like we have to give it a name and a thing in our system to make that work.

**47:02** · Do we charge the same as a regular end user seat? Probably not. Probably it's got to be cheaper. But then there's a lot of situations where the agent doesn't need an ongoing seat. They just need to be doing a lot of operations in which case it's it's probably just pure consumption. So I think it really depends on where does your software category land on is there a reason why

**47:22** · you'd have an agent be stateful in that organization and and and kind of take on an identity and take on ongoing work versus it's a thing that just every employee calls on demand and that that would probably determine you know, what that business model looks like.

### How Box itself is going headless

**47:37** · What does headless mean Box? How do you guys go about it?

**47:41** · We kind of think about it as everything you would ever want to do with your enterprise content you should be able to do via an external agentic interface and so the examples are let's say you want an agent to go and like read through you know, 100 contracts or review a data room that you've created for risks in a client. We just launched this example with the cloud for for legal solutions announcement.

**48:03** · So, you can put all your contracts in a folder and then the agent within, you know, cloud co-work can go and and kind of work through all of that data and use it as a knowledge repository for its work. You could do you know, a client onboarding process where the client has to upload a bunch of documentation. It's got to get stored somewhere and then processed.

**48:21** · All of those are situations where Box will be the back end sort of behind the scenes for some kind of agentic work that's happening whether the user is sort of interacting with the agent or the agent is just kind of running, you know, on some kind of deterministic or non-deterministic event that happens.

**48:39** · And what's what's, you know, we we kind of like conveniently have not had to do like massive, you know, kind of crazy transformations of the model because we've always had an API basically like almost on day one of the business we had an API. So, for us whether it's a headless agentic user or a headless system machine application user is kind of, you know, eventually it talks to our system in in roughly the same way.

**49:04** · There are some nuances which is like, you know, headless users might want to sign up for the service on their own. And so, we we've had to think about like account provisioning differently or they might use our search in a different way where they need more context than what a platform deterministic use case would would have looked like like like they're going to use our search tool a very aggressively.

**49:25** · So, we have to, you know, inform them as they're doing their searches, you know, how to think about this certain context, you know, that that that's inside these files. So, there's a lot of work that we are doing to make our system better for agents, but the concept of being headless and the concept of being API first is kind of wired into our DNA.

### How the org chart actually evolves

**49:42** · How do you think org charts evolve? So, we're going to have agents, we're going to have internal FTEs. How does the rest of the organization evolve. I'm sure that must be a key real concern when you talk to global 2000 companies, right? Like the whole partly you know, AI is taking my job kind of thing.

**50:03** · This sort of relates to the AI coding versus the rest of knowledge work and and you know, I kind of set it up at the very beginning on obviously this diffusion thing. But the reason why I'm I'm less concerned about the job part and more optimistic is when we most get fearful of jobs, we look at coding as the example.

**50:20** · And again, back to this coding issue, coding has this other unique property that's kind of different from a lot of the the rest of knowledge work, which is if I write code and and it's like super sloppy because the agent is writing this code, it kind of at the end of the day doesn't matter short of like a a security risk or maybe like, you know, it's using extra memory that it shouldn't use or or whatnot. If the software just runs, like if it's like I could throw I could I could have you know, an application that has 100,000 lines of code or 1,000 lines of code if it's doing the thing that it needs to do, it really doesn't matter.

**50:51** · And so so this is sort of why you're seeing a little bit more like hands-off the steering wheel emerge in in coding and it's like we're just going to throw agents on agents on agents and and then that's going to go and solve the problem.

**51:04** · Take take you know, the other maybe most topical category is like legal as a as an alternative. In legal you you can't do that. I can't have online, you know, 2004 uh of the contract it it sort of like adjust the liability rate, you know, slightly cuz cuz I had an agent go and write this thing whole cloth.

**51:23** · Um that that doesn't matter like there's no way for me to verify the the I mean, I can layer on agents and agents and agents and they review each other and then they review each other again and and I can get kind of down to smaller and smaller percentages of risk. But at the end of the day, you're still going to have some lawyer that has to basically say I I believe that this is 100% valid and I can, you know, put this up for my client or I can go in and you know, ship this.

**51:49** · Um and so this last mile of agentic work, I think it's going to remain in in in a much broader set of knowledge work areas than I think we realize. And there was um I I I mentioned this a little bit in the past, but there was this funny article from the Financial Times like 3 weeks ago of like lawyers being inundated with um uh with all of these like, you know, contracts that their client, you know, created or you know, the client went to chat GPT and asked a bunch of legal questions that now that the lawyer has to go and adjudicate and kind of provide, you know, answers on.

**52:19** · Uh and I think it's a it's kind of a microcosm of the the real-life kind of application of AI, which is it excel it can accelerate one thing massively. I can review the contract far faster and I can go and get to the risky areas or can generate a contract much faster, but in both those scenarios, there's still a lawyer on on either end doing real work. And so, I've removed one part of the bottleneck, still I'm constrained by another part of the bottleneck.

**52:46** · And so, um and so that that's just why like the jobs don't get eliminated as as sort of the first thing. But the second thing is is, you know, we've we've talked about this, but but and the market is I think fully beaten over the head on Jevons paradox, but but nobody ever factors in the Jevons paradox thing. And I mentioned this with designers, but designers are kind of like a you know, kind of a maybe minor example relative to all of the all of the areas where this is going to show up, which is if you go to Caterpillar or Eli Lilly or Johnson &amp; Johnson, you know, John Deere, I'm just naming like big industrial companies just like not in Silicon Valley.

**53:17** · These companies forever, they they want the top engineers like everybody else. They they they are working on incredibly mission-critical, you know, areas of of, you know, creating a new drug, building autonomous um uh you know, kind of industrial equipment. So, they need top engineers like everybody else. They have to go and sign up for similar-level scale projects as everybody else. But those engineers have largely sort of seen that that no, like you go to CS and then you you you go to Google or you go to Meta, etc.

**53:43** · So, what's going to happen now with agents is all of the sudden that all of those other companies are going to light up far more technical projects and technical work in their organizations because for the first time ever one of their engineers now has the capacity of three or five or or 10 or whatever metric you want. And so that's going to get them to sign up for way bigger projects than they would have been able to afford, which means that that they now are that have a greater demand for that engineering capacity.

**54:11** · And then you throw in one more category, which is every basically small business on the planet is going to, you know, be able to go and and augment any of their functions that they wouldn't have had internally before with agents. And each of those functions, back to the human in a loop component, often will need some human to be going and doing the extra work that it takes to make that that that agent actually effective. So, let's say you want to do the marketing campaign agent and you're like a solo entrepreneur, maybe it's a three-person team, and like you're doing it and you're moonlighting, but then you're like, "Oh, this is actually really effective.

**54:42** · This marketing campaign's working." Probably the next thing I'm going to do is go hire a marketing person to go and manage these agents to go and do this at scale. So, you you I'm I'm like a complete Jevons paradox pill person because I first of all I see it in our own business, I see it in customers, and I see it in small startups where these startups are hiring as fast as possible because they've all these job functions that their productivity gains are causing them to need to hire for.

**55:06** · So, this is this is sort of, you know, you can kind of pick your your argument, but there's like multiple reasons why the job argument ends up falling on its face once once you start to see actually how AI is rolling out in in a lot of organizations. I mean, so, you know, for us as an end of one example, I mean, we continue to hire in a decent percentage of the functions that we've always had.

**55:28** · Just the work that those functions are doing just is going to look entirely different in the future because they should be augmented, you know, you know, meaningfully by by agents doing doing additional work for them. Um it's it's certainly changing what we can invest in and and what we tilt toward. Um but some of that is actually just a byproduct of our business evolution and and where we're seeing demand in the market. Um but you know, we're we're hiring people in marketing. We're hiring people in uh we're hiring engineers uh quite actively. We're hiring people in IT to build these agents. We're hiring sales reps.

**55:58** · Um so so like those contours aren't aren't shifting as much as as one would expect at like the at the, you know, name of the job title. Um if I if I had to, you know, really, let's say, lean into the future scenario, uh I think I think what happens is is, you know, there's some kind of embedded AI IT capacity in most functions.

**56:21** · There will be a uh there'll be an AI person {slash} team in sales and an AI person {slash} team in marketing and at different subsections of marketing and they'll be in they already exist in engineering cuz engineering has been going through these sort of productivity gains. And I would I would assume that that person {slash} team, their job should be looking at like, "Hey, what do you do every day as like a demand gen person? And how can I bring automation to that? So we could be testing five times the number of campaign, you know, ideas and keywords.

**56:52** · Uh and we could be integrating one part of the design process to to a campaign life cycle much faster. So so you have a kind of a technical sort of person kind of wired up next to the business. Um and do over time, like in 20 years from now, is that maybe just the new expectation of one of those business people? It could very well be. And then and then you'd kind of compress that, which is like the new job like it might be that in 10 years from now, if you go into marketing, you also, you know, basically are going to be a CS minor equivalent of whatever agents are doing.

**57:23** · And your job is like you better know how to wire up a full agentic marketing workflow, not in like again, I chatted with ChatGPT, but like I could I could deploy a full end-to-end marketing campaign, you know, as as one of the tasks of marketing.

**57:38** · Right now, that that doesn't really exist in in most areas of knowledge work. That might change. Again, I think I think, you know, feels like it's every function augmented by agents. And then in some companies, I can totally see the scenario of where where the perceived risk is. So, in some companies are like, I had 10 designers, but if I had an agent next to my top five designers, they would just do all of the the all of the stuff. I think that's very very plausible.

**58:03** · But but there's going to be then equally 20 companies that say, "I can now do design, you know, for the first time ever in a in a very kind of high-quality way." And those people will just take those five designers and employ them for the first time. So, on a net jobs basis, that is why I'm kind of largely unworried is is I think what happens is, you know, there are definitely some companies that that reached saturation of their their particular demand of a function already with humans. And so, agents coming in, they don't have more work to do.

**58:34** · But but I think that's like true of maybe 10% of the economy. And the rest of the economy is like, "Oh my gosh, like actually, if I could have one designer that now does the work of 10 designers, then that's the first time I can go and hire that designer because now they can be doing websites and campaigns and videos. And and so so I think you're going to see some collapsing of obviously like all of the micro adjacencies of functions, but but not so far that it breaks and collapses like entire domains of work.

**59:06** · Um I I don't I think that there are people that have an eye for design. Uh and I think the people that have an eye for design will just be the you know, both designers and managers of agents doing design. I don't think that may means you take a copywriter and you make them a world-class designer. Uh just as in engineering where we're already seeing obviously this kind of like tension. Uh like I think we're already coming to the other end of it. There was this period which is like oh the product manager can ship production code. And it's like okay, but it's probably going to be slop.

**59:37** · Or the engineer doesn't need the PM because they can like write their specs and it's like okay, but who's going to get on the call with the next 20 customers when when you want feedback on that feature? Do you really want your engineer taking from their engineering capacity time to go do that? And it's like no, those actually make sense as specialist jobs. Like like Adam Smith, you know, figured this out a long time ago. Like division of labor is like a really powerful thing. Agents haven't fundamentally changed the concept of division of labor.

**1:00:02** · There might be some new definitions of of where the divisions fall, but like you probably want your designers being really good at design.

**1:00:11** · You probably want your sales reps really good at selling. You don't want them having to like do like lead generation as a side project. You don't want your your product manager trying to figure out how to become a designer. Like I I think that there's less collapse than than the superb again kind of like, you know, hype train is on right now. But there's probably incrementally more collapse than what we would have thought 10 years ago.

### Future-proofing yourself as an enterprise employee

**1:00:33** · If I'm a an employee in a large company, so again G, Procter &amp; Gamble type companies, how do I future-proof myself? What what do I need to do today so that I'm not caught flat-footed?

**1:00:48** · Not not to get too kind of like paternalistic on this, but but I do think that companies owe uh owe the the you know, employees and broadly society some some help in this regard. I think there is a kind of a social contract which is like you probably do want like the next generation to be having jobs and you probably do want like people to not have complete and utter fear when they're leaving college

**1:01:15** · of like are there jobs on the other end of this or am I moving into this kind of ruthless dystopian environment?

**1:01:22** · Yep. And booing famous CEOs at graduation speeches.

**1:01:25** · Oh, totally. And that's just like the beginning, right? Of the of the issues.

**1:01:28** · So So I I think like I mean, I'm I'm I'm like I'm the most deeply kind of pro-AI, pro-innovation, pro-acceleration person you'll find up to the one point which is which is if you if you stop caring about the overall, you know, sort of societal impact and and people side, then then like not I'm not even worried about like the revolts of like, you know, you know, we're going to get socialism or whatever as like a political matter.

**1:01:55** · It's just like it's just like society works really well when like people want to work at companies and and and they and they can, you know, they can feed their families and and and you don't want to blow that up just because you wanted like one extra point of of operating margin. So I do think companies owe owe their employees and the future employees a real shot at upgrading their skills and upgrading their talent. So like some percentage of this is on the company themselves for the upskilling, for the training, for the enablement, for all of that.

**1:02:23** · Now, once you've done all of that, um and and as a hedge, as a as an employee, I'd be doing this no matter what because I I like I'm relatively like like to go on my own and do everything, so it's very easy for me to say. But like as an employee, I would be spending, you know, 5% of my time, 10% of my time, whatever you can kind of carve out of just getting really good at this stuff.

**1:02:45** · Like I mean, your podcast alone probably could would would probably add like 30% extra knowledge to every person on the planet if they were just listening to your your average episode, maybe minus this one.

**1:02:59** · Careful, I may I may I may clip this and play it on repeat.

**1:03:02** · Okay, okay. But like But like they should just be doing this. And they should just like there's And there's five other podcasts that that that that do this and But not as well.

**1:03:09** · Not nearly as well. Um cuz mostly it's just, you know, fighting with Jensen. Um so so \[laughter\] um so first of all, everybody should be consuming some percentage of this content and and and and having a fluency. You you have to use the tools. There's no There's no way around that.

**1:03:27** · You've I mean, you should just You should try and find a way to spend 100 bucks, 50 bucks a month, some some number like stop your your turn off one of your your cable subscriptions to do this and just start to use agents a lot.

**1:03:43** · Use Codex, use Co-work, use Perplexity Computer, use, you know, Cursor if you're semi-technical and and and just figure out what these things are doing, how they work, connect it up to a couple systems, try it out on a on a personal workflow, have some fluency and then and then let your mind kind of wander a little bit of like, well, what would I do if I had if I had this sort of, you know, everybody has a slightly different analogy for it. Like one of the best ones I guess that's emerging is like, what if I just did have a chief of staff?

**1:04:15** · That that I could throw any task to and it could go and do all of that stuff and come back. What would you give an unlimited chief of staff to to kind of work on and and that kind of opens up your mind a little bit of of oh, this is actually the the power. And how would you rewire that workflow in your organization? So, so I think there's a lot that that you can do. It doesn't require like insanely high agency to do this. You don't have to be a YC startup founder to do anything that that that I just said. Like every It's available to every knowledge worker. Like Like you should just you should give it a shot or use the free tools that are out there.

**1:04:47** · Please use the VC subsidies to your advantage as much as possible. And and and start playing with these tools. And and and like even I have had to rethink my way of thinking about work multiple times in the past year.

**1:05:01** · Shout out to you know, one fun shout out Perplexity Computer I find does a better job than any other computer-based agent for just being a workhorse, for going through websites and and doing search related things where you have to you have to click on the page and you have to read the page and all that. And so I I give it these tasks where I start to think like man, actually like if I did have an agent that was always running kind of like ongoing and it was doing XYZ thing, you know, these are like maybe a sales workflow.

**1:05:32** · I could probably very quickly beat like like like make a lot of extra money by doing that on an ongoing basis.

**1:05:40** · And so but like I wouldn't have known that if I didn't, you know, at 11:00 p.m. one night go in and start a project that that I actually just like pushed the limits of this thing and then the other end of it I'm like, oh, this is incredibly powerful. Now, fun asterisk, at the end of that project after doing it, my conclusion was man, I don't ever want to do that again personally. I'd rather hire somebody to go do that for me.

**1:06:00** · And so and so another example of like the job creation thing is like is like I I have multiple tasks where if I hired a person to go and use agents to do something for me, I I could easily pay for that person overnight, but I'm not going to myself go and do all the wiring up and all the prompting. And so you will actually see interestingly if you're like a executive you and you start to do this, you'll see lots of areas actually where you should hire more people because you're like, oh my god, this thing is spitting out, you know, incredible gold mine of value, but who's going to go and run with that?

**1:06:30** · What what are you going to do next with all that value that was created? That's the next set of jobs. So I think as an employee, you got to be using the tools and and pushing your kind of thinking on this.

### Are we all just going to work for OpenAI and Anthropic?

**1:06:40** · So as we get to towards the end of this conversation, curious about your thoughts on market structure for lack of better term. Obviously we are heading towards extraordinary IPOs and we've seen companies that are compounding faster than than ever. What do you think that leaves startups, including vertical startups? Where do you see the opportunities? Are we in a in a world where everybody is ultimately either an OpenAI or Anthropic employee or in a service industry supporting them or is there room for lots of people to do lots of different things?

### Where startups can still win as the labs move up

**1:07:11** · I remain pretty pretty confident and optimistic on the the need for a kind of a bridge layer from the AI capability to the end user workflow and and some might sort of say that this gets kind of better lessened out which is which is you know oh these things are wrappers on the model and and at some point there's a training run where it just like is the final training run that makes the the renders the the kind of vertical app or or function specific you know app you know not as useful.

**1:07:41** · And I think that is a little bit too much of an accelerationist view of what people are doing with the tool which is like it's not just like what the model is spitting out or the models ability to review information it is how is the thing wired up into the business workflow how did it get the context that it needed to be useful I think if you're in a in an in an industry or a line of business there's a heavy amount of of kind of integration with data sets heavy amount of of kind of bespoke workflows that company does that usually means

**1:08:10** · that there's going to be a need for change management implementation ongoing support ongoing expertise and unless the labs build out literally the equivalent of hundreds or thousands of people for every single vertical and every single line of business that means that there's actually a lot of opportunity in that in that kind of bridge area of of the work.

**1:08:31** · Now what is the exact mix and make up of of what that work looks like and what those opportunities are I think that's ongoing and and and I I I think this this is sort of one of the big kind of questions. Now there's there's this interesting thing that I'm I'm trying to think through and and workshop a little bit which is which is you know the labs are obviously going to keep moving up into the applied use cases.

**1:08:54** · And and they're going to do some well and some not well and we're seeing the announcements all the time and and and I think you know there are some announcements where like I'm now using the lab for that thing as opposed to using the vertical application because it was so good and there's some where it's like no that that was still like the the kind of poor man's version of of that and so you still need the vertical application. And there's there's a mix of all of these.

**1:09:15** · I do think it at at some point maybe things will settle settle out where where the labs will kind of have to decide do you want these things to be plug-in in intelligence for applied use cases? Do you want everything to kind of you know orbit within your application?

**1:09:30** · Um I I think we're going to have to kind of see where the tension ends up landing on on this. Um some of it is to some extent an account control issue.

**1:09:40** · If you're a lab, you don't want necessarily to have a vendor above you that can swap you out at any moment per the token cost point earlier. So it's like very strategic, it makes sense which is like I don't want if I if like I don't want you to go and be able to swap me for another model the moment that that you find one tweak that could make that more efficient. So I I need a I need control of that account.

**1:10:04** · But obviously by virtue of having control of that account now now there's sort of less to be done in that vertical, you know, layer. And so we have to kind of figure that out.

**1:10:12** · I I think there's I think we're very early in in where that lands, but I could see some world where maybe there's a kind of a of a you know kind of a a peace treaty which is like if you bring in the intelligence from this lab then then you know X happens inside this product. Um you know, very very hazy. The hyperscalers actually had to figure this out interestingly enough where they basically had to figure out like where where are they going to compete in the applied layer versus where are they going to partner and and kind of be a pull-through mechanism.

**1:10:44** · You can see like things like the AWS marketplace be a I think a very successful project on their end and they are pulling through tons of of products that they might otherwise normally compete with because the the bigger prize for them is the most amount of infrastructure. And so the labs might equally kind of think about this as, "Okay, well, actually the biggest prize is the ultimate amount of inference. And so we we do need to make sure that there's a balance of that ecosystem." So I think we're we're just in the early stages of of how these kind of things land.

**1:11:11** · And and the great thing is is like it you know, capitalism is very good at this, which is like if if some companies lean too heavily in a non-ecosystem approach, then then somebody else emerges if they and and and you kind of can balance it out that way. But I I still remain very bullish on a lot of the applied layer of AI, simply because the the level of of focused kind of approaches you need for these things uh you know, tends to be much more intense than uh than I think people people realize.

**1:11:38** · Like the the the difference between us doing a prompt with AI, seeing this incredible outcome, and we're like, "Oh my god, like obviously that thing could completely destroy this one application." To then the ongoing daily sort of mechanics of that product, the implementation of it in an in a workflow, the knowledge worker that doesn't have time for any of this stuff.

**1:12:00** · Like they don't want to know like where was the skills file stored in their file system. They're like, "No, I just I just need to like move on with my day." Like the compression of all of that into applied use cases is uh is I think where where the vertical players etc. are going to are going to have a you know, you know, that's where they're they'll have their opportunity to to compete.

**1:12:19** · Okay, so we are concluding on the capitalism fixes all ills. Uh \[laughter\] That feels like a wonderful place to leave it. Thank you so much, Aaron. This was fantastic. Really appreciate it.

**1:12:31** · Thanks, Matt. Appreciate it.

**1:12:34** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks, and see you at the next episode.
