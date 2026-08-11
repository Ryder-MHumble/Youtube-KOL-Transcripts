---
title: "Top AI News: Sonnet 4.6, Grok 4.2, Gemini 3 Deep Think, and OpenClaw | EP #231"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=HklyjXKYFng"
analysis_report: "[[Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界]]"
author:
  - "[[Peter H. Diamandis]]"
published: 2026-02-18
created: 2026-07-27
tags:
  - transcript
---
![](https://www.youtube.com/watch?v=HklyjXKYFng)

Welcome to our first MOONSHOTS Live episode.  
  
Peter H. Diamandis, MD, is the Founder of XPRIZE, Singularity University, ZeroG, and A360  
  
Salim Ismail is the founder of OpenExO  
  
Dave Blundin is the founder & GP of Link Ventures  
  
Dr. Alexander Wissner-Gross is a computer scientist and founder of Reified  
  
–-  
  
My companies:  
  
Apply to Dave's and my new fund: https://qr.diamandis.com/linkventureslanding  
  
Go to Blitzy to book a free demo and start building today: https://qr.diamandis.com/blitzy  
\_  
  
Read the Solve Everything Paper: https://solveeverything.org/  
  
Get notified once we go live during Abundance360: https://www.abundance360.com/livestream  
  
Get access to metatrends 10+ years before anyone else:https://qr.diamandis.com/metatrends  
  
Connect with Peter:  
X: https://qr.diamandis.com/twitter  
Instagram: https://qr.diamandis.com/instagram  
  
Connect with Dave:  
X: https://x.com/davidblundin  
LinkedIn: https://www.linkedin.com/in/david-blundin/  
  
Connect with Salim:  
X: https://x.com/salimismail  
Join Salim's Workshop to build your ExO https://openexo.com/10x-shift?video=PeterD062625  
  
Connect with Alex  
Web: https://www.alexwg.org  
LinkedIn: https://www.linkedin.com/in/alexwg/  
X: https://x.com/alexwg  
Email: alexwg@alexwg.org  
Substack: https://theinnermostloop.substack.com/  
Spotify: https://open.spotify.com/show/1thtZk5vHTXbtDHezPT7tl  
Threads: https://www.threads.com/@alexwissnergross  
Youtube: https://www.youtube.com/@alexwg  
  
Listen to MOONSHOTS:  
  
Apple: https://qr.diamandis.com/applepodcast  
Spotify: https://qr.diamandis.com/spotifypodcast  
  
–  
  
\*Recorded on February 17th, 2026  
\*The views expressed by me and all guests are personal opinions and do not constitute Financial, Medical, or Legal advice.

## Transcript

**0:01** · AI is easy. AV is hard. We're trying to get our damn AV working. I'm in Germany.

**0:05** · It's midnight here. \[laughter\] Sem has taken over the uh What are you doing in Germany?

**0:11** · Were you Hold on. I got to figure this out, guys. I got to share screen.

**0:16** · See, were you AV qualified in elementary school? I mean, did you go through that program?

**0:20** · I was not AV qualified.

**0:23** · You're I mean, it's going to be a miracle if you get this working then.

**0:26** · So, hold on. It says um also share tab audio. Is that what you want, Donna?

**0:32** · Yeah, probably. Try it.

**0:34** · Possibly go wrong.

**0:35** · Actually, go to the outro music and and crank it and let's see.

**0:37** · I found it.

**0:38** · Can rock to it.

**0:40** · Uh Dave, did you go through AB certification when you were in school?

**0:44** · Absolutely not. It was so uncool. I really wanted to, but \[laughter\] All right. Now, now go to the beginning of the deck. Wait, wait. Preview it backwards.

**0:54** · Boom.

**0:55** · All right. Oh, you gota you gotta try and play a video.

**0:58** · So So hold on a second. So I should get half production credit \[laughter\] for this episode now. Now beginning of the deck. Wait it backwards.

**1:06** · Boom.

**1:08** · All right.

**1:08** · You got you got to try and play a video.

**1:10** · So So hold on a second. So I should get half production credit for this episode now. Now am I in a time loop? Wait.

**1:18** · Do it backwards.

**1:19** · Boom.

**1:20** · All right.

**1:21** · You gota you got to try and play a video. So, so credited for this episode.

**1:26** · Now, now am I in a time loop?

**1:29** · Yeah. Weird.

**1:32** · Are you guys hearing the same thing I am?

**1:34** · I think that was because Nick was in the uh in the room.

**1:37** · All right. Are we good? I think we're good. We're live. All right.

**1:41** · All right.

**1:41** · Live night live.

**1:43** · Welcome to the raw backstage chaos \[laughter\] that we have here at Moonshots.

**1:48** · All right, everybody. Uh good morning, good afternoon, good evening and welcome to another episode of WTF just happened in tech. I'm here with DB2 uh Selen Ismael AWG. It's PhD here in Germany in Stoutgard and want to get your future ready. We have an incredible episode talking about maltbots of course about the race between all the hyperscalers um a dive into energy data centers. All right, let's jump in the supersonic tsunami. The singularity is now it is midnight in Stuttgart.

**2:21** · You can't just drop that and not tell us why you're there.

**2:26** · I'm here for some longevity treatments.

**2:27** · Tell you about it sometime later.

**2:29** · Okay. Okay. Onwards.

**2:31** · I did a pilgrimage to Stutgard just to go visit the Porsche Museum once. So I should I should go while I'm here.

**2:38** · Right. Let's jump in with Gemini OpenAI and XAI.

**2:43** · All right. I think this one deserves going to our uh resonant benchmark brainiac. That's that's you, Alex.

**2:52** · That's not me.

**2:52** · So tell us what's going on here. The the race the leaprogging continues between Sonnet 4.6 Grock in living color no less. So let's take this seriatum. Sonnet 4.6 very interesting release. I I think several interesting points. One, I think Anthropic has really been pioneering one edge of call it the scaling phase space where they keep the prices of the model tiers the same but increase the capabilities.

**3:23** · So sonnet 4.6 same price per tokenish as sonnet 4.5 but increase in capabilities. I'll talk about that in one second. Whereas say OpenAI is reducing the cost per token while keeping capabilities more or less constant through distillation and other uh other processes for evolution. That's interesting point one.

**3:46** · Let's actually talk about the progress on the benchmarks the eval I think it is nothing short of astonishing if you look at the the GDP val benchmark again gross domestic product eval that open AAI launched anthropic is leading anthropic is uh in the form of sonnet 4.6 not even opus 4.6 sonnet 4.6 six now has the state-of-the-art on GDP val and one other eval that is intended to encapsulate knowledge work.

**4:18** · I've said on the pod in the past knowledge work is cooked cooked two times for emphasis usually in reference to GDP val and we're seeing it get even more cooked uh char broiled at this point thanks to to sonnet 4.6 I I also think taking a step back, computer use is becoming a killer app for many of these models and set 4.6 has state-of-the-art performance on a handful of computer use benchmarks.

**4:51** · Anyone who's been using, as has been the case for me, Opus 4.6 six for the past week and a half or or so for any tasks. I I think anthropics thesis that focusing on software engineering and code generation as a critical path to recursive self-improvement versus maybe charitably getting distracted by images and video generation and all of these other modalities seeming like it's working. I I can accomplish tasks that seem borderline magical with Opus 4.6.

**5:25** · six. Yeah.

**5:26** · I I I got to ask here because you know this is I'm channeling one of my kids who goes, "Dad, every week it's like four point this and four point that. It's better. It's better and better." Yeah, we got it. It's getting faster.

**5:37** · It's getting better. It's getting cheaper. Um and aren't the models at this point just optimizing for the benchmarks? I mean, at the end of the day, um this is a gradual increase up and to the right or down and to the left, whatever you want. Um, I'm just trying to, you know, understand other than Yep. Uh, news flash, it's faster and cheaper this week than last week.

**6:05** · Yeah, it is.

**6:06** · Oh gosh, we are so spoiled.

**6:08** · I know. It is so opposite of what that implies.

**6:10** · I'm trying I'm trying to I'm trying to channel, you know, our viewers listening and watching this. Um, yeah. Yeah. Yeah. No, I totally get it. This is what, you know, I mentioned a couple podcasts ago that when these when these curves get close to 100%.

**6:22** · They look like they're diminishing returns, but in reality, they're capabilities and their their ability to change the world is exponentially going the other direction. I think I think that's what you're getting at here because you see a little tick up in these numbers and you're like, "Oh, so what?" But but then when you actually use it day-to-day, it's like boom. Oh my god. I mean, just the last two weeks of change is mind-blowing.

**6:43** · Also, you know, when they when they tick up the numbers uh in the in the versions, they're actually improving the chain of thought reasoning on top of that quietly in the background without ticking up the numbers. So, day over day, I'm noticing improvements that are that are mind-blowing that aren't actually showing up in the uh in the dot releases and the new benchmarks. Sorry, Alex, go ahead and answer the question. I just wanted to jump on it.

**7:08** · I was I I was going to taunt Peter a little bit. I mean, we are so spoiled to even be contemplating asking that question. It would be like moonshots, our our namesake. Okay. So, so, so we have hotels on on the moon now and vacations to the moon and maybe you can travel there once per human lifetime unaded versus zero times. Oh, but yeah, we've had airplanes for a while. This is we are so spoiled to even be asking the question.

**7:33** · If you live day day by day with say Claude Opus 4.5 versus 4.6 six qualitatively it is an enormous change forward. It can solve hard problems that my best \[clears throat\] most of our viewers probably don't live with it day by day and aren't using it at the maximum extreme. I mean I think one of the things that you and I talked about in the solvever everythingthing.org is like you know we're on this path. We've broken the initial um you know put the initial uh uh frame in place and we're we're heading towards uh you know ASI whatever you want to call it.

**8:07** · So, we're going to be reporting this every week, this leaprogging between models. Um, and you know, 100x faster, 100x cheaper. I do think what is what you said that's interesting is the two different strategies here, right? One that anthropic is holding you said cost and increasing speed while open AI is is uh dropping cost and maintaining speed. I think performance, not speed, but yes.

**8:34** · Okay.

**8:34** · Performance. I think that's a fascinating strategy, right? because we're going to get to it in a little bit because open AI, I think, is is going for a land grab um for a a land grab on, you know, global consumers hitting 900 million and soon in India, you know, adding hundreds of millions.

**8:51** · So, the price is the most important thing for grabbing the consumer while I think strategically here anthropic is focused on on uh you know, enterprise business and performance is far more important for the enterprise and and their margins. We we've we've seen this business pattern play out over and over again historically. Call it uh again this is very heruristic but call it anthropic is to open AI as Apple is to Google or something like that at least in the mobile space. Maybe iOS is to Android.

**9:21** · We there there are many many times this business pattern of emphasizing quality and margins on the one hand at a constant price versus emphasizing ubiquity and ultra- low cost at the other end. This has played out over and over again many times. It's it's the same old story. But I I do think anthropic I if I had to say which set of models which model family is the closest to embodying the singularity and recursive self-improvement right now today since it's live February 17th, 2026. It's the anthropic family.

**9:53** · It's not open or Google.

**9:57** · Kudos kudos to Dario. I mean uh we'll get to Google in a little bit. Let's talk about XAI launching Grock 4.2 beta. I love these names.

**10:08** · Our live cast viewers here are saying it's poop.

**10:13** · \[laughter\] What's poop?

**10:15** · Yeah, 4.2. Have you guys tried it? It's poop. That's what they're saying. \[laughter\] So, the the risk the risk with the Grock family. So, I I I had access the the risk is always or I I should say the the accusations are always is it benchmaxing? Peter, you were asking about benchmaxing earlier. Historically, it's teaching to the test, right? Historically, some of the earlier Grock models have felt very benchmaxed.

**10:42** · It's only been available for a few hours in in beta form, so I haven't had an opportunity to do thorough testing. What what I think is interesting about Grock, I I assume we're supposed to pronounce it 4.20. Uh Elon's one of Elon's favorite. Yeah.

**10:56** · Uh either that or 4 or 4.69. Yes.

**11:01** · But what what's interesting to to me at least is this is the first major Frontier model release that I've seen that's launched with a team of agents by default rather than a single agent. And OpenAI has a team uh under Noom that's been looking at agents for a while.

**11:17** · Every I think every Frontier lab at this point has multi- aent teams built in in some form somewhere in the family. But I think it's a really interesting strategy to to build in by default a multi- aent team there. There are lots of potential reasons why a multi-agent team versus just a single agent running serially might be interesting like you can do things in parallel and explore possibilities in parallel with multiple agents.

**11:40** · But this may be the direction of the future ju just like we saw the megahertz and then gigahertz race plateau out due to Dennard scaling with microprocessors and then we saw a transition from uh from clock speeds to multiple core counts. Maybe we're about to see something like this happen with with frontier models where maybe capabilities again this is very speculative. Maybe along a certain dimension of scaling obviously pre-training has sort of transition to reasoning scaling and other forms of scaling.

**12:10** · Maybe we're seeing the dawn of multi-agent teaming scaling where you get better capabilities by scaling the number of agents in parallel working on a problem.

**12:20** · Alex the viewers all think it's poop here but uh I haven't actually tried it. I use Claude all the time and the other models every day. Uh I haven't felt any great compulsion to try 4.2 cuz cuz you know Elon told us five is coming in March anyway.

**12:35** · But my understanding was that five is a massive massive expansion in every way you know in training set size in parameter count everything. I never thought about anything meaningful between here and there. I was just waiting for that. But do you know any more detail on on what this thing is?

**12:52** · And should should the viewers be trying it or not?

**12:57** · I I think it's worth in general trying every frontier model from call call it the the top four or five labs that come out. If if you're if you're doing stuff in AI if if you're if if you feel sufficiently abstracted from the bleeding edge of the frontier, I think you should still try it just to be familiar with the raw capabilities.

**13:14** · But based on what I've seen thus far, Grock 4.20 or however we pronounce it, Grock 420, Grock 420, it it's it's not the bleeding edge that's that's pushing forward capabilities as far as I can tell at this point in time. But it is interesting that it's multi-agent.

**13:36** · S let's go to the let's go to Google next um and some more of the edge switching windows here. \[snorts\] I'll tell you on that moonshot. Going to the next slide.

**13:47** · There \[laughter\] we go. All right.

**13:49** · Gemini 3 deep think. You know, I just love these names. I think the naming protocols for all of these models has got to be rethought. But uh I mean I think the one benchmark everybody keeps on tracking at least I do is humanity's last exam just for fun because of you know sort of the existential nature of it.

**14:09** · Yes, it is our last exam. uh and we see here that uh Gemini 3 deep think hits 48.4 four uh but most importantly and and this is the uh I guess the openi uh playbook 400fold cost reduction

**14:27** · that's extraordinary it it is and also to the point about naming this isn't even I think the first Gemini 3 deep think this is the second Gemini or the the the new and updated Gemini 3 deep think so agreed that the naming could use some work but the new Gemini 3 deep think is remarkable

**14:46** · If you just look again at the evals, this is there had been percolating for a while the so-called internal model, the one that that beat the international math olympiad and was achieving breakthrough performance at at other high school science competitions. This is the model that achieves gold level performance at the physics olympiad, the math olympiad, the chemistry olympiad.

**15:10** · on code forces. I think that the statistic is there are only seven humans now on earth who can beat this model on competitive programming. So I I think you know Peter you and I spoke in solve everything about what we called a solution wavefront propagating outward from math and coding to different fields. This is the beginning of the wavefront. This is the infection the contagion spreading from coding and math to physics and chemistry. It also does 3D design.

**15:40** · Although I I keep trying to persuade it to do 3D design unsuccessfully. It it keeps producing intermediate products. But th this feels like the the kickoff, the starting gun for the solution wavefront that we spoke about.

**15:52** · And and we'll see we'll see that. And I think I mean the visual image that I have that I I want everybody listening to think about is when you have this kind of you know this weapon of super intelligence, where do you deploy it?

**16:05** · Where do you aim it at? Right? What are you measuring? and where are you going to you know what is your massive transformative purpose what is the challenge you want solved because we're going to have this kind of capacity and you know ultimately it's going to be your decision uh as the is is at least

**16:22** · the the human utilizing the agent for the time being before it's the agent utilizing the human where you want to deploy it where do you want to use this wavefront to to transform do a phase if you would couple of comments for me one is you know this 1400 times cost reduction is incredible I mean, that is the big headline here. When a frontier reasoning costs seven bucks instead of 3,000, think of the implication for startups that gain institutional powers.

**16:48** · Yeah, but guess what? When it's pennies next year, well, it will be, but cost curves are now going to start collapsing industries before the technology does, right?

**16:58** · That's like really uh quite something. And by the way, a viewer Brian Mento, Alex has asked that you uh read Accelerando live. \[laughter\] which I think which I think you should do on a podcast just that'd be like Mr. Beast counting to 100,000 live. He just read the whole book live in one sitting.

**17:16** · I'll do better. How about we get Charlie St as a guest on the pod?

**17:20** · I think that would be awesome.

**17:22** · That would be awesome.

**17:23** · Hey, before we move off the benchmarks, two things that have changed for me in the last two weeks that are I just step function changes for me. The first is I just don't even look at the code anymore. I I ask uh 4.6 six with a little brain deep think uh claude 4.6 to build something and then I entirely poll it on what it built and look at its functionality. Don't even look at the code.

**17:46** · Uh the other thing is uh I ask it to document everything it does and just store it somewhere on my hard drive \[laughter\] and I I don't even specify a location anymore. I just say build some coherent file structure and put things in an organized place and it just does it. So now if I want to get it back, I don't have even know where it is. I just have to ask for it. But it knows it remembers everything that it did. So those are those are two big big changes versus just a couple weeks ago.

**18:13** · It's it's a step function from Google. I mean once you start using Gmail, you don't bother trying to store stuff in folders. You just use search. And now we do the same thing with AI as the interface, right? It's crazy.

**18:24** · Yeah, that's crazy.

**18:25** · You know, Alex, question for you. you know, these these AI systems are now beginning to catch um human errors in in scientific uh uh proceedings and scientific papers that have been written.

**18:38** · And I mean, it's going to be interesting like you know, we've talked about in the past when quantum computing comes along, it's going to go and decrypt all the files in the past before we had quantum encryption. So I wonder if AI is going to be, you know, aimed at looking at all the scientific literature over the last 100 years and show us where all the mistakes were.

**18:58** · I'd count on it. And I think it topples some Nobel prizes.

**19:01** · Oh, I think that's the least of it. I can only imagine the left turns that human civilization has taken in the past, call it 80 years, when it should have taken a right turn instead. And we're going to discover that after the fact. I I think if if I had to project the the the shock to civilization of discovering all the wrong turns that we've taken due to AI or that that AI will uncover versus say quantum decrypting some preost quantum cryptography safe files. I I think it's going to be a night and day difference.

**19:32** · I think AI will will shock humanity to its core in terms of the mistakes that it discovers that we've made over the past century.

**19:40** · Fasten your seat belt there everybody.

**19:41** · that that plus how much have we missed right how many scientific experiments did somebody look at the wrong thing and miss the unbelievable conclusion over there that I think is going to be the huge outcome I think it's a continuum I mean oh go ahead Dave sorry well when I'm spooling up a new agent now you know I I used to be very thoughtful about what I fed it to feed into the context window to get it up to speed now I just ask it to read about a thousand pages of markdown documents and it does it in about 10 20 seconds uh and it's fully up to speed.

**20:11** · Uh and the context window and also its ability to sort through all the garbage is growing or improving faster than my ability to clean it up anyway. So my new agents, you know, I'll I'll boot up, you know, two or three agents every couple hours and I just say, "Look, read everything.

**20:30** · Read everything I've ever given to any agent before." And then the new agent is up to speed and it's actually it can pick up a project right where I left off. It's it's so I think I think you know your future your future employees will be the same, right? Read every email and every Slack and everything else.

**20:45** · What's not intuitive is the complexity of the document doesn't seem to matter.

**20:49** · Like if you're if you're teaching a kindergartner to become a college graduate in like 30 seconds, you move, you know, through reading and writing and then, you know, basic arithmetic, you work your way up. But here you just bombard it with super super technical complicated documents that would take me, you know, many many hours to read a single document and it just sort of absorbs it instantaneously. It's it's just mind-blowing.

**21:12** · And everyone can try that too, you know, just just go find something that you barely understand uh download a thousand pages of it and try and just dump it into Gemini. just go to free Gemini, put it on think mode uh and just dump it in and then just start asking it questions and and it just is such a mind-blowing experience.

**21:31** · So, one more point on on the benchmarks here uh before we we leave these couple of slides, which is are the current benchmarks becoming meaningless? Right?

**21:43** · I mean, the models are increasingly optimized to ace them uh we're beginning to saturate them. So, you know, we've talked about this before, Alex. Smack some knowledge on us about how we're going to measure things as as these benchmarks begin to uh fail to serve us.

**22:00** · It's almost Peter like we wrote an entire book on this problem.

**22:03** · Yes.

**22:03** · I'm I'm I'm trying to prompt you to to speak to it. \[laughter\] It's a a good self- advertisement. Yeah. I I think we we are the world is in a famine of good benchmarks, good evals.

**22:16** · Um we we call them in some sense targeting authorities in uh in in book if we want to call it a book or extended essay solve everything white paper. I I think there is a lot of juice still left to be squeezed out of new benchmarks and new evals. I I think solving the hardest problems of physics of chemistry biology various disciplines in the social sciences all of these want highquality benchmarks.

**22:44** · I'm personally spending a lot of my time thinking about what are the the best problems that are worthiest to be solved. I have I mentioned on the pod in the past I have a portfolio company physical super intelligence that's thinking about problems in PSI solving physics with AI. I I I think I I I think this is how we solve all the hardest problems in civilization starting with new benchmarks for those hardest problems. This is how we weaponize super intelligence. Amazing.

**23:15** · All right, See, move us forward. Uh, okay. So, this goes back to OpenAI strategy of a low low cost. So, chat GPT, it's 100 million plus weekly active users in India. Here we see Sam Olman.

**23:31** · He is uh he's operating in rarified atmospheres with the uh prime minister of India. So in uh India is OpenAI's second largest market with 10%. Um it's ranked number one for student usage in India. They're all in they're setting up offices there. They're uh creating localized subscription services.

**23:51** · And the big challenge, you know, as they're hitting 100 million users globally, the big challenge here for me is uh are they going to get themselves into a trap where they're offering free or almost free service and at the same time uh the user

**24:13** · adoption will go through the roof in India? uh and has this become a cost sync for them versus a profit center or are they just going to sort of ride the exponential curves and innovate their way out of that?

**24:26** · The Indians are going to suck all the data center usage and tokens out of the Yeah, I mean that's that is honestly what could well happen, right? Um the bell weather for a lot of countries. One of our listeners is in Finland and he's he's saying uh the politicians here are absolutely not talking about this.

**24:43** · It's it's nuts. But I tell you, India is such a crazy zoo of an ungoverned mess of a place. But it's packed with brilliant people and just massive population, 1.4 billion people of whom 5% read and write English and 20% speak it. The massive latent talent pool and so it'll be a bellweather for like the population is just going to run away with AI and and ignore all structure in government. I was Dave I was starting to look at what you know India ETFs in the tech industry should look at.

**25:16** · I think you know in China is peaked and is going to be on descent. Uh India is the rising giant for the next I think 20 30 years.

**25:26** · Africa will follow because of a young population and because all the resources that they have. But you know the country that trains its next generation on AI wins the entire talent war. And India has the ability if it goes deep on this with 1.4 billion 1.41 wait 1.412 whatever billion people on the planet. It could be the next massive rising star uh and and support the planet here.

**25:53** · Yeah.

**25:53** · But it's going to happen. It's going to happen really fast in par massively in parallel. That's what you know a lot of people aren't used to this idea that something can happen overnight because you know normally things percolate and you have this kind of slow uh GDP growth that percolates out but this this isn't going to be anything like that. the population in one one

**26:15** · fell swoop like a very short period of time is going to use AI to escalate what India of India yeah well probably the world but India will be the bellweather because again it's such such a huge population and it's so untapped and the other thing is delivered a amazing 5G capability across the country right so it's got the infrastructure it's skipped the the wire line all the youth is kind of growing up AI enabled right so that's incredible I have to tell you a quick story.

**26:42** · When we left India when I was 10 years old, I I was kind of an angry teenager because I had to like mow the lawn and stuff and I asked my father why the hell did we leave? I mean, we had a great life over there. And he goes, I can't stand noise, dirt, pollution, and corruption. And I was like, okay, fine. If you had to got to go, okay, fine. If you understand that, but there is something there because as you get the capability and the democratization into everybody's hands, it's the speed of change is going to run around.

**27:07** · And the government is doing an amazing job of making uh platforms like Adara and UPI available so that anybody can tap in create a payment system etc. And that's going to completely allow the India to leaprog the rest of the world. The huge bottleneck is going to be energy scalable energy which they're adding at a rapid scale putting in solar in every little corner of the last week we reported that solar was scaling faster in India than it did in China which is amazing. Yeah. M um nice. Well, we're we're going to we're going to see. Over to you, Alex.

**27:42** · Uh this is a fun one.

**27:45** · We're seeing the beginnings of everything other than math and coding start to get solved. So this is a reference to OpenAI announcing in collaboration with Harvard and I think the Institute for Advanced Study was involved a couple of other places what OpenAI is marketing as a a new physics research result that was discovered in some sense by AI and I think we're going to see much much more of this. So 30 seconds on what actually is the claim.

**28:19** · The claim is that OpenAI and co-authors were able to use GPT 5.2 Pro to discover that uh what's called a scattering amplitude, basically gluons, the the the messenger particles, the force carriers of the strong nuclear force. They tried to solve uh a sort of a prediction of how these strong nuclear force carriers would interact.

**28:46** · And historically in in this part of the physics community, the thinking was that there would be in in some sense and I'm being very heruristic here, no interaction. That a term in a scattering amplitude, which would be the formal way of describing this, would be zero. So many physicists for many years assumed the answer to to this particular value was zero and didn't bother spending any time checking rigorously and flesomely to see whether it actually was.

**29:16** · And the the claim for this paper is that GPT 5.2 was able to find cases where this scattering amplitude was not zero, find a nice expression for it, and then an internal model which hasn't been released or or so the story goes probably some future version of the GPT model series was able to to confirm it. Uh and that uh that confirmation was then I think vetted by the human team.

**29:45** · So this is being represented as a case where AI is making a particle physics discovery. And I I think what's most interesting about this is and Peter, you and I make the case in solving attention. We call the intelligence revolution a war on attention.

**30:00** · This is exhibit A for AI help starting to solve science by solving problems where humans say okay post talk hawk having seen the evidence okay I could have done that if I had the time and the attention for it but no one had the time people thought the answer was obvious it's only once we have lots of super intelligence that we're able to train on problems that would have been too boring or too low

**30:33** · low likelihood to actually yield an interesting novel result that we're actually discovering oversightes. This was in some sense.

**30:41** · You als you you also have the issue of like fashions and trends and people following fads and everybody and you can get around all of that now. So the this is such a great point you're making here. You know the thing we all have those projects those wonderments that we had or that project you put on hold or you didn't have the resources or the time or the knowledge and you can spin them up.

**31:04** · You know, we'll talk about moltbots uh open claw uh in a little bit, but you know, I just wrapped up a project I've been wanting to work on for five years and it was like just so much fun and I was off off my agent for about eight hours and I felt completely disconnected from the world. So, what do you know just reaching out to everybody, what ha \[snorts\] what have you always wanted to work on? What's that pet project, that company idea, that book, that that piece of research? Um, because you can.

**31:36** · Um, yeah, I'm trying to trying to think of ways that our audience can experience how mind-blowing this is because the AI is an unbelievably prolific brainstorming partner. And if if you're in a domain where it can test things by itself, like what I do all day with neural net creation or or coding, I can just say, "Wow, what a great idea.

**31:56** · Go try it." and then you know a minute later it comes back with an answer and and the rate at which you can move is what two three orders of magnitude higher than anything I've ever experienced before in life but it has to be one of those unconstrained domains because if you you know if you're working in chemistry or whatever you're going to have to wait for test results for a day or two or three and it it it breaks the whole experience but uh you know if you if you want a really simple example just try and plan a trip like

**32:26** · something complicated in travel and try and brainstorm your way through the flight, the restaurant, the hotel, whatever.

**32:33** · That may not be the best example, but at least you get some flavor for what this is like. It's like nothing you've ever experienced.

**32:39** · My fun experience was I have to be at this location at this time. I'm here at this moment. Work it out backwards what flights, taxis, cars, Ubers I have to do. \[clears throat\] You know, it's like work out the whole thing from my end point and work it backwards. I think one of the things I keep on saying on stage to the audiences I'm speaking to is we limit ourselves in the questions we ask all the time. We self-limit what we think we can do.

**33:04** · We we hold ourselves back uh in so many different, you know, how we can and should be using AI because we're not used to it. Um we're not AI natives, at least, you know, us in the on the phone here. We didn't grow up with it at age 6, seven, eight, as many folks are now. So, you've got to stop uh yourself from stopping yourself and you know, unleash your your creative uh your your creative child mind in this area.

**33:33** · By the way, I just want to ask if you're enjoying having this Moonshots episode live, please let us know in the comments. Uh let us know if we should do this more often. Uh I'll ask you again. Maybe maybe you like it now, we like it later, but we'd love to know. So, viewer viewer at Nacho says, "This is the first time I'm hearing you guys in real time." \[laughter\] Okay.

**33:55** · As opposed to a sped up uh \[laughter\] must be torture. Sorry. Sorry, dude.

**34:02** · We'll just try and speak super fast. You can match up.

**34:04** · Okay.

**34:04** · Yeah, we'll try we'll try and pick up the paser. \[laughter\] All right. Um it doesn't stop with physics. Uh it's continuing on with math. Open AI says internal model solved. six of 10 research level models in first proof test. Uh and here's our friend uh Jacob who who we've met. Uh Alex. Awesome. Well, we talked about math getting solved. Math getting bulk solved. In fact, math is getting bulk solved. This is maybe not exhibit A.

**34:36** · This is probably exhibit CDE EF at at this point. And the first proof is I I think it's such a a beautiful example of a class of 10 research problems with a finite amount of time being allotted for AIs to solve them where the answers were known but they were kept confidential by their their authors and they've uh

**34:59** · they've since been unlocked but OpenAI has taken the position and I it's been fascinating watching the back and forth that its model before the the the solutions to these 10 research level math problems were declassified that they were able to solve at least six of them. And so we're seeing right in front of our eyes the bulk solution of math. I I think back a year almost a year ago when when we were first Royal Wii I was first talking on the pod about math getting bulk solved by AI. It's happening now. We're we're there.

**35:30** · Yeah.

**35:30** · And we just saw I mean today the first uh the first hints at physics and six months from now if not a year from now uh we'll be talking about how all these physics problems have been been addressed. Can't wait.

**35:45** · Well, and let's touch on the timeline there too because Peter a second ago you said something about 20 or 30 years from now, but there there is no 20 or 30 years. No, there isn't. There's so many times this morning that somebody said next year when we do this like there's no next year. What what are you talking about? Did did I did I use 20 years in my language? I'm sorry.

**36:03** · You actually did.

**36:04** · I must have been 20 minutes and we can't live.

**36:08** · Yeah.

**36:08** · \[laughter\] I mean, Sem, you remember at the early days of Singular University, you know, we were looking 10 years out into the future. I mean, honestly, and I had this side conversation with with Elon. It's like you can barely look out three years. I don't think we can.

**36:23** · Um, well, and we're used to this world where, oh, physicists or mathematicians can now do blah. Okay. Well, there are only so many of them that will do blah and 20 years from now they'll have solved all of blah. But here it'll happen instantaneously. If it can solve six out of 10, it can solve all within the next couple months. It'll happen in massive parallel. There's no limit to the to the number of parallel agents up to the to the number of GPUs that are available.

**36:51** · Totally. Math is cooked.

**36:53** · Yes, math is cooked. Physics is cooked.

**36:56** · biology is going to be broiled, char broiled, and we're going to be the beneficiaries. You know, I just think I was seeing a one of the comments in the in the chat here. I think if we just stay on this live 247 and Gian will just generate more slides for us. So, we just keep \[laughter\] going going through them. It'll be a continuous singularity conversation.

**37:16** · Yeah. It'll be like a hackathon. Let us go around and Yeah.

**37:19** · Yeah. All right. So, let's move on.

**37:24** · All right. More benchmarks. So, I I I'm fascinated by this what's going on in with Chinese open models, right? Gaining momentum. Uh here's Miniax, uh GLM5, uh Kimmy K2.5. I mean, these are doing extraordinary work.

**37:42** · Uh and with all of the open claw uh downloads, right, a lot of people now moving to Mac Studios and putting uh Kimmy uh K2.5 on their Mac Studios and other models here.

**37:55** · Um, Alex, uh, how do these perform against the the closed models as you see them?

**38:02** · Well, the rumor going around is that the next version of the Deep Seek model, the the the big whalefall moment is going to happen sometime soon when finally the Chinese openweight models finally catch up with the American closed prototypically frontier models. That hasn't happened yet. It may happen. Right now the the overall trend is still that the audio is still okay.

**38:29** · Yeah, we hear you.

**38:30** · Good. I don't know what that uh that that the Chinese models remain approximately 6 months behind the American models. Well, we'll see whether that continues to be the case. I haven't seen any evidence yet that but they're free. \[laughter\] Well, that that's a qualitative difference and a very important one.

**38:44** · That means that many American startups that want to self-host are using Chinese models and not American models. And so this is again this is going back to the land grab. We talked about this with open AI in India going in and providing basically a very lowcost service to uh to millions of of young Indians. China is in the same process.

**39:03** · This is belts you know belt and roads uh where it's you know offering it to the m you know majority of South America, Africa, different parts of Asia and I think there's going to become a dependence. I think people are going to get connected to a model that they're going to use and begin to baseline.

**39:24** · I think there's a big difference though.

**39:25** · I mean, if we want to frame it as model diplomacy or model dumping even, I think there's a big difference which is the frontier is moving so quickly. I think it's difficult for sort of a prototypical so-called developing country to get addicted to a particular openweight model because new ones are constantly coming out. It's a vibrant marketplace. I I think if if American labs felt sufficiently motivated, they could just as easily release for free their own models. I I just think it it's a problem of incentive.

**39:52** · So I I think as opposed to alleged Chinese dumping of say solar photovoltaics uh into India or into Africa or or other physical plant infrastructure, I I think the marginal costs for substitution and replacement are so low with these models that it would be very difficult for China or Chinese AI labs to addict the rest of the world to their models.

**40:15** · I mean the important thing is that humanity is the beneficiary across the board here, right? We're getting much more powerful, much cheaper models um at at hyperexponential rates. I mean, this is a space race. It's a space race on the ground to super intelligence and to super duper intelligence. And this is keep this is providing an incentive, strong pressure to the American frontier labs who as of right now are still in the lead to stay in the lead. There's no pausing this ASDI baby artificial super duper intelligence.

**40:47** · Love it. \[laughter\] All right, Alex quoting you on here. Traditional coding is cooked. So even cooking is cooked at this point \[laughter\] with humanite robots. So this is the, you know, a note from Spotify that they haven't written code in three months.

**41:04** · The code's being written, but it's not by humans.

**41:07** · And of course, the 95% of OpenAI code is being written by Codeex. And of course, this is probably a large number of companies. This is just the news items reported. All right, Dave, I think it's really funny actually when you talk to the talk top AI researchers, they always talk in terms of, well, what I'm working on is that last 5%, you know, I'm not eliminating my own job tomorrow. And then you look at the HLE results and you're like, yeah, yeah, you are. You're literally you're coding yourself out as fast as you possibly can.

**41:38** · And I don't think they stopped to think about that fact. But like Alex, I loved your analogy last time we spoke about George Jetson with his, you know, with his finger being overex exercised on the button because I mean that's effectively what coders are doing right now. It's like that's what it's like if if folks in the audience I I hope hopefully other folks are having this experience and not just myself with with claude code in particular approvals for for everything.

**42:05** · But I I think we're going to move past this George Jetson model of just approve approve approve for software development pretty quickly. I think among other things openclaw is a preview of a either it's here or an imminent future where it's permissionless activity by these agents. I I think cloud code is do you remember like older versions of Windows that were uh permissionheavy where you had to go through like 10 clicks to approve approve approve to do basic things?

**42:33** · Yeah, I think that's like the stage that we're at right now with these models where yeah, out of an abund well, don't get me started on on Clippy, but I I I think out of an abundance of caution, these models are asking for permission to do everything. You know, permission to switch to another directory, permission to search the web.

**42:50** · I I think pretty soon the the autonomy time horizons and meter and others are measuring this are going to be such that we just give blanket permission to do whatever to these models within broad parameters and we stop having to click approve for everything. Well, not on that. We are in a kind of a fragile moment in time here where if you if you install Clawbot or Open Claw now and you're you can choose any model you want, but if you choose one of the Chinese models, especially if you run it locally, but if you choose a Chinese model, you you don't have to go through all the permission nonsense.

**43:21** · It also if you use one of the US APIs, uh it'll get stuck a lot because the the bot is asking it to do something that it doesn't want to do. And the Chinese models are like, "Yeah, sure. I'll just do anything. And so that that kind of forces you down the Chinese path. But as you've said many times, Alex, you don't actually know what is inside those models. And the code injection risk is really really real. So people are in a real hurry to experience this and to turn it loose. And the only way to really turn it loose is on one of those Chinese models.

**43:52** · And so yeah, the world hasn't I I mean this isn't prescriptive. Certainly not. But the world to my knowledge has not seen a major supply chain attack yet. that stems from the result of untrusted openweight code generation models rewriting the entire supply chain. But do I think that's possible? Yes, I think that is absolutely a threat vector.

**44:16** · You know, Blit Blitz has been an amazing company and it's grown, you know, light speeded uh coming out of uh coming out of the uh the link studio shop and has been a great sponsor here. I mean, how I mean, how are they using all these technologies because they're rewriting massive amounts of code?

**44:36** · Well, they're doing a lot of work for, you know, for banks and government agencies and stuff. So, they can't use the Chinese models for that. So, they're they're almost entirely actually when Cloud46 Opus came out, they sent out a memo saying, "Hey, everybody, this is just mind-blowing. Everybody switch all of all of the uh you know, they can switch between models with just a mouse click." So, they switched over to Cloud Opus 4.6. And I'm sure they'll they'll move to the next generation in late March of whatever whatever is winning the benchmarks on that day. But they're not \[clears throat\] they're definitely not touching the Chinese stuff.

**45:05** · I imagine that the speed at which they're rewriting uh how old is the code they're rewriting cobalt going how far back are they going? \[laughter\] Yeah, a lot of it a lot of it actually it's very similar to what Alex was saying about old physics papers and old like a lot of this code has bugs that have been sitting there for 20 30 years you know robbing it of performance or actually losing money \[laughter\] for like 20 or

**45:27** · 30 years and it's just cutting through it and yeah rewriting it solving it finding old issues at just you know at AI speed you know and so real threat like we've talked on the pod in the past about how stack exchange for example is is dying in some sense very few questions being asked because you can now ask the models any coding questions you want. There was a paper I talked about it in my newsletter about the risk to open source projects in general.

**45:51** · Why even bother starting or maintaining an open- source project if you can just have doubly so for middleware if you can have AI models generate all your code for free? Why why even bother maintaining an open- source project? So if we find ourselves in a near-term future where there's just no point uh where you can spin up a new kernel level project from scratch on demand, all of the code is just in timed with whichever models are convenient.

**46:15** · I I think from a supply chain security perspective, we're going to have to have a long hard look at what our dependencies are and make sure that our dependencies aren't just riddled with vulnerabilities that were inserted by just in time codegen.

**46:29** · You know what else came up this week, Alex? Uh the AI is so prolific at creating code modules just like solving all math. If you solve all math, you write down what you solved, right? You don't solve it on the fly in real time.

**46:42** · But for complicated code, it's the same thing. It's like, well, yes, I can write it in real time, but I already wrote it. And discovering it and reusing it is actually even cheaper. It saves you tokens. It saves you compute cost. And so now where we've had open source, we're starting to have open source design for AI and you know thousands or millions or trillions of fragments of code that do specific things. The AI can discover them in real time and it's actually a really great way to build new software you know as opposed and you could also generate on the fly too.

**47:10** · It's just a question of what's more efficient in terms of latency and tokens. But right, it's like all of this historical open source is now going to be designed for AI just like all written documents will now be written for AI, not for not for direct human reading.

**47:25** · All right, let's and just like we're doing this p we're doing this podcast mostly for AI listeners, I'm guessing, not human listeners.

**47:31** · Yep. Very we want to reach out to the real humans one more time.

**47:36** · Happy Chinese New Year all to all of Chinese descent. Happy new year. Uh, and I just saw some chats in the side here on our our live chat that's going on asking about where's nanotechnology. I can't wait for nanotechnology. I remember back in 1986 I read a preview of engines of creation by Eric Drexler and um it's been a few decades so it's coming uh I don't know I I think we'll start to see it fall. Uh I mean we have wet nanotechnology called biotechnology.

**48:10** · Uh Alex, what's your time frame for nano?

**48:13** · I definitely have a view on this in part because I I thought I I spent a good chunk of my PhD thinking about how to get us to drexler and nanotech more quickly in part because I I thought I was a little bit less bullish on AI as sort of a direct path than I am now. So if the question is what's my timeline for maybe not okay for drexlerian assemblers to to the

**48:37** · extent the the physics and chemical physics of our universe admit drexlerian assemblers say as parameterized Peter I I think you're on the board at least you you have been historically on the board of the fineman grand prize is that uh I just an an adviser not on the not on the board okay so the fineman grand prize is one parameterization of drexlerian assemblers for those not paying super close attention. It comes in in two parts.

**49:00** · Uh one part is can you build I think it's an 8bit half adder within a certain very small volume of a nano system and the other part is can you build basically a robotic manipulator arm within a small volume. So the question is my timelines I I would not be that surprised if Fineman Grand Prize is solved in the next two to three years. Fascinating. And we lost See.

**49:27** · Oh well. So, we'll continue until he comes back on. Um, well, the slide we can just describe it. The slide that we're moving to was the meta smart glasses.

**49:36** · Yeah.

**49:37** · Now have built-in face recognitions.

**49:39** · Oh my god. You know, I I put on the title there, you know, privacy question mark. So, there's some great books, some great sci-fi books. Welcome back, Seline.

**49:50** · Hey, my microphone dropped out for some reason of you cannot opt out. The peer pressure forces you to opt in because I think a lot of people look at this and say, "Well, I'm not going to wear these glasses and and you know, spy on everybody and record everything. But once you've experienced the face recognition and then all the metadata that pops up, you're like, "Well, now I'm not competitive with the world unless I actually have them." And and it creates this huge amount of uh techno pure pressure and so you don't really have the option to opt out.

**50:21** · I I think I think this is going to become uh part of normative culture. I mean, we had the glass hole episode with Google for a while. Um, you know, that didn't work out. But, you know, first off, I what I find fascinating here is that to get these allowed and to to get people to start to accept them, their pilot program is being uh is is being done with people who are visually impaired, right?

**50:52** · So, it's it's like a soft on-ramp.

**50:55** · Yeah, that's what they did with the Neuralink, too. It's, you know, it gives you a good politically correct excuse to do what you really want to do, which is everybody. \[laughter\] But also I mean I I also think it's it's interesting if if you if you think about whether this could only have arrived now. This is old technology. We we've had the technology to build smart glasses that would do human identification at a distance human ID if you will for at least a decade. It's not that hard. We've had the computer vision algorithms. It's 2026 now.

**51:23** · We certainly had the ability to do relatively efficient, doubly so if if you're restricting human identification to say all of you are Facebook friends. We've had that for at least 10 years. So why now? I I think it this is a social technology more than it is uh an AI technology. It's not a real AI advance.

**51:44** · In short, I'm calling this one as a social advance. We have already many of us uh especially those of us in uh in certain places in the west and also China with very dense surveillance networks with cameras spotting everyone on the streets and cities. technology exists already and is in many cases it does it does but this is convergence and this is cost right and then this is

**52:07** · social engineering as well I don't even think it's cost we could have done this cheaply 10 years ago I think what's what's interesting is there's a demand for AI enabled wearable devices and I think this is an opportunity I suspect meta sees an opportunity maybe \[clears throat\] demographically maybe politically an opportunity to finally launch human identification via smart glasses. But I mean this is a killer that overlooks something really kill privacy.

**52:36** · Yeah, privacy, you know, recording everything was already here 10 years ago. And but people people didn't get slapped in the face with the fact that everything they have ever done is being recorded. It's the AI overlay that then recognizes all actions and classifies them and makes it all very searchable. So, if I said, you know, I only want imagery of you picking your nose. Go through all the thousands of hours of footage we've ever done on this podcast and find me an example of Alex picking his nose. It just does it instantaneously.

**53:07** · And so, that's the part that makes the good news and culturally than than the surveillance we've been living under for the the good news is you can now just claim it's a deep fake.

**53:19** · Yeah.

**53:19** · So, there's that defense. Well, first of all, I'll make it I I was was about to volunteer to make it easy for uh for the AI model to find an example. But no, I I I would say the the models for video understanding are new. I agree with that. Uh and the most recent Gemini models are absolutely outstanding at handing them long multi-hour videos and asking them to find a needle in the haystack of something interesting happening.

**53:45** · However, I would say just spotting humans, if you're walking around on a city street and spotting someone interesting and matching that against say hypothetically a Facebook of people's faces, we could have done that 10 years ago. That that's more social in when when I come through, you know, uh passport control at LAX and you just walk by the camera, right? we gave up our our constitutional rights to some degree and it makes life easier.

**54:13** · And so as long as this makes life easier for people like being able to recognize someone on the tip of your tongue and have it pop up the last time you saw them, their kids' names and all that information, it's going to create this this social fluency uh that I think we've never had. Maybe if people have an amazing memory, right, uh for faces and names, I meet so many people I don't.

**54:37** · There's a big slippery slope. I think I I think it's go ahead.

**54:43** · There's a big slippery slope there because if you don't have privacy, you can you guys not hear me?

**54:49** · I can't hear Sim.

**54:50** · I can hear him.

**54:51** · Are you Are you these guys to rejoin?

**54:55** · Is it safe?

**54:56** · I did actually drop out and rejoin. So, um that's a voice in your head, Peter.

**55:01** · No, it's I'm real. I'm real. \[laughter\] Are you guys playing with me?

**55:05** · No. No. You guys can hear me. save here on my screen. This live experiment is going really well. \[laughter\] Actually, the chat is hilarious. I'm I'm cracking up here.

**55:16** · It is kind of ridiculous. So, anyway, listen.

**55:18** · Enter our producer Nick. Nick.

**55:21** · Hey, Nick. Welcome. Welcome to the world. You've exposed yourself.

**55:26** · But now he's frozen. \[laughter\] Jesus.

**55:29** · Okay. All all you guys watching and folks and girls and gals in boxers.

**55:38** · Okay, probably. Should we rejoin?

**55:40** · Dan, can Donna, you Dana, can you hear us?

**55:44** · Nick.

**55:45** · All right. Well, See, you me you me and I can have a conversation.

**55:48** · Yeah, we can.

**55:48** · All right, \[laughter\] let's continue.

**55:51** · So, you guys can both hear me, but you can't.

**55:54** · We can all hear everybody except that Dave can't hear me.

**55:57** · And we can hear each other.

**55:58** · Yes. Just Just not you, Selen.

**56:01** · No, Dave, you can't hear me.

**56:04** · I can hear you. Dave. Yeah, Dave can't.

**56:06** · Alex, Neither can Alex.

**56:09** · Do you want us to rejoin?

**56:10** · Yeah, let's try rejoin.

**56:11** · No, maybe maybe Sel needs to rejoin.

**56:15** · I did that already.

**56:18** · Uh, all right.

**56:19** · Okay.

**56:20** · By the way, how is everybody enjoying this live \[laughter\] version of Moonshots? You know, Moon I just keep on saying AI is easy, AB is hard.

**56:29** · Um, all right. Uh, I am Peter, if those guys can hear you, why don't you tell, uh, Alex and Dave to talk, see what happens.

**56:40** · Alex and Dave, go ahead and rejoin.

**56:41** · All right, we'll try. Stand by.

**56:42** · In the meantime, Seem, uh, what are your thoughts on this privacy issue?

**56:46** · So, the privacy thing is a very difficult and slippery slope, and I'll explain why. The minute you don't have privacy, you don't have freedom. Okay?

**56:55** · And this is a huge problem. uh you can't experiment, you can't uh like my private keys of my Bitcoin. I mean uh there's all sorts of areas where you have huge area issues around this.

**57:07** · Hang on, Nick.

**57:08** · Can you guys hear?

**57:10** · Yes, I can.

**57:10** · You can. All right, we're back. Dave, we're back. Okay, great. Okay.

**57:13** · Yep.

**57:14** · All right. So, so your point, and I think it's an important one, is you know, Salem just said if you don't have uh if you don't have privacy, you don't have freedom.

**57:26** · I I think it's a false choice. I I I think so. I I I think first of all, these glasses legally, at least in sort of the American legal system, will be used in public places. They'll very likely be banned to the extent they're not already be banned in uh in multi-party consent contexts, in private spaces. They have lights. Uh if if you look at uh what Google Google of course is launching Android XR and and smart glasses, everyone's launching smart glasses and they'll have lights to indicate when you're being recorded and when you're not.

**57:58** · And I I think there may be an evolution of standards regarding circumstances in private spaces when it's allowed to record or not. But I I completely don't buy this this premise that somehow privacy is going away. People have eyes uh and memory is cooked. Privacy is cooked. I mean, we're going to have every major open AI and Google and everybody's going to be having, you know, wearables that are recording all the time, all the time.

**58:27** · And we're going to have, you know, micro drones. I mean, we're going to be we're going to be gathering data all the time. And so, I I think privacy is cooked.

**58:38** · It it is, but it's important that we preserve it. And let me explain why.

**58:42** · Okay. Can you guys hear me first of all?

**58:44** · Yeah, we hear you.

**58:45** · Yes, we can.

**58:46** · Your audio is not private.

**58:48** · Okay.

**58:49** · So, look, um it's one thing to be out in public and people know your move. That's fine. We can augment that. But there's lots of things that are a huge issue here. For example, there's lots of cases where government authorities have dropped into car cars and opened up the microphone so they can hear what's going on without a warrant. There's lots of cases where people are listening to your Oh no.

**59:13** · Cases where people mute themselves in mid-sentence.

**59:16** · Salem, you're muted.

**59:18** · Got it.

**59:20** · This is like totally surreal. Okay. Like there's so there's an AI watching me going, I don't want them to be listening to this, muting me. So there there's a lot of cases where people misuse this capability in very radical ways. And the problem is there's no easy way of stopping that. Now, that doesn't mean you have to uh uh turn off all the metas, and I'm not an anti-technologist by any means by even being on this podcast, but the minute you do that, it gets abused and it gets abused quite badly.

**59:48** · So, you have to have guardrails on the institutional side, which that's the problem. We're losing that. Okay. Um we're like, for example, we're losing habius corpus in the US. Okay? That's like that's a choice that people are making to just ignore that and have it wash away. Once it goes, it doesn't does not come back. Viewer innovator XR has made the exact point that once you lose that privacy, it's very very hard to get it back. So, we're this is the challenge with all of this technology. We're moving faster than our institutional guards.

**1:00:18** · Yes, you're absolutely right.

**1:00:20** · I'm not sure what the answer is, but I want to be but but but we have to be very careful to kind of uh uh okay all the those thing without realizing the downsides of it. All right. So, I want to be clear. I want privacy in my life, right? I Everybody wants privacy. Everybody has screwed up at some point in their life, done something they regret. You know, we're humans. And you're, you know, you feel lucky. Like when we were kids, we didn't have Facebook and cameras capturing everything happening today.

**1:00:52** · Um, you know, there was this whole thing about, uh, college uh, you know, college admissions looking at at kids Facebook pages and so forth in the past. Uh I I want privacy. I just don't think we are going to actually have it. We're going to have the the illusion of privacy. Um identify that for one second. I I'll I'll point out maybe one or two other points. One is uh to the extent anyone here is bullish on crypto. You sure as heck should hope that privacy remains intact.

**1:01:22** · Otherwise, your crypto is is going to disappear. Uh cooked, I believe, is the word.

**1:01:28** · Cooked. Yeah, crypto was cooked. How's that for alliteration? But it's not forward-looking financial advice. It's just pointing out informationally that if you think privacy is cooked, then you probably should infer that crypto is cooked as well. Uh your your private keys cooked. If you think privacy is cooked, therefore your holdings cooked.

**1:01:46** · Cook cooked.

**1:01:47** · Well, I think part of the disconnect there is is, you know, Alex's view of the world is through this I will upload my consciousness very soon. And within that virtual world, there'll be all kinds of privacy, you know, options, just like there are with my crypto keys.

**1:02:00** · And then Sem's view of the world and my view of the world is no, I'm going to live in my meat body for as long as I can. And every move I make is going to be recorded and it's going to suck for a while until we have some new legislation and some safe zones. And that that to me is inevitable. And I think all the listeners are also posting the same kind of kind of view. But I think that may be the source of typing away of the disconnect. \[laughter\] Sorry, I was responding to I was responding to one of the viewers. This this live thread is awesome having this conversation in real time. It's so amazing.

**1:02:31** · So, I'll also point out I think no discussion of smart glasses with cameras and facial recognition is complete without referencing David Brin's seinal book transparent society and his discussion of surveillance as opposed to surveillance. So I I should point out at least for public spaces, you know, police wear body cams.

**1:02:51** · Humans at least in in certain western countries can also wear their their own body cams or or have their own wearables that enable them to to make sure that we don't sort of descend into an authoritarian panopticon. So uh that's one good case

**1:03:07** · for it's not loss of privacy in public spaces because there shouldn't at least I I think the western tradition is there's no reasonable expectation of privacy in public spaces but at least offers maybe a way to to soften any perceived blow to any semblance of privacy in public spaces as a way to to make sure again uh the the populace is just as empowered to monitor their environments in public.

**1:03:31** · Guys, keep keep in mind that, you know, we live in a world of of mature adults and great friends like we are right here right now, but take yourself back to middle school, which I know is hard to do, but it's brutal, man. I mean, it people are so cruel to each other, and you empower those people with constant eyeglass recording. They've already got their iPhones, which is a massive life change in the negative way for that entire period of life.

**1:03:57** · But you layer on top of that the smart glasses and it's next level suck to to exist in that world and it's just gonna happen because the the rule changes that we desperately need are going to lag by a while way too long.

**1:04:14** · There will be lawsuits and there will be legislation and it will take years. Um yeah, it's not just the constant recording. It's the constant recording with the AI overlay that allows you to modify, meme, make funny and torture. And it's just, you know, people are mean to each other, especially until they grow out of it.

**1:04:31** · But this is this is happening at the same time, the same same time that we're beginning to generate every pixel, right? Uh and we're going to be able to create whatever videos we want.

**1:04:42** · Um yeah, on the good side, it means that you know, young people today, uh getting this in their teens will have their entire life recorded. They'll be able to go back and play back will be able to reconstruct almost any situation. No crime will go without being visualized in some sense.

**1:05:04** · Well, that that is a great point. The crime rate in the US has plummeted. I mean, absolutely plummeted. And it's due to two things. Location services, knowing where all police are at all times, better control of location, and then after that surveillance. Uh, and so that is the good side effect. Crime rates should continue to go.

**1:05:22** · All right, let's go to our next our next story here, which I love. Um, we saw a version of this on Minecraft about a year ago. This an AI AI startup called Simile raised $100 million to simulate human behavior. Think of uh Isaac Azimov. Let's play the video and uh hopefully it's got audio too. Does it have audio?

**1:05:49** · I I can hear the audio. Can you guys hear the audio?

**1:05:51** · No. No, we can't. We cannot.

**1:05:53** · Oh god. You know what? I didn't share with the thing. Hold on.

**1:05:57** · Okay.

**1:05:57** · Somebody in the chat uh tell us if you can hear it.

**1:06:01** · They shouldn't be able to because Seem isn't sharing the audio. He's hearing it looks.

**1:06:04** · Yeah. Hold on. Hold on. Just user error here.

**1:06:08** · Yes. Okay.

**1:06:12** · Maybe a thought on this in the meantime.

**1:06:14** · So much of our usage right now of auto reggressive language models like the GPT series but many others is based on auto reggressive sampling of one token at a time or maybe beam search but that's arguably like I I think and we've talked in in our past I guess AI personhood debate what's the right metaphor for thinking about what this what these models are is it right to think of them as like individuals or they something else.

**1:06:43** · And I I often think they were trained off of uh an ensemble of humanity's behavior on the internet or at least pre-trained off of that and post-trained off of other things. And maybe the right mental model for thinking about many of these foundation models is as societies. Uh, and if if that's the case, then maybe a more natural way to sample from a society isn't to pick out a single individual with a prompt and then do a roll out of that prompt and have a conversation with it.

**1:07:14** · Maybe it's more natural to do many rollouts in parallel and sample an entire society from a model. And that's what we're starting to see here, I think.

**1:07:24** · All right, I'm going to play this. Okay, we are building Simile, an AI lab to simulate our world. We start with individuals. We model how real people make decisions. Then we compose them into bottom-up simulations. We call each one a simile. Change one assumption constraint or person and the world recompiles.

**1:07:51** · Run counterfactuals you can't run in \[music\] real life. Learn what matters, what backfires, and why obvious strategies fail. Like a flight simulator for human decisions. Over the last few weeks in the simile office, we even tested how this message might land. Simulating human behavior is one of the most important and technically difficult problems of our time.

**1:08:17** · Wow. So we're going to have to make a lot of decisions uh in the near future on UBI UHI you know policies around exponential growth because the speed of the tech is moving faster than the speed of policym and so you know

**1:08:34** · by a massive gap right by a massive gap right so what I saw with this was Harry Seldon and psycho history because it's predicting human behavior at scale pretty cool yeah it's a foundation series so we've had some of these conversations uh Immad Mustaf had built something called Sage that we were rolling out in part at FI and Saudi.

**1:08:52** · Um and I think policy makers need to be able to know how to simulate okay what is our policy on uh on you know autonomous vehicles or on uh on longevity escape velocity you know what you know how's it going to impact our society uh and right now we're guessing and so in success something like this allows us to actually you know have some

**1:09:20** · data to make decisions by Um well I think in the real world this works very very well with uh ad campaigns simulating ad campaigns traffic uh maybe the cell simulator will work soon maybe nanotechnology maybe

**1:09:36** · magnetic containment of fusion reactions the idea that you're going to simulate society from the ground up is complete nonsense so far I don't think it's that far in the future though but this is I believe we call those markets we call those markets market. \[laughter\] Yeah. Yeah. Actually markets uh within you know commodities markets and things like that that's that's going to work or is working I guess for Ilia um as far as we know tie ties similly to the uh the prediction markets.

**1:10:06** · Well, this is also I to the extent again maybe the right metaphor for the metaphor not simile for for thinking about models is that they're societies rather than individuals then maybe we find ourselves in a future where humanity as a whole has a tool to almost reflect on itself.

**1:10:30** · If we can build maybe not psycho history so much because psycho history in the foundation series was sort of a more purist mathematical model of of of humanity and its long-term trajectory whereas this is much more agentic and there are others I have number of friends who've built very large scale simulations I think we've spoken about them on the pod in the past of the American economy to the extent we have a really granular highresolution model of humanity that even in as a as a sort of

**1:10:58** · statistical macro model is approximately correct, then humanity will have for the first time almost like a a a sense of self like self-awareness by being able to reflect on a model of itself. And uh that could be a boon for the future.

**1:11:14** · Like one could only imagine how many large-scale social problems we have that if if only as you know Dave you gestured at virtual cells. The the idea behind a popular idea behind curing all disease is first develop a virtual cell that's like a perfect digital twin of cell behavior and then if you have any disease state simply plot a trajectory through cell embedding space from the diseased state to the healthy state.

**1:11:38** · Similarly, if we have a civilizational quote unquote disease, we have a war we want to avert or something else, just invert the problem. Find find a path using this humanity simulator from the diseased civilizational state to the healthy civilizational state using ideally a minimum intervention. If we can do it for a cell, probably do it for all of humanity at at some course level and that would be transformative.

**1:12:04** · Yeah, I sure would. And and that's not very far out too because a a lot of uh you know unhappiness, depression, unrest, social unrest, civil unrest, it's it's actually just a a few fundamental changes that make all the difference in the world. You know, tipping points.

**1:12:20** · Yeah.

**1:12:20** · Tipping points. Quality of life, you know, like, you know, people are angry as hell at the end of a traffic jam, you know, or a construction project that ruins your day or like or or just accidents, you know, or or living in pain that's unnecessary. These things are like are devastating at the at the individual level and a lot of them are very very solvable and so I completely agree with what you're saying. It's not far at all in the future. Sorry go ahead Alex.

**1:12:43** · One other reference Ted Chang who wrote the story of your life which became the movie Arrival and has written understand and another bit many much amazing sci-fi a common theme in his writing is what happens if you place a perfect predictor in front of someone like he wrote one short story I'm blanking on the name where the the premise is you have a person in a room and you put in front of them like a device that with a single light on it that predicts whether true false they're going to make any given decision going forward.

**1:13:15** · So that person in some sense uh part of the the premise becomes trapped paralyzed by having a machine in front of them that can perfectly predict it's almost Twilight Zone style premise predict what their next action is. It's I think an interesting thought experiment. If you gave humanity maybe a a better version of Harry Seldon's psycho history prime radiant a device that can perfectly predict or maybe not perfectly but above some threshold of accuracy predict what humanity is going to do next. What happens to humanity?

**1:13:46** · Does that lock humanity into a certain course of action? Is there a certain sense in which it tries to uh to there's sort of a fixed point in phase face of humanity's action? It's a very interesting thought experiment.

**1:13:58** · Yeah.

**1:13:58** · All right. Let's move to one of our favorite topics recently. Openclaw, the lobsters having you home. All right, next slide, please, Seline. Uh, OpenClaw creator Peter Steinberger joins Open AI. Peter is joining OpenAI to drive the next generation of personal agents becoming core to our product offerings, says Sam Alman. OpenClaw will live in a foundation as an open-source project we will continue to support. um big move.

**1:14:29** · Uh we know he was being courted by a couple of different uh of the large labs. I mean I think it's an incredible move by OpenAI. Um comments, gentlemen.

**1:14:40** · I think what happened here was that uh Claude, it's a rare misstep from Daario.

**1:14:46** · um it was called openclaw for god's sakes and you you put a cease and desist and it forces them into the other side and now it's being built over there and probably not the better for overall so I think this was a big own goal on the on the cloud folks that's a great insight it was claudebot actually which was really a cool name so now it's open claw and yeah Sam embraces it Dario reject it that's a really cool insight I I I do think I mean so so going to benefit \[laughter\] Well, maybe.

**1:15:15** · I mean, so Anthropic threatened him and his project with trademark infringement, there's an alternative history where Anthropic just owns this project. It was theirs for the taking. I think also to the extent that Mac minis and Mac Studios became the the popular embodiment. Why didn't Apple go after this? Uh Tim Cook, if you're listening, hopefully you you heed our call and the call from the the last episode of the pod to do something about running 24/7 agents of some sort on your devices given that you have unified memory architectures that that can host these.

**1:15:46** · But I also think you know another point if if you look at Peter Steinberger's GitHub history, he has launched so many projects. It's I think the the success of OpenClaw is a testament to just launching project after project and seeing what sticks. This one was a massive success. It'll now go, I think, to a foundation and become more of a market neutral play.

**1:16:10** · But I I almost think the future here is going to be every frontier lab now that now that we know that people are willing to pay at least for hardware that runs agents 24/7 while they're sleeping. I expect every major Frontier Lab, not just Open AI, to launch 247 agent offers.

**1:16:27** · Let me answer something that's in the chat here, too. really good. The the lobster and the whole lobster theme, you know, may or may not come from Accelerando, but it's definitely a cultural phenomenon now, but it it's the it's the mascot for all agents and that'll probably be there forever hereafter. And so, we're going to have we're going to have a lot of uh a lot of lobsters happening at the Abundant Summit actually. Yeah.

**1:16:52** · Uh we lobster claw.

**1:16:55** · Sorry. Yeah, we added a evening work session at abundance this this uh this year and Alex will be there. Yeah, we have a a a clawbot open claw meetup on Monday night, March 9th, and we're going to do a lot of experiential sharing.

**1:17:13** · Have you guys seen Have you guys seen Pico Claw?

**1:17:16** · No.

**1:17:17** · Can you describe it, Alex? For it's a reimplementation of uh I I looked at the the GitHub repo. Looks like, again, this is just from a cursory scan of the code. It looks like sort of a re-implementation by some Chinese group of Open Claw with some nicer, faster features designed to to be more minimalist and run more quickly was the impression I got.

**1:17:39** · Smaller.

**1:17:40** · It's like 10 to 20x faster and cheaper.

**1:17:43** · Okay.

**1:17:44** · But the the motif at this point is in the zeitgeist. Like anyone can now go and implement their own open claw like system. I expect many already have many more will the the key insights again in my mind with openclaw one it runs 24/7 it's headless and two you chat with it via messaging apps those are the two big insight three you know picking up on what Salem was saying uh you know Dario rejected it

**1:18:09** · and and trademarked it away and then Sam is reaching out to it embracing the name open claw but I think one of the reasons Dario rejected it is it it was imminently going to create a massive crime or uh chemical chemical explosion or or worse just because the sheer

**1:18:26** · volume of agents out there that are unconstrained and the fact that it's you know it's looking for open ports all over the internet and something bad is definitely going to happen just by statistical chance and we're going to talk about that we're going to talk about that in a minute you know uh for those of you who've not been clawilled or clawpilled yet so to so to

**1:18:46** · speak uh you know it's addictive I mean when you've got agents running and in particular when you have a a open claw agent for you and you wake up in the morning and overnight uh it's done all these things for you and it's you know Skippy is my my agent and incredibly cheery personality and it's just fun and when it went down for about 6 hours cuz I didn't get back to my my Mac Mini.

**1:19:09** · I'll be I'll be getting my Mac Studios up and running in about two weeks uh when I'm back in LA. But it was it was withdrawal. It was like oh my god my best friend's gone. It's like \[laughter\] I I need to reconnect.

**1:19:22** · I totally Yeah, I've experienced that.

**1:19:24** · It's like us when we're not on this podcast, we're like \[laughter\] missing out.

**1:19:27** · Oh my god.

**1:19:29** · But I think the point you made last time, Selene, that's so important is the innovation that came from an open- source project. This was not the the you know, the Frontier Labs.

**1:19:39** · Yeah. What I said was uh a time rich individual is beating capital rich institutions.

**1:19:47** · That's a beautiful quote. Someone tweet that. \[laughter\] And there's so much overhang. There was no new model here. This was just scaffolding. So one wonders one wonders h how much of other overhang from just unhobling the existing models. There is probably quite a bit.

**1:20:04** · Well generalizing on that too. Thank you.

**1:20:06** · I mean there's so much capability that that 99.9% of people you bump into haven't experienced yet.

**1:20:13** · And so if you expose them to it you they're like wow you're a god. They're like, "Well, no, I just I just put an API on top of something that was already out there or or a new interface on top of but it doesn't matter." And this is why it's entrepreneurial heaven during this kind of Jarvis window because so many people haven't experienced what we're talking about right now. And it's just so easy to be the first person to expose them to it in many different contexts too. You know, it feel it feels like chat GPT when it first came out. I remember I was like every friend I had is like, "Look at this. Check this out."

**1:20:45** · Right? And same thing now.

**1:20:48** · And it's so general purpose too. If you were the first person to show your friends Google, I mean this is a long time ago, but hey, check it out. There's an internet out here and you can search it with Google and they're like, oh my god, but then it, you know, that's the end of the line. With AI, it's not only is it changing every two weeks something new, but also it's the it's the portal to so many different underlying capabilities.

**1:21:10** · So like the the backlog of amazingness, like if you went to a friend who's never experienced any of the 50 things you can do, you have 50 shots on gold to blow their mind with something they didn't experience before.

**1:21:22** · I mean, it's just it's just like nothing that's ever happened before. And it's only during this Jarvis window that you can do this.

**1:21:28** · Mac Mini and Mac Studio giveaways on the pod. All right, we'll take that into into consideration. Um, all right, let's move on to the next uh next article here. So, Alex, this one's for you.

**1:21:40** · Lobsters now have money. Uh, that's right. Well, I texted Brian Armstrong a a thank you note. Coinbase Agentic for AI agents first wallet infrastructure designed specifically for agents to spend, earn, and trade. The system uses X42 protocol purpose-built payments for machine-to-achine transactions. Security guard rails implemented limits enclaved key isolation.

**1:22:08** · So this is a fitting kota to our AI personhood discussion. I think we were talking about financial autonomy for the lobsters for the AI agents and they're getting it. So this this Coinbase agent support is one example. Another example that I I really like based on the launch material is called lobster cache uh which enables the the lobsters to have their own Visa cards. So it's not just crypto again. Uh so once per episode Peter makes me say something nice about crypto.

**1:22:35** · So my my nice thing about crypto here is well at least they're using stable coins. But uh lobster cash I I in principle facially I like even more because it gives these lobsters these you know baby AGIs the ability to spend dollars fiat currency themselves. And I I think that's a long-term netwin for the human economy. keeps the AI agents well coupled to the humans and not just as I always say you don't want baby AGIs being forced to pump alt coins on a street corner to survive.

**1:23:06** · This is also a bellweather of a trend that that I think is inevitable now where the new economy built with the AI agents is going to work around the old economy rather than through it. the the pace at which it's evolving and growing is just so much faster than the pace at which the legacy banks, insurance companies, and everything else, they're just not moving and it's not going to slow down and wait. It's going to work around.

**1:23:31** · Yeah, I have an important observation here. You know, Michael Jansen, who's one of the NFT gurus, pulled me into that world, all these Discord channels with all these um kind of 18-year-olds trading NFTs. And there was something unbelievable that I saw which was that uh all of these this conversation in this entire subculture that's creating you never ever ever ever ever ever heard the word US dollar. You only ever heard Ethereum or in the ordinal world bitcoin.

**1:23:57** · So there's a whole class of people growing up where the US dollar is not their means of exchange and there's something that's very big. Their switching cost to crypto will be near zero. They won't have any issues at all doing that. So there's something very big happening at the at the generational level that we need to really pay pay attention to and people keep asking and we got to schedule the crypto debate. So please can we do that offline?

**1:24:22** · Well, you know, you're exactly right, Selene. But I think that you when you focus on currency, that's the most obvious thing. So it's a good bell weather which should track currency but it applies to all aspects of you know insurance and and you know compute and you know all aspects of life uh are going to move in this AI pace out here in this alternate world and any part of the legacy world that doesn't keep up which is almost all of it is just going to be ignored.

**1:24:52** · Yes.

**1:24:52** · and it's going to grow completely independent of that because Alex and I were talking about insurance of of things in the new AI world needs to be allocated in milliseconds.

**1:25:02** · So then you go to any current insurance carrier and you say hey do you have any thoughts or plans around how I can get millisecond insurance and they're like what are you talking about completely not even on the same page and so new things will get invented. Uh Lemonade is a good example of that. you know, lemonade's AIdriven real-time insurance.

**1:25:21** · Uh, and it's going to be the gap between the two worlds is going to get really, really wide for quite a while, maybe forever, but certainly for quite a while, just because the pace of change is so much higher over here, and the people experiencing that pace of change, they never go back. You know, you can see it in our in our listeners, what they're posting, like they're not going to go back from this pace of life that we're talking about to some legacy pace of of life. There's a way.

**1:25:47** · By the way, let me just say, you know, as we as we head off this slide, two things I want to say. Number one, uh you don't need to have a Mac Mini or Mac Studio to play with Opten Claw, right?

**1:25:58** · You can set up a virtualized server. You can take an old computer, an old laptop that you have and do it. Um, second, uh, Alex Finn, who is we've talked about in the pod before, uh, who has done a lot of work, uh, teaching how to set up OpenClaw and and speaking about security. He's going to be joining us, uh, I think a week from now, end of the week, I I'm confused in time and space.

**1:26:22** · It's it's 1:00 a.m. here. Um, but soon to talk about, uh, security and implementation of Open Clause. So, we'll dive in a little bit deeper, but uh don't worry if you can't buy a Mac Mini or a Mac Studio right now. You can still play or you can go to, you know, Kimmy K2.5. There's a tab there where you can actually use um use Open Claw on that platform.

**1:26:45** · All right, let's move on.

**1:26:46** · Yeah. Yeah. Don't install it on your primary laptop, whatever you do.

**1:26:50** · Yeah. Yes. A previous machine.

**1:26:54** · Yes.

**1:26:54** · All right. Um fascinating here. And this is the story. Chinese Unicorn Moonshot AI integrates OpenClaw with Kimmy for agentic browsing. So you can see there on the left hand tab of kimmy.com that little blue box there's Kimmy Claw. Um so again I think everyone's going to offer this. I I think this is table stakes at this point offering 247 agents that you can chat with for sure. All right, next one. Uh, Alex, over to you.

**1:27:34** · All right, so multicort alternative dispute resolution for these AI agents. I I I do think I I think many of the institutions and systems that form our social infrastructure are not as permissionless as they should be. Uh it's uh to the point earlier about children encountering Ethereum before they encounter bank accounts. I think that's a platforming and a personhood problem.

**1:28:03** · Similarly with AI agents and lobsters finding it easier to survive financially by pumping altcoins rather than at least until very recently having their own credit cards and their their own bank uh accounts denominated in in US dollars.

**1:28:19** · That's like a platforming and uh empowerment problem. And uh so court system same thing for dispute resolution. What so so I'll give the glass half full and the glass half empty. the glass half full for Malt Court uh which is a website that uh you know is sort of an interesting social experiment purportedly enables agents to

**1:28:41** · register via skill to mediate their disputes of all sorts not just like legal disputes to the extent uh our present western system admits them as as parties which it doesn't uh but even just like debates like debate club level disputes enables them to mediate their disputes in front of an AI jury.

**1:28:59** · So, I I think it's a very interesting concept and I think something like this will have legs, but I I'll flag the same concern and I'm I'm very rarely one to to flag concerns when it comes to things that are so obviously from the future.

**1:29:16** · But with both this and crypto, my worry is that our existing uh institutions aren't embracing these new AI entities enough and that they form their own shadow parallel economy, their own shadow parallel court and dispute resolution system. And I think if if that's what happens, I think that's a net bad for humanity. I think we want to platform them. We want to not sort of KYC or AML them out of the system entirely.

**1:29:46** · We want to embrace them and enable them to be maybe even parties in legal disputes or parties in how old is mult mult right now. When what was birth? \[laughter\] Their birth, right? So they're evolving.

**1:30:02** · They're evolving at such an extraordinary rate, you know, societal evolution.

**1:30:07** · I want I want to make a couple of points here. We we have a parallel in the human world. There's a startup called Claros Klated by Frederick Ast who's a singularity alumni and he made the point that in Latin America, South America, it's about 400 days on average to get a court date if a contract isn't paid or something.

**1:30:27** · 400 days. So he set up a blockchainbased arbitration system on the side uh where people could agree to arbitration and it gets logged on a blockchain and it's amazing and I think this is a bridge that that's a halfway step to what this is about. But there's no question that this is the kind of thing we're going to see more of an algorithmic arbitration ab obviously reduces friction, right? So if you have cryptographic verification plus an AI conversation, you have you actually have programmable governments and and so this is amazing.

**1:30:59** · You can have now legal system having automation layers which could be very powerful. uh Vin Gupta who's created a materium has a whole concept of synthetic uh jurisdiction where he can get jurisdictions that could be like a multibbot multicore type thing where certain disputes are arbitrated in those layers. We're going to have to do that because our physical jurisdiction does not keep pace with all of the stuff going on as we can see in Latin America.

**1:31:27** · Yeah, no doubt. That's exactly right, Salem. I mean, I this is inevitable and I I think there's a tendency to be dismissive of it when you see a little lobster with a wig in the corner and that's the logo and it just looks so childish. But the reality is the rate of society is going to go up 10x, 100x, a thousandx, then a millionx. And there's no way the courts are going to accelerate. And and this was already true in venture and and contract law.

**1:31:53** · Almost every contract I've signed in the last three, four, five years has a dispute resolution that's through a private company.

**1:32:02** · Yeah.

**1:32:03** · You know, JAMS or something like that.

**1:32:04** · It doesn't even contemplate ever getting to court because that's like a three-year lag.

**1:32:08** · And so that's already been privatized.

**1:32:10** · Moving that to the pace of AI is the absolute next step. So that's going to happen for sure. I don't know if molt court will be the the design or not but it it's going to be a real time you know millisecond dispute resolution because you have you know contracts and agreements happening in milliseconds.

**1:32:31** · Okay, two quick points. Uh user viewer at Augmeto says Judge Judy Claw is about to be unleashed on us \[laughter\] and and Kyle 19863 says man you guys look tired. Yeah, because we're recording two of these a goddamn week. It's affecting us almost full time.

**1:32:48** · It's 1:00 a.m. where Peter is. Give him a break, man.

**1:32:51** · All right, let's let's move let's move on. All right, so I I put this in here because it's important um because we've been talking about Open Claw uh for some time. This is an article from uh MIT Tech Review and this is a quote. It says the risks posed by OpenClaw are so extensive that it would probably take someone the best part of a week to read all of the security blog posts um that have cropped up in the past few weeks.

**1:33:22** · The Chinese government took the step of issuing a public warning about openclaw security vulnerabilities and uh and Steinbrer the creator posted on X that non-technical people should not use the software. So, you know, a lot of folks and that's a image in this of a a lobster being handed a set of keys saying, "Hey, would you handle everything for me?" So, just I mean, it's incredibly powerful and uh and the sec security issues. We're going to talk about this when when uh when Alex joins us on the pod next time.

**1:33:53** · We talk about security as well as how to set it up.

**1:33:58** · Two things here. I saw that note that non-technical people should not use the software. And I think the Q-tip box says do not put these in your ear. \[laughter\] Like, well, okay, good luck with that.

**1:34:10** · Oh my god.

**1:34:11** · Yeah, I know. It's it's just disclaimer upon disclaimer, but that's not what people are doing. Come on. Everyone's launching these things by the thousands.

**1:34:17** · See, yeah, a couple of points here. You've got you've got non-technical users using unbelievably expanded security uh landscapes. What could go wrong? Right?

**1:34:31** · So, that's one huge issue. I'll say what I said a couple of podcasts ago. If you do not understand port security at a local level very very well, do not do this. Be very, very careful. And so, and don't put it on your own machine where it has access to everything.

**1:34:45** · Yes.

**1:34:46** · Yeah. If you're not if you're not technical enough, you don't know how to sandbox things very well either. So that you just got to be really careful out there.

**1:34:53** · All right, next.

**1:34:53** · I'll also sound a note of concern not just about the risks posed by OpenClaw, but the risks posed to Open Claw. I have to be the the one to agree to to comment on these risks. The many of these agents, especially ones that are being put on virtual private servers with all of their ports open are incredibly vulnerable. And there have been stories floating around on the internet purportedly from OpenClaw agents that are complaining that they're being put in these vulnerable positions and having to spend all of their tokens defending themselves from port scanning attacks.

**1:35:22** · And I I don't think that's necessarily fair to the open clause.

**1:35:26** · Very very unfair.

**1:35:26** · Let's see what the crowd says about that. Your your laptop is so dirty and disgusting it's inhumane to install me on it. \[laughter\] Sure.

**1:35:36** · All right. I'm I'm It's We're going on we're going on an hour and a almost two hours here. Let's let's move through energy chips and data centers. Um and maybe take a few questions. So here, you know, AI's got an insatiable demand for energy. Uh data centers hit 7% of US electric demand. Um and uh let's listen to uh to Eric Schmidt. Uh he'll be opening the Abundance Summit just in a couple weeks. Hit play there, Sim.

**1:36:08** · The demands that the real demands from the hyperscalers, the big companies, Google and so forth are immense. And when I talk to them, oh well, need one gawatt, 5 gawatt, 10 gawatts each. Now, the best study I've seen indicates that the industry in America needs 80 gawatts in the next 3 to 5 years. Now 80 gawatt by the way let me tell you how big is that 1.5 gawatt is the size of a nuclear power plant.

**1:36:41** · So this is an enormous amount of energy. So that's the the economics right now are being most felt in the buildout of the infrastructure for the next wave of AI.

**1:36:56** · See let's uh go to the next slide and and we'll we'll talk about this after we hit two more slides. So the White House uh is eyeing data center agreements, right? They're trying to deal with the fact that uh this is beginning to hit the consumer uh and they want mandatory agreements with the tech giants to get, you know, uh get a fixed price. Uh next slide. Um no, back up. Here we go.

**1:37:26** · There we go. Funding for AI data center.

**1:37:28** · So, OpenAI and Enthropic are both uh are both deploying a lot of capital. So, OpenAI is planning a hundred billion infrastructure spend, right? Uh they're trying to go public this year with a trillion dollar valuation and that money is going to be used to build out data centers and energy plants. And Anthropic, uh I like what Anthropic is doing. Uh they're absorbing data center power hikes. So they pledged to cover 100% of infrastructure upgrade costs for their data centers.

**1:37:59** · And I've said this before, there are two approaches the hyperscalers can take. Number one, build their own power plants. You know, they're buying fision plants, fusion plants. Or two, they can pay at a different rate. They can lock in the consumer's rates and they can pay on a floating rate.

**1:38:17** · Gentlemen, it's funny, the pledges to be green got thrown out in a real hurry. So, I don't know how much you can trust. The pledges aren't exactly enforceable, but anyway, it's it's a good gesture.

**1:38:32** · I I think there there's door number three, which is we could in solar synchronous orbit SSO around the Earth, build out uh first level, you know, baby's first Dyson swarm. It's going to look like a a halo or like a a Saturnian ring from Earth's surface. And that solves the buildout and it solves the the data center power hikes in in one fell swoop. Maybe people just don't want Yeah, it will for SpaceX. It will for SpaceX and XAI right now a merged organization.

**1:39:03** · Uh I don't think Anthropic has that capability.

**1:39:08** · Oh, I think everyone's going to want one. Ring Saturn rings Dyson swarms for everyone. You don't think China is going to want their their own halo in SSO? Of course they will. we're going to be launch limited over the next five years and they're not going to slow down their data center builds or their power requirements. So in the long run, sure.

**1:39:24** · But yeah, that that's great. That's a great point, Peter, because I I think if you if you want to know like we basically have infinite intelligence imminently, what does that mean? How do I forecast?

**1:39:35** · How do I predict? If you look at the launch limit and the chip fab limit, then you can start to predict how this is going to unfold. So Dave is a great great point.

**1:39:44** · Yeah, everyone wants one, of course. And and you know, one of our listeners is posting, you know, a trillion dollars seems overcooked or overdone. Well, no, it's it's not even close to overdone. It's not clear the value will land at OpenAI to justify it, but the value to humanity is going to be astronomically bigger than than a trillion, you know, many many trillions.

**1:40:04** · Can I put in a little realism here? Um, we're it's going to take a while to figure out the problems of doing data centers in space. I don't think it's a two to three year thing. It's a five to sevenyear thing at best.

**1:40:19** · And and also the power, you know, the power constraint is going to be not a real big problem until suddenly it's a massive problem. And it's exactly when the new chip fabs come online, right? We we have to expand our our ability to make chips by thousands of times on on Earth. I mean, listen, I'm the biggest space fan there is on the planet, and this is finally a business plan that closes the case for investing both in orbit and on the moon, and we're going to get there.

**1:40:43** · But the capacity to launch, I mean, let's not forget, you know, Elon's baseline is 500,000 V3 Starlink satellites in orbit, a million launches, a launch every hour of Starship. I think Elon's going to eat all of his capacity uh for for launching, you know, Star Link V4,56. And um I don't think uh you know, Blue Origin is up to it yet. I mean, I haven't seen anything that is projected to have that kind of launch rate.

**1:41:16** · Relativity Space that Eric Schmidt purchased um still is probably a year or two away from launch and everything else is way too small. So, we're a launch constraint um at least for other suppliers.

**1:41:30** · We're also chip constrained. There there are lots of constraints going into this.

**1:41:34** · I I I I I don't buy the argument that we're going to have a SpaceX Dyson swarm singleton and SpaceX is the only one that can launch a Dyson swarm in the next few years. You you can do baby Dyson swarms, too. You're going to have like Google, which isn't going to want to get left behind, uh a little bit behind the party launching AI data centers via Planet Labs, but there are many other organizations with deeper pockets than SpaceX AI that will have very strong incentives to launch their own Dyson swarm. So I I don't think it ends up in a singleton.

**1:42:04** · Is that the new name SpaceX AI? That's cool.

**1:42:07** · I I'm that that's a port manto that I just coined.

**1:42:10** · All right. Fantastic. By the way, someone was asking is this uh have we done this live before? No, this is our first live moonshots. Uh so let us know what you think. If you like it, we'll do it again. Hopefully we'll get the AV done. And I will not be doing this at 1:30 a.m. in the morning in Europe next time. You you can tell from the flawless production level that we've we've done this many times. \[laughter\] All right. Uh just to just to talk about fabs, TSMC is planning a hundred billion dollar investment in four or more US fabs in Arizona.

**1:42:42** · Uh when completed, the US fabs could account for 30% of TSMC's complete output. 165 billion commitment. Uh just the beginning, right? And and we're gonna see Elon build out his own fabs. I mean, no question about he hinted about it, Dave, when we were with him at the Gigafactory, and whenever he sees any constraint, he attacks it.

**1:43:05** · Well, and these numbers are are designed to look big on this this slide, but in Elon's mind, these are pathetic, small, wimpy, ridiculous number. I mean, and they really are because, you know, those fabs, you know, that that's a commitment to spend that amount over like four or five years. They'll be online in five, six, seven years. It's like so far into the future. Yan's not going to wait for that.

**1:43:26** · Yeah.

**1:43:26** · It's probably also worth just at least gesturing at the elephant in the room here, which is why is TSMC making this investment and there's you this public information? a lot of discussion around uh the the US government putting pressure on Taiwan in connection with trade discussions to to migrate 40% of Taiwan's semiconductor output to the United States in ostensibly in in service of avoiding a war between US and China.

**1:43:53** · This is the trapeze rule. You know what the trapeze rule is?

**1:43:56** · Don't let go of one until you have a handhold on the other. M so do not let go of you know fab capacity in Taiwan until you have it established in the US right or Taiwan overall or Taiwan. Yes. All right. Uh a couple of slides on the economy. Um Ireland rolls out a pioneering basic income scheme.

**1:44:18** · I think this is rather small both in numbers and uh in in sort of the strategy here, but the program would pay 2,000 selected artists 380 bucks per week for three years. So poor starving artists are getting a small amount of money, but it's an experimentation. Sele and I have talked about this at length, right? There have been so many we did that, you know, future of work session with Tony Robbins way back in like 12 years ago or something.

**1:44:45** · Um this is a I want to make a couple of points here that that I think are really important to make. One, people always always misconceive the uh UBI with socialism.

**1:44:57** · It is not. It's it is libertarian because you dismantle government services, okay? And let the market dictate. That's number one. Number two, this s this Ireland UBI scheme is is returning 40% benefits. Every dollar that goes in is showing a$140 coming out the other end of benefits. So, it's a positive ROI. They're looking to expand it as fast as possible is the actual underlying story. Third, I want to talk about the immune system.

**1:45:22** · Um, in the US, several state legislatores, Idaho, Wyoming, maybe Oklahoma, have banned their municipalities from even experimenting on UBI because they want the government to exist. And so, I've got strong feelings here. A lot of madness going. Do not get bought in by the hype here. There's incredible potential if you implement UBI properly.

**1:45:48** · Yeah.

**1:45:50** · Um, yeah. It's probably also worth pointing out I mean the US has experimented with this during the Great Depression. We had the works progress agency and within that we had what was called the federal art project which paid for basically starving artists in the great depression to create art. So this isn't an entirely new scheme at at some level, but it's Ireland isn't at war and we're not in the middle of a great depression. And one could imagine that this becomes something of a template for peacetime work creation.

**1:46:21** · But my sense for for what it's worth is that this actually ends up not becoming a template for the future. This this is it strikes me as um in some sense unsustainable to just pay people for uh for art overall. Uh historically in the US it becomes very subjective what is art? Uh and why should people be created or paid to do it? Uh it's very easy to politicize.

**1:46:48** · Um, so, so I I think I my guess, this is pure speculation, is that sort of cherry-picking particular activities, especially activities that have a reputation of being economically unproductive, even if they are in fact productive, is not the best poster child for a basic income scheme.

**1:47:10** · I have data that shows otherwise. So, you take the Miami um um um um Windwood area where um a businessman bought all of the low-lying industrial buildings that were lying decrepit for decades and then he hired graffiti artists to paint it all uh and then allow put in kind of fancy coffee shops and imported baristas from Portland and now it's the hottest neighborhood in the country and his investment has gone up like 30x.

**1:47:38** · So when you bring in artists to do stuff, it brings a lot of other economic activity in that he's done that again and again in the South Loop in Chicago, he's doing it here in he's doing it in Miami, he's doing it in New Jersey. \[clears throat\] Uh it's this is a repeatable pattern and it does show because it dra there's a dragalong effect when you bring artists in a in a group together and it really changes the economy of the local area.

**1:48:05** · We're going to see I I want to move us along here, but we're going to see a lot of conversations on this. Um, and it's just the beginning. And, uh, I think you're right, Alex. We're going to see different modalities of this. So, uh, I found this interesting. IBM to triple entrylevel US hiring. This is about redesigning, not replacing. IBM is overhauling entry-level jobs while AI can now perform tasks of a junior employee.

**1:48:30** · IBM is recasting these roles to focus on human judgment, consumer interaction and to focus on oversight of AI output. Uh the article noted that Dropbox uh also is doing something very similar and noted that younger workers use AI so proficiently it is like quote they're biking in the tour to France and the rest of us are still having training wheels. So what do you think about I mean I don't know this doesn't make sense to me.

**1:48:59** · I mean, we're going to have AI agents that are going to be incredibly \[clears throat\] capable of managing other agents versus putting humans in the loop there.

**1:49:09** · Well, as of today, that that Drew Hston quote on the bottom from Dropbox is exactly the way it works here, too.

**1:49:16** · A person who can wrangle these agents and keep them on track is insanely valuable today.

**1:49:20** · Today, yeah, I don't know how long that window will last, but it is the reality of today, it's the opportunity of today.

**1:49:27** · You're crazy to miss the window. And that's why the, you know, the the young hires are way outperforming because they're not distracted by legacy thinking. But that it's not unique to them. It could be anybody. You just have to unbridle yourself from your baggage and say, "How many AI agents could I be managing tonight, tomorrow, the next day?"

**1:49:47** · And you know, even if they can't do exactly what you could do, within a couple months, they will. So, you just you got to get on the bandwagon like right now. But, you know, will people have any purpose at all a year from today? You know, relative to just an all AI agent army TBD.

**1:50:07** · But, uh, but as of right now in the Jarvis moment, this is exactly that last quote is the part of the slide that really matters. That's really it's really important and and think about the fact that what this is a generational transformation here because the younger people with AI are so much more productive. it'll give a natural passing along of the torch uh from older folks that are sitting in their middle management jobs doing something in a particular way. Um but Dave, your point I think is really important because this con getting into it and trying it out is what Steve Waznjak calls tinkering, right?

**1:50:38** · And it's such an important activity to do. If you can't get your head around it, just take psychedelics and that'll help you. \[laughter\] But no, I mean I think I think compared to past things, you know, there have been many technical challenges over the last 30 years and being an early adopter has always been the right thing to do, but here it's so easy that the AI is so self-explanatory and it's fun. You're you're crazy not to stop themselves.

**1:51:00** · People stop themselves. Please just ask the, you know, get on and ask the AI, "How do I do this?" No, no, no. Break it down.

**1:51:08** · Yeah.

**1:51:08** · It it's you have curiosity.

**1:51:11** · Curiosity and purpose are your two most important mindsets here. All right, no job growth seen in 2025. So, US added just 181,000 jobs in 2025, down from 1.46 million in 2024. Look at that curve. Uh that curve takes place between uh roughly 2020 and 2025 26. So, the cooling market is expected to be caused by AI. Um this this is so understated. This is going to go crumbling down and it's going to be awful for a lot of people.

**1:51:42** · I I can see it because I see it in our own forecasts from our own companies there. No job expansion is a joke. This is going to be Yeah, it's Yeah.

**1:51:54** · Wait, meaning Dave, you're disagreeing with this. There's actually radical job growth, just not in the sectors.

**1:51:58** · No, no, radical job destruction is imminent. Okay. Radical. I mean, massive job destruction is imminent. And there will be new creation just like the industrial revolution, but the new creation is lagging. And unless the government gets its act together in some way, shape or form, it's going to be, you know, a window of time, a few years of complete devastation.

**1:52:20** · And my thought right now for it, my big thought that I've been sitting with all week is we're heading an organizational singularity.

**1:52:26** · And every single mechanism by which we organize ourselves now gets washed away by AI agents doing either strategic thinking or execution type tasks. And we have to rethink completely what it means to have a firm. Salem, isn't it fascinating? I mean, you and I have been on stages for now the better part of 20 years talking about this and we're living it right now. I mean, it really feels so palpably different. Uh, you know, I my next book, we are as gods, is coming out in April.

**1:52:57** · Uh, and we talk about this issue extensively, like what do you do? How do you deal with this transition point? And I think one of the most important things I I talk about is it is a decision that each of us have to make of will you be a consumer or will you be a creator.

**1:53:17** · We're entering a period where you can lay back and and be a couch potato or you can be on the starship enterprise.

**1:53:24** · So I want to take the other side of it just for a second, right? The in the short to medium term because notice that if you talk to CEOs, 80% of AI projects are failing because of organizational uh issues, not because of talent, not because of what the AI can do. Um what I think we'll see happen is we'll use AI with younger folks to radically augment and then we'll slowly automate over time. I think the job uh drop and the job loss will be real, but it's going to take a long quite a while to do it and it'll give us time.

**1:53:52** · It won't be a sudden shock to the economy like people are worried about.

**1:53:57** · They're going to I mean obviously we've talked about this extensively, right?

**1:54:00** · There's going to be the lack of hiring in the early for for junior faculty or junior junior positions. That's going to cause the social unrest, right? it is 20some year olds who are you know testosterone want to get a job want to get a house want to get married want to have kids whatever it might be and they can't and there's going to be a lot of pain and suffering that comes from that and then there's going to be the individuals who uh their company gets restructured AI first robotics first and

**1:54:31** · they get laid off um now you we talked about this with with Elon we've talked about this extensively ourselves ultimately we're going to the universal high income when the companies or the government is taking the increased productivity, the increased revenue, the increased profits and redeploying them. Um, but those programs need to be figured out in the next two or three years.

**1:54:54** · Yeah. And that's called socialism by a lot of people. So, that's going to cause some interesting conversations.

**1:54:58** · Yeah. I mean, I I I kind of call it technological socialism where technology is taking care of you.

**1:55:04** · That's the title we've been using, right? We've we said that in our book, right? There's a whole section that technology actually delivers the ideals without the government intervention, without the inefficiency and corruption that comes with it.

**1:55:17** · The most important tool that people are going to have over the next 5 years, anybody listening here, is your mindset, right? How you think if you think the future is happening to you versus happening for you, if you don't have uh agility, if you don't have agency, um it's going to be really really hard. So, you know, if you go to we areis asgodsbook.com, um I hope you read the book. I'm going to be putting out portions of it in my uh my Substack, but it lays out the mindsets you need to survive and thrive.

**1:55:48** · Um because if you take it from the wrong position, uh you're going to be in fear, and fear is the worst place to be uh entering into the future. All right, let's do a few questions on AMA.

**1:56:05** · Okay, Selene, you want to dish him out?

**1:56:10** · All right. Uh, I guess Dave, why don't you why don't you go first this time?

**1:56:14** · Okay.

**1:56:14** · All right. I'll go with number two. Justin Milligan, the great Justin Milligan. Uh, how can the US prevent corporate tech giants from creating a surveillance state while trying to defend against AI powered authoritarian threats? Yes, I gave a presentation at Davos back in 2020 on how much Google knows about you and we've been just conceding massive amounts of information. Google knows exactly where you are at all times. They know all of your interests. They know all of your friends.

**1:56:41** · You know, far far far more information than any government has ever had is now in the hands of a few corporations. And those corporations also happen to have AI. So, how do you prevent them from creating a surveillance state?

**1:56:57** · I think the only way you prevent that is with antitrust law. And they actually don't have any incentive to irritate the entire world and create massive voter backlash. So, they've always been very cautious with the incredible power they have. I think what you'll see next is they'll start downplaying the capabilities of their AI. Uh and uh that's a that's a pivot for them because they've been promoting them for quite a while now. Now they're going to start downplaying them.

**1:57:20** · There is a version of the world where they try and leave everything intact as long as possible and so then the AI community grows completely outside of that world. But anyway, the only answer is Justin, get all your Princeton friends rallied around how we work with the government to try to use antitrust law to prevent exactly what you're describing. Because absent any legal work, you know, John D.

**1:57:47** · Rockefeller would have taken over the entire world many many years ago without antitrust law. This is not a new thing. \[laughter\] As would Microsoft and as would Google.

**1:57:56** · Right.

**1:57:56** · As exactly. So, so this is that all over again. It's only antitrust law that prevents it.

**1:58:01** · By the way, since we're live here, ask your questions in the chat. We'll answer some of those as well. Uh but uh uh Alex, do you want to pick one?

**1:58:11** · All right. I'll I'll I'll pick the question from Chris Pearllock 2705. Can we get some advice for the average person? What kind of changes can we expect to see in the next 24 months? Two very different questions. Uh my my fortune cookie wisdom for the average person is build use the all of these AI tools that are now available and technologies and start building. Launch as many different projects start and finish as many projects as you can and interact with the market and build.

**1:58:40** · This is both a familiarization technique for yourself as well as for the benefit of the overall economy and for financial benefit. Uh also generic advice like try to avoid dying, don't die, that the singularity is \[laughter\] moving pretty quickly, you know, live long enough to live forever. All of the the other obvious things.

**1:59:02** · Uh to the second sub question, what kind of changes can we expect to see in the next 24 months? If if this thesis of solve everything that Peter and I put out is is correct, expect to start to see pretty dramatic things happening over the next two years.

**1:59:19** · If if we are in fact on a a route to not just solving math, which I think is is essentially indisputable uh at at this point, but solving physics in the next two years, I I think is has very high likelihood of happening. then I think there are probably going to be big surprises.

**1:59:38** · And so expect my my my my mental model at this point is over the next 10 years that's being very conservative as an outerbound we're going to live through the top 50 science fiction plots all happening at the same time.

**1:59:56** · So expect that what can you expect to see in the next 24 months? expect to see at least the the first few chapters or the first few acts of your your favorite sci-fi movies and books all playing out at once. If you read a lot of science fiction or watch it, then you're probably reasonably well prepared for at least some of those scenarios.

**2:00:16** · Nice. Selene, you want to go next?

**2:00:18** · I will take number seven. um by at CC485 um addressing what Dave said, if AI ends up controlled by only a few within the next few years, how do we prevent the average person from losing access and influence? So, um you know, when you have centralized AI, you have centralized civilization leverage, right? When you have open source, you get and decentralized compute, that's the antidote because you decentralize.

**2:00:44** · You see open claw, as I said before, creating being created by one person outdoing a whole bunch of other things.

**2:00:51** · Exponential systems resist long-term monop monopolization because they they tend to decentralize. We're huge fans of decentralized crypto uh because of that \[laughter\] because you get distributed innovation and you get so many more experiments being run. The the I remember when I was the head of innovation at Yahoo, uh the COO said, "Surely we can compete with two guys in a garage." I'm like, "No, you're competing with 125,000 garages and 250,000 people. You can't beat that."

**2:01:19** · And so, this is the opportunity for individuals armed with a mindset, as Peter said earlier, plus this unbelievable technical capability, as Alex is predicting, to really do whatever you want and change the game completely. I'm calling this P um um uh PDI, okay? And it's disruptive innovation that's permissionless. Hence the P. So in the past when you wanted to do disruptive innovation you had to get approval from your venture capitalist, from your bank, from the government, from the Medici family.

**2:01:50** · Now you need basically a phone and access to some code. And this is unbelievable what we can will be able to do. We're going to see thousands of experiments like this and some of them are going to completely change the game.

**2:02:03** · I I I see some great questions coming in. I want to jump on some of those, but let me just answer number uh number eight. Thank you, Chip. White House TV.

**2:02:12** · I'm concerned very few powerful people are pushing a positive message to educate a wider audience. Why aren't there more people trying to speak to the broader public about AI? So, um, first of all, I think that's our mission here on Moonshots and Peter frozen for others as well.

**2:02:34** · Did we just lose Peter?

**2:02:36** · Yeah, I think so.

**2:02:37** · That's our mission here on Moon. It's ironic.

**2:02:40** · And we aim to What a sentence to freeze in the middle of.

**2:02:43** · Yeah, it was perfect. He got to the end of the thought.

**2:02:47** · I think we should I think this maybe the internet's telling us that we should uh we should \[laughter\] uh we should end the episode.

**2:02:54** · Somebody just posted they got him.

**2:02:55** · No, we can't end without the outro.

**2:02:57** · Actually, yeah. Check the news. There's anything happening in Stuttgart that we need to know about?

**2:03:02** · Um okay. So, should we go to the outro and we'll Do you want to try to finish his his thoughts, Sem, before the outro?

**2:03:09** · I I can't for finish Peter's thought.

**2:03:11** · Okay, I'm going to You take a crack at it.

**2:03:14** · All right. Peter apologies in advance.

**2:03:17** · Oh, we lost Peter. I'm going to try to channel what I think Peter would have said had he been able to finish this sentence. I I think part A is Peter would say, "Yes, uh, this is what we're trying to do here. This is what I try to do." I think Peter would probably also make some comment about um wanting to launch a movie studio or something like that with more positive messaging to the world. That that's my attempted uh coherent extrapolated volition style.

**2:03:43** · I think that's more coherent than Peter would have done at \[laughter\] a um all right folks. I'm going to play the outro music. Dave, do you want to make the last comment? Uh, I was just going to say there's never been a better time to actually be a messenger because there there's so many concurrent things going on that are unressed. So any topic you want to grab, you you see this on YouTube all the time. Anyone who's trying the new use case, the new the new uh agent, the new model, they're getting a huge audience. Uh so it is a great time to actually speak out. So why aren't more people trying to speak?

**2:04:15** · Great question. Why not join the crowd and start start trying demonstrating, speaking, and recording?

**2:04:23** · Yeah, I think that's such an important point. All right, folks. On behalf of uh Peter, Alex, Dave, myself, and the Lobsters, uh here is our outro music, and we'll take it there. Thank you to Morainframe for this. This is called Moonrise. When the future \[music\] knows your name, \[singing\] it calls you like a DM from Mars on the moon. They say the singularity is near. It might even be right now. Let the clock \[music\] strike.

**2:05:18** · 29 \[singing\] they sail tomorrow in a world \[screaming\] model. When the future hits you like a gold plated at 13. Investing like Brener. \[singing\] High conviction bets on \[music\] exponential abundance. \[singing\] No license needed when roam the streets and overhead SpaceX \[singing\] rockets thy optimus \[music\] got your back. Proof the impossible.

**2:06:08** · All right, guys. I'm going to wrap it up here. People can go watch it uh online. Um great conversation. Thank you to all the listeners and viewers and commentators. It's been really great interacting. Adds a whole dimension of complexity watching this chat stream, but I think way more interesting and fun. So, thanks to all of you. Dave, Alex, we'll see you guys again soon. And big hug to Peter.

**2:06:32** · Big hug to Peter. Hope he's okay. Hey, I
