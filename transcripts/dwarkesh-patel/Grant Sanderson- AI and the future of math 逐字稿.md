---
title: Grant Sanderson (@3blue1brown) – AI disproved a famous math conjecture. Now what?
source_url: https://www.youtube.com/watch?v=TfyPshgMbug
video_id: TfyPshgMbug
account: '[[accounts/dwarkesh-patel|Dwarkesh Patel]]'
account_name: Dwarkesh Patel
account_url: https://www.youtube.com/@DwarkeshPatel
featured_people:
- '[[people/grant-sanderson|Grant Sanderson]]'
published: 2026-07-01
created: 2026-07-21
language: en
speaker_attribution: contextual
description: Always so much fun to chat with @3blue1brown AI has been making much faster progress in math than in other fields. As a result, mathematics is showing us, very concretely, what AI progress in other
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=TfyPshgMbug)

Always so much fun to chat with @3blue1brown  
  
AI has been making much faster progress in math than in other fields. As a result, mathematics is showing us, very concretely, what AI progress in other fields will look like. Even within mathematics, there's a jagged landscape. What does it look like?  
  
What is the nature of the most important conceptual breakthroughs in the history of mathematics, and how different are they from what AIs are currently able to do?  
  
Does AI (on net) increase or decrease human understanding of the field?  
  
How big is the overhang from having AIs systematically try to connect ideas already in the literature?  
  
And what advice does Grant have for aspiring mathematicians, coders, and other students who are passionate about fields that are being most transformed upon by AI?  
  
𝐄𝐏𝐈𝐒𝐎𝐃𝐄 𝐋𝐈𝐍𝐊𝐒  
\* Transcript: https://www.dwarkesh.com/p/grant-sanderson-2  
\* Apple Podcasts: https://podcasts.apple.com/us/podcast/grant-sanderson-ai-and-the-future-of-math/id1516093381?i=1000774870615  
\* Spotify: https://open.spotify.com/episode/0X3t4uRlpVT4MXPYDIrNYX?si=HZf\_0Ky2Q42tOWYZNvWi6w  
  
𝐒𝐏𝐎𝐍𝐒𝐎𝐑𝐒  
\* Gemini 3.5 Live Translate is what I wished I'd had on my last trip to China. It detects more than 70 languages and translates them in near real-time… and it preserves your original pacing and intonation. If you're building an app that needs live translation, you should check out Gemini 3.5 Live Translate. Get started at https://ai.studio/live  
  
\* Cursor’s harness lets me use models for a huge range of tasks at the podcast. For example, Cursor cuts out the ads from each episode I produce so I can post them on Bilibili. It also helps me prep for interviews — I have a repo full of books and papers that Cursor sorts through to find the exact right file for any given question. Try Cursor yourself at https://cursor.com/dwarkesh  
  
\* Jane Street sponsors 3Blue1Brown, so Grant has gotten to spend a lot of time with various Jane Streeters. He actually just recorded an interview with a few of them, so when we sat down for this episode, he told me about some of the things he learned, like how Jane Street keeps their role definitions fuzzy to make sure their people keep learning and growing. Go check out Grant’s full interview at https://3b1b.co/janestreet  
  
To sponsor a future episode, visit https://dwarkesh.com/advertise.  
  
𝐓𝐈𝐌𝐄𝐒𝐓𝐀𝐌𝐏𝐒  
00:00:00 – AI is discovering new proofs. Is that AGI?  
00:11:32 – The verification loop on conceptual breakthroughs can be a century long  
00:26:12 – Will we understand an AI proof of the Riemann hypothesis?  
00:38:08 – Can AI find the hidden bridges between fields?  
00:53:48 – Why real-world tasks don’t fit into RL environments  
01:07:07 – Good writing requires theory of mind that AI still lacks  
01:16:02 – Why learning will still depend on human curation

## Transcript

### AI is discovering new proofs. Is that AGI?

**0:00** · Today, I'm chatting with Grant Sanderson, who runs 3Blue1Brown and is now working on a new project documenting the progress AI is making in math. I wanted to talk to you about this because AI has been making the fastest progress in mathematics out of any other field.

**0:13** · Whatever is happening here, and whatever way we're seeing AI progress happen or not happen, will tell us about what will happen to the rest of the world as AI gets better and better.

**0:21** · I wanted to start with this question I asked you when I first interviewed you three years ago.

**0:26** · I asked you, once we have AIs that can get gold in the International Math Olympiad, wouldn't that just be AGI? Wouldn't this just be able to do anything any human can do, given how hard these problems are?

**0:35** · You had an answer, which in retrospect turned out to be very wise and correct.

**0:40** · You said it'll be another benchmark, like all these other benchmarks that AI are passing.

**0:43** · Obviously, AI has gotten better in a general way since then, but there won't be some "aha" moment when this happens. First, I'd be curious to get your heuristics on why that turned out to be true. Second, I'm curious how long you think this narrowness can continue to be true. By the point that AI has solved a Millennium Prize problem, do you think it's still possible that there are lots of tasks humans are doing that AI still can’t automate in the economy? It's an interesting question because it's hard to answer without knowing what the solution looks like ahead of time.

**1:16** · If we take the IMO, the spirit of your question three years ago was in looking at how some of the solutions to these problems really seem to require creativity.

**1:26** · The designers of these problems try to come up with things that you can't train for as easily.

**1:32** · The dirty secret with the IMO is that you really can train for a lot of them.

**1:38** · With the whole AI and math project underway, as you point out, one of the reasons it's interesting at all is that there's a spiky frontier to AI, and math is just right there in one of the spikes.

**1:48** · But there's a fractal nature to that spikiness, because when you zoom into the specific progress within math, you have some things that are a lot easier than others.

**1:56** · If we just think about IMO, which is old news at this point.

**1:58** · It's been two years since they're really doing quite well.

**2:01** · They would have gotten a gold in 2024 if not for the following reason.

**2:05** · They're very good. They just cold-solved geometry basically.

**2:10** · The IMO has these four categories of problems: geometry, number theory, algebra, and combinatorics. Geometry, it just solves it in nineteen seconds since 2024 because it's a brute force solver. The dirty secret is that for students, there's also a brute force way you can go at it. Combinatorics is the wild card: much more playful, puzzly-seeming problems. There were two combinatorics problems on that year's test, and there's not always. There are four categories and six different problems, so it's a toss-up which one is going to have two questions.

**2:43** · Had it been more geometry questions, they would have gotten a gold that year.

**2:47** · But it struggles on those combinatorics ones. Someone who's trying to keep that torch of the last holdout of math for humanity might say those are the ones that require more creativity.

**2:59** · Even then, the spirit of your question—if they're solving a Millennium Prize problem, does that also service a lot of white-collar work?—suggests that whatever the rate limiter is between where we are now and that is the same as the rate limiter for making things better at white-collar work.

**3:17** · We could paint a couple of different ways. If we focus on the Riemann hypothesis, what would it look like to solve that? These things are extremely good at a specific domain of knowledge, knowing it very deeply, and then knowing another domain, and another.

**3:35** · You've pointed this out. It's bizarre to have something with this superhuman breadth that knows all the fields so well, and yet isn't finding those lightning bolts that connect them.

**3:44** · I think we're starting to see sparks of it actually finding connections between the things it's an expert at. I'm sure we'll talk about it.

**3:51** · If the nature of the solution to the Riemann hypothesis was something like that, that feels pretty distinct to me from what's necessary to get good at white-collar work.

**4:00** · And there's a reason to believe that might be the nature of the solution.

**4:04** · I don't know if you know the story of Hugh Montgomery and Freeman Dyson at the IAS.

**4:11** · This is a side tangent, but it's a fun story. I don't know if it was over lunch or something like that, but you have this number theorist who is just trying to understand the statistical correlation between pairs of zeros of the Riemann zeta function.

**4:25** · The Riemann hypothesis is all about whether all these zeros sit on a straight line.

**4:29** · He finds this quantitative question you could ask, and he writes down a formula.

**4:32** · It looks like one over sine squared or something like that.

**4:35** · Freeman Dyson, a physicist, is like, "I know that expression.

**4:38** · That expression comes up in studying the eigenvalues for random Hermitian matrices," which was something that comes up in studying the energy levels of a nucleus.

**4:48** · The idea that the statistics of those two seemingly different things were the same prompted an exploration of whether there are aspects of random matrix theory that might be relevant to the Riemann zeta function. I think it's a little bit of an open question whether there is fruit to be had there. But that bridging together of two different fields—if it turned out that the solution to the Riemann hypothesis was exploring an idea like that even further—has the character of how you expect LLMs to be good at math.

**5:17** · They're experts at quantum physics. They're experts at analytic number theory.

**5:20** · They should be able to see that similarity in a way that doesn't require Montgomery and Dyson to be having lunch and happen to talk about it. That's totally different from white-collar work.

**5:30** · To the extent that you have a hard time using an AI as an editor, it's not because they know everything and you just need them to find that lightning bolt in between.

**5:40** · A different possibility would be… What's the right analogy?

**5:46** · Maybe if we think of Fermat's Last Theorem, between the moment of Fermat phrasing the question and what the solution itself looks like, where the solution ultimately involves such heavy machinery in math. The beauty of that problem is you can phrase it so simply. You ask about xⁿ + yⁿ = zⁿ.

**6:03** · Do you have integer solutions for this when n is bigger than three?

**6:09** · It's something you might expect there to be an elementary number theory approach to, but as far as we can tell, there's just not. Whereas the actual solution, maybe there is something simpler, but this might be what it has to be.

**6:22** · There’s such a complicated set of ideas that build on centuries of work centered around elliptic curves. Then there's this other mountain of ideas centered around these things called modular forms. Both of those mountains have to be built before you can ask the right question that connects them. If the solution to the Riemann hypothesis involved building a new mountain, that's a kind of skill—the ability to come up with the right new ideas—that feels sufficiently different from the character of how they're intelligent right now.

**6:51** · It's not like that's what you need from your hired video editor per se.

**6:54** · But if it's capable of building mountains that are the correct new theory crystallizing how we should be thinking about a subject, that's just such a level of intelligence that it would be surprising if it didn't permeate into other aspects of the economy besides just the mountain-building for math itself. Or at the very least, even if it couldn't literally do every single thing white-collar humans can do, it would just have transformative effects in the way that getting gold in the IMO did not have transformative effects on the world.

**7:24** · First of all, I do want to point out that I'm totally moving the goalpost here.

**7:29** · When I interviewed Dario two or three years ago, I asked this question about why they haven't been able to use their vast knowledge to connect ideas together and come up with a new discovery that way. That seems like the kind of thing where even a moderately intelligent person, if they knew this much information, would be able to come up with a medical diagnosis from the fact that this drug causes migraines, and this other thing does this, and maybe it's the same drug that can cure both things.

**7:52** · From an outsider's perspective, mathematics seems clearly like a field where finding the counterexample to the unit distance problem conjecture was an example of this kind of thing.

**8:01** · So it’s total goalpost moving. But then we can ask, what is the next benchmark?

**8:05** · Now that AIs can do this thing we should have thought they'd be able to do, what is the next thing that would be quite impressive? There are a couple of candidate ideas here.

**8:15** · One could be coming up with interesting problems in the first place, and the other is coming up with new kinds of objects or conceptualizations that create or unify fields.

**8:25** · On the first one, right now we have these Millennium Prize problems because mathematicians have noted them. Riemann came up with this idea of the Riemann zeta function because he thought the zeros of this function would have some connection to the density of prime numbers. Figuring out why we think this is an interesting thing to study in the first place, why we are building this object and trying to answer questions about it—and answer this particular question about it—seems like the kind of thing that would be the next benchmark. You highlight two pretty good examples there.

**9:03** · For anyone curious about the unit distance conjecture, there's this really nice video by a math channel called Polylog where they talk about it.

**9:11** · All of these discussions cause people to reflect on the process of doing math.

**9:15** · They're like, "Oh, this thing can do this impressive stuff.

**9:17** · What does that mean for us?" One of the people in that video highlights this quote: "good mathematicians prove theorems, great mathematicians come up with conjectures, and the greatest mathematicians come up with definitions." That's more or less exactly your framing here.

**9:31** · We need the conjecture generator and then the definition generator.

**9:35** · That's the premium-tier mathematician. I don't understand how exactly you'd make that a benchmark. Usually, when I think of the word benchmark, I'm thinking of something that is a goalpost. The ball is through the goal or it's not.

**9:48** · You can clearly say, "Yes, this is done." Partly that's to be able to do things like RLVR, but also partly just to know that you haven't moved the goalpost in answering.

**9:58** · OpenAI can have their headline on disproving the unit distance conjecture because it's a clear, distinct thing. It did it. Whereas imagine trying to have a headline on GPT-5.4 coming up with a really good conjecture. "We promise, everyone thinks it's a good conjecture." It just doesn't land the same way.

**10:16** · But maybe that doesn't negate the fact that it's the right thing to be thinking about.

**10:21** · I would be surprised if it ever took the form of looking like a benchmark, where we have a score saying it's passed because we can quantify how good a conjecture is.

**10:30** · The nature of what it would take is probably that you'd feel a tone shift in conversations with mathematicians about the way it's useful to work with.

**10:40** · This series you referenced, which is not at all produced yet and probably won't be for a couple of months, takes the form of us interviewing a lot of mathematicians.

**10:48** · What's interesting is that we started doing this over a year ago, and it's fun to see a little bit of a tone shift in the way they talk about AI between mid-2025 and where we are now in 2026.

**10:59** · In the real world, that's a very short amount of time.

**11:01** · In the AI world, that's eons. We're able to see this tone shift over those eons.

**11:06** · I think the way you'd measure conjecture-generating ability is going to be more subjective, based on that tone shift. It will be mathematicians saying they're not just using it to solve their problems, but that as they step back and decide what their research field should even be, a conversation with such-and-such model was genuinely helpful for that.

**11:24** · I don't think it's likely you'd see it in the form of a headline saying this was yet another benchmark knocked down. It's very interesting. The kinds of things you can't make benchmarks for are also the kinds of things, at least in the current paradigm, you can't easily train for. There's really no fundamental difference between a benchmark and a training environment. It's very easy to come up with some dichotomy of, "here's a deep reason why AI can't do a certain thing", and then it turns out you're just thinking about it the wrong way, and actually it can do it pretty soon thereafter.

### The verification loop on conceptual breakthroughs can be a century long

**11:57** · But I'm going to come up with— You're going to come up with a couple anyway.

**12:04** · It'll probably turn out that there are ways we can train AIs to do these kinds of things in the relatively near term. But it seems like it would have to be different from current RLVR training. The thing I'm curious about—and the thing that seems to me to drive a lot of the big progress in mathematics and in science generally—is coming up with a new way to think about a problem or a new way to understand the world that unifies different fields, spawns entire new fields, and solves problems we weren't even trying to solve in the first place. The reason Einstein was thinking about GR is not because he wanted to explain why light bends or why black holes exist.

**12:41** · These are phenomena he didn't even need explained in the first place.

**12:45** · In mathematics, as a total outsider who doesn’t even know what he’s talking about here, it seems like there are often ways to prove a specific problem that can motivate a new conceptualization—one which results in a whole new field, a whole new way of thinking, which is immensely productive—and ways which don't. I'd be curious to hear you talk about Galois coming up with group theory, distinguishing his solution to the quintic having no formula for the roots, and Abel coming up with a different proof a few years earlier that didn't come up with group theory.

**13:17** · If you wanted to do a verification loop on whether group theory is an interesting concept—was something useful done here, or why is this proof better?—potentially that verification loop is a hundred years long.

**13:28** · It involves cryptography coming around and physics making progress, and the ideas in group theory being relevant to understanding symmetries in physics.

**13:37** · There's a hundred-year verification loop on why this is a productive concept in the first place.

**13:44** · You struck a nerve, because I had this project about Galois I was going to do in 2022 that I put on the shelf, but I spent a year of my life thinking a lot about what he did.

**13:53** · There's a risk of me accidentally talking too long on the specifics, which you can hold me back on.

**13:59** · It's a perfect example for your case, because describing why it was a valuable insight does not come from immediate utility. Certainly, if you're thinking about RLVR environments, this is going to be really hard to do.

**14:15** · But it's interesting to note that even with human verifiers at the time, it took a really long time to recognize it as being useful. With Einstein and GR, people could feel this was a good theory right away. What makes Galois theory such an interesting example is that you literally have this hundred-year segment of an idea that flows through many different people's heads before it settles into something the math community agrees is good.

**14:41** · To back up a little bit… Do you want the background on the problem at all?

**14:48** · We all learn about the quadratic formula in school.

**14:51** · I thought you were going to say we all learn about group theory in school, but I missed that class.

**14:54** · We all learn about group theory… No, the quadratic formula.

**14:58** · This was known. In some sense, the Greeks could solve quadratics, but they didn't really write things in algebra. It's really the Arabs who wrote down that formula.

**15:07** · There's this delightful story about dueling Italian mathematicians—not real duels, just intellectual challenges—who secretly found a formula for the cubic, and then very shortly thereafter found a formula for degree-four polynomials.

**15:24** · So a natural open question for mathematicians is, can you find a formula that solves degree-five equations?

**15:30** · The degree-four formula is a monster. It would be wild to write it down.

**15:35** · You usually don't write it down in full. You break it up as a procedural thing.

**15:39** · You might believe these things have this exponentially increasing complexity.

**15:42** · So for many hundreds of years, nobody was really answering that question.

**15:45** · Usually, we say Abel was the first to prove it. He was this young, precocious Norwegian mathematician. He showed it's simply impossible.

**15:54** · It’s not that you can find a quintic formula. He thought he found one initially, but he showed it's impossible. I think the real credit though, you have to back up a bit and talk about Lagrange. He found the right kind of question to ask about this. I'll give it at a very high level.

**16:13** · He was studying the question and recognized that being able to solve these polynomials is very related to understanding the way certain algebraic expressions are symmetric.

**16:24** · If I write down a + b + c + d, just adding four variables, and I permute those, it doesn't change the value of the expression. Whereas if I write a + b \* c + d, some of the permutations don't change it, but some of them do. He had this really nice insight about how if you can find expressions that have four free variables, but all the permutations take on three distinct values, that has this unexpected relationship with being able to reduce degree four into degree three. He started approaching the question of whether we can find a quintic polynomial by wondering if he could extend that method.

**16:56** · To extend that method, you would have to have an expression that has five free variables such that as you permute them over all the five factorial permutations, it takes on only four values or fewer. You could put that in a puzzle book.

**17:08** · You could put that in a brain teaser that a twelve-year-old could engage with.

**17:13** · It's not too hard to find yourself feeling like that's an impossible task.

**17:17** · Lagrange is sitting there saying, "Here is a strategy to solve this problem of finding a quintic polynomial. It seems like it might be impossible, at least from this strategy." But that was the first time in history that people had the instinct that some kind of question about symmetry was the right way to study these polynomials. In his mind, it was just a way.

**17:37** · It had yet to be discovered that there was actually a tighter connection.

**17:40** · Also maybe rather than searching for the formula, we should be asking the opposite question: can you prove that it's impossible? He sort of planted that seed.

**17:48** · Around fifty years later, Abel definitely read Lagrange and was influenced by it.

**17:53** · We know that Galois loved Lagrange when he was falling in love with math.

**17:56** · It's very hard to imagine that these two young geniuses coming up with pretty similar insights around that problem wasn't born from Lagrange. But to your question on whether you are able to verify that this was a good idea, there wasn't any result that Lagrange came to.

**18:13** · He didn't solve the problem, so it wasn't a case of knowing it was the right question to ask based on a solution. He just asked it. There's some intrinsically interesting thing about it. It also wasn't very important for math at the time. Most people were more interested in the applications to physics. This was almost a side, recreational, hobbyist-type thing. Abel started working on quintic stuff, but then he was advised to spend more of his efforts studying elliptic functions, so more of his work was on that before he died young. He died at twenty-six from tuberculosis.

**18:42** · And then Galois pushed both of those ideas in the right direction, where he really understood the nature of abstraction. He had this really nice piece that he wrote while he was in prison. We could talk all about his life story.

**18:58** · It's pretty wild. But he's this teenager, he's in prison, and he had tried to submit his math papers and they had been rejected. So again, thinking about verifiable reward, the verifier function that is the academy at that time is rejecting what he wrote.

**19:11** · Frankly, it was not very coherent. It wasn't a complete proof.

**19:13** · He wasn't giving a clear thought of what the theory actually was.

**19:16** · He was just a young fledgling mathematician getting his bearings.

**19:20** · The verified reward there is, "No good." But he has some instinct that there's something there. So he's writing this diatribe on the nature of math being something that undergoes these shifts over time.

**19:33** · He talks about the advent of algebra itself and going from just thinking in terms of numbers to having a certain fluency with pure algebraic expressions, where you're not tied to interpreting those expressions. He has this instinct that there seems to be another layer of abstraction that we should be doing, where rather than thinking about the formulas themselves, we're thinking about what symmetries underlie those formulas.

**19:56** · But it was still a pretty ill-defined theory. If you're trying to say the verified reward is that he solved a problem that other people haven't, well, Abel already proved that quintics are unsolvable. So what was Galois doing?

**20:08** · In principle, Galois theory lets you take a specific polynomial, and it gives you the rules to say whether that specific polynomial has roots that you could write down.

**20:16** · For example, with x⁵ - 1, you know that a solution is 1.

**20:20** · Or x⁵ - 2, you can write down the fifth root of two.

**20:23** · So it's not that you can't write down the solution for every quintic polynomial, but could you find a specific one where you prove you can't write the solution using radicals?

**20:30** · He also didn't even solve that exactly. He didn't show for a specific example that he couldn't. Even describing what problem he solved is very tricky. He then dies. It's this very romantic story of him having this duel. There's a lot of myth around how he supposedly writes up all his ideas the night before the duel, but really, he tried to get them published five times before. Working on the quintic doesn't seem to be good for your health. It's very bad. If you're a young genius, don't work on the quintic. He asks his brother and his close friend to get his notes to Gauss, to get these notes to the important mathematicians of the day, because he thinks there's something there. Even then, it didn't really take.

**21:07** · His brother and his friend tried to get them out, but it was another twenty years until Liouville sees these notes, sees that maybe there's something in them, and tries to clean them up and understand what Galois was getting at. Even then, it was another twenty years or so until Jordan actually puts together something like a modern treatment of group theory that they attributed to Galois. You could easily imagine history turning differently, where these ideas were coming about from other points in math, and Galois could have been forgotten in history if he was a less florid character.

**21:39** · But between the time of Lagrange having this inkling that maybe symmetries of roots is the right way to go, to where it all looks like modern group theory, you've got this long span.

**21:50** · A lot of the time, it's not even passing the verified reward of human reviewers.

**21:54** · It gets on someone's desk and they say, "I don't really know if there's anything here."

**21:58** · You have to have this one person recognize it. Even then, it's not really solving practical problems at that point. You pointed out cryptography and physics and things like that. You have to get into the twentieth century before you have Gell-Mann thinking that maybe understanding the nature of how certain groups break down has a relationship with what particles are made out of.

**22:21** · He anticipates quarks based on a purely group-theoretic question.

**22:25** · That's one of the more interesting applications of group theory: to even predict the existence of quarks is a group-theoretic question. That's so long after Lagrange before you have anything like that. So you have to ask, what is the way of measuring progress that's not based on solving a problem, but that is somehow capturing the instinct inside Galois's mind when he says, "I think there's something here"?

**22:50** · What's the instinct inside Lagrange's mind when he says, "I think this is the right way to think about it"? What's the instinct inside Liouville's mind when he says, "These scattered notes from this long-dead youngster might have something to them"?

**23:01** · It's so hard to put a finger on that. A different series of videos I'm making right now is about the whole "compression is intelligence" idea.

**23:12** · Even though this isn't really the angle I'm taking, there is something to the idea that the smaller expression that's more predictive feels more intelligent.

**23:22** · So I wonder the extent to which you can give some kind of verifiable reward around not just whether you solved it or what it is solving, but around the smallness of the concepts required to do it.

**23:34** · Going back to Riemann hypothesis solutions, what would that look like if an AI solves it?

**23:37** · I think a third way it could happen is it just straight-up works harder.

**23:41** · In the same way, you could maybe have an elementary proof of Fermat's Last Theorem that's just spelled out over thousands of pages that would be incoherent.

**23:48** · But the cleaner way to view it is with elliptic curves and all that.

**23:51** · Maybe there's some thousand-page proof of the Riemann hypothesis that no one's really getting anything out of, and what you actually want are the succinct, compressed versions of those ideas that would then lend themselves to human understanding.

**24:07** · Maybe you throw Kolmogorov complexity into your attempt to quantify what you mean by elegance.

**24:14** · I don't think it's easy, but I do think it's something you would have to do in order to reward the Galois-like instinct, rather than just rewarding whether you solved a problem.

**24:23** · It's very hard to come up with the heuristic for science.

**24:27** · But it's clear humans have been doing this somehow, and obviously, AIs will do it at some point. It's relevant also not just in terms of verified reward, but presumably, the end goal is understanding, human understanding.

**24:40** · Even if you do have some thousand-page proof of some math thing or some grand new physical theory, the goal is understanding. Maybe if the goal is predictiveness, you can just have automated engineers go off and build rocket ships where we have no idea how they work, but we can get between stars. But there are going to be a lot of people who want to understand. You're still going to want whatever the concision function is that distills down this complicated way of thinking into the right one, like the equivalent of the universal law of gravitation for Newton.

**25:10** · You would still want to train AIs to be able to do that and find the compressed representation.

**25:16** · I grew up in India until I was eight, so in addition to English, I also speak Gujarati.

**25:21** · And since Google just released Gemini 3.5 Live Translate, I thought it'd be fun to put it to the test in this mid-roll. (Gujarati) Gemini 3.5 Live Translate automatically detects more than 70 different languages and translates in almost real-time into the target language. Live translate your original speed and format while speaking. Just like it’s doing right now.

**25:45** · I visited China back in 2024, and I remember thinking at the time that the trip would've been so much more productive if I'd been able to live-translate the conversations I was having with researchers and random people I met on the street. Now we have that technology.

**25:57** · So if you're building an app that needs live translation, you should 100% check out Gemini 3.5 Live Translate. It's available now via the Gemini Live API and in AI Studio. Go to ai.studio/live to get started.

### Will we understand an AI proof of the Riemann hypothesis?

**26:12** · People have this worry about mathematics in particular that AIs will prove the Riemann hypothesis, and our understanding of mathematics won't be any the better for it.

**26:21** · I have a couple of questions about this. The first one is whether this is something you should expect. Isn't the reason humans come up with general, natural objects and subgoals when we're working on a big problem that this is just useful when you're trying to work on a complicated, important problem?

**26:42** · Theoretically, would this even be a simpler way to solve the Riemann hypothesis, as opposed to just coming up with the natural abstractions that are relevant to thinking about the problem?

**26:50** · And then two, empirically, is this what we observe when AIs make progress on problems today?

**26:54** · When the AI came up with that counterexample to the unit distance conjecture, you can just read its chain of thought. It's not understandable to me, because I don't know anything about mathematics, but it seems that to other mathematicians it was understandable.

**27:09** · It made use of known concepts of mathematics and proved relationships between them, all in natural language. As a result, it accelerated our understanding of the connection between this object and this conjecture.

**27:22** · Empirically, is this a thing we should be worried about?

**27:24** · I think it depends on the nature… If we break down the three possible ways of solving the Riemann hypothesis… The other big one from this year was a certain Erdős problem numbered 1196, about these things called primitive sets. It had that character of bringing an idea from a seemingly different field. As soon as you present the basic idea to a mathematician… You say, "What if we try the Markov chain process where we show that this thing is one from the bottom up probabilistically rather than the top down, and use the von Mangoldt function?"

**27:59** · If you say that to someone in the know, they’d know how to run with it.

**28:02** · You have this very small idea that has the form of expertise in one field and expertise in another, drawing a little lightning bolt between them. Those are going to be very human-parsable, because all you have to do is show the start and end point of what those connections are.

**28:17** · If the character of it is mountain building, you have to put in a lot more time to understand that new mountain that was built, because it's a new thread, not just a lightning bolt between them.

**28:26** · And if the nature of the progress was just raw hustle—a super long chain of reasoning with no new theories—then you would have that worry of this whole digestion process.

**28:38** · So I don't think there's one clear answer. It depends on what the solution would look like.

**28:44** · On the mountain building side, that would actually be really interesting to see.

**28:48** · Is it by default very human-understandable, the way we see new theories from great mathematicians?

**28:54** · Or is it an alien, different kind of mountain being built where we have to reprocess the kinds of abstractions we engage with? The closest example here would be the attempted solution of the abc conjecture. We maybe shouldn't get into that one, but it probably is not a correct solution. Basically it's this whole new way of thinking that this otherwise reputable mathematician in Japan had come up with.

**29:23** · It took mathematicians a long time to even parse what he was saying, but it had the feeling of an alien bit of mathematics that's theory building, not just a long chain of reasoning.

**29:34** · He called it inter-universal geometry. The biggest fear would be that an AI does that, and then much like the abc conjecture, people work for years to go up the mountain, and they're like, "Dang it. This just isn't right." If it turns out to be wrong, but it really looked right. Even if it was right, there's just a lot of effort to hike up a new mountain. If we end up in that situation, David Bessis had a really great blog post called "The Fall of the Theorem Economy".

**30:01** · He's talking about how historically, as you were saying, mathematics is coming up with these definitions and problems, and it's about proving theorems about them.

**30:13** · The theorem-proving stuff is what gets all the credit, but it's really a parasite on the coming-up-with-the-definition stuff. Historically, this has not been a problem in terms of credit apportionment, because if you come up with a definition, you're probably going to be the guy who comes up with a theorem. But now we're in a situation where if the valuable work is coming up with the insight and AI automates the latter part… Imagine a scenario where an AI comes up with Abel-like direct arguments about a bunch of important conjectures in the world, and then we just have these proofs.

**30:47** · Now it's up to humans or future AIs to consolidate.

**30:55** · Again, having no object-level understanding of this argument whatsoever, I'm sure that if you had access to it, it would make it easier for you to think about what's going on.

**31:03** · Is there some deeper way in which we can understand why this proof works that would make it easier to come up with the ideas behind group theory?

**31:11** · I think it would be hugely helpful. So much of trying to discover new math is mostly being wrong. You're trying to solve a problem, and it doesn't feel like constantly taking the correct step up the mountain.

**31:25** · Mostly it feels like a random drunken walk, where you're doing a thing and then you're wrong and constantly discovering that. If at the very least you know that trying to digest what you have is ultimately leading to a correct solution, that feels like progress, simply because of the sense of knowing it leads to a solution.

**31:43** · There are plenty of instances in the recent history of math where it feels like the reach has exceeded the grasp, where things are proven long before they're understood.

**31:53** · One of my favorite openings to a paper—it's not even a research paper, it's more like an expository one—is from a mathematician named Timothy Chow, who was trying to understand a concept called forcing. There's this problem called the continuum hypothesis that more or less asks: you have a size of infinity for the natural numbers, and a size of infinity for the real numbers. Is there something in between?

**32:16** · The answer is both yes and no. It depends on your axioms.

**32:19** · It's outside the scope of our usual axiom systems, which is an interesting answer.

**32:23** · But the method to describe it is really hard to understand.

**32:27** · It's this thing called forcing. In the beginning of this paper, he writes, everyone knows the idea of an unsolved research problem.

**32:34** · I want to propose the idea of an unsolved expository problem.

**32:38** · Sure, we've proven it, but we don't really know why it's true.

**32:41** · Then he proposes a partial solution to that expository problem.

**32:45** · You can imagine why I loved that framing, because this is my whole life.

**32:49** · I don't do research math. It's wholly about what's the most clear way to understand this, even if it's proven. There is a difference between proof and explanation, and I think you're getting at the importance of that distinction.

**33:04** · Yeah. That will be the main incentive. Or the incentive would have to change, not just in mathematics but in other areas of science, from proving things about the world to consolidating proofs into problems or higher-level insights. We were having a discussion earlier at lunch about a recent talk you were giving on design and how it helps us understand things.

**33:31** · In the limit, is there really a difference between the conceptualization of an idea and the idea itself? If you think about special relativity and spacetime diagrams, and Minkowski spacetime, this is a way in which we illustrate why there's length contraction and time dilation. But that is the reality… So, the exposition does seem to be the explanation in some sense here. There's a couple of interesting things there.

**34:00** · One is that there seems to be a really strong correlation between the people who come up with genuinely novel insights and the people who are actually quite clear in their communication of it.

**34:10** · You might imagine the opposite, given that the experience of a university student is often that the expert teaching them is not necessarily the best explainer of that topic, because they're so spoiled by their expertise. But what seems, at least in some cases, to be the case is that the people who are really coming up with something quite novel—you've got Einstein or Claude Shannon or someone—you read their papers, and they're really lucid.

**34:33** · It doesn't feel like this is just for the experts and you have to chop through it with a machete.

**34:38** · They're very good expositors. Feynman has this characteristic too, he’s a very good expositor.

**34:43** · Maybe the same part of the brain that comes up with the correct new way of thinking about it at a research level also has this knack for good explanation.

**34:52** · I think this is pertinent to AI. I used to think that AIs would become these automated theorem provers, but the role of mathematicians was going to shift towards my job, explaining these things. Now I suspect that actually they'll also be quite good at doing that, probably better than most humans are at explaining and distilling.

**35:13** · So digesting and explaining what was going on is probably actually not what's left for mathematicians, by the nature of how these things are going.

**35:24** · We can talk about ways this might not be it, but probably the same thing that comes up with the really good new idea that solves some new problem is also just good at explaining it.

**35:35** · That's a way my beliefs have changed. What's the last thing you think you'll be doing?

**35:40** · Both you and also what the human mathematical community will be doing.

**35:45** · I will probably be doing something like what I am until I die.

**35:53** · If the doomers are right, maybe it'll be for the same reason.

**35:58** · Yeah. You build a man a fire, and he's warm for one night.

**36:02** · But set a man on fire, and he's warm for the rest of his life.

**36:05** · So that's where I am with AI. Some of the function of an explainer or a teacher is to add clarity to a thing that someone's curious about.

**36:16** · That's one thing. But some of it is more relational, providing motivation and a sense of curation. One interesting take that I've heard about what mathematicians will end up being is that it's actually more analogous to art museum curators than anything else. The AI solved the thing, so the art exists.

**36:36** · They even know how to explain it really well. But you still want someone to help you navigate this nearly infinite space of what ideas are worth engaging with.

**36:47** · Even if AIs were in some sense better at that, I think we would always still prefer a human that we had a relationship with, because the way we get motivated to be interested in things is a social phenomenon. If you have some specific technology you're trying to build, that might be different. But the people listening to this podcast trust your curation on what's an interesting topic in the first place.

**37:11** · It's not that they're landing here because whatever your next topic is, that's what they wanted to understand in a prior sense. They're trusting you as a curator.

**37:19** · So my role, and arguably that of other mathematicians, might actually just shift subtly into that curation direction of what ideas are worth pursuing.

**37:28** · That's a lot of my job right now. I think people assume a lot of the time for a video goes into the visuals. Sure, it does. It’s not immediate. But actually a lot of it is just deciding what's worth saying in the first place, what's worth putting there.

**37:46** · I want to engage with that, and I think I have a trust with certain people, and they're curious what I would choose to put forward even if the AIs are better than that.

**37:53** · It's the same reason human musicians are always going to have a role: that social function of the story behind them, even if the objective quality of the MP3 file coming out of some model is better. That's what I see happening to my job.

### Can AI find the hidden bridges between fields?

**38:08** · I want to go back to a question from earlier. Just as AI has crossed this threshold, this important benchmark of being able to connect existing ideas to come up with a new discovery or prove or disprove something, we're like, "Okay, but what's the next thing?"

**38:27** · There's a lot more to do on that one, by the way. Just because a couple lightning bolts have been thrown… I think there's this flourishing future over the next couple years of really connecting.

**38:35** · Right. So in the limit, you could even say—I don't know if this is accurate, but potentially—a lot of the biggest breakthroughs look like this at some level.

**38:46** · With general relativity, you're just connecting together Riemannian geometry and special relativity. So as AIs keep getting better and better at this connection thing, maybe a lot of big breakthroughs are not really of a different qualitative nature.

**39:02** · I don't know if you have a take on that. A lot of the conversation has focused on problem-solving and that nature of math, ticking off Erdős problems or something.

**39:11** · But I'd say it's not even a majority of mathematicians who would characterize their work as really targeting the next problem to tick down. Are you familiar with the Langlands program?

**39:21** · No. It's not even a field of math so much as it is a research ethos. Fermat's Last Theorem is one inkling of this.

**39:30** · You had these two seemingly disparate things, and a connection between them led to a solution.

**39:37** · Langlands was a mathematician. He has this famous letter essentially spelling out how it seems likely that there's a lot more connections like that.

**39:46** · He even got a little bit more specific about the nature of the connections, such that you might imagine this large map, and you've got this valley over here and this mountain over here and this set of plains over there.

**39:57** · There's a lot of mathematicians who would characterize their work as being part of trying to understand the threads on this map. The progress there, it's not even "Here's this one specific problem that we know will be solved by that connection."

**40:08** · It's more that time and time again, there have been cases where big problems were knocked down by finding connections, such that it's almost preemptively finding the connections.

**40:19** · It's actually very interesting. Anytime you run into a mathematician, ask them whether the character of their work is more akin to the Langlands program or to targeting one particular problem. You get a certain bifurcated split there.

**40:36** · The possibility of AIs being supercharged connectors feels like it might be an amplifying tool in that pursuit. It's hard to measure, though.

**40:49** · This cuts to what we were saying earlier: How do you assign a score to say, "Yes, you've done it"?

**40:55** · If it's knocking down a problem, you have a clear way of saying, "Yes, you've done it."

**40:59** · You can write the headline. You can have your PR move as the AI company to say, "We did it." Whereas if it feels like that was the right connection to draw, you can write theorems around it.

**41:08** · That's the nature of what the papers in that field look like.

**41:10** · But I think it will require a lot more "human in the loop" to say, "What was the kind of connection that we were going for?" That's my guess on what most of the useful progress from these models will look like in the next five years.

**41:26** · It's just really filling in that landscape of connections that you can draw if you're an expert in multiple fields. As you've pointed out, it's kind of surprising we haven't already had this. I would be curious to know at a technical level what causes the unlock there. On the one hand, you can paint an explanation in your head for why you could be an expert in all of these things and not be drawing those connections.

**41:51** · When the method of reasoning is this autoregressive chain-of-thought phenomenon… Autoregression is actually a really weird way to produce stuff, if you think about it.

**42:06** · You're an intelligent person. Imagine I've locked you in a box, and the only way you have of interacting with the world is that you receive a slip of paper, and someone says, "Can you predict what will come next?" You predict what will come next, and then your memory's wiped. You get another slip of paper.

**42:23** · Imagine that was done a whole bunch of times, and then what comes out on the other end.

**42:26** · They say, "Look at this essay that you wrote." You might look at that and say, "This is awful.

**42:30** · That's not the essay that I would've written." The process of repeatedly predicting something is just pretty different from how you would think as a writer to compose it and think it through.

**42:40** · In particular, what would probably happen is that you're a slave to your context.

**42:45** · You might be answering some question about a particular field, so you draw on all the context around that. But the connection where all the substance is going to come from is, by its nature, a very unlikely one.

**42:59** · You can do all the RL that you want to try to get better in some way, but what's the thing that's specifically upweighting and incentivizing making these unlikely connections when the vast majority of them aren't the predictable next token that would come in there?

**43:12** · So it might be the case that you just have this intelligence locked inside that box, but it's a weird way of interacting with it. The thing I'm curious about is: do you ever get any fruit by questioning the premise of how tokens are generated?

**43:30** · I don't think it would be as simple as manipulating the temperature, but are there any things that you can do that take the existing level of intelligence but find the right ways of sparking those connections that unlock these sorts of things that we've seen?

**43:46** · Or do you just need a little bit more intelligence, such that at the level of prediction, it's predicting that it should be making that lightning bolt to another field?

**43:55** · I think it's more productive to reason, instead of architecture or even loss function, about data.

**44:06** · We have diffusion models that do text, and the kinds of things they produce are not of a wholly different character. They've just not been explored as much.

**44:14** · I think the more relevant thing is: what is the data on which whatever architecture or loss function you have is incentivizing you to produce? It does seem like they're getting better.

**44:27** · Forget about math. We did have a couple of examples of this kind of thing, but if you just look at why they're getting better at being autonomous agents… They're in an environment where they’re autoregressively producing the step that says "Let's step back and do a search over the whole codebase," and then "Let's step back and assess my mistake," is the thing that works.

**44:50** · I assume what happened in the case of progress in science or maybe in math is you have frontier math-like problems. Mathematicians have specifically designed them because they require connecting together two different fields.

**45:07** · I'm guessing there's all kinds of clever, partially synthetic ways to make harder and harder problems like that that require these kinds of connections—for example, by eliminating assumptions and still requiring the AI to get to the answer—and then it doesn't really end up mattering what the loss function is. It's really about, can you come up with an environment that incentivizes this ability? It feels like you should be able to.

**45:32** · I certainly can't speak to the correct ways of doing that to unlock all this, but it would just be pretty surprising. Don't you think it would be surprising if, over the next three years, there weren't a lot more of those lightning bolts?

**45:43** · I think this is an important thing to think about. We often think about how smart a single system is.

**45:48** · And we don't think about AIs having advantages that are more the result of other facts about them. So in this context, the key fact about them is that we can just parallelize and arbitrarily scale them.

**46:04** · Whatever level of capability they have, it's not just one idiosyncratic genius in the history of mathematics who makes a few connections and then dies in a duel.

**46:13** · It's universally applying that waterline across all problems that are accessible at that level of capability. This is among the many advantages that digital minds inherently have that we don't think enough about.

**46:26** · The other ones being that they can merge all their knowledge together—or at least that there will be techniques that allow this to happen—and that you can spawn off copies with identical levels of knowledge. This parallelization is quite an important property. I'd be curious about your predictions.

**46:43** · Even if they're not as smart as human mathematicians, the fact that for PR reasons the AI companies are just throwing billions and billions of dollars at this means that quantity has a quality all of its own. That seems in the right direction.

**47:00** · If we take that conversation between Montgomery and Dyson at the IAS that suggests some connection between the Riemann hypothesis—or the Riemann zeta-function zeros—and random matrices, that feels like the kind of thing that you could try to automate.

**47:16** · You have agents representing expertise in all these fields.

**47:21** · We all know that an institute is smarter than an individual.

**47:24** · The reason for having people all in the same geographic location is that you want those serendipitous conversations to happen. What does it look like to engineer those between agents? It's interesting, because you point out that you can pool all your knowledge, but I really wonder if one of the advantages is that you can do the opposite of that. Sometimes when an AI is failing, it's because it gets into a bad chain of thought and it's really hard to get it out.

**47:51** · So you say, "I'll just start again." Same deal with humans. Sometimes you start thinking about it in a certain way, and what's required is to just back up.

**48:02** · There are stories about people trying to prove something for a long time, and then at some point they say, "Hang on a second. What if I tried to prove that it's impossible, or prove the opposite?" Unwinding your own context and going at it with a fresh mind… You could imagine systematizing that, or having multiple different agents deliberately given different pieces of context and trying to compare and contrast there.

**48:21** · We don't have the same level of manipulation on our own context.

**48:26** · In this AI and math series, the first episode we'll do will be about when they solved the IMO.

**48:32** · I want to focus on one specific IMO problem that they failed on, which is one that a lot of very smart students failed on. Terry Tao also failed on it.

**48:43** · People were very mad at the problem because they called it a troll problem.

**48:47** · I almost don't want to spoil it, because I want to construct the episode around leading someone in without their knowing that it turns out to have a simple solution.

**48:56** · You can really empathize with what it's like to be a student solving this.

**49:01** · Basically, there's a really elegant way of going down what you really feel like is going to be the solution based on the context of it being an International Math Olympiad problem.

**49:11** · The character of the solution is really enticing, but it's hard to prove that it's the best.

**49:15** · The reason is that it's not. There's this almost brain-dead solution that is the best. The relevance of that to the whole AI story is that for a human, what's required to answer that question is to escape your context.

**49:27** · Escape the context of being in the IMO. Escape the context of the way you've been trained to solve these contest math problems. If you just approached it like a brain teaser that I throw at someone off the street, they'd probably answer it well.

**49:40** · You want the same sometimes for human research in other contexts, just being able to refresh your thinking and come at it completely differently. Of all the advantages that digital minds have, that might actually be one of them: a more systematic approach to refreshing your thinking.

**50:02** · Spin off two agents, one who's trying to prove it and one who's trying to disprove it, one who tries it this way and one who tries it another. They deliberately have different contexts.

**50:10** · I would be curious to see, if we're having this conversation three years from now, how many of the significant results that make headlines have that character of basically erasing the context previously, trying a bunch of different things as opposed to merging the results of a bunch of different agents. It is incredibly interesting, because a common concern people have about AIs is this entropy collapse where they all think the same way, because they're trained in similar ways. This is why they're bad at writing.

**50:35** · They go down the same path and have similar patterns of speaking and so forth.

**50:40** · But maybe the key advantage AIs have is that you can systematically… It sounded like one of the reasons the unit distance problem conjecture took so long to be disproven was that people assumed the conjecture was actually true, so they were mostly trying to figure out ways to prove it.

**50:58** · Maybe one of the key advantages the AIs will have is to increase the entropy by systematically trying out both the negation and trying to prove the positive of any given statement, or being able to systematically give different agents different biases.

**51:17** · It seems like an important thing in the history of human science is that Einstein was really motivated by this bias that things should look the same in different reference frames.

**51:26** · He had multiple other biases like these, but that one was very formative in his thinking.

**51:30** · You can systematically survey a bunch of heuristics and see which ones are being productive on a given problem.

**51:36** · So you would suggest systematically increasing entropy at the prompt level even though you have this inevitable collapse at the autoregression level?

**51:49** · Einstein would be an interesting example, because he's got this bias toward things being relative.

**51:53** · He also has a bias toward "God should not play dice."

**51:57** · You want to make sure you don't accidentally have all your LLMs be Einstein, because you might halt progress on quantum mechanics. Which goes to show you that there's not a correct heuristic for science. You just need multiple independent research programs with their own heuristics. That feels like old-school software.

**52:13** · As long as you're able to describe that in some way.

**52:15** · You have old-school software that amplifies that entropy.

**52:19** · If you're able to put a clear ontology to the distinct ways of thinking that you want to prompt, you explore that full ontology, and then each individual one runs off doing what it is.

**52:33** · There's a certain design question there about how exactly you describe the different approaches.

**52:38** · The easy one is: are you trying to prove it or disprove it?

**52:40** · The harder one would be to say, what are all the tactics you could take to prove this, and make sure you're applying sufficient breadth to exploring them.

**52:50** · I don't think people appreciate the kinds of things these models can just go handle for you when you equip them with a good harness like Cursor.

**52:57** · For example, I started publishing my episodes on Bilibili for a hopefully burgeoning Chinese audience — but everything I upload there needs the sponsored segments cut out.

**53:06** · Normally that would have meant asking my editors to go back through all the old episodes, cut the ads, and re-export everything. But in about as much time as it would've taken me to send them that Slack message, I can just tell Cursor to do it instead and spare them.And for podcast research, I have a whole repo where I've put every single book and paper that's been relevant to prepping any of the recent episodes. I've been able to just throw everything in there, because the Cursor harness is extremely good at helping the model figure out exactly what to pull — whether from my repo or from the web — to answer the questions I have while I'm researching.

**53:40** · So whatever you happen to be working on right now, just try pointing Cursor at it.

**53:44** · Go to cursor.com/dwarkesh to get started. Obviously, AI in math is making much faster progress than everything else, and people point to the verifiability of the domain as the key reason this is happening. I think that's one of the two important reasons, but people really neglect the other one. I'm outside the labs, so I don't know what's actually going on. This is a totally naive theory.

### Why real-world tasks don’t fit into RL environments

**54:12** · A tangential question to why AI is making so much progress in math: why has it been so slow at computer use? A computer is very verifiable.

**54:21** · Is my Etsy package coming? Is my event booked? These are extremely verifiable things to survey. What computer use lacks is grindability.

**54:32** · Because websites have bot detectors—and it takes a tremendous amount of compute to run parallel rollouts—it's very hard to run a thousand parallel rollouts of the same checkout flow on Amazon.

**54:44** · You'll get shut down by Andy Jassy. Him personally. He presses the red X on Dwarkesh button. Exactly. You could try to build clones of every single website, but that's very labor-intensive and slows you down.

**54:59** · The reason you currently need to do so many parallel rollouts to learn a skill with deep learning is that we haven't solved sample efficiency.

**55:08** · Sucking supervision through a straw, as Karpathy says?

**55:10** · Exactly. Of course people are working on many different techniques, but fundamentally there's this big constraint in the way we train AIs. With code, you can containerize a given level of progress in a repository and then spin out hundreds of parallel containers and say, "Try to implement this feature," and it's totally deterministic.

**55:31** · Because it's deterministic, you can solve the credit assignment problem because you know that whatever caused this rollout to succeed and this one to fail, the diff is the thing that worked.

**55:41** · If you have situations that are starting off at different starting points, this credit assignment problem becomes much harder to solve. Most things in the real world are very hard to containerize in the same way. Coding and math are exceptions to this rule.

**55:55** · But if you're trying to figure out how to build a new business that succeeds, or how to go trade in the markets for a day and make money, the fact that you have to interact with the real world and things change day after day means that you can't keep replaying and grinding and farming the simulator. Math, of course, is the exception, and I feel like this is an important driver of progress in this domain and also in coding.

**56:20** · It's not just verifiability; it has to be grindable.

**56:23** · The third reason people point out that AI is making fast progress is they focus a lot on Lean and formalization. Again, I have literally no idea what's going on in the labs. I feel like Lean just doesn't matter that much for the current level of progress in AI. Why is AI able to disprove the conjecture about the unit distance problem? They released the chain of thought, or at least a rewrite of the chain of thought. It didn't have any Lean in it.

**56:50** · I think the process-based supervision that Lean provides, where you know each step is correct, seems less relevant than just having this grindable outcome that is verifiable.

**56:59** · It's an interesting point about grindability mattering more.

**57:06** · Naively you might think Lean provides something unique for math because you're able to see if it can prove it. You have old-school software that can tell you yes or no, and you use that as your VR. What would corroborate your point is the initial attempts. Again, I'll circle back to the IMO.

**57:22** · Initially, DeepMind basically does that. Everything is in Lean, and then the next year it's all in natural language. So to your point, it's not needed.

**57:29** · I do think there's a yet-to-be-explored benefit of that formalization domain, which is that at the moment you still need a human reviewing that counterexample to the unit distance conjecture to say, "Looks good." That provides a certain bound on how endlessly explorable things are.

**57:48** · If you consider AlphaGo or AlphaZero-style systems, they're off in their own universe playing a bunch of Go and exploring themselves, potentially going off the rails of what any human needs to look at, but they still have this automated verifiable reward. It's not just that you can do RL on that.

**58:09** · It's also that you basically never have to check in, and you can just pour compute at them exploring the universe of Go. What stands to be interesting—maybe this won't pan out, but the jury should still be out on whether it'll yield anything—is that with Lean, you could imagine having a basically endlessly running program that's constantly trying to extend Mathlib. Mathlib is this GitHub repository that's basically all of math written in code. It's very far from all of math, but they want it to be all of math.

**58:39** · It’s written in code where you can ask, "Is this proof correct?" It's very labor-intensive to write these proofs.

**58:45** · There's a whole subcommunity around it. But you could imagine having an AI where you say, "Simply try to extend Mathlib." Maybe it's a fork of it so that it doesn't have trash in it, because people have a certain taste for what they want to be in there.

**59:01** · So you have your fork of the pure AI Mathlib, and it just goes and it doesn't stop.

**59:05** · It doesn't need anybody to check in on it. It could just keep going.

**59:09** · It might come up with its own conjectures. It might come up with its own theories and different definitions. Maybe many of them are useless, but it just has this infinite tree that it can grow out. That's a very unique thing that math has that nothing else has, where you could press go and just pour compute at it, look away for ten years, and then come back and say, "What do you have?" There's going to be something.

**59:30** · Then there's a question: is it useful or not? How do you suss that out?

**59:33** · That's just an interesting thing to be able to do. It would be very surprising if that didn't yield some sort of interesting mathematical insight from it.

**59:44** · There are two different ways that Lean is important in this story.

**59:48** · The first one is how you could let go, not even check in, and progress will be made.

**59:54** · You can do that with Go. I don't think you can do that with natural language math. That's very interesting. Did you see Karpathy's auto research idea? He wrote this one Python file that does basic LLM training, and then had a repo where LLM agents would try to make modifications to the file, and if it sped up the speed run, the modification stays.

**1:00:18** · Eric Jang, who came on to explain how AlphaGo works, did a similar thing when he was trying to build a very strong Go bot. He had interesting observations. It's really good at running an experiment and going down that path, but it's bad at stopping at dead ends and doing extremely parallel things. Anyway, this will probably change in the future.

**1:00:41** · It's very interesting to think about what it looks like in the limit.

**1:00:44** · This is fundamentally what the human institution of mathematical research is.

**1:00:50** · It's a library extended in interesting and useful ways.

**1:00:54** · This way you don't have any outcome-based supervision.

**1:00:57** · There's no outcome that you're trying to incentivize, but you have a process.

**1:01:00** · You know the steps are correct, you just don't know if it's going in an interesting direction.

**1:01:04** · If you were doing that, you don't want to completely go off the rails and do a random walk through the space of logic. You'd probably want some supervisor model that's trying to provide heuristics on whether it's useful or not.

**1:01:17** · You know people are working on it. That's one of those "five years from now" things where I'd be curious to get the future version of us talking about it.

**1:01:26** · Maybe that goes nowhere, but Terry Tao was talking about one research project that tries to exhaustively search the space of possible algebras.

**1:01:36** · You could imagine different axioms that you apply to algebraic systems.

**1:01:40** · When we come up with group theory, there's a certain axiom system that looks like arbitrary rules unless you know the motivation. What if you tried all of them?

**1:01:49** · Do any of them yield useful things? The vast majority of them are just trash in some way. It all collapses to no interesting results.

**1:01:55** · But every now and then, there would be this little island of a completely different type of axiom system that at the very least seems rich in terms of the number of theorems that can come out of it.

**1:02:05** · That's bread and butter for what you would imagine automated provers being good for, exploring that space and seeing which one of them turns out to be something.

**1:02:13** · Maybe one of those islands actually turns out to be something you can retroactively put motivation on, to say this is the kind of structure it's trying to get at.

**1:02:19** · In the same way that you could imagine looking at the axioms for a group, not knowing that it's about symmetry, but you retroactively realize this is very relevant to studying symmetry.

**1:02:29** · You could imagine results of that flavor, but instead of just exploring possible algebra systems, it's exploring all possible logical consequences of any kind of axiom.

**1:02:39** · On the point about whether you can provide process-based supervision without Lean, DeepSeek had their DeepSeek Math model. They released a paper on how they trained it, and it was quite interesting. The problem with natural language proofs is you don't know if it's correct or not. They have a verifier, and the verifier is trained by a meta-verifier that makes sure that for all the problems they're training this model to solve in the art of problem-solving, the verifier is giving good feedback.

**1:03:09** · It works. It's interesting that natural language verification with some sort of meta-verification seems to work so far in the published literature. It also seems to work in the published products that we're using. If you look at coding agents, they're getting better and better at writing clean code and refactoring code.

**1:03:28** · I'm sure there are process-based "LLM-as-a-judge" systems providing taste and saying, "Is this a clean way to write this function? Are there duplicates of the same kind of modular forms?" That should also work for mathematics, right?

**1:03:46** · It seems more plausible for math than anything else, even if you're only working in natural language, that you could trust a verifier. You and I were talking earlier about why they're bad at writing. They seem to be good judges.

**1:04:00** · If I give them two essays that students wrote, they'd be able to say which one is more accurate and insightful. So why can't you just have a verifier saying, "Is this a good piece of writing or not?" Maybe the ultimate failure there is that even if they're good at discriminating between a B essay and an A essay, they're not actually good at discriminating between an A essay and a thing you actually want to read, something that would be followable on Substack and insightful. They actually end up preferring uninsightful pieces of writing. On the math front, the step to simply know if a proof is correct or not lends itself to an automated verifier, even in natural language.

**1:04:42** · You could probably still make a ton of progress. I still like the tree of logic out of Lean, just in that you can really go off the rails. There's no constraint on the previous way things had been phrased before. Everyone talks about move 37 in AlphaGo.

**1:05:00** · What is the thing that lends itself to going outside the prior heuristics?

**1:05:05** · It seems productive to have a disconnection from the rest of the world in that exploration, as a complementary research pursuit to the natural language math front.

**1:05:17** · The other relevance of Lean would be, let's say you have your pure natural language RL environments and a pure natural language set of proofs.

**1:05:28** · People say, "Proceed, AI mathematicians," and they generate ten papers a day.

**1:05:38** · If there's any error rate to that at all… Alex Kontorovich has talked about this.

**1:05:43** · It becomes insufferable as a mathematician. Every single time you see one of these, you don't know if it's worth your time. Even if 99 out of 100 are right, I don’t know if it’s worth my time because it's really labor-intensive to find what that error would be.

**1:05:59** · It's really frustrating to spend all your time on a paper that was trash.

**1:06:04** · Having something that's able to give you that green checkmark that says, "Even if this is going to be complicated to understand, even if it’s going to be a pain, you at the very least know it is correct," every other field would kill for that.

**1:06:16** · Math has that. If the models are also able to take their natural language proofs and formalize them, that seems huge. Every field would love to have something like that. So I think you're right that Lean is maybe overrated regarding its importance as a VR environment for progress in math generally.

**1:06:40** · But I definitely wouldn't write it out of the story.

**1:06:44** · I also love this extension of Mathlib as a metaphor for what's going to happen to our civilization pretty soon. For millennia, humanity has built this corpus of knowledge and understanding, and everything that we have is now distilled into these models.

**1:07:02** · At some point, the models will just extend that arbitrarily.

### Good writing requires theory of mind that AI still lacks

**1:07:07** · By the way, on the writing front, I have a theory of why writing is making worse progress than these other domains. One reason is what you said, that they're bad at judging not only A versus B, but they get totally derailed by B\*, which is this shitty essay that hits all the bells and whistles that A is supposed to hit.

**1:07:29** · The reward hacking thing just goes off the rails. But the other important thing is that writing is not modular in the same way that code and math are.

**1:07:40** · You can write a function many different ways, and they do the same thing.

**1:07:43** · Of course you want it to be clean, but at the end of the day, if it works, it works.

**1:07:46** · Same with lemmas in mathematics.

**1:07:49** · You can have some end product that's different from the way it's produced.

**1:07:54** · Code is the thing that produces some end product, and you want a functional end product.

**1:08:00** · Whereas in writing, the end product is directly the thing the AI is producing.

**1:08:05** · Each paragraph, sentence, and word matters because that is the substance.

**1:08:13** · It's not some separate thing produced out of the writing.

**1:08:18** · It can't be slop in the way that code can be slop and still produce the outcome you want.

**1:08:25** · But you were just pointing out how we've actually gotten much better at agents writing not just functional code, but clean code. Why is it not the case that the same progress that lets you go from merely functional to a clean and mergeable PR also results in clearer writing?

**1:08:42** · That's a good point. Also, has it not? I agree there are many ways in which they're terrible writers. But for a lot of writing I consume, I find it's better to just copy-paste it into an LLM and say, "Explain this to me."

**1:08:56** · The explanation will be better than the thing produced by the human.

**1:09:00** · It's funny that we say these are such terrible writers, and yet my revealed preference is to have an LLM explain it. Even when I'm talking to a human expert live on a call, if it's a piece of knowledge that only they have that's not encoded in the distribution, I want them to explain it to me. But if in order to understand that, I need to understand a more basic concept, I would prefer if it were socially acceptable for me to just say, "Let's pause here. I'm just going to ask an LLM how that works, and then we can come back to your special piece of knowledge."

**1:09:32** · That's distillation, an explanation. If I'm thinking of your quality as an essay writer—if I give you a book to read and I want a book report—I might believe that the LLM gives me a better book report. But what people are really getting at when they say it’s bad is, what is writing? It's not just the distillation of preexisting ideas. It's not just how you explain clearly, because they are good explainers. It's about what the insight is.

**1:10:01** · This is where autoregression is a very weird way to generate things.

**1:10:06** · When you're writing, you sort of know that in order for it to be good, you have to have an element of the unpredictable. It's not just increasing the temperature in your mind. It's knowing exactly the correct point when you want to make an unpredictable move, and that that's going to be what's more insightful.

**1:10:23** · Even if it's better at explaining a preexisting thing, what generated that book that you wanted distilled in the first place? It wasn't an LLM that generated it and you just needed it. It was some author who, through a lot of exploration of ideas in the world, decided what aspects were interesting and what ways of presenting it formed a coherent, well-motivated narrative.

**1:10:45** · They put that all together in some way. If they're a good author, you would probably err on the side of reading their book instead of the distillation.

**1:10:53** · Still, what makes it worthwhile to explore at all in the first place and want to upload it at all?

**1:10:59** · It's that side of it that people cite when they say LLMs are bad at writing.

**1:11:04** · It's that element of unpredictability, of deliberately choosing something novel that is very directly contradictory to the way things are typically produced.

**1:11:13** · That's a good point. I think they're also really bad at building really good mental models of people, which is a very important skill in writing.

**1:11:21** · Andy Matuschak and another collaborator, whose name I'm forgetting right now, did an interesting report where they tried to teach LLMs to write good spaced-repetition prompts.

**1:11:29** · I really like this because even though it seems like a totally random skill… It's just like, people are talking about recursive self-improvement in a year, and we can't get these things to write good flashcards. What's going on there? They tried many different kinds of techniques, and they're sophisticated people.

**1:11:48** · They tried to RL open source models. They tried all kinds of things, including chain of thought and a big prompt they sent to the best closed source model.

**1:11:56** · The key constraint, it seemed to me, was that writing a good card is about projecting somebody's mind in three months. What is the way in which they'll associate the question? What kind of answer will they be thinking at that moment? Is the elicitation that inspires the detail you actually want to take away from the passage you're trying to make cards about?

**1:12:21** · I think writing is similar to this. If you're writing something, the reason it's such an enervating process that takes so long is that with each word or each sentence, you have to be thinking: what is happening in my reader's mind right now?

**1:12:35** · Even if I flip the phrasing around so the end phrase goes to the beginning and this is the first image that comes to your mind before you read the rest of the sentence… Maybe autoregression is bad at that. This is maybe a more diffusion-like property of considering the whole rather than going sentence by sentence.

**1:12:51** · But also I think that requires a lot of mentalizing, which these models weirdly struggle at. It's an interesting question. Is it weird that they struggle at that? I might butcher this. You know how you cite studies that you once read and maybe the study wasn't real?

**1:13:06** · There's one very memorable one. Let's say you want to quiz people's EQ.

**1:13:14** · You show a flashcard of someone's facial expression and someone is trying to describe that emotion. There are really good tests online that have a face and then four possible emotions. It's surprisingly hard to describe exactly the correct emotion, but you also get the sense there really is a correct answer.

**1:13:32** · If you try this with people in your life, you'll notice that the ones who are pretty plugged in socially do really well on it, and the ones who are a little bit more left-brain don't.

**1:13:42** · That is a kind of test you can do. I vaguely remember an experiment to this effect where they took people who had freshly gotten Botox, and they did a pretest and a post-test.

**1:13:53** · Post-test, they were just much worse at reading people's expressions.

**1:13:56** · That feels weird. Wait, they got Botox?

**1:13:59** · The person taking the test. You do the test, and then you go and get Botox and your face is all frozen, and now you're worse at understanding the emotions of what you see.

**1:14:08** · The thought is that part of understanding the emotion you're looking at is doing it yourself.

**1:14:15** · At a facial level, you're moving your face muscles.

**1:14:19** · You see that, you mimic that, and you're like, "Oh yeah, that's anxiety," at some very subconscious level. So in that sense, if it is the case that models have bad theory of mind, sure, they know everything because they've read what everyone wrote. But at the level of actually being able to put themselves in your shoes in the same way that my face muscles are mimicking your face muscles—that's what helps me understand how you feel—it's not surprising at all.

**1:14:43** · They don't have face muscles. Their brain works completely differently.

**1:14:45** · It's like an alien trying to empathize. How could it have theory of mind?

**1:14:50** · It would be this very emergent thing to have. Whereas we can just plug it into our own minds.

**1:14:55** · We've got the ready-made hardware to just place it in.

**1:15:00** · From that lens, it's not that surprising. Okay, Grant, we're both partners with Jane Street.

**1:15:06** · I'm sure over the years you've interacted with a lot of Jane Streeters — what have you found that's unique about them, or their culture? I did this interview with them this year, that was partially interesting because they don't usually have anything outward-facing.

**1:15:17** · I mean in the industry they're known for having a pretty wild retention rate — people just stay there — getting an inside view of that. I remember in one of their comments someone saying: even though the people have role titles — researcher, or trader, or engineer — they often don't know what their colleagues' actual role is, because everyone's doing a little bit of everything else. Like even if you're officially a trader, you're doing a lot of research; even if you're officially a researcher, you're doing a lot of coding.

**1:15:40** · And I suspect that's part of why they have the insane retention they do.

**1:15:44** · Because anyone who wants to grow just has the chance to do a lot of different kinds of things.

**1:15:49** · All right, Grant, I'll do the plug for you this time.

**1:15:51** · If you want to watch the full sit-down interview Grant did with some of the folks there, go to 3b1b.co/janestreet. All right, Grant — let's talk more about AI and math. What advice do you have about using LLMs to learn?

### Why learning will still depend on human curation

**1:16:08** · As I was describing, for a lot of well-known concepts, I find them very helpful.

**1:16:13** · But often, just a couple of messages further down, I'm trying to understand something, and they're so confused themselves that they're confusing me. They don't explain it the right way.

**1:16:26** · I know that talking to the right human could clear up my confusion in three minutes.

**1:16:32** · More and more, we're going to want to use these things to learn.

**1:16:39** · People talk a lot about education and representation stuff.

**1:16:42** · Have you noticed ways to use them more productively to understand concepts?

**1:16:45** · I'm curious to hear your take on this. I'll give mine. Even pre-LLM, I feel like a relevant insight in learning was recognizing who matters more than what.

**1:16:56** · My advice to any college student when they're choosing what courses to take: care a little bit less about your preexisting interests, because they're kind of arbitrary right now, and care a little bit more about whether the person teaching it is a good educator and someone you resonate with. In choosing what books to read, who the author is maybe matters more than whether it's a prior interest.

**1:17:16** · If there's a book you've liked before, read what else that author has written rather than reading another thing on that subject. I'm getting to LLMs on this.

**1:17:26** · There's a difference in feel for trying to learn something from a Wikipedia page versus, if it's a philosophy topic, going to the Stanford Encyclopedia of Philosophy.

**1:17:35** · Or if it's a math topic, you go to the Princeton Companion to Mathematics.

**1:17:40** · The difference there is the articles are deliberately written by one individual who tries to actually craft a motivation around it. Whereas on Wikipedia, it's this local minimum that's reached where every sentence has to be correct.

**1:17:56** · In a good exposition, you care a little bit less about correctness on the way.

**1:18:01** · You can deliberately craft things that are a little bit wrong that you correct along the way, which gets edited out in a crowdsourced environment.

**1:18:09** · LLM explanations feel to me at the moment a lot like Wikipedia, which is to say, amazing.

**1:18:15** · Imagine a world before Wikipedia, how long it would take to find and suss everything.

**1:18:20** · But nevertheless, what's the most useful part of a Wikipedia page?

**1:18:24** · It's often just the references at the bottom. You look at the key references, and you go to them, and you read them. Sometimes that gives a much better overview.

**1:18:32** · So often I like to just ask an LLM, "Who should I read?"

**1:18:38** · Maybe I can even give some specifics on ways I want to learn.

**1:18:41** · I actually got gaslit by this once when I was trying to learn about semiconductors or something.

**1:18:46** · I felt it was a very visual topic, but all the resources were text.

**1:18:48** · I asked, "Is there a well-visualized video explaining the concepts you're getting at?"

**1:18:57** · And Claude said, "Yeah, here's a couple," and the top one was like, "Here’s one from 3Blue1Brown".

**1:19:02** · I’m like, "I can guarantee that there’s not." It was an actual video, an actual link, but it had just misattributed someone else's. It was good. I had a much better experience clicking over and watching it to learn rather than trying to proceed forward with questions there.

**1:19:20** · In that sense, I'm basically using it like a very souped-up version of Google to zero in on the right human-written resource. What about you? You engage with these a lot.

**1:19:29** · What's the best way to use them? I think you put your finger on it.

**1:19:31** · The most productive learning sessions I've had are when there's some artifact that a human has produced—whether it's an article, a book, or a video—that organizes the relevant concepts in the correct way. It builds up the motivation for why the next idea would be relevant to solving the next problem you'd encounter, and the next idea, and the next idea. Then you use the LLMs to just do a little bit of pruning around this branch that the book has identified.

**1:20:02** · I was actually going through—I think you might have recommended it—Steven Strogatz's textbook on… The chaos one? Nonlinear Dynamics and Chaos? I love that book.

**1:20:11** · Yeah, I was going through it, and it was bliss. It was like your videos in book form.

**1:20:19** · It was super fun. The way I was learning it, I'd have his university lecture on one-third of the screen, that part of the textbook on another third, and an LLM on the last third.

**1:20:30** · I was actually thinking, if I were back in college and watching this lecture live, it would totally go over my head. These kids must be really smart, because I'm pausing, reading the textbook, talking to LLMs, and then restarting again.

**1:20:43** · But with him curating the right order to understand concepts and the right problems to motivate understanding them… Another thing LLMs are really bad at.

**1:20:55** · Something a really good human can do, when you ask a question, a human can say, "Actually, you're not really thinking about this topic the correct way.

**1:21:02** · The question you want to be asking, the correct way to organize these concepts, is X."

**1:21:06** · An LLM just can't really do that. It's a little too placating.

**1:21:11** · This is ultimately that sycophantic behavior where it's very, "Oh, what an insightful question."

**1:21:16** · You want to strip that down. That's a good point, and I think it cuts to theory of mind a little bit, recognizing that asking a certain kind of question reveals that the student's mental structures are not the same as the explainer's.

**1:21:34** · Sometimes people do this to a fault. With a really good teacher, let's say you have a middle school math classroom. If a student asks a question that suggests they're thinking about it in a different way, it's actually really hard to take that seriously in the moment and ask, "Hang on, could you get to a right answer with that?" before you say, "Instead of that, let's do this." The really good teachers are able to jujitsu the creative way the student was thinking about it and bring it in.

**1:22:05** · LLMs aren't doing that. They aren't reframing your question.

**1:22:09** · Instead, they kind of run off. At the very least, it feels like there are three levels here. An LLM is at one, a good explainer is at another, but the A+ explainer is the one who can jujitsu your way of thinking and say, "That's where that's useful." Maybe there is a cycle all the way around where, five years from now, the LLMs will be doing that, but in a better way.

**1:22:31** · What is your recommendation to students who I'm sure email you this question all the time: "I was curious about doing mathematics. I'm really passionate about the subject, but seeing all the progress AIs are making, I don't know if it makes sense for me to pursue this as a career." This is relevant not only to people in mathematics, but to anyone noticing that their field is getting productivity gains from AI.

**1:22:59** · Coding is very adjacent to this. What advice do you have for people?

**1:23:06** · I wouldn't trust any advice that I give. That's how I'd couch it.

**1:23:11** · But even pre-AI, it feels very important for any job you're going to go into to really understand… If we're talking about a job—not being a gentleman-scientist engaging with the math world or something—you should understand where the money is coming from, what value you're actually adding, and the connection between those two. A surprisingly small amount of thought is put towards that, especially by students. They're in this environment where they probably want to go into math because they've always been good at it.

**1:23:40** · They've been rewarded in life for proceeding through the next hoop correctly.

**1:23:44** · When they think they want to be a mathematician, it's because they think it's a way to continue engaging with that. They think, "Where do people get to do this?" rather than thinking, "What value am I adding to other people, and to what extent is that the reason a salary is flowing in my direction?" It's actually quite different in different cases.

**1:24:02** · In some cases, it's a very prestigious mathematician, and their presence at a university lends a certain brand value, which is why the university wants them.

**1:24:10** · In some cases, an NSF grant is given because of the public good belief we have around basic science. You've got an institution around that, and a whole bureaucracy acting as a proxy for what we think that public good is, with a whole song and dance around how to make them correctly predict that your progress will be in the spirit of that funding. Sometimes it's just straight-up teaching.

**1:24:36** · People like to send their kids to an institute that has experts teaching them.

**1:24:40** · You provide brand value by being an expert, and direct value by being a teacher.

**1:24:47** · Regardless of whether AIs are proving theorems or not, or whether we're talking about 2016 or 2026, that is something not enough students thinking "I want to be a mathematician" consider.

**1:24:56** · I think it's worth thinking about. For me, I wasn't necessarily thinking about it, and I stumbled into a career path where math exploration can be monetized as entertainment.

**1:25:08** · I stumbled into that and I'm very grateful I did, but it was an accident.

**1:25:12** · It wasn't deliberate. I could have avoided relying on serendipity and done it a little bit more by design had I been thinking critically about it. To your question—if we have almost-automated theorem proving, and let's say they're also really good explainers so you even get the human understanding—I think a lot of the social role that mathematicians serve actually doesn't change that much.

**1:25:37** · As a public, we still feel there's value to basic science, and we trust the judgment of mathematicians to determine where their time is best spent. The prestige comes from within that community.

**1:25:53** · It's other members saying that a result is really good, more than the grant writer really understanding algebraic number theory to understand it was a good result.

**1:26:02** · There's going to be an inner culture of what constitutes valuable contributions.

**1:26:06** · Maybe it shifts away from theorem proving and towards good definition writing.

**1:26:10** · Maybe it's that museum curator idea. But you're going to have that same community as long as society as a whole is still valuing the premise of basic science.

**1:26:19** · And if we're in the abundance world that AI brings, there's probably more funding in that direction in some sense. On the side of prestige to institutions for who their lecturers are, I actually think teaching is one of the most stable post-AGI jobs that there is, because it's so relational. This is where parents want to spend their money if they have an abundance of wealth: on good teaching and good educating.

**1:26:46** · It goes so far beyond explanations. Even if LLMs are good explainers, the thing that a teacher is doing is such a social, coaching, mentor-type thing that that's probably one of the most stable careers that's going to exist over the next fifty years.

**1:27:01** · Insofar as a lot of mathematicians' roles overlap with that, as the prospective student going into it, you could lean into that. I actually think a lot more students should think about and give credence to the idea of being just a math educator and the value that can serve towards the next generation. I'll couch again that I don't think I'm the one to say, "Here, prospective young mathematician, here's how you should think about the future," because I'm a YouTuber. I'm not in the institution that they're thinking of going into, so I'm speaking as an outsider looking in.

**1:27:36** · But it feels like generally good, universal advice: know where the money is coming from, know where you plug into that. And if you're just asking those questions, you're actually already steps ahead of all the other fledgling prospective mathematicians.

**1:27:51** · In fact, think about the crazy world where, within five or ten years, the AIs are coming up with not only solutions to the Millennium Prize problems, but totally novel problems to be solving in the first place, novel mathematical fields and objects and stuff.

**1:28:09** · It is in that world where, first of all, there's a ton of abundance.

**1:28:12** · Two, the thing AI minds will have gone furthest in, where they will have seen furthest beyond our horizons, will be mathematics. There will be so much demand for, "What have the AIs seen? Can you explain it to us?"

**1:28:31** · In that world, if there are any jobs whatsoever, surely distilling what the AIs have learned will be one of them. Also, it's funny because all of this presumes that it's useless. We're not talking about the actual practical applications of what math is being done. Insofar as there's any economic utility to it, you would imagine that the people who understand it and are able to make the decision of where it should point actually have a lot more economic value by being able to make that judgment as a curator and point this behemoth of new math in a useful direction.

**1:29:03** · Suddenly, that's a much more levered move to make than it had been previously.

**1:29:07** · Can I ask you about that? Obviously, one question for AI for math is not only can it do it, but is it any good? Or is it good for anything?

**1:29:20** · You were describing all the ways in which, with group theory, we're trying to figure out random facts about the roots of different kinds of functions, and now there are all these different applications that are practical across many different fields.

**1:29:33** · Do you have some sense of whether, if we just totally get to a place where the field of human mathematics is accelerated 10X or 100X and some crazy shit happens, or are we just going to be bottlenecked by other fields? I think there are some fields that probably will.

**1:29:55** · It's super spiky. With progress in algebraic number theory, it feels unlikely that that then unlocks something. But I remember talking to this mathematician who does more dynamics and PDE-solving type stuff. He was referencing that his group had some ideas.

**1:30:16** · Let me see if I summarize this right. It’s like the way Boeing would make planes is that they'd make it, do a bunch of tests, and they had to disassemble it and reassemble it based on those tests. His group essentially had some insights on how to do more in simulation such that you don't have to deconstruct and rebuild it.

**1:30:32** · It saved Boeing billions of dollars or something, and then they just started funding that group.

**1:30:37** · That's much more obviously application-adjacent, because PDEs just are that.

**1:30:45** · Progress in that domain, you would imagine actually does unlock some things.

**1:30:50** · I don't know if it's these step changes, but maybe it's more on the side of engine design becoming a little bit more fluid, or coming up with the right wing shape instead of running a whole bunch of complicated CFD. Maybe you're able to speed up your CFD simulations because certain pure math insights make those more efficient.

**1:31:09** · I bet you'd just see a lot of great incremental improvement there.

**1:31:14** · It seems less likely that the massive breakthroughs in math immediately turn into this massive economic breakthrough, like you solve the Navier-Stokes problems, and then that unlocks an ability to simulate more things. But you probably will see, at those fringes, some meaningful leakage out of the pure math insights into other things.

**1:31:39** · There's a ton of people working on things like AI engineering, physical engineering, and material science. You have to imagine they'd be in a good position to look at the AI math insights and decide whether they're relevant in some way or not.

**1:31:57** · It's another one of these things where I'm not going to sit here and put a flag in the sand predicting that there will be. But it'd be a little bit disappointing and a little bit surprising if there weren't, over the next five years, economically valuable improvements made that were directly referable to the AI progress in math.

**1:32:15** · It would just be disappointing if it was just taking down a bunch of Erdős problems and none of them were doing any of the math that actually directly touches the physical world.

**1:32:25** · To your point about how a lot of the history of mathematics was about building up these piles of concepts and connections. Sometimes the piles connect with each other, or you discover an application somewhere else. At the very least, you just build up this huge pile. Then as broader progress in society happens during the singularity, when we get to the industrial part of the singularity, you just have all these different ideas that hopefully are useful in other parts of the world.

**1:32:53** · As I said, one of the interesting things about what's happening is it causes people to step back and ask, "What is math?" Maybe one of the awkward conclusions will be revealing that it's just become wholly useless. The kind of questions being asked have become so divorced from things that are physically applicable that that's one of the things mathematicians have to come to terms with. Everyone will look and say, "Hang on a second, weren't you guys supposed to… If there's 10X progress there, why aren't we seeing it over here?" And then mathematicians are like, "Ugh."

**1:33:23** · Every time we wrote those grant proposals and said, "Trust us, the elliptic curve progress is going to help with cryptography," it shines a light on the fact that maybe it doesn't.

**1:33:32** · So that's one possibility. Grant, this was super fun.

**1:33:36** · Thanks so much for doing it. Absolutely. My pleasure.
