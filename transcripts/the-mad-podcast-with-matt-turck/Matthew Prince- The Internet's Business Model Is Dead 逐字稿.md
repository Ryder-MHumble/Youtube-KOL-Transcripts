---
title: 'Cloudflare CEO: The Internet''s Business Model Is Dead'
source_url: https://www.youtube.com/watch?v=UN47z_opfmo
video_id: UN47z_opfmo
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/matthew-prince|Matthew Prince]]'
published: 2026-06-25
created: 2026-07-21
language: en
speaker_attribution: contextual
description: Cloudflare CEO and co-founder Matthew Prince joins Matt Turck for a wide-ranging and fascinating conversation about what happens when the Internet is no longer mostly used by humans, but by bots, AI a
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=UN47z_opfmo)

Cloudflare CEO and co-founder Matthew Prince joins Matt Turck for a wide-ranging and fascinating conversation about what happens when the Internet is no longer mostly used by humans, but by bots, AI agents and machines. Matthew explains why Cloudflare now sees automated traffic overtaking human traffic online, why agents could create a massive explosion in Internet traffic, and why the old web business model built around clicks, ads, and pageviews may be breaking. We also go deep on what Cloudflare actually does, how it built one of the world’s most important Internet networks, why products like Workers, AI Gateway, edge inference, Durable Objects, sandboxes, and agent security matter, and how Cloudflare is reorganizing itself for the AI era. Along the way, Matthew shares wild Cloudflare origin stories involving hacker kids, human rights groups, cricket in Pakistan, root servers, Eurovision, JPMorgan, and the strange paths that led Cloudflare from scrappy startup to critical Internet infrastructure.  
  
Matthew Prince  
LinkedIn - https://www.linkedin.com/in/mprince  
X/Twitter - https://x.com/eastdakota  
  
Cloudflare  
Website - https://www.cloudflare.com  
X/Twitter - https://x.com/Cloudflare  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id1686238724  
  
00:00 — Cold open  
00:34 — Intro  
01:27 — The moment bots passed humans online  
04:05 — "Agent," "bot," "crawler" — what they really mean  
05:28 — Why your AI agent visits 5,000 sites to do one thing  
06:27 — The internet's business model is breaking  
06:52 — What happens to "brands" when machines do the buying  
08:11 — What Cloudflare actually does, explained simply  
10:29 — Hackers, human rights groups & an accidental product-market fit  
13:37 — Building a global network (and the Telecom Pakistan cricket story)  
21:10 — One hacker, from Turkish escort sites to Eurovision to JP Morgan  
30:54 — Fundraising, VCs & an unlikely founding team  
37:06 — How Cloudflare became an AI infrastructure company  
40:24 — Cloudflare Workers and why the edge wins for inference  
44:30 — AI Gateway: auditing, guardrails & runaway costs  
47:05 — Why agents need a new kind of compute  
52:13 — A "Log4j every week": security in the agentic era  
56:03 — Inside Cloudflare: 241 billion tokens and "Cloudflare OS"  
01:05:02 — Builders, sellers — and "measurers"  
01:06:30 — The decision Matthew thinks every company will face  
01:11:09 — What to do if AI is coming for your job  
01:13:56 — Content Independence Day & the new economics of the web  
01:18:27 — Pay-per-crawl, micropayments & out-scaling Visa  
01:20:20 — A better internet: Spotify, local news & "holes in the cheese"

## Transcript

### Cold open

**0:00** · We actually had bot traffic pass human traffic online in the first half of 2026. In 5 years, you might have a thousand times as much traffic on the internet as you do today. In the next 6 to 12 months, almost every company is going to go through some exercise like this where they're going to cut a bunch of their their team. The underlying business model of the internet for the last 28 years has remained basically the same, which is it's largely advertising.

**0:28** · The problem is bots don't click on ads.

**0:31** · Over the next 5 years, the business model of the internet's going to change radically. Hi, I'm Matt Turk. Welcome to the Matt podcast. Today, I'm excited to welcome Matthew Prince, co-founder and CEO of Cloudflare, one of the internet's most important companies \[music\] that sits in front of a very large portion of global internet traffic. We start the conversation by unpacking a huge milestone. For the first time, the number of bots and AI agents has outnumbered \[music\] humans on the internet. We also cover how Cloudflare has become an AI infrastructure company and \[music\] dig into Cloudflare workers, AI gateway, and agent security.

### Intro

**1:03** · We also don't shy away \[music\] from some of the more controversial topics, including Cloudflare's recent decision to rightsize its team to adapt to the new AI era. I should add that Matthew is a wonderful storyteller, and he shares some truly wild and hilarious episodes from Cloudflare's journey from scrappy startup to the massive public company it is today. Please enjoy this fantastic conversation with Matthew.

### The moment bots passed humans online

**1:28** · I want to start with something that feels like a very crucial important moment in the history of the internet.

**1:35** · What you tweeted a couple of weeks ago and you said effectively that the number of bots and machines on the internet now outnumbers humans. So c can you unpack that and explain what that was?

**1:48** · Yeah, so I mean \[clears throat\] there have always been bots that ran around online. The way Google works is they scrape the internet and they uh then build their index based on that. Uh and historically throughout most of the history of cloud it was about 20% of traffic on the internet was bots and that held fairly consistent over a period of time until until about two years ago when we started to see a real rise in bots driven mainly by AI and and the LLMs and everything that was going on uh behind those.

**2:15** · And uh last fall uh in the fall of 2025, I was asked at what point will automated traffic pass human traffic? And we pulled the data and we sort of extrapolated out uh the trends and and we thought that it was going to be the end of 2027. Fast forward to South by Southwest this year, March of 2026, and I was asked the same question again and we looked at the data again and we're like, "Oh, wow. It's growing a lot faster than we expected. It's moved now to the first half of 2027.

**2:44** · Uh, and then, you know, I was pretty shocked when my team uh came to me just a few weeks ago and they said, "You won't believe it. Um, but we actually had bot traffic pass human traffic online uh in the first half of 2026." So I think what that shows is just how fast these different systems again almost all driven by AI are growing and they're really driving so much more traffic across the internet and what was the denominator was like a HTTP request.

**3:17** · Yeah.

**3:17** · So, so Cloudflare sits in front of, you know, a huge percentage of the internet and so we and it's and a and a super representative sample and uh and so as a result we can always look at what are the general trends um across the internet and we have a a site we call radar if you go to radar.cloudflow.com cloudflare.com that's tracking a number of different things and one of those is how much human traffic is there how much bot traffic is there and in in the last couple months it it uh the the bot traffic exceeded the human traffic and I and I I think that if you extrapolate this out you know in 5 years I think

**3:47** · you'll see a thousand times more bot traffic than human traffic and if I had to take kind of an overunder bet on that I'd take the overb that it's just going to it's it's growing at such an exponential rate uh that that you're just going to see an enormous amount of the internet that's driven by by by these by these various bots and agents and other systems.

### "Agent," "bot," "crawler" — what they really mean

**4:05** · And when we say bots, uh do we mean agents? Do we mean crawling bots? What do we mean?

**4:11** · I mean, I think that agent, bot, crawler are all synonyms. It it all means the same thing. It depends on whether you want to describe it in a sort of normatively positive way, in which case you call it an agent. If you want to describe it kind of the ickiest way, you call it a crawler or a scraper. But it's the same thing behind the scenes. It's it's a it's a machine that's accessing resources as opposed to kind of a human eyeball driving a browser accessing those those resources.

**4:37** · And um and again in this particular case um you you still have a whole bunch of the sort of scraper crawler hacker traffic. That hasn't changed that much. You still have some of the sort of bots like Google bot that are that are building search indexes. That hasn't changed that much.

**4:53** · If anything, it's gone a little bit down. Um, but the thing that's really driving this is what I think we would all call agents, which is, you know, if if I go to Chat GBT or I go to Claude or I go to, you know, any of these systems and and I'm shopping for a digital camera, you you're going to see, you know, thousands of times more site visits for that same activity, that same job to be done of of shopping for a digital camera than if I did it myself.

**5:17** · I might visit five sites uh if I'm, you know, personally trying to figure out what digital camera to to buy, whereas my agent might visit 5,000. And that's that's what's really driving this this um increased demand.

### Why your AI agent visits 5,000 sites to do one thing

**5:28** · Yeah.

**5:28** · And what what does that change from, I guess, in an infrastructure perspective, like what you just described 5,000 sites versus five in some ways. That sounds inefficient. I mean, it's efficient uh for me as a user ultimately because I guess the best answer. What does that change in terms of requirements for the infrastructure?

**5:45** · Yeah, I think I mean first of all there there if if this trend continues there's just going to be an enormous amount of additional demand on on the internet and I go back to you know during co where over the course of 2 weeks we saw internet traffic double um you know if if if our projections are right um that's going to seem quaint very soon um you know in 5 years you might have a thousand times as much traffic on the internet as you do today and that's going to mean more you know server s

**6:15** · more network infrastructure, more CPUs, more GPUs, more memory, all of the things that have to serve these bots are are going to be very important. And it's also going to mean we're going to have to figure out some new business model in order to fund that. Someone has to pay for it. And um and you know, the the business model of the internet historically has been ads and bots don't click on ads. So, it's it's going to be something different going forward.

### The internet's business model is breaking

**6:36** · And um you know I I think the most interesting question uh that in in the world today is over the next 5 years the business model of the internet's going to change radically and what it changes to um is is is totally undefined at this point.

### What happens to "brands" when machines do the buying

**6:52** · Yeah, that's a whole new vocabulary because it used to be uh clicks and views and what is it going to be now like uh actions or we've got to figure out exactly what that is and it's going to you know change a number of things like you know what is a brand in an agentic world. Um, you know, a brand historically has been, you know, a way uh as a as a shortcut to tell humans kind of this is something that has a certain set of expectations, will have a certain um set of experience associated with it.

**7:22** · If I if I see a Walmart logo on the side of a building, I know what it's going to be like when I walk in. If I see a Marriott logo, if I see a McDonald's logo, I know what that's going to be like. um you know the the thing about the thing about bots is they have infinite amount of patience in order to discover you know everything that that might be might be right. So the a what the the basic idea of what a brand is going forward is going to be very different than what it has been in what had been the very much human-driven um kind of commerce and and internet experience.

**7:53** · Um, and uh, and again, I I'm not sure I'm not sure that I I have I have ideas of what that might look like. Um, and and I think that Kleer will play some role in in helping figure that out, but but I think it's it's all going to get discovered over the next 5 years, and that's that's incredibly exciting.

### What Cloudflare actually does, explained simply

**8:11** · All right. Fascinating. I'd love to spend a little bit of time on Cloudflare 101. If I put Cloudflare in front of my website, what what happens?

**8:21** · Yeah.

**8:21** · So um you know what what Cloudflare started out as was um how can you take um a a firewall like a a security product and put it in the cloud. And the and the original idea came from you know a realization that you know software was moving the cloud, servers were moving in the cloud therefore all the security and networking infrastructure had to move to the cloud um as well. And um and so that was the basic premise that that we started with.

**8:48** · And so if you signed up for Cloudflare 15 years ago um and you put us in front of your website, what you were effectively doing is is essentially putting a bouncer uh in front of the website that could check anyone who was trying to come to it uh and then stop the bad ones. And then because we were we we needed to make sure we didn't slow things down, um we would also then um uh take a lot of the load off of your website uh and and be able to um you know for for good visitors deliver the content significantly faster.

**9:17** · So the original idea of Kleer was sort of performance and security in a very easy to adopt um package. We knew as a business that in order to succeed we eventually had to sell our services to you know major banks and governments and health all the things that we are now count as as customers. in the early days um those

**9:40** · those those things didn't they were never going to trust us because we were a dopey little startup uh and and had you know I mean we had no infrastructure we had no data to actually provide the security services and so the thing that we did was we pro we created a free sort of stripped down version of the service with the idea of making it available um uh to to everyone. what was what was interesting we we expected it was going to be a bunch of like you know SMBs and

**10:06** · startups and and and individuals that would sign up um but it turns out that you know if you think of it as sort of xy axis and you know the x-axis is is budget and the y- axis is is like security issues there's almost a a perfectly diagonal line uh that the smaller your budget is the fewer security issues you have the bigger your budget is the more security issues you have and so it turned out that the Um we even SMBs startups wouldn't sign up even though it was free.

### Hackers, human rights groups & an accidental product-market fit

**10:34** · Um but two organizations kind of defy that or two two groups defy that. Um one was was hacker kids um because they're all always attacking each other and so overnight every hacker kid in the world signed up for for Cloudflare and and and then they were attacking each other trying to take us down.

**10:51** · Um and then the other were um uh you know sort of uh human rights organizations, humanitarian organizations, nonprofits because if you're doing any of that work, turns out nine times out of 10 you're pissing somebody off and and oftent times it's you know a government or something that will then attack you. So overnight we had like every humanitarian organization in the world, every hacker kid in the world using Cloudflare. they were all, you know, and we all of a sudden came under just massive attacks. And so we were constantly trying to figure out how do we stay in front of it?

**11:22** · How do we actually um continue to to exist and thrive in this world and that that forced us to build uh you know a number of different things. So we you know we we built a registar product so you could register domains because we had used a registar and we came this close to our domain getting stolen which would have been a disaster um for us. We had to build DOS mitigation which initially we didn't think we wanted to build at all.

**11:48** · We had to build you know a DNS infrastructure because we couldn't get anyone else uh to support us. We we needed to build our own sort of VPN because everybody else was too slow or not secure enough. Uh and eventually we had to build our own developer platform where you could where our team could turn around and actually take um the ideas that they had and deploy them in a way that was that was um uh able to be

**12:12** · you know incredibly limited sandboxed and other things cuz you know at some point we got big enough that if if we had an issue it it was it was incredibly um you know uh disruptive to the world um in terms of what we were doing. And so, you know, the real story of Cloudflare has been, you know, we started with this idea that was pretty simple, which was how do you put a firewall in the cloud and then that and then we sort of created so many problems

**12:36** · over time for ourselves that we had to solve and then in the process of solving those problems um we've built a whole series of of products and so Clevveler today unlike when we started you know I I mean I have a hard time articulating exactly what it is that we do at some level. We um you know we're we're we're we're sort of the next generation um sort of AWS or or Google Cloud where we're we've rethought how that works.

**13:00** · We still provide, you know, security and performance uh across that, but we have, you know, additional products that take advantage of the network that we have in order to provide things like a cloud-based VPN and and other things.

**13:15** · And and and you know, we're increasingly because of the massive percentage of the internet that we sit in front of, we're increasingly sort of playing a role in figuring out what's that business model of of the internet of the future. And so our our mission is to help build a better internet. And I think anything that sort of is in fulfillment of that mission is is is the sort of problem that we're always thinking about.

### Building a global network (and the Telecom Pakistan cricket story)

**13:37** · Yeah.

**13:37** · The the concept of network is is fascinating and seems very central to the story and it's a network of users but it's also physical network right like what what you guys did initially was to create this edge network like how does one even go about building that as a young startup? I mean in the very beginning um you know we when we when we launched um we had um servers in five cities around the world uh the Chicago, Ashurn, Virginia, uh San Jose, California um Amsterdam and Tokyo.

**14:11** · except Tokyo sort of, if we had been totally honest, deserved an asterisk because we couldn't totally figure out the routing. And if we got it wrong, a whole bunch of traffic from the US ended up hitting hitting Tokyo. And so we would literally turn the Tokyo um servers on and off throughout the day depending on uh you know where who was who was awake uh around the world. Um today, fast forward and you know, we're in over 350 cities worldwide.

**14:34** · We're in over a thousand data centers uh worldwide and and we will go from you know the minimum deployment is sort of like a rack of servers in some places we'll have hundreds of racks of servers just depending on what's what's needed there. Um, but I think that that was the that was, you know, a huge focus um, behind the scenes was how do you figure out how to get into all of these places around around the world and it was um, I

**15:02** · mean it's it's a a series of of kind of stories of how did we create enough value to, you know, the ISPs uh, around the world, the the the internet providers for consumers that they would invite us to be into their into their buildings. And it you know was a number of of of different things. I remember um we uh telecom Pakistan it was this incredibly difficult organization to work with and we there was there's a lot of people in Pakistan so there was there was a lot of traffic that was coming from it.

**15:31** · It was all hitting our Frankfurt data center and and I kept saying we should we should put servers in Pakistan and they said and our team kept saying you don't understand. They're incredibly difficult. They've kicked Facebook out. They've kicked YouTube out. They've kicked Okami out.

**15:42** · They're never going to let us in. And then out of the blue one day um we get an email from the guy who's the head of networks at Telecom Pakistan and he says, "Hey, we is there any way that we can get Cloudflare gear into our into our into our our our network and into our system?" And I went to the email. I was like, I thought you said these guys were difficult. And so we we got the guy who ran networks on the phone and I were like, oh, you know, we we'd heard you were kind of difficult. Why why do you want us there? And he said, I'm a huge cricket fan.

**16:13** · And the Pakistani national cricket team is a Cloudflare customer.

**16:18** · They were a free customer. Um and um I'm sick of the the latency of backhauling the traffic to Frankfurt. So send us servers and we'll we'll install them in in in our network. And so the the secret to Cloudflare success has always been how do we provide you know a a a huge number of services for free to a bunch of people and then it it ends up being that there's somebody in that group which is which is really important. We do other things as well.

**16:44** · So um you know if you if if you type in you know www.amazon.com um it turns out that you know Amazon gets to choose where www points.

**16:58** · Verasign which runs.com gets to choose where Amazon.com points. Um the question is who gets to decide where.com points?

**17:07** · The answer is uh there are these 13 root servers that are out there um that that underly the internet. And and when I when I say a server, people picture a single box, but in these cases, they're often, you know, thousands of machines that are that are sitting behind this.

**17:21** · And they're run by organizations that you'd be sort of surprised by. Like USC has one, the University of Maryland has one, NASA has one. And the reason there are 13 is because that's the amount that you can stick in a in a standard packet.

**17:36** · So there will never be a 14th um root server and and the organizations that run them will probably never change as well because this has become this incredibly political topic like China wants one, Russia wants one and and and and so as a result the University of Maryland will probably continue to run it even though you know why the University of Maryland um we provide the infrastructure for two of the 13 root servers. We don't run the root servers themselves, but they they are on our network.

**18:04** · And that's incredibly important because anytime you send an email, anytime you click on a link, anytime you use an app on your phone, um the very first thing that happens is a is a request to one of these root servers.

**18:15** · And so, um we provide those services, we provide them for free. Uh and and we do it for two of the 13. We've been asked to do it for more, but we think two is sufficient. Um and and that's again one of the things that when we go to an ISP anywhere in the world, we say hey would you like one of the root servers to be running inside your network and they're like absolutely that'll improve everything. And then in the process of getting that in that then helps us um you know all of the other services that we provide um run on that same same infrastructure.

**18:44** · And so because we've done the hard work to make it so that every service at Cloudflare can run on any one of our servers, um when when we can get into these places, it means that we we we um then have a really privileged access to kind of the fundamental core of how the internet works.

**19:01** · It's amazing, right? Like we all take the internet for granted. It's so uh unbelievably interesting to to hear this, right? Like how it all works. So uh that's a physical network. Do you think of Cloudflare as a network effects uh kind of business currently around you know whether that's a data network effect or otherwise or is that is that more of a VC way of looking at the world?

**19:23** · No, I mean I think networks inherently have network effects and you know as we see um as we have gotten bigger um our rate of growth uh of of who uses us has continued to accelerate. And so I think there are multiple different network effects that that are stacking on top of each other.

**19:39** · Um but but but one of them is you know we provide a a VPN service and and a and a and one of the most popular DNS services uh in the world 1.1.1 um everyone who uses one of those things um then the they're inherently going to get uh access to everything else on Cloudflare a little bit faster.

**20:02** · Um, and so as more people use kind of one side of our network, um, it's just it it just makes the other side of our network much more valuable. And as more people use the other side of our network, it makes the other side of the network more valuable. And so I think those things are very much compounding. Um, and then going forward, you know, as we think about, you know, what is what is what is the future business model of the internet going to look like?

**20:26** · Um, I think that's going to be another place where um it it's going to make it incredibly compelling for for as many people as possible to to be to be on our network.

**20:37** · Um, but it's, you know, it's it's interesting. We it takes about 5 minutes to sign up for Clafller's basic services. It takes about, you know, 10 seconds to leave. And so I I while I think that there are things that are always driving um what it is that's the value behind Cloudflare, we have to constantly live up to providing that value. Otherwise, you know, there's there's like our customers \[snorts\] aren't locked in in any way.

**21:01** · And if we if we're not providing service, if we're not creating value, um you know, the whole thing could go away, you know, very quickly.

### One hacker, from Turkish escort sites to Eurovision to JP Morgan

**21:10** · But at least from a security standpoint, why would you? I guess you could always go to a competitor, but like you you you benefit from the collective wisdom of knowing all the DOS attacks in the world at any point in time.

**21:22** · And that's and again I think that's another one of the the um the network effects that we have is that you know we we act almost like an immune system and so an attack against any one of our customers um benefits all of the customers uh that that are out there. um that the the story that Michelle, my my co-founder, wouldn't want me to tell cuz it's a little it's a little um it's a little blue, I guess, was that early on I I remember we we used to have a bell that would go off anytime anyone signed up um for for Cloudflare.

**21:53** · And uh and the bell went off and we all would run back to our, you know, laptops to see what was who who had signed up. And um and this was back in in 2010 or or or maybe early 2011. And um and I remember just being like my I mean my eyes got wide and I and I and I and I blushed cuz it was a a Turkish um prostitution website that had signed up and and it was like, "Oh, okay.

**22:20** · I guess we need a like employee handbook or or somebody to sort of say, you know, there might be some kind of uh colorful things that sign up for Cloudflare." But but then what happened next is the bell went off again and it was another Turkish prostitution site and then another one and then another one and by the end of the first week like over a thousand Turkish prostitution sites had signed up for Cloudflare and it was really strange cuz we were like \[laughter\] and I mean we didn't have we didn't have a sales team. We hadn't market we had translated the website into Turkish.

**22:49** · There was I mean it was it was just like and it wasn't like there were a bunch of like I don't know Bulgarian you know escort sites that were signing up was for whatever reason was Turkish. And so we, you know, curiosity got the better of us. And so we contacted one of the web masters behind us. We set up a Skype call with them. And and it was interesting. He he he was first of all, we got on the phone and he was just effusively thankful for for Cloudflare.

**23:13** · And um and he said, you know, we we you might not know this about Turkey, but as you know, you go further west in Turkey, it's very European. They don't love what we do, but they kind of tolerate it. Um, but as you go further east, it becomes a very much more conservative, much more Muslim country. And they think what we're doing is just the epitome of evil.

**23:31** · And, um, and so, uh, a and so he said, "Listen, one of when someone reads Techrunch, they heard about you. We signed up. Um, we we are always getting these attacks, we assume, from kind of, um, sort of more um sort of uh, Muslim fundamentalist kind of Eastern Turkish uh, people. You protected us from this tax. By the way, there's there's not a lot of money in Turkish Escort, so we're using the free version of your service and and and and thank you very much. And so, and we have machine learning systems that will categorize attacks.

**24:00** · And so, we labeled this style of attacks the the TE, which stood for Turkish escort attacks. And so, anytime we'd see, you know, that this the system would identify, you know, the TE attacks are are coming. Fast forward a year later and I was in our office late uh on a I think Thursday or Friday afternoon and um and and \[clears throat\] the phone rings and it's a Dutch gentleman. He's calling from Baku Azerbaijan and he says the contest is tomorrow. We're completely offline.

**24:31** · Everyone has told us you're the only ones who can who can help. And I was like what contest? And I I grew up in Park City, Utah. Like I I you know hadn't traveled out out of the country until until college. and you know wasn't wasn't very familiar with um with things that happen around the rest of the world. So when he said Eurovision, I said, "What's that?"

**24:52** · Right? And he's like, "No, it's a really big deal." And I was like, "A song contest? Like it's like American Idol with nationalism, whatever. \[laughter\] Just, you know, sign up for the surface." He's like, "No, no, we need help." And I'm like, "No, just whatever.

**25:03** · Sign up. You'll be fine." Um what had happened was it the finals in Eurovvision, one of the six uh contestants was uh transgender and Baku, you know, is a again a very relatively conservative Muslim country and some people thought that this was incredibly offensive that this was happening there and so they launched pretty significant attacks against against them and um and uh and and and knocked them um you know off offline.

**25:31** · I came in the next morning and we had a bunch of French engineers and their eyes were like saucers and they're like, "Do you know who signed up last night?" And I'm like, "Oh yeah, that that that song contest." And they're like, "No, no, you don't understand what a big deal it is." And for those of you who are also ignorant Americans in the audience, Eurovision gets more like viewers than the Super Bowl. Like it's it's this it is it's American Idol with nationalism.

**25:52** · It's crazy. and and so and so we protected them and we looked at like the attacks and and the system is identifying them and it goes te exact same pattern exact same um attacker. Fast forward a year after that, I get a frantic call from um the CTO of JP Morgan and uh he's like, "We're under attack. Um you know, they they they're they're taking offline a bunch of our kind of consumerf facing um services. We've heard you guys are really good at at this.

**26:23** · You need to bring your best solutions engineers and best salespeople and be in New York first thing Monday morning." We didn't have salespeople. Um, and so and our and and our one network guy didn't own a suit. So we like over the weekend we bought him a suit and we all fly out Sunday night and we're in the JP Morgan offices first thing like 6:00 a.m. on uh

**26:45** · on Monday morning and like I remember they have this whole room, this a war room where they're they're dealing with this and they slide this stack of logs across the table and and this guy on our team, his name's Sheree, he looks at it and he goes, "Oh, we know these guys. It's the Turkish escort attackers.

**27:01** · \[laughter\] What what it turns out is it it actually wasn't anyone in Turkey. It turns out it was a originally a student in Iran um who who again saw what was happening in Turkey and thought it was it was repugnant. So, you know, launched attacks against them, then saw the Eurovvision contest, launched attacks against them. that got him recognized and he actually got brought into the um the Iranian um military apparatus, the

**27:27** · sort of forward cyber that um offensive cyber uh capabilities at which point they attacked a bunch of US banks, which is how how they came after this. And the same guy uh to this day is running all of Iranian um cyber attacks. Um, and so

**27:44** · when you see like all of the things where they were creating like the sort of Lego style movies, it's this one guy who's uh who who started out as the as as attacking, you know, Turkish escorts and and and again that's I think shows kind of the power of Cloudflare serving everyone helps us learn from even these sort of weird corners of the internet and as a result today you know almost every major financial institution in the world almost every government um you know relies on us in order to uh in order to stay stay safe online.

**28:13** · That's fascinating and and hilarious.

**28:15** · Yeah.

**28:15** · And Michelle will be mortified when she's she's like, "You need to stop." I was It was funny. I I um I I I Allen and Company, the big investment bank, um invited me to one of their conferences they do in in Arizona. And I told this story and um I haven't been invited back since. So So \[laughter\] anyway, there you go.

**28:40** · Okay.

**28:40** · Well, thanks for sharing, you know, the fact that you found your initial uh customer sort of segment in like hacker kids and uh human right organizations, you know, when you when you think about like VC slides and and and raising money. That's uh not exactly your first obvious uh you know, Silicon Valley kind of play.

**29:00** · No, no. And it was it was it's interesting. I remember a VC early on said, "Okay, you guys have gotten really popular, but how are you going to expand outside of, you know, the Bay Area?"

**29:13** · And I remember sort of saying and and the the person was just completely incredulous. I was like, "We're really big in like, you know, Tunisia, but I we don't have anyone in the Bay Area." \[laughter\] And so it it turned out that wherever the internet was slow, wherever sort of um, you know, it was more lawless, th those were the places that we initially got, you know, most of our our traffic.

**29:35** · And it actually took a really long time for us to win sort of the tech natives, the the YC crowd, um, you know, the the folks that were were that would be sort of what you would think would be our natural um, audience.

**29:49** · Um whereas you know I mean we were like in if you went to Congo you know 50% of the top hundred local websites in Congo you know were using Cloudflare because it was a because the further you were actually away from sort of the tech epicenters the the more valuable what we provided was.

**30:05** · Yeah.

**30:05** · goes to show there's not one way of doing things and no no no one playbook \[clears throat\] and and and again I think you know it's and and this this I say this to people and and sometimes kind of frustrates them but it like it wasn't like we wrote grand strategy memos on why we built a developer platform we built it because we needed it um but but that's then turned out to be incredibly valuable kind of to defining what what Cloudflare is is going forward.

**30:35** · And so at at some level the story of Cloudflare has always been, you know, create these really thorny hard technical problems, solve them for ourselves, and then in the process that that that builds um what it is that that um really drives the business going forward.

### Fundraising, VCs & an unlikely founding team

**30:54** · Yeah.

**30:54** · And speaking of uh VCs, there was uh some like fun back and forth on X uh maybe a couple weeks ago now, I guess, without necessarily relitigating the the specifics precisely because you had a little bit of a different kind of business um what was your path and what were some of the I guess lessons learned in terms of like yeah, fundraising, you know? I think first of all I mean we ended up getting to work with just some incredible um investors uh over time.

**31:24** · you know, Carl Led Better, um, Scott Sandell, um, Brad Burnham at USV, um, you know, they they they really matched kind of our style. And what what our style tended to be was we thought of venture capitalists primarily as, you know, sources of money. And you know, mostly sort of we wanted when when we needed money, we wanted to be able to to access capital with no thought leadership, but we yeah, we we we really just weren't like we didn't need help hiring.

**31:54** · We didn't we we didn't really want to buddy. We sort of wanted like we wanted people who, you know, would would would push us from time to time would would sort of say, "Hey, have you thought about what's, you know, over the horizon?" Um but but weren't, you know, in our business being like, "Well, I think you should price it at, you know, $22.99, not, you know, $21.99." Like, we didn't was we we were sort of like, we we know our business better than anyone else. And so, like, if you believe in us, um do that and get out of the way.

**32:24** · We saw we saw lots of other varieties of that, you know, people who, you know, really wanted to be kind of operators.

**32:31** · Um and and and I and again I think there's not one way of doing this. For some founders that's that's that's incredibly valuable uh to them and and they and they want that and and so you know we had um you we we talked to almost everyone that was that was out there and there were lots of people that just thought you know we were complete idiots. um guy at um like

**32:57** · a bunch of people at Eggin Capital like Santi and Gordon who who I love, but there was one guy who was just like, "You're an idiot and we're never going to invest in you." And um and again, I I get it. We kind of were. Um but but but that's okay cuz we found people who who did believe in us and and um and have and have, you know, done incredibly well coming along the journey with us. Uh and it made sense. But we were an odd, you know, company.

**33:24** · Um, you know, I think that you, if you look at the three of us that founded it, most companies get founded by by people who are friends with each other. Michelle, Lee, and I, we were not friends. It wasn't we were enemies. I think we had a ton of respect for each other, but we were just radically different people to this day.

**33:40** · Like, um, you know, Michelle, like she has a giant pink \[clears throat\] piano in her living room. and her idea of a good time is at night to sit down with her kids and she plays piano, her husband plays guitar, and the kids sing along. That sounds like the lowest circle of hell to me. Um, and and but but again, like that's but we we're we've obviously, you know, we we've become friends over time because we, you know, built this together, but we were radically different as as people.

**34:07** · And I think that some investors when they looked at us, they were like, "How does this mly crew fit together?" But what was powerful was because we were so different and the way Michelle describes it is she's like when you're starting a company you want to you want it to be like a ven diagram where you know you've got big circles and they have just enough overlap that you can like still communicate with the other people but that your lanes are incredibly clearly defined and and so you know in the

**34:39** · \[snorts\] you know 16 now almost 17 years that we've been at this like Michelle and I have never really had a fight. Um because and and because fundamentally like what I do and what she does are just in you we we each have our own lanes and we can we can we can succeed in those those lanes. Um and even though you know even though I I am I am good at some things um she is good at a completely different set of things. And then that just really drives a lot of um of of what I think has has caused us to be be successful over time.

**35:10** · And you know, we we now get u founders that are coming to us for advice all the time.

**35:15** · And one of the most common questions we get is like, "How did you guys split up responsibilities?"

**35:21** · And you know, I I it depends on how snarky a mood I'm in. But if you're asking that question, it probably means you have the wrong co-founders. Um because fundamentally, like what you want is is to cover as much surface area as possible and for each person to have a very distinct lane. And so in in our case, I you know, Lee was the technical genius that was that just was heads down writing code. You didn't want to be on the board, didn't want to meet with investors, was sort of, you know, but he he but but an absolute technical genius.

**35:53** · Um Michelle was sort of the operations person who, you know, like would take a thing that worked once and figure out how to scale it to, you know, a million uh times. uh and so you know ended up running uh a lot of like our go to market organization those things that you need to have real process and and scale and then I I'm I'm a good storyteller and so um and so like in this you know in the case of the VC thing like you know Venode Kosla we is

**36:21** · thinking of investing in us I'm doing most of the talking because I'm the good storyteller Michelle's you know thinking about I mean she was a she literally was a six sigma black belt like she's she's a process person and and she's incredibly good at I'm terri terrible at that. But like she was doing that. And Lee's like, "Why am I at this dinner?"

**36:38** · Like seriously, I could be have so many more productive things going on if I was just back writing code. And so again, I don't I don't blame people for saying like, you know, if if you're pattern matching off, you know, everyone's got to be a good storyteller.

**36:54** · That that wasn't that was that just wasn't what we were. But I but I actually think there's real strength in that because you want different people with different perspectives and different different skills. And I think that's, you know, part of why we were such a a strong founding team.

### How Cloudflare became an AI infrastructure company

**37:06** · Okay. Awesome. Let's talk about the AI stuff at Cloudflare from a product standpoint because you guys have built so much.

**37:17** · Uh, and I think the world is starting to realize, but I was I was struck. I'm like I knew some of the things you build, but as I was prepping for this, like just like such a list. So walk us through the general strategy and maybe timeline of like when you started building for AI and what you built.

**37:37** · Yeah.

**37:37** · So I I think that um the the real kind of beginning of it starts back in well I mean at some level Cloudflare has always been an AI company and I remember pitching Benchmark actually and um and I said you know Cloudflare is an AI company and like Matt Kohler rolled his eyes so like that I was like I'm never going to say that ever again. Um and that was back in like 2010 or something.

**38:02** · And um but at some level that's always been true again. the Turkish escorts like that's a machine learning system that's recognizing patterns and then and and the whole thesis was if you get enough traffic going through our system and you can run machine learning systems against it you can do interesting things. So, so like that's always been kind of in our DNA. And if you if you actually kind of look at where the real start of Cloudflare was.

**38:22** · Um it it came from Paul Graham before Y Combinator used to throw a um used to throw a conference at MIT called the MIT anti-PAM conference and um and it was it was really a machine learning conference because spam was this perfect machine learning um place and you know like like

**38:42** · John Graham who's now on our board but was our our CTO for a really long time like he was a machine learning guy and so like that was always kind of in our in our core but but we would but we would would not have really described ourselves. I think that the modern era of kind of Cloudflare and AI started really in 2017 and what had happened was

**39:02** · we were deploying software in the same way that everyone was deploying software, you know, and and um but but our network kept growing and then the the size and importance of the customers that we had uh kept growing and it it was terrifying because if you pushed when you pushed code out it um you know there was always a risk you'd make a mistake. and take things down. And we had we had done that and I remember getting a call from the CEO of FedEx at the time and we we were in the midst of an outage and he was like, "When are you going to be back online?"

**39:31** · And and I and I was like, "Any second now, we're so sorry, but but you're not even a customer." And he's like, "No, no, but we rely on a bunch of your customers and some of our planes can't land if you're off if you're offline." And they could technically land, but they had a sort of checklist of procedures. And one of these things was to check against, you know, some systems that were on us. And and that was just terrifying to us. And so we thought, we've got to build a new way of developing and deploying software which can be extremely lightweight.

**40:01** · It can um scale, you know, automatically to whatever whatever size um you need. uh it it can be you know rolled out to a single customer or a group of customers or to all of our customers in you know really fine grain controlled way. You can pull it back very quickly. Um and and it and it needs to be cost effective because we're we're you know we're still running and trying to you know build this as a as as as efficiently as as possible.

### Cloudflare Workers and why the edge wins for inference

**40:32** · And that gave rise to the Cloudflare developer platform which we call Cloudflare workers. I wish I could say that we saw, you know, what was coming in AI and \[snorts\] and we and we did in some cases back in 20 20 either late 21 or early 22, I can't remember.

**40:47** · Um we uh did a partnership with this um you know graphics processor company to put um GPUs at the edge of our network in order we said to be able to do a bunch of interesting things including inference.

**41:05** · issued a press release, did did a whole thing. It was crickets. No one cared. Um and and we're like, "Huh, that that's surprising." Um and that graphics chip company was Nvidia. And um and and and and hilariously, like 2 or 3 years later, 2024, we we and you can look this up, we actually issued the exact same press release, just changed the date

**41:33** · and our stock doubled like and so um and so I think we've always kind of been in this space thinking about it. Um, and I think because we are so close to users around the world and we are so connected to everything else, it we it makes us just a very natural place to take some of these AI tasks.

**41:53** · So, you know, inference we're really really good at and and you know, almost all of the the models you can now use Cloudflare to directly access and you get better performance, you get better responsiveness, you we can deliver at a much lower lower cost than than most most anyone else and those are open-source models that

**42:15** · but even the even the big like you know Open AI is you know big customer of ours um you know all their mobile app is built you know on on on us we have you know direct access to to them and we can get you better performance um than than you can if you often times just go directly to them.

**42:31** · Um Anthropic again another big customer um all of cloud.ai AI sits sits on top of of us and so but if I'm if I'm a developer and I'm looking to run Kimmy Mistl whatever I can do this on totally run run on us uh and and that in

**42:48** · that case those will be processed on the GPUs that are sitting you know in our network um distributed around the world in you know hundreds of of of cities and that's for in France you you the edge network doesn't lend itself to training necessarily not not today um you know I think that if you think about what you need for training, you need lots and lots and lots of machines with very powerful GPUs.

**43:11** · We have both of those things, but what we don't have is a way of like we don't have an Infiniband um you know network fabric that's connecting all of those machines. And so where you know an an AWS or or you know even an you know SpaceX they're they're building giant data centers with lots of machines very close together hyperworked.

**43:33** · Um we're we're we have just as many machines but they're spread out um all around the world and as a result um most training tasks were not the right place um to do that. We're always testing and experimenting and you know I I don't know that that will necessarily be be the case forever.

**43:51** · Um but but but what we are really good at is anything that you need kind of a beef beefy machine where like your phone or your laptop isn't enough. uh and you want it to be either fast or or lower cost or um or or you have some sort of regulatory jurisdictional reason why why you want it to run, you know, in a particular region and not necessarily get sent back to, you know, Ashurn, Virginia.

**44:19** · And uh and I think that's driven, you know, a huge amount of the adoption of of the these AI workloads um across across our network. And that's by far the fastest growing part of our business. So that's workers. Another product that seems incredibly timely given the current conversation is the gateway. Do you want to talk about that? What that does?

### AI Gateway: auditing, guardrails & runaway costs

**44:40** · Yeah.

**44:40** · So I mean again this it's all driven by by us and so we needed to be able to use AI models but we're a security company. We're you know we have you know various regulatory um requirements based on the customers that we have. And so we needed some way to be able to understand like how our team was using these these models. And so we built something that we you know call the AI gateway. And um and it it allows you to do a couple of things.

**45:07** · One is uh it allows you to audit uh as if you're the CIO or CTO audit all of the sort of um the prompts that have gone off to various AI systems and then all the responses that you get back. And we actually have an AI system that's that allows you to very quickly surface things based on, you know, what you might think of as problematic. If you've got a customer support agent and it starts acting like a Nazi, like you want to be able to see that, you know, incredibly quickly.

**45:38** · And so we give you that auditing. We also allow you to do basically, you know, prompt injection.

**45:44** · the way that if if you're you the way that Claude or the the way that Anthropic um sort of uh put guard rails around around um Fable in order to take what was mythos and and turn it into something that they they thought they could release broadly is they put a whole bunch of prompts and say do not do you know the following things. you as a business like if you're if you're cloudflare you know there are certain things that we don't want AI systems to do and the AI gateway allows you to to

**46:12** · inject that into it and then the and then the third thing which again we built for ourselves was you need to control costs um the the cost of all these tokens just you know it can can be just overwhelming and it's really easy for that to lose for you to lose control

**46:29** · of that gateway allows you to route things intelligently where you don't necessarily have I don't know somebody who wants um you know an AI agent to summarize their email like you don't need the latest frontier model in order to do that you can run it on something which is a lot simpler and so

**46:47** · for for our team often times they have no idea which model they're hitting gateway is just deciding that um for them and again we built that for ourselves and we and and people are always asking us like what are you guys doing around AI and we showed it off and and people like I need that and so now again that's turned into into a into a product.

### Why agents need a new kind of compute

**47:05** · So, continuing our tour, uh, dable objects, a SDK, uh, workflows, browser runs, send boxes, it's all just it's stuff we needed and then it turns out other developers needed it as well. And so, you know, if you think about like how did AWS develop, it was it was Amazon's way of building essentially systems where um you know, their own team could could build things very very quickly.

**47:30** · And um and that that was uh and that that that I I think the the story of Cloudflare has very much been the same thing where we needed all of these things to build what we were doing. And then that's turning out to be incredibly valuable to our to our customers and and to to anyone who's trying to do anything in AI. Um today there we are the best place to build any kind of agentic workload.

**47:54** · Um here an example of this. If you you take every knowledge worker on Earth and you imagine that they're um they're each going to have one agent that is working on their behalf. Um it turns out that the CPU utilization of that is more it's 40

**48:15** · times the current annual CPU production that's out there. uh if you're doing it in a traditional sort of AWS containersbased way, it's just it's just too expensive to do that. And and I think the idea of every knowledge worker having just one agent is insane. You you're going to have hundreds of different agents that are working on your behalf, in which case we don't we just don't have the capacity um to be able to provide that.

**48:42** · And so what we've done is said there's got to be a better way of of doing that.

**48:47** · And so um again what workers did is they said you know if if once upon a time we had you know physical servers and then we had VMs then we had containers um workers said what's the next step beyond that that's even more efficient and and we built all of workers around a concept which is which everyone's familiar with because it's the the tabs in your browser which are isolates and that that is a you know safe environment that is sandboxed from the other tabs that are running.

**49:15** · Um, but it doesn't need to have, you know, a whole new copy of of the operating system. It doesn't need to have a a whole bunch of tools. And as a result, you can stand it up much more quickly. You can tear it down much more quickly. And for agentic workloads where your agent is effectively going to be write whatever you're asking it to do, it's effectively going to be writing code for you all the time.

**49:36** · It that is turning out to be kind of the perfect environment to be able to um to to be able to build these things. and and again I I wish it was because we were so clever and and saw the future. Um but I think a lot of it is it was it was what we needed to build for ourselves and it's turning out to be just a very powerful platform for for you know anyone who's doing doing anything kind of on the modern internet.

**50:01** · That looming CPU shortage crisis by the way it seems to be an under somewhat under discussed topic. I mean these ages like you need a lot of GPUs. We all know how but like CPU utilization is is going through the roof and and that's going to be you know in a in a bunch of different in a bunch of different directions. And so we're constantly trying to think about you know how can we improve the underlying kind of efficiency of of the network.

**50:28** · So, you know, like um a while back three three or four months now um we um we we rewrote WordPress uh in in Rust in order to um in order to to to um to to deliver it and we called it Mdash because we used to play on the fact that we used um AI to do it. And people are like, you know, why'd you do that? Um and and we did it because like there's a huge community that supports WordPress.

**50:55** · WordPress should be successful going forward, but there's no way that WordPress is going to be able to scale for what's coming going forward. It's just, you know, it's a it's a PHP piece of software. Again, amazing for what it was, but it cost like, I don't know, three or$4 dollars at current traffic levels in order to run. If traffic explodes a thousand times, like people aren't going to be putting WordPress sites up because it's going to cost three or 4 thousand dollars in order to be able to to to run these things.

**51:23** · So, we've got to reinvent a bunch of these fundamental technologies that are out there. Not not not not because not not not because we're like oh we want it you know we need to donate we open source we give it you know we give it away but because we believe that our mission is to help build a better internet and what the the title wave that is coming if we

**51:46** · don't get in front of it if we don't upgrade some of these fundamental systems you know it's it's going to it's going to make you know a lot of of the internet just break because we have to have an infrastructure that can actually scale and that's going to be you know how do we how do We take the the user interfaces and the things that people know and are familiar with and have an ecosystem around them, but then port them into ways that they're just significantly more cost effective and efficient to run.

### A "Log4j every week": security in the agentic era

**52:13** · In terms of breaking, what what does an agentic internet mean in terms of security?

**52:19** · Yeah.

**52:19** · I mean, it's it's that the security is going to be um I I think for the next two years, uh we're going to see just a series of really scary um things happen happen on online. um you know the the probably the worst kind of bug that was out there for a long time was this thing called log 4j where you could send a very simple command and compromise um uh almost any any server

**52:48** · running anywhere um you know I think for for the next um uh you know 104 day 104 weeks so two years um you're going to see a log 4j like vulnerability every single week um because like and again we

**53:07** · were we were part of glasswing and and got to use um you know mythos to to look at software we we get early releases of of um you the various \[clears throat\] um uh open AI u models we've built our own security models the these models are incredible at finding vulnerabilities and they're going to find them like crazy and I think security is going to be it's going to seem really scary for the next little bit there's going to be a bunch of VCs that invest a bunch of money cuz you're going to see just, you know, an explosion in cyber security companies that are stopping this.

**53:38** · But what's interesting is I think it's going to be a little bit of a head fake. Um because I I think that 2 years from now, um what's going to happen is software is going to get just massively better as a result. Um, so internally at Cloudflare, you know, we um we we like last year we had an we had an outage that was incredibly embarrassing and and and awful and we said we have to get better.

**54:05** · And so we actually built an agent that not only reviews every code release that we we send out, but every configuration change. So if you go to the Cloudflow dashboard, you you push a button that that generates a file that then gets pushed out to the rest of uh of our network. And we now have an agent that's checking all of those all of those files every code release and it's trained on 10 years of incidents. We have big public incidents that, you know, make the news, but there's there's sort of a background noise of small incidents over time.

**54:33** · And like one of those sort of just audible gasp moments um that we had was a guy who runs our um uh infrastructure engineering team who was presenting at our all hands meeting and he said, "Okay, here's sort of our background noise of incidents and then there's a cliff and then it goes like this." He's like, "What do you think happened there?" And that was the moment that we released this agent that's checking in.

**54:57** · And I think one of the things that people don't appreciate um and don't talk about enough with AI is yeah AI is you know good at replacing a bunch of tasks that that humans do and it doesn't tire and it doesn't need breaks and it it doesn't you know have have um have to sleep but the really interesting thing is it's also uncorrelated to all the other biases that are within an organization. a team of people working together will tend to develop a set of biases. And that doesn't mean that AI doesn't have biases, but they're uncorrelated with the rest of the team.

**55:29** · And so, it's actually incredibly good at measuring things. And what I think you're going to see is that if it's going to seem like software is incredibly scary for the next two years and then it'll kind of just fade away and we're going to all be releasing software which is so much better than it ever has been before. And so like our uptime and our reliability and our performance has gone up, you know, an order of magnitude uh over the course of the last year. And it's all because we're using agents in order to more securely, you know, build build our systems.

**56:00** · And I I think everyone is is going to be doing that going forward.

### Inside Cloudflare: 241 billion tokens and "Cloudflare OS"

**56:04** · Since we are on the on that topic, let let's go into how you guys use Yeah.

**56:09** · internally. Uh you have some interesting stats that you published just um a few weeks ago in April. uh where you said the company has 93% of R&amp;D employees uh using AI coding tools, 3,683 internal users, uh whatever 241 billion tokens. How did you get there? How did you create that culture for a company that was started in 2009? And two, how do you measure success?

**56:35** · We were selling picks and shovels and sort of the AI gold rush. Um but we were actually pretty cautious users um ourselves. We would run experiments but but we were sort of not kind of all in on it. Um and and we had a bunch of people internally um that were that were skeptical. Um guy named Kenton Varta who built the workers platform is incredible um engineer. Um you know we're not supposed to talk about 10x engineers but Kent is clearly a 10x engineer. He's just he's he's just a genius.

**57:04** · Um, and he, you know, last, um, in the spring of, um, 2025, he's like, "This AI stuff is is BS. I'm going to go play with all of these tools and show you just how much of a mess they they are and why why why we shouldn't be relying on them." And and he did. He went away, super senior guy on our team.

**57:26** · Went away from a month, played with him, came back and he was like, "Oh my god, I am now a hundred times more productive than I was before, which is which if that's right, and he's a 10x engineer means that he alone was more productive than our entire team was back in like 2019, right?" And so u and and and like I kind of believe that's true. Like it's it's it was it was remarkable.

**57:49** · And so internally on the engineering side, I think it spread pretty quickly and and I think the real turning point for us was um probably November of 2025 where it felt like and it was with the release of Claude Opus and and and a bunch of things, but it felt like it it tipped where we all of a sudden on our engineering side were getting, you know, much much much more productive. I think that's the story everyone that's sort of where everyone is today. Um and everyone is seeing some version of that.

**58:17** · Um, I will say that, you know, for us, um, you know, we've there there there have like the the the people that I continue to worry about are the ones that, um, have been very hesitant to embrace these tools. And it tends to be not the super senior folks, not the super junior folks. It tends to be the people kind of in the middle of their career.

**58:38** · And it makes some sense where they um they they've been doing well in the world that existed. they've been told this is the game to play and if you play this game you're going to succeed and so they they've played the game and now someone comes along and says we're changing the rules of the game on you and um and that feels deeply deeply deeply unfair um and and yet again you kind of have to adjust to what's out there but I I really do worry that we're going to have this sort of lost generation of of sort of either you

**59:10** · know young millennials or or older Gen Z folks that just they they're they were sort of they're going to have incentives to to say we shouldn't use these tools because again it it if they do they they don't feel like they have any advantage of the people who are coming coming from behind them and so a lot of what I've been trying to do is how do you bring those groups groups along the other piece was you know I think engineering teams are very natural users of these these products and and and and coding

**59:43** · has been a place where you know you've gotten really clear value um from them.

**59:49** · But like that's just a small part of of Cloudflare. We've got you know legal, finance, um you know marketing, sales, all of these other organizations that are part of the team that that were like how can we make them significantly more productive as well? and and and so we came up with this idea that, you know, could we create sort of a a

**1:00:15** · userfriendly system that allowed, you know, someone on the finance team to be able to um you know do their job um incredibly incredibly efficiently and um and we called it Cloudflare OS and it's it's it's it's basically it's a harness where we've taken a bunch of things that have to be true and gotten them into it.

**1:00:39** · We've taken a bunch of things that are sort of just informative based on our experience and then we've taught it skills where it can do various things that the there's nothing that's that magical about what we did except that you know we had a pretty significant advantage because we had all the security tooling where we could hook

**1:00:59** · into all the different systems of record we have the ERP system we have the the you know sales uh systems we have the the workplace management systems that we have and do it in a way that was secure and where an agent working on behalf of a user could in could inherit the the specific kind of access that that user had. And I think that's where a lot of these things fall down is where people don't have like that security model in place. We did and so we were able to build it um pretty quickly.

**1:01:26** · The other thing that was was where I think people fall down is like if you ask someone to describe that what they do in their job, they'll they'll describe it, but they'll leave like half of their job out. Um, and so the question is how do you capture really what are the jobs to be done within an organization? And so the clever thing, a guy named Sam Ray on our on our team, and he um he he he was like, "Listen, we're going to set up an email address, and we're going to tell everyone that it's a magic AI agent." So for us, it was auto@cloudflow.com.

**1:02:01** · And um and we told everyone it's a magic AI agent. We've set it up. You can ask it anything. Now, in reality, behind the scenes, it was a team of about 20 people that staff this 247. And yes, they were using AI tools, but what they were really doing was gathering kind of the the the information about what are the real problems that people have in their jobs. And then they were building that in and turning it into a set of skill files and information to to to be to be done.

**1:02:30** · And so an example of this is there's a a woman named Heather who's on our um investor relations team. And and so we're a public company. So every time we have uh earnings, it's about 2 weeks of prep ahead of time to generate all the IR documents and and and everything that that needs to be done. And it's it's kind of arduous kind of drudgerous work to put this all all together. Um and Heather's like, I think I can automate it all. And so we went from what used to be a two-week process down to what is now a threeinut process.

**1:03:00** · It is more accurate. we actually found errors in in um in things that we had put out before. Nothing nothing significant but you know little little things here and there. Um and now we're able to take that and that means that then our team can spend more time meeting with investors, talking with you know our shareholders, doing all the things that are actually the really productive parts of their job and much less time actually generating those documents. And so I I think that that every company is going to be going through this. And it's it's interesting.

**1:03:34** · We um again we we get questions like, "Hey, how are you guys doing this?" And we keep showing off this Cloudflare OS thing. Um I I was I was on the um I'm on the organizing uh part of the the group that's organizing the 2034 Olympics in in Utah. And I was talking to the academy who's the CTO of the IOC and he's like, "Hey, listen.

**1:03:56** · we need this, we need a system to do this. And and I was like, well, let me show you what we're doing at Cleler. And and so I showed it to him again. We never thought this was going to be a product. Um and he's like, I need you in Lucan, you know, next week to and to and bring your team because we need to implement this. And so we all flew up and now they're actually using this to um you know, to to help like better organize the Olympic Games.

**1:04:19** · And and I think that that if you get and every organization is going to have to build something like this uh and if you do it in a way which is secure that gives users access again I think it's going to it's going to just massively empower teams in order to to be successful. I I'm not sort of in the sort of the I guess the Daario camp of you know AI is going to replace all jobs. I think it is going to replace a certain set of jobs.

**1:04:46** · Like I think we're g like if I have a developer and I can now give them AI tools and they're 10 times as productive. I'm gonna hire as many developers as I can. If I, you know, have a salesperson and I can give them tools that eliminate the parts of their job that they don't like, which is coming up with account plans and and doing all of those things, what they want is to be in front of customers and and out there selling. I'm not as many salespeople as I as I can. Where I think there's going to be a big change is the parts of the organization that that aren't building and they aren't selling.

### Builders, sellers — and "measurers"

**1:05:16** · They're basically measuring and it turns out that AI systems are much better measurers than than than any humans again in part because they're uncorrelated and uh and I and so I think a lot of those things are are going to be the case. Another example internally, you know, internal audit, which is again one of these things that you do when you're a public company. You probably don't do it when you're a small startup, but you do you do it eventually. We have 105 or something risk areas.

**1:05:39** · And every quarter historically the the internal audit team has picked you know six to 10 of them and then they do sort of these deep dive um audits to make sure that we're you know not screwing up procurement or we're doing revenue recognition correctly or you know and they're they're measuring effectively the the organization.

**1:06:00** · We're now getting to a place with these tools where we can take all 105 of those risk areas and continuously audit them and find any any issues um that are there. And I think that that's like that's making us a better organization. It's freeing up people to be able to work on either building or selling which are really where value is created within organizations. And uh and it's and it it's just incredible to see to see how much more productive the teams are.

### The decision Matthew thinks every company will face

**1:06:30** · And do you think that there is a painful transition period from the current world to the next world? So do you think everybody's going to have to go through this as organizations recalibrate?

**1:06:42** · We laid off more than 20% of our of our team. Uh and not because the business was struggling, but and not because they weren't great team members. Um but we just need fewer middle managers. We need fewer measurers. Um and um a and those roles were going away. And as I talked to peers at other companies, they're all seeing the same thing and they're all saying, "Yeah, we're going to have to do the same thing at some point." And you're and you're seeing these sort of trickle out.

**1:07:11** · But there's a real fear in leaders out there that they don't want to be the first ones um to to to do that. And um you know, pardon the vernacular, but I think that's chicken because the crulest thing that you can do is wait. Um I do think in the next 6 to 12 months almost every company is going to go through some exercise like this where they're going to cut a bunch of their their team.

**1:07:39** · Uh and and I think a lot of people are wait a lot of a lot of CEOs are waiting around to do it cuz they're afraid that they're going to look bad in the process.

**1:07:51** · What really struck me was the realization that once you know that that change is going to happen, the kindest thing that you can do for your your team is to do it as soon as possible because it's way easier to get a job today than it's going to be in 6 to 12 months cuz the the market's going to get flooded. And so we put together an incredibly I mean the the most generous severance package in in in tech that that we've seen. and we let stock continue to invest, which nobody does, but we we did.

**1:08:20** · Um, and we're working incredibly hard to place these people because they're incredible people. And somebody who is a middle manager at Cloudflare can be a senior manager at a startup and do an extraordinary job. But but once you're as an organization, you've realized you're going to do it.

**1:08:39** · Like the the kindest thing that you can do for your team is to do it as soon as possible because what the worst thing that can happen is that there's just a blood bath 6 to 12 months from now where everyone does it at the same time and the and the market gets flooded with a bunch of people who are all of a sudden looking looking for jobs. And so \[snorts\] that that was the cat that was sort of the the rationale that went through us. And again, I there there are people who are really close friends of mine uh who who we let go because the roles that they had just didn't make sense uh anymore.

**1:09:07** · And um and and and we we wanted to do it in a significant enough way that we would never have to do it again. And so we're I feel comfortable saying that for the foreseeable future, we're not going to have to do anything like that again because we've reorganized the organization. And and I think that you know one of the metrics that that we look at is um is span of control.

**1:09:27** · And so how many direct reports what's the average number of direct reports in an in an organization and you the the historic number that like the Harvard Business School did a study and they they came up that the the right number for that is about six. So for every manager they have six direct reports and that was exactly what we we were at.

**1:09:51** · It's so clear that with these new tools, a manager can manage a lot more people. Um, you know, Meta is trying to get to 50 to one. I think that's a that seems like too many to me. But but I think 12 to one is right. And and the benefit of expanding the number of the average number of direct reports is it inherently flattens the organization.

**1:10:12** · The the fewer number of direct reports on average a manager has inherently the organization is going to be much more hierarchical. the more direct reports they have, it's going to be flatter. And I think one of the things that, you know, we're seeing is that the flatter the organization is, the more the easier it is for us to to move quickly, to be able to deliver things. And and um and again, I think that's that's what's that's what's driven a lot of us. But yeah, I think this is coming across the industry. Um and and and again, it's not a statement that any person is is is is a is a bad person or a bad individual.

**1:10:48** · Um, in fact, they they they're they're great, but there are roles that you're just not going to need uh anymore. And and and some people you're going to be able to sort of rehome and reskill inside your organization. But like if you if you're going to go from, you know, 6:1 to 12:1, that that means a whole bunch of middle managers are going to are going to go away.

### What to do if AI is coming for your job

**1:11:09** · So, what do you do if you're one of those people? If you're a middle manager and I think earlier you mentioned old Gen Z or young millennial and you find yourself in that situation like midcareer, do you just go down a complete rabbit hole of like just making yourself as AI pill as possible?

**1:11:26** · I think I I think yes. Um and and and recognize that it's natural for that to feel scary and that the and that your instinct is going to be to fight against it. Um, but that the more that you can embrace these tools, um, the better. I I've I've never seen, you know, and again, running this now for for 17 years, like I've never seen more senior managers on our team say raise their hand and say, "Hey, I want to go back to being an individual contributor."

**1:11:55** · And so we're rethinking like even how compensation works and and everything else because I think that the the the power of an individual contributor and the amount of of of work that they can do is is extraordinary. And so I think that for us, you know, our most senior members of our team are embracing this because it's a way for them to reinvent themselves and they're senior enough that they're not scared about it. Our most junior folks, so we we we hired 1,111.

**1:12:24** · number is meaningful to us but interns this summer you and and I mean it's like they are the most extraordinary humans because everybody stopped hiring interns which I think is just total mistake um and so we got sort of the pick of the litter and um and and they're and they're all totally AI native and what we're trying to do is get both of those groups to get the the folks that have been more hesitant because the fact is 92% of organization engineering organizations using AI tools like that.

**1:12:56** · That should be 100%. For sure. And and but you've got to get people who especially are sort of mid-career to be brave enough to learn these new these new tricks. And and I think that that's that's that's really important and and that and again you can't have one person who is 10 or 100 times as productive in the same role as somebody else making the same amount of money a as somebody else who's who's sort of doing it the old way. Like one of those two is going to leave.

**1:13:27** · And the worst case is if the person who's 100 times as productive leaves. And so we're just we are continuously trying to get every you know lift everyone up and and again part of why we did the layoff was in order to be able to um you know really really free up the resources and and catalyze the entire organization uh to be able to do this but and it's not just your developers has to be finance legal marketing everything has got to be embracing these new tools.

**1:13:55** · So almost a year ago now you declared I think that was content independence day July 1st.

### Content Independence Day & the new economics of the web

**1:14:03** · July 1st coming up on the second second anniversary or first I guess first anniversary.

**1:14:07** · Yes. What happened in the last year? How is that whole uh debate evolving?

**1:14:11** · Yeah. So um and what was it in the first place?

**1:14:14** · Yeah.

**1:14:14** · So so so again I think that it is you've just seen an enormous rise in the amount of sort of automated traffic that's running across the internet. Um I I I think in 5 years it'll that you'll that bots and agents will outnumber humans online a thousand to one. Um at the same time like the interface through which we access the internet is changing. Um and we we've gone through other sort of platform changes before.

**1:14:42** · Um you know we we went from browsing the internet on on a browser on your on your desktop or laptop to social to mobile.

**1:14:52** · But throughout all of those things, the underlying business model of the internet for the last 28 years has remained basically the same, which is it's largely advertising and then to a lesser extent subscription driven. The problem is that first um there's just going to be a lot more cost to run on the internet because you're going to have a thousand times as much traffic, which means you're going to have to have servers and and CPUs and network and all that stuff.

**1:15:22** · and and someone needs to, you know, pay for it. Um, and the business model of the last 28 years, which largely advertising based, doesn't work because bots don't click on ads. And so something has to change. Um, and so a part of that is how do we make the internet more efficient? Like how do we take legacy software and port it to things that are, you know, can continue to scale in a cost-effective way. But another big part of that is how do we figure out what the future business model of the internet is is is going to look like.

**1:15:53** · And you know, we we have great relations with all the different AI labs and and companies and and they get it. Um, and they actually, you know, they they they say, "Listen, as long as it's fair, as long as everybody has to do the same thing, we we get that we've got to pay for the content that we're using in order to build our systems and our and our and our models, but we've got to build a system to to do that."

**1:16:19** · And so, like, we're experimenting in a bunch of of different ways. The first thing that we did was we said, in order for a market to exist, you know, you always think you have to have supply and demand. It's not exactly right. What you actually need to have is scarcity of supply and demand. Um if everything is free then then no one pays for it. Like we're sitting in this room, we're breathing the air doesn't cost us anything. Um on the other hand, if we go scuba diving, air is scarce and so we have to pay for it. And so you know that that's that.

**1:16:48** · So step one was we said we we need to create controls that allow the people who have content online to be able to say who can access it and who who can't. And and again, it's everyone's going to make different decisions. Um, in our case, we want all the bots to be consuming our our information. We want that to be out there, and that's probably half of our customers are in that camp where they actually want to make it as easy as possible. And so, we provide the tools to as cost-effectively, as efficiently as possible, get information in.

**1:17:16** · Take take HTML, which has all this croft around it, convert it into markdown, which is a much more streamlined system.

**1:17:26** · And then as a result like you can get more information in these AI systems without blowing up their contact windows and all kinds of things. It makes sense in that case. On the other hand, if you're an ad supported business like agents aren't good for you cuz they're taking your content and then people are consuming it through their AI system and you're not getting eyeballs. So you're the ad systems don't work. So we said like let's give everyone the tools to be able to stop it. Let's create some scarcity in the supply that's out there.

**1:17:56** · And what we've seen is if you go across the biggest publishers in the world, condandy NAS-maredith, you know, they they are they because we've now given them these tools, they're actually signing much better deals with the AI companies. And so that's I think that's sort of the first step. But we've got to go beyond that because if you're a small blog or, you know, influencer, a content creator, like you don't have the ability to go strike the same deal that a condandy NAS does. There should be some basically a micro payment. every time we access a site and get information, we're happy to pay a fraction of a penny in order to to do that.

### Pay-per-crawl, micropayments & out-scaling Visa

**1:18:27** · Um, that's harder than it sounds. Um, so we process uh in any given second about half a billion um requests through our network.

**1:18:40** · We estimate that somewhere between 1 and 10% of those would be um sort of monetizable through some micro um payment transaction. And uh and so that means that you have to be able to support day one, call it 10 million financial transactions per second with a clear ramp to be able to get to 100 million uh transactions per second.

**1:19:01** · Visa, which is the largest payments network in the world, does fewer than 100,000 transactions per second. So we need to be, you know, two orders of magnitude um bigger than Visa, but but at much much smaller um uh volumes. And so we're working on that. And and we think that, you know, in partnership with with folks like Coinbase and Stripe, you know, and and and protocols like um X42, which is, you know, it is interesting where the original internet um had something a a response code the

**1:19:33** · 402, we all know 404, which is not found, and 500, which is an error. I mean, there different things, but 402 was payment required, and we just never have really built anything around that.

**1:19:43** · I think that's going to happen going forward. And so, you know, Google really is responsible for having built the business model that's powered the last 28 years of the internet. And I think we are trying to figure out, you know, what is that business model that's going to power the next 28 years of the internet. But something has to pay content creators cuz they deserve to eat.

**1:20:05** · Something has to pay for the infrastructure that all of these bots are are are are taxing effectively. and um and and and I and and I think we're working um a lot around figuring out exactly what that looks like.

### A better internet: Spotify, local news & "holes in the cheese"

**1:20:20** · Great. It's been an absolutely fascinating conversation. the the overarching thought um as I was listening to you is um to which extent Cloudflare is becoming even more relevant today than it's been for the last 17 years which you built the network uh and now the internet is changing and uh you are absolutely at the sort of central point for it. Yeah.

**1:20:44** · Is that how you how you guys think about it like you're you're you have another 17 years? People are like, "Why, you know, why do you keep doing this?" Um, because there are days that aren't fun.

**1:20:54** · I mean, laying off a bunch of people. I mean, that wasn't that was that wasn't fun. Um, and it's and you know, I've made plenty of money. Um, so it's it's not about any of that. Um, what it is about is is really our mission. And we and we believe in that mission fundamentally. we we do things that that cost us money or or that certainly don't make us any money um because we believe in helping build a better internet.

**1:21:21** · And um like I I I can't imagine anything that I could possibly be doing that is more rewarding than than figuring out how do we create some sort of sustainable um business for the future. And I think there's there's a lot that's to to be incredibly optimistic about. The the business model of the internet for the last 28 years wasn't the most healthy. Um traffic has always been a terrible proxy for value.

**1:21:48** · And um and and and and and like so much of like the media landscape was how do you sort of define your narrow audience and then with a headline piss them off enough that they'll click on a link in order to you know drive eyeballs to to your to your site. And you know so much of this so much of what is dividing the world today is actually the underlying business model of the internet which has been trafficbased. How do you drive as much traffic as possible? That's going away.

**1:22:20** · And I think that, you know, if we think about what can replace it going forward, it can be something which is which is which is much healthier and much much better. I was I uh I flipped to Stockholm um to to meet with Daniel A who started um Spotify and um and because I mean like nobody has compensated creators at scale like Spotify. It's just it's just it's remarkable.

**1:22:46** · And we can quibble about are the right people getting the money or not, but but there's more money going into music creation today on on per capita, per GDP, than any time in human history by far. And and Spotify gets a lot of credit for that. And and you you forget that like 22 years ago the music industry was dying. You know, Kazan and Napster and everything. Every was just normalizing. Everyone was stealing stealing content. Um and then, you know, Steve Jobs steps on stage, announces iTunes 99 cents a song.

**1:23:12** · That's not the business model that won, but it at least planted a flag that said that there's there's something that's there.

**1:23:18** · And then I mean Spotify last year sent something like 12 billion dollars out to music creators. That's more than the that's more than the entire music industry's market cap was 22 years ago, which is which is extraordinary. And and so Daniel was telling the story. He said, "One of the things that they that they do is if you search on Spotify for like Taylor Swift, Shake It Off, like they know they return results and they know that those results are what you were actually looking for.

**1:23:43** · On the other hand, if you search for like I want a song to a disco beat about how much fun it is to dance with my cat, they also return results, but they know that that that they probably don't have that. And what they do is they actually publish those queries that are sort of bad results back to music creators. And there are hundreds of music creators that are making a living off just doing this. One in particular is based in Denmark.

**1:24:09** · Um Daniel shared is making something like €40 million a year just writing songs for unfulfilled Spotify queries. And I think there's something that's actually quite beautiful about that because if you search for like a something on Spotify, what you're searching for is how do I kind of bring an emotion out and and so going forward like we for the first time in human history have essentially a mathematical model of all of human knowledge. That's what the LLM are, right? It's not perfect, but it gives you that. It also shows you where the gaps are, where there are the holes.

**1:24:39** · I I picture like a giant block of Swiss cheese. There's lots of cheese, but there's a lot of holes in the cheese. And when you talk to the AI companies, what they want is highly reputable sources that are filling in the holes in the cheese.

**1:24:53** · They're they're contributing net new knowledge. They don't want yet another story about what happened at 1500 Pennsylvania Avenue, right? They want something where people are actually telling and creating new information that moves the world forward. And I think that's what I want. I think that's what you want. I think that's what all of us are craving is how do we get back to sort of a media environment which isn't just trying to provoke outrage in order to drive traffic but is actually trying to find the truth and fill that in.

**1:25:21** · And if we can create a system where the people who again are highly reputable and are creating sort of net new knowledge that those are the people that get rewarded then I think that's incredibly incredibly beautiful. What I what I keep pushing the AI labs to do is I'm like we should create the equivalent of I don't know if it's the Academy Awards and Nobel Prize where we measure across a whole bunch of different segments who has contributed the most to human knowledge in the last year in you know I don't know cancer research and you know foreign policy news I mean you

**1:25:54** · can create a bunch of these things and they can actually measure and say you know this particular year the best podcast was you know the first Mark podcast that was that was out there or whatever it is. And we should be rewarding and celebrating both both in terms of honoring these people, but then also paying them for doing that. And I think if we do that, you're going to get a lot more, you know, interesting information. My my wife and I bought the local newspaper in our in our hometown, Park City, Utah. I think we will make more this year off AI licensing deals than we do off display ads. Why?

**1:26:24** · Because if you're planning a vacation to go skiing in Park City, Utah, you want to know what's the best hotel to stay at, what's the best restaurant, who's going to be performing, you know, what are the snow conditions like? And and the only place that has that is the local newspaper.

**1:26:40** · And so while the last 28 years of the internet kind of killed local, quirky, unique, interesting information, what I'm hopeful is that as we figure out what the business model is for the next 28 years, it actually brings a lot of those things back and and it actually gets back to let's talk about facts, let's talk about reality.

**1:27:00** · And like I like the New York Times be amazing if they were covering like in the Marriott Marquee Hotel in in Times Square, room 1313 is better than room 1314. Or if you know if you're if you want to sleep in late, room you know 1314 faces north and so it's less likely to get sun in the morning. Like those are the sorts of here's the best bodega in New York.

**1:27:25** · The very interesting quirky local stories. I think that that is both a media future and an internet future that we all crave and want and I think it's one that we we actually have an opportunity to build because we get to reinvent what the business model is going to be.

**1:27:40** · Fascinating. Well, Matthew, thank you so much. This was an absolutely wonderful conversation. Really appreciate it.

**1:27:45** · Thank you for having me. \[music\] Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already, or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks, and see you at the next episode.
