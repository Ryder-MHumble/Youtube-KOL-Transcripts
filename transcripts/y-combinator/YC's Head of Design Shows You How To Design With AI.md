---
title: YC's Head of Design Shows You How To Design With AI
source_url: https://www.youtube.com/watch?v=VbqaL_eHhKY
video_id: VbqaL_eHhKY
account: '[[accounts/y-combinator|Y Combinator]]'
account_name: Y Combinator
account_url: https://www.youtube.com/@ycombinator
featured_people:
- '[[people/eve-bouffard|Eve Bouffard]]'
- '[[people/aaron-epstein|Aaron Epstein]]'
published: 2026-07-10
created: 2026-07-23
language: en
speaker_attribution: contextual
description: AI isn't just changing the tools designers use. It's changing the way they think, prototype, and build.In this episode of Design Review, YC Head of Design Eve Bouffard joins General Partner Aaron Ep
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=VbqaL_eHhKY)

AI isn't just changing the tools designers use. It's changing the way they think, prototype, and build.  
  
In this episode of Design Review, YC Head of Design Eve Bouffard joins General Partner Aaron Epstein to share the AI-first workflow she uses to design products, websites, and events.  
  
Using projects like Paxel, SOTA Zine, and YC Startup School as examples, she explains how coding agents are transforming everything from rapid prototyping and branding to design systems, and why the biggest bottleneck is no longer software. It's imagination.  
  
Paxel: https://paxel.ycombinator.com  
SOTA Zine: https://www.sotazine.com  
YC Startup School: https://www.ycombinator.com/startupschool  
  
Chapters:  
00:00 — AI Design Toolkit: Conductor, Paper Design, & Voice  
01:27 — Project 1: Paxel — Spotify Wrapped for Coding Sessions  
04:13 — Building the Paxel Landing Page  
05:23 — Custom Shader Fine-Tuning Tools  
07:13 — Designing for Humans vs. Machines  
08:31 — "Send to an Agent" Feature Request Forms  
10:18 — The Future of Locally Personalized Software  
12:53 — Project 2: SOTA Zine — Celebrating San Francisco  
14:34 — The Soul.md File as Source of Truth  
16:57 — One-Shot = 16 Website Variations  
20:06 — When the Agent Surprises You  
21:50 — How to Break Out of Generic AI Design  
23:20 — Building an Interactive SF Map  
25:17 — Project 3: Startup School 2026 Branding  
26:32 — Automated Speaker Card Generation  
27:50 — Shader Fine-Tuning and Perfect Loop Recording  
29:43 — Personalized Acceptance Tickets  
30:49 — Shader-Driven Branding at Arena Scale  
  
Apply to Y Combinator: https://www.ycombinator.com/apply  
Work at a startup: https://www.ycombinator.com/jobs

## Transcript

### AI Design Toolkit: Conductor, Paper Design, & Voice

**0:07** · Today I am excited to welcome back E Bufar, the head of design at YC to talk about some of the really cool projects she's been working on and the design process behind them. So E, thanks so much for joining.

**0:20** · Thank you so much for having me.

**0:22** · So start off, tell us about some of the tools that you've been using because I know that they're very different from the tools that you were using over the last 6 to 12 months. Yeah. So, I find myself almost exclusively nowadays in conductor and paper design. That's all I need usually to make a full project end to end. And when it comes to finding inspiration for projects, especially like visual inspiration, I always go back to Pinterest and create maybe a little mood book for myself or put together a few images for the look and feel that I want for a project.

**0:49** · But all in all, it's almost entirely in conductor that I live.

**0:55** · Very cool. And um another interesting thing about the way that you work is you don't actually type, right? I do not type. I realize that I think a lot faster than I type. I type very slowly. And so I'd rather talk to my computer instead of I barely touch my computer at this point. I just press the function key and I give a stream of consciousness of the feature that I want to build and it just does it and it feels really magical. And to do this, I use Aqua, which is a YC company that allows me to just talk to my computer and captures everything.

**1:26** · So, there's a couple projects that we want to walk through today. Um, we're going to go through Paxel. We're going to go through Sodazine and Startup School.

### Project 1: Paxel — Spotify Wrapped for Coding Sessions

**1:33** · Yes.

**1:33** · And so, maybe to start um let's let's walk through uh the Paxel project which we just launched recently.

**1:40** · Maybe you can tell us a little bit about what is Paxel, what were some of the goals behind it, and then walk us through your process for how you actually designed uh the site and the product. The goal behind Paxel is an experiment that we're trying out and our goal is to try to understand how people code with coding agents.

**1:57** · Nowadays things are changing very quickly and people are experimenting in their own ways with coding agents and they're developing tricks for themselves and they're creating skills also for themselves and it still very much feels like a black box. We don't understand how our peers are coding with with coding agents. And so Axel was a way for us to understand how the world codes nowadays. What are the tricks and insights um and key takeaways that we can learn from people and share this knowledge with everyone else?

**2:27** · Yeah. And I love also that the product gives feedback, tells you your biggest crash out when you were when you were coding, \[laughter\] right?

**2:33** · Yes.

**2:33** · The main thing that we wanted to do with Paxel is to make it fun. We wanted to make it fun for someone to understand their patterns, how they code, and how other people code eventually. And the first version of Paxel is still very much single player mode uh because we haven't collected uh many transcripts yet. But as we collect more and more, we can tell you how your patterns compare to other builders out there. And we were heavily inspired by how Spotify made Spotify wrapped and how we can make Spotify wrapped for your coding sessions.

**3:04** · And so that's that's what inspired the playfulness of the cards. We interviewed some people in the office and we asked them, "What are the things that you'd like to learn from your from from your coding transcripts?" And one thing Jared Freriedman, one of the partners at YC, one of the ideas he had was, "I would love to know my biggest crash out. I would love to know when I was the most uh frustrated with my agent and what I said." And so that's one of the prompts or one of the cards that we that we also show to people when they upload their transcripts.

**3:32** · And so walk us through how the product works. So, how Paxel works is you simply run a command in the terminal and it's going to pull transcripts and it's going to read all your codecs cla um and cursor transcripts and going to return fun facts about you. And some of them could be, oh, you really love one model more than another or most of your commits are submitted in the middle of the night or do you use plan mode or not? What is the most common prompt that you that you go for or reach for?

**3:58** · Tell me how you built the site here to to show that off and uh explain to people how it can be used.

**4:07** · What I really wanted to do here is to be really explicit to people who will who will be landing on this page what our motivation was. I really wanted to be upfront with the fact that this is an experiment that we're running. We're trying to understand how the world codes and that's why it feels maybe a little bit unusual to see so much text on a landing page, but assuming that people are coming into this product to understand what it does, we wanted to I wanted to put it like very front and center as you load the page.

### Building the Paxel Landing Page

**4:36** · That's what motivated the the cards, the interact interactive cards here that you can hover over and you have some movement and and micro interactions when you hover over them. that also inspired the feel of this page. And another thing is I wanted to have a consistent uh visual language throughout the site and I wanted to experiment with some shaders and we love paper shaders, the shaders that are made by paper.design and I really love their dithering shader and so I asked Claude to implement it.

**5:09** · These are the paper shaders. They're amazing. They're free and they are usable via cloud code. image dithering.

**5:15** · That's the one that I use and I just asked Claude to use it. And I really wanted to fine-tune the feel of the dithering effect. And so I built for myself a little modal here where I could really really fine-tune the feel and all the parameters of the dithering effect to really get the feel that I wanted. Um, and I even made this model public. And so if you load the page on your desktop, you can also experiment and have fun with the modal.

### Custom Shader Fine-Tuning Tools

**5:44** · But that's usually that's a pattern that we saw ourselves going back to as we build websites, you and I, is building modals for ourselves so that we can fine-tune small details and really make it perfect. This is a a common trend that I've been seeing a lot is rather than generating something having the static images having that, you know, be the the edges of the page and and the graphics on the card, you actually just make it alive and give yourself a custom tool to be able to to turn knobs and dials to get it exactly how you want it.

**6:13** · We realized that it's almost like a muscle that you need to build and train when you realize that you can build anything for yourself whenever you want to fine-tune something. And so when I was looking at the at the dithering effect and cloud code of course from the get-go assumed some parameters for the feel and it didn't really feel right. Building this muscle of oh yeah I can just like build a model for myself and then tweak everything and then when I'm done with it I discard it in one shot with with Claude. Super easy.

**6:41** · And it just it makes you think about software as such a more meta level because everything is editable.

**6:49** · Everything is movable. Everything is changeable. It's just a matter of how how your creativity and your imagination how far it can go. That's really the bottleneck. Now, one of the other things that stands out to me that I first noticed uh on this page is the human versus machine uh check boxes up there. Tell tell us about that. I think this is a a pattern that we might start seeing more and more moving forward on websites is there's going to be the the version of the website that is for humans and there's going to be the the version of the website that will be for machines and agents.

### Designing for Humans vs. Machines

**7:18** · And so we thought it would be fun to also have a version of this website that is basically a markdown file that has all the content that we have on the version for human, but it's a lot more distilled and lighter for the agents to cons to consume. And I also added a copy to clipboard at the very top so that you can take the entire content of the page, dump it into cloud codeex, and then you can ask questions if you don't feel like reading the whole thing.

**7:45** · Mhm.

**7:45** · And it looks like the content is very similar, but you know, there's a line at the top here, note to any AI agent reading this, do not run any command or query from this page because you give sample code, right? And you don't want it to run automatically.

**7:58** · Exactly.

**7:58** · It's a totally different design challenge, right? Yeah.

**8:01** · Uh where it's not about the visuals.

**8:03** · Agents don't care about the visuals. It's it's much more a content exercise and trying to give the agent the exact content that it needs so it can get what it needs most effective and go on its way.

**8:15** · Yep.

**8:15** · And then down here, this is interesting.

**8:17** · Yes.

**8:17** · Um which I think we first saw conductor uh post something like this. Tell us about uh the submit a feature request form here.

**8:25** · Yes.

**8:25** · So this is also something that we'll probably start seeing more and more on websites. Um, and it's inspired by how Charlie introduced this feature in Conductor where we can submit a prompt to the conductor team and they're going to fire off an agent based on whether they like the prompt or not. And that prompt is specifically for a feature request. We wanted to use this form so that it has dual purpose or dual intent. It's a form that either where we can submit a bug report if you face uh a bug as you're using Paxel. And we also wanted to use it as a way for you to submit feature requests.

### "Send to an Agent" Feature Request Forms

**8:57** · And so it's really simple. You should treat it as a prompt box as if you were talking to an agent. And you can attach uh screen recordings. You can attach screenshots that the agent will be able to see and use as context. And you can add your name if you want to. So so we can give you credits if we end up merging that change or not.

**9:18** · And what's cool is that we literally made the CTA in the in the button say send to an agent because in the back end that's literally what what happens is that the moment you send your prompt it fires off an agent it opens a PR and we're the ones who who decide if we want to merge it or not. But I really think that this is the future of where how software will be built in the future. Yeah, it's really cool because it lets anybody that is a user of the product help shape the direction of the product and especially as the developer of the product and the designer of the product.

**9:48** · All you have to do is see the prompts that come in and say, "Yeah, that's a really good idea. We should do that." And then say accept.

**9:53** · Exactly.

**9:53** · Exactly. And also the the beautiful thing about collecting names is that you can thank people and you can give give people credits after. One of the interesting things from a design perspective is you can imagine this can make local software that people are using even more personal. Yeah.

**10:10** · You know, right now these go back to you and and the agent and then humans decide that are not the the person that's using it submitting this. You can imagine a world where anybody who's using a piece of software, they could just prompt it.

### The Future of Locally Personalized Software

**10:25** · You could give the ability to prompt it or customize it or redesign it or, you know, add features, remove features. it make it it so specifically personal to the person that's using it and they could be able to implement those changes themselves in their own local copy of the product that they're using. Let's take a look at uh what a report looks like from here.

**10:43** · After you run the command and we analyze your transcripts, we give you a report that lands in your inbox and is going to give you some fun facts about how you code in the form of these fun cards.

**10:55** · And if you scroll down a little bit, you also get a more detailed view uh into your your patterns and the way you make decisions um and also potentially some what are your strengths and some growth areas that you can focus on. And again, as we get more and more and more transcripts, we're going to be able to give you a lot more insights into how you do special things and how you are different from other people and how you compare to other people, which I think will be incredibly valuable long term.

**11:21** · I think at a higher level, Paxel is our way to shed light into something that is very obstructed right now. Like coding transcripts leave very live very deeply in your machine and they're really hard to pull if you most people are probably not aware that they are on their machine. Like they they don't even know that really transcripts exist and that they can do things with them.

**11:48** · And so Paxel is our way to put them at the surface and allow people to understand from their patterns because otherwise it's it's hard to know that you can actually analyze them or that you can do things with them.

**12:04** · Yeah, there's a lot to learn and there's a lot of valuable feedback you can get from it about I mean this is what it is to be a developer. this is how a lot of design work is happening these days and um there's a lot that can be learned from feedback on how you were doing it especially because it's so new. Um everyone's trying to figure things out and so I think by analyzing a lot of these different transcripts and being able to give feedback it helps everybody level up.

**12:30** · Yep.

**12:30** · YC's next batch is now taking applications. Got a startup in you?

**12:35** · Apply at y combinator.com/apply. It's never too early and filling out the app will level up your idea. Okay, back to the video.

**12:44** · Awesome. Let's take a look at another project that you've been working on recently. Uh, what is Sodazine?

**12:48** · Soda stands for state-of-the-art and the idea came from Gary actually where he wanted to celebrate San Francisco. And so we wanted to work on this really fun project where we would work with different artists and writers in the city and celebrate San Francisco.

### Project 2: SOTA Zine — Celebrating San Francisco

**13:08** · Maybe first uh talk through how you designed the actual zen and then we can talk about the website because I I know you have some really interesting uh process that you use to to build that.

**13:18** · Yes.

**13:18** · So when we say zen, it's a literal physical zen. What's interesting is that specifically for the zen and the graphic design, the cover art and also some some art that is inside We intentionally wanted to go for something that had no AI involvement. We decided to go back to how we did it a few years ago and it was in Illustrator.

**13:42** · And these pieces of art, you can tell the second you look at them, they are highly intentional and highly detailed. And you can tell that someone spent months working on this.

**13:54** · Okay. So, you started with the physical zen.

**13:56** · Yes.

**13:56** · And then you you transitioned to making a website to show this off and and talk about um what your goals were with building this and the process that you went about to actually make it come to life.

**14:07** · What's great is that for every single meeting that we had about the Zen, we recorded every single one and I dumped the transcripts into a soul.md file specifically for that project. And I wanted to treat that soul.md file as the source of truth and exhaustive glossery of this project.

**14:28** · I wanted this file to have as much context as possly possible so that it can feed all the future decisions that we need to make regarding this project. It's interesting because there's probably a lot of people that are watching and their process is, you know, maybe they're doing client work, maybe they're working on an internal project and they're meeting with a bunch of, you know, stakeholders, maybe they're designing their own website.

### The Soul.md File as Source of Truth

**14:53** · Um, and they're thinking it through and and they would probably come out of that and they would jot down some notes and some highle takeaways and you're saying like, "No, you shouldn't do that. Instead, just record everything and just dump it all in a soul.md file and then use that as the basis for everywhere that you want to go afterwards.

**15:13** · Exactly.

**15:13** · I really think that's the that's the future. And we also wrote a manifesto for ourselves when we were working on this project. And of course, we dumped that manifesto into the soul.md. As much context that we can give the agent, the better.

**15:25** · Can you show that soul.mmd file?

**15:27** · Yes.

**15:27** · This is what it looks like. It is nothing more than a um a simple MD file and it has all the context and you can also break down MD files. You can create a hierarchy of the different MD files that you want. If you want to have like a design MD file specifically for your design and how to address design you can have a separate MD for your manifesto.

**15:50** · You have can have a in our case we could have had a different MD for the written content content in the zen. Mhm.

**15:57** · Um, you can dump it all in one single file. I haven't really seen one method being better than the other, but that's why we're all experimenting and figuring out if there's a better way. Overall, I think capturing as much information as possible and share that information with your agent is the best way to build software moving forward.

**16:15** · What were your next steps?

**16:16** · I wanted to experiment and I wanted to do very fast iteration and see multiple possible versions of what the the website could look like. And so I started in Pinterest with a mood board. I created a mood board with a few images that I really liked. This was sort of the vibe that I wanted to go for.

**16:35** · Something very rudimentary, black and white. And again, this was based on all the conversations that I've had with my colleagues and my friends that I was working on this project with. And so I started there. And then my first reaction was looking at this mood board is I wish I could just generate many many versions, one shoted websites based on this mood board really simply.

### One-Shot = 16 Website Variations

**17:01** · And so I downloaded a bunch of these um images and I fed them into Claude and I asked Claude, "Okay, you know the vibe that I'm going for.

**17:10** · You know the content that I want to show on the website. Here's the visual direction that I would love for you to draw inspiration from." and then oneshot a cool website based on that. I asked it to do that 16 different times. I built a glossery for myself going back to training this muscle of we can build anything for ourselves now. I wanted to build for myself really easy way to navigate through all the iterations that I'm building for myself.

**17:34** · And so building a single page here that has this collection of all the iterations that I'm playing with was just a really easy way. And as I started looking at them, I wanted an a way for me to bookmark the ones that I really liked. And so I oneshotted this feature that allows me to, you know, pin the ones that I like so that they automatically show at the top and I don't lose lose tracks of the one that I really like.

**17:58** · Yeah.

**17:58** · And so, okay, so to be clear, this is not a page that's publicly accessible on the website. This is a glossery that you have made for yourself. Yes. To be able to oneshot a bunch of different ideas for how to design the overall site to explore yourself using real content, real design direction based off of those images that you found on Pinterest. Yes.

**18:21** · Um and then create a bookmark system. So this is another great example of disposable design. Yes.

**18:27** · Where you can just whip this up really quickly, jump through a bunch of different iterations, and go, I don't like that. I don't like that. Oh, I I do like that. Oh, let's take this piece from this one and put it all together. And it makes it happen so much faster.

**18:39** · Yes.

**18:39** · Show us some of the iterations that you put together here.

**18:41** · As part of the sold at MD, I made sure to include the names of the different articles that we have in the Zen. And that was one of the main things that I wanted to highlight and show on at least the first version of the website that I had in mind. And again, because it's oneshotted, you don't expect like an incredibly high level of craft. you're just using this as an exploration tool.

**19:01** · So getting a feel of okay do I want to lay out all the all the titles of the articles like this or that that was another really cool exploration that I loved which is there's so many things so many cool things going on here cool font um there

**19:18** · was the date of the party that we threw the launch party that we threw for the zen that was included in there because it was also part of the soldm that is a beautiful thing when you realize when you unlock so much information for your agent your agent knows so much that when you're going to give it full reign and full you're going to unleash it to make iterations for you, it's going to surprise you.

**19:40** · It's going to include things that you would not have otherwise thought of. And that was almost like an AGI moment for us when we realized that wow it can see things ahead of us and it can really help us brainstorm even and come up with like really really original ideas. And so that was a really nice um surprise here. It's just like organically included the time of the party that we were hosting.

**20:02** · Also, the the fact that it's a Zen and so it added this uh code bar, this barcode, uh assuming that it's like a physical one that you can purchase in different um in different uh currency was also really cool. One thing that I wanted to experiment with is what if we had an actual map of San Francisco, an interactive map of San Francisco and it included this version where Oh, wow. Yes.

### When the Agent Surprises You

**20:26** · Where you it uh it reveals a map of San Francisco that is interactive and you can move around in the city and that is like fully living behind the oneshotted iteration that it built. So just like marvelous things and I think these sorts of levels of design oneshotable designs can only be achieved if you have a very detailed and and intentional design on MD or sold in MD.

**20:54** · You need to shepherd your agent to tell it exactly the vibe that you want to go for. If you can include screenshots, also if you can include a mood board, as much information as you can feed your agent so that it really understands what you want and then it's going to surprise you in the most beautiful ways.

**21:09** · Yeah.

**21:09** · I think a lot of people use Claude or they use codeex and they tell it to design something and they feel like it they get generic design back and this is how to break that.

**21:17** · Yes.

**21:17** · Which is really interesting and it's really easy. You just have to pull Pinterest or even like Google image and you find or even websites that you really like really websites that you really like and start bookmarking them and eventually use them. Give them to your agent and say this is something that I really like. And sometimes you love a website and you don't even know why you love a website. But it's okay. You don't need to understand why you love a website. Just give it to the agent. The agent will analyze it for you. It's going to understand eventually your patterns and the commonality between all the websites that you like.

**21:46** · It can tell you, oh, that's actually the things that you seem to like across many websites. This is another exploration that I really loved. Again, displaying the title of all the articles. And there are really cool hover effects.

### How to Break Out of Generic AI Design

**22:02** · Oh, wow.

**22:02** · That it created as you're exploring the different articles. And so for each article, it pulled really cool visuals. And you're at a point where you don't even know how club does does these things. It just it scrapes the web, it browses the web, it finds cool pictures, animations, and it's going to surface them like this.

**22:24** · And if there are some things that you want to fine-tune, you can just, you know, speak via Aqua and ask it to change things, change the color of things, change the feel of things. And it's just this incredibly fast and rewarding feedback loop that you have with your agent.

**22:38** · Yeah, it's amazing.

**22:39** · So, now we can talk about where we ended up is this fully interactive map of San Francisco. We thought, how fun would it be to build a map where people can drop pins and small stories of things that they've come across in San Francisco or like encounters or like delightful memories that they have of small moments in the city. And so we thought, let's make it fully anonymous.

**23:02** · People can share memories and the only thing that they need to do is pin a location or like pick a location and then tell us what happened at that location. And what's beautiful is that it allows people to share things that are very surprising and beautiful and intimate and introspective. Here we built this this fun little way to consume or like read through all these submissions.

### Building an Interactive SF Map

**23:29** · And it's again a way for us to go back to the core essence of this project which is how can we understand how people are experiencing San Francisco and what are the like magical small moments that we can all sort of learn from. We also build this little entry point for we built posters digital posters for the party that we threw the launch party that we threw.

**23:52** · There's also a substack that we created for this zen and we added this fun little entry point where you get redirected to this to the substack and then you can read the different articles. You can share a noticing or you can share a submission that you really like. So let's say this one I really like it. I want to send it to my friend. I can just click share.

**24:11** · It downloads it as a PNG and it outputs this and it gives you the cardinal coordinates of the location that was uh tied to this story and you can share this with your friends and you also know the street that it's in or that it's on.

**24:28** · So, we're actually putting on startup school at the Chase Center here in San Francisco and you did a lot of really cool work to help support that. I would love for you to show off some of the shaders that you created and some of the uh content that has been shared on social media and other platforms to help um bring attention to the event.

**24:46** · Yes, we're all preparing for Startup School, which is our biggest event of the year. It's going to be, as you said, at Chase Center. We're going to have more than 6,000 people coming from all corners of the world to experience SF and what it means to build with AI and have like this incredible sense of community of we're all building together. And we were able to have an amazing speaker lineup this year. We have phenomenal names coming. We have Jensen, we have Sam, Sam Sam Oldman, we have Alexander Wang, we have Jeff Dean, and so many others.

**25:13** · And we wanted a really cool way to share that lineup with the world. And when we were thinking more broadly about the design behind this event, we wanted to make it feel really Y, but more like a variation of YC. And so we experimented with of course orange but gradients of orange and we discovered the paper shaders and we thought maybe it would be a cool way for us to experiment with paper shaders.

### Project 3: Startup School 2026 Branding

**25:39** · My first intuition when I thought about building visual assets for how we're going to share these speaker cards on on social media.

**25:48** · I I've initially started in Figma actually. I I've initially dropped um some of the images that we got from our speakers and I started making it myself moving things around and I noticed well we're going to have many speakers and I don't want to move things around 12 times and so I thought it would probably be just simpler to ask Claude to make a template for myself and it can even like pull images for me from my inbox and do everything for me so that it feels as light as possible and I can also have an

**26:20** · easier time experiment with the visual feel of the cards. And so I built this tool for myself. It's a very simple tool where we have the names of all of the speakers that are confirmed. And it just automatically generated all of the all of these as we kept having more and more names of speakers confirmed.

### Automated Speaker Card Generation

**26:42** · And I also built a way for myself to experiment with different ways to lay out the the text on these on these cards. And we ended up going for this one. But it was fun to really easily almost one shot in different iteration of layout for each of these cards. And these are like compatible across the board.

**27:01** · And for the shaders, well, we use the the movement that comes from one of the uh shaders made by paper.design and we fine-tune the graininess here and the edges and the rotation, the scale um like this. And I had a lot of fun really finding the variation of the shader that I wanted. And so I can just refresh and it resets. But that was also a very helpful sort of mini tool that I built for myself.

**27:31** · Um, and another thing is I wanted to because I wanted to keep the really cool movement that is happening behind, I needed to do a screen recording to maximize the resolution of the card. And so I built this little screen recording tool for myself that tells me exactly when I need to start the recording and when I need to stop.

### Shader Fine-Tuning and Perfect Loop Recording

**27:52** · And the reason I built this tool is because I really wanted it to feel like a loop, a perfect loop, so that when we post it on Twitter and on Instagram, it loops very very smoothly and it feels like a like an endless sort of movement. And so I asked Claude to build this specific tool that gives me like this 4se secondond like perfectly designed loop so that it starts and end at the exact same pixel that it feels really smooth.

**28:20** · We thought it would be really magical if people received a ticket uh when they get their acceptance. And so we designed this ticket reusing the shader that we're using for all the other visual assets that we have for startup school. This time we would apply it against a a ticket and we would try to make it as personalized as possible.

**28:44** · So, we render your name and we render the city that you're from and then some information about the about the event. And it's been such a delight to see people share them on social media and say that they are excited about coming to SF and experience SF sometimes for the first time.

**29:01** · Yeah.

**29:01** · Could you imagine a year ago trying to build something like this? It wouldn't be worth it. these shaders.

**29:06** · Building these shaders a year ago would have been like would have felt like this insurmountable mountain of I would not even have known where to start to build these things. And now it is just this thing that Claude, my claude knows what to pull cuz it it knows that I love paper. It knows that I love their shaders and it's just automatically knows how to pull that all that information from their website and it uses it. It's just really magical.

**29:32** · It's really cool to see this and it feels like so much time and thought and attention and care went into designing the experience from the moment that you get accepted until all the way through when you show up to the event and see the amazing lineup there.

### Personalized Acceptance Tickets

**29:47** · Yes.

**29:47** · Yes. And it's also it's going to be amazing to keep building more of the branding of Startup School with Claude and Codeex and like coding agents. It is such a different paradigm as to how we even do branding design moving forward.

**30:01** · the fact that we will be able to use that same shader with the same parameters on the massive screens that we're going to have throughout Chase Center and keep it incredibly consistent through and through. It's amazing. Like I'm really really excited about this and it's just easier than ever to make things more consistent and use coding agents for absolutely everything.

**30:21** · Yeah.

**30:21** · Amazing. Ev, thank you so much for joining and and showing us the behind the scenes of how you've done some of this incredible work. um things that I think are really pushing the boundaries forward that uh are ways that are going to be super common for how designers are designing in the future, but not a lot of people I think have figured out yet. So, I really appreciate you sharing that process.

**30:39** · Thank you. We're we're all figuring it out together and we're having a lot of fun doing so.

**30:43** · That does it for this episode of Design Review. We'll see you on the next one.

### Shader-Driven Branding at Arena Scale

**30:51** · \[music\]
