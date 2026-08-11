---
title: "S3 E19 Seb Boyer from Farmwise: AI to help feed the world"
source: "https://www.youtube.com/watch?v=Iad_LZxZqbc"
analysis_report: "[[Seb Boyer- 农业 AI 的核心不是无人农场，而是把每株植物变成决策单位]]"
author:
  - "[[The Robot Brains Podcast]]"
published: 2023-08-11
created: 2026-07-29
description: "S3 E19 Seb Boyer from Farmwise: AI to help feed the worldWhat's in this episode:00:00:00 Seb Boyer00:01:14  sponsors: Index Ventures and Weights and Biases00:02:20 history of tech in farming00:0"
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=Iad_LZxZqbc)

S3 E19 Seb Boyer from Farmwise: AI to help feed the world  
  
What's in this episode:  
00:00:00 Seb Boyer  
00:01:14 sponsors: Index Ventures and Weights and Biases  
00:02:20 history of tech in farming  
00:07:01 Haber–Bosch process  
00:10:00 GMO vs non-GMO, organic vs non-organic  
00:14:12 AI robotics in farming  
00:17:00 polyculture  
00:21:55 permaculture and polyculture maybe possible with AI robotics  
00:23:50 AI robotics in agriculture used today  
00:26:22 the role of the tractor  
00:29:11 role of FarmWise  
00:31:24 mechanical weeding  
00:33:23 under the hood of the computer vision system  
00:35:37 the way the neural network was built  
00:37:29 general vs specific models  
00:39:02 camera system in a real-world lighting conditions  
00:43:26 robot arm operation  
00:45:23 open for business  
00:47:37 next farming technologies on the horizon  
00:51:24 farming technologies developed by others  
00:53:37 growing up  
00:57:55 relaxing  
  
Links:  
https://farmwise.io/  
https://www.linkedin.com/in/boyerseb/  
  
Listen:  
Apple: https://bit.ly/3DS1jdD  
Spotify: https://bit.ly/3sbSLM4  
Amazon: https://bit.ly/3QAanvA  
Google: https://bit.ly/3KzVQMq  
Acast: https://bit.ly/3KAwdLB  
  
  
Host: Pieter Abbeel  
Production: Bo Obradovic.

## Transcript

### Seb Boyer

**0:12** · Our guest today is is founding CEO of FarmWise.

**0:19** · Following his true passion for sustainability issues, Seb co-founded FarmWise in 2016 with a mission to help farmers transition to more sustainable farming practices and deal with new regulatory and societal changes.

**0:36** · Before co-founding FarmWise, Seb worked as a mathematician for IBM Research and a data scientist for Facebook.

**0:46** · He holds a master's in electrical engineering and computer sciences MIT where he studied machine learning.

**0:53** · Seb was one of the winners of the MIT Tech Review's 35 Innovators Under 35 Europe in 2018 and named to the 2019 Forbes 30 under 30.

**1:05** · Seb, so great to have you here. Welcome to the show. Thank you, Peter. I'm so glad to be here. Thanks for the invite.

**1:11** · Looking forward to to this. Same here. Now, before diving into today's conversation, I'd like to thank our podcast sponsors, Index Ventures and Weights &amp; Biases.

### sponsors: Index Ventures and Weights and Biases

**1:23** · Index Ventures is a venture capital firm that invests in exceptional entrepreneurs across all stages from seed to IPO.

**1:32** · With offices in San Francisco, New York, and London, the firm backs founders across a variety of verticals including AI, SaaS, fintech, security, gaming, and consumer.

**1:46** · On a personal note, Index is an investor in Covariant and I couldn't recommend them any higher.

**1:53** · Weights &amp; Biases is an ML ops platform that helps you train better models faster with experiment tracking, model and data set versioning, and model management.

**2:06** · They are used by OpenAI, Nvidia, and almost every lab releasing a large model. In fact, many, if not all of my students at Berkeley and colleagues at Covariant are big users of Weights &amp; Biases.

### history of tech in farming

**2:20** · Seb, so great to have you here.

**2:23** · Um in this podcast, of course, we talk a lot about AI and if I look at recent episodes, it's been very often in the digital world where a lot is happening in AI, but just as much in the physical world things are happening and what what's more physical than, you know, our food supply chain and making sure we actually stay physically fit, eat good foods, and so forth. Um before we dive into the AI itself, um I think it might be good for us to chat a little bit about the history of tech in farming overall.

**2:51** · Um So, when you think about farming from what it used to be when, you know, farming started thousands of years ago, where did things really started to change?

**3:07** · Yeah, um that's something that I think is really interesting and I spent quite a bit of time studying this. Um I think really like the beginning of the 20th century is when technology or this new wave of technology really hit the the farm.

**3:24** · Um and I I can go over a couple of them.

**3:27** · Like the first one really was um the Haber-Bosch process.

**3:32** · The that process that made it possible to produce fertilizer um out of essentially thin air. Um and that really unlocked a new um degree of productivity and and yield ratios on on the farm.

**3:48** · That really happened at the like the first 20 years of the of the 20th century.

**3:53** · Then you have different revolution. You have the tractor revolution from 19 100 all the way to 1950 1960 where we went from zero farm having tractors to pretty much every farm having tractors.

**4:09** · And that obviously replaced uh horses um and that added like a whole new level of productivity.

**4:18** · Then in the '60s and '70s, we had chemistry um the invention of the first kind of very powerful um chemicals.

**4:27** · And then alongside that, a little bit later, but kind of alongside that, we had um GMOs which also um essentially created uh crops that were much more resilient to a lot of different factors which increased yields um drastically as well.

**4:43** · And definitely after that, in the in the 1990s and uh the 2000, we had we we had GPSs and that again uh helped farmers kind of get reach a new level of productivity.

**4:59** · Um I think that today and since maybe like 10 years ago and and onward for the next couple of decades, we're in the middle of a new wave of um technology um hitting the farm with AI and robotics.

**5:14** · And some of the numbers that I find interesting is that when you look at the um the the some of the numbers that capture the productivity on the farm in in 1900 and you look at the same numbers in in in 2020, uh which is kind of the most recent data um I could find.

**5:30** · It's it's really drastic. Like you for one number, I think one of the most interesting one is just the the sheer number of people that are required to feed um society. In in 1900, about 40% of population was involved with food production. 40%. So, that's al- almost like one in one in two.

**5:53** · Um today it's around 2%.

**5:56** · And the um the the number of acres hasn't changed.

**6:00** · Like we the US farms about the same number of acres than it did in in 1900.

**6:05** · Um so that's a first measure of productivity gain. Another one is just the the yield per per acre.

**6:14** · Um corn, for instance, I've seen like a five to six X increase in um the the just the the weight of produce that comes out of each acre um between 1900 again and 2020. So, I think these are kind of a couple of numbers that to me are striking because um they show us how much technology and these different technology waves have impacted productivity and therefore impacted um just efficiency uh on on the farm. And I think we're not done yet.

**6:46** · And I think AI and robotics, as we're going to talk about, um are going to be are going to have as much of an impact on on farm productivity as these other revolutions had in the past.

**6:59** · So, I'm pretty excited about this. It sounds really I mean, mind-boggling the productivity increases. Um I want to double-click on a few things you said there. You said the Haber-Bosch um process could generate fertilizer out of thin air. That sounds pretty magical.

### Haber–Bosch process

**7:16** · What exactly is that process and what kind of thin air is being used for this?

**7:22** · Yeah, so um it's so like be- before Haber-Bosch, um we we we relied on um am- ammonia that was found on um on on on carries in like mostly in South America. Like we would ship ammonia throughout the world, Europe, US from South America mostly in in a couple of other places.

**7:44** · The there was like a huge trade of that product.

**7:48** · Um and in about the 1900s, we essentially ran out.

**7:53** · Uh and it's an amazing story. By the way, I highly recommend the book that speaks about this from um from Thomas Hager that's called The Alchemy of Air. Uh I think it's an amazing book and it essentially explains how we run out of that um very essential product that all like every farmer in the world relied on.

**8:14** · Um just the world just ran out of it and so there was this huge science race to figure out a way to create it because everyone now relied on it. Kind of similar to almost like fossil fuel today. We all rely on it. We're running out of it. We need to find uh alternatives. Very similar story.

**8:32** · And these two scientists from from Germany, Haber and Bosch, spent, I don't exactly remember, 15 20 years um researching ways to do that. Uh we see that we're not alone, but they kind of won that race.

**8:47** · Uh and that um and and so they figured out this heavy chemical process that essentially is capable of transforming the nitrogen from the air into the ammonia. So, like like essentially um like doing chemistry on the nitrogen from the air to turn it into ammonia that plants can uh can take. And that's the process that today uh feed essentially feeds the world.

**9:15** · Um now, as we're going to see, like this has a whole new um side to it because this process is now responsible for almost 2% of CO2 emissions globally. So, if you look at all CO2 emissions um from rockets to cars to industrial processes, almost 2% of all of these emissions are due to that process and essentially are due to the need for society to produce fertilizer.

**9:47** · Uh so, there huge opportunities to now kind of do better, but that process like 100 years ago unlocked um a new um new level of of productivity and and yield. It's interesting you allude to some of the side effects here and that massive productivity increase, but some side effects that we might want to mitigate or avoid altogether.

### GMO vs non-GMO, organic vs non-organic

**10:07** · And that also came to mind when you mentioned the the chemicals that improve the agricultural yield and productivity because when you go shopping now um go to grocery store here in in California, it'll often say organic food and organic food means the chemicals haven't been applied sprayed onto the crops.

**10:34** · Um or even often in people are the food will advertise non-GMO um to specifically say we're not using the GMO um techniques to to improve yield. Um so so I'm curious, what are your thoughts about that? I mean I mean specifically GMO non-GMO people debate whether it matters or not. Um the chemicals it seems is less up for debate and it seems pretty clear people think it's better to to avoid, but I'm curious about your take.

**11:05** · Yeah, so I think for for most of these um technology revolutions, they came with side effects. Like the first order is awesome. The first order in like being able to apply fertilizer really cheaply, it's amazing. It's kind of magical. Same for tractors. Same for chemicals.

**11:22** · Like when we um when the the chemical industry came up with these powerful chemicals that were able to prevent diseases, prevent insects from from um taking out yield, and prevent um weeds from from growing on fields, that essentially appeared to be pretty magical uh invention. Now, couple of decades later, so that that was like super cool invention and and we obviously um derived a lot of advantages from these inventions.

**11:53** · Couple of decades later, now we're starting to kind of feel the side effects. Um so mentioned the side effect of Haber-Bosch. You're right to say that chemicals um have a ton of side effects. We now know that they're very harmful for the health of farmers to start with. Uh they're most likely a lot of them are not good at all for the health of consumers. Uh you have residues on the plant and so you have residues on on the food that you eat that has side effects actually correlated with uh with cancers.

**12:27** · Um and then you have impact of these same chemicals on biodiversity in and around farms. Residues from these chemicals um kill very essential wildlife like bees for instance. So we now we're starting to really feel all yeah, feel and become conscious of the side effects.

**12:48** · With GMOs, I think that's one is is still up for debate. I don't think it My current understanding is that we just don't have enough data to conclude.

**12:56** · Um there is for now no conclusive um data to say that they're harmful um or that they're safe. Um so kind of this one I think is up for debate. I I don't want to necessarily um uh guess here, but for these other things, we do have very measurable side effects that we now need to to tackle.

**13:18** · So new challenges ahead and some sense opportunity to to take things to the next level and I think it's in that context that you started your company.

**13:26** · Absolutely. As you say, um challenges bring new um new opportunities. And so my co-founder and I started FarmWise um starting from this idea that chemicals have way more side effects than what um we want to tolerate as a society. I mentioned all all of them uh um just a a minute ago. And so we wanted to tackle that particular issue first um and see if we could do better.

**13:55** · Um and as we started, we um got quickly convinced that AI and robotics was actually uh potential great solution to help farmers um do better uh with with chemicals. So that's why we started FarmWise, you're right. There's a lot of revolutions in farming happening in parallel.

### AI robotics in farming

**14:13** · Um and I guess we can all cover them in different orders, but how about we dive in with AI robotics, but other things are on my mind like indoor farming, um vertical farming, all kinds of things that are seeing new things happen. But let's start with the AI and robotics closest to my heart.

**14:33** · Why do you think AI and robotics are so important for the future of farming?

**14:39** · Yeah. Um thanks for the question like so essentially when you look at the big challenges of agriculture today, um you need um so we need to decrease reliance on on chemicals. Essentially, what that means is that we need to be as a society and like farmers first and foremost need to become much more precise. They need to be able to grow as much or more food with drastically um less resources, whether they're chemicals, water, um hopefully land at some point.

**15:11** · So we need to become more precise. And so society need to help farmers um increase precision.

**15:20** · And I think that's typically something that AI is very good at and AI combined with robotics can be very good at. Um we can essentially with new technology capture more information, more detailed granular information, and use that information to have actions to to take actions that are much more specific.

**15:40** · So at FarmWise like the the entire um like the the global view that we have is that we're going to move from a world where farmers essentially do the same thing across the field because they can't really do anything else. So they use a simple machine for instance, they set that machine at the beginning of the field, and they cover the entire field.

**16:02** · That's today.

**16:03** · We think we're going to move from that world to a world where using AI and robotics, the same farmer using a similar machine can now differentiate what he she decides to do on a plant-by-plant basis. And by differentiating what you do on a plant-by-plant basis, you can drastically increase efficiency.

**16:22** · So by efficiency, I mean you can use less chemicals to achieve the same outcome to the same result. You can use um less labor. Like it it doesn't have to be much more um time consuming to do that task. So you can essentially drastically reduce uh inputs with inputs defined, you know, really broad sense, whether it's labor, water, chemicals, land, and achieve the same outcome. I think that's really is the promise of um of AI and robotics.

**16:53** · That's what we're super excited about at FarmWise and why we we started FarmWise in the first place, to unlock that potential. That's a term I've heard in that context and and you tell me if it's relevant or not is polyculture. So let's talk about this a little bit. Um it's kind of related. Now, it's not exactly what I'm talking about.

### polyculture

**17:15** · There this comes up a lot like either uh permaculture or polyculture.

**17:22** · Uh these are kind of potential ideas for how we can or farmers can can do better can can um can produce same food with drastically less inputs. And that comes from the fact that it's been shown that if you uh have different culture on the same field, then you need essentially less chemicals to achieve the same the same outcome.

**17:45** · What people often overlook is that this come this comes as a um with a big cost, which is a cost of being way more labor intensive.

**17:56** · If I tell you that now your field that used to be only salads has now one salad, one tomato uh plant, one one broccoli plant, it's going to be much more challenging to to handle.

**18:08** · So while I think permaculture and these types of um ideas are in very interesting and they're um legitimate ideas to put forward, I don't think that this is where the society wants to go. I don't think society wants to go um to to a system that requires much more human intervention, much more labor to to grow the food.

**18:31** · So I think we can strike a good balance by using AI and robotics to achieve a little bit of that precision that we want without jeopardizing the entire economy like without relying on 10x more people coming back to the field to work the land.

**18:50** · Now, I do want to touch a little bit on indoor farming if you remember me because um because that's another potential idea and that's like if the way I see it is you have like permaculture or polyculture kind of going back to small farms with a lot of human intervention, you have making outdoor farms just more efficient using the AI and robotics, and then you have this other idea of indoor farming.

**19:17** · Um you may or may not have followed the news on that, but over the past like 12 to 18 months, um we've seen kind of a a great reckoning away from uh from indoor farming with a lot of bankrupt like unfortunately bankruptcies happening in that space because today the economics just don't work for most of them.

**19:41** · Um and that's essentially because they compete with outdoor farms that can leverage uh essentially free sun and free water from sunlight and rain. And that's a And And then like much cheaper land cuz they don't need to build actual buildings.

**19:59** · So, it's a very tough competition for indoor farms.

**20:03** · So, I think that indoor farms have a place or have a role to play in the future with like within very specific niche.

**20:14** · Um typically if you want fresh raspberries in the center of New York City in December, you may want to rely on on on indoor farming. Like that probably is more cost efficient than than like doing some I mean than having to ship them uh by plane from the other side of the world. So, there are like a few things like this. Same for the Middle East for instance, um that's pro- probably a good place for indoor farms to go.

**20:44** · Now, I think for most of us and for most of what we eat on a daily basis, my bet is on outdoor farms. My bet is on making outdoor farmers and outdoor farms more and more efficient through technology as opposed to um shifting everything to to indoor. Now, that's a personal opinion, definitely up to debate for debate. But recently we've seen um a lot of again a lot of indoor companies are not doing so well because of the uh um economics. Right.

**21:10** · And some of the indoor farms would have vertical farming so they'd have an even smaller footprint, but I guess need even more water as I understand it too to run it.

**21:22** · Correct. I think like you have outdoor farms, like indoor, like greenhouses, and then even further than that you have uh vertical farming which requires even more lands, more energy.

**21:34** · Um so, I think yeah, the closer you get to um outdoor farm, I think the wider the range of like the wider the market opportunity is going to be. So, I think we we will most likely see a balance between greenhouses and outdoor farms.

**21:50** · But I think vertical farming is going to be a tough sell for for most of the market. Now, I want to push back on one little thing here when you talked about the permaculture polyculture a tomato followed by tomato plant followed by a lettuce followed by a broccoli and you said it would induce a lot more labor hence it's not so practical, but it seems like maybe with enough advances in AI and robotics

### permaculture and polyculture maybe possible with AI robotics

**22:15** · and it might take a while, maybe it wouldn't that wouldn't be a problem anymore and then it could become part of the future, but we just need a lot more innovation on that front first.

**22:28** · I Thank you for saying this and I and I love that you mentioned that cuz this this has been like a a dream a dream of mine for for quite some time.

**22:36** · Um I think you're absolutely right. I think that's almost the end goal of outdoor farm innovation. Um the more advanced we can get with robotics and AI, the more things the more we can decorrelate uh polyculture and these types of um things that are today very labor intensive with um with actual like need to have humans like more and more humans on on the field. So, you're absolutely right.

**23:03** · Um I think there's still quite a way to go and I think that one of the things that people that I typically disagree with with um people that are talking about permaculture um is that like essentially a lot of that is correlated with like going back to almost like technology-less or like farms with very little technology.

**23:32** · Um I I disagree and I think the way we achieve that optimal efficiency is on on the contrary by using a lot of technology to be able to get the most out of um each acre without um without having major impact on the environment around it.

### AI robotics in agriculture used today

**23:50** · Well, it'll be interesting to see when that that'll become possible, but in the meantime, let's talk about what's possible today and near term.

**24:01** · What are some examples of AI and robotics being used in outdoor farming today and what's on the horizon from here? There are a couple of things like first the like information gathering capabilities have been enhanced by our ability to process um a lot of data at very low cost. So, that unlocks some power from uh from satellite imagery um a little bit in some use cases from drones.

**24:29** · Now, this is a little bit harder because data is more expensive.

**24:37** · Um but AI has started to be used with these tools in in combination with these tools to process data at scale uh cost effectively. And that helps farmers.

**24:48** · On the field and that's where um I think things become even more in- interesting.

**24:54** · The AI is concretely starting to be used in kind of two ways.

**24:59** · One um you have companies are building self-driving capabilities. Essentially tools to make the farmer that's typically is like sitting in their in a tractor cab and and kind of doing various things to make him to make him more productive.

**25:14** · And the way they do that is typically having a bunch of sensors and and and being able to precisely drive uh the tool or the tractor. But the This is really the the main tool that that farmers are using to to drive that tool very precisely and and almost autonomously so that the farmer inside that that tractor can focus on more value add tasks. So, that's kind of a first application.

**25:41** · Another applic- application and that's This is where my company plays um is in the precision tasks.

**25:49** · So, the ability for ag equipment to again precisely target specific areas of the field or even specific plants as opposed to doing the same thing throughout throughout the field.

**26:03** · Um and this is where FarmWise plays and this is where personally I see um the the most opportunities cuz I think there is almost no limit to how much more precise you can get if you have good data, good data processing, and then good systems to leverage that data to take more precise actions.

### the role of the tractor

**26:22** · Now, Sam, for somebody like me who has actually never worked on a farm and not really closely observed what's going on there, can you maybe take a quick step back and when a tractor drives through the field, what is the job of that tractor or whatever devices are attached to that tractor?

**26:40** · Yeah. Um So, first of all, tractors as their name um uh uh indicates, they're here to tract. So, the typically tractors actually don't do anything.

**26:52** · What tractors do is that they tract, they carry implements.

**26:57** · Um and these implements are the ones that are actually doing something. So, first and foremost like tractors in of themselves, they don't do anything, but they carry stuff that do things.

**27:09** · What are the things that need to be done? Uh essentially if you look at the cycle between um sitting and harvesting, so first you have these two things, sitting harvesting.

**27:18** · In the middle, you have a couple of different tasks that need to happen.

**27:21** · Obviously that varies depending on crop types, geographies, seasons.

**27:27** · But by and large, you um need to water need to water the field.

**27:31** · That's typically not done by tractors.

**27:32** · That's typically done by fixed infrastructure. So, things that don't look like tractors like actual rotating gears or um pipes that are buried in the ground, things like this.

**27:44** · You have all of the um treatment the the chemical treatment. So, fungicides and for diseases like to control diseases, insecticides, herbicides.

**27:56** · These are typically applied by um sprayers. So, have um a very wide like 100 ft wide bar with dozens of nozzles that are applying specific chemicals whether fungicide, insecticide, uh herbicides to prevent diseases, to prevent insects from from coming to the field or to prevent weeds uh from from growing.

**28:23** · So, that's one task. Then you have um fertilizing. So, fertilizing can be done different ways either through the water so through that fixed infrastructure that I talked about or through tractors with again like um some some special gears, sprayers that are applying uh fertilizer directly on top of the crops.

**28:44** · And these tasks typically happen more than once. So, you can imagine that essentially on a typical acre of uh farmlands, there is something happening almost every day um or at least three to five times um a week. So, the fields are busy. Like they don't stay idle for like three or four months before harvest.

**29:05** · Um farmers do a lot on them using tractors and implements.

**29:10** · I hope that helps.

### role of FarmWise

**29:11** · That helped a lot. Thank Thank you.

**29:15** · Now, with that context in mind, how is FarmWise changing that process?

**29:22** · We essentially build um new type of implements. So, the things that are um carried by tractors. And the the way our implements are new is that they come um from the get-go with with cameras and computers um that are capable of taking pictures of plants, analyzing these pictures in order to decide on specific actions to take on each of these plants.

**29:52** · So, for instance, our first product is a mechanical weeding implement.

**29:57** · So, what that product does is it again takes images of plants.

**30:01** · Um it's the detects each individual plant and classify them into species. So, let's say like this is a broccoli um or this is a weed for instance.

**30:14** · It locates these plants in the the 3D space as precisely as we can.

**30:21** · Um so, we have the species, we have the location in the 3D space.

**30:25** · And then we use that information to move tiny blades about size of the size of a finger. Um we have about um like 30 of them on each uh of our machines.

**30:38** · And these tiny blades are going to come to like 1 in deep into the ground to precisely cut out the weeds uh in the field.

**30:49** · And the trick here is that you don't want to hurt the crop. You have a field, you have crops that you want to harvest at some point, and you have weeds that you don't want, and they're actually competing with your crop for water, for sunlight, for nutrients. So, you want to get rid of them.

**31:03** · So, what our machine does is essentially getting rid of these weeds uh but the way we do it does not use any like not a single drop of of chemical product.

**31:16** · So, we use essentially AI and robotics instead of chemistry to remove weeds. So, it's kind of an the the AI herbicide if you will. Now, this is very interesting on many fronts.

### mechanical weeding

**31:26** · First of all, one call out is that I think I've heard uh something similar from a startup called Blue River acquired by John Deere, but not exactly same. I think they would do precision spraying, but you're saying you can even let go of any kind of spray. You can not use any chemicals.

**31:44** · You can directly mechanically remove the weeds. Is that right?

**31:48** · Absolutely right. So, Blue River is a great company that we know very well, and you right like they came up with a way to spray more precisely on plant on for specific use cases in in salad lettuce specifically.

**32:04** · Our system um essentially use mechanical blades instead of instead of chemistry um but requires the same or even greater level of precision to be able to move these blades uh in in the ground.

**32:20** · Now, after you cut the weed, do you need to pick it up or can you just leave it there?

**32:26** · Great question. Um actually you it's fine to just leave it there.

**32:31** · Be- because um the reason for that is typically when farmers do these um processes, they try to go early when the weeds are pretty small yet because once they're too big, essentially damage is already done. Like they already took all of the nutrients and and water that you did not want them to take in the first place.

**32:51** · So, you go there when they're tiny. And the good thing when they're tiny is that it doesn't take much to kill them. So, essentially disturbing their roots enough by cutting them, kind of leaving them on top of the soil is enough to to kill them. And what happens is that they're going to dry out under the sun in a matter of a few minutes.

**33:13** · So, that makes our job easier because we can essentially go out there disturb them enough um not pick them up, and they will still die. I'm curious about the It must be a computer vision system that's ultimately helping the machine target the weeds. Um can you say a bit about what kind of data do you use to train the system? What's under the hood?

### under the hood of the computer vision system

**33:37** · What's being trained? Uh what kind of level of precision are you able to achieve?

**33:42** · Yeah, um so from the start like we designed our our computer vision system to be deep learning based end-to-end.

**33:50** · So, we had that kind of data uh angle very early on.

**33:55** · We rely on our own data. So, when we started and it's still mostly the case today um but when we started 7 years ago, obviously you could not um search on Google any uh like big large data set of plants on farms.

**34:12** · So, we had to build that data set ourselves. So, the way we we've done it is through different generations of of robots, of machines on the field we stored we we captured and stored every single um plant that we've seen.

**34:28** · Um today that amounts to we're like getting close to about a billion plants in our database. So, we have about a billion individual image uh images of plants that we've gathered uh through the years. So, that's the data. That's the raw data that we um rely on to build a system.

**34:50** · Uh from there like we use um essentially labeling techniques to go from uh from the raw images to labels. And then we train model to be able to do that differentiation that I was talking about, being able to label species and then um kind of estimate the geometry of each plant through deep learning uh methods.

**35:10** · So, that's what um that's how the system works or part of the system cuz that's only part of that's a piece of the equation, but then you have systems around it both before that processing to capture very high very highly accurate images and after the processing to be able to do something with with their their predictions. Going one level deeper even, I got a quick question here.

### the way the neural network was built

**35:39** · Um I can imagine two ways of building this neural network in terms of the outputs.

**35:46** · Uh one could be weed or not weed, just a binary classification. Another way could be an actual classification into each of the into each of the individual plant species, which would be many more possibilities on the output, but probably also require network to think much deeper and maybe perform better as a consequence.

**36:08** · Yes, that's a that's a great point. And actually that shifted over the years.

**36:12** · Um so, when we started like we started with um essentially building models that were specific to e- each plant species. So, we would go on a broccoli field to take that example again and essentially train the model to be able to do a simple broccoli not broccoli type of prediction.

**36:35** · Um that was like level one. Now, we do much more complex things and which actually improves the overall accuracy by having a larger model that is able to leverage much more data because we don't only we don't only work on broccoli like we work on about 12 different um plant species. So, we have data set on romaine the data set on celery, on carrots, on tomatoes.

**37:00** · Like we have um dozens of millions of images for each of these plant species. So, the ability for one model to leverage all of that knowledge we actually were able to make it work so that it improves the overall accuracy even on specific task.

**37:19** · So, now we train kind of more um centralized larger models that are achieving higher accuracy, but we started off by building like simpler smaller models. It's very interesting to hear because we're at Covariant we're saying the same thing. It's better to train a single model for all the items we might want to pick and place in a warehouse rather than warehouse specific models for the specific items in those warehouses. Somehow the one bigger model understands in some sense items in warehouses better even when applying it later to a specific warehouse.

### general vs specific models

**37:54** · Yeah, super interesting. Um for us it was both like a um question of accuracy. So, we we were able to achieve better accuracy. It was also a question of usability.

**38:06** · And the ability to have one single model that kind of works seamlessly on many different type of fields is of pretty good value for us because that's kind of one last step for humans to make mistakes.

**38:21** · Uh because before that like we relied on some human operator to pick the model. Essentially to tell us which type of um plant this field is.

**38:33** · That would be right 95 98% of the time, but you still like two two to five percent of the time like you have mistakes like human errors that are misleading the model by telling him oh you're on a tomato field uh but you're actually on a celery field. And that will mess up the entire system. So, by moving to a more general model, we can also kind of remove one more steps one more step from uh from the the user uh experience.

**38:59** · When I think about uh deploying AI robotic systems out in the fields I mean these fields the lighting conditions can change dramatically, which seems like it would affect what the camera sees, how well computer vision will be able to do.

### camera system in a real-world lighting conditions

**39:22** · Um there is so much I mean, dirt is maybe not the right word because dirt makes it sound like a like a bad thing, but there's so much physical stuff that can get into the way of both the robot's functioning and the camera's functioning.

**39:40** · How do you deal with all of that?

**39:43** · Yeah, that's a great That's a great point. And obviously, we've we we've put and we still put a lot of effort into making sure that this works well.

**39:52** · Uh and it's not easy.

**39:53** · So, the first thing you mentioned, you're totally right. Like lighting conditions. Like there is no two similar uh days on on the field. Like you have clouds, shadows, all of these different things.

**40:06** · Um we had different solutions over the years. Like initially, we started by having shades.

**40:10** · So, we'll kind of cover the system with shades, make sure to remove as much um light coming in as possible, and then have very basic lights inside the shades to sort of have a consistent um lighting across that small portion of the field that the camera was looking at.

**40:29** · We used that for for a while. It kind of worked well. The downside of of it is that it's it's heavy. Uh you need to to add hardware that and hardware can break. Like it does come at a at a at a pretty significant cost in terms of operations and and and capex, like hardware cost.

**40:48** · More recently, with the last generation of our product, we switched away from the from from this solution.

**40:56** · And now we use um custom lights that are extremely powerful and that we designed specifically to get a um consistent homogeneous lighting across that small part of the field that we're looking at and to essentially beat the sun at its own game uh by being able to over we essentially over light shadows, so they essentially disappear. It's pretty impressive.

**41:24** · Um and even with under the worst conditions, when you have like your super bright sun and with someone standing that kind of casts a very clear shadow, all lights are able to um compensate for that. And you get an image that where essentially you can't even notice the the the shadow. So, that's our new solution now.

**41:46** · And that provides us or provides the computer or the camera with with very homogeneous um images, which obviously makes it way simpler for models to learn from. Uh kind of we remove one degree of freedom. We remove one dimension of variability from the data set by controlling the the lights uh very precisely. Just overpowering how much light the sun would Exactly.

**42:12** · Do you need to do anything with the cameras to make sure they're not overexposed?

**42:16** · Um obviously, yes. Like we we I mean, they they they work together, the lights and the cameras. So, we put a a great deal of effort into picking the sensors, tuning the the parameters of the camera so that we we're not over over overexposed. Another constraint that we have is that all systems are taking pictures at a pretty high speed.

**42:37** · So, we need to handle like we need to have very um uh small exposure time and things like this. So, we have um good part of the team that's dedicated to making sure that all of these hardware systems uh work really well together. And they're not kind of off-the-shelf um systems that we can buy. Like we need to handpick a lot of the components to be able to build these um systems that are going to be very reliable in terms of accuracy and terms of overall um robustness.

**43:08** · Cuz obviously, on top of everything that we mentioned, all of that needs to handle water, dust, winds, um uh and and a lot of mark like a lot of um perturbations that that that that happen to them. So, we need these systems to also be very robust. When you're cutting essentially the root into the root of a weed, um is that a robot arm that extends to get there? How does that work?

### robot arm operation

**43:35** · And how does that interact with the fact that this field might well be a little bumpy and the tractor might that whole thing might be shaking quite a bit. Yet, you need to be very precise to not cut into the plants. We use like we call them robotic arm. They're not your typical um 15 degrees of freedom type of uh robotic arm.

**43:58** · They essentially have three degrees of freedom.

**44:01** · They can um each blade can essentially move left and right.

**44:06** · Um they can kind of rotate uh with a with an axis that's kind of um coming from like a top-down axis around the top-down axis.

**44:18** · And then um they can the entire thing can uh move up and down to follow the bumps of the field.

**44:25** · So, these three degrees of freedom are essentially enough for the precision that we need. Cuz we want the blades to follow kind of a path which is um almost in the 2D plane, but not exactly. Cuz the 2D plane is actually like this.

**44:39** · So, it's kind of a 2D plane that um with hills and and valleys. So, we need three degrees of freedom to to achieve that. But we don't need like very sophisticated, expensive robotic arms.

**44:52** · Uh and actually, we could not mhm do with these types of things because we need um all robotic arms to move very quickly.

**45:02** · Um to give you a sense, like they're typically about like between 30 and 50 ms between two actions, two independent actions of the same robotic arm.

**45:12** · So, we need these arms to move not only very precisely, but also very quickly.

**45:17** · Um so, limiting the number of degrees of freedom is a key to uh uh to to to achieve this. We've talked a lot about the the technical side of what you're doing. Uh can you say something about the business side? Are you open for business or is this just prototypes?

### open for business

**45:31** · Is there places where if we visited a farm, if we got to access, we could see your system in action?

**45:37** · Yeah, we're we're definitely open for for business. Uh we take we take orders.

**45:41** · Uh if you're interested, you can go on the website, schedule a demo. Um we currently have kind of two ways that farmers can access our technology.

**45:51** · The first one and the historical one, the one we've been deploying for a couple of years now, is a service model.

**45:58** · So, the first way farmers can access our technology is by paying us on a per acre basis.

**46:03** · Um and with that service, like we are all operators wearing FarmWise hats, come on your uh fields and use our technology to perform the task. Um farmers have been using this for for three years now.

**46:19** · They pay us on a per acre basis for really the work that we do.

**46:24** · Now, more recently, like with with the the maturity of the product reaching new new new levels, we started to sell. And so, we're now also open to sell our next generation of our new generation of of machine to farmers directly. So, they can use with their own operators um this technology that this technology themselves. There are mostly a lot of advantages for them to purchase the equipment cuz they're like they have they have more more flexibility. It's also better uh economics.

**46:57** · But we need to achieve the level of product maturity that we have today to be able to start doing this. So, this is what we do now. Um we work with farmers in mostly in California and Arizona in the US, so West Coast of the US. West and South Coast of the US.

**47:14** · Um and we're looking at obviously Europe for expansion in the next couple of months. Very exciting. Uh it's in at least in my experience, it's never easy to truly get things working in the real world. And you're doing that now for three years and counting. Uh congratulations. It's it's amazing.

**47:30** · Thanks. It's big team effort. Yeah.

**47:32** · Thank you. I'm sure it is.

**47:36** · Now, when you look ahead, um right now, you are doing chemical-free weeding effectively, right? Um and that in itself, I imagine, can be a very large business. But as the technology is maturing, I imagine you're you've been thinking about next steps.

### next farming technologies on the horizon

**47:56** · So, what are the next technologies you want to develop and then bring to market, both yourself and maybe I'm also curious maybe things you wouldn't take on, but that you think are on the horizon that we could see happen. But maybe, you know, you'll let other companies take on. Hm. Yeah, for sure.

**48:12** · Um so, there are a couple of very exciting uh new projects that are happening at FarmWise right now. Like some of them I can't talk about, but some of them I can. Um one of the kind of key um directions that we're taking is finding ways to make our technology available to a broader set of um farm farming machines.

**48:34** · So, we've developed, as I mentioned, a huge um software stack from capturing images to to training to deploying models.

**48:43** · I also talked about the all of the efforts that we put into the cameras and the the data capture systems that we have today.

**48:53** · Uh and obviously, there's the entire kind of robotics side of things.

**48:58** · We're actively working on finding or or or like designing products to adapt the first two, adapt the the software stack and adapt the data capture capabilities to other farming machines. And so, we're talking with OEMs, like ag manufacturers, and um we have active discussions with them to to work together to essentially make most farming machines uh smart. And that's kind of our dream.

**49:23** · That's uh been my co-founder and I dreams for for seven years now, seeing every farming machines in the world um equipped with cameras and computer vision algorithms to be able to um be drastically more precise because we're doing it on weeding today, but the very same principles apply for fertilizing, for for fungicide application, for insecticide application, and even for like to to some extent harvesting and and and all the tasks.

**49:55** · So, we're super excited to now that we have a product that's working for one task to be able to expand this to to other tasks as well.

**50:05** · And then there is another dimension of expansion for for this type of technology, which is working on different type of crop. I talked a lot about broccoli for instance. We work today on vegetables, mostly vegetables.

**50:21** · And we have more than a dozen crops that the same machine can work on.

**50:25** · We're actively looking at adapting the technology to be able to work on different segment of the farming industry, namely the big acres farm, the corn, the soybean, things like this. You can think about fruits and trees as well.

**50:41** · So, each of these different segments come with different specificities that you need to account for, but we're very excited to essentially take the same principles the and some of the same technology and adapt it to these different tasks and to these different crop types.

**50:58** · So, that's in a nutshell kind of what's next for us.

**51:01** · And that's obviously a pretty exciting exciting thing for for for me and for for us.

**51:07** · With the goal being the same always, which is how we cut on the inputs, the the chemical inputs, the fertilizer, how we drastically cut that while achieving same or better outcome in terms of yields and and quality of of food produced. Are there other things that are on your on your mind that you don't see within the scope for for FarmWise, but that you think are also going to really affect how farming is done?

### farming technologies developed by others

**51:33** · In terms of like the broader technology landscape, I think there is like super exciting things happening on the um like bio biology side, both the genetics and the bacteria work. Like we're just starting to scratch the surface of understanding what makes a good soil and how to use bacteria and and and and the the soil biome to optimize yields.

**52:02** · That's kind of an all new type of technology that I'm pretty excited about. Has nothing to do or very little to do with AI and and robotics, but I think it's very exciting to So, the combination of good genetics with good understanding of the the bacteria ecosystem in the soil, I think is a very exciting exciting field. It reminds me of other things that are studied a lot these days.

**52:26** · In fact, in in just a couple episodes ago, I talked with Yaniv Altschuler from Meta and they're optimizing the essentially the digestion of cows with effectively you know probiotics supplements, which is not in the soil, but the soil is in some sense the digestion system for the plants where that lives and this is the for the cows very very very similar in many ways.

**52:55** · Bacteria, the right bacteria Yeah.

**52:58** · somehow optimizing things in a way that you know is just so much better than otherwise. That's that's very cool. That's very cool.

**53:06** · Actually, um in terms of productivity, I also know that like from the 1900 to 2020, um milk production per cow has I think 5x.

**53:19** · So, it's not it doesn't only like these productivity gains don't only apply to acres. They will also apply to different segment of the food production industry including milk.

**53:30** · So, I'm not surprised that there is still a lot of innovation to be done in in that segment as well. So, I'm curious, where did you grow up and how did you end up so interested in the combination of AI and farming? Yeah, so I I grew up in the suburbs of Paris for most of my life.

### growing up

**53:54** · Went to undergrads in same like different suburbs, but still around Paris.

**53:59** · I then moved to the US for for grad school. Spent two years at MIT studying computer science and that's when I first got introduced to AI technologies and and machine learning, deep learning technologies that obviously I found fascinating. So, I spent my two years studying these technologies and playing around with them.

**54:20** · So, that's essentially when I really fell in love with the technology side of of things.

**54:27** · And then when I graduated, so that was like summer 2016 I graduated from MIT and I had this very good friend that was actually graduating from from Stanford. We had gone through undergrad together.

**54:41** · And we decided to explore like how could we apply this very new cool and what seems to be very powerful technology to do something good in the world. That's kind of very cheesy maybe, but but but true. And we explored a few different industries and we got quickly fascinated by by farming for a couple of reasons. Like the first one being it's it's a massive industry.

**55:09** · It touches everyone uh and it's obviously worldwide and has a massive impact on the environment. We talked about this at the beginning.

**55:18** · So, the impact of that industry is is massive. It's not only economically massive, but it's massive in terms of negative impact, but also opportunities to make that impact better.

**55:29** · So, that's the first that was the first reason. And then when we started to talk to farmers, the like we we talked to uh almost 100 farmer probably like we we would go to to farmers markets and kind of ask them to if we could visit their farm and then accompany them to their farm to kind of spend spend time with them.

**55:51** · We discovered that they had a lot of problems but that no company was really kind of even looking at leveraging AI and robotics to provide some new solutions to them.

**56:04** · You had on one hand the big ag companies, the the John Deere and Monsanto of the world.

**56:11** · They were not talking much about AI, data, or robotics at the time. Almost nothing.

**56:19** · And then on on the other side you had the obvious tech companies, Facebook, Google, like all of these large tech companies.

**56:26** · And quickly we realized there was no way on earth they're going to ever sell directly to farmers. Like farming is very specific industry. It's very hard to sell into.

**56:37** · Um So, that's what got us very interested.

**56:40** · Like we we figured that there was probably bigger opportunities there because because of that of that discrepancy between the size of the problems and the number of people actually trying to address them. And so from there you just incorporated and and got going? Pretty much. We incorporated.

**56:58** · We kind of I So, I was living in Cambridge in Cambridge, Massachusetts at the time. I moved to to San Francisco and then we started the I guess pretty classic startup um startup game. We raised from angels. We went through an incubator.

**57:14** · We did very weird looking prototype that didn't work, but attracted a little bit of a customer validation that we used to raise money and then kind of we we went around that circle a couple of times to to raise more and more money and and hire a bigger engineering team to to finally kind of build a product that that made sense for for farmers.

**57:39** · Well, congratulations on on this journey and I'm very happy with personally with what you're doing because I think you know healthier food is going to help so many so many people, better climate situation. So many good things are coming out of what you're doing. Now, of course you keep very busy, but do you ever have time to relax and if so, what do you do?

### relaxing

**58:03** · Um I Yeah, I sometimes have time. It really depends. I did not have time for many years, but yeah, I So, couple of things I I mean I love reading. I mentioned one book. I think it's I highly recommend that book, The Alchemy of Air.

**58:18** · But I I love reading. I spend quite a bit of time reading.

**58:21** · Um I love meeting interesting people that are doing um interesting things either in academia or or businesses in a wide variety of of domains. Like I I studied physics and maths in in maths in in undergrads, so I had a sweet spot for for everything that's like highly scientific.

**58:41** · So, I really enjoy like meeting people that are doing interesting things like this.

**58:46** · I maybe like yeah, I play chess a little bit. I started to play chess a few years ago.

**58:53** · And then I I try to play squash once a week when when when I have time. Also getting some some physical exercise and Trying to trying to. It's great. Well, Seb, this has been such a wonderful conversation.

**59:08** · I learned so much. Thank you so much for joining us. Thank you for having me. It was a pleasure, Peter.
