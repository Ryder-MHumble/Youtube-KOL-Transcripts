---
title: "Dave Plummer: Programming, Autism, and Old-School Microsoft Stories"
source: "https://www.youtube.com/watch?v=HsLgZzgpz9Y"
transcript_source: "https://lexfridman.com/dave-plummer-transcript/"
episode_url: "https://lexfridman.com/dave-plummer/"
author:
  - "[[Lex Fridman]]"
guest:
  - "[[Dave Plummer]]"
guest_title: "Creator of Task Manager"
published: 2025-09-06
created: 2026-07-24
description: "This is a transcript of Lex Fridman Podcast #479 with Dave Plummer. The timestamps in the transcript are clickable links that take you directly to that point in the main video. Please note that the transcript is human generated, and may have errors. Here are some useful links: Go back to this episode’s main page Watch the full YouTube version of the podcast Table of Contents Here are the loose “chapters” in the conversation. Click link to jump approximately to that part in the transcript: 0:00 –"
analysis_report: '[[Lex Fridman - Dave Plummer：Programming, Autism, and Old-School Microsoft Stories]]'
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=HsLgZzgpz9Y)

This is a transcript of Lex Fridman Podcast #479 with Dave Plummer. The timestamps in the transcript are clickable links that take you directly to that point in the main video. Please note that the transcript is human generated, and may have errors. Here are some useful links: Go back to this episode’s main page Watch the full YouTube version of the podcast Table of Contents Here are the loose “chapters” in the conversation. Click link to jump approximately to that part in the transcript: 0:00 –

Timestamps:
0:00 - Introduction
1:22 - First computer
7:00 - Dropping out of high-school
14:41 - Joining Microsoft
16:53 - MS-DOS
20:05 - Windows 95
26:52 - The man behind Windows
31:48 - Debugging
37:05 - Task Manager
42:14 - 3D Pinball: Space Cadet
47:13 - Start menu and taskbar
58:12 - Blue Screen of Death
1:00:21 - Best programmers
1:08:22 - Scariest time of Dave’s life
1:15:50 - Best Windows version
1:17:40 - Slot machines
1:21:23 - Autism and ADHD
1:40:43 - Fastest programming language
1:44:48 - Future of programming

## Transcript


### Introduction

**0:00** · Lex Fridman: The following is a conversation with Dave Plummer, programmer and an old-school Microsoft software engineer who helped work on Windows 95, NT, and XP, building a lot of incredible tools, some of which have been continuously used by hundreds of millions of people, like the famed Windows Task Manager. Yes, the Windows Task Manager, and the zip/unzip compression support in Windows. He also ported the code for Space Cadet Pinball, also known as 3D Pinball, to Windows. Today, he’s loved by many programmers and engineers for his amazing YouTube channel called Dave’s Garage. You should definitely go check it out.

**0:44** · Lex Fridman: Also, he wrote a book on autism, and about his life story, called Secrets of the Autistic Millionaire, where he gives really interesting insights about how to navigate relationships, career, and day-to-day life with autism. All this taken together, this was a super fun conversation about the history and future of programming, computing, technology, and just building cool stuff in the proverbial garage. This is the Lex Fridman Podcast. To support it, please check out our sponsors in the description, and now, dear friends, here’s Dave Plummer.


### First computer

**1:22** · Lex Fridman: Tell me about your first computer. Do you remember?

**1:25** · Dave Plummer: I do. I didn’t own my first computer for a long time, but the first computer I ever used was a TRS-80 Model 1, Level 1, 4K machine, and I rode my bike in fifth or sixth grade, so I was about 11, to the local RadioShack. They had the standard component stereo systems, everything else RadioShack had, but they had a stack of boxes that was labeled “computer.” So I was asking the people who worked there about it, and they said they just got it and they hadn’t set it up yet. I was rather precocious and I figured, “Well, I’ll set it up for you,” and they said, “Okay. Have a shot.”

**1:53** · Lex Fridman: Did you know what you were doing?

**1:54** · Dave Plummer: Absolutely not. I mean, it’s no worse than a component stereo. The only thing is that Tandy, in their infinite wisdom, used the same five-pin DIN connector for power, video, and I think cassette, so they were all identical, and if you plugged them in wrong, you’d blow it up. So I read the label and got it working and wound up playing with it and not knowing anything about computers. So I’m typing English commands into it and, you know, PRINT 2+2 works perfectly, yet more simple English that you enter into a basic Level 1 interpreter is not going to get you very far.

**2:23** · Lex Fridman: So you’re trying to talk to it in English?

**2:26** · Dave Plummer: Didn’t know any better. And I still have an old foolscap that I wrote in sixth grade of a program that’s kind of illogically correct but has no chance of working on any interpreter that existed at the time, so it took me a while to figure out what was actually going on with them. But I rode my bike down there every Thursday and Saturday, and they were gracious to let me use the machine.

**2:45** · Lex Fridman: When was this?

**2:46** · Dave Plummer: ’79, ’80.

**2:47** · Lex Fridman: Okay. What was the state of the art of computing back then? So what are we talking about?

**2:50** · Dave Plummer: Well, the big three had come out. There was the TRS-80 Model 1, there was the PET 2001, and the Apple II came out roughly simultaneously.

**2:59** · Lex Fridman: Apple II. Would you say that’s the greatest computer ever built?

**3:02** · Dave Plummer: Probably in retrospect. Well, I would probably give that to the Commodore 64.

**3:06** · Lex Fridman: Yeah. You and I agree on this, that that was my first computer probably many years after it was released, but yeah, Commodore 64’s incredible. But yes, Apple II had a huge impact on the history of personal computers.

**3:18** · Dave Plummer: Right. It’s hard to gauge the long-term impact, but I think the 64 itself probably influenced more people, so that’s my reason for picking that one.

**3:26** · Lex Fridman: You think so?

**3:26** · Dave Plummer: The sales were certainly higher.

**3:28** · Lex Fridman: So Commodore 64 sold a lot?

**3:30** · Dave Plummer: Yeah. I mean, the numbers are hard to believe. It depends which numbers you believe, but even the medium estimates were pretty high.

**3:36** · Lex Fridman: All right, cool. So you eventually graduated to the Commodore 64. Tell me about that machine. What did you do on the Commodore 64?

**3:45** · Dave Plummer: Well, the first thing I did was overheat the floppy drive on it, which was unfortunate because it wasn’t a warranty machine. My parents didn’t have a lot of money so we bought it from Computer House as opposed to one of the major retailers, which meant when it died, it had to go back to Germany or something to be fixed. So I was left with no floppy and so I had a cassette deck, which was the best you could do at the time, and so I was writing small things, and I had a machine language monitor that you could load from cassette. It didn’t have an assembler built in, but it had a disassembler, so you could enter the op codes in 6502 in hex, and if you were careful about planning, you’d be able to write some basic programs.

**4:17** · Dave Plummer: So that’s kind of how I learned, and the first thing I ever wrote on it was a clone of Galaga. Now, it’s a bad clone of Galaga, but it has the major enemies that attack over time, and it’s all written in hand-coded machine language, and you can’t relocate 6502, so if you need to add code in the middle, you need to manually sort of jump to somewhere else, do your work, jump back to where you were. It’s just hideous spaghetti code. But it all worked eventually, and I went to make a backup of it to preserve it for future scholars or whatever the hell I was doing. And I copied my blank floppy onto my data floppy. So that was my first experience with data management.

**4:53** · Lex Fridman: Oh, no.

**4:53** · Dave Plummer: So I don’t have a copy of my first program anymore.

**4:55** · Lex Fridman: What was that feeling like? Do you remember, of, of just doing something if I may say so, like stupid, you know? Which is a part of the programming experience.

**5:04** · Dave Plummer: Yeah, there was a huge amount of guilt because, right, you destroyed several weeks- … of work and you know it was because you rushed- or you did something stupid or you made an unwise choice.

**5:12** · Lex Fridman: What can you tell me about the programming involved in that game?

**5:15** · Dave Plummer: So it’s literally machine language.

**5:17** · Lex Fridman: So machine… So it’s not-

**5:19** · Dave Plummer: Yeah, 65 with-

**5:19** · Lex Fridman: … even assembly.

**5:19** · Dave Plummer: Not assembly yet because there was no assembler built in, so I should have written an assembler as my first task, but I wasn’t that clever.

**5:26** · Lex Fridman: How hard is that to do?

**5:28** · Dave Plummer: Trivial, and it’s one of those things that sticks, I think. You do it so many times. You know, if I give you a C issue, there are certain syntactic issues in C that you’re never going to forget and get wrong. And it’s just one of those.

**5:40** · Lex Fridman: Like, what are the limitations of programming in machine code, as a programmer?

**5:44** · Dave Plummer: The biggest issue is you have to write completely sequentially because at least in that variant, 6502, you can’t add things later. You can only add things on the end. So it’s like programming a tape in a way.

**5:54** · Lex Fridman: What was the most complicated thing you’ve built with machine language?

**5:57** · Dave Plummer: That game would be. I mean, in assembly language, I’ve done a fair bit of complicated stuff, but in actual machine language, I think that game would be the only thing I’ve actually-

**6:04** · Lex Fridman: You literally built a game.

**6:06** · Dave Plummer: Not a great game, but it worked.

**6:07** · Lex Fridman: Okay, all right, and then you erased it?

**6:10** · Dave Plummer: I did.

**6:10** · Lex Fridman: All right. When did you first fall in love with programming? When you figured out, like, this is a, this is something special.

**6:18** · Dave Plummer: … I think there was two stages for me. I always knew immediately that I was fascinated with these machines, from the TRS-80 Model I. It’s all I wanted to do was ride my bike back there and have more time with it. And I did that, you know, to wear out my welcome as much as I could. And the other revelation came, I think about second or third year of university when I realized, “I love programming, but I have no idea what I’m going to do. Am I going to make the 12 flash on a VCR somewhere? Or am I going to go work on an operating system? I have abso- absolutely no idea what I’m going to do post-graduation. But I love what I do.” And so, I think that was a lot of consolation. It’s like, it doesn’t really matter what I’m doing at this point, ’cause I kind of love doing it, so…

**6:54** · Lex Fridman: So, you’ll figure it out. As long as you’re following this kind of feeling that’s telling you-

**6:58** · Dave Plummer: I knew I was in the right area, finally. Yeah.


### Dropping out of high-school

**6:59** · Lex Fridman: Yeah. All right. You dropped out of high school.

**7:02** · Dave Plummer: Yeah. Not the smartest move.

**7:03** · Lex Fridman: Okay. But you ended up going back to school and being very successful at school and, just in general, successful as a programmer, as a developer, as a creator of software. How were you able to find your way? Can you tell that journey of dropping out— …and then finding your way back?

**7:21** · Dave Plummer: There’s no moment when I dropped out. You just go less and less and less until you realize it’s going to be embarrassing if I show up because I haven’t been there in a long time, and then pretty soon you’re just not going, and that’s how you drop out of high school. So, if you find yourself on that path, stop doing that. But that’s precisely what I did. And so now I’m not at school and I have to get a job, so I’m working at 7-Eleven and a paint warehouse and stuff like that. And 7-Eleven is actually kind of an interesting job because it’s a job I think they keep rotating for people that are smart enough to do the night shift with all the accounting and the administration and stuff they make the night shift do, but that have reasons personally that they need to work at 7-Eleven.

**7:56** · Dave Plummer: And I was one of those people because I had no high school diploma.

**8:00** · Lex Fridman: What are some memorable moments from that time at 7-Eleven? Or maybe what do you appreciate about the difficulty of that job?

**8:09** · Dave Plummer: Probably the worst moment for me… I mean, I got held up at knife-point and stuff, and that’s all entertaining, but the worst… …The most… The suckiest part for me was doing the gas dips. We’ve got a long… It’s a, like a 15 or 20-foot wooden stick and it’s measured in gradients of inches and feet, and you drop it into the gasoline tanks and then you bring it up and you measure where the gasoline sits because there’s no electronic sensor. So, I’m doing that, and the first time I do it, I drop the pole and I re-grab it. Well, that’s about a thousand splinters of wood into your hands, and it’s 40 below out and that really sucked.

**8:38** · Lex Fridman: Oh, wow.

**8:39** · Dave Plummer: And I realized, “I don’t want to do this for a whole life.” I knew that, so…

**8:44** · Lex Fridman: Okay. So you stand there frozen with splinters in your hand.

**8:47** · Dave Plummer: And at some point, I have a revelation about my life that next time I’m going to do it differently. And then how ludicrous that is hits me about three seconds later, right? And I think that was really the moment for me where I realized that I’ve got to do something different. And so even though I was 21, I went and I talked to the principal of my local high school and I was like, “Can you let me back in?” And he’s, “No, you’re too old and we don’t have room,” was his main reason. And I said, “Well, between now and then, somebody’s going to drop out. So, you’ll have room. So, let’s assume you have room. Can I come back?” And he was gracious and let me come back. And so I did the three or four classes that I needed.

**9:24** · Lex Fridman: Yeah, just if you can linger on that, the slow dropping out. That’s a weird thing that you can do with your brain. You realize to yourself that you don’t have to do the thing that everybody else is doing, and that’s a dangerous realization because, like, you kind of have to be part of society to do certain things.

**9:44** · Dave Plummer: Right.

**9:44** · Lex Fridman: And if you realize you don’t have to do what everybody else is doing, you can either have an incredible life or a really difficult life.

**9:54** · Dave Plummer: Well, the problem with that process is you’re making a much smaller decision. “I’m just not gonna go to class today.” And that’s all you’re deciding, but you do that enough times, you’re making a much bigger decision. And that’s the problem.

**10:04** · Lex Fridman: So it’s better to make… If you want to live life in a non-standard way, it’s better to make the big decision explicitly and then you can stop going. Don’t allow yourself to make the slip-ups, though.

**10:15** · Dave Plummer: It’ll be made for you eventually.

**10:17** · Lex Fridman: Okay. Well, you got back, and you eventually went to college and were very successful as a student, and you weren’t that good of a student before.

**10:24** · Dave Plummer: No, I was a terrible student in high school, and even my first semester of college, I still wasn’t taking it quite seriously because I got mercy passed in Geometry 90, which is like the makeup class for the Geometry 12th-grade class that I didn’t have. And that scared me because I realized by 1% or the grace of the professor that let me through, I just about ended my entire university career here. So, fortunately, those marks don’t count on your transcript because they’re remedial classes. So, I got kind of a fresh start the next semester and did it for real, and I did it for me, and that made all the difference.

**10:55** · Lex Fridman: What can you speak to maybe by way of advice on how to be successful as a student?

**11:00** · Dave Plummer: Well, ideally, there’s some aspect of school that you do enjoy, whether it’s art, whether it’s computer science, whether it’s shop class, whatever. So, go for those classes and just put up with and do the hard stuff because it’s way easier than having to do it later, and that’s easy to say when you’re 50-something. It’s harder to say when you’re 15-something, but— … it makes a lot of sense.

**11:20** · Lex Fridman: All right. What’s the story of you joining Microsoft? How did we get there from 7-Eleven to Microsoft?

**11:27** · Dave Plummer: Yeah, it’s a big jump. So, I had gone back to school, and I think it was in my third year of university. I was working for the phone company for the summer as a summer job, and I’m doing conversions of their UBNet to TCP/IP and modern networking, which really amounts to swapping cards but then figuring out why their config.sys doesn’t allow Lotus to run anymore because it’s got 10K less than it used to, and it’s just a horrible time to be working in computers, but I was doing it. And at lunch, I’m sitting in the food court with the old and the bored, and I’m reading a book that I had bought called “Microsoft or Bill Gates and the Making of Microsoft Hard Drive,” I think is the title. And it’s a great book.

**12:02** · Dave Plummer: It’s just sort of a matter-of-fact history of how Microsoft came to be, what it’s like, how it operates, what the people are like there. And I’m reading this book, and I become really entranced by it and fascinated because it sounds like exactly the place that I want to be, but I’m in Saskatchewan, so what am I going to do about it? And what I wound up doing was, I had put myself through school with a program called HyperCache, which is a file system cache for the Amiga because the Amiga didn’t have any out of the box, and it had done reasonably well.

**12:29** · Dave Plummer: So, I went through my registration cards, because in those days you had a four-by-six card that people had to fill out with their name and their address and, if they had an email, their email, and they’d send it in, they’d get notifications of updates and so on. Well, it’s shareware. And I went through the whole stack looking for anybody with a Microsoft email address, and I found maybe three or four people, and I just cold-emailed them and said, “Hey, I’m an operating system student in Saskatchewan looking for an opportunity.” I don’t remember exactly what I said.

**12:54** · Dave Plummer: But one guy, Alasdair Banks, he wrote back and he said, “I know somebody that I can put you in contact with.” And he put me in contact, I think, with a guy named Ben Slifka, who did a phone interview, who eventually wanted to hire me to work on MS-DOS for the summer. So, that’s how I got there.

**13:10** · Lex Fridman: You put yourself through school by… Tell me about HyperCache. You built a piece of software-

**13:15** · Dave Plummer: It’s the weight loss program for hard drives.

**13:17** · Lex Fridman: That was sufficiently useful to a large number of people that would somehow give you money?

**13:24** · Dave Plummer: Yeah, it made decent money. I mean, I sold a couple thousand copies. At 20 bucks a copy or 40 bucks a copy, depending on the rules.

**13:29** · Lex Fridman: What program, what language was it written in?

**13:31** · Dave Plummer: C. So there were some assemblers. The actual really tight code to do the real work of transferring data to and from the cache was 68,000 assembly. Everything else was C.

**13:40** · Lex Fridman: Okay. This is like file system I/O?

**13:43** · Dave Plummer: Device block I/O. So any block that gets serviced from the drive would go through my cache first, and it was an N-way associative cache, and so it would try to match the geometry of the drive and do pre-fetch based on you’re trying to read a whole track at one time, that kind of thing.

**13:57** · Lex Fridman: What was it like trying to get your software out there at that time? How were you able to find customers?

**14:05** · Dave Plummer: Yeah, it’s interesting. I think I started on Usenet and some of the Amiga forums, posted, “Here’s my trial version, try it out for 30 days, see what you like.” And eventually it got picked up by a few retailers, and I remember I was with my… Now wife in her car, and she had a cell phone, because her dad was very concerned about her safety. And so this is late ’80s, and she’s got, you know, the antenna on the roof and the big box in the trunk, the whole deal. But we got a call from one of the software retailers that wanted to buy 50 copies at… 20 Bucks, which to me is a thousand bucks, which in 1989 or whatever year it is was a big deal. And so eventually a number of companies just bought inventory.


### Joining Microsoft

**14:41** · Lex Fridman: Let’s go to that time. It’s such an interesting time with Bill Gates and Microsoft. Why do you think Microsoft was dominating the software and the personal computing space at that time and, and really for many, many, many years after?

**14:52** · Dave Plummer: At the time, it was the single most potent assemblage of smart people that I’ve ever been a part of. And I’ve been in academia and I’ve been in industry to a certain extent, and you know, when you’re working at a regular computer company, the one guy who actually knows what he’s doing, his smarter friend? He probably works at Microsoft. So when you get there, you’re the big cheese from your small town, you think you know a lot, and all of a sudden, you’re just in an environment where, like, “Uh-oh, I’m just not going to speak because I don’t want to look stupid.”

**15:20** · Lex Fridman: Okay. What about Bill Gates himself? What are some qualities of Bill Gates that you think contribute to the success of Microsoft?

**15:28** · Dave Plummer: I think he was relentless in the pursuit of his one dream, which was his old slogan of a computer in every home and a computer on every desk. It was his special interest, and he was a smart guy, super determined, and he hired people that were as smart or smarter than him to help him execute it. And he built an almost unstoppable machine of intellect to go forth and make, let’s say, very simple products. MS-DOS is not a complicated product by any stretch, but it’s exactly what the market needed at that time.

**15:56** · Lex Fridman: MS-DOS changed the game. And that’s actually the team you joined, the MS-DOS team, and I think you joined before Windows 95. Was released. So tell me about the story of MS-DOS. Its success is probably pivotal to the success of Microsoft.

**16:18** · Dave Plummer: Before DOS, they were largely a language company, so they had made BASIC for a lot of computers, and they had a Fortran compiler and a Pascal compiler, that kind of thing. But their deal to have MS-DOS included with every version or every instance of the PC effectively set them as a standard that they were able to leverage for decades going forward. To a certain extent, they lucked into that, and on the other hand, they were smart to have done it. They didn’t charge IBM a lot of money for it, but making it a standard really played out to their advantage over time.


### MS-DOS

**16:51** · Lex Fridman: So at that time, MS-DOS, no graphical interface. Can you just speak to what the heck MS-DOS is?

**16:57** · Dave Plummer: It’s largely a command launcher. So you type in a name of a command, it looks it up to see if that’s in the current directory or on a special path of folders, and it loads it into memory and executes it if it’s there. And that’s 90% of what MS-DOS does. Now, it has environment variables and some complexity and a small scripting language built in, but it is basically just an operating system shell that allows you to use the resources of the computer, like the hard drive or the CPU, and it doesn’t allow you to multitask. There’s no graphical interface. Now, Microsoft did a- add a text-based graphical interface for things like an editor and QuickBASIC in DOS 5.0, I believe, and there was a DOS shell, which was sort of a graphical file manager in MS-DOS 4.0.

**17:38** · Dave Plummer: So they experimented with it, but it’s largely a command prompt.

**17:42** · Lex Fridman: Does it have the ability to communicate with external devices, so drivers and all that kind of stuff? How expansive of an operating system was MS-DOS?

**17:52** · Dave Plummer: Well, it was limited by the original x86 instruction set, which limited it to 640K. And then there were various Band-Aids on top of that to do high mem and then extended memory beyond that, and a lot of hoops have to be jumped through to make anything work without consuming base RAM.

**18:10** · Lex Fridman: Yeah, I mean, you programmed on MS-DOS. What’s it like? What are some interesting details there? Like you said, there’s the memory constraints of 640 kilobytes.

**18:20** · Dave Plummer: Yeah, 640K is the maximum that’s ever gonna be available, so it’s not what’s available to you as an operating system developer, because whatever you use is what the user won’t get. So if you use 10K needlessly, you’re gonna… Every machine in the world now has 10K less, so it’s kind of a big responsibility.

**18:35** · Lex Fridman: Is that a true quote from Bill Gates, where he said,

**18:38** · Dave Plummer: Nobody will ever need more than 640K? Yeah, no, it’s not him. It’s been attributed to him, but not real.

**18:43** · Lex Fridman: What are some interesting aspects of what you were able to do as an intern and when you joined on MS-DOS and beyond?

**18:52** · Dave Plummer: One of the first things I did was to take SmartDrive, the disk cache, ’cause I had familiarity with disk caches- and to add CD-ROM caching to it, because that was new. CD-ROMs were just coming out. Microsoft Bookshelf is one of the few products you could run for it. And as you can imagine, caching a CD speeds it up by dozens of times if you’re smart about it. So it was a big performance win and a nice thing to work on. A bigger part of that was moving a bunch of SmartDrive and eventually the double-space compression engine up into what’s known as high memory.

**19:19** · Dave Plummer: And without rat holing on the technical aspect of it, on the x86, there’s something I believe called the A20 line. And I probably have this backwards, or I got a 50-50 shot at it, but if you’ve got the A20 line asserted, then your memory pointers wrap at the one megabyte mark.

**19:34** · Dave Plummer: And if not, they don’t. So you continue going up in memory. So you can rewrite memory above by combining your segment and offset registers to a number bigger than one megabyte, and you get an extra 64K. And you put your code in there, and then you just put stubs to jump to it from low memory. And so you can get another 64K out of the machine that way, and we did that for a couple of the products. And that’s … I had no idea what HIMEM was, ’cause I was an Amiga programmer and I’d never written any x86 code before I got there, so …


### Windows 95

**20:02** · Lex Fridman: So that was, like, a cool optimization you got to be a part of. So what about Windows? There was a parallel development of Windows 95, right, at that time. Did you get a chance to interact with those folks?

**20:12** · Dave Plummer: I actually worked on Windows 95 for about three or four months. I was on the COM/OLE team doing the presentation cache, which is when you insert a, say, a Word or an Excel spreadsheet or chart into a Word document. You don’t want Excel to have to be loaded to render it every time, so there’s a presentation cache of enhanced metafiles and I was working on that. So that shipped in Windows 95, but I moved to the Shell team about six months after getting to Microsoft, and so I worked on NT from there forward.

**20:38** · Lex Fridman: Okay, and what’s 95? What’s NT?

**20:40** · Dave Plummer: Windows 95 is an evolution of the original 16-bit Windows 3.1, which was the very first popular version of Windows. And it adds 32-bit support, then VxD drivers and a bunch of new technology and an entirely new user interface. And it’s something that at the time was revolutionary. The people lined up at night to wait in line to buy the thing.

**21:00** · Lex Fridman: Can you just take us back to that time and describe why 95 was such a big leap from 3.1? So Apple already had a graphical interface. Windows 3.1 had a graphical interface. Why was Windows 95 such a gigantic leap?

**21:17** · Dave Plummer: I don’t want to make it as basic as the Start menu, but I think… …It’s a big part of it. I know when I first saw it… …I couldn’t quantify what about it was different and awesome, but I realized that I wanted to be a part of it, and that’s why I started writing a Shell extension, which became Zip folders at some point. But I was just fascinated by the new Shell, and that’s why I wound up working on the team that brought that Shell over to the NT and what’s Windows today.

**21:39** · Lex Fridman: Would you say that’s the greatest operating system ever? What’s the most impactful operating system ever?

**21:46** · Dave Plummer: Windows 95 would be number two for me. I think OS/360 is going to be number one.

**21:50** · Lex Fridman: Okay, interesting.

**21:51** · Dave Plummer: Because you could take a machine and write a COBOL program for it in 1962, jump in your time machine, go to Poughkeepsie and boot up an IBM z17 mainframe and run it today. And they’ve been doing it for however many years that is. And it’s all on the business side, so we as consumers don’t have much access to it, but I think it was probably as influential in the commercial side as Windows 95 was in the home side. And then probably Linux would be number three for me. I put Linux as bigger than Unix, which doesn’t work because you can’t have one without the other, but the impact of Unix, BSD, and so forth, is largely in the academic space. It’s by programmers for programmers.

**22:29** · Lex Fridman: So, yeah, Linux created… I mean, it was the embodiment of the open source spirit at its largest scale. Right? So it almost created a community and it created a spirit of programming that propagates to this day. That’s true. That’s true. Like scale matters.

**22:51** · Dave Plummer: Yeah, and its penetration on the server side of things now is, I don’t know if it’s equivalent to what System/360 achieved, but it’s almost ubiquitous, so…

**22:59** · Lex Fridman: Yeah, the world… I mean, this is the quiet secret of the universe, is it runs on Linux. Okay, so tell me about your work days. What were they like back then? Back in the MS-DOS and Windows 95 days? Take me through a productive day.

**23:17** · Dave Plummer: Well, your day starts coming in and you’ve got to download the address book, which is… Microsoft has between 10 and 15,000 employees at this point, and we’re all on MS Mail. We’re just getting off of the PDP-11 called Miss Piggy, which ran Whizmail, and we’re running MS Mail. But MS Mail has a fixed address book that every user must download every morning, and when there are 10,000 people downloading 10,000 people, it gets pretty messy. And I think we were on 10 megabit networking at the time, so your first hour is downloading the address book, which was always frustrating. But you’d use that time to look at the crashes that would have happened overnight from a process we called Stress, which is NNT…

**23:53** · Dave Plummer: All the machines that are unused run tests all night long and they try to crash themselves, and if they manage to crash themselves, it will drop into a debugger with a serial cable to another machine and you can connect to that other machine and remotely debug the crashed machine. So you come in and they will have triaged bugs, you know, there was a crash in the Start menu, so we’ll assign that to Dave, and so you come in and that’s your first thing, is to connect, because you’ve got to get that machine back to the guy that owns it and unlock the machine, so that’s your first hour of your day, is basically triage for bugs that have come up from Stress overnight and then at that point it’s probably back to coding, which unfortunately 80% of the time is fixing bugs, especially in my career it

**24:31** · Dave Plummer: was porting code and fixing bugs. I wasn’t writing a lot of new code and there were exceptions. I wrote a lot of new code on the side to get it out of my system… …From a day-to-day grind of always fixing bugs in other people’s code, which is amazing learning experience.

**24:46** · Lex Fridman: So you did a lot of the… At Microsoft, you did a lot of the porting of what is it, Windows 95 code to NT?

**24:53** · Dave Plummer: Yeah. We took the entire Windows 95 user interface, and we ported it to NT, which meant making it Unicode, for one thing. So everything that was eight bits is now 16 bits.

**25:02** · Lex Fridman: Okay.

**25:02** · Dave Plummer: …pointers. It’s quite a mess when you switch the code over, as you can imagine.

**25:07** · Lex Fridman: Can you give us insights into what is involved in porting?

**25:12** · Dave Plummer: It’s like breaking into somebody’s house and going through all their stuff and seeing the stuff in their drawers that they didn’t want you to see. You find all the good stuff, the pretty pictures hanging on the wall, and you find some disturbing stuff in the nightstand. I saw code that was like 200 characters wide with, you know, profanity and swears in it. It eventually got all cleaned up over the years by the time I left. But it was not always the most professional code in the world.

**25:37** · Lex Fridman: Right, because every single piece of code you have to go through.

**25:40** · Dave Plummer: Line by line, so you see it all.

**25:41** · Lex Fridman: Yeah. I mean, that’s the story of programmers. You write a piece of code, and you think it’ll never be seen by anybody. And sometimes, oftentimes, that code is going to be seen by a very large number of people, …that come after you, including you five years later. You yourself looking at your own code. Okay, so tell me about Windows NT. That was a giant leap too.

**26:06** · Dave Plummer: It was. It was basically a clean-sheet design. So they went and they got Dave Cutler from Digital Equipment, who had done operating systems for them, VMS and RSX-11, he had done. And so he came over after, I believe it was Prism and MICA were some projects at DEC West that got canceled. And so you had a whole team of guys where their project is canceled, and basically, they took a whole bunch of them and came to Microsoft. And I don’t know the specifics of the deal, but they all showed up. So you had Dave Cutler and Mark Lucovsky and all these really smart guys from DEC, and they did basically a clean sheet, but they also had OS/2 as a starting point. But OS/2 was, of course, written in assembly language, and NT is going to be written in C.

**26:46** · Dave Plummer: So to what extent they were able to leverage any of that, I don’t actually know, but at least they had a system to start with.


### The man behind Windows

**26:53** · Lex Fridman: You said that Dave Cutler’s the man, the mind behind Windows. Can you explain?

**26:59** · Dave Plummer: So Dave Cutler is the architect of the kernel. So he is Linus in the Linux world. It’s Dave C. in the Windows world.

**27:06** · Lex Fridman: Yeah. Dave C., okay.

**27:07** · Dave Plummer: And it’s not that there weren’t other people that contributed, of course, huge pieces to it. But I think he’s the driving force behind it and always largely has been. And he’s still… I think he’s 85 now. He still codes every day. He’s a Microsoft Fellow. He, as far as I know, still goes into work, so…

**27:21** · Lex Fridman: Can you speak to the genius of that guy? Like, what’s interesting about his mind, having worked with him, having interacted with Dave Cutler?

**27:30** · Dave Plummer: Well, the dude’s wicked smart, but he’s also like a farmer. He’s like the guy that will follow you around and make sure that stuff gets done and gets done right to make sure that you’re not checking any crap into his operating system. And he won’t tolerate it. And he’s a real taskmaster in that regard, but I think it really paid off ’cause it was a very big paradigm shift for Microsoft developers to be subjected to the Dave Cutler Digital Equipment style of leadership.

**27:55** · Lex Fridman: What did you learn from that about successful software teams, where there’s a large number of people collaborating? Because Microsoft had a lot of brilliant engineers back then, and like you said, Dave Cutler. They had to they had to create completely new systems, many of which we still use today. What have you learned about great software engineering teams from that time?

**28:21** · Dave Plummer: Tools are everything, I think, for one. And people are everything. We’ll grant that. But the tool set is a huge factor. If we went ahead with Git, it would have been immensely easier. We were using Diff and, you know, manual Deltas. …To do this porting and stuff. So being able to fork a branch of source code would be a luxury that is new to me. At the time, it would have been really handy.

**28:44** · Lex Fridman: What were some memorable conversations from that time when you walked over next door-

**28:49** · Dave Plummer: Well, what…

**28:50** · Lex Fridman: … and talked to some of these folks?

**28:50** · Dave Plummer: …I was not present for was, somebody was complaining, a new hire came into the team and was working on what I believe was called Cairo. Cairo was going to be the next future operating system, was going to be beautiful, and have a whole new user interface newer than Windows 95, and it never materialized. But while they were working on it, one of the guys working on Cairo was kind of flaming on the open NT dev alias, which is thousands of people, how shitty the NT boot experience was. The response that came back was an epic flame that I wish I would have saved, and I won’t name the guy who wrote it. He knows who he is, but… … It was a work of art of angry flame mail, kind of like the ones you see Linus send every now and then about kernel stuff. So it’s a very similar sentiment.

**29:32** · Lex Fridman: Were there, like, kind of intellectual debates, like-

**29:35** · Dave Plummer: Oh yeah.

**29:35** · Lex Fridman: … there’s some, some heated stuff with the engineers?

**29:38** · Dave Plummer: It was… Yeah, it got contentious. So you’ve got intellects competing, and eventually, the technical merits for some people are secondary, and it’s about besting the other person in that argument. And it’s no longer productive at that point half the time, but there was a fair bit of that.

**29:53** · Lex Fridman: Yeah, I’ve seen those kind of debates in programming language design communities, like Guido van Rossum, the leaders of those communities, it can wear them down because people get… You almost forget the mission you’re on and start being very nitpicky about the details. I mean, engineering minds get together, and you just go to war over the stupidest, like, syntax subtlety.

**30:20** · Dave Plummer: Right.

**30:20** · Lex Fridman: Well, I shouldn’t say stupid, but it’s a small syntax subtlety for programming language. I’m sure there are internal battles about specific kernel components.

**30:32** · Dave Plummer: Yeah, I mean, there’s one that I lost that still bugs me to this day, I think.

**30:35** · Lex Fridman: Okay, yeah. What’s that?

**30:38** · Dave Plummer: ‘Cause I still think was right. Well, when we were doing the shell, we were porting everything from ANSI to Unicode, so every character that was eight bits now becomes 16 bits. Now, the problem is I’m on a MIPS box ’cause I’m porting it to RISC…. and you can’t have unaligned addresses. But if you take two ID lists, which are basically past components, you take the one for C colon backslash, take the one for Windows, take the one for System32, and you add them together. But if you’ve got an odd number of characters, now you’re at an odd address in this thing, and it takes me an immense amount of work to turn on exception handlers, to do unaligned byte access, to pull the string out and copy it manually.

**31:11** · Dave Plummer: And it’s literally like a hundred to a thousand times the amount of work to read a string out of this ID list on a MIPS machine because it’s unaligned. So I’m having the argument that even though it’s late in the Windows 95, they’ve already shipped one beta, that we should now just guarantee that ID lists are always an even number of bytes, or do some hack to just make sure this never happens so the code that references them on all this hard work can just blaze through it. And it became a shouting match and sort of a personal match and I lost that one. And I still think that, I know today, that that code running on Windows is thousands of times slower than it has to be and it- nobody cares ’cause it’s plenty fast but- …it could be a lot faster.


### Debugging

**31:49** · Lex Fridman: Yeah. So yeah, I mean you mentioned MIPS and RISC. How deeply did you have to understand the lowest level? Sort of the lowest level of the software and even the hardware with the stuff you were building. Like what are the layers of the abstractions you had to understand to be successful with all the stuff you’re doing with NT and before that with…

**32:12** · Dave Plummer: Well, about half your day is going to be spent debugging, and most of the time is going to be spent in call stacks that are in pure assembly language because there’s no source level debugging. So it’s not like we’re in Visual Studio, and you hit a breakpoint, and it pops up, and there’s the source code. You can go look at the source code, but you’re looking at the raw assembly dump from the machine at all times.

**32:29** · Lex Fridman: So even if you’re programming in C, the debugging is in assembly?

**32:33** · Dave Plummer: Yeah, 100%.

**32:34** · Lex Fridman: Oh man.

**32:35** · Dave Plummer: So it’s a little cumbersome.

**32:36** · Lex Fridman: Oh.

**32:37** · Dave Plummer: And better yet, we’re doing four instruction sets because we’re doing Intel MIPS, Alpha, and PowerPC. So depending on which machine it crashes on, you’ve got an entirely different instruction set… …That registers. And so you get reasonably adept at debugging all four, but I had more experience in MIPS, so MIPS stuff would come my way.

**32:54** · Lex Fridman: That’s a real endurance event. I mean, can you speak to that? The torture there is debugging, especially that kind of debugging without the tooling associated with it. I mean that’s, you know, programming, kids these days, programming isn’t all about creating beautiful things, right? It’s also about fixing things.

**33:18** · Dave Plummer: Yeah, I would say that 20% of my professional life has been creating and 80% has been debugging and fixing. And I mean, I got a bit of a reputation as somebody who could fix stuff, and so stuff like that would flow to me, and so I would spend more time doing that. I wasn’t renowned as a creative UI genius where I’m flowering all these new ideas. So I got to fix ugly stuff, but you get really good at that. So I don’t mind it until it’s one of those things where you’ve been chasing it for so long that you don’t know what to do next and you can’t understand why it doesn’t work or how it ever worked or whatever situation you happen to be in, and you know, after a day of it, it can get pretty trying.

**33:52** · Lex Fridman: Yeah, debugging can be real torture. It can be really, really difficult. There’s a psychological component, I think, of perseverance.

**34:00** · Dave Plummer: I think the ones that, you know, take you a day, they resolve one of two ways. Either it’s like, “Oh, extra semicolon,” and then you finally see it… …Or it’s some horrible manifestation of cross-threaded apartment nonsense that was really hard. But it can go both ways. I had a bug. It wasn’t my bug, actually, but it was a manifestation of a bug in Task Manager where every now and then it would say greater than 100% total CPU usage, and this looks pretty silly for a task manager. So I had tried to resolve it for a long time, and I’d talked to the kernel guys about my issue, and they were unsympathetic, let’s say, because the kernel guys are a special breed, and they weren’t interested in my user land problems. “It’s probably some issue in my code,” right?

**34:40** · Dave Plummer: And they’re probably right, but it wasn’t in this case, and I was sure of it, and so I kept adding asserts all through the code to make sure that the preparatory steps of adding the stuff together were never more than 100, and that the final sum was never more than 100, and finally it never asserted. But occasionally we would get this bug where people would still see it, and so I finally put my phone number in the assert, and I was like, “If you see this message, call DavePL at 425-836,” my phone number. And finally, we did get a catch in the actual stress debugger that I was talking about earlier where it happened to somebody with a debugger connected.

**35:16** · Dave Plummer: We were able to go through, and it was actually a kernel accounting issue, and it wasn’t a Task Manager issue, so they just fixed it in the kernel once I was able to prove that it was in fact a kernel issue. And you’d think we would then remove my phone number, but we just commented it out, so it’s shipped, and it’s in all the damn source code leaks for NT that are out there, so…

**35:32** · Lex Fridman: That’s awesome.

**35:32** · Dave Plummer: …that’s how I find Task Manager code. I search for my phone number on Google, and it will reverse-find…

**35:37** · Lex Fridman: Oh, yeah, that’s fantastic.

**35:38** · Dave Plummer: …the NT source code.

**35:39** · Lex Fridman: Can you speak to the assert thing? By the way, I saw, I think you tweeted or you said somewhere that if you want to take your asserts really seriously, you add your home phone number in there. It’s true, it’s true.

**35:49** · Dave Plummer: A little facetious, because it’s probably not the smartest thing, but…

**35:51** · Lex Fridman: No, it’s not.

**35:51** · Dave Plummer: …you will find out.

**35:52** · Lex Fridman: But I mean, assert by itself is already a serious thing, because it stops all execution. I mean, this is one of the reasons I really, really love asserts, because they stop everything and force you to take care of the problem.

**36:07** · Dave Plummer: Yeah, I’m a little religious about my asserts too. I don’t assert things that I hope aren’t true. I assert things that I know cannot be true, and I think that’s really the intent of an assertion. So I’m overstating the obvious, but when it does occur, it’s a bug, plain and simple. It’s not a warning.

**36:21** · Lex Fridman: It’s kind of fascinating how often it can really help you figure out the problem, because if you put asserts everywhere, you can get very quickly to the source of the problem.

**36:34** · Dave Plummer: Yeah, I tend to… it’s not something I want to suggest you go back and add later. It’s something you should do organically as you build your code.

**36:40** · Lex Fridman: As you’re building.

**36:40** · Dave Plummer: So for each function, if you’ve got assumptions like, “I know that this pointer is never null,” well, assert that. If you know this count is always less than twice the byte width, assert that. And don’t be afraid, because if it asserts, it’s doing you a favor. I think some people are afraid. You know, it’s like when you turn out of an intersection, and you think maybe there’s somebody coming, and you don’t look left. Or maybe I’m one to do that. But it’s like that. People don’t assert because they’re afraid they’re going to fire. Well, no, you want to know.


### Task Manager

**37:05** · Lex Fridman: You mentioned Task Manager. Obviously, we have to talk about this, the legendary program that you created, the Windows Task Manager. Tell me every detail of how you built it. What is Windows Task Manager?

**37:18** · Dave Plummer: So Windows Task Manager is a way to go in and find out which apps on your system are using the computer, using the hardware, using the CPU, using the memory, and which ones might be using too much or locked up or going crazy. And it gives you the ability to terminate and kill those ones. So it’s an inspection and a fixing tool.

**37:34** · Lex Fridman: Yeah, it lists all the processes. I mean, it’s a legendary piece of software. It’s crazy. You just take it for granted. It’s like the Start menu, right? It’s like genius.

**37:44** · Dave Plummer: Well, I had the great fortune of working on a lot of things that people are familiar with. And Task Manager was one of those side projects that I started as something that I wanted for myself and eventually came in-house. So I started writing it at home and I got the basics up and running. I was using, I think it’s HKey Current Performance or HKey Performance in the registry to get the stats because I didn’t have access to the internal APIs because I was working from home and I don’t call those if I’m working from home.

**38:08** · Dave Plummer: And when I brought it in-house then I was able to call things like NtQuerySystemInformation or NtQueryProcessInformation and get the real answers very quickly, which enabled it to become a very fast and responsive app. So people have come to rely on it because I wrote it to be as reliable as possible. I wasn’t worried about the features. It was a basic set of functionality that I wanted in there. I got everything I wanted, but I wanted it to be really robust. And small. And the original was like 87k.

**38:35** · Lex Fridman: Okay, can you speak to what it takes to build a piece of software like that that doesn’t freeze?

**38:40** · Dave Plummer: You don’t assume much, right? If you’re going to call the shell to run an app, well, that could be a network path that’s on a TCP/IP share that takes 90 seconds to time out. So anytime you do any kind of API call like that, that could take time, you’re going to wind up doing it on a separate thread. And so the app becomes a little more complex because everything is multithreaded.

**38:59** · Lex Fridman: Okay, so what programming language were you working in?

**39:01** · Dave Plummer: C++.

**39:02** · Lex Fridman: So this was for Windows NT?

**39:04** · Dave Plummer: Yes.

**39:05** · Lex Fridman: Okay.

**39:05** · Dave Plummer: So this shipped initially in NT 4.0.

**39:07** · Lex Fridman: Okay, so what are some interesting details about this program? Because you have to get it as simple as possible, but also as robust as possible. What are some interesting optimizations, for example, you had to implement?

**39:20** · Dave Plummer: There are a couple of things that are a little hardcore now. I’m surprised I did. Like, I didn’t want to link to the C runtimes at all. So I made sure never to call a runtime call and I didn’t link to them, and that saved me whatever the C runtime is, 96k or something. So, it almost doubled the size of the app if you just touched any C call. So I was careful not to do that, but then I was actually writing in C++, which is C with objects more than anything. But in order to get it to work, I had to go through and call all the object constructors manually from the dispatch table and stuff because you don’t have the runtimes to do it for you.

**39:50** · Dave Plummer: So you’re working with a compiler that doesn’t have its runtime, and I don’t want to get off-topic on the technical issues, but it’s a lot of extra work to get it to work, but when you do, it’s incredibly small and tight.

**40:00** · Lex Fridman: That’s about the size- of the program. What are some interesting aspects of tracking down every process and how much CPU usage is in that process?

**40:10** · Dave Plummer: One of the cooler things that I saw is… I don’t want to say I invented Hamming code, but I kind of invented Hamming code without knowing Hamming code existed. So every column and every row in Task Manager has a bit on whether it’s become dirty or not, and then I can look, basically the same way Hamming code looks in your X and Y columns, to find out which rows have changed, go through, and find out which ones actually need to be repainted. So Task Manager is super efficient and it works in concert with the ListView control, which provides that functionality to go through and repaint as little as an individual cell that changes from frame to frame. So it could paint very fast, it can resize very smoothly, and resizing was probably my biggest personal goal with that app.

**40:51** · Dave Plummer: So you can size it to any size and it still works and even if you have 32 CPUs, which wasn’t possible in the day, it will draw, I think, only eight graphs and then it wraps but it still works today. So kind of proud of that.

**41:06** · Lex Fridman: It is incredible. You’ve gotten the chance to observe the evolution of Task Manager. In some ways, it really hasn’t changed much. Maybe there are some prettier aspects to it that fit into whatever version of Windows it’s in, but it’s really basically the same thing.

**41:23** · Dave Plummer: The functionality is very same. The reporting is more because they’ve added GPU and thermals and things like that, which is really nice to have. And we didn’t have that ability in the day, so…

**41:32** · Lex Fridman: I mean, what can you say? Do you know about, like, was there any refactoring done or is it basically the same code?

**41:37** · Dave Plummer: As far as I know, the original code’s still mostly all there so there are layers of drawing code and dark mode code and whatever else, XML, schema code, that goes on top of that that makes it four megabytes instead of 87k but that’s the world we live in, so…

**41:51** · Lex Fridman: Yeah, it’s one of those pieces of software you create and just stay once it’s there. It’s just really like the Start menu, and I’m sure if you remove it, people would just lose their mind.

**42:02** · Dave Plummer: Yeah, it might be locked in for a while, on that one. It might be good.


### 3D Pinball: Space Cadet

**42:06** · Lex Fridman: Yeah, I thought that would be true for Clippy, but Clippy will make it back one day. All right, what are some other pieces of software you created at the time that are legendary? So you were part of Space Cadet Pinball, at least porting.

**42:22** · Dave Plummer: Yeah, so they came into my office and said, “Hey, what are you doing?” And I told them what I was doing and they said, “Well, how do you want to spend your next three months?” And I said, “I have no idea.” And they said, “Do you want to port Pinball?” And I’d seen Space Cadet Pinball as a game standalone for the Win95 platform and it had a couple different tables and it was a cool game so I was kind of excited. What they wanted was some visual splash for NT to show that NT can do, for then, high-speed graphics or at least responsive graphics.

**42:48** · Dave Plummer: And so I took a shot, and unfortunately, a lot of the code was in Assembly, and I was on a MIPS, so I had to rewrite the code in C so that I could then port it to all the different platforms. At the heart of the game is a huge state engine, and it’s like a giant switch statement with, if I remember, like 50 entries in it.

**43:06** · Dave Plummer: And it’s got an Easter egg built in. And decoding the state, it’s like running a neural network through this thing as you hit it with different states. And I just put it aside and treated it as a black box. So my code runs on top of that and does the drawing and the sound and everything else. But the original game is still running. And somebody recently asked me why it is slightly different; the physics are slightly different from the Windows 95 version, but it should be the same code because I’m trying very hard to preserve that. But what it is, is I had a bug where I will draw as many frames per second as I can, which on a modern computer can be 5,000 frames a second for Pinball because it’s a pretty basic game.

**43:45** · Dave Plummer: And so all your physics are interpolated 5,000 times per second instead of 30 times a second, or whatever you would’ve got on the old one. So you’re getting arguably better, or at least different physics, but they fixed that since, so…

**43:57** · Lex Fridman: Why is that game so awesome?

**43:59** · Dave Plummer: I think it’s a great design. I mean, I take no credit for that. That’s all totally the guys at Cinematronics. But the original game is a great design. It’s very similar to Black Knight 2000, which I own as an actual physical pinball machine. And the layout is actually very similar. I don’t know if it was inspired by it or not. So it’s a good game.

**44:15** · Lex Fridman: Yeah. Sometimes I think about Tetris, about certain games with pretty primitive graphics that captivate the excitement of a large number of people. And maybe it’s the excitement of a large number of people that contributes to the awesomeness of the game. So when many people together get excited and talk about it, that sort of gets implanted into your head. But that’s one of the great games. I mean, even like Solitaire and Minesweeper. I mean, there’s just a generation of people that have gone to war in Minesweeper, right?

**44:48** · Dave Plummer: Well, those things were included in the OS not as games, but as educational tools to get you to use a mouse.

**44:53** · Lex Fridman: Oh, interesting.

**44:54** · Dave Plummer: So Solitaire is there to show you how to do drag and drop. And Minesweeper’s probably right-click. I think you put a flag or some item. I’m not a Minesweeper guy, but so each one of them teaches you something.

**45:03** · Lex Fridman: Minesweeper guy? That’s funny. Yeah. Wow, I didn’t know that. That’s interesting. And that’s true. But I don’t know how many hours I’ve spent on these games, and millions of people have spent millions of hours on these games.

**45:16** · Dave Plummer: I used to volunteer teaching computer science at my kids’ school, you know, for the third graders and stuff. So it’s more like logging in than computer science. But the kids, of course, all their dads work at Microsoft, so nobody’s impressed by anything you do. But so one of the kids found out I worked on Pinball, and then they were like, “Whoa, you worked on Pinball?” Because they all knew that in those days. Now the kids are probably aged out, they don’t know it anymore, but for a brief period.

**45:38** · Lex Fridman: You’re behind the Windows activation.

**45:42** · Dave Plummer: You say it like it’s a bad thing.

**45:44** · Lex Fridman: Everything’s a matter of perspective. So tell the story of that. What’s Windows activation? How’d you get involved?

**45:53** · Dave Plummer: So they came to me late in the XP ship process. I don’t know if the beta had gone out. I don’t think the beta had gone out yet, but they had intended to take the Office activation code and then adapt it to Windows and add activation to Windows. But whoever was responsible for doing it had slipped it enough times that it wasn’t going to happen. So I had kind of a reputation for being able to fix things quickly, so they came to me and said, “Can you get this done in time for XP?” “I don’t know, but I’ll try.” So with the help of the guys that were doing the DRM stuff on the DRM side and the research guys doing the math for the product keys and everything else, we cranked it out in time for XP.

**46:26** · Dave Plummer: And I don’t know what its actual impact is for revenue, but I imagine it’s substantial when you start enforcing license keys.

**46:35** · Lex Fridman: I wonder what it is.

**46:36** · Dave Plummer: I don’t know.

**46:36** · Lex Fridman: Because it’s also annoying.

**46:39** · Dave Plummer: It is, especially if you have to phone activate. And that was just the case that we had to carry with us as an albatross around our neck, where you’ve got to pass data up to the clearinghouse, the backend systems that are going to approve your key. You’ve got to tell it all your hardware parameters, like how much memory and hard drive space and the various things the hardware key is bound to, as well as the product key, and you’ve got it encoded in letters and numbers that somebody’s willing to read in over a phone. And if you think doing product activation is painful over the phone, could you imagine being the person that worked on the other end of that line? I mean, that’s just got to be a mind-numbing job to listen to product keys for eight hours a day.


### Start menu and taskbar

**47:13** · Lex Fridman: Yeah, one of the challenges with Windows, and it’s been a frustration point for me, but I understand from a design perspective it’s very difficult, is so many different kinds of people use Windows. But it’s been frustrating how over time Windows has more and more leaned into the direction of not the power user, I should say, which is why Linux has always been really wonderful. But from an activation perspective or from any kind of configuration, it’s been a source of a lot of frustration.

**47:49** · Dave Plummer: Yeah, one of my more popular episodes of late has been why you can’t move the Windows taskbar. And I had no idea, but the outrage is palpable amongst people that you—

**47:56** · Lex Fridman: Yes.

**47:57** · Dave Plummer: …just put it on the left or top and you can’t anymore, and it is an affront to their existence. And I understand it to a certain extent.

**48:02** · Lex Fridman: Well, it’s one of the main reasons I really just dislike Windows. There’s a lot of aspects about Windows 11 I dislike. One of which is like you can’t customize things as much about the position of the taskbar, just basic customization. Can we just configure stuff? Because there’s going to be a small contingent of power users that are just going to enjoy the hell out of this operating system if you just give them that option. It costs you nothing. Just give them that freedom.

**48:28** · Dave Plummer: Well, it does cost, right? Because the freedom to put the Start menu on the left or the top or the right really increases the complexity of the code that renders the Start menu and lays out the tabs and does all the things, and now it’s a much larger surface for bugs and it’s a much larger piece of code to maintain, so you probably need more developers or another developer or some portion of a developer’s time. So the question becomes at what point is it still worth it to satisfy the niche needs of a small set of users? Those decisions weren’t mine to make, but I could see it from both sides.

**49:04** · Lex Fridman: I think just like the people who make movies and insert very nuanced details that only a small number of people will realize are there, that’s going to really pay off. There’s a kind of reputation that builds over time that has a very powerful ripple effect. That I think it has so many benefits, including for hiring great software engineers. It’s like you create this aura of a place that puts love into every detail, that really takes care of the power users, that takes care of the developers, and I think Microsoft has more and more moved in that direction with GitHub and acquiring GitHub and just taking care of the developers. But on the Windows interface side, come on, some customization.

**50:04** · Lex Fridman: With VS Code, you can customize everything. Why can’t we customize the Start menu, all right? And the taskbar, and really every aspect of the Windows interface. I don’t know, maybe you’re right. Maybe it increases the complexity of the code. I suspect that’s just not the case.

**50:24** · Dave Plummer: I bet it was. I bet it was a scheduling decision when they rewrote the Start menu. I think they rewrote it because it’s different than the old taskbar.

**50:31** · Dave Plummer: And somebody was tasked with, “You’ve got to deliver this set of functionality, and if I cut out putting it on the left and the top and the right and two rows of tabs and all the other cool features, I can deliver it four months sooner.” And I’m not saying that’s the right decision, but I’m guessing that might be the kind of thing that motivates it. And they’re on such a different release schedule now. It used to be… You won’t see much craftsmanship unless somebody owns a component for a long time and it settles to a point that then you can work on and polish it, right? But if it’s always churning and the UI is changing every release, it’s never going to get that level of polish. Although I think the UI is pretty nice, but…

**51:06** · Lex Fridman: Yeah, it is nice, but I think it’s a craftsmanship thing. Just like you with the Task Manager, if there’s a guy or a girl in there who takes ownership of it, who has a passionate… For them, it’s a thing that they take pride in over a period of time, they can by themselves in a short amount of time create something truly wonderful.

**51:33** · Dave Plummer: Right.

**51:34** · Lex Fridman: And like, I think if you have large software engineering teams with managers and scheduling of meetings and all this kind of stuff, yeah, okay. Then your argument applies. But if you allow the flourishing of individuals that create cool stuff and their own sort of side project, which Google is very good at.

**51:55** · Dave Plummer: They’ve tried that, right? At Google, yeah.

**51:56** · Lex Fridman: Yeah, like have fun with it. Like do some crazy stuff and then we’ll integrate it. We’ll try to integrate it into the whole ecosystem. I don’t know. I don’t know, because to me, it’s such a great joy for an individual developer to create something like customization of the Start menu or the taskbar because you know that millions of people are going to use the taskbar. And then you know that thousands, tens of thousands of developers might be using to customize even little subtle aspects of the taskbar. You know how much joy you create, you give to people to customize, to have some kind of JSON thing where you customize something about the taskbar?

**52:37** · Dave Plummer: Okay, but how do you respond to the Steve Jobs aspect of giving you customization implies that we couldn’t figure out the right answer for you? Or maybe there is no right answer and all four answers are equally right. I have no idea, but…

**52:51** · Lex Fridman: Right. I think I’ve always— I’m glad Apple exists. It’s a beautiful thing, and that idea of design is wonderful, but I always thought that Windows creates the contrast. The point of Windows is to be the operating system that works on all kinds of devices, that’s supposed to be much more open. And they’ve moved towards that direction more and more with Windows Subsystem for Linux. It’s just this whole developer-friendly ecosystem. The interface should be in the spirit of that, I think. But I do think that there could also be security vulnerabilities created with that. It’s not just the complexity of the code, because Windows is just under attack.

**53:30** · Lex Fridman: It’s very difficult to keep it secure. Anyway, taking that tangent, you also developed ZIP file support for Windows, creating Visual ZIP, which eventually evolved into ZIP folders. Tell the story of that.

**53:44** · Dave Plummer: So that was a piece of software that I wrote at home again, and what happened was, I was out with my wife, and I think it was a Sunday afternoon. We were driving around. This is 1993, and we’re living in our apartment, and we’re just seeing what the housing market is like out there. And there’s a guy, he’s got this beautiful three-bedroom house and a Corvette convertible, ’93 red, torch red, parked in the driveway, and the house is for sale, and it’s like 300K, I think. And there’s no chance I’m coming up with 300K at that point, or even the down payment on that. So I took the flyer, and I cut the picture of the house out, and I taped it to my monitor. And that was my incentive to just write something at night, because when I came home, I was doing two things.

**54:21** · Dave Plummer: I was, one, expressing a creativity that I couldn’t get out at work when I was just fixing bugs, and I was trying to make some extra money. And so I wrote a Shell extension. Before I actually went to the Shell team, I started it, and that’s what led to my interest in going to the Shell team, based on an MSDN sample or MSJ at the time, an MSJ sample that I saw on how to, like, bring up a folder. Well, once I had the very basic bring up a folder template, adding ZIP file support to it was just incremental all the way. And I released it as a shareware product.

**54:50** · Dave Plummer: I think it was 19.95 or 29.95, and I sold, whatever, a couple of hundreds or thousands of copies. And one day, I’m getting ready for work, and I get a call, and it’s a lady, and she says, “Are you Dave Plummer?” I said, “Yeah.” She said, “Are you the guy that wrote Visual ZIP?” I said, “Yeah.” And she said, “Well, this is Betsy from Microsoft, and we’d like you to come by and come in and talk about an acquisition of it.” And I said, “Okay, what building are you in?” And she’s like, “What do you mean?” And I said, “Well, I’ll come by.” And she said, “Well, no, you got to talk to travel, and you got to talk to legal, and this all has to be set up.” And I’m like, “I don’t get it. We both work at the same place.” Why can’t I just stop by?” I don’t know if I said that literally—

**55:24** · Dave Plummer: …but it was a few minutes of back and forth where we both realized that she didn’t know I worked there.

**55:28** · Lex Fridman: Yeah, that’s funny.

**55:29** · Dave Plummer: They had just cold-called the author and then found out that it was me.

**55:32** · Lex Fridman: Yeah, that’s funny.

**55:32** · Dave Plummer: And so they made me an offer on it, and it’s the kind of thing where if I don’t accept the offer, well, now my choices are: I can keep selling my own version and quit Microsoft, or I can stop selling my own version and work for Microsoft. Neither of those is great. I mean, I’d like to keep my job, of course, but I’d like to still— …have this income stream. And the other option was accept their offer, which is what I did. So then I bought a used ’93 red Corvette, and…

**55:56** · Lex Fridman: And you got to continue building it internally?

**56:00** · Dave Plummer: I did. So we took a lot of features out, right, to simplify, because it had encryption, and it had a number of features that were common in ZIP programs of the day, but probably weren’t appropriate for Windows. And, at the time, encryption was like a munition, so you couldn’t just add encryption willy-nilly to various parts of the operating system, so we took out some things like that. Multi-volume support, I think, was taken out just to simplify it.

**56:23** · Lex Fridman: Can you speak to ZIP in general, just the history of ZIP and, you know, compression, that whole thing?

**56:29** · Dave Plummer: Yeah, it was really borne out of the BBS era when people were dialing in on modems to download trialware and shareware and other things from BBSs online and to compress them. Executables compressed about half their size. Other stuff compresses much more. But a guy named Phil Katz came up with a command-line program for MS-DOS called PKZIP, which was able to do compression of programs, and he has a rather tragic arc. But it became ubiquitous in the entire PC industry, and pretty much everybody was using it. So when Windows came out, there was no way to open up a ZIP file, but everybody had been creating them for a decade, and so that really drove the desire to have the ZIP support right in Windows.

**57:11** · Lex Fridman: Yeah, and that’s another piece of software that’s just kind of with us to this day.

**57:15** · Dave Plummer: Mm-hmm. And it could be vastly improved, but, you know, it was written in the single-core days, so it doesn’t do anything multi-threaded. And you’ve got a 96-core 7995, well, it uses one of them to unzip your file.

**57:26** · Lex Fridman: What other awesome things were you a part of at Microsoft? What other pieces of software?

**57:32** · Dave Plummer: I worked on the initial prototypes of Windows Media Center. So we did—

**57:35** · Lex Fridman: Nice.

**57:35** · Dave Plummer: …that in ’96, I believe. And we didn’t have, at the time, any sources, so we had like a CD of MPEG video files of Raging Rudolph and I think the original South Park video— …the Christmas one, which is all wildly inappropriate in the workplace today, but— it’s all the content we had until we got actually… We had them put a satellite dish on the roof, a DSS, whatever the 18-inch dish is, because we couldn’t get cable to the building. And so we built up this thing that would eventually look a lot like Media Center, and it was distance viewing UI for Windows, so you could sit with a remote control on a desktop and have, you know… The current Start menu is not great at 20 feet away.


### Blue Screen of Death

**58:13** · Lex Fridman: Tell me the story of the infamous blue screen of death.

**58:17** · Dave Plummer: What it is is when Windows has no other option, when the kernel gets into a state where something illegal has happened, so let’s say a device driver is trying to write to a piece of memory it doesn’t own or is trying to free a piece of memory twice, something that just cannot happen, and the kernel has no other option, it will shut the machine down to save your work. And… Well, not save, but prevent further damage, and it puts up a blue screen and it prints out the stack information, depending how your settings are. Sometimes it’s just a sad face. In the current Windows.

**58:46** · Lex Fridman: I wonder what the first version of Windows when the blue screen came to be.

**58:51** · Dave Plummer: So, Windows 3 had a blue screen- but it’s completely unrelated to the blue screen in Windows NT. And I talked to the guy who wrote the blue screen in Windows NT. His name’s Jon Viert, and the reason he picked white on blue, I had thought, I’d always heard it was because in the labs, you could walk through a lab where we have 50 PCs all running stressed. “Oh, that one’s got a blue screen. It’s—” “crashed.” It wasn’t that simple. It was just the MIPS firmware that he was building it on was blue on white, and Visual SlickEdit that he was using as an editor was also the same color scheme. And so you could code, boot, crash, and reboot, all in the same color scheme.

**59:25** · Lex Fridman: Why do you think so many problems with computers can be solved by turning it off and turning it back on again?

**59:34** · Dave Plummer: I think there’s two major things that happen with computers as you run them over time. One is memory gets used and not freed. And so it accumulates on the heap or in the swap file or wherever, and things get sluggish. And the other is, code gets into a state that the developers didn’t anticipate or didn’t test very well. And maybe that’s a rare state, but now that Notepad or Word or Excel is in that state, your system is goofy. So if you just reboot the thing or shut it down or restart it, you’re getting a fresh state and there are no memory leaks, so it covers a lot of sins, basically.

**1:00:03** · Lex Fridman: And the intricate ways that several pieces of software in a goofy state interact with each other creates sort of a meta goofy state that just the entire system starts acting a little weird. And then somehow fixes it. What are some of the best and the worst code you’ve seen during that time at Microsoft? What’s some beautiful code and what’s some ugly code that pops to memory?


### Best programmers

**1:00:31** · Dave Plummer: In terms of beautiful code, there’s two that stand out for me. One is the kernel in general. When you get down into the Windows kernel-

**1:00:38** · Dave Plummer: …in the actual NT APIs and stuff, it’s very well written, and it’s written to a standard that you don’t see on the user side, or at least is uncommon on the user side. On the user side, probably the coolest code I remember seeing was a guy named Bob Day, who wrote a named pipe implementation to eliminate the use of shared memory. So Windows 95 had a big shared segment amongst all the shell processes where it would store stuff that was common to all the shells. We didn’t want to do that. Shared memory is a bad idea on NT at an industrial level, so he came up with a way to do it with named pipes, and I remember doing a code review on it, and it was very impressive to walk through the code.

**1:01:15** · Dave Plummer: It was one of those things where it was like, “Oh, I don’t think I could have done that if I was trying.”

**1:01:19** · Lex Fridman: Who’s the greatest programmer you’ve ever encountered?

**1:01:22** · Dave Plummer: You know what? I don’t think there is any one. I’ve met a number of great programmers, but I’ll tell you one story that impressed me a lot. When I was brand new at the company, I’d been there like six weeks, and I’m working on this OLE Presentation Cache that I’d mentioned earlier. And I’m on Windows 95, and I’ve got Excel inserted into Word, and I’m in the kernel debugger, and something’s going wrong in the scheduler. And I’ve been there, you know, I’ve barely written any x86 code, and I’m looking at the Windows scheduler, trying to figure out why my thing is deadlocked.

**1:01:49** · Dave Plummer: And eventually, I get stuck, so I’m kind of out of my element, and I send an email to the Windows 95 kernel team and say, “Could you send somebody by?” So about 10 minutes later, this developer strolls in, and they’re just holding a null modem cable, which is to connect my two machines together so they can debug one with the other in case I didn’t have it, but it was already set up. And so they sit down, and they’re using WinDbg, which is a horrible debugger. It’s just accursed.

**1:02:10** · Dave Plummer: But they’re very, very competent with it, and they are just blasting through the call stacks, and they’re checking all these objects in the kernel and trying to find out who’s waiting on what and why things are deadlocked, and what things are signaled and what’s not. And it’s just this quicksilver ballet of call stacks flying by, and I’m watching this, and I’m pretty blown away because I’m a good programmer, but this person is an amazing debugger, and I’ve never seen a performance like this. And about five minutes in, I just hear, “Oh, I see.” And then they disconnected and got up and left. And that was Laura Butler, who became a distinguished engineer at Microsoft. I think she may still be; I’m not sure if she’s retired or not, but…

**1:02:49** · Dave Plummer: So she kind of set my template for, you know, what Microsoft developers were like when they’re debugging and what kernel developers were like, and even what female developers were like, because I had such a small sample set. But it was a very high standard, so…

**1:03:02** · Lex Fridman: There are few things I love in life more than people who are ultra-competent at anything, really. But the lower level, the better, in the engineering space. They’re able to, for example, run or maintain the computer infrastructure. So not the individual computer, but the computers communicating and working together. Those people are just magicians. It’s so inspiring to make… It’s like watching a great carpenter or…

**1:03:28** · Dave Plummer: I love anything done really, really well.

**1:03:30** · Lex Fridman: Yeah, it’s beautiful to see. It’s beautiful to see that humans are able to accomplish that. Even in civil engineering, when I look at bridges, it’s like the number of people that had to come together to build that, and now millions of people use it every single day. With software, sometimes you don’t get to see visually just the number of people impacted by a thing. So imagine how many people are impacted by Linux and all the different open-source systems that make up Linux. It’s incredible. And Task Manager is an example of a piece of software. Just how many people have used that over the years, and how many times? It’s crazy. It’s probably, is it billions? Billions have used that.

**1:04:12** · Dave Plummer: Yeah, two billion a month or something.

**1:04:13** · Lex Fridman: Two billion?

**1:04:14** · Dave Plummer: Something like that. I’ve seen the metrics, and it’s up there.

**1:04:16** · Lex Fridman: Oh, crazy to think.

**1:04:18** · Dave Plummer: It is. What I love about it, though, and I’m sure you’ve had this experience, where sometimes you design a piece of software, and it’s complex, and you get it working in your head, and you get the plumbing working, and you know how it’s going to run and flow, and then eventually you write the code, and the code does that thing that you had pictured in your head. And now there are billions of copies of that thing that I had in my head running on billions of people and machines, and that in itself is really cool to me. It’s not a vanity thing so much as I’m impressed by it, I guess.

**1:04:46** · Lex Fridman: How’s your programming evolved over the years?

**1:04:50** · Dave Plummer: I take a lot more care with complexity these days. So it used to be you would write code and just keep writing code, writing code, and then at some point, go back and clean it up. Well, I write the other way now. I try to write really clean initial skeletal code and then flesh it out because I have been involved in too many projects of my own and of other people’s making where things get so messed up that they’re just not fixable. And so sometimes the work you put in upfront pays off, you know?

**1:05:18** · Lex Fridman: What programming languages have you used over the years? What’s been your main go-tos?

**1:05:22** · Dave Plummer: For me, it’s been C++ and assembly language.

**1:05:25** · Lex Fridman: And still to this day, C++ is really what you lean on?

**1:05:28** · Dave Plummer: Yeah, right now I’m 100% Lua and Python, but that’s just a side project I’m working on.

**1:05:33** · Lex Fridman: Can you speak to the Lua and the Python detour that you took, and what do you love about C++?

**1:05:40** · Dave Plummer: What I’m doing is I wanted to build an AI to play the game Tempest. That’s the old Atari game, Tempest. This is a game that I actually hold the world record on.

**1:05:49** · Lex Fridman: Can you take me to this Atari game, Tempest? Okay, Atari Tempest. What kind of game is this?

**1:05:55** · Dave Plummer: So it’s a 3D vector game from 1980.

**1:05:59** · Lex Fridman: Okay.

**1:05:59** · Dave Plummer: And it’s a very complex game. You’ve got full 360 degrees of motion, you have eight shots on the screen, there are like 11 enemies, there are spikes. So it’s a very complex game. It’s not like trying to do Pong or something. And what I wound up doing was first taking the ROMs out of the machine and reverse engineering the code. So I got a sense of where all the code in Tempest lives and what it does, where the zero-page variables are, where things live. And yeah, there’s one.

**1:06:23** · Lex Fridman: So, oh, wow. That’s a very geometric… Okay, what can you explain to me about the gameplay?

**1:06:28** · Dave Plummer: Yeah, that’s me playing the game right there.

**1:06:30** · Lex Fridman: This is literally you playing?

**1:06:31** · Dave Plummer: This is me. Dave is the high score, you’ll see, in the top center there.

**1:06:34** · Lex Fridman: Can you explain to me what I’m looking at?

**1:06:36** · Dave Plummer: Well, it’s a 3D geometric world. It’s basically 3D Space Invaders wrapped into a shape, and the enemies descend from the center of the tube towards the outside, and they all have different behaviors.

**1:06:50** · Lex Fridman: Wow.

**1:06:51** · Dave Plummer: So long story short, it’s a fairly complicated game to play well, and I wanted to see if I could get an AI to do it. So once I had figured out where all the interesting parts of the game lived in memory, I added them as parameters and built a Lua app to extract everything from the game’s memory as it’s running and puts them together as parameters, which sends it to the Python side over a socket, and then the Python side does RL learning. I’m using a dueling Deep-Q, and I believe… Two with two head and tail, and they chase each other and it can play up to about level 36 now, which is way better than most humans. But that’s level 96, so it’s got a ways to go yet.

**1:07:27** · Lex Fridman: And you’re the red thing shooting?

**1:07:29** · Dave Plummer: Yes.

**1:07:30** · Lex Fridman: You’re controlling the red thing that’s shooting? Okay. What are the options? You can just move clockwise or counterclockwise and then you could shoot.

**1:07:38** · Dave Plummer: Yeah, so you have a rotating knob- …which is an optical spinner, and you have a fire button and a super zapper for emergencies. But that’s it. Fire and rotate, basically.

**1:07:46** · Lex Fridman: All right, let’s get back to your favorite C++. What do you love about C++? Why have you stayed with it for all these years?

**1:07:51** · Dave Plummer: Because it allows me to encapsulate my favorite C code in classes. I’m not a big-

**1:07:57** · Lex Fridman: You’re really a C guy.

**1:07:58** · Dave Plummer: Well, I actually-

**1:07:58** · Lex Fridman: Okay, I got you.

**1:07:58** · Dave Plummer: Yeah, I’m really a C guy. Although I write two kinds of C++. I write really modern C++ 20 using no pointers, no strings, or no character strings, so there are… you know, it’s basically as safe as Rust as far as I’m concerned. Or I write C with classes, which is standard C, but, you know, with polymorphism and encapsulation. That’s most of what my code is, but I try to do both.


### Scariest time of Dave’s life

**1:08:23** · Lex Fridman: Let me ask you about the whole stretch of time that we kind of skipped over. You built a lot of software over the years after Microsoft, on the side while at Microsoft and afterwards, a lot of successful pieces of software. One of your companies was Software Online, and it got into trouble for nagging users too much, I guess-

**1:08:44** · Dave Plummer: Yep.

**1:08:44** · Lex Fridman: … to upgrade. That’s what I saw. What was all that about and what did you learn from that experience?

**1:08:49** · Dave Plummer: That was… Other than, like, family health scares, you know, when kids are sick, that was the scariest time of my life. And the period leading up to it was one of the most invigorating and exciting, because what had happened was while I was at Microsoft, I had written all these shareware utilities and I was selling them on the side and sold one to Microsoft, as we talked about, and they started to do really well. And then I discovered banner advertising online. So I signed up with my credit card for a site, I think it was called Fast Click, and you could say, “I will pay this much for a banner ad impression. Here’s my banner.” And it would rotate it in. And I didn’t set a cap on it. I came back on Monday and I saw I had spent like $10,000 in banner ads.

**1:09:26** · Dave Plummer: I was like, “Holy crap. How am I going to explain this to my wife? This is a bug, it’s a mistake, it was my fault.” And I looked at the sales and it had made like $38,000 worth of sales. And I was like, “Holy cow. So all I have to do is scale that at some point,” and basically did that for the next several years. And the reason we got in trouble was the AG came in and they had… well, I was blown away because they had like 12 court claims of action and 10 of them were outrageous, which to me as a person with autism, I couldn’t get past. It’s like, I know these 10 things are absolutely not true. Why are we even here talking about them? And then all they care are the two things that might be true.

**1:10:03** · Dave Plummer: And the two things that might be true were that it was a 30-day trial version, and after your 30 days were up, it would then, if you continued to run it and not buy it or uninstall it, it would remind you once a day. Not like every 10 minutes, but once a day or every time you booted your computer, but most once a day. And the AG contended that was too often; it amounted to spam. And so we agreed with them to limit it to once a week, I believe. And, you know, there had to be a button to just uninstall with one click. So we did those kinds of things. The other one was, in those days, when somebody bought a piece of software, even if they bought it online and got a download, they fully expected there would be media showing up at their house.

**1:10:38** · Dave Plummer: So in the year 2001, which were 2001-2003 we’re talking about, if you bought software, there was an expectation that a disc would show up. And so we made that the default, was to fulfill by disc and it was $3.95 or $4.95 extra, and it was very obvious, but it was a checkbox and it was turned on to ship the disc to your house. Because we found if we didn’t do that, we got all these calls, people would wait, they’d order, two weeks later call, “Where’s my disc?” And we’d look, “Oh, you didn’t order a disc.” “Well, cancel it all.

**1:11:04** · Dave Plummer: I don’t want it because I’m not waiting for it.” And so we got a lot of returns and we didn’t include the disc, and so we decided to include the disc, but that is an a priori violation of negative affirmation billing in Washington State because you’re giving them a default higher purchase price.

**1:11:18** · Lex Fridman: What about the software user relationship? It’s interesting, like, how often to annoy the user with a thing. Right? If you never mention anything, they might never discover something they actually want. But if you mention it too much, then they can get annoyed.

**1:11:46** · Dave Plummer: Yeah. And what you don’t want is you don’t want them to have to do it or buy it or do something to get rid of it.

**1:11:51** · Lex Fridman: That’s one of the things that bothers me with… I think Windows does that a little bit still to this day, where it bothers me by asking me certain questions, like, “Do you want this?” For example, I really don’t like to use my Microsoft account to log into Windows. I think now it’s basically required. I think there’s just no way around it. But they make it so difficult to not do that. It’s almost like they think they can just trick me into… It really does feel like I’m getting tricked into not doing what I want to do.

**1:12:32** · Lex Fridman: It’s… I have to, like, think, “Okay, I need to click skip,” and then it’ll do something, “Are you sure?” Like, I have to use too much of my brain to do the thing I need… As an interface, you know what I’m trying to do. You’re trying to trick me into not doing the thing I want to do. And what I hate about that is, like… It’s probably effective, sure, for converting people, but it’s really not good long-term for taking care of the interests of the user.

**1:13:06** · Dave Plummer: Yeah, the one that really throws me is the user recommended settings. So I just did a Windows upgrade, I went through the steps, and, you know, I’m going through this new dialog or wizard, and “use recommended settings” sounds like the thing you should do, but I’m pretty sure that resets you to using the Edge browser and… …And all this other stuff. So yeah, recommended by them, but not recommended for me. And that’s the difficulty.

**1:13:25** · Lex Fridman: That’s a really good example. What effect do you think that does in resetting the default browser to Edge? Do you think you’re going to really earn the loyalty of a user if you do that? Don’t you think that there are actually… What you’re going to create… You’re going to create some passive loyalty from some user base, so on the metrics, it might actually look like you’ve increased the number of Edge users, but really, it’s that reputation hit you take over time where it just forms where the Edge is the thing that you can’t quite trust. Unfairly, because I think Edge is a really great browser, but just this unpleasant feeling. I don’t know what that is, and…

**1:14:10** · Dave Plummer: Well, you don’t want your operating system to be an adversary, right? And sometimes Windows can feel adversarial. Like, it doesn’t have your best interests at heart, and that bugs me to a certain extent.

**1:14:20** · Lex Fridman: I mean, we have this feeling, I think we just have general distrust when somebody is super nice to you and is basically selling something. There’s a certain aura about that kind of interaction. And when an operating system is interacting with you in that way, it’s like…

**1:14:36** · Dave Plummer: Yeah, I would much rather pay $199 for Windows Pro per year, or 20 bucks a month, or whatever the fee schedule would be, and not be upsold any further and not have my data monetized, and those kinds of things, so…

**1:14:47** · Lex Fridman: Did you learn about finding the right balance from that?

**1:14:50** · Dave Plummer: Yeah, I mean, I’m way more self-aware now. There are things I would do much differently, particularly in terms of the advertising. I always figured… There’s a guy named David Ogilvy, and he did this ad long ago for the Volkswagen Beetle where it had a picture of a Beetle, black and white, and it just said, “Lemon,” and there was a block of text below it. So it’s clickbait-y and then informational, and I always tried to follow that pattern. But there are three ways to sell something, I think, and you can use sex, fear, or greed. Sex doesn’t work really well for software. Fear works well for antivirus and stuff, but not so much for optimization and make your computer faster utilities.

**1:15:24** · Dave Plummer: And so I always tried to cater to the greed aspect. You know, make your computer faster, get more RAM available, whatever the value proposition is. But I realize now that I’m looking at that with my knowledge, and as an autistic person, I now have an appreciation that other people are going to look at it with their background knowledge and may conclude something different. So I might be scaring people where I was just trying to incentivize or get their greed instinct going. So I’d be more sensitive about that kind of thing today.


### Best Windows version

**1:15:50** · Lex Fridman: Ridiculous question, but what do you think are the top three Windows operating systems? The different versions?

**1:15:59** · Dave Plummer: I’m a fan of Windows 2000 server. That’s

**1:16:02** · Lex Fridman: Really? Okay. … Wait, wait, pl-

**1:16:04** · Dave Plummer: That’s what I ran my business on and I ran my brother’s business. We set up multiple salons all VPNed to one another and using the SQL Server and…

**1:16:11** · Lex Fridman: I don’t know if I ever got to experience Windows 2000 server, so when was XP out?

**1:16:16** · Dave Plummer: 2001.

**1:16:18** · Lex Fridman: What was before XP?

**1:16:20** · Dave Plummer: 2000.

**1:16:21** · Lex Fridman: 2000. Was that good?

**1:16:23** · Dave Plummer: Yeah, I liked it. I mean, it doesn’t have the visual flash that came with XP, but as a system, and especially as a server operating system, it was great for the day.

**1:16:29** · Lex Fridman: But then XP was, hmm, I would say probably from a completeness perspective and impact and how long it lasted, it was probably the greatest Windows for consumers, the operating system.

**1:16:44** · Dave Plummer: I would think so. It’s certainly got the longevity for it. There are people who still run it. I mean, I’d still run it on stuff if you could get security updates ’cause it does 98% of what I need Windows to do, but…

**1:16:52** · Lex Fridman: Yeah, that was incredible. I mean, so Windows 95, I’ll probably put Windows XP as the number one for me and then Windows 95 two.

**1:17:01** · Dave Plummer: What’s your metric? Personal preference or industry impact or…

**1:17:05** · Lex Fridman: Industry impact, stability, just there’s certain, like, just like with programming, you have code smell. Just, like, how well all the features were orchestrated together, how there’s a design philosophy that permeated the whole thing and was consistent. Not too many features, not dumbed down too much.

**1:17:26** · Dave Plummer: Right.

**1:17:27** · Lex Fridman: But not overcomplicated. How often it crashes to blue screen. All of those things.

**1:17:33** · Dave Plummer: I don’t know if it’s a very apt description, but I think of it as crisp. So there’s not a lot of rough edges. It does what it does, does it snappy and…


### Slot machines

**1:17:39** · Lex Fridman: You said you play slot machines, and given that you love hardware and software, you’re the perfect person to ask, how do slot machines work?

**1:17:50** · Dave Plummer: Well, I’m happy to ruin them for you.

**1:17:52** · Lex Fridman: Okay.

**1:17:52** · Dave Plummer: So- It’s ironic to me that I play slot machines because I know it’s a losing bet overall, but there’s a whole dopamine feast there of bright lights and high contrast colors that I enjoy. So I do play them. But what happens is, internally, there’s basically a black box mechanism that does nothing more than generate the next random number and what the outcome is in terms of probability and payout. And then the game says, “I’ve got to make up a movie to go along with that.” And maybe it’s three bars or whatever it is, but there’s no correlation. It’s not spinning the reels, seeing where they land, and looking that up to see what you won. It’s completely the other direction. It determines whether or not or if you won and then makes something up to fit that scenario.

**1:18:29** · Lex Fridman: That, that indeed is ruining it for everyone.

**1:18:31** · Dave Plummer: A little bit.

**1:18:33** · Lex Fridman: What kind of code runs them?

**1:18:35** · Dave Plummer: I don’t really know. I tried to get down and get inside access to one, and it was very hard. They don’t want to tell you a lot about them, and I’m sure it’s not that deep of a secret, but… They’re all basic Windows PCs, but they’re basic Windows PCs on top of a very secure enclave of some kind that I don’t know a lot about.

**1:18:53** · Lex Fridman: Yeah, it has to be extremely secure, right?

**1:18:56** · Dave Plummer: Yeah. Well, in the 70s or 80s, there was a tech in Vegas who went around and he was burning his own ROMs for the slot machines. With a backdoor in them, so when he serviced the machine, he would just put his ROM in.

**1:19:06** · Lex Fridman: Nice.

**1:19:06** · Dave Plummer: And he’d come back six months later and…

**1:19:07** · Lex Fridman: Nice.

**1:19:08** · Dave Plummer: Invoke the backdoor and…

**1:19:09** · Lex Fridman: I love humans so much. Anyway, do you have other favorite kinds of systems like that?

**1:19:15** · Dave Plummer: I like a lot of old hardware. I restore cars, so I do a lot of 1960s muscle cars, cars and trucks.

**1:19:20** · Lex Fridman: Nice.

**1:19:21** · Dave Plummer: And old computers, so I restore PDP-11s. It’s been my fascination and my special interest for the last six months or so, and I’ve built a number of those.

**1:19:30** · Lex Fridman: Yeah, I’ve seen you posting videos about it, the PDP-11/83. What’s that whole project?

**1:19:40** · Dave Plummer: So basically, what it is, is I had built a number of PDP-11s. And so over the years, I had acquired all these parts and I decided, “Well, let me build the best PDP-11 that I can.” And so it was kind of a quest to, just like you try to max out a PC, I tried to max out a PDP-11. So it’s got four megabytes of memory, which would be massive in the day. And yeah, that’s it there. And it’s got lots of blinking lights, and I had to rewrite the BSD kernel to make the lights work and…

**1:20:05** · Lex Fridman: What are we looking at here? What’s…

**1:20:09** · Dave Plummer: So the very top is a PDP-11/70 control panel, which we can largely ignore, and then there’s two chassis below that. One has-

**1:20:15** · Lex Fridman: What are the different knobs? Sorry to ask dumb questions here.

**1:20:18** · Dave Plummer: The knobs, they, uh- … control what view you get of the LEDs.

**1:20:22** · Lex Fridman: Oh.

**1:20:22** · Dave Plummer: So normally, you see the data bus and you can see the address bus. And you can pause the machine, you can edit the add- address on the bus, and you can deposit stuff into memory with the switches.

**1:20:32** · Lex Fridman: Man, the haptic plus the LEDs. That’s what you imagine a computer to be.

**1:20:39** · Dave Plummer: Yeah.

**1:20:39** · Lex Fridman: That’s so cool. That’s so cool. And then these are what? What are these? These are DU1, DU2?

**1:20:45** · Dave Plummer: Yeah. It’s a weird floppy drive. It’s a dual floppy drive with one stepper motor. So both heads seek together like Siamese twins.

**1:20:52** · Lex Fridman: Okay. So what, what kind of stuff are you doing with this? What are you- … are you trying to restore them?

**1:20:57** · Dave Plummer: Yeah. So I restore them and-

**1:20:58** · Lex Fridman: Does it actually run? Oh, all the blinking lights are real?

**1:21:01** · Dave Plummer: Yeah, it’s all real.

**1:21:03** · Lex Fridman: Wow.

**1:21:04** · Dave Plummer: Then I had to rebuild the kernel and all that, so I had to learn the BSD kernel. I’m pretty familiar with it now to get… ‘Cause you can’t just add a device driver, right? You’ve got to rebuild the kernel to add support for whatever device. So you add a new disk controller. It’s time to build the kernel, so you gotta go find the source and find the code and…


### Autism and ADHD

**1:21:20** · Lex Fridman: And you can run code on this? You’ve written a couple books on autism. Being autistic yourself, I was wondering if you could tell me about, like, fundamental differences about the mind of a person with autism versus a, let’s say, a neurotypical individual.

**1:21:34** · Dave Plummer: Well, the fundamental theory of thought for autism is called monotropism. And basically what that means is that my brain does one thing and does it very intensely, and then when it’s done I can move on and do something else. But I’m not a multitasker. I’m a serial single-tasker by any stretch. Autism usually brings with it sensory sensitivities and repetitive behaviors, behavioral issues that compound it. And if they rise to the level where an individual can’t moderate or accommodate them in their life, it becomes a disorder. And that’s probably one to two percent of the population.

**1:22:08** · Lex Fridman: What’s the biggest benefit of life with autism?

**1:22:11** · Dave Plummer: I can bring to bear an incredible amount of focus and dedication on a particular task. It has to be something I love, it has to be something that’s rewarding, it has to be something I can make progress on, and there have to be all these things that are true about it. And it could be like a kid playing with trains. I get that same feeling.

**1:22:28** · Lex Fridman: That said, you also said that you struggle with ADHD.

**1:22:33** · Dave Plummer: Yeah, a fair bit.

**1:22:33** · Lex Fridman: So that’s part of the component, like, maintaining the focus?

**1:22:38** · Dave Plummer: Actually, acquiring the focus is the issue. So I’m very easily distracted. I fall asleep with noise-canceling headphones or I can’t fall asleep, that kind of thing. But once I get locked in, I’m very hard to distract. So it’s kind of a paradox.

**1:22:52** · Lex Fridman: Oh, that’s fascinating.

**1:22:53** · Dave Plummer: It’s hard to get into that state.

**1:22:54** · Lex Fridman: Okay. What’s the biggest challenge of life with an autistic mind?

**1:22:58** · Dave Plummer: That I don’t know what anybody else is thinking. So I know what I would think about this interaction if I was in your position and I was you. And that’s the best I can do. But I think most neurotypical people have a sense of, “Well, Lex probably feels this way or that way ’cause he’s acting this way and his reactions are this and his facial expressions say this and…” That’s all kind of lost on me. So I run a little proxy NPC game for everybody I deal with.

**1:23:20** · Lex Fridman: So I guess that makes social interaction a little bit complicated.

**1:23:22** · Dave Plummer: It can be, yeah. Telephone is especially hard because I rely on a lot of other cues, and when somebody is just on the phone and I just have their voice, there’s so much that’s implied between people that I miss. And so I’m much better on FaceTime, where if somebody makes a joke, they might smile after- Whereas on the phone, I don’t know if you’re being sarcastic or serious and that kind of thing, so…

**1:23:42** · Lex Fridman: So that’s probably gotten you into trouble over the years a bit.

**1:23:45** · Dave Plummer: Yeah. There’s lots of times with my wife, too, where… Well, there’s a certain literalism that comes with autism. And we spent years where she would say something and I’d say, “But that doesn’t make sense.” She’d say, “You know what I mean.” I’m like, “No, I know what you said and I’m not being just combative here. I literally only know what you said,” and I don’t have that. And I remember we’ve been in meetings with people, and you know, if there’s three or four people in the meeting and I’m the only autistic person, I’ll tell them that they’ve got this communication loop going on and I have to… You gotta tell me what’s going on because I really don’t know what’s being said here. So…

**1:24:19** · Lex Fridman: You told me related to this that there was an early, somewhat awkward encounter with Bill Gates. Can you share the story of that interaction and how autism comes into play here?

**1:24:32** · Dave Plummer: Yeah. My very first summer at Microsoft when I got the internship, Bill had all the interns over. I guess it was 20 or maybe 25 of us, that got hired that year over to his house for burgers and beers and just chat in the backyard. And of course, it’s still Bill Gates, and he’s a big enough deal even then that you’re a little nervous. And so my manager, Ben, who was sort of my mentor at the time, took me over to introduce me to Bill because he knew him. And he’s explaining, “This is Dave. He’s our intern from Canada. And in the space of four months, he’s done this feature and just copy and smart drive,” and he listed off all the stuff I was doing.

**1:25:05** · Dave Plummer: But I stopped because I’m like, “Well, actually, it was three months.” And I had to interrupt them, and they both kind of, “What?” And they looked at each other, and I realized that was the wrong time to… …Correct a guy. But…

**1:25:17** · Lex Fridman: Yeah. So you, like, little inaccuracies?

**1:25:20** · Dave Plummer: Oh, drive me crazy.

**1:25:22** · Lex Fridman: And then you, of course you don’t… The impact that might have on a casual social interaction, it’s not trivial for you to be aware of that.

**1:25:38** · Dave Plummer: Yeah. I’m much better than I used to be. Before, I didn’t know and I didn’t know how injecting a correction meaninglessly into a conversation could impact or make the other person feel. Now I have a better sense of it, but…

**1:25:49** · Lex Fridman: What advice would you have for folks who have an autistic mind on how to flourish in this world?

**1:25:56** · Dave Plummer: In terms of prosperity and finances, the biggest thing I can say is sell what you can do and not yourself. Because if you go into a job interview and you try to wow them with your personality and how amazing you are, it may or may not go well. But if you go in with your portfolio of work and say, “Look, here’s my GitHub history and here are the awesome projects I contributed to, and here’s the actual algorithm I wrote, and this is what I do,” I think you get a lot further with that. So, whether you’re playing the piano or writing code.

**1:26:21** · Lex Fridman: That said, so much of software engineering on large teams has a social component to it, right?

**1:26:29** · Dave Plummer: It does, and that was a liability for me.

**1:26:31** · Lex Fridman: How do you… I mean, what have you learned about how to solve that little puzzle?

**1:26:36** · Dave Plummer: I think the biggest deficit for me was when I started to manage people, because now you’re concerned about their hopes, dreams, aspirations, what motivates them. They have entire lives that are kind of a mystery to me, because I assume they want to be motivated and led and encouraged and compensated exactly as I would. And that’s not always the case. Some people need a lot more affirmation, some people just want money, some people want to be in the important meetings and make decisions. But I was largely oblivious to that. And so eventually I had to learn that everybody that you’re managing has their own set of incentives and priorities, and they’re completely different from what I think they probably are.

**1:27:11** · Lex Fridman: So you could, I guess, make things more explicit and just communicate better about, like, ask them about what their interests are.

**1:27:19** · Dave Plummer: Yeah. And that’s something I started doing, is overtly asking. Because it’s hard for me to nudge somebody there. I’m not good with that kind of social dance, so…

**1:27:27** · Lex Fridman: Yeah, part of the social dance is there’s a lot of stuff that’s unsaid. You can kind of figure out… You can read people. But if that’s… With autism, it might be a little bit difficult to do that, and so you have to make things more explicit. Plus, like, sarcasm and satire and humor might be difficult. I would love to be a fly on the wall in some of your earlier interactions with Microsoft. I mean, some of the greatest engineers have a mind like this, so…

**1:27:58** · Dave Plummer: Yeah, I’ve had laptops thrown at me and stuff, and I’m sure it was my own fault, so…

**1:28:01** · Lex Fridman: You write about the 10-second autism test. Could you explain how this works?

**1:28:05** · Dave Plummer: Yeah. Now, there is, of course… Anything that has two answers has a high error rate, but… So what’s more important to society as a whole from the people, is it cooperation or creativity? And if you had to pick one, which is the most important? And most neurotypical people will generally lean towards cooperation, whereas people on the spectrum tend to lean towards creativity as individual problem-solvers.

**1:28:26** · Lex Fridman: Of course, there’s some kind of error rate there.

**1:28:28** · Dave Plummer: So if you want to double your precision, you can use a second test, which is you ask, “There’s a room with 10 chairs, and six people come in and sit down in those chairs. How many chairs are left?” Now, some people are going to say four, but I’m going to say 10, because that’s how many chairs are still there. Literally true. And I’m not being a dick.

**1:28:46** · Lex Fridman: Yeah, okay.

**1:28:46** · Dave Plummer: I’m not trying to be complicated, but that is how my mind works. And so when I see that question, it’s like it depends how you answer it.

**1:28:53** · Lex Fridman: So you’re how literally you take things?

**1:28:57** · Dave Plummer: Yeah. Everything is very literal for me. I remember as a kid, my grandfather was building a planter holder in the kitchen for my mom. And he was using these big angle brackets that I thought were a little overkill, and I said, “Do you think that’ll be big enough to hold the plant?” And he says, “It’ll be big enough to hold a horse.” And I was only five, but I was very confused about, A, why you would bring a horse into your kitchen, why you would put a horse up on a planter, and all of these things that didn’t make any sense to me when obviously it was a figure of speech. But for a lot of my life, I took figures of speech as literal, so…

**1:29:26** · Lex Fridman: You’ve mentioned emotional post-processing as a strategy you use to replace social interactions so you can sort of reverse engineer to help you understand the neurotypical world. I think this is going to be useful to a lot of people. What does that entail? How does that help you?

**1:29:43** · Dave Plummer: So if I meet somebody, particularly somebody new, and it’s my first couple interactions with them, so even meeting you today, then I will go home later and replay all of the moments where I had choices to make. And probably the most uncomfortable ones first, to find out, what did I do wrong in that moment? What did I miss? What was the other person thinking? How can I improve that kind of situation next time, and do I need to go fix it or make a phone call, that kind of thing in a bad… you know, in an extreme case. But… And that’s happened a couple times in my life. Like, I had a car restored that my dad had bought new in ’69. I still have it, so we’ve had it 50 years.

**1:30:18** · Dave Plummer: About 20 years ago, I had it restored, and it was a three-year process of craftsmen working on this car for thousands of hours. I go out to pick it up and I’m inspecting the car and I’m very impressed with the work, and I’m saying, “Oh, this is nice and this is great,” and everything else. Then I fly home and write the check and the car gets delivered. And then I realized probably 10 years later that I had a whole bunch of craftsmen that had worked on my car for three years, and I probably should have blown some smoke up their butts about what a great job they did, but I never did that because it’s not what I wanted or needed in that moment. And I was completely oblivious to that.

**1:30:51** · Dave Plummer: So I sent an email to the manager, or to the owner of the place, and I said, “I don’t know if you remember this, but 10 years ago, I picked up my car and I probably looked unimpressed, but I want you to know that I was very impressed with everything and the quality and everything else.” And he wrote back. He’s like, “I’ve thought of that moment often.” (laughs) So I’m like, “Now I’m glad I brought it up.”

**1:31:08** · Lex Fridman: Yeah, there’s subtle things about human interaction that mean a lot to people, and if you ask them straight up, they might not be able to articulate that, but it means a lot. And when it’s off, when something is off, it bothers them.

**1:31:22** · Dave Plummer: Right.

**1:31:22** · Lex Fridman: But to reverse engineer that, to figure that out for a person who might not sense those little subtleties of human interaction is tough.

**1:31:32** · Dave Plummer: That’s a good point to jump in there, too, on empathy because there is some perception in the community that people with autism lack empathy, and I don’t think that’s the case at all. I can only speak for myself. I feel fairly empathetic, but I think the problem is a communication one, and it works in both directions, whereas I don’t know how you’re feeling, so it’s hard for me to be empathetic with it until you communicate to me what it is you’re experiencing. And then once I know, once I have an understanding of what’s going on in your head, I can feel incredibly sorry for you. But until then, I’m going to assume you’re going to handle it just like I would in your position, in my case, with what I know now.

**1:32:06** · Lex Fridman: What advice would you give to people on the other side? How can they help you be a better friend or partner or colleague? How should they communicate with you to help, like, give more information?

**1:32:18** · Dave Plummer: Yeah. Be really specific. And don’t assume I’m going to pick up on clues and nuance and subtlety. So if you’re trying to nudge me into a particular behavior, you’re much better off saying, “Dave, this is what you need to do.”

**1:32:31** · Lex Fridman: Have I failed in any way today?

**1:32:32** · Dave Plummer: No, not yet.

**1:32:33** · Lex Fridman: All right. What score would you give me out of one to ten? Am I a six? A seven?

**1:32:43** · Dave Plummer: 7.5.

**1:32:43** · Lex Fridman: Communication? 7.5? (laughs) Floating point. Nice. Masking. You got to tell me what that is. It’s a significant experience for many on the spectrum. What is masking? And tell me about any of the experiences you’ve had with masking.

**1:33:00** · Dave Plummer: So masking is, and it’s probably not the right way to describe it, but it’s the act of acting normal. And that is, how do I conduct myself in a social situation in a way that other neurotypical people are going to receive and accept it the right way? And everything you do in a social interaction, from waving my hands to making facial expressions to tone of voice to posture, it’s a huge contrivance and it’s work. So it comes natural to most people, it’s just what they do, and cool people do it really well. But for somebody on the spectrum, you’ve got to fake it all.

**1:33:41** · Lex Fridman: Yeah. Acting normal.

**1:33:44** · Dave Plummer: There’s a song by Rush, you know the band? Limelight. And it’s written by Neil Peart. I only speculate about people who have passed on, so I’ve got a sense he was probably on the spectrum. But the line is something like, “All the world’s indeed a stage, and we are merely players, performers and portrayers, each another’s audience.” And he talks at length in the song about not being able to treat strangers as friends and being able to fake an affect and all that, so it seems like he’s struggling with masking a lot in the song. I have no idea, but that was what I took from it.

**1:34:13** · Lex Fridman: You described meltdowns as an overwhelming experience. Can you describe meltdowns? What typically triggers a meltdown?

**1:34:22** · Dave Plummer: Generally, it is… it’s when you’re emotionally overwhelmed to the point that you can’t manage your behavior anymore. So you see it in the movie Rain Man when he’s trying to get on the airplane and he’s kind of forced and he starts losing it. That’s a meltdown. Or I’ve seen it on… They did kind of a… Well, actually, probably the best portrayal I’ve seen in media is… What’s the TV show where the doctor is autistic? He’s… Anyway, there’s a TV show where a doctor’s autistic and he’s a surgeon and he is eventually banned from surgery because of his autism, and he’s always wanted to be a surgeon and he has a complete meltdown, and it’s a pretty good portrayal on television.

**1:34:56** · Lex Fridman: What is actually happening? Like, there’s a threshold you cross that it’s just like…

**1:35:00** · Dave Plummer: Yeah. The switch flips.

**1:35:01** · Lex Fridman: It’s like a blue screen essentially-

**1:35:05** · Dave Plummer: Yeah. Kind of.

**1:35:05** · Lex Fridman: … for the brain algorithm?

**1:35:07** · Dave Plummer: So the switch flips. You go to a primitive brain. Your frontal cortex shuts down to an extent, I think, so you don’t have the benefit of decision-making and filtering. You’re a very reptilian brain in that state. And it’s really a panic state. And so it’s a panic and a fight or flight response to not being able to tolerate the current reality. And perhaps it’s been so frustrating or you’ve been so randomized or you had a bad travel day or an argument at work or whatever, it’s added up to the point that something has now triggered you and your brain loses its ability to adequately moderate your behavior.

**1:35:41** · Lex Fridman: What about love and relationships? What are some of the challenges of that and… You know, there’s a show, Love on the Spectrum.

**1:35:47** · Dave Plummer: I’ve heard of it. I’ve not seen it, but I’ve heard of it.

**1:35:49** · Lex Fridman: Because certain aspects, like literal interpretation of things, it just makes the complexity of romantic relationships even more explicit in that context.

**1:36:01** · Dave Plummer: You know, I’ve been married 31 years and together for 37, so a long history there, and I think our first indication that we knew we were very different was we were sitting in the car one night out front of the house at dark and across the street there’s kind of a nice house, and it has these big brick pillars that are linked by, like, anchor chains and it forms a fence around the yard. And I’m looking at these things ’cause they’re about two feet square and they got capstone and I’m like, “You know, I wonder if they’re hollow or are they backfilled?” Are they filled with concrete or what?” And my now wife looks at me and she’s like, “What’s wrong with you?” “Why do you have a place in your head that cares about that?”

**1:36:36** · Lex Fridman: Yeah. That’s great.

**1:36:37** · Dave Plummer: And we just knew in the moment that I was passionately involved and caring, and she was passionately involved, and why would you even worry about that kind of thing? We knew we were very different.

**1:36:47** · Lex Fridman: Yeah. Very specific, seemingly irrelevant details.

**1:36:51** · Dave Plummer: But- …I was never good with people. I don’t get it when people like me, I guess. And so my son is the same way, because they don’t fall very far from the tree. I got them a T-shirt that says, “If you’re hitting on me, please let me know and be specific, because I’m clueless.” And it’s very similar for me. I mean, I had to be around a long time and kind of grow on people because I had no game, I had no ability to do the social dances that that whole thing requires. So my only option is to just be myself, and that works for some people.

**1:37:21** · Lex Fridman: Were you able to say, like, “I love you,” that kind of stuff?

**1:37:26** · Dave Plummer: Yeah. I mean, her family was way more open with that kind of thing than mine was. So it was a growing period for me. But, yeah, that’s not a problem I have.

**1:37:33** · Lex Fridman: Okay. All right. But it seems unimportant. Like, what is that actually accomplishing?

**1:37:41** · Dave Plummer: Well, now we do a lot of affirmation and checking. In the last couple of years, we do a thing where she’ll just be like, “You good?” I’m like, “Yeah.” And there’s two steps to that. There’s the “Are you good?” and then there’s my response, because if I’m like, “Yeah,” she knows something’s up.

**1:37:55** · Lex Fridman: Yeah. So,

**1:37:55** · Dave Plummer: And so there’s always this pinging back and forth because there’s not the ability to read people just from looking at them to know what’s going on, so we have this explicit check mechanism, I think, where we develop that.

**1:38:05** · Lex Fridman: So there’s a vast chasm between yeah and neh. Again, that subtlety of human communication. You’ve written about the experience that people have of feeling, quote, “a little bit autistic.” Could you elaborate on this concept?

**1:38:25** · Dave Plummer: Yeah, I think a lot of people, maybe 10 to 20% of the population, is somewhere on the autism spectrum, but isn’t impacted by it enough that it rises to the level of a disorder. But they still have many of the characteristics that arise from autism. And I think if they can understand and identify and manage some of those behaviors in an optimal way, they can both leverage them and take advantage of some of the skills and mediate some of the deficits and problems that come with it. And I wrote it mostly for my kids because none of them, as far as I know, have ASD, but they’ve all got certain aspects of my behavior that are particularly related to it, so I thought I’d write a little manual for them, basically.

**1:39:02** · Lex Fridman: Hmm. Why do you think so many programmers, like excellent, great programmers and great engineers, are on the spectrum?

**1:39:08** · Dave Plummer: I think it’s that single-minded focus and the ability to reduce a problem, and to be ultimately curious about what’s inside stuff. That’s been an obsession for me my whole life: what’s inside? I gotta take my mom’s oven apart because I gotta know how the flip clock works. And I think that’s a good habit to have if you’re gonna be a programmer.

**1:39:26** · Lex Fridman: And being willing, being excited to get into the details. Yeah. What’s a cool thing you hope to program to build this year? What are you working on? So we got the RL learning how to play Tempest. Where are you on that, by the way? Like, what’s the ETA on success and dominance? Like victory?

**1:39:47** · Dave Plummer: Well, it’s very close to working. I think now it’s tweaking the model size and layers and stuff like that to get it to learn past the one threshold. But, you know, it’s a couple thousand lines of Lua and it’s a couple thousand lines of Python, and they all interact and they all work, so it’s like 95% of the work is done now. It’s tuning hyperparameters and hoping for the best.

**1:40:04** · Lex Fridman: So it’s already a success in a sense, but now you’re seeing how far can this go?

**1:40:08** · Dave Plummer: Yeah, my goal was to be able to beat me.

**1:40:11** · Lex Fridman: That’s tough for.

**1:40:13** · Dave Plummer: It is, but lots of games now are, you know, they play them better than humans, but maybe not games this complex.

**1:40:19** · Lex Fridman: What other cool things are you working on? What do you hope to build this year?

**1:40:22** · Dave Plummer: The PDP-11 stuff, I’m trying to get what’s called an RA82 drive. It’s the big 14-inch monster that spins at 3600 rpm and sounds like a washing machine. And then I’ll find the controller card and write the code and integrate it into the driver and try to get that all working.

**1:40:35** · Lex Fridman: What kind of code are you trying to run on it?

**1:40:38** · Dave Plummer: I’m going to have to get the driver stack to work, so I have to incorporate the driver for it into the kernel.


### Fastest programming language

**1:40:43** · Lex Fridman: You built a machine recently with one terabyte of RAM. How did that happen and why?

**1:40:52** · Dave Plummer: We have a project called GitHub Primes. If you just search for GitHub Primes, you’ll find it, and it is…

**1:40:57** · Lex Fridman: GitHub Primes.

**1:40:57** · Dave Plummer: …a single set of prime number algorithms implemented in about 100 different languages. So it’s the exact same algorithm, and we require that you follow certain rules to make it fair. Then you express that algorithm in whatever language you choose to the best of your ability, and we run a benchmark every night, and we compile the results and find out which languages are fastest.

**1:41:16** · Lex Fridman: Is this the one? Oh, so this is it. You’re using this for? Oh, so-

**1:41:25** · Dave Plummer: So-

**1:41:25** · Lex Fridman: This machine runs those tests? Okay, you’ve got to tell me about this project. This is an epic project. So you’re comparing the performance of the different programming languages.

**1:41:34** · Dave Plummer: Of all these languages. So they all get built into an individual Docker container, and then they all run. And so-

**1:41:38** · Lex Fridman: This is an incredible project. This is really, really cool. It’s really measuring the performance of the different languages. So what have you learned about which languages? Which language usually wins?

**1:41:51** · Dave Plummer: Zig, I think right now.

**1:41:52** · Lex Fridman: Zig.

**1:41:52** · Dave Plummer: It does, it varies. People will make an improvement to the C++ then it’ll pass for a while, and then the Zig guys will get angry and come back and make it faster.

**1:41:59** · Lex Fridman: So Zig, Rust, C++, C? And what kind of code is being run? What’s the piece of code that they’re trying to run to measure the performance?

**1:42:10** · Dave Plummer: So what they’re doing is they’re solving the primes up to 100 million as many times per second as they can in a five-second loop.

**1:42:17** · Lex Fridman: And so it’s a loop, got it. Over and over and over and over and over again.

**1:42:19** · Dave Plummer: Yeah, on all cores.

**1:42:21** · Lex Fridman: So what-

**1:42:21** · Dave Plummer: Across all CPUs.

**1:42:22** · Lex Fridman: What about, like, how the program is written? Does that vary?

**1:42:25** · Dave Plummer: No. So you can do anything you want, but it has to be a prime sieve. You’re allowed to use one bit per integer at most, so you can’t use a byte, which is cheaper and easier. There are a number of rules like that that you have to allocate the memory within your timed loop. And so we have a set of rules and we have some solutions that don’t follow the rules like the 6502 because you’ve only got 64K, you can’t do 100 million sieve. So there’s a lot of solutions like that that we run as exhibition projects, but among the main languages, they all follow the same rules, and so it really should just be the how the algorithm is expressed in that language. And many of them use the same backend compiler, so it really is how you’re expressing it and the limitations or the benefits of that language.

**1:43:04** · Lex Fridman: They’re allowed to be multiple submissions per language?

**1:43:07** · Dave Plummer: Yeah, yeah. So if you look in the C, there’s like five, I think.

**1:43:10** · Lex Fridman: Okay. And then they, some of them might use different compilers, or no?

**1:43:14** · Dave Plummer: Yeah, some are GCC, some are Clang, LLVM.

**1:43:17** · Lex Fridman: I’m looking at a snapshot here from a couple years ago, Zig was at the top, then Rust, then Nim, Haskell. Oh, no, this is not, this is not ordered by slowness, or is it? It is.

**1:43:28** · Dave Plummer: So C would be 1.5 times as long as Zig.

**1:43:31** · Lex Fridman: Wow. Okay. Fascinating. Well, it’s a super cool project.

**1:43:36** · Dave Plummer: And we’ve got in crazy languages like PowerShell. There’s a version in PowerShell, and stuff like that.

**1:43:41** · Lex Fridman: So this is automated, like in terms of organization of like how the submissions are done, there’s a structure to it? That’s cool.

**1:43:47** · Dave Plummer: Yeah, there’s two guys over in Europe Rucker and Tudor basically own this now. I started as just three languages, I did Python, C#, and C++. And I checked them in and I published the episode, and then people started throwing more solutions in there and it just got out of hand, so I had to get somebody to manage that one and they’ve been great doing that for me.

**1:44:05** · Lex Fridman: What’s the happiest moment for you when you’re programming and building a thing? Like, what do you enjoy most?

**1:44:11** · Dave Plummer: I think the most fun for me is when I build something complex, and I’ve thought through how it should work, and then I run it and it does work that way. That creates intense satisfaction. So seeing the results come out the way that I planned them and have it work, because it rarely does the first time, but…

**1:44:28** · Lex Fridman: Yeah. Or especially if it does work the first time.

**1:44:31** · Dave Plummer: I never trust that. I always feel like I’m missing something.


### Future of programming

**1:44:33** · Lex Fridman: That’s true. But, you know, with compiled languages like C++, that’s always a good feeling. You write a bunch of code, and you compile it all, it compiles without warnings, without errors. It’s a cool feeling. What do you think is the future of programming? So now, I don’t know how much you’ve got to really experience the impact of LLMs with code generation. Have you used Cursor much, Cursor VSCode with code generation?

**1:45:05** · Dave Plummer: Yeah, I’ve done a ton of it for the Python side because I’m not great with Python, and I’m kind of new to it. So I found it very helpful because I’ve learned a lot from watching the code that it generates if I don’t know how to do something. Because if I were to write Python from scratch, it’s going to be about four times as long as what the AI can crank out because Python can be pretty terse if you’re good at it.

**1:45:23** · Lex Fridman: Oh, that’s cool. So you essentially learned Python for this project?

**1:45:27** · Dave Plummer: Yeah.

**1:45:29** · Lex Fridman: So this is a good case study of a great programmer in C++ quickly learning a language.

**1:45:36** · Dave Plummer: Yeah, I’m vibe coding my way through it, I guess.

**1:45:38** · Lex Fridman: Vibe coding your way through it. I mean, that is a really powerful use case to learn a language for. If you’re already a good programmer, to learn either a new language or a new way to approach a problem by having it generate it because you already you probably understand the Python code it generates.

**1:45:55** · Dave Plummer: Yeah.

**1:45:56** · Lex Fridman: Like without actually looking up any of the syntax.

**1:45:58** · Dave Plummer: Yeah, it’s all pretty self-explanatory once you see it but, you know, creating it from whole cloth is a little different, so.

**1:46:03** · Lex Fridman: Yeah, but you still have to learn how to program in order to use it in that way.

**1:46:08** · Dave Plummer: Oh, and to read it and to know what to tell it to do next and all that, yeah. I don’t think you can vibe code yourself if you’re just new and haven’t coded but if you’re a good programmer, AI can make you incredibly powerful.

**1:46:19** · Lex Fridman: What do you think is the future of programming, like 5, 10, 20 years from now, this whole process? Now, vibe coding is kind of a fun meme thing because you still have to be… The people that don’t know how to program and are just vibe coding are almost entirely creating systems that are not usable in production. They’re not… It’s very difficult-

**1:46:38** · Lex Fridman: It’s very difficult to create a product. And the people who are already great programmers kind of vibe code just for… in the way that you’re doing it. They’re basically… it’s just a fancy autocomplete, and they end up editing it, or it’s a way to learn a new API, or new language, or a new whatever, a new specific use case, or maybe a different kind of gooey component or something like that. But as they get smarter and smarter, we don’t know where the ceiling is. That might change the nature of what it means to be a programmer. So do you think about that?

**1:47:12** · Dave Plummer: I do. I don’t want to say prompt engineer, but I think it’s going to be something like that in the sense that if you’re an architect building a bridge, at some point, guys were down there welding beams together, but now you’re dragging things around in AutoCAD and assembling from big pre-formed sections. And I assume that’s what programming will be like. You won’t be in there throwing individual lines of code around; you’ll be moving components and interfaces and describing to the AI what those interactions should be and letting it build the components. But I think we’re still quite a ways from it being able to whole cloth generate… You can’t say, “Give me a Linux kernel that’s compatible with Linux.” One day, we’ll be able to, and it’ll crank it out, but we’re not there yet.

**1:47:51** · Lex Fridman: Does it make you sad that we’re climbing the layers of abstraction so quickly so you, somebody that used to do machine code and then assembly, then C and C++, that we’re getting to a point where we’re vibe coding with natural language?

**1:48:07** · Dave Plummer: Yeah, I kind of came up at a really fortunate time, I think, because I had to come up with the technology over the course of 30 or 40 years, so I understand TTL logic, and I can use AI to write code, and I kind of know all the pieces in between. There certainly are holes in my knowledge, but I think the only way to have got that level of knowledge or the completeness of that picture is to have lived it for that long. And it’s going to be hard to duplicate that for people starting now.

**1:48:32** · Lex Fridman: What do you think is the meaning of this whole thing? Of existence of life, whatever is going on here?

**1:48:44** · Dave Plummer: Making cool stuff. I guess, fundamentally, what I care about is being able to make complex things that are useful to other people, which leverages my abilities in a way that allows me to be creative and to create things that other people can use in a way that if I was limited to painting or sculpting or whatever in the classic arts, I would be hopeless. And so for me, that’s really the meaning of life, and then maybe you raise a couple of good kids to hand the baton off to.

**1:49:14** · Lex Fridman: Yeah, and you’ve created a lot of cool stuff over your life that impacted millions, probably billions of people, and now you’re inspiring… You’re creating cool stuff for everyone to see on your YouTube, and you’re inspiring people in that way. So for everything you’ve done in the past and everything you’re doing now, I’m a big fan. I’m really grateful for what-

**1:49:40** · Dave Plummer: Great.

**1:49:40** · Lex Fridman: … you’re doing and grateful that we got a chance to talk today. Thank you, brother.

**1:49:44** · Dave Plummer: Thank you.

**1:49:46** · Lex Fridman: Thanks for listening to this conversation with Dave Plummer. To support this podcast, please check out our sponsors in the description. And now, let me leave with some words from Bjarne Stroustrup, creator of C++ and somebody who, by the way, I interviewed a long, long time ago, Episode 48 of the podcast. He said, “There are only two kinds of languages. The ones people complain about and the ones nobody uses.” Thank you for listening, and hope to see you next time.
