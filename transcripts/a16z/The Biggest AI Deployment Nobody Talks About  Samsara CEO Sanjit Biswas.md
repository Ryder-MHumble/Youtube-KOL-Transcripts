---
title: "The Biggest AI Deployment Nobody Talks About | Samsara CEO Sanjit Biswas"
source: "https://www.youtube.com/watch?v=3FHsGiONOGw"
author:
  - "[[The MAD Podcast with Matt Turck]]"
published: 2026-07-30
created: 2026-08-10
description: "Sanjit Biswas runs what may be the largest AI deployment in the physical world — and almost nobody in AI talks about it. Samsara (NYSE: IOT), the ~$20B company he co-founded after selling Meraki to Ci"
analysis_report: "[[The MAD Podcast with Matt Turck- The Biggest AI Deployment Nobody Talks About Samsara CEO Sanjit Biswas 分析]]"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=3FHsGiONOGw)

Sanjit Biswas runs what may be the largest AI deployment in the physical world — and almost nobody in AI talks about it. Samsara (NYSE: IOT), the ~$20B company he co-founded after selling Meraki to Cisco for $1.2B, puts AI on millions of trucks, cranes, and industrial assets: 25 trillion data points a year, 99% of US roads driven every single day, ~$2B in ARR growing 30% profitably. In this episode we go through the entire physical AI stack — asset tags you can run over with a truck, a paper-thin disposable tracking label, engine fault codes, and dash cams running inference at the edge — then into agents, including the Agent Studio warranty agent that compresses an hour of human work into under a minute. We also get into the uncomfortable part (when AI watches you drive all day, is that coaching or surveillance — and why drivers actually want the cameras), mixed fleets of humans and robots, why autonomous trucking will take far longer than robotaxis, and a startling stat from the field: one utility building 3x more grid capacity in the next five years than it did in the previous 125, with 90% of that demand coming from data centers.  
  
00:00 The biggest AI deployment nobody talks about  
01:16 What is physical AI?  
03:04 From IoT dashboards to agentic action  
04:36 Why physical AI is harder than software AI  
06:07 Safety, cybersecurity, and real-world consequences  
07:11 What Samsara does  
08:22 $2B ARR, 25 trillion data points, and 380,000 crashes  
09:44 How AI can prevent road accidents  
11:28 From an MIT research project to Meraki  
13:42 Learning physical operations from scratch  
15:42 Samsara’s stack: sensors, intelligence, and action  
16:39 Inside Samsara’s industrial asset trackers  
18:36 Bluetooth, battery life, and connected infrastructure  
19:49 A disposable tracking device built like a sticker  
21:08 Vehicle gateways and engine diagnostics  
22:16 How AI dash cams coach drivers in real time  
23:28 Turning the dash cam into an AI interface  
24:49 Organizing physical-world data in the cloud  
26:32 Selling AI to traditional industries  
27:52 Is Samsara’s real-world data its AI moat?  
29:22 The network effects of covering 99% of U.S. roads  
31:23 Edge AI versus cloud AI  
32:35 The models running inside Samsara’s devices  
33:52 Generative AI and video reasoning  
35:57 Which AI models does Samsara use?  
36:50 Inside Samsara Agent Studio  
37:56 How an AI warranty agent works  
38:50 Starting with practical, lower-risk automation  
40:10 Combining agents, workflows, rules, and guardrails  
42:07 What today’s AI agents still cannot do  
43:07 AI ride-alongs and the future of driver coaching  
45:17 Is workplace AI becoming Big Brother?  
46:27 How cameras can protect and exonerate drivers  
48:48 When AI becomes the judge of your work  
50:37 Robots, humanoids, and mixed human-machine fleets  
53:19 Samsara’s role in autonomous operations  
54:50 How quickly will autonomous trucking arrive?  
56:32 AI data centers and America’s infrastructure boom  
58:16 Should lawyers become plumbers? Demand for tradespeople  
59:54 Closing thoughts  
  
Sanjit Biswas  
LinkedIn - https://www.linkedin.com/in/sanjitbiswas/  
X/Twitter - https://x.com/SanjitB17270430  
  
Samsara  
Website - https://www.samsara.com/  
X/Twitter - https://x.com/Samsara  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark Capital  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id168623872

## Transcript

### The biggest AI deployment nobody talks about

**0:00** · These are not the tokens you're going to find online. Like you can't crawl Reddit and find out about what happened on a construction site. The Samsara system in a given day were driving 99% of the US roads usually multiple times a day. I was just in the field last week with a large energy utility. And uh they shared with me a really interesting stat. They said over the last 125 years we built a certain amount of grid capacity. In the next 5 years, we're going to triple that. We're talking about millions and millions of vehicles. We believe we helped prevent about 380,000 car crashes, road accidents in the last year.

**0:31** · Hi, I'm Matt Turk. Welcome to the Matt podcast. My guest today is Sanjit Biswas, co-founder and CEO of Sanssara, the 20 billion company running what might be the largest AI deployment in the physical world. Millions of vehicles, 25 trillion data points a year, driving 99% of US roads every single day. We talked about physical AI, agents for truckers and frontline workers, humanoids, autonomous trucks, and why the AI boom is really an infrastructure construction project.

**0:58** · Oh, and if you're enjoying this episode or if you've liked others in the past, please do us a favor and hit that subscribe button. It takes a second. New episodes will show up right in your feed and it really helps the podcast. Now, here's Sanjit.

### What is physical AI?

**1:16** · All right, Sanjit. On this podcast, we've talked a lot about AI models and software agents, but we have spoken a little less about physical AI. So, this feels like the episode where we're going to talk about how uh AI is confronting the physical reality of transportation and construction and plants and utilities. So, maybe let's start with physical AI. That's a term that uh we hear about more and more often these days, typically in the context of like humanoids and robot taxes. from your perspective, what is physical AI?

**1:48** · Yeah, absolutely. Well, first Matt, thanks for having me on your show. Um, I would say physical AI is really the application of AI to the physical world.

**1:55** · So, if you think about the infrastructure of our planet, it's way more than just the roads where you might see a Whimo robo taxi. Uh, it's the construction sites, it's the electrical grid, it's really kind of like all the plumbing that's under the street. It's it's it's everything out there. The interesting challenge, I think, with physical AI is that it's not digitized.

**2:13** · Uh, right? like this is the frontier where you don't have decades of bits that you can reason over and tokenize and and quickly ingest and that makes it really fascinating because the amount of value is is kind of that's trapped is really significant. Um so we think about it in a few different ways. We think about um you know digitizing things like location from GPS tracking. Of course we think about using cameras as sensors. So you can use that to understand the physical world in a pretty rich way especially when you ingest lots and lots of basically video footage.

**2:41** · Uh if you think about how many frames you get from that it's really significant. And then there's a lot of other uh kind of data sources uh whether it's like weather sources of like what happened with precipitation on all the roads. um you can think about speed limit data like there's lots and lots of physical aspects of the world that uh when you put them together when you fuse them together uh there's a huge value unlock and um maybe walk us through how AI

### From IoT dashboards to agentic action

**3:09** · changes that whole discussion so uh you know there was industrial automation obviously that's been going on for decades and perhaps centuries then there was a whole wave of IoT and famously your ticker as a public company is IoT and Navas AI I um how how different is the current moment?

**3:28** · Yeah.

**3:28** · Well, it's interesting you mentioned centuries because that is like the right time scale to think about physical infrastructure, right? All the way back to like the Roman era, like there's pretty significant infrastructure out there. So many of these processes of like how do you maintain a roadway have been in place for a very very long time. A lot of that process was manual, right? Like let's go inspect the condition of the road. let's understand when it was last worked on, you know, let let's kind of dig it up and see what we find. If you think about the ability to digitize that and then use sensor data, it's a huge unlock.

**3:56** · So the question becomes how do you get the data? Then how do you process it? And then how do you come up with a meaningful insight or really an action like what should we do about it? Uh and that's that's I think now possible. The last call it two decades was around reporting like how do we ingest the data and give you a really cool like table so you can look at it and reason about it, figure it out. Now what's awesome really in the last two three years is the AIS are able to reason about this kind of information.

**4:23** · They can look for other context clues and then give you the insight and now we're actually seeing a Gentic AI of course which is it can take an action for you can maybe schedule the work to be done or or start performing some of the work itself.

### Why physical AI is harder than software AI

**4:36** · Why hasn't um Silicon Valley been all over that problem space? I mean it feels like we've been talking about chatbots and then agent more in the kind of digital and software realm. Uh I mean obviously there's Tesla there's there's you know humanoids being being built. Um but is that is that did all of that need to happen before this could be applied to the physical world or is or is the physical world just like a different set of challenges altogether?

**5:02** · You know, I think it makes complete sense where all of this AI wave has started, which is in the digital word world. We had all the bits. We had, you know, you know, pabytes of data to reason over and there's a great training set. So, you think about all the trillions of tokens that were needed to get these models bootstrapped. The physical world is much messier and there's also a hardware component to it. And there's kind of this saying of like hardware is hard, right? Like this stuff has to like hold up in the environment. It's got to relay the data over like unreliable networks.

**5:32** · uh it has to be deployed to the front lines and that requires a lot of sort of messy work, right? Um physical hardware installations, getting millions of frontline workers to adopt new technologies like integrate it into their day-to-day work and it's basically not as much lowhanging fruit as what we've seen kind of in the digital world.

**5:50** · All that being said, it's a massive part of the global economy, right? All these industries, they make up about 40 50% of world GDP. And so it's an area where you can have tremendous impact, but you have to really roll up your sleeves and get much more involved than uh kind of connecting to a large database that may have already existed.

### Safety, cybersecurity, and real-world consequences

**6:07** · Is it fair to say that it's also a much more unforgiving environment where mistakes are potentially much much more consequential?

**6:17** · Absolutely.

**6:17** · So of course you're dealing with human life in a lot of physical operations and that's an area for tremendous impact. So if you can build safety systems that keep workers safe, that's a great thing. But you also have to be careful that you don't somehow introduce risk into the into the picture. Um there are other sides of that too which is like these are digital technologies so we want to make sure they're hardened from a cyber perspective like they're not introducing cyber security risk but really practically um the physical world is a pretty dangerous place. Think about a construction job site, right?

**6:45** · There's a lot of like earthmoving equipment multi-tonon, right? Like really dangerous stuff. It's kind of low visibility. Um and so you know the operators that are are operating that equipment are taking some risk. The people on the site are taking a lot of risk. So it's inherently a risky environment and our question has been can we find ways to make it less risky using data. So we see that the risk as the opportunity as opposed to the challenge.

### What Samsara does

**7:12** · All right. So you alluded to to some of this but um for contextual awareness early in this conversation uh maybe give us a 60cond on on on what sensor does.

**7:22** · Yeah.

**7:22** · So Samsara is a technology company serving the world of physical operations. So think about those construction companies, the energy utilities, the supply chain and logistics companies that power the planet. Uh we help digitize their operation. So that's a combination of hardware. So think uh GPS trackers, dash cameras, asset trackers, all kinds of different devices. Uh cloud services to ingest all the data and then now AI and applications to really close the loop, right? to help people take some kind of action or ideally automate the action that's needed.

**7:54** · Um what we found is it's helpful to start with just tangible real world problems and then expand over time. So where we started was around fleets of vehicles almost all of these industries that have you know tens of thousands of vehicles that they need to perform their work but uh over time we've expanded now into those frontline operations and we're able to fuse all this data together from different sources on our platform third party sources and and unlock tremendous amounts of value for the customer.

### 2B ARR, 25 trillion data points, and 380,000 crashes

**8:22** · Okay. And uh you just crossed two billion in AR is that is that correct?

**8:27** · That's right. with uh you're a profitable company growing at 30%. Is that that's correct the right metrics?

**8:34** · Okay. Just a beautiful beautiful company. Any other metrics you can share about the the kind of the volume of uh data points you're seeing or just to give people a sense for the scale of the of the company?

**8:46** · Yeah.

**8:46** · Um so on the data points side of things, these are numbers that feel abstract even to me and I live them every day. But we're talking about 25 trillion data points. GPS, video, thirdparty API integrations, all kinds of data flowing into the system.

**9:00** · Millions and millions of vehicles, for example. Uh we're talking about, you know, millions of frontline workers that are using our apps every day. Um and in terms of impact, that's the other sort of set of data points we look at, which is like, well, how is all this technology having impact in the world?

**9:14** · Uh we believe we helped prevent about 380,000 car crashes, uh you know, road accidents in the last year. That's meaningful to us because as engineers and product builders, we are able to have like significant impact in the world this way. Uh we've helped uh avoid the emission of billions of pounds of CO2 by helping do things like optimize routes and reducing you know engine idling things that seem simple but uh you technologically simple perhaps but the execution matters a lot. What's cool is you see that real world impact.

**9:42** · Yeah, that that's a crazy number. 380,000 and that's because uh you're able to detect uh whether uh a driver can get sleepy or that kind of stuff.

### How AI can prevent road accidents

**9:55** · You got it. Yeah. So there's so many different factors that produce risk. And you know, we're very excited about autonomy and robo taxis and everything that we're seeing sort of on the frontiers, but there are a lot of these industries like um in heavy duty trucking or construction, people work very long shift. Um you know, maybe they've been out in the field for 10 12 hours, it's been hot and so they're exhausted. So you know, fatigue is definitely one of them. U you also tend to see more accidents in general at night, right?

**10:21** · Because the roads are less visible. you see accidents in foggy conditions after it snows or rains, things like that. So, we're able to help prevent a lot of risk by warning the driver of when we see, you know, kind of the risk increasing. We can provide some real-time feedback and that helps them be much more alert, much more aware. And we can also coach away some of the bad habits that people develop. Um, this is an interesting stat, but in the US, approximately 10% of people don't regularly wear their seatelt.

**10:48** · And that, uh, varies by state, it varies by industry, but that's like one of the biggest things you can do to improve your risk outcome is just simply put on the seat belt. And it makes sense because sometimes people are doing a quick trip or that, you know, they're distracted. But that little reminder helps save lives, right? So that's one simple one. Putting down your mobile phone is the other one, right?

**11:07** · When you take a look at your mobile phone, like lots of people have this habit. um your your car if you're driving can move the length of a football field and that is hard to think because you're like I'm just taking a quick look to see what that message was about but then you look up and you've moved 100 yards, right?

**11:24** · That's the kind of risk avoidance that we can create with real-time alerting.

### From an MIT research project to Meraki

**11:28** · Okay, great. I'd love to spend a few minutes on on your entrepreneurial story uh leading to the creation of the company which I believe was Stanford to MIT to Merke uh Moroi.

**11:40** · Yeah. This is like walk us through like how it all came about. You started the first company as a student or right after your PhD.

**11:47** · That that's correct. Um actually during our PhD. So my co-founder John and I we met at MIT as PhD students uh over 20 years ago. I I now cap it because we're just old. Uh but it was it was a fun sort of research project that we worked on which was um this was around the time that Wi-Fi was emerging as a new technology. We built a uh research project called roofnet. We covered essentially the city of Cambridge, the area between MIT and Harvard with free Wi-Fi in the early 2000s. So that was really exciting. It's like a hands-on kind of very practical research project.

**12:17** · We did a bunch of academic research on routing protocols and you know how to build the network. Um but the first company Moroi came out of that project which was we thought it was tremendously cool this idea that Wi-Fi could connect so many people just incredibly useful.

**12:31** · We wanted to help other people build big networks. And so we essentially took that research um and and now I would use the word distill like we condensed it down to uh you know run in a box that other people could build networks out of and then we started essentially making that product available. So that was Moroi. Um to be honest we kind of thought of it as a project like we weren't even thinking of it as a company. Uh we kind of bootstrapped the business in Boston. We ended up moving to California. Um and it was fascinating because this is 2006 like 20 years ago.

**13:03** · Wi-Fi was a brand new kind of naent technology and there were some real challenges, right? How do you do guest access? How do you do networks at scale?

**13:12** · How do you deal with people starting to use YouTube which was brand new back then? Like hard to imagine, right? Um but that kind of exposed us to how fun it was to solve real problems. And um we had a huge, you know, kind of deep background in networking. We had a lot of friends from grad school that we recruited to start that company. And so we got off the ground quickly. we started seeing these devices get out in the world and Moroi ended up kind of just growing and growing and growing. It was doubling in revenue every year. Um so that was the beginning of our entrepreneurial journey. It was a little bit of an accidental start.

### Learning physical operations from scratch

**13:42** · And when you started Samsara, you know, as opposed to to what you did in Moro, that was a brand new area where u as far as could tell from what I read like you guys didn't have a prior background in that. So like how does one become an expert as an entrepreneur in a domain that they don't have a background in?

**14:00** · Yeah, you're you're very right. We had never spent time like in a loading dock or warehouse or like in a construction yard. Um but we were always fascinated by them and I think that was really the key is uh this is just like nerdy curiosity of like well how does electrical grid really work? Right? I have an electrical engineering background.

**14:15** · I was just always kind of like fascinated by this. um or like supply chain if you're just curious about like well that Amazon package like how how far did it travel like you know where where were the goods stored like all of those kinds of questions were fascinating to us and um similar to Maro

**14:32** · we weren't intending to start this company right out of Cisco like we had been kind of on this pretty intense run uh but the curiosity kind of got the better of us and we started reading lots of books about this and you know like just trying to learn about the world um the challenge with physical operation though is you can't learn about it in a book like you actually need to go on site and to do that you need a reason

**14:54** · you need an excuse essentially and so we said well maybe we can be helpful to these industries right because um like I was saying earlier it's the infrastructure of our plan so massive there have to be interesting problems to solve there so we kind of started this company market first very steep learning curve and I have to say as a second time through entrepreneur I'm really glad we had that experience because had we gone back and it we probably would have overweighted our prior experience and said, "Hey, this is how it's done or this is how we did it at Moroi." Uh, with Samsara, it's a different customer.

**15:27** · We serve the world of operations much more than the kind of technical buyer. Um, we sell direct, so we interact directly with our customers versus via channel. And that reset was enough for us to kind of go back to beginner's mind, which I think is also very important for most companies.

### Samsara’s stack: sensors, intelligence, and action

**15:43** · Okay.

**15:43** · All right. Thank you for all of this. uh let's deep dive uh into the product itself. So uh based on what we've said so far um you have a hardware layer which is the sensors. So uh just to use an analogy and and and stop me if that doesn't seem right but that would be the the sensors so the ears and the eyes.

**16:07** · Then you have a software layer I guess now with AI which would be the the brain. Mhm.

**16:14** · And you just added recently and we're going to talk a bunch about that you added an energetic layer which would be uh the the arms for the action. Is that is that directionally uh how you think about it?

**16:27** · Yeah.

**16:27** · And I would say um you know every single one of those layers has some connective tissue attached to it. So if you think about the hardware, I've got hardware on my desk of course and so this would be an example of one of our sensors.

### Inside Samsara’s industrial asset trackers

**16:39** · So what is this? What is this?

**16:40** · Uh this is what we call an asset tag.

**16:42** · So, you could put this on a piece of construction equipment, right? Um, it's got an accelerometer in there, so it can tell, you know, how much it's been moving. It's got a Bluetooth radio that's a little bit more powerful than what you've probably used on the consumer side. So, you know, your AirPods have Bluetooth. This is a industrial-grade Bluetooth. Um, it's got a battery inside and then it's built to be super tough. So, you can like beat this thing up. You can drive over it with the truck and u, you know, it'll it'll continue to operate that layer. It has hardware, but also has firmware that's running it on it on it. It's got network connectivity.

**17:13** · I mentioned Bluetooth. So, this connects to the millions of Samsara gateways, tens of millions of phones and handsets that can act as kind of a relay point for us. And then we we're able to get that to the cloud in a secure way. So, that's the data capture side, right? Going from motion like the accelerometer into the Bluetooth layer into the cloud.

**17:31** · Um, but from there, you need to organize it because like you got signals coming from all over. uh you need to be able to like operate on it in a pretty methodical way and that's what's going to feed the AI because if you give the AI pretty noisy data you'll get you know it's like less signal noise ratio so we need to get get clean data in um and then to use your analogy that's the brain right like that's where we we store it we operate on it um you can surface those insights

**17:59** · to the end user or the agentic piece is you can just take an action right um maybe change a safety setting right like say hey we're gonna ask our entire fleet in uh New York because it's raining to increase the following distance versus on a bright sunny day, right? Um that kind of change would have normally required a human in the loop. We're now finding that the AI can do it very consistently and uh can do it at scale that people wouldn't be able to get to because you'd need someone just sitting there monitoring all the settings for thousands of vehicles.

**18:29** · Not very practical. So, it just doesn't get done. And that's the maybe the arms the kind of action side of things.

### Bluetooth, battery life, and connected infrastructure

**18:36** · Okay, great. All right. So that's the overall architecture. Um, so going back to that hardware layer. So you showed us an asset tracker. Uh, you said it connects via Bluetooth. That's Bluetooth. Uh, it's been a while since I looked at at at all the things, but like it's not like Laura one and that that kind of uh frameworks and Yes, this is it's Bluetooth low energy.

**19:01** · uh if you're familiar with the BLE that you you know would see on your uh fitness device or your AirPods, that kind of thing. So, uh Bluetooth has come a long way over the years, it's it's kind of gotten added on to and it's it's picked up a lot of the great characteristics that many of these other standards had. So, we can get a lot of range out of these trackers. And then we add a layer on top of that of security.

**19:22** · How do we make sure that uh we preserve the privacy and the security of the the the tag that it's being applied to?

**19:28** · And it's powered by battery. You said like how much autonomy would a tracker have? Like how long does it last?

**19:34** · Uh this specific one would last about uh 3 years. We have others that last 6 plus years. Uh we even have a really small form factor one. I've got these on my desk as well. And I don't know if you can see them, but this is like a tracking label. So we're talking about a sticker.

### A disposable tracking device built like a sticker

**19:49** · That's the one you just launched in Vegas a few weeks ago. Okay.

**19:52** · Exactly.

**19:52** · So these last about uh 45 days or so. Um so long enough for shipments to kind of go one way. And then these are disposable. So, um, they don't have lithium-ion batteries in them, for example. So, you can just, uh, peel them, stick them, track them, and then dispose of them.

**20:07** · But, show them again on camera if if you will.

**20:10** · Yeah. This is a So, this So, this is literally a sticker. So, what's what's in it?

**20:16** · What's in it? Um, it's hard to make out on camera, but there's basically some batteries and then, of course, the Bluetooth chip, right, as running our firmware. Um and that is how it it beakens up essentially its signal of where it is.

**20:29** · How are you able to get such a flat and small um like form factor? Is that is that where the innovation is like just miniaturization or like what what's the I I would say for us it's systems innovation. We did not build the battery. We don't make the silicon or the chip but we work with partners to integrate all this together. And then we have the network which is essentially think about um you know the millions of vehicles on the road all the people running the Samsara stack they form a community and relay signals for each other.

**20:58** · Um and you've actually probably seen this in the consumer side with the Apple Air Tag kind of that concept of an ecosystem. We apply basically the industrial strength version of that.

### Vehicle gateways and engine diagnostics

**21:08** · Okay. Very cool stuff. So what else do you have at the hardware layer? Uh I read some more vehicle gateways.

**21:14** · What what what does this what do those do?

**21:16** · Yeah.

**21:16** · Unfortunately, I don't have all the hardware that we make on my desk, but the vehicle gateway, think of it as a black box that goes on a truck or a piece of construction equipment or basically any kind of moving asset. Um, that is a a different type of collector, right? So, it collects diagnostic information from the engine computers and that's everything from uh you know, how much fuel is it consuming to does it have fault codes to uh was the driver's foot on the accelerator or the brake.

**21:43** · That's all there on the diagnostic port. So we're able to ingest that information.

**21:47** · It's like a long time series of some sort.

**21:49** · Yes.

**21:49** · Uh well it's we have to collect it and organize it but it forms a long time series of many many different signals.

**21:55** · And even something that sounds as simple as a fault code really there's a lot of depth and richness to that too because if you read the fault codes very carefully you can understand very specific dynamics about different kinds of engines and fuel types and you know air pressures and so on. So we we take all of that in. Um we have uh and then you have uh AI dash cams.

### How AI dash cams coach drivers in real time

**22:19** · What are those?

**22:20** · That's right. So I think you're familiar with dash cams. You've seen them in Ubers, right? Like um and super valuable, useful for drivers because if something happens on the road, you can exonerate yourself very quickly. Um so we have a connected version of that. So it records HD video, it has some storage, it's got the ability to send that to the cloud. Um and we run AI models at the edge. So we can do things like um provide you feedback to increase your following distance like I said based on the weather condition. Um now we're also seeing the driver side of that camera. So it's like you know outward and inward facing.

**22:50** · The driver side of the camera can do things like detect fatigue or mobile phone usage provide real-time feedback to the driver. And the idea is they can self-correct uh self coach and that is like the aha is it breaks the the cycle or the bad feedback loop of I'm going to look at my phone. If you get a sort of like audio alert in the moment and it happens many many times you tend to break the habit because it's sort of negative reinforcement.

**23:15** · Um that was a huge breakthrough for us um six seven years ago uh as we introduced AI at the edge and now we're kind of going further with that concept finding other forms of risk and so on right because it used to be a safety device and now it's an interface uh that the driver can can communicate with the AI.

### Turning the dash cam into an AI interface

**23:36** · Exactly.

**23:36** · Because now that you've got the technology in the cab, what else could you do with it? Could you give the driver uh driver a briefing in the morning as they start their shift about where all they're going to go and traffic conditions and weather? Um, we have a little button. They can use that to uh, you know, call dispatch, for example, and say, "Hey, I'm going to be late because I need to uh go pick up some tools or something like that." So, the that connectivity layer just got enhanced with the presence of all this technology and all of this. And I know you have other sensors for like temperature and that kind of stuff. uh all of this is is built by you.

**24:07** · So you mentioned not all the components but like all of this is is propos the system and it's designed as an open system by the way because a lot of these newer assets they have uh APIs effectively right so a lot of newer trucks for example we can do a cloud-tocloud connection so you don't necessarily need the black box but you want the data and you want it like organized and and seamless with all of your other assets uh because typically in operations you'll have Ford trucks and GM trucks and Caterpillar and Freightlininer and all kinds of other equipment coming together.

**24:38** · Um, so we act as that orchestration layer. Uh, so the hardware is very much part of the story, but we also have software in interfaces coming into the system.

### Organizing physical-world data in the cloud

**24:49** · All right. So you got all of this and then uh you move it to the cloud and then uh what do you have there? Like you have a gigantic data warehouse and like ETL kind of data transformation. Uh is that how it works?

**25:05** · Um that's right. From an ingestion perspective, I think you got it. Um, so just massive amounts of data storage.

**25:11** · Uh, this is all kind of sitting in modern hyperscaler cloud. So it's not that we have like one big warehouse/data center, but um, you know, pretty large system. Um, so we ingest the data, we're storing it and organizing it, and then we like basically have a bunch of processes that are that are um automating like sort of automatically working on top of that data as well. And then you have the UIUX collaboration interface where you're a customer whether you're a dispatcher or a truck driver or uh the business owner like everybody has access.

**25:43** · That's right. And and there many different personas. So you named a few of the the key ones. Um the drivers in the front line are are very much like just regular users of the system. Um you do have the dispatchers. You'll have other people who'd be like safety managers or uh in certain cases if they have to do paperwork like uh essentially compliance managers and but you also have people that do maintenance for example and so they want to know what is the health of all these assets in the field which truck will I need to maintain at the end of the day when it comes back to the yard.

**26:10** · Um and then you do have the executives and all these other business uh minded people who want to know well did we show up on time right like what is the efficiency of our fleet and how do we do this at scale many of our customers actually most of our customers are large enterprises so think operations have thousands tens of

**26:28** · thousands of people and tens of thousands of assets and so on as a thought uh so selling to a bunch of different personas especially in like more traditional industries uh especially as you've added this AI layer recently how do you go about it like how do you convince people in you know typically non technology industry to to buy?

### Selling AI to traditional industries

**26:48** · Well, you know, I think the the great part about this technology is very tangible and um it's the kind of thing that when you see it, you get it very quickly. So, what we do is we tend to go on site, we will demo the technology and do trials. So, you can easily these are plug-and-play so you can easily try it out in your environment, in your industry. And um like I said, there's so many challenges in physical operations.

**27:09** · It tends to never just be one thing. So yes, we want to reduce the number of accidents we get into, but I think we're also like leaving our trucks idling a lot because it's just a bad habit or we're leaving tools behind at the job site and we'd like to get those back cuz we spend millions of dollars replacing them. So we will often find multiple challenges like that. Then we demonstrate to them at small scale like maybe a team or you know a region or or something like that that this works and when they see it they get it immediately. These are people who are experts in their industry. So they would say, "I immediately see the value or the ROI."

**27:40** · Uh, but they have to see it in that kind of tangible way. They're not just buying it because it's AI or big data or something like that. They're like, "No, if this solves problems for us in our construction business, great.

**27:51** · Let's do it."

### Is Samsara’s real-world data its AI moat?

**27:52** · And when you think about the long-term defensibility of the the business, uh, especially in a world where models may or may not commoditize, I think most people would say they are commoditizing.

**28:04** · Mhm.

**28:04** · Is it the data layer that you that you feel protects sensara or how do you think about modes?

**28:12** · Yeah, there are a few things. Um, we see whether it commoditizes or not, these models are incredible, right? And uh the amount of value they can unlock with their ability to ingest the data and reason is is awesome. Um, so we're very excited about what we're seeing on that front. Um, the operational data that I was talking about, the physical world kind of digitization side of thing is where we come in, right? These are not the tokens you're going to find online.

**28:35** · Like you can't crawl Reddit and find out about what happened on a construction site, right? Nor can you do, you know, test time reasoning about it. You can't just you you can simulate all kinds of environments, but really what our customers need to know is like what was going on in that specific environment at that time, right? Um that requires this interplay of hardware and software, but also the change management. How do you get this out into the field and that partnership? So that's a unique area for us that we focus on. Um this is what we've been doing for the last decade plus and it takes a lot of work.

**29:05** · I have to I have to emphasize that too is like we get out in the field with our customers, understand their business and work backwards. So it's not something that can purely be like just you know uh one click uh deployed. It really requires a kind of a nuanced approach.

### The network effects of covering 99% of U.S. roads

**29:22** · Do you have a concept of a data network effect or data flywheel across customers? So does something that you learn in the context of a dash cam with uh customer X in geography Y also apply to customer Z in a different geography like in terms of learnings. uh very much. So, you know, on the dash cam side of things, the key insight there is, um, while these may be all different companies, we're all driving on the same roads, right?

**29:49** · Um, the Samsara system, uh, in a given day, we're driving 99% of the US roads, usually multiple times a day. So, you can use that of course on the risk side. So, we can understand where are the risky intersections or where weather conditions bad and and how do we warn other drivers. So, there's a network effect there. Um, but there are other sort of uh side effects, right? Um because we drive all the roads and we have cameras, we can tell you where all the potholes are, right? And that is super useful for the city.

**30:16** · So like this, you know, city of Chicago for example, they want to know which potholes are, you know, happen after the winter weather season. What order should we go after the men in terms of severity? You can use the camera data for that, the accelerometer data from the GPS tracker that I mentioned. So every time you see that big bump in the road, um you look at the video. And the cool part about that is not only do you know where the pothole is, but we can see what's happening to it over time. Is it getting bigger? Is it, you know, cracking? All that kind of stuff. So that is another sort of data network effect that we get.

**30:50** · And then maybe the third, since we talked about asset trackers early, you have these millions of vehicles driving around. A Bluetooth tracker on its own probably doesn't get picked up, right?

**31:00** · Because think about a construction site. It could be acres and acres of land. But if you have, you know, one company delivering building materials, another company performing construction, the electrical contractor, one of those guys may pick it up and that is another network effect that you get with millions of these vehicles and then tens of millions of handsets like the mobile devices. Uh it's a incredible kind of mesh network that forms.

### Edge AI versus cloud AI

**31:23** · All right. So going back to the the product and and the eye stuff. So you mentioned uh edge and cloud. Where do you guys do what in what proportion? We could spend an hour just talking about where where what is going on. Um if I had to generalize, I would say at the edge we're typically running inference and data collection. So the data collection of course gets us the training data. The inference is essentially running models where we have the weights and we send them down from the cloud and they're running at many frames per second at the edge.

**31:50** · And this is how we do the the kind of real-time or the low latency detections and closed loop alerting to the driver. Um the reason we do it at the edge is is practical, right? So sometimes you don't have a great sell signal. Uh many of our customers are operating in the middle of nowhere. Um and then also the latency matters. If you can get uh feedback to the driver, you know, really very soon after something happened, it's much more likely they'll they'll change that behavior. So uh again very kind of practical architecture for us.

**32:21** · It's worked really well um in terms of how robust it is and how it holds up. Um but that being said, it's not fixed. So if that means we need to do some inference in the cloud, we are set up to do that. We have real-time tunnels that that connect these devices.

### The models running inside Samsara’s devices

**32:35** · Presumably what you run at the edge would be smaller models. Are those um your your traditional quote unquote uh convolutional neural networks that are trained for images like a very specific tasks versus um you know other forms of like more modern generative AI. There are lots of different model types. So, uh, convolutional neural networks are very much where we started.

**33:02** · That's basically from the imageet era of like, okay, can we detect a mobile phone, right? Um, from there these models have become more sophisticated. So, we run basically a model backbone with many different classifiers and and heads or attention heads. So, um, basically once we see a device in somebody's hand, what is it? Is it a phone? Is it a vape pen?

**33:23** · Is it a sandwich? um you know what is the activity that's going on with it.

**33:27** · That's not a single shot detection. It it tends to be a little more nuanced than that. Same thing when we look outward. Uh we have cameras that point out at the road. We have some cameras that point at the sides or or to the back and we're trying to do things like uh estimate depth, right? So, am I likely to run into a lamp post or a mailbox or something like that? That's a different kind of model than like a what a CNN would be able to do. And then what has um uh generative AI fundamentally changed for for you guys? Um is that video reasoning?

### Generative AI and video reasoning

**34:00** · What what what do you use for for what?

**34:04** · We use generative in a few different ways. I would say if we think about the overall class of models, yes, you can now reason about video. So uh what would have required a human in the loop reviewer um or you know and that's the kind of work that might have been done overseas in lowerc cost geos or something like that you can now do at much more volume um in the cloud using these models. So uh for example if someone slams on the brakes right while they're driving their truck um the the naive thing to assume is like hey the driver was distracted and they they kind of woke up.

**34:35** · The more nuanced thing is that driver might have been avoiding a deer or a dog or, you know, some kind of uh defensive event. If you can watch that as a video clip, you can now say, "Hey, we're actually going to give the driver some positive feedback because they did a really good thing." The VLMs are able to effectively do what I just said, right? Um, similarly, like if you want to understand, did someone run a a red light, right? These things happen.

**35:01** · you need to have a pretty sophisticated model that understands the geometry of the road and all the conditions and and so on. So that would be like a a JEPA style model for example. So we're able to use a few different model families.

**35:13** · On the generative side of like actually being able to create video that's also very interesting because from a coaching perspective most of our customers are bottlenecked on the number of humanto human interactions they can have. Like for me to sit down with you Matt and say hey we need to talk about your driving from last week. We could probably do that for a small fraction, but I can't do that for every driver. It's not practical. Um, you may have seen like, you know, AI generated avatars like AI generated people.

**35:38** · We can generate a coach and that can resemble the VP of safety from the company or, you know, a celebrity or who knows, you know, whatever the customer wants, but that can be a very effective way to deliver end of week coaching. So, that's a form of generative video that frankly we couldn't have even dreamed of five years ago. Do you build some of your own models or do you take stuff off the shelf and customize it? Are you an open source shop? Are you in OpenAI anthropic shop, Gemini shop? Um what what do you use?

### Which AI models does Samsara use?

**36:10** · We are universally accepting of models in the sense of there's so much innovation happening. Um so yes, the frontier labs are doing great work, right? The and we'll use multiple models from different labs uh simultaneously.

**36:22** · Um the open source models are are pretty compelling. I think it's having its moment now. But we've been seeing u and this is really I think from the academic communities open source and really open weights models really give you a lot of operational freedom. So we can do things like distill them uh for example to shrink them down to fit on a device. Um so we use models like that and then there's others that we train from scratch. Those might be smaller models call it tens of millions of parameters but very specific to something we need to do in the field.

### Inside Samsara Agent Studio

**36:50** · All right let's talk about agents. So that's the that was the big launch that you guys had at the um your Beyond 2026 conference in Las Vegas just at the end of June. So less than a month ago now.

**37:05** · Uh and you launched agent studio. So maybe walk us through this and I think in the past you describe a progression from uh connecting operations to understanding them to taking action. So how does that all fit together?

**37:18** · Yeah.

**37:18** · Well, a few years ago, we did introduce LLMs into our product. We called it the Samsar Assistant. So, think of it as like a chatbot tied to your operational data. Um, it became very popular. We saw customers asking all kinds of, you know, practical questions like who are my safest drivers or which trucks need maintenance, things like that. Um, those tended to be, you know, single turn or maybe like a few turn interactions like you just go back and forth with the the chatbot window on the side. The breakthrough that of course happened last year is these agents can operate over much longer time horizons.

**37:48** · So instead of an AI responding to a question in a second, it can like go do some work on its own, develop a plan and go after it. We've seen the impact of that in the coding world, but there's also a lot of implication for the operational world, right? So um the one of the demos I did on stage is we have a warranty agent. when it sees a fault code, it can basically crack the service manual, look at your uh specific

### How an AI warranty agent works

**38:12** · like OEM negotiated warranty agreements and then correlate the two and say, "Yes, this specific issue given the age or you know the number of miles that have been driven on this vehicle is actually covered under warranty." Then it can open a work order, put in the steps and also tell you, hey, do any of the other trucks have that issue? That is a, you know, like what would have been like an hour or two of human labor that we've been able to automate down to like under a minute. That is the huge kind of breakthrough unlock. And I I just went very deep on warranties.

**38:40** · But you can see how that would apply to reporting, how it would apply to, you know, briefing a driver at the beginning of the day. You can use in all kinds of creative ways.

### Starting with practical, lower-risk automation

**38:50** · It sounds like u for all perhaps the obvious reasons you're starting with um non-risky kind of use cases. Is that is that how you guys think about it? Like something where if you make the wrong warranty claim, you know, it's not great, but uh yeah, you know, nobody dies.

**39:08** · Yeah.

**39:08** · Um I I think of it as we're just starting with the most practical areas we can have impact. The the reality, by the way, is most of those warranty claims just are unfulfilled, right?

**39:17** · Nobody has the time to go do all that work that I just mentioned and and do the paperwork. So that's an area of of tremendous interest for our customers is you know hey I have all this extra work that I know would be useful but I'm not able to get to so how do I do that? Um

**39:32** · and then you know over time I think the idea will be how do we really like autonomously run parts of the operation for the customer if that's like replanning the route for example before uh every morning shift we now have the technology to do that and again it's not super risky but it requires a lot of business judgment of you know that route actually is run by this person because they have a relationship they've been you know seeing that customer for 10 years you

**40:00** · need to have all that context So in that sense we are starting with things where we know we can have an impact and then we're working with customers to figure out what else could we do.

### Combining agents, workflows, rules, and guardrails

**40:10** · You use the word um autonomously. I'm I'm I'm always uh fascinated for people that that build real agents that work in the real world just like you guys do. What would you say is the proportion of um sort of a gentic reasoning versus having some good old you know code enough code workflow and rules that's built into it for for ultimate success like you know ultimately who cares you

**40:37** · know what what does what as long as it works but like what is the recipe to make it work is that is a combination or are we at a stage where just agent reasoning can do so much so that you don't need that much like rules built into the overall solution I I think agent reasoning was a huge unlock like I said this ability to build plans and work over long time horizons but you do need to outline what is it that I want the agent to do right and that is in in some lightweight sense

**41:03** · like the workflow it's also the guardrails like at at what point do you say hey agent you should you know ask me for some help or agent I don't want you to go down that rabbit hole right like we we have to kind of keep it on track so it's some combination of operational context which comes through workflow and guardrail with also this now kind of new agentic reasoning ability. I don't think either really works well in sort of isolation and the workflow side of things. By the way, we had elements of that in our product.

**41:32** · Um I'll give you a very simple example in u in most commercial industries there's a walkound inspection that you do at the beginning of your shift and end of your shift. We see about 300 350 million of those a year.

**41:47** · that has historically just been a workflow on a mobile device, right? Like you're kind of going step by step, taking some pictures, saying something's safe. If you combine that with the diagnostic information, the location information, who last did the check, like you know, what was in the picture, that is is a huge unlock. So that's kind of what we mean by combining these two things.

### What today’s AI agents still cannot do

**42:07** · What do you think agents are not able to do just yet?

**42:11** · Oh boy, that that ceiling question, it changes like, you know, I feel like every week. Um, and you there's there's some nuance to this. So, for example, these new models like the kind of Fable 5 class and and GPD soul, it's hard to figure out where the practical ceiling is, but sometimes you do see them go and get um distracted or like lost in a loop somewhere, right? So, I think there is some aspect of like they may find the answer eventually, but can they find the answer in um 10 seconds or 1 minute or even 1 hour, right?

**42:44** · So that's one area where I think there is still a practical ceiling and my guess is as these models become more and more powerful more sophisticated that will shrink and then these algorithms are getting more efficient. So maybe the compute combined with the algorithm combined with just like smarter model architectures will make what would have been like a one-day task a 1-hour task or you know even faster than that. And if you suspend disbelief a little bit, what do you think you would be able to do uh in like a year or two? You know, not 10 because obviously who knows.

### AI ride-alongs and the future of driver coaching

**43:15** · Um but uh given the progress, so right now you're able to do um uh you give the example of warranty, you give the example of uh sort of pre-planning a day uh for for a driver. What what else do you think you can do in the next year?

**43:31** · I I think a lot of our ability to predict what happens next year or two is by looking at what is like barely possible now and then what will the sort of um cost curves look like or or capability curves look like and um something that we talked about at our beyond conference last month was this idea of a of a driver ride along. So, in operations, it's quite common to basically have a manager sit with you over the course of your day, like drive around with you for 8 hours.

**44:00** · And what they're doing is they're not looking for, you know, uh, how fast you're going. They're looking for your habits of like, do you check your mirrors, like, you know, are you alert and are you aware? That kind of thing. That's basically a massive amount of, uh, video computation, right? So, you can run a tokenizer. It just turns into like a lot of compute. You can do that today. It's it's pretty expensive and costly, but it it works and it's doable.

**44:23** · We're pretty optimistic that the you know cost per million tokens is dropping so fast and the capabilities are rising that we can deliver that at better and better cost over time to our customer. So I think in a year or two that will be possible and I have to say like you know just over last weekend I was playing um Sarah which is one of those big like wafer scale chip companies. they have uh an inference model that you can run on their chip which is basically Gemma 4 but like hyper accelerated like that's a great example of like that is nonlinear in

**44:55** · terms of jump right like what you get out of these big models today if you run Gemma 4 on your GP you might get like 100 tokens per second if you have a fast card if you run it in their cloud you get anywhere from 800 to 1500 tokens per second so call it 10x faster um that is the kind of thing where it unlocks these new use cases that we couldn't get to because it would have been too either expensive or too slow.

### Is workplace AI becoming Big Brother?

**45:18** · Not to promote the podcast on the podcast, but by the time we release this uh the prior episode will be precisely an episode with Andrew Feldman of Serial Brush if anybody missed it and of and of commercial. I'm I'm glad you mentioned the the the ride along because I think there's a fascinating aspect to uh the whole dash cam almost from a societal standpoint. uh in in that uh uh

**45:46** · it could be like an interesting blueprint in terms of like how we professionally interact with AI uh not just when we query it through AI chatbots but like having AI live with us on a on a on a on a permanent basis. So, you know, sort of the obvious question is that this there's an element of like arguably big brother is watching you.

**46:05** · You know, AI is watching every single move that you make. Um, and you know, for your own good, but it's also looking at what you may not do well. I'm curious about what you've learned from the perspective of uh uh making everyone happy, if there's such a thing, whether that's the the customer, the driver, and you know, people for people not ripping out the the camera in rage.

### How cameras can protect and exonerate drivers

**46:28** · Yeah.

**46:28** · So, uh, you know, a couple of thoughts there. The first is we actually do spend a lot of time on the front line with drivers and other, you know, frontline workers. So, it's very important for us to get their perspective because they're the primary users and and really beneficiaries of the system. Something people don't often think of is, you know, if you have a dash camera, what is it used for? The majority use case is actually exoneration. So, what I mean by that is helping explain what happened if there was an accident. Because for example, if you are the Home Depot, you're a very well-known brand. They're a customer of ours.

**46:58** · Um, lots of claims, auto claims are placed against you because they'll say, "Hey, a Home Depot truck backed into my car on this highway." Right? And that is something that really upsets a driver because they'll say, "Look, I was doing my job great. Like, I didn't run into that guy." Now, you can basically produce HD video evidence of where you were and if there was an accident, who caused it, all that stuff. That's it.

**47:22** · eliminates all the ambiguity, right?

**47:24** · Like now you can just resolve it and look, if there was an accident, the company may choose to just settle it out and and pay it out. But if there wasn't, which is like a very common case, now you can really fight it and say, "Look, we we know exactly what happened."

**47:37** · Drivers love that because I I have to say 90% of the time they're doing a great job and nobody's seeing it, right?

**47:43** · And so that has been a huge unlock is this positive reinforcement of we're analyzing the whole drive. we're seeing all these good behaviors, defensive driving or exonerations, things like that. That I think is what is is sort of the counterwe to the hey what is all this for? Like how is it being used? If you have that in your culture, if you are kind of doing the equivalent of employee of the month but showcasing really great work, I think people get really excited about this.

**48:09** · Also uh from a safety perspective we should remember in physical industries the risk uh of injury is on the person right so in other words like we want everyone to go home the same way they came to work right that is an important concept that I think people don't don't think about if you're working construction you're working oil field services or something like that you take a lot of risk when you do your job every day so it's actually in the what's in it for me it's like we are trying to keep you safe uh

**48:39** · if you have that and you do it in a transparent, thoughtful, you know, respectful from a privacy perspective way, it it goes a very long way with the front line.

### When AI becomes the judge of your work

**48:48** · Very interesting. And that makes a lot of sense. Just to push a little bit, if I if I may, um um in in some ways the eye also becomes a judge of the quality of your work.

**49:01** · I don't know if you agree or disagree.

**49:03** · Uh I'm curious if there's any uh kind of like safeguards about how that happens or should happen in the future and perhaps it's a fact of life. You know, we just had the World Cup and like we we now familiar with the VAR review and it is what it is. You were offside and that's just what it is and technology is here to tell everyone that you are offside. Curious about like what what you've learned. It seems like such an important current topic.

**49:29** · Yeah, very much important. I think transparency again is like the key word here. It's not and by the way our cameras are not hidden cameras. They're they're quite visible. So it's not like a secret sort of recording device. Uh and the the whole idea is to bring the front line along. So we call this change management, right? Like hey, we're introducing these things. What do they do? What are they for? How can you use them? How can they be useful to you?

**49:49** · If you have that conversation early in a transparent way, it tends to be quite constructive because um I mentioned Home Depot earlier. they saw like a 65% reduction in their claims like auto claims. That was a huge win for that organization both at the sort of executive level but more importantly at the sort of like regional level. Um those kinds of wins are what we want to like help create. Now could you use this like in a bad guy kind of way? You could but that would be like who is sitting there watching like each driver?

**50:19** · It's like super boring by the way to like sit and watch drivers, right? Um so when when you kind of are transparent about what the system's doing and what it's not doing and then how the data is used that is like how you get the buy in and and you earn the trust uh of of that entire organization.

### Robots, humanoids, and mixed human-machine fleets

**50:37** · All right. So you sit at the very forefront of of of all of this in in physical AI. Um I'm curious where you see the world going as we maybe uh take a step back. Are we going towards a world of like mixed fleets of of just people and just robots and is that is that what you're seeing?

**50:59** · Yeah, this is the like if we kind of imagine 5 10 years out like where does this go? I I do think yes. Um we expect there to be a lot more robots sort of involved in physical operations. You see this actually if you go into a warehouse today, right? So if you go into either manufacturing or fulfillment center, there's actually a lot of automation robotics going on. And the the cool part about that is it reduces risk of injury to a lot of the human workers like lifting injuries were very common uh 10 20 years ago. They're way less common these days because quite literally the robots doing the heavy lifting.

**51:31** · Now there's still humans working there because there's kind of um all the handoffs and you know there there's some nuance to the operation but we expect something similar to happen out in the field right so think about a construction site or maybe a company building a roadway or you know uh modernizing the grid. There's a lot of kind of repetitive work that has to happen. Imagine you're grading a site like you're making it level. Could that happen during the third shift between midnight and 8 am right?

**51:59** · That could be a really cool way to do productive work on the side of the road where you're just going for like five miles making it flat, right? Um we we see robots being able to do that in the next 5 years. Now, all the rest of it though, it's still pretty messy and construction has like exception after exception. Like you're solving problems constantly.

**52:20** · That's where I think the humans offer a lot of experience and judgment of well, how should this work? And I'm waiting on this building material while I can perform this other thing. Meanwhile, the robots like making the road flat, right?

**52:31** · So, that's kind of what we see in the next few years. The same thing applies, I believe, to logistics and supply chain. So, um now like there's a lot of kind of last mile complication that happens and you have to physically pick up deliver package. Some of our customers, they stock the shelves in the grocery store. Maybe we get there with humanoids and you know, never say never like this stuff always is evolving. But in the meantime, could you automate the longhaul segment between Dallas and Phoenix, right, of all of those, you know, beverage cans coming in or something like that?

**53:02** · So, we see this as an exciting like and uh in terms of what the future looks like. And what we've seen in operations is very diverse, lots of different types of equipment, lots of different types of labor. So, it's going to be, you know, different makes and models and different makes and models of different kinds of robots is my guess.

### Samsara’s role in autonomous operations

**53:19** · And from your perspective as a business, you would just par it all. Uh I guess where would automated trucks and humanoids on the construction site fit in the overall picture at Simsar?

**53:31** · Well, practically speaking, most of our customers would tell you they're supply limited in terms of labor, right? So these are uh labor intensive asset heavy industries. So they welcome this idea of like could I automate some of this labor so we can basically perform more. So that's kind of like our customers are are going to be around. they have like a lot of work to do. What we want to do is provide the sort of uh single pane of glass so they can orchestrate the whole operation, trigger the workflow of like okay that truck is arriving from Dallas.

**54:00** · Let's get queued up so the warehouse systems ready to go and accept it. Um let's make sure that we're notifying our end customer and so on. And then I showed the tracking label earlier. You could put that on the pallet of goods.

**54:11** · So you can track it end to end as it's changes hands through the supply chain as it makes its way to a job site um as it's installed. This is all very opaque today. Like if you think about your, you know, shipments that you receive as a consumer, you might get like five five updates, right? Like left this left the facility, you know, out out on the road, out for delivery, etc. We see like hundreds and hundreds of pings. That's going to be really important when things are moving on their own. you know, where is that um aerospace assembly, right?

**54:42** · Like we have customers who want to know where this really expensive asset is that they need to perform their job right now. That's sort of like unttracked.

### How quickly will autonomous trucking arrive?

**54:50** · Do you think uh automated uh you know self-driving trucking is just around the corner? It seems to be around the corner for cars. I mean obviously it's already happening with Whimos uh and and Teslas now and automated pilot. In three years are we at 10% uh self-driving trucks?

**55:07** · Are we at 75%? What's your gut?

**55:11** · I think on the robo taxi side it's going to happen a bit faster because the operations are much more regional. Um they're much more um similar, right?

**55:20** · Like the way that you and I ride in a taxi across town is going to be quite similar. And so that's I think where you're going to see the biggest sort of like visible impact of autonomous vehicles. Um, on the trucking side, it's also important to realize like there's long haul trucking and kind of like moving stuff from point A to point B.

**55:37** · That tends to be a minority fraction of what the commercial vehicles on the road are doing. Most of the commercial vehicles are um in like industries like field service, right? So, they're HVAC technicians or plumbers, electricians, so people performing some work. Um, and they're also they're either doing something like that or they're in industries like construction where they're building the road. that tends to be where current day sort of like autonomy doesn't work so well. It's like the really messy long tail. So for that reason, we think the adoption might be a bit slower, but it's not like a no. It's just it might take 10 20 years.

**56:10** · And these are industries where again the equipment's highly specialized. Like if you look at cement mixers or you know garbage trucks, like these are customuilt. So for um for the autonomy systems to make their way out to that edge is just going to be a longer diffusion curve than you know for a sedan which is or or a van or something like that which is very much the same.

### AI data centers and America’s infrastructure boom

**56:33** · Great. Maybe to to close um I'm very very curious like you're at the heart of this real economy as we said at the at the beginning of this conversation transportation and utilities and manufacturing and all those you know fundamentally important things. What what's your sense of the reality of American industrial power today? Are you seeing same level of velocity? Are you seeing an acceleration?

**57:01** · Uh is the AI boom and like the data centers like having a real impact on your customers? What what's your um sense of the level of just um velocity?

**57:13** · Yeah, very much. So I I think our customers have it's very clear they're busier than they've ever been before. So from like an American economy perspective, like we're seeing a lot of intensity. Um I was just in the field last week with a large energy utility.

**57:27** · Um and they've been involved in grid modernization and uh they shared with me a really interesting stat. They said, you know, over the last 125 years, we built a certain amount of grid capacity in in megawatts or or gigawatts really.

**57:39** · Um in the next 5 years, we're going to triple that. Like they as a company are going to 3x the amount of power they deliver. And that's like in five years versus 125 years. So that requires a tremendous amount of infrastructure build even with new technologies. It's like they can't work fast enough. U we are seeing that across so many different kinds of industries. And in that case like they also shared you know 90% of that demand is data center related. So as the data center demand continues to skyrocket the energy needs or all these like different bottlenecks that have been appearing.

**58:09** · So many of our physical operations companies uh customer companies are involved in in that directly. I know a lot of people that your customers employ are trades people.

### Should lawyers become plumbers? Demand for tradespeople

**58:20** · What what's your take on evolution of trade? Like the the the idea that you know we've seen we've all seen in the last like couple of years is that uh actually being a plumber uh becoming a plumber might be a great idea if your lawyer job is going to get automated.

**58:34** · Some of it is some level joke but I'm I'm curious about uh what what you what what you take is Yeah. I I I will warn the lawyers thinking about becoming plumbers. It's it's a pretty messy job, right? So, it's much harder.

**58:46** · It's it's pretty hard stuff. Um, so yes, we've been continuing to see that there's a basically a labor shortage, labor bottleneck in a number of different trades, but also things like long haul trucking, commercial driver's license holders, things like that. So, uh, in general, I think there's a lot of growing demand for these uh, professions. And this data center boom is a great example. There are just like not enough electricians, uh, out there right now.

**59:09** · So you see companies like Meta doing initiatives to like reskill people, train them on how to become, you know, a good electrician and then how can you take the people who are trained and make their jobs as efficient as possible. So you don't want them like waiting on materials at a job site like you want to put them to work to perform uh you know wherever their skills are needed kind of thing. So very much kind of a bottleneck, but the trades are in incredible demand.

**59:33** · And I also think that their jobs are getting um more modernized as well because if you think about it as an electrician, a lot of it is getting to the job site and having the materials and knowing what you're going to do. If an AI can kind of help you with that, it takes a lot of the mental load off and you can focus on on the really unique trade kind of value you have.

### Closing thoughts

**59:54** · Well, Sanj, it's been a fantastic conversation. Thank you so much. very excited about uh what you guys are continuing to build and like its sheer importance in the overall economy and it's been wonderful to learn more about it. So, thank you.

**1:00:07** · Thank you. It's been fun.

**1:00:10** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks and see you at the next episode.