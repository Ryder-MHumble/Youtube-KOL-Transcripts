---
title: "Inside Zipline's Autonomous System: 140M Miles, Zero Incidents"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=6bGxm8gX41o"
analysis_report: "[[Zipline- 自动物流不是无人机，而是物理世界的操作系统]]"
author:
  - "[[Sequoia Capital]]"
published: 2026-07-07
created: 2026-07-27
tags:
  - transcript
---
![](https://www.youtube.com/watch?v=6bGxm8gX41o)

The largest commercial autonomous system on earth isn't a robotaxi fleet — it's Zipline, which has flown 140 million autonomous miles with zero safety incidents. Co-founder Keller Rinaudo Cliffton and Eric Watson, who leads systems engineering and safety, explain why the drone itself is only 15% of the solution. The rest spans inventory management, air traffic integration, and engineering systems such as a dual flight computer failover protocol that recently saved a delivery mid-flight. They trace Zipline's path from launching blood delivery in Rwanda in 2016 (when drone delivery was illegal in the US) to a 51% reduction in maternal mortality in that country, a $550 million commercial diplomacy partnership with the State Department, and a cost curve that fell from $300 per delivery to $12. Zipline is now racing toward a million deliveries a day, and a quiet inflection point when autonomous delivery becomes cheaper than sending a car.  
  
Hosted by Alfred Lin and Pat Grady, Sequoia Capital  
  
00:00 Introduction  
02:28 Early Vision and Regulation  
04:09 Rwanda Launch Hard Lessons  
06:49 Scaling to 24/7 Impact  
09:35 Real World Ops Surprises  
11:15 Safety Redundancy Failover  
20:24 Precision Delivery Pod Tech  
25:34 Building the Drone Network  
26:51 Fleet Commanders Explained  
28:22 Scaling to a Million a Day  
29:51 Autonomy Enables 24 7 Ops  
31:52 Reinventing Air Traffic Control  
36:08 Why Zipline Is Vertical  
41:40 First Principles Delete Parts  
44:45 Market Explosion and Closing Thoughts

## Transcript

### Introduction

**0:00** · I remember being in Rwanda early days and going out and meeting with some of the doctors and lab techs that we were serving and asking for them like, you know, how's it going? What what do you think? What's your feedback? Here I am kind of you know, up and coming you know, learning engineer thinking they're going to say something about the drone or some of these things and the main piece of feedback that I received was people get sick 24/7. Why are you guys only open 12 hours a day?

**0:23** · Mhm.

**0:24** · Right?

**0:24** · Especially when you're delivering life-saving blood.

**0:26** · Yeah, exactly. And so that was a really key insight for me where it's like, man, we have found product market fit in a market where yeah, our our you know, our product wasn't great yet, but it was solving a real need.

**0:38** · Uh and so having that that really beachhead market where there's a real problem being solved and when your customer is telling you that their main feedback is they want \[music\] more of your service, it's like that's a good sign.

**0:55** · \[music\] Welcome Keller and Eric um to the show. You guys have been working at Zipline for a long period of time. Keller is the co-founder and Eric, you are in charge of systems engineering and safety and we got lots of things to talk about in this whole world of drones, drone systems and how you guys started in this hardware space before LLMs even started. So we have lots of questions.

**1:26** · Awesome. But you don't like you don't like Zipline being described as a drone company even though you're the you're probably the largest autonomous drone company in the world right now.

**1:36** · I mean, you know, we we've always wanted to be an extremely customer obsessed company and the reality is none of our customers care at all about drones. You know, like we our our goal was always to build an automated logistics system for Earth and to approximate teleportation. And all the customers who are like living on Zipline today, they really don't care how they don't care about the technology operating behind the curtain.

**2:00** · What they care about is their ability to like download an app, open it up, uh you know, see a huge number of different brands and amazing, you know, restaurants that they want to shop with and then click a button and have it delivered to them 5 minutes later. So, we've always really tried to focus on the experience rather on rather than on like the specific technology.

**2:19** · Well, this show is about technology.

**2:22** · \[laughter\] We're excited about that.

**2:23** · This podcast is about technology. What is the underlying technology behind Zipline? You started in 2011. You pivoted in 2014. This is way before anything related to AI or robotics.

### Early Vision and Regulation

**2:37** · AI, robotics, foundation models, anything related to that.

**2:41** · Yeah.

**2:41** · But you've kind of you were before all of that and you're riding the wave of all of the things that have come afterward as well.

**2:47** · Yeah, this was when like starting a robotics company was the dumbest thing you could possibly do. Like why you know, you're talking to an investor in the time about I mean, it wasn't easy and it was particularly hard cuz so many of those conversations, you know, I mean I was 23, 24. Eric joined the company around that time and we were starting to describe this vision of autonomous logistics system for Earth that would be 10 times as fast, half the cost, zero emission.

**3:14** · Um you know, one of the biggest problems when we're trying to raise money for that vision was investors would say, "Isn't this illegal in the US?" In fact, I think that that's the question you asked me when we started talking about this.

**3:23** · We weren't We weren't allowed to fly beyond uh visual line of sight.

**3:27** · weren't allowed to fly at all, really, but like yeah, and and so the answer was yes, it's illegal. And then most investors would be like, "Well, we don't invest in illegal things. So, like we're not \[laughter\] going to invest." But you know, for weird reasons, this is what basically took Zipline down this path of like well, if it's illegal in the US, then we can launch in other parts of the world where you know, the the value of the service would be extremely high.

**3:47** · Zipline decided to launch in Rwanda in in delivering blood transfusions directly to hospitals and primary care facilities. Um this enabled us to have a use case was so powerful that a government would work very closely with us to make it happen.

**4:03** · Make it legal.

**4:03** · And to make it legal um or at least make an exemption to their existing kind of regulatory framework.

### Rwanda Launch Hard Lessons

**4:09** · And um you know, and then the other thing, you know, when it comes to how to think about Zipline as a company, you know, when we launched in 2016, we were like, we have this really cool drone. We put all this work into designing these really cool aircraft that you know, and it's it has all these great fundamental features. And when we launched, it was a total disaster.

**4:26** · Um because the reality what we what we learned in that first year is for the first eight we we'd signed a contract to sign 21 to serve 21 hospitals. And we served one hospital for the first 9 months. And Eric in particular, like how much did you sleep during those nights? I mean a lot of time in Rwanda and didn't sleep a lot.

**4:43** · when you're in the US, like we'd get woken up at like midnight cuz that's when the distribution center was turning on and it would everything would be broken. Nothing was working. And it was totally desperate, constant all-nighters and working through the weekends because we'd made this big error which was that thinking that like the cool vehicle was the majority of the solution.

**5:00** · What we learned during that first year is that the drone is 15% of the complexity of the solution. Like Zipline had drone, the hardware of it.

**5:08** · Yeah.

**5:08** · Is only 15%. to build so many auxiliary software systems, maintenance systems, uh it how do we hold the inventory and do inventory management, how do we integrate with a national civil aviation authority which we'll talk more about, how do we integrate with a national healthcare system, how do we do ordering and demand management. You know, we had to build out all of these other parts of the overall logistics system. So this is the reason I think a lot of people might look at Zipline be like, wow, it's a cool drone company. They build a cool aircraft.

**5:34** · The reality is the aircraft is like 15% of the solution that's required to build something that just feels like magical, reliable, teleportation 24/7, 365 to the now, you know, hundreds of millions of people who depend on the service.

**5:50** · Speaking of 24/7, I remember being in Rwanda early days and going out and meeting with some of the doctors and lab techs that we were serving and asking them like, you know, how's it going?

**5:59** · What what do you think? What's your feedback? Just really being customer obsessed and and wanting to optimize the product. And, you know, here I am kind of you know, up-and-coming you know, learning engineer thinking they're going to say something about the drone or some of these things. And the main piece of feedback that I received was people get sick 24/7. Why are you guys only open 12 hours a day?

**6:20** · Mhm.

**6:20** · Right? And so Especially when you're delivering life-saving blood.

**6:24** · Yeah, exactly. And so that was our, you know, you got to start somewhere, right?

**6:26** · So we started being open 12 hours a day and trying to expand and and grow from there. And so that was a really key insight for me where it's like, man, we found product-market fit in a market where yeah, our our, you know, our product wasn't great yet, but it was solving a real need. Uh and so having that that really beachhead market where there's a real problem being solved and when your customer is telling you that their main feedback is they want more of your service, it's like that's a good sign.

### Scaling to 24/7 Impact

**6:49** · Yeah, we were 24/7 within the first year.

**6:52** · 24/7.

**6:53** · 24/7 365. I mean, on Christmas day I usually call all of our different distribution centers to like thank them and check in with them. So like there is no day when these facilities don't depend on, you know, we went from serving one to 20 to 500 now to 5,000 hospitals and health facilities across the world across eight countries that are served by the system. It's become the largest commercial autonomous system on Earth.

**7:15** · Can you size for us the largest system on Earth?

**7:19** · We just crossed 140 million commercial autonomous miles, which I mean, how many times is that I think that that's like to the sun and back or One of the one of the things that I like is every road in the United States, there's a lot of roads in the United States, driving on every single road more than 30 times.

**7:32** · Wow.

**7:33** · It's a good stat.

**7:34** · It's a lot. That's a lot just to put in perspective.

**7:36** · You know, seeing the impact that that system is now having in across all these eight countries, I mean, University of Pennsylvania just published a study showing a 51% reduction in maternal mortality thanks to Zipline. So, half as many moms losing their lives in childbirth. Um we have you know, across all the different use cases that Zipline serves, some of our partners estimate that we're saving between 10 and 12,000 lives a year. And that impact is growing exponentially as we're now expanding, especially as a result of this new partnership we have with the US State Department.

**8:06** · What is that partnership with the State Department?

**8:07** · December, we announced a $550 million partnership with the US State Department to expand the impact of Zipline's life-saving service across a lot of the countries where we're already operating.

**8:17** · So, with USAID being shut down, the US was really seeking like new ways of engaging in these countries and helping save lives in these countries, but they wanted to do it in a way that would um that that would accelerate the economies of these countries and help the US economically. And so, the new strategy they're calling commercial diplomacy. The idea is that we want all of the developing world should be built on top of US AI and robotics technology.

**8:41** · We should be going and, you know, economically helping. We should be bringing the best that the US has to offer. Interesting thing is when you talk to these countries about what they want, they'll tell you they are sick of, you know, low-quality aid provided by NGOs for free because these services engender dependence and prevent economic growth in the countries. What they want is high-paying jobs, entrepreneurship, technology.

**9:04** · Mhm.

**9:04** · And so, the US is is, you know, going through a big strategic shift where it's like, well, we have that. We have those things.

**9:10** · Like, so let's let's basically go out and incentivize these countries to adopt that kind of infrastructure, make sure that, you know, as these countries are accelerating, they're they're doing it using US robotics and and AI technology. And this is something that will be great for those countries. It saves lives. It saves them money, but it also means that it will it will make it possible for the US to secure our lead in manufacturing and robotics of the decades to come.

### Real World Ops Surprises

**9:35** · I'm curious about, you know, you guys because you now run the largest autonomous system in the world and you you launched it 10 years ago at this point. So, you've been in production for 10 years. You've learned a lot of stuff that your average engineer sitting behind a computer screen has no idea they're going to run into when they try to deploy AI into the real world. And so, I I'm curious what some of those lessons learned are.

**9:58** · And maybe one way to ask the question is what popped up over the last 10 years that you never would have guessed you needed to be good at when you first started launching these systems in 2016.

**10:09** · Yeah.

**10:10** · You know, we started off delivering life-saving products, right? And our customers need need life-saving products all the time in all weather conditions. And you would think it's, you know, wind, these things, but one of the weirdest things is actually solar weather.

**10:24** · So, there's solar flares that happen on the sun. So, they're basically big explosions that send radiation to the earth. They can mess with the ionosphere and that can cause basically the RF signals coming from GPS satellites to be faster or slower than you expect. And that can lead to degradation and challenges in navigation systems. And so, here's one example that, we know, when we were starting off, we didn't think that this was going to be something we have to figure out. Uh but we actually have, uh you know, gone pretty deep in this space and and really it's two things.

**10:51** · One is designing our navigation system and our our GNSS systems to be robust to these conditions to ensure that we can still know where, you know, where our aircraft are with centimeter-level precision in those conditions and those challenging solar flare times, as well as designing the system to have redundancy beyond GNSS such that if things get really bad, we can still safely operate.

### Safety Redundancy Failover

**11:15** · Eric, you're in charge of safety. Tell us about uh what you've learned about safety today and and specifically about the compute failover system that you have.

**11:25** · Yeah.

**11:25** · Yeah, absolutely. I mean, there's so many things that we've learned over the last decade of operating, you know, the the system in the real world. Um one of the things that that we're proud of is uh how we we've developed to to your point um compute failover. So, there's a flight computer, flies the aircraft, lots of sensors come into this uh into this computer, and that basically does a lot of math and sends commands to actuators, right? So, motors, control services, these things. So, this is the brain that flies the aircraft, right?

**11:52** · Um, there, you know, one of the things that we've learned is you need to assume that any part of the system can have a fault, can have a hiccup, something can go wrong. And that's how you really design something to be robust, reliable, and safe. So, what do we do if this flight computer has a challenge? Could be a software challenge, it could be a connector challenge, could be these different things.

**12:11** · Bit flip due to solar radiation.

**12:13** · All kinds of things, right? And so, what we've done is we have two flight computers. And both of these flight computers think that they're flying the aircraft at any given point in time.

**12:22** · They're all receiving all the information from the sensors, they're all sending in commands to the actuators, and there's uh like a kind of a third arbiter, a little computer, that is monitoring the health of those two and telling everyone every other node on the on the aircraft who to listen to, who's actually in charge.

**12:37** · What if the arbiter fails?

**12:38** · Yeah, if the arbiter fails, then the the primary computer that was flying just keeps flying. Right? So, one's in charge, and if the thing that's monitoring itself fails, then now we say, "Okay, like, you know, now we're just going to keep flying on the thing that was good, and we're going to keep flying the mission." Um, so Two heads are better than one.

**12:56** · \[laughter\] Yeah, it's something we're really proud of. Um, we had actually had one of these events happen uh a couple weeks ago, yeah, where we had after a delivery, we delivered the package to the customer, and then we had a a hiccup on the main flight computer, and we switched over to the backup, the aircraft flew itself home, landed, everything was totally fine. So, just, you know, designing the systems to be robust and reliable through and through is is, you know, how you get the 2.5 million deliveries and 140 million miles flown with no safety incidents.

**13:23** · And a lot of what Zip line's doing, it's not like, "Oh, this is totally revolutionary. No one has ever thought about having a secondary flight computer. That's how Boeing 777 works. But the cost of a flight computer on a Boeing 777 is in the millions of dollars. And so a lot of what Zipline's having to do is take a lot of the best ideas that you can see in aerospace safety best practices for aerospace companies.

**13:45** · And you and then you got to figure out how to build that using components coming out of the smartphone supply chain.

**13:51** · Yeah.

**13:51** · do it for you know tens of dollars or hundreds of dollars. You can achieve similar levels of safety to traditional aerospace, but you can move 100 times as fast at 1/100 of the cost.

**14:03** · Yeah.

**14:03** · So you you mentioned that the aircraft is only 15%. Describe the other 85% in like layers and maybe go down deep in some of your systems that are really really sophisticated like your like I know this because of what being a board member like the detect and avoid systems.

**14:21** · So you know how do we test why do we test? Really um the way I think about it is there maybe first of all we're we're not a software company, right? We're a real world AI robotics company. And so there's electromechanical systems out out in the real world. So there's hardware test aspects, there's software test aspects, and there's the integrated system test aspects. We have a lot of different environments that we test a lot of different approaches. I'll I'll name a few of them.

**14:44** · You know on the hardware side we do a lot of component level testing halt testing highly accelerated lifetime testing where we're taking components maybe it's a motor these kinds of things and we're putting them through you know through hell, right? We're putting them through all kinds of challenging conditions making it rain making it hot making it human making it corrosive all these things while we're exercising you know while we're spinning the motor while we're moving things all of the things, right? UV like you name And just to give a context for scale and there are 700 unique components on the aircraft designed from scratch by Zipline.

**15:14** · We are designing not just the flight computer from scratch, the power distribution board, the motor controllers, the battery, the battery management system, the you know, the pod is the smaller robot that we're using to actually make deliveries to people's homes. There's an entire Nvidia Nvidia GPU-powered flight computer on the pod. We're building the electronics that go into the docking station where the Zip is flying in and out of.

**15:37** · Uh we you all of that, even the electric motor being designed from scratch by Zipline because we need a you know, a a thrust-to-weight ratio that is not available in off-the-shelf electric motors. So, you have to design something from scratch. So, you know, 700 unique components, 43 major sub-assemblies on the aircraft, all then coming together on the manufacturing line that you both have gotten to visit. Uh and getting assembled into one overall aircraft. But anyway, that's the So, for So, for each of those components They're all right. Going through this type of testing.

**16:04** · And what you know, thinking about other industries, often times when I talk to people from maybe automotive or aerospace some of these like, "Hey, how do you think about reliability challenges?" And a common answer is like, "Well, I ask the supplier what the reliability of the part is."

**16:16** · Yeah.

**16:16** · And I'm like, "Okay, cool. Like, what if we're the supplier, you know?" So, anyway, so we're that vertical integration where we have component testing on the ground, we have system testing on the ground where we're taking full aircraft for you know, and as well as other parts of the of the system and putting them through vibration tables, wind tunnels, thermal chambers you can walk into, like all of these things um in order to understand is how is this going to break, right? More than just is it good enough? Like, we want to know how it's going to break. And then we can understand, okay, cool. Like, let's make it better. Or maybe it's like, "Oh, that's not too worrisome. Like, great."

**16:48** · You know, we we didn't break any of the ways we were worried about. It broke in that way. Fantastic. So, like, we don't just want to say, "We ran the test campaign and nothing failed. We're done." It's like, "No, no, let's take this thing to failure, right? Let's see where the limits are."

**16:57** · 49° C, which is very hot.

**17:00** · Hot. Cold.

**17:01** · -25° C, which is very cold.

**17:04** · all the things, yeah.

**17:05** · You don't fly anywhere at 49° C.

**17:08** · You do? That's what We wouldn't test at 49 if we're not worried about it. Where are you flying at 49?

**17:12** · I think Phoenix during the summer.

**17:13** · Phoenix during the summer, yeah. So, And then where's -25?

**17:17** · So, northern parts northern parts of the United States. Actually curious what you guys think about that like I could imagine a different version of the world where you guys are like hey look if it's too hot we're just not going to fly.

**17:28** · Totally.

**17:28** · And if it's too cold we're just not going to fly. And if it's raining too hard we're just not going to fly.

**17:33** · Yeah.

**17:33** · And and and like there are trade-offs to be made you know and obviously your customers would prefer that you fly at all times. But how do you think about those trade-offs?

**17:40** · The easiest way to think about the trade-off was because of the use cases that Zipline started with.

**17:44** · That's right.

**17:44** · Which was basically saving lives.

**17:47** · Yeah you can count on us with your life and the lives of your loved ones as long as the sun is shining.

**17:52** · \[laughter\] It's not super compelling you know like \[clears throat\] Zipline would fly and in fact I mean for the first you know for the first couple years we took a lot of risk. I mean we would basically fly. We were like look if it's a life saving delivery happening and there's someone whose life is on the line we're going to go for it. And we had a civilian aviation authority that was you know generally a great partner with us on that front. We took a lot of risk we learned a lot and you know almost always it worked out in favor of like we saved the person's life.

**18:24** · And you know the worst thing that could happen was you know we had a parawing which is the kind of like Zipline's safety mechanism of last resort is we can pull a parachute on the aircraft and bring it gently to the ground.

**18:34** · How often does that learned a lot. It happened very often in the first few years like yeah very very rare today. I mean to put it into perspective you know our original goal was to be 10 times safer than cars.

**18:45** · Actually Alfred was the one put pushing in our last board meeting he's like that's a BS goal we need to be two times safer than Waymo. And so Eric literally went and reset the goal and now we're like the Zipline's target for the end of this year is to be two times safer than Waymo. He's like cars that's like archaic technology.

**19:00** · Waymo I think is about 10X right?

**19:02** · They're about 10X safer than 10 12.

**19:04** · So our goal is to be 2X safer than Waymo.

**19:06** · Yeah.

**19:06** · And the right comparison you're flying. You have to be safe in the in in the air not safe on the ground.

**19:12** · we're substituting something that's typically going in cars, so it's like debatable. But um you know, suffice it to say I mean we we now have 140 million commercial autonomous miles and zero safety incidents.

**19:22** · Zero.

**19:23** · If you were to drive 140 million miles, you would have 600 accidents, 100 injuries, and somewhere between two and six fatalities depending on what country you're talking about. And um you know, this is why it's you know, we really pride ourselves in like picking the right use cases. It's like it's life saving and it really makes a lot of sense to go do it. And also we're going to be by God we're going to be as safe as humanly possible from an engineering and testing and validation perspective.

**19:45** · We really take that um that's a that's a deep part of the DNA of the company.

**19:49** · One last point, you know, what is the outcome of all of that testing that Eric is talking about? The outcome of all that testing is we have individual aircraft in the commercial fleet that have flown more than a million commercial autonomous miles. And so I think people, you know, that's just from an intuition perspective, a lot of people look at this and they're like, "Wow, it kind of seems maybe exquisite or fragile, probably very sensitive to like extreme conditions or weather." I mean, you know, raise your hand if you have a car that has a million miles on it.

**20:19** · It's pretty impressive.

**20:19** · These systems are already like way more rugged and durable and robust than people necessarily think.

### Precision Delivery Pod Tech

**20:25** · ask you about the precision?

**20:26** · Like one of the things that blew my mind when I saw some of the I haven't had a chance to experience in person, you know, a delivery.

**20:32** · Patrick.

**20:33** · I got to I got to go experience it. But just but just in watching the videos, the drone's 100 ft up and it drops the package, it lowers the package to a I don't know, a circle that's got a 18-in radius or whatever it is, right? Like how do you guys achieve such precision even when it's windy, even when it's raining? Yeah. How do you How do you pull that off?

**20:54** · First of all, the aircraft's about 100 m up.

**20:56** · 100 m up. Okay, yeah, there you go.

**20:58** · it harder. Um and uh you know, there multiple layers of there's the the delivery pod that comes down, right? So the delivery pod comes down. That's really the delivery and pick up like precision part of it, right? So the the drone is hovering above.

**21:13** · Um it it you know, it knows where the target is. Maybe let's say it's it's this coffee table, for example, if there wasn't a roof above us. Um so it's this coffee table, and so the aircraft is going to hover above, but it actually needs to consider what the wind conditions are, right? So if the wind's blowing in one direction, then the aircraft's going to kind of be shifted, you know, upwind, right? So it's going to shift in the direction to help um with that with those wind conditions.

**21:34** · And then it's going to lower that delivery pod down. Um as Keller mentioned, we we do uh take advantage of GNSS, so real-time kinematic GNSS. That gives you centimeter level um confidence of of where you are. But the thing is, we don't know the GPS coordinates of this table, right? It's not like someone came in and surveyed the middle of the table and sent us the coordinates, right? No one wants to do that. So what we have to do is we kind of that we use that to kind of get close, right? We're like, "Okay, here's the backyard. Here's where we kind of know things that the things roughly are."

**22:03** · And then the job of this delivery pod is to be lowered down, you know, fight the wind conditions, fight these different things, and be able to use its onboard perception autonomy systems to identify where's the best place for me to leave the package, right? Like if there's a little table and there's a whole bunch of drinks, probably I shouldn't, you know, try and drop down on top of these drinks and make a mess. Maybe I should go to the ground right next to the table, right?

**22:26** · And so it has these autonomous, you know, onboard real-time compute uh to be able to identify what am I looking at?

**22:33** · What am I seeing? And how can I find the best place to leave the package? And then come down, touch the ground, opens its doors, gets retracted back up, and there you go, the package is left on the ground, and the the delivery pod comes back up, stows, and the aircraft flies back home.

**22:46** · A couple big advantages, I mean, just to be specific. So that pod, it not only has its own Nvidia GPU running its own AI autonomy stack, so it Yeah, and survey and like know exactly where it's delivering, even at night.

**22:58** · Yeah.

**22:59** · But um it's it's also controlling its own position That's right.

**23:03** · in the X and Y axis, so it can Yeah. it it can not just know, but then move. Um and the advantage of that architecture, which you can probably guess, but there are two huge advantages of doing it in this way. One is it's quiet. People have this perception of I mean, first of all, most drones are really freaking annoying. Like the sound is just It's basically the most grating annoying sound that you could possibly subject a human to. And so, you know, like we Zipline has a big team of aerodynamics, aeroacoustics, and controls experts.

**23:31** · Every part of the vehicle is designed with sound in mind for the vehicle to be as quiet as humanly possible. We want it to be no louder than the sound of like gentle leaves moving in trees. Um and for the when the pod is delivering, we're keeping the main aircraft 100 m in the air. So, it's like the thing that is creating noise is really far away. That's also a huge benefit from a safety perspective.

**23:56** · Because the only thing that is coming anywhere close to you, your family, your pets, your kids, is something that is super cute and safe. And it's you know, it's really like a Styrofoam kind of like a cute anthropomorphic Styrofoam tub tub.

**24:09** · \[laughter\] Yeah. How long was the technology tested outside the United States before it came to the United States? And was the path to getting into the US now that you're flying in Dallas and delivering packages there?

**24:22** · We spent 8 years, I think, right? About about about 8 years. I mean, I depending on how you measure it, maybe like six six to eight years. And then it was I mean, we launched in Rwanda in 2016, our commercial service. And we really launched the this kind of next generation home delivery service, the thing that's now like in sort of insane hyper scaling mode. That only launched January of last year. So, depending on how you measure it, you could even say it was like almost 9 years.

**24:47** · And then when you got to the US, was it just smooth sailing? What What was the sort of regulatory path that you had to go through?

**24:53** · Yeah, I mean, we really started, I would say, you know, like meaningfully engaging with US, what you know, FAA and other um regulators in the US around 2020 or so. Um so, it doesn't mean we didn't show up in 2025 and everything was smooth sailing. It was really a partnership of working through um as you mentioned in kind of 2016, all of this stuff was there was no pathways.

**25:14** · It's kind of illegal as we as we joked earlier. And so, um yeah, so we really was a partnership to identify, "Hey, you know, we have a shared goals, right? Our shared goals are safe and efficient airspace integration. And so, while we have uh experience doing that successfully in different countries, uh we can bring some of that experience and we have opinions on how this should work, the regulators had opinions on maybe how they thought it should work.

### Building the Drone Network

**25:38** · And so, it was a partnership over the course of a couple years to identify what those paths look like and how we could kind of converge and align before we were able to execute on that.

**25:46** · And you had to show your ability to manage all these aircrafts that are flying. So, you wrote systems, you built systems.

**25:52** · Yeah, I think it's a huge part of, you know, Keller's mentioning that the drone is only a part of the of the, you know, of the overall system, the overall complexity. What we're really building is an infrastructure layer, right? We're building an infrastructure layer that can enable instant access to products. And you don't do that with one aircraft flying from one place to another place.

**26:09** · You do that with a network of um charging locations, hundreds of aircraft uh spread across an area that uh with the autonomous systems in the in the cloud that can understand where am I having demand, where where do I have supply, where do I have aircraft, um what's coming up is about to be the dinner rush, uh what's the weather at these different locations, how can I kind of self-balance these things, as well as how do I efficiently uh pull like pull in people when needed, right?

**26:37** · So, these these aircraft are autonomous, they're operating, they don't require human intervention through these flights, uh but there are times in which it makes sense to alert a person that, "Hey, maybe there's there's an issue here or the weather is a little bit uh the wind is is in this area, right?" So, there are humans, you know, trained aviation professionals that are monitoring our like our network, I would call it.

### Fleet Commanders Explained

**26:57** · They're fleet commanders.

**26:58** · Fleet commanders, that's right.

**27:00** · We used to call them pilots, \[laughter\] you know, cuz when we originally launched in the US, the first regulatory permission we got was to fly one to one. So, that meant that we had one pilot sitting in an Remote pilot in command.

**27:12** · who was sitting in an office basically just observing an aircraft do its thing. And again, you know, it's exceedingly rare that a human should ever have to issue any kind of a command to a vehicle, but we would have one human watching one aircraft. Not great for unit economics.

**27:25** · Uh but as Zipline proved out these systems, we went from one to one to one to three, one to six, one to 20, one to 40, and now operating one to 100, and have plans to go well beyond that.

**27:38** · Well, one fleet fleet commander now.

**27:40** · So, yeah, we technically changed the name cuz I think pilot's confusing. So, we're inspired by Ender's Game. We now call these this group of this team of people at Zipline, we call them fleet commanders. And I'd actually says that in the FAA documentation, we say fleet commander shall do the following. And yeah, they are overseeing a group of 100 aircraft. And to me, this is like the exciting cool thing about technology cuz people think about like, well, you know, what about um you know, how humans used to solve this problem? It's like it's not, you know, the it it it it's cool how robots enable humans to like up level, right?

**28:11** · Like the human is still getting to like strategically manage the system. It's just the human is now maintaining and commanding robots rather than like doing the actual work herself.

### Scaling to a Million a Day

**28:22** · Now that you guys are kind of in hyper scale mode, you solved so many problems in the last 10 or 15 years. What new problems are you running into?

**28:29** · Yeah, I mean, what I would say like thematically, I I mentioned earlier that as you know, getting to 2.5 million deliveries, the you know, the it only happens every couple of years. It's like kind of a one in a million chances. Um these things start to matter, right?

**28:43** · We're we're on the path towards a million deliveries every day. And if you have a one in a million situation, it's going to happen every single day, right?

**28:49** · Yeah, can I just just just to really make that clear. So, it took Zipline from 2014 when we started building the original version of the technology to 2020 4 to do our first million deliveries. Was it the end of 2024? Maybe it was even early 2025 actually that we did we had done a million deliveries in the cumulative history of the company.

**29:10** · Yeah.

**29:11** · So, it's a almost a decade. Maybe say about a decade to do a million deliveries. Zipline is now in the very near future going to be doing a million deliveries a day. And so, that is definitely humbling. It's like, wow, okay. Everything about the way we've been solving the problem is going to break. The bar goes way way up.

**29:31** · Yeah.

**29:31** · And I mean, you know, one specific example, you know, maintenance becomes really hard. Like, you know, the scale of the problems, the number of vehicles that you're managing in the fleet, the cost of a screw-up or if some if a certain process is operating in very inefficient ways becomes extremely high.

**29:48** · And so, there's just high degree of criticality for all these systems. One interesting point though, you know, there are a lot of ways that these systems operate that I think people don't yet appreciate the advantages of autonomy. One good example is that like the system wants to operate 24/7. It does operate 24/7. So, I think people are used to like logistics is generally being like, well, here are the hours when humans are driving trucks.

### Autonomy Enables 24 7 Ops

**30:10** · That's not how these systems operate.

**30:12** · They want to operate 24/7. They can be fully utilized. They they can be as happily delivering at 2:00 a.m. and 3:00 a.m. delivering something so it's like ready for you on your doorstep or in your backyard when you wake up at 6:00 a.m. before you go to work as they are delivering at 2:00 p.m. Um, they can deliver in 5 minutes. They are they are available 100% of the time. We are soon going to be flying vehicles straight out of our factory in South San Francisco into commercial operation. If you've seen, you know, Tesla Model uh 3's and Model Y's delivering themselves to customers, Zipline aircraft will fly straight from the factory into operation.

**30:41** · It's huge advantage from a maintenance perspective that as soon as a vehicle needs to go through some kind of proactive maintenance, it will fly itself to the maintenance depot. So, the human can then quickly make, you know, do whatever process necessary and then the vehicle flies itself back into operations. We can also dynamically assign capacity in a metro based on what the system is seeing. There's no like set home for a vehicle.

**31:04** · It can go to wherever it's needed.

**31:06** · Yeah, I think to to to your question about, you know, getting to a million a day and what are the new challenges, I think, you know, Keller hit on some of them. To the previous thought about the drone is only 15% of the problem.

**31:16** · Really, it's the way that we currently manufacture aircraft, maintain aircraft, support all these things, you know, troubleshoot problems. Like, the way that we do it today isn't going to work when we're at a million deliveries a day. And so, there's still like, okay, we need better tools, we need better software systems, we need better processes, we need better, you know, all these things. So, it's like, um, you know, Elon talks about designing the machine that builds the machine.

**31:37** · And so, you know, this is really one of the things that I see Zipline tackling over the coming couple years is we're going to be investing much more in the machines that build and run the machines.

### Reinventing Air Traffic Control

**31:52** · Mhm.

**31:52** · I mean, from a scale perspective, I think the largest airline in the US is doing about 5,000 flights a day.

**31:57** · Yeah.

**31:58** · Zipline is going to surpass that in the next month. And when we get to a million deliveries a day, Zipline will be doing like somewhere between, I don't know, 40 and 80 times as many flights in the US in commercial airspace as all other airlines combined.

**32:14** · Yeah.

**32:15** · And so, it's obviously a different class it's completely different class of aircraft, it's a totally different kind of problem, but the reality is when you look at air traffic control, they don't make a distinction. And so, there's there's also when you talk about all the, you know, auxiliary systems that have to be built, there is a huge transformation that's going to have to happen in air traffic control as we start to realize that, you know, people are really excited about electrification of vehicles, People are excited about autonomous vehicles.

**32:38** · The reality is what as those transformations occur, there are going to be 10 times as many autonomous vehicles in the air as there are using these teeny archaic constrained things that we call roads.

**32:50** · And so like the sky is a big place. It makes sense to utilize it. You can give Earth back to humans. You can make neighborhoods quieter, safer, less pollution, less traffic. You know, you can make huge improvements to Earth if we can more effectively utilize the sky.

**33:05** · This is going to require huge transformation of how we think about air traffic control in the US. And it means that we need to design it with AI and autonomy in mind rather than the way it was designed which was in 1950 using, you know, pencils and paper and note cards and like a human looking out trying to watch the airplane.

**33:23** · Are you helping the FAA to design that?

**33:26** · It's really yeah, I mean what needs to happen is like collaborative innovation is one way to put it, right? It's like if one company solving this problem for themselves is not going to solve the problem for the industry. And so we are heavily involved in I mean first of all, what a key part of the solution we believe is aircraft should be talking to each other. They should be telling each other where they are. They should be automatically detecting that hey, there's a conflict on the horizon here.

**33:51** · And so therefore we're going to you know, you go up, I go down, right? These kinds of these kinds of things. Um and our aircraft do that. And we're working with other kind of you know, other new entrants into the airspace with autonomous aircraft and autonomous drones to do the same thing. To make sure that our systems can talk to their systems and we can all collaborate to make sure it's efficient and safe use usage of the airspace.

**34:12** · We're also to your point Alfred working with regulators, working with standards bodies to take some of these best practice and innovations that that we and others have developed and try and make them, you know, broadly accepted and utilized so that we can all collaborate and we can all, you know, safely and efficiently use the airspace.

**34:28** · Cuz you guys are have developed a very sophisticated we because we were when we were launching in all these other countries like we had to build something from scratch and so we built the thing from scratch. We provided all this software to the civil aviation authorities so that they could use it to monitor this entirely new class of autonomous vehicles in the airspace. Interestingly, you know, there are multiple public companies in the United States that build air traffic control software that are worth more than 10 billion dollars, right?

**34:52** · And so it's like I often look at that I mean I think there are many companies inside Zip line that are likely it's like oh that's like a public company inside Zip line that is having to get built from scratch. We're building it because every part of the ecosystem we sort of had to build from scratch to enable the overall technology to flourish. Um you know, air traffic control is an interesting like the more you learn the more disturbing it is. I mean we're starting to see the impact you know, you read about like you know, a plane crashing into a helicopter in DC a few months ago. You read about like two planes colliding on um I think on a on a taxiway in an airport.

**35:25** · I don't remember where that was a month ago. You're like wow, why are all these accidents happening? Turns out like 50% of air traffic controllers are over the age of 45, 20% are are about to retire and nobody is going into air traffic control as a career path right now in the US.

**35:42** · And so there's actually a huge labor crisis uh around these kinds of jobs and and so you you you have pressure coming from different angles for like transformation is required. That we cannot use a system that was designed for airspace for airspace in the 1950s. The labor isn't available to do it even if we wanted to and also there is this like giant influx of new technology AI and autonomous vehicles that are going to require us to transform how these systems work.

### Why Zipline Is Vertical

**36:08** · So you're a hardware company and a software company. You build you design your own operations, manufacturing You design your own parts. You build your own aircraft. You write your own software. You You do your own operations. This look pretty vertically integrated company. Talk about the benefits of like complete vertical integration versus buying component parts or buying component software and putting it all together.

**36:33** · And how you get people who come from such different disciplines and domains to see eye to eye and work together collaboratively.

**36:41** · Yeah.

**36:41** · I mean, I think that interestingly, you know, this is doing it is such an incredible pain in the butt that you would never \[laughter\] do it. Like if you, you know, I have this flag over my desk that says we do this not because it is easy but because we thought that it would be easy.

**36:57** · \[laughter\] And this is definitely like the definition of Zipline, you know, and it's such a pain in the butt actually that it's almost if you look at the history of all these hardware companies, they all tried to not do it first. Like you can look at the Roadster, right?

**37:08** · They're like we're going to use a Lotus Elise chassis, we're going to buy the battery pack from a secondary supplier, and we're just going to put the two together and it's going to be awesome.

**37:15** · You know, kind of Roadster lost a lot of money and wasn't very reliable, right?

**37:20** · But like it was it was an important part of getting to the Model S. Zipline, when we started, you know, Eric knows well, we were like buying everything from suppliers, we were like, you know, paying people to design different parts of the system for us or trying to buy off-the-shelf stuff, and we crashed airplanes. I mean, at test sites, and we just we crashed and we crashed and we realized, wow, this stuff is like super expensive and it's also totally unreliable. And so, you know, you know, part by part, you're like, all right, well, like rip that out. We'll design the motor controller from scratch. Okay, rip that out. We're going to have to describe, you know, design the GPS module from scratch. Navigation system.

**37:53** · So, you know, part by part, you sort of like rip it out. And I think there's a fundamental realization, probably similar to the realization that happened that made the Model S possible, is like, hey, if we want to build a really great specific product in this totally new area of technology, we're going to have to design every single one of these components from scratch to meet the specific requirements of this new area.

**38:13** · You know, you might think, oh, like drones, I mean, there are already lots of drones cuz DJI makes, you know, plastic quadcopters and they make millions of them. And like the US buys $20 predator aircraft that can fly 100 mph. The reality is actually both of these systems are very unreliable, and nothing is in a level of like reliability and safety at unit economics that would work for this new industry that Zipline was trying to kind of like pioneer. And so, we realized we had to go build like an automotive-grade solution.

**38:43** · It has to be super reliable, and it has to be extremely cost-effective, cuz you're competing against cars and motorcycles, which are actually really cost-effective. I mean, we've had 100 years to make them reliable and cheap. So, you never do it uh I think intentionally. Maybe you just like slowly freak out and through desperation realize like, "Wow, we got to tear all this out, and we got to build it all from scratch." The advantage of doing it from scratch is like is speed and integration.

**39:10** · And so, you know, our offices, you guys know cuz you've been, but like when you visit Zipline's offices, I mean, we are all like absolutely packed into like, you know, sardines into this small building where you have firmware engineers sitting next to mechanical engineers sitting next to autonomy engineers sitting next to, you know, cloud infra sitting next to um aero-aero acoustics, guidance navigation controls, systems engineering, manufacturing and everything all everybody in one place. And then our factory is a 3-minute drive away.

**39:38** · And so, our team is like on the factory floor working, seeing parts get integrated into the overall system, and then we have our test sites, which are just a short drive away. So, you can go to the test sites, watch the vehicles flying, observe how the system is performing. Like, combining all these things together means that, you know, stuff is always breaking. Stuff's always going wrong. As Erica described, the advantage is when the thing goes wrong, we can basically go straight to the person's desk and be like, "You and I are pulling an all-nighter tonight."

**40:09** · Mhm.

**40:10** · Whereas if you're Boeing and something's going wrong with the battery on the 787, you're like going and suing a supplier and taking, you know, 2 years to try to figure out whose fault it is and like it's three layers deep in the rats nest, you know, cluster of like how these procurement deals and supply chains work for for aerospace. It's why it's so broken.

**40:32** · Yeah, I think back to your your kind of question there about getting these different discipline folks to work together. Honestly, I think it's quite easy. It's easy when you have set up the way that Keller just mentioned, right? Like first of all, everyone's rowing in the same direction. We all have the same goals.

**40:47** · And when you can ground it in reality and it's tangible, then we're all just here to solve the same problems, right?

**40:52** · Yeah.

**40:52** · So, we actually with a vertical integration, with having a very diverse team, we actually cut through a lot of the stuff, right? A lot of the things that happen where oh, you know, that engineer won't tell me what the actual source code does cuz they said it's IP and so we don't actually know what the fault detection looks like and you don't have any of that. You just like literally go walk over, sit next to the person's desk and be like, "Hey, I we failed that test. Tell me about how this part of the system works."

**41:15** · Mhm.

**41:16** · Oh, cool. Pull up the code. Great. Let's look through it. Oh, interesting. You're making that assumption? That's not how I designed it, right? Cool. Let's get to the bottom of it, right? And so this idea of just rapid collaboration where you just, you know, the manufacturing team, the operations team, the engineering team are all just like really together is the way to solve these problems and I I found that it's actually not that hard, right? When you have that those ingredients, it actually makes it, you know, it makes it pretty fast and efficient.

### First Principles Delete Parts

**41:40** · And, you know, too, I mean, Eric's saying that it really makes you realize when you build these like complex you know, AI and robotic systems that combine hardware and software, you really appreciate like the deep religious truth of how dumb requirements usually are.

**41:56** · Mhm.

**41:56** · Question every requirement, which is, you know, the number one part of like Elon's algorithm they talk about at SpaceX. Like question every requirement is like is is like so profoundly and deeply true. You must have every team question every requirement. The requirement is always stupid. When you And you're like, well, you know, it's supposed that you go to this team, that team. You like Often you have to dig like two levels deep to realize like this is But um questioning every requirement is a fundamental part of like getting through this. And then, you know, the other thing is um delete the part.

**42:24** · The most reliable part on an aircraft is the part that is not on the aircraft at all because you deleted it in the last design. That part will never fail.

**42:34** · And you know, you take a lot of inspiration from looking at like the Raptor 1, Raptor 2, Raptor 3. I'm sure you've seen you know, those engines next to each other. Actually, a lot of people who come to the factory now and get to see like the EV3 aircraft. You can see the EV2 aircraft, the EV1 aircraft, plus like the 10 different hardware versions that we built on the initial on the on the first version of Zipline's technology. Um you would just delete, delete, delete. Like, you know, there's a huge amount of it's really hard to delete things. It's an act of courage.

**43:02** · No one wants to delete the thing. You look like an idiot if you delete the thing and then like the system can't perform or doesn't work because you deleted the thing, but like, you know, true confidence in like the physics and the performance of the system enables you to start deleting things. It's a big advantage of having like full integrate full stack integrated control of all of these systems. It makes it possible to question every requirement. It makes it possible to delete parts.

**43:27** · Yeah, I think first principles thinking is a huge part of that. I remember the um platform one aircraft, early days it had a deployable tail hook cuz how it landed. It had this big hook, it's like a meter long, that would come down from the aircraft and make had a line that would catch that and slow the airplane down. It's this kind of complicated contraption. And we had this idea that we should be able to move that complexity to the ground systems and have the recovery system, the landing system, more like an aircraft carrier, like crab the airplane, right?

**43:53** · We can we can you know, put the actuation on the basically a robot that goes up and grabs the airplane. And we're like, man, that's going to make the aircraft so much simpler, so much lighter, so much more reliable.

**44:03** · Um we didn't have it working yet. And it was time to to build that next generation of the aircraft and we're like, so do we building these next week?

**44:12** · Do we build them with the meter long tail hook or do we delete the tail hook and put the 2 cm long tail hook on the back and bet that we can get this thing working. We got a room like delete it, right? Like let's do this thing. And so we're like from first principles it should work. We can make it work. We haven't done it yet, but we can do it. And the next couple weeks looked like myself included a lot of people pulling a lot of a lot of late nights getting that thing working and sure enough those first aircraft came and we caught them and landed them. So it's a lot of courage but that like really being grounded in first principles thinking with a tight integrated team is is how you do that.

### Market Explosion and Closing Thoughts

**44:45** · Is there a version of the future in which instead of delivering life-saving medicine and cheeseburgers you're delivering human beings?

**44:52** · Uh-oh. \[laughter\] And the board member that's control their costs.

**44:57** · \[laughter\] I mean, you know, safe, reliable, battle tested. I don't know. Seems like Seems like if we're going to liberate ourselves from the tyranny of streets it's a pretty decent solution.

**45:09** · Gosh, I I I think I agree with you. Um I think that He's going to come to you and ask for another billion dollars.

**45:16** · \[laughter\] Um I think you know, a couple thoughts. Like one is that I think Alfred knows I'm measured in the way I answer that question because to be clear like you know, building a new infrastructure layer for the planet that can deliver packages as efficiently as the internet moves information is going to be one of the biggest companies on earth. Like it's a huge opportunity and we definitely want to stay like humble and paranoid about how super hard that's going to be. The level of execution for us to scale the way we want to scale over the next couple years.

**45:49** · And you know, to put into perspective I I described this goal of getting to a million deliveries a day in the in the very near future. We now have many partners who are at each asking to buy a million deliveries a day of capacity from Zipline in the last few months.

**46:04** · And so our operating plan has now become our unit of sale. That's a pretty crazy realization and it's leading us, you know, we had originally built then we we'd sized the entire factory to build uh 20,000 aircraft a year. That was what about what was required for a million deliveries a day. Like all of this is kind of being thrown we're realizing the market is way bigger.

**46:24** · And one one thing, you know, when you look at this, you know, totally hyperbolic curve that I think I showed you only a few months ago of like, you know, the what our total flights have total daily flight volumes have done over the last 16 months, the level of complexity of all the different systems that are required to basically like stay on that track um is quite high. Yeah. But you know, there are 5 and 1/2 billion instant deliveries being done by humans in the United States every year.

**46:56** · And that's what you know, we're we're using a 4,000 lb gas combustion vehicle.

**47:00** · It's like Yeah, half an hour to an hour.

**47:02** · Exactly.

**47:02** · It's good marketing that it's called instant, but yeah, exactly. And uh you know, 30 minutes, 45 minutes, an hour, you know, uh significant percentage of the drivers report eating some of the food that they've delivered in the last month, like more than 50%. Um there are significant safety, you know, concerns associated with these kinds of delivery.

**47:20** · But 5 and 1/2 billion instant deliveries, what we're realizing when you look you know, Zipline is now at massive scale in Dallas and we're we're now launching four more metros in the next 4 months. Um when you just look at Dallas, if you were to extend the buying behavior that we're observing from Zipline customers in Dallas to the rest of the United States, there would be 55 billion instant deliveries happening, not five.

**47:41** · Wow.

**47:42** · 55 billion.

**47:43** · Yeah.

**47:43** · There's a huge market expansion. I think it's similar to how people looked at Uber when they were launching in San Francisco and they're like, oh, even if Uber gets to be 33% of the taxi market in San Francisco, it's only going to be a $15 billion company. And obviously what they missed is like Uber's now 10 times the size of the taxi market. You know, like if you make something more convenient and less expensive and a better product experience, people are going to consume a lot more of it. We are clearly seeing customer behavior where customers order every day rather than a couple times a month.

**48:12** · Um I mean, I met a grandma the other day who's ordered 350 times from Zipline in the last year.

**48:18** · \[snorts\] She's 80 years old.

**48:19** · Amazing.

**48:20** · Um actually nursing homes are like big Zipline like they're like big demand centers for Zipline. It makes sense.

**48:26** · Like and actually it's funny old people as like maybe being, you know, not capable of using technology. They're all like living on their iPhones, you know, like they they're probably doom scrolling actually which is maybe not a good thing, but like um they are very comfortable using like, you know, Apple ID, um Apple Pay or Face ID, Apple Pay and just ordering and having it delivered directly to them. Um so, there are definitely not enough humans in the United States to do 55 billion deliveries.

**48:55** · Yeah.

**48:56** · The only way we're going to be able to serve this kind of demand is with automated systems and there's definitely not enough roads. And when you look at, you know, traffic in most of our major cities, you're like, "Oh, can we just like maybe double the number of cars on the road so that we can do way more deliveries?"

**49:10** · It obviously doesn't work. We actually need to be taking cars off the roads if we want to like enable human growth and flourishing. And so, I think it, you know, this this change is it is inevitable.

**49:21** · So, how many flights are you doing a day now and how many will you do in a month?

**49:26** · Zipline is now doing almost 5,000 flights a day um and you know, we're anticipating exiting this year at about 30,000 flights uh a day. And our goal is to get to a million flights a day as fast as humanly possible which we we expect to achieve in the very near future. Like all of the supply chain manufacturing and capacity decisions we're making right now are designed not just to get us to a million deliveries a day, but also um accelerate past that.

**49:52** · The things that are interesting to think about on the unit economics front is like whenever we meet hardware companies and you always talk to them about like how much do you think the system is going to cost? And they're always like it's going to cost X and you're like cool, it's going to cost 10 X just so you know. Like when you build it, it's going to cost 10 X.

**50:05** · That's your advice to founders.

**50:06** · That's my advice to founders is like for hardware companies like if I cuz you know, I'm I'm like try to you know, be a good seed investor and pay it forward and stuff and like you're always meeting these founders and they're always like it's going to cost this much. I'm like cool, just like assume it's going to cost 10 times that and like does it work and what would you do if it cost 10 times that? And I we're speaking from experience. Like when we launched our system in 2016, we were charging $30 a delivery to deliver a blood transfusion over 80 to 100 miles and that was like cost comparable.

**50:31** · And so we that's what we signed the contract for and we thought that we're going to launch a system that cost about $30 a delivery. How much do you think it cost when we launched?

**50:41** · $300.

**50:41** · Yeah, \[laughter\] it cost $300 a delivery and Alfred was surprisingly chill about it.

**50:46** · Um and you know, we were like all right, we got work to do. And so you know, the next year we got it to like 120 and then the next year we got it to 75, then the next year we got it to 40, and then we got it to 28, then we got it to 18. It's now 12 for the kind of you know, the the long range technology that we operate outside the US. Right now what's happening this summer is the the fully burdened unit economics of these systems is just now in the process of falling below the cost of using cars to deliver things. And I think it's it is a cool moment that I think most people don't really realize. It's happening quietly.

**51:18** · Like you're not reading about this in the New York Times or whatever, but um you know, I think that this this thing is happening in the next month or two that is going to have a big impact on the world and how the world looks and and how people how people most people normal people even live their lives because it is now more cost effective to use a robot in logistics than it is to use a human. And that's really good news for the environment.

**51:42** · It's really good news for neighborhoods that are going to get quieter and safer and less traffic, less pollution. And it's really good news for customers cuz you can get things way faster and more reliably. And and and and for less expensive. You know, our customers love like there are obviously so many cool things about the system that, you know, you can talk about and and that you see customers taking advantage of, but like no tip {exclamation point} {exclamation point} \[laughter\] {exclamation point} is like a big, you know, that's probably the number one comment.

**52:07** · I think that um customers love not having to feel guilty and being able to just have a system that they know how much it's going to cost.

**52:17** · Well, thank you, Keller and Eric, for being here with us. I thought you were going to say it it takes longer than you thought, not 10x more than it costs.

**52:25** · But, anyway.

**52:27** · Yeah.

**52:27** · That's a great great way to end.

**52:29** · It does also take a lot longer. I mean, I think, you know, the memo that Sean wrote here at Sequoia a few years ago, I think, is like is deeply true.

**52:38** · I don't know if he'll ever publish that publicly or if it'll be allowed, but I, you know, I do think, you know, suffice it to say, there's an internal Sequoia memo that has had a big impact on me talking about A, why hardware companies are going to be some of the most impactful companies for humanity's progress over the coming decades, and B, why it's super hard to get those companies off the ground and fundraise for them, and C, like how, you know, investors should think about funding those kinds of companies. It's interesting like when you look at the world today to see I mean, it wow, how fast the world changes. Cuz think about it, we spent 10 years being the freaking black sheep.

**53:13** · Like, hardware company, no, thank you. Like, like, \[laughter\] let's invest in, you know, SaaS, let's invest in margins. Like, this this is where the whole future was and like, you know, iPhone apps, blah blah blah. So, I don't know. I guess I feel like um Now you're cool.

**53:25** · Bane. Remember Bane and Batman? What does he say?

**53:28** · Like, you adopted the darkness. I was born in it. Like, man, we built a robotics company for 10 years before building a robotics company was a cool thing to do.

**53:36** · But, um you know, I do think that especially important for like US competitiveness and just for our ability to like build the future that we'd be really proud to hand to our kids and to our grandkids, and to build the sci-fi version of the future that we were all promised, like we got to get good at building stuff again. And we got to get good at building not just you know, uh vehicles and hardware, we got to get good at building infrastructure. Like we're depending on the crumbling infrastructure that our grandparents built for us.

**54:04** · I read the other day the you know, we just installed these like anti-suicide nets on the Golden Gate Bridge. Have you guys read about that project? It cost more to install those nets than it cost our grandparents to build that bridge.

**54:17** · I believe it.

**54:17** · So anyway, we get really excited just like we think the future like promising future is like we should be able to build infrastructure you know, we got to we have to be interested in it um and I think people have to have the stomach for it.

**54:29** · And we have to learn how to manufacture and run complex supply chains again. And we have to be you know, bold and like believe in sci-fi versions of the future if we're going to build them.

**54:39** · Awesome. Let's end it at at that.

**54:41** · Believe in the sci-fi future.

**54:43** · Yeah.

**54:44** · Thank you guys for being with us.

**54:45** · Thank you.

**54:46** · Thanks for inviting us.

**54:50** · \[music\] \[music\] \[music\]
