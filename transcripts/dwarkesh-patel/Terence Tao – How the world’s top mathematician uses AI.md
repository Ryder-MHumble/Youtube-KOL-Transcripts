---
title: Terence Tao – How the world’s top mathematician uses AI
source_url: https://www.youtube.com/watch?v=Q8Fkpi18QXU
video_id: Q8Fkpi18QXU
account: '[[accounts/dwarkesh-patel|Dwarkesh Patel]]'
account_name: Dwarkesh Patel
account_url: https://www.youtube.com/@DwarkeshPatel
featured_people:
- '[[people/terence-tao|Terence Tao]]'
published: 2026-03-21
created: 2026-07-23
language: en
speaker_attribution: contextual
description: We begin the episode with the absolutely ingenious and surprising way in which Kepler discovered the laws of planetary motion.People sometimes say that AI will make especially fast progress at scien
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=Q8Fkpi18QXU)

We begin the episode with the absolutely ingenious and surprising way in which Kepler discovered the laws of planetary motion.  
  
People sometimes say that AI will make especially fast progress at scientific discovery because of tight verification loops. But the story of how we discovered the shape of our solar system shows how the verification loop for correct ideas can be decades (or even millennia) long.  
  
During this time, what we know today as the better theory can often actually make worse predictions (Copernicus's model of circular orbits around the sun was actually less accurate than Ptolemy's geocentric model). And the reasons it survives this epistemic hell is some mixture of judgment and heuristics that we don’t even understand well enough to actually articulate, much less codify into an RL loop.  
  
Hope you enjoy!  
  
𝐄𝐏𝐈𝐒𝐎𝐃𝐄 𝐋𝐈𝐍𝐊𝐒  
\* Transcript: https://www.dwarkesh.com/p/terence-tao  
\* Apple Podcasts: https://podcasts.apple.com/us/podcast/terence-tao-kepler-newton-and-the-true/id1516093381?i=1000756353875  
\* Spotify: https://open.spotify.com/episode/24xF8YGra2w3HXZYbhgVKU?si=U5V-SgvSQ8eVIcG2Z86wfQ  
  
𝐒𝐏𝐎𝐍𝐒𝐎𝐑𝐒  
\- Jane Street loves challenging my audience with different creative puzzles. One of my listeners, Shawn, solved Jane Street’s ResNet challenge and posted a great walk-through on X ( https://x.com/hynwprk/status/2026376546286711206 ). If you want to try one of these puzzles yourself, there’s one live now at https://janestreet.com/dwarkesh  
\- Labelbox can get you rubric-based evals, no matter your domain. These rubrics allow you to give your model feedback on all the dimensions you care about, so you can train how it thinks, not just what it thinks. Whatever you’re focused on—math, physics, finance, psychology or something else—Labelbox can help. Learn more at https://labelbox.com/dwarkesh  
\- Mercury just released a new feature called Insights. Insights summarizes your money in and out, showing you your biggest transactions and calling out anything worth paying attention to. It’s a super low-friction way to stay on top of your business. Learn more at https://mercury.com/insights  
  
To sponsor a future episode, visit https://dwarkesh.com/advertise.  
  
𝐓𝐈𝐌𝐄𝐒𝐓𝐀𝐌𝐏𝐒  
00:00:00 – Kepler was a high temperature LLM  
00:11:44 – How would we know if there’s a new unifying concept within heaps of AI slop?  
00:26:10 – The deductive overhang  
00:30:31 – Selection bias in reported AI discoveries  
00:46:43 – AI makes papers richer and broader, but not deeper  
00:53:00 – If AI solves a problem, can humans get understanding out of it?  
00:59:20 – We need a semi-formal language for the way that scientists actually talk to each other  
01:09:48 – How Terry uses his time  
01:17:05 – Human-AI hybrids will dominate math for a lot longer

## Transcript

### Kepler was a high temperature LLM

**0:00** · Today, I'm chatting with Terence Tao, who needs no introduction.

**0:04** · Terence, I want to begin by having you retell the story of how Kepler discovered the laws of planetary motion because I think this will be a great jumping off point to talk about AI for math.

**0:16** · I've always had an amateur interest in astronomy.

**0:18** · I've loved stories of how the early astronomers worked out the nature of the universe.

**0:24** · Kepler was building on the work of Copernicus, who was himself building on the work of Aristarchus.

**0:31** · Copernicus very famously proposed the heliocentric model, that instead of the planets and the Sun going around the Earth, the Sun was at the center of the solar system and the other planets were going around the Sun. Copernicus proposed that the orbits of the planets were perfect circles. His theory fit the observations that the Greeks, the Arabs, and the Indians had worked out over centuries.

**0:57** · Kepler learned about these theories in his studies, and he made this observation that the ratios of the size of the orbits that Copernicus predicted seemed to have some geometric meaning.

**1:12** · He started proposing that if you take the orbit of the Earth and you enclose it in a cube, the outer sphere that encloses the cube almost perfectly matched the orbit of Mars, and so forth.

**1:26** · There were six planets known at the time and five gaps between them, and there were five perfect Platonic solids: the cube, the tetrahedron, icosahedron, octahedron, and dodecahedron.

**1:35** · So he had this theory, which he thought was absolutely beautiful, that you could inscribe these Platonic solids between the spheres of the planets.

**1:44** · It seemed to fit, and it seemed to him that God's design of the planets was matching this mathematical perfection of the Platonic solids. He needed data to confirm this theory.

**1:56** · At the time, there was only one really high-quality dataset in existence.

**2:02** · Tycho Brahe, this very wealthy, eccentric Danish astronomer, had managed to convince the Danish government to fund this extremely expensive observatory.

**2:12** · In fact, it was an entire island where he had taken decades of observations of all the planets, like Mars and Jupiter, at least every night for which the weather was clear, with the naked eye.

**2:24** · He was the last of the naked-eye astronomers. He had all this data which Kepler could use to confirm his theory. Kepler started working with Tycho, but Tycho was very jealous of the data. He only gave him little bits of it at a time.

**2:38** · Kepler eventually just stole the data. He copied it and had to have a fight with Brahe's descendants. He did get the data, and then he worked out, to his disappointment, that his beautiful theory didn't quite work.

**2:53** · The data was off from his Platonic solid theory by 10% or something.

**2:57** · He tried all kinds of fudges, moving the circles around, and it didn't quite work.

**3:02** · But he worked on this problem for years and years, and eventually, he figured out how to use the data to work out the actual orbits of the planets. That was an incredibly clever, genius amount of data analysis. And then he worked out that the orbits were actually ellipses, not circles, which was shocking for him.

**3:26** · So he worked out the two laws of planetary motion: the ellipses, and also that equal areas sweep out equal times. Then ten years later, after collecting a lot of data—the furthest planets like Saturn and Jupiter were the hardest for him to work out—he finally worked out this third law, that the time it takes for a planet to complete its orbit was proportional to some power of the distance to the Sun.

**3:55** · These are the three famous Kepler's laws of motion.

**3:59** · He had no explanation for them. It was all driven by experiment, and it took Newton a century later to give a theory that explained all three laws at once.

**4:09** · The take I want to try on you is that Kepler was a high-temperature LLM.

**4:17** · Newton comes up with this explanation of why the three laws of planetary motion must be true.

**4:22** · Of course, the way that Kepler discovers the laws of planetary motion, or figures out the relative orbits of the different planets, is as you say a work of genius.

**4:29** · But through his career, he's just trying random relationships.

**4:33** · In fact, in the book in which he writes down the third law of planetary motion, it's an aside on The Harmonics of the World, which is just a book about how all these different planets have these different harmonies. And the reason there's so much famine and misery on Earth is because the Earth is mi-fa-mi, that's the note of Earth.

**4:50** · It's all this random astrology, but in there is the cube-square law, which tells you what relationship the period has to a planet's distance from the Sun.

**5:00** · As you were detailing, if you add that to Newton's F=ma and the equation for centripetal acceleration, you get the inverse-square law. And so Newton works that out.

**5:12** · But the reason I think this is an interesting story is that I feel LLMs can do the kind of thing of trying random relationships for twenty years, some of which make no sense, as long as there's a verifiable data bank like Brahe's dataset. "Ok, I'm going to try out random things about musical notes, Platonic objects, or different geometries, I have this bias that there's some important thing about the geometry of these orbits." Then one thing works. As long as you can verify it, these empirical regularities can then drive actual deep scientific progress.

**5:44** · Traditionally, when we talk about the history of science, idea generation has always been the prestige part of science. A scientific problem comes with many steps.

**5:53** · You have to identify a problem, and then you have to identify a good, fruitful problem to work on.

**5:59** · Then you need to collect data, figure out a strategy to analyze the data, and make a hypothesis. At this point, you need to propose a good hypothesis, and then you need to validate. Then you need to write things up and explain.

**6:11** · There are a dozen different components. The ones we celebrate are these eureka genius moments of idea generation. Kepler certainly had to cycle through many ideas, several of which didn't work. I bet there were many that he didn't even publish at all because they just didn't fit. That's an important part of the process, trying all kinds of random things and seeing if they worked.

**6:41** · But as you say, it has to be matched by an equal amount of verification, otherwise it's slop.

**6:50** · We celebrate Kepler, but we should also celebrate Brahe for his assiduous data collection, which was ten times more precise than any previous observation.

**7:00** · That extra decimal point of accuracy was essential for Kepler to get his results.

**7:09** · He was using Euclidean geometry and the most advanced mathematics he could use at the time to match his models with the data. All aspects had to be in play: the data, the theory, and the hypothesis generation. I'm not sure nowadays that hypothesis generation is the bottleneck anymore. Science has changed in the century since.

**7:38** · Classically, the two big paradigms for science were theory and experiment.

**7:44** · Then in the 20th century, numerical simulation came along, so you can do computer simulations to test theories. Finally, in the late 20th century, we had big data. We had the era of data analysis.

**7:59** · A lot of new progress is actually driven now by analyzing massive datasets first.

**8:03** · You collect large datasets and then draw patterns from them to deduce thoughts.

**8:09** · This is a little bit different from how science used to work, where you make a few observations or have one out-of-the-blue idea, and then collect data to test your idea.

**8:17** · That's the classic scientific method. Now it's almost reversed. You collect big data first, and then you try to get hypotheses from it. Kepler was maybe one of the first early data scientists, but even he didn't start with Tycho's dataset and then analyze it.

**8:35** · He had some preconceived theories first. It seems like this is less and less the way we make progress, just because the data is so much more massive and useful.

**8:48** · Oh, interesting. I feel like the 20th-century science that you're describing actually very well describes what happened with Kepler. He did have these ideas—1595 and '96 is where he comes up with the polygons and then the Platonic objects theory—but they were wrong.

**9:06** · Then a few years later, he gets Brahe's data, and it's only after twenty years of trying random things that he gets this empirical regularity. It actually feels a bit closer to Brahe's data being analogous to some massive data bank of simulations, and now that you've got the data, you can keep trying random things. If it wasn't for that, Kepler would be out there just writing books about harmonics and Platonic objects, and there would be nothing to actually verify against. The data was extremely important.

**9:33** · The distinction I was trying to make was that traditionally, you make a hypothesis and then you test it against data. But now with machine learning, data analysis, and statistics, you can start with data and through statistics work out laws that were not present before. Kepler's third law is a little bit like this, except that instead of having the thousand data points that Brahe had, Kepler had six data points.

**10:09** · For every planet, he knew the length of the orbit and the distance to the Sun.

**10:13** · There were five or six data points, and he did what we would now call regression.

**10:19** · He fit a curve to these six data points and got a square-cube law, which was amazing.

**10:24** · But he was quite lucky that these six data points gave him the right conclusion.

**10:30** · That's not enough data to be really reliable. There was a later astronomer, Johann Bode, who took the same data—the distances to the planets—and inspired by Kepler, he had a prediction that the distances to the planets formed a shifted geometric progression.

**10:48** · He also fit a curve, except there was one point missing.

**10:52** · There was a big gap between Mars and Jupiter. His law predicted that there was a missing planet.

**10:57** · It was kind of a crank theory, except when Uranus was discovered by Herschel, the distance to Uranus fit exactly this pattern. Then Ceres was discovered in the asteroid belt, and it also fit the pattern. People got really excited that Bode had discovered this amazing new law of nature. But then Neptune was discovered, and it was way off. Basically it was just a numerical fluke.

**11:26** · There were six data points. Maybe one reason why Kepler didn't highlight his third law as much as the first two laws is that instinctively, even though he didn't have modern statistics, he kind of knew that with six data points, he had to be somewhat tentative with the conclusions.

### How would we know if there’s a new unifying concept within heaps of AI slop?

**11:45** · To ask the question about the analogy more explicitly, does this analogy make sense if in the future we have smarter and smarter AIs? We'll have millions of them, and they can go out and hunt for all these empirical irregularities. It sounds like you don't think the bottleneck in science is finding more things that are the equivalent of the third law of planetary motion for each given field, so that later on somebody can say, "Oh, we need a way to explain this. Let's work out the math. Here's the inverse-square law of gravity."

**12:18** · I think AI has driven the cost of idea generation down to almost zero, in a very similar way to how the internet drove the cost of communication down to almost zero.

**12:27** · It’s an amazing thing, but it doesn't create abundance by itself. Now the bottleneck is different. We're now in a situation where suddenly people can generate thousands of theories for a given scientific problem. Now we have to verify them, evaluate them.

**12:46** · This is something which we have to change our structures of science to actually sort this out. Traditionally, we build walls. In the past, before we had AI slop, we had amateur scientists have their own theories of the universe, many of which were of very little value.

**13:07** · We built these peer review publication systems to filter out and try to isolate the high signal ideas to test. But now that we can generate these possible explanations at massive scale, and some of them are good and a lot are terrible, human reviewers are already being overwhelmed. Many journals are reporting that AI-generated submissions are just flooding their submissions.

**13:34** · It's great that we can generate all kinds of things now with AI, but it means that the rest of the aspects of science have to catch up: verification, validation, and assessing what ideas actually move the subject forward and which ones are dead ends or red herrings. That's not something we know how to do at scale.

**14:02** · For each individual paper, we can have a debate among scientists and get to a consensus in a few years. But when we're generating a thousand of these every day, this doesn't work. There's this incredibly interesting question. If you have billions of AI scientists, not only how do you gauge which ones are real progress, but how do you... This is actually a question that human science has had to face and we've solved somehow, and I’m actually not sure how we solved this.

**14:29** · Let's say in the 1940s, if you're at Bell Labs and there are these new technologies coming out.

**14:37** · Pulse-code modulation, how do you transfer signals? How do you digitize signals?

**14:41** · How do you transfer them over analog wires? There are all these papers about the engineering constraints and the details, and then there's one which comes up with the idea of the bit, which has implications across many different fields. You need some system which can then look at that and say, "Okay, we need to apply this to probability.

**14:56** · We need to apply this to computer science," et cetera.

**15:00** · In the future, the AIs are coming up with the next version of this unifying concept.

**15:06** · How would you identify it among millions of papers that might actually constitute progress, but which have much less in terms of general unifying ideas? A lot of it's the test of time.

**15:16** · Many great ideas didn't actually get a great reception at the time they were first proposed.

**15:21** · It was only after some other scientists realized that they could take it further and apply them to their own... Deep learning itself was a niche area of AI for a long time. The idea of getting answers entirely through training on data and not through first principles reasoning was very controversial, and it just took a long time before it started bearing fruit. You mentioned the bit. There were other proposals for computer architectures than the zero-one that is universal today.

**15:50** · I think there were trits, three-valued logic. In an alternate universe, maybe a different paradigm would have shown up. The transformer, for example, is the foundation of all modern large language models, and it was the first deep learning architecture that really was sophisticated enough to capture language. But it didn't have to be that way.

**16:13** · There could've been some other architecture that was the first to do it and once that was adopted, it would become the standard. One reason why it's hard to assess whether a given idea is going to be fruitful is that it depends on the future.

**16:29** · It depends also on the culture and society, which ones get adopted, which ones don't.

**16:38** · The base ten numeral system in mathematics is extremely useful, much better than the Roman numeral system, for instance. But again, there's nothing special about ten.

**16:48** · It's a system that is useful for us because everyone else uses it. We've standardized it. We've built all our computers and our number representation systems around it, so we're stuck with it now. Some people occasionally push for other systems than decimal, but there's just too much inertia. It's not something where you can look at any given scientific achievement purely in isolation and give it an objective grade without being aware of the context both in the past and the future.

**17:19** · So it may never be something that you can just reinforcement learn the same way that you can for much more localized problems.

**17:33** · Often in the history of science when a new theory comes up that in retrospect we realize is correct, it seems to make implications that either make no sense because they're wrong, and we realize later on why they're wrong, or they're correct but seem wildly implausible at the time.

**17:50** · As you talked about, Aristarchus had heliocentrism in the third century BC.

**17:58** · The ancient Athenians were like, "This can't be because if the earth is going around the sun, we should see the relative position of the stars change as we're going around the sun, and the only way that wouldn't be the case is if they're so far away that you don't notice any parallax," which is actually the correct implication. But there's times when the implication is incorrect and we just need to graduate to a better level of understanding.

**18:19** · Leibniz would chide Newton and disagree with Newton's theory of gravity on the basis that it implied action at a distance, and they didn't know the mechanism, and Newton himself was sort of stunned that inertial mass and gravitational mass were the same quantity.

**18:34** · All these things later were resolved by Einstein. But it was still progress. So the question for a system of peer review for AI would be: even if you can falsify a theory, how would you notice that it still constitutes progress relative to the thing before?

**18:49** · Often, the ultimately correct theory initially is worse in many ways.

**18:54** · Copernicus's theory of the planets was less accurate than Ptolemy's theory.

**19:00** · Geocentrism had been developed for a millennium by that point, and they had made many tweaks and increasingly complicated ad hoc fixes to make it more and more accurate.

**19:13** · Copernicus's theory was a lot simpler but much less accurate.

**19:16** · It was only Kepler that made it more accurate than Ptolemy's theory.

**19:21** · Science is always a work in progress. When you only get part of the solution, it looks worse than a theory which is incorrect but somehow has been completed to the point where it kind of answers all the questions. As you say, Newton's theory had big mysteries.

**19:42** · They had the equivalence of mass and action at a distance, which were only resolved with a very conceptually different approach centuries afterwards.

**19:54** · Often progress has to be made not by adding more theories, but by deleting some assumptions that you have in your mind. One reason why geocentrism held on for so long is we had this idea that objects naturally want to stay at rest.

**20:10** · This is the Aristotelian notion of physics, and so the idea that the Earth was moving… How come we weren't all falling over? Once you have Newton's laws of motion—an object in motion remains in motion and so forth—then it makes sense.

**20:25** · Conceptually, it's a very big leap to realize that the Earth is in motion.

**20:30** · It doesn't feel like it's in motion. The biggest advances, like Darwin's theory of evolution, is the idea that species are not static.

**20:42** · This is not obvious because you don't see evolution in your lifetime.

**20:47** · Well, now we actually can, but it seems permanent and static.

**20:57** · Right now we're going through a cognitive version of the Copernican revolution, where we used to think that human intelligence is the center of the universe, and now we're seeing that there are very different types of intelligence out there with very different strengths and weaknesses.

**21:14** · Our assessment of which tasks require intelligence, which ones don't, has to be reordered quite a bit. Trying to fit AI into our theories of scientific progress and what is hard and what is easy, we're struggling quite a lot.

**21:30** · We have to ask questions that we've never really had to ask before.

**21:32** · Or maybe the philosophers had, but now we all have to deal with it.

**21:35** · This brings up a topic I've been very curious about.

**21:39** · You mentioned Darwin's theory of evolution. There's this book, The Clockwork Universe by Edward Dolnick, which covers a lot of this era of history we're talking about.

**21:47** · He has this interesting observation in there. The Origin of Species was published in 1859.

**21:52** · Principia Mathematica was published in 1687. So The Origin of Species comes out two centuries after Principia. Conceptually, it seems like Darwin's theory is simpler. There's a contemporaneous biologist to Darwin, Thomas Huxley, who reads The Origin of Species and he says, "How stupid not to have thought of that."

**22:09** · Nobody ever says that about Principia, chiding themselves for not having beaten Newton to gravity. So there's a question of why did it take longer?

**22:17** · It seems like a big part of the reason is what you were saying.

**22:20** · The evidence for natural selection is overwhelming in a certain sense, but it's cumulative and retrospective, whereas Newton can just say, "Here are my equations.

**22:27** · Let me see the moon's orbital period and its distance, and if it lines up, then we've made progress." Lucretius actually had this idea that species adapted to their environment in the first century BC but nobody really talks about it until Darwin because Lucretius couldn't run some experiment and force people to pay attention.

**22:48** · I wonder if we'll in retrospect end up seeing much more progress in domains which have this kind of tight data loop where you can verify them quite easily, even though they're conceptually much more difficult. I think one aspect of science is that it's not just creating a new theory and validating it, but communicating it to others.

**23:09** · Darwin was an amazing science communicator. He wrote in English, in natural language. I'm speaking like a— No Lean.

**23:22** · I have to get out of my technical mindset. He spoke in plain English, didn't use equations, and he synthesized a lot of disparate facts. Little pieces of evolution had been worked out in the past, but he had this very compelling vision. Again, he was still missing things.

**23:42** · He didn't know the mechanism for heredity, he didn't have DNA.

**23:49** · But his writing style was persuasive, and that helped a lot. Newton wrote in Latin.

**23:57** · He had invented entire new areas of mathematics just to explain what he was doing.

**24:02** · He was also from an era where scientists were much more secretive and competitive.

**24:07** · Academia is still competitive, but it was even worse back in Newton's day.

**24:11** · He held back some of his best insights because he didn't want his rivals to get any advantage.

**24:17** · He was also a somewhat unpleasant person from what I gather.

**24:23** · It was only a couple of decades after Newton when other scientists explained his work in much simpler terms that they became widespread. The art of exposition and making a case and creating a narrative is also a very important part of science.

**24:45** · If you have the data, it helps, but people need to be convinced, otherwise they will not push it further or take the initial investment to learn your theory and really explore it.

**24:58** · That's another thing which is really hard to reinforcement learn on.

**25:01** · How can you score how persuasive you are? Well, there are entire marketing departments trying to do this. Maybe it's good that AI is not yet optimized to be persuasive. There's a social aspect to science.

**25:19** · Even though we pride ourselves on having an objective side to it, where there's data and experiment and validation, we still have to tell stories and convince our fellow scientists. That's a soft, squishy thing. It's a combination of data and painting a narrative, and it's a narrative of gaps. Even with Darwin, as I said, there were pieces of his theory he could not explain.

**25:46** · But he could still make a case that in the future, people would find transitional forms, that they would find the mechanism of inheritance, and they did. I don't know how you can quantify that in such a precise way that you can start doing reinforcement learning.

**26:06** · Maybe that will be forever the human side of science.

### The deductive overhang

**26:10** · One takeaway I had from reading and watching your stuff on the cosmic distance ladder… By the way, I highly recommend people watch your series with 3Blue1Brown on the cosmic distance ladder.

**26:22** · One takeaway was that the deductive overhang in many fields could be so much bigger than people realize. If you just had the right insight about how to study a problem, you might be surprised at how much more you could learn about the world.

**26:38** · I wonder if you think that's a product of astronomy at the particular times in history that you're studying. Or is it just that based on the data that is incident on the Earth right now, we could actually divine a lot more than we happen to know?

**26:52** · Astronomy was one of the first sciences to really embrace data analysis and squeezing every last possible drop of information out of the information they had because data was the bottleneck. It still is the bottleneck. It's really hard to collect astronomical data.

**27:10** · Astronomers are world-class in extracting all kinds of conclusions from little traces of data, almost like Sherlock. I hear that for a lot of quant hedge funds, their preferred hire is an astronomy PhD, actually. They are also very interested for other reasons in extracting signals from various random bits of data.

**27:35** · Okay, speaking of clever ideas, one of my listeners, Shawn, solved the puzzle that Jane Street made for my audience and posted a great walkthrough on X.

**27:44** · For context, Jane Street trained a ResNet, shuffled all 96 layers, and then challenged people to put them back in the right order using only the model's outputs and training data.

**27:54** · You can't brute force this – there's more possible orderings than atoms in the universe.

**27:58** · So Shawn broke the problem into two different parts.

**28:01** · First, pair the layers into 48 different blocks. And second, put those blocks in the right order.

**28:06** · For pairing, Shawn realized that in a well-trained ResNet, the product of two weight matrices in a residual block should have a distinctive negative diagonal pattern.

**28:16** · This arises as a way for the model to keep the residual stream from growing out of control.

**28:20** · From this insight, he was able to recover the right pairings.

**28:23** · For ordering, Shawn noticed that the model seemed to improve if he sorted the blocks by the size of their residual contributions. Starting with that rough approximation, he combined a clever ranking heuristic with local swaps to recover the exact right order.

**28:36** · His full walkthrough is linked in the description.

**28:39** · Don't worry if you didn't get to this puzzle in time, though.

**28:40** · There's still one up about backdoored LLMs that even Jane Street doesn't know how to solve.

**28:44** · You can find it at janestreet.com/dwarkesh. Alright, back to Terence!

**28:51** · We do under-explore how to extract extra information from various signals.

**29:00** · Just to pick one random study, I remember reading once that people were trying to measure how often scientists actually read the papers that they cite. How do you measure this? You could try to survey different scientists, but they had a clever trick.

**29:21** · Many citations have little typos, like a number is wrong or punctuation is almost wrong.

**29:28** · They measured how often a typo got copied from one reference to the next, and they could infer whether an author was just copying and pasting a reference without actually checking it.

**29:40** · From that, they were able to infer some measure of how much attention people were paying.

**29:46** · So there are some clever tricks to extract… These questions you posed earlier of how we can assess whether a scientific development is fruitful, interesting, or represents real progress… Maybe there are really useful metrics or footprints of this phenomenon in data.

**30:12** · We can examine citations and how often something is mentioned in a conference.

**30:17** · Maybe there's a lot of sociology of science research to be done that could actually detect these things. Maybe we should get some astronomers on the case, actually. That brings us nicely to the progress that, from the outside, it seems like AI for math is making. You had a post recently where you pointed out that over the last few months, AI programs have solved fifty out of the eleven hundred odd Erdős problems. I don’t know if it’s still correct, but as of a month ago you said that there had been a pause because the low-hanging fruit had been picked.

### Selection bias in reported AI discoveries

**30:55** · First of all, I'm curious if that is still the case, that we have picked the low-hanging fruit and now we're at this plateau currently. It does seem so. Fifty-odd problems have been solved with AI assistance, which is great, but there's like six hundred to go.

**31:12** · People are still chipping away at one or two of these right now.

**31:17** · We're seeing a lot fewer pure AI solutions now where the AI just one-shots the problem.

**31:24** · There was a month where that happened and that has stopped, not for lack of trying.

**31:28** · I know of three separate attempts to get frontier model AIs to just attack every single one of the problems simultaneously. They pick out some minor observations, or maybe they find that some problem was already solved in the literature, but there hasn't been any further purely AI-powered solution yet. People are using AI a lot currently.

**31:50** · Someone might use AI to generate a possible proof strategy, and then another person will use a separate AI tool to critique it, rewrite it, generate some numerical data for it, or do a literature survey. Some problems have been solved by an ongoing conversation between lots of humans and lots of AI tools.

**32:11** · But it does seem like it was this one-off thing. Maybe one analogy for these problems is that you're in some sort of mountain range with all kinds of cliffs and walls.

**32:27** · Maybe there's a little wall which is three feet high, and one that's six feet high, and then there's fifteen feet high, and then there are some mile-high cliffs.

**32:39** · You're trying to climb as many of these cliffs as possible, but it's in the dark.

**32:43** · We don't know which ones are tall, which ones are short.

**32:46** · So we try to light some candles and make some maps, and slowly we figure out some of them are climbable. Some of them we can identify a partial track in the wall that you can reach first. These AI tools, they're like jumping machines that can jump two meters in the air, higher than any human.

**33:06** · Sometimes they jump in the wrong direction, and sometimes they crash, but sometimes they can reach the tops of the lowest walls that we couldn't reach before.

**33:18** · We've just set them loose in this mountain range, hopping around.

**33:23** · There was this exciting period where they could actually find all the low ones and reach them.

**33:32** · Maybe the next time there's a big advance in the models, they will try it again, and a few more will be breached. But it's a different style of doing mathematics.

**33:48** · Normally we would hill climb, make little markers, and try to identify partial things.

**33:56** · These tools either succeed or they fail. They've been really bad at creating partial progress or identifying intermediate stages that you should focus on first.

**34:09** · Going back to this previous discussion, we don't have a way of evaluating partial progress the same way we can evaluate a one-shot success or failure of solving a problem.

**34:19** · There's two different ways to think through what you've just said.

**34:23** · One of them is more bearish on AI progress, and one of them is more bullish.

**34:26** · The bearish one being, "Oh, they're only getting to a certain height of wall, which is not as high as humans are reaching." The second is that they have this powerful property that once they achieve a certain waterline, they can fill every single problem that is available at that waterline, which we simply can't do with humans.

**34:45** · We can't make a million copies of you and give each of them a million dollars of inference compute and have you do a hundred years of subjective time research on a million different problems at the same time. But once AIs reach Terence Tao-level, they could do that. Once they reach intermediate levels, they could do the intermediate version of that. The same reason that we should be bearish now is the reason we should be especially bullish. Not even when they achieve superhuman intelligence, but just when they achieve human-level intelligence, because their human-level intelligence is qualitatively wider and more powerful than our human-level intelligence. I agree.

**35:19** · They excel at breadth, and humans excel at depth, human experts at least. I think they're very complementary.

**35:30** · But our current way of doing math and science is focused on depth because that's where human expertise is, because humans can't do breadth. We have to redesign the way we do science to take full advantage of this breadth capability that we now have.

**35:51** · We should have a lot more effort in creating very broad classes of problems to work on rather than one or two really deep, important problems. We should still have the deep, important problems, and humans should still be working on them. But now we have this other way of doing science.

**36:10** · We can explore entirely new fields of science by first getting these broad, moderately competent AIs to map it out and make all the easy observations.

**36:21** · And then identify certain islands of difficulty, which human experts can then come and work on.

**36:29** · I see very much a future of very complementary science.

**36:34** · Eventually, you would hope to get both breadth and depth and somehow get the best of both worlds.

**36:41** · But we need practice with the breadth side. It's too new. We don't even have the paradigms to really take full advantage of it. But we will, and then science will be unrecognizable after that, I think. To this point about complementarity, programmers have noticed that they're way more productive as a result of these AI tools.

**37:05** · I don't know if you as a mathematician feel the same way, but it does seem like one big difference between vibe coding and vibe researching is that with software, the whole point is to have some effect on the world through your work.

**37:21** · If it leads to you better understanding a problem or coming up with some clean abstraction to embody in your code, that is instrumental to the end goal.

**37:29** · Whereas with research, the reason we care about solving the Millennium Prize Problems is that presumably that in the process of solving them, we discover new mathematical objects or new techniques that advance our civilization's understanding of mathematics.

**37:45** · So the proof is instrumental to the intermediate work.

**37:50** · I don't know if you agree with that dichotomy or if that in any way will explain the relative uplift we'll see in software versus research. Certainly in math, the process is often more important than the problem itself. The problem is kind of a proxy for measuring progress. I think even in software, there are different types of software tasks. If you just create a webpage that does the same thing that a thousand other webpages do, there's no skill to be learned.

**38:19** · Well, there is still some skill maybe that the individual programmer could pick up.

**38:24** · But for boilerplate-type code, it's something that you should definitely offload to AI.

**38:35** · Sometimes once you make the code, you still have to maintain it.

**38:39** · There are issues with upgrading it and making it compatible with other things.

**38:44** · I've heard programmers report that even if an AI can create the first prototype of a tool, making it mesh with everything else and making it interact with the real world in the way they want is an ongoing process. If you don't have the skills that you pick up from writing the code, that may impact your ability to maintain it down the road.

**39:10** · So yes, certainly mathematicians, we've used problems to build intuition and to train people to have a good idea of what's true, what to expect, what is provable, and what is difficult.

**39:26** · Just getting the answers right away may actually inhibit that process.

**39:35** · I made a distinction between theory and experiment before.

**39:39** · In most sciences, there's an equal division between the theoretical side and the experimental side. Math has been unique in that it's almost entirely theoretical. We place a premium on trying to have coherent, clean theories of why things are true and false. We haven't done many experiments as to, if we have two different ways to solve a problem, which is more effective.

**40:04** · We have some intuition, but we haven't done large-scale studies where we take a thousand problems and just test them. But we can do that now.

**40:13** · I think AI-type tools will actually revolutionize the experimental side of math, where you don't care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don't.

**40:30** · The same way that if you're a software company and you want to roll out a thousand pieces of software, you don't really want to handcraft each one and learn lessons from each.

**40:39** · You just want to find what workflows let you scale.

**40:46** · The idea of doing mathematics at scale is at its infancy.

**40:49** · But that's where AI is really going to revolutionize the subject.

**40:53** · I feel like a big crux in these conversations about how good AI will be for science is, I think you said this, that they're using existing techniques and modifying them.

**41:06** · It would be interesting to understand how much progress one can make simply from using existing techniques. If I looked at the top math journals, how many of the papers are coming up with a new technique, whatever that means, versus using existing techniques on new problems? What is the overhang? If you just applied every known technique to every open problem, would that constitute a humongous uplift in our civilization's knowledge, or would that not be that impressive and useful? This is a great question, and we don't have the data to fully answer it yet.

**41:38** · Certainly, a lot of work that human mathematicians do… When you take a new problem, one of the first things we do is we look at all the standard things that have worked on similar problems in the past, and we try them one by one.

**41:54** · Sometimes that works, and that's still worth publishing because the question was important.

**41:59** · Sometimes they almost work, and you have to add one more wrinkle to it, and that's also interesting. But the papers that go into the top journals are usually ones where the existing methods can kind of solve 80% of the problem, but then there is this 20% which is resistant and a new technique has to be invented to fill in the gaps.

**42:21** · It's very rare now that a problem gets solved with no reliance on past literature, where all the ideas come out of nowhere. That was more common in the past, but math is so mature now that it's just so much of a handicap to not use the literature first.

**42:44** · AI tools are getting really good at the first part of that, just trying all the standard techniques on a problem, often making fewer mistakes in applying them than humans.

**42:55** · They still make mistakes, but I've tested these tools on little tasks that I can do, and sometimes they pick up errors that I make. Sometimes I pick up errors that they make.

**43:07** · It's about a tie right now. But I haven't yet seen them take the next step.

**43:17** · When there are holes in the argument where none of the things are working, then what do you do?

**43:25** · They can suggest random things, but often I find that trying to chase them down to make them work, and finding they don't work, wastes more time than it saves.

**43:38** · I think some fraction of problems that we currently think are hard will fall from this method, especially the ones that haven't received enough attention.

**43:48** · With the Erdős problems, almost all of the 50 problems that were solved by AIs were ones for which there was basically no literature. Erdős posed the problem once or twice.

**43:59** · Maybe some people tried it casually and couldn't do it, but they never wrote up anything.

**44:03** · But it turned out that there was a solution, and it was just combining this one obscure technique that not many people know about with some other result in the literature.

**44:12** · That's the median level of what AI can accomplish, and that's really great.

**44:17** · It clears out 50 of these problems. So I think you will see some isolated successes.

**44:24** · But what we found… Some people have done large-scale sweeps of these Erdős problems.

**44:29** · If you only focus on the success stories, the ones that get broadcast on social media, it looks amazing. All these problems that haven't been solved for decades, now they're falling. But whenever we do a systematic study, on any given problem an AI tool has a success rate of maybe 1% or 2%.

**44:46** · It's just that they can buy scale, and you just pick the winners. It looks great. I think there'll be a similar thing happening with the hundreds of really prestigious, difficult math problems out there. Some AI may get lucky and actually solve them, and there will be some backdoor to solve the problem that everyone else missed.

**45:08** · That will get a lot of publicity. But then people will try these fancy tools on their own favorite problem, and they will again experience the 1% to 2% success rate.

**45:18** · There'll be a lot of noise amongst the signal of when they're working and when they're not.

**45:28** · It will be increasingly important to collect these really standardized datasets.

**45:32** · There are efforts now to create a standard set of challenge problems for AIs to solve, and not just rely on the AI companies to only publish their wins and not disclose their negative results.

**45:44** · That will maybe give more clarity as to where we're actually at.

**45:48** · Although I think it's worth emphasizing how much progress in AI it constitutes already, to have models that are capable of applying some technique that nobody had written down as applicable to this particular problem. The progress is simultaneously amazing and disappointing. It is a very strange feeling to see these tools in action. But people also acclimatize really quickly.

**46:12** · I remember when Google's web search came out 20 years ago.

**46:16** · It just blew all the other searches out of the water.

**46:18** · You're getting relevant hits on the front page, exactly what you wanted.

**46:23** · It was amazing, and then after a few years, you just took for granted that you could Google anything. 2026-level AI would be stunning in 2021.

**46:35** · A lot of it—face recognition, natural speech, doing college-level math problems—we just take for granted now. Speaking of 2026 AI, you made a prediction in 2023 that by 2026 it would be like a colleague in mathematics?

### AI makes papers richer and broader, but not deeper

**46:53** · A trustworthy co-author if used correctly. Which is looking pretty good in retrospect.

**46:57** · Yeah, I'm pretty pleased. So let's see if you can continue this streak.

**47:04** · You personally are 2x more productive as a result of AI.

**47:08** · What year would you say that? Productivity, I think, is not quite a one-dimensional quantity. I'm definitely noticing that the style in which I do mathematics is changing quite a bit, and the type of things I do.

**47:23** · For example, my papers now have a lot more code, a lot more pictures, because it's so easy to generate these things now. Some plot which would have taken me hours to do, now I can do in minutes. But in the past, I just wouldn't have put the plot in my paper in the first place. I would just talk about it in words.

**47:41** · So it's hard to measure what 2x means. On the one hand, I think the type of papers that I would write today, if I had to do them without AI assistance, would definitely take five times longer. But I would not write my papers that way.

**47:58** · 5x? Yeah, but these are auxiliary tasks.

**48:06** · Things like doing a much deeper literature search or supplying a lot more numerics.

**48:14** · They enrich the paper. The core of what I do, actually solving the most difficult part of a math problem, hasn't changed too much. I still use pen and paper for that.

**48:28** · But there's lots of silly things. I use an AI agent now to reformat.

**48:35** · Sometimes if all my parentheses are not quite the right size, I used to manually change them by hand, and now I can get an AI agent to do all that quite nicely in the background.

**48:46** · They've really sped up lots of secondary tasks. They haven't yet sped up the core thing that I do, but it's allowed me to add more things to my papers.

**49:00** · By the same token, if I were to write a paper I wrote in 2020 again—and not add all these extra features, but just have something of the same level of functionality—it actually hasn't saved that much time, to be honest. It's made the papers richer and broader, but not necessarily deeper. You made this distinction between artificial cleverness and artificial intelligence. I would like to better understand those concepts.

**49:29** · What is an example of intelligence that is not just cleverness?

**49:40** · Intelligence is famously hard to define.

**49:41** · It's one of these things that you know when you see it.

**49:45** · But when I talk to someone and we're trying to collaboratively solve a math problem together, there's this conversation where neither of us knows how to solve the problem initially.

**50:00** · One of us has some idea and it looks promising, so then we have some sort of prototype strategy.

**50:06** · We test it, and it doesn't work, but then we modify it.

**50:10** · There's adaptivity and continual improvement of the idea over time.

**50:18** · Eventually, we've systematically mapped out what doesn't work and what does work, and we can see a path forward, but it's evolving with our discussion.

**50:30** · This isn't quite what the AIs do. The AIs can mimic this a little bit.

**50:37** · To go back to this analogy of these jumping robots, they can jump and fail, and jump and fail.

**50:44** · But what they can't do is jump a little bit, reach some handhold, stay there, pull other people up, and then try to jump from there. There isn't this cumulative process which is built up interactively. It seems to be a lot more trial and error and just repetition: brute force. It scales, and it can work amazingly well in certain contexts. But this idea of building up cumulatively from partial progress is what's still not quite there yet.

**51:23** · Interesting. You're saying if Gemini 3 or Claude 4.5, whatever, solves a problem, it is not the case that its own understanding of math has progressed.

**51:32** · No. Or even if it works on a problem without solving it, it's not that its own understanding of math has progressed.

**51:36** · Yeah. You run a new session and it's forgotten what it just did.

**51:40** · It has no new skills to build on related problems. Maybe what you just did is 0.001% of the training data for the next generation. So maybe eventually some of it gets absorbed.

**51:54** · So Terence talks about the importance of decomposing particularly gnarly problems into a series of easier chunks. Even if this doesn't result in the full solution, approaching problems in this way helps you build up the intuitions and practice the techniques that you'll need to keep making progress. But models today tend to struggle with these kinds of problem-solving techniques. That's where Labelbox comes in.

**52:14** · Labelbox helps you train models not just to get the right answer, but to think the right way.

**52:19** · They've operationalized these reasoning behaviors into rubrics, giving you the ability to evaluate every important dimension of a model's output. These rubrics go beyond simple correctness.

**52:28** · Did the model reach for the right tools? Did it check its own work and explore alternative paths? How clear was its response?

**52:35** · These skills are useful across domains: math, physics, finance, psychology, and more.

**52:40** · And they're becoming increasingly important as models take on harder, open-ended problems, some of which have multiple solutions and some of which we don't even know the solutions to.

**52:48** · Labelbox can get you rubrics tailored to your domain, helping you systematically measure and shape how your models think. Learn more at labelbox.com/dwarkesh.

### If AI solves a problem, can humans get understanding out of it?

**53:00** · One big question I have is how plausible is it that if we just keep training AIs—they get better and better at solving problems in Lean—that they will continue to solve more and more impressive problems, and then we will be surprised at how little insight we got from some Lean solution to proving the Riemann hypothesis or something. Or do you think it is a necessary condition of solving the Riemann hypothesis, even by an AI that is doing it entirely in Lean, that the constructions and definitions created in the Lean program have to advance our understanding of mathematics? Or could it just be assembly code gobbledygook?

**53:40** · We don't know. Some problems have been basically solved by pure brute force.

**53:44** · The four color theorem is a famous example. We have still not found a conceptually elegant proof of this theorem, and maybe we never will. Some problems may only be solvable by splitting into an enormous number of cases and doing brute force, uninsightful computer analysis on each case.

**54:00** · Part of the reason we prize problems like the Riemann hypothesis is that we're pretty sure a new type of mathematics has to be created, or a new connection between two previously unconnected areas of mathematics has to be discovered to make this work. We don't even know what the shape of the solution is, but it doesn't feel like a problem that will be solved just by exhaustively checking cases.

**54:30** · Or it could be false actually. Okay, there is an unlikely scenario that the hypothesis is false, and you can just compute a zero off the line, and a massive computer calculation verifies it. That would be very disappointing. I do feel that fully autonomous, one-shot approaches are not the right approach for these problems.

**54:59** · You'll get a lot more mileage out of the interplay of humans collaborating with these tools.

**55:08** · I can see one of these problems being solved by smart humans assisted by extremely powerful AI tools. But the exact dynamic may be very different from what we envision right now. It could be a collaboration of a type that just doesn't exist yet. There may be a way to generate a million variants of the Riemann zeta function and do AI-assisted data analysis to discover some pattern connecting them that we didn't know about before.

**55:41** · This lets you transform the problem into a different area of mathematics. There could be all kinds of scenarios.

**55:51** · Suppose the AI figures it out, and latent in the Lean is some brand-new construction which, if we realized its significance, we would be able to apply in all these different situations.

**56:04** · How would we even recognize it? Again, a very naive question, but if you come up with the equivalent of Descartes' idea that you can have a coordinate system unifying algebra and geometry, in Lean code it would just look like R→R, and it wouldn't look that significant.

**56:22** · I'm sure there are other constructions which have this kind of property.

**56:26** · The beauty of formalizing a proof in something like Lean is that you can take any piece of it and study it atomically. When I read a paper which solves some difficult problem, there's often a big sequence of lemmas and theorems.

**56:44** · Ideally, the author will talk their way through what's important and what's not.

**56:48** · But sometimes they don't reveal what steps were the important ones and which ones were just boilerplate, standard steps. You can study each lemma in isolation.

**56:59** · Some of them I can see look fairly standard and resemble something I'm familiar with.

**57:04** · I'm pretty sure there's nothing interesting going on there.

**57:06** · But this other lemma, that's something I haven't seen before, and I can see why having this result would really help prove the main result. You can assess whether a step is really key to your argument or not, and Lean really facilitates that.

**57:26** · The individual steps are identified really precisely.

**57:29** · I think in the future, there will be entire professions of mathematicians who might take a giant Lean-generated proof and do some ablation on it, trying to remove parts of it and find more elegant ways. They might get other AIs to do some reinforcement learning to make the proof more elegant, and maybe other AIs will grade whether this proof looks better or not. One thing that will change quite a bit in the near future is how we write papers. Until recently, writing papers was the most time-consuming and expensive part of the job. So you did it very rarely.

**58:07** · You only wrote up your results once all the other parts of your argument were checked out, because rewriting and refactoring was just a total pain. That's become a lot easier now with modern AI tools. You don't have to have just one version of your paper. Once you have one, people can generate hundreds more. One giant messy Lean proof may not be very meaningful or understandable on its own, but other people can refactor it and do all kinds of things with it. We've seen this with the Erdős problem website.

**58:42** · An AI will generate a proof, and here are 3,000 lines of code that verify the proof.

**58:47** · Then people got other AIs to summarize the proof, and people write their own proofs. There's actually post-processing. Once you have one proof, we have a lot of tools now to deconstruct and interpret it. It's a very nascent area of mathematics, but I'm not as worried about it. Some people are concerned about what happens if the Riemann hypothesis is proven with a completely incomprehensible proof.

**59:14** · I think once you have the artifact of a proof, we can do a lot of analysis on it.

### We need a semi-formal language for the way that scientists actually talk to each other

**59:20** · You posted recently that it would be helpful to have a formal or semi-formal language for mathematical strategies as opposed to just mathematical proofs, which is what Lean specializes in. I would love to learn more about what that would involve or look like. We don't really know. We've been very lucky in mathematics that we have worked out the laws of logic and mathematics, but this is a fairly recent accomplishment. It was started by Euclid two millennia ago, but only in the early 20th century did we finally list out the axioms of mathematics, the standard axioms of what we call ZFC, the axioms of first-order logic, and what a proof is.

**1:00:00** · This we've managed to automate and have a formal language for.

**1:00:05** · There could be some way to assess plausibility. You have a conjecture that something is true, you test a few examples, and it works out. How does this increase your confidence that the conjecture is true? We have a few sort of mathematical ways to model this, like Bayesian probability, for example. But you often have to set certain base assumptions, and there's a lot of subjectivity still in these tasks.

**1:00:44** · This is more of a wish than a plan to develop these languages, but just seeing how successful having a formal framework in place, like Lean, has made deductive proofs so much easier to automate and train AI on… The bottleneck for using AI to create strategies and make conjectures is we have to rely on human experts and the test of time to validate whether something is plausible or not.

**1:01:16** · If there was some semi-formal framework where this could be done semi-automatically in a way that isn't easily hackable... It's really important with these formal proof assistants that there are no backdoors or exploits you can use to somehow get your certified proof without actually proving it, because reinforcement learning is just so good at finding these backdoors.

**1:01:44** · If there's some framework that mimics how scientists talk to each other in a semi-formal way, using data and argument, but also constructing narratives... There's some subjective aspect of science that we don't know how to capture in a way that we can insert AI into it in any useful way.

**1:02:18** · This is a future problem. There are research efforts to try to create automated conjectures, and maybe there are ways to benchmark these and simulate this, but it's all very new science.

**1:02:35** · Can you help me get some intuition? I have two sub-questions. One, it would be very helpful to have a specific example of what something like this would look like, the way scientists communicate that we can't formalize yet. Two, it seems almost definitionally paradoxical to say you're building up some narrative or natural language explanation and then also having something which you could have formalized.

**1:03:10** · I'm sure there's some intuition behind where that overlap is, and I'd love to understand that better.

**1:03:20** · An example of a conjecture: Gauss was interested in the prime numbers and created one of the first mathematical datasets. He just computed the first 100,000 prime numbers or so, hoping to find patterns. He did find a pattern, but maybe not the pattern he was expecting. He found a statistical pattern in the primes that if you count how many primes there are up to 100, 1,000, one million, and so forth, they get sparser and sparser, but the drop-off in the density was inversely proportional to the natural logarithm of the range of numbers.

**1:03:54** · So he conjectured what we now call the prime number theorem: the number of primes up to X is X divided by the natural log of X.

**1:04:05** · He had no way to prove this. It was data-driven. This was a conjecture.

**1:04:12** · It was revolutionary for its time because it was maybe the first really important conjecture of math that was statistical in nature. Normally you're talking about a pattern, like maybe the spacing between the primes has a certain regularity.

**1:04:27** · But this didn't tell you exactly how many primes there were in any given range.

**1:04:32** · It just gave you an approximation that got better and better as you went further and further out.

**1:04:42** · It started the field of what we call analytic number theory.

**1:04:47** · It was the first in many conjectures like this, many of which got proved, which started consolidating the idea that the prime numbers didn't really have a pattern, that they behaved like random sets of numbers with a certain density.

**1:05:03** · They had some patterns, like they're almost all odd.

**1:05:07** · They're also not actually random, they're what's called pseudo-random.

**1:05:10** · There's no random number generation involved in creating the prime numbers.

**1:05:14** · But over time, it became more and more productive to think of the primes as if they were just generated by some god rolling dice all the time and creating this random set.

**1:05:26** · This allowed us to make all these other predictions.

**1:05:28** · There's a still-open conjecture in number theory called the twin prime conjecture, that there should be infinitely many pairs of primes that are twins just two apart, like 11 and 13.

**1:05:37** · We can't prove that, and there are good reasons why we can't prove it.

**1:05:41** · But because of this statistical random model of the primes, we are absolutely convinced it's true.

**1:05:46** · We know that if the primes were generated by flipping coins, we would just—by random chance like infinite monkeys at a typewriter—see twin primes appear over and over again.

**1:05:57** · We have over time developed this very accurate conceptual model of what the primes should behave like based on statistics and probability. It's mostly heuristic and non-rigorous, but extremely accurate. The few times when we actually can prove things about the primes, it has matched up with the predictions of what we call the random model of the primes. We have this conjectural concept framework for understanding the primes that everyone believes in.

**1:06:25** · It's the same reason why we believe the Riemann hypothesis is true, and why we believe that cryptography based on the primes is mathematically secure.

**1:06:35** · It's all part of this belief. In fact, one reason why we care about the Riemann hypothesis is that if the Riemann hypothesis failed, if we knew it was false, it would be a serious blow to this model.

**1:06:49** · It would mean there's a secret pattern to the primes that we were not aware of.

**1:06:54** · I think we would very rapidly abandon any cryptography based on the primes, because if there was one pattern that we didn't know about, there are probably more, and these patterns can lead to exploits in crypto. It would be a big shock.

**1:07:07** · So we really want to make sure that doesn't happen.

**1:07:15** · We've been convinced of things like the Riemann hypothesis over time.

**1:07:20** · Some of it is experimental evidence, and some is that the few times we've been able to make theoretical results, they've always aligned. It is possible that the consensus is wrong and we've all just missed something very basic. There have been paradigm shifts in the past in scientific history. But we don't really have a way of measuring this, partly because we don't have enough data on how math or science develops.

**1:07:46** · We have one timeline of history, and we have maybe 100 stories of turning points in history.

**1:07:53** · If we had access to a million alien civilizations, each with a different development of history and science in different orders, then maybe we'd actually have a decent shot at understanding how we measure what progress is and what is a good strategy.

**1:08:12** · We could maybe start formalizing it and actually having a framework.

**1:08:18** · Maybe what we need to do is start creating lots of mini-universes or simulations of AI solving very basic problems in arithmetic or whatever, but coming up with their own strategies for doing these things and having these little laboratories to test.

**1:08:34** · There are people who investigate what's the smallest neural network that can do 10-digit multiplication and things like that. I think we could learn a lot just from evolving small AIs on simple problems. I was super excited when Mercury reached out about sponsoring the podcast because I've been banking with them for years.

**1:08:54** · I think I opened my first account with them in 2023.

**1:08:56** · Something I've come to appreciate over the last few years is that Mercury is constantly updating things and adding new features. Take their newest feature, Insights.

**1:09:03** · Insights summarizes your money in and out, showing you your biggest transactions and calling out anything that deserves extra attention. Like maybe your revenue from a particular partner has gone down, or you've got a big uncategorized purchase that needs to be investigated.

**1:09:15** · It's a super low-friction way for me to keep tabs on my business and make quick decisions.

**1:09:19** · For example, I try to invest any cash that I don't need on hand to keep running the business.

**1:09:23** · With Insights, with just a couple of clicks, I was able to see exactly how much money I spent in each month of 2025 and that lets me know exactly how much cash I'll need for the next year or so of operations. And then I can go invest the rest.

**1:09:35** · Mercury just keeps adding new features like this. Go to mercury.com to check it out.

**1:09:39** · Mercury is a fintech company, not an FDIC Insured Bank.

**1:09:42** · Banking services provided through Choice Financial Group and Column NA, members FDIC.

### How Terry uses his time

**1:09:48** · You have to learn about new fields not only very rapidly, but deeply enough to contribute to the frontier. So in some sense, you're also one of the world's greatest autodidacts. What is your process of learning about a new subfield in math? What does that look like? We talked about depth and breadth before.

**1:10:12** · It's not a purely human-AI distinction. Humans also, I think it was Berlin who split them into hedgehogs and foxes. The hedgehog knows one thing very well, and a fox knows a little bit about everything. I definitely think of myself as a fox.

**1:10:32** · I work with hedgehogs a lot, and sometimes I can be a hedgehog if need be.

**1:10:40** · I've always had a little bit of an obsessive streak.

**1:10:43** · If there's something I read about which I feel like I have the capability to understand, but I don't understand why it works and there's some magic in it… Someone was able to use a type of mathematics I'm not familiar with and get a result I would like to prove.

**1:10:58** · I can't do it myself, but they could do it by their method, and I want to find out what their trick was. It bugs me that someone else can do something I think I can do, but I can't. I've always had that obsessive, completionist streak. I've had to wean myself off computer games because if I start a game, I want to play it to completion, through all the levels.

**1:11:23** · That's one way I learn new fields. I collaborate with a lot of people who have taught me other types of mathematics. I just make friends with another mathematician working on another area of mathematics. I find their problems interesting, but they have to teach me some of the basic tricks, what's known, and what's not known.

**1:11:44** · I learn a lot from that. I found that writing about what I've learned helps. I have a blog where I sometimes record things I've learned. In the past when I was younger, I would learn something, do this cool trick, and say, "Okay, I'm going to remember this."

**1:12:02** · Then six months later, I'd forgotten it. I remember remembering it, but I can't reconstruct my arguments. The first few times, it was so frustrating to have understood something and then lost it. I resolved I should always write down anything cool that I've learned. That's part of how this blog came about.

**1:12:22** · How long does it take you to write a blog post? It's something I often do when I don't want to do other work. There's some referee report or something that feels slightly unpleasant for me to do at the time.

**1:12:35** · Writing a blog feels creative and fun. It's something I do for myself.

**1:12:42** · Depending on the topic, it could be a quick half an hour or several hours.

**1:12:49** · Because it's something I do voluntarily, time flies when I write these things down, as opposed to doing something I have to do for administrative reasons that is just drudgery.

**1:13:03** · Those are tasks, by the way, that AI is really helping with nowadays.

**1:13:07** · If civilization could from first principles decide how to use Terry Tao's time, as a limited resource, what is the biggest difference? What if the veil of ignorance got to decide how to use Terry Tao's time versus what it does now? This podcast wouldn't be happening.

**1:13:29** · As much as I complain about certain tasks that I don't want to do, but have to do… As you get more senior in academia, you get more and more responsibilities, more committees, and whatever.

**1:13:42** · I have also found that a lot of events I reluctantly went to because I was obliged to for one reason or another… Because it's outside my comfort zone, it often results in interactions with people I wouldn't normally talk to, like you for instance.

**1:13:57** · I would learn interesting things and have interesting experiences.

**1:14:01** · I would have opportunities to then network with other people that I never would have before.

**1:14:08** · So I do believe a lot in serendipity. I do optimize portions of my day where I schedule very carefully. But I am willing to leave some portions just to do something that is not my usual thing. Maybe it'll be a waste of my time, but maybe I will learn something. More often than not, I get a positive experience that I wouldn't have planned for. So I believe a lot in serendipity.

**1:14:45** · Maybe there's a danger in modern societies, not just with AI, that we've become really good at optimizing everything. We’re not optimizing our own optimization.

**1:14:59** · With COVID, for example, we switched a lot to remote meetings, so everything was scheduled.

**1:15:07** · We kept busy in academia. We met almost the same number of people we met in person, but everything had to be planned in advance. What we lost out on was the casual knocking on a hallway door, just meeting someone while getting a coffee.

**1:15:28** · Those serendipitous interactions may not seem optimal, but they are actually really important.

**1:15:37** · When I was a grad student, I would go to the library to look for a journal article.

**1:15:42** · You had to physically check out the journal and read the article.

**1:15:46** · You could browse through and sometimes the next article was also interesting.

**1:15:52** · Sometimes it wasn’t, but you could accidentally find interesting things.

**1:15:56** · That has basically been lost now. If you want to access an article, you just type it into a search engine or an AI, and you get exactly what you want instantly.

**1:16:06** · But you don't get the accidental things you might have found if you'd done it more inefficiently.

**1:16:20** · I spent a year once at the Institute for Advanced Study, which is a great place with no distractions. You're there just to do research.

**1:16:29** · The first few weeks you're there, it's great. You're getting all these papers written up that you've been wanting to do for a long time. You think about problems for blocks of hours at a time. But I find if I stay there for more than several months, I run out of inspiration. I get bored. I surf the internet a lot more.

**1:16:46** · You actually do need a certain level of distraction in your life.

**1:16:50** · It adds enough randomness and high temperature. I don't know the optimal way to schedule my life. It just seems to work. I'm very curious when you expect AIs that can actually do frontier math at least as well as the best human mathematicians.

### Human-AI hybrids will dominate math for a lot longer

**1:17:15** · In some ways, they're already doing frontier math that is super intelligent that humans can't do, but it's a different frontier from what we're used to.

**1:17:24** · You could argue that calculators were doing frontier math that humans could not accomplish, but it was number crunching. But replacing Terry Tao completely.

**1:17:38** · I mean, what do you want me for? You'll just go on all the podcasts after.

**1:17:50** · It might not be the right question to ask. I think within a decade, a lot of things that math students currently do—what we spend the bulk of our time doing and a lot of stuff we put in our papers today—can be done by AI. But we will find that that actually wasn't the most important part of what we do. A hundred years ago, a lot of mathematicians were just solving differential equations.

**1:18:20** · Physicists needed some exact solution to some system, and they hired a mathematician to laboriously go through the calculus and work out the solution to this fluid equation, whatever. A lot of what a 19th-century mathematician would do, you could make a call to Mathematica, Wolfram Alpha, a computer algebra package, or now more recently to an AI, and it would just solve the problem in a few minutes. But we moved on. We worked on different types of problems after that.

**1:18:53** · Once computers came along—computers used to be human. People used to laboriously create log tables and work out primes as Gauss did, and that has all been outsourced to computers. But we moved on. In genetics, to sequence the genome of a single organism, that was an entire PhD of a geneticist, carefully separating all the chromosomes and whatever.

**1:19:23** · Now you can just spend $1,000 and send it to a sequencer and get it done.

**1:19:26** · But genetics is not dead as a subject. You move to a different scale.

**1:19:31** · Maybe you study whole ecosystems rather than individuals.

**1:19:34** · I take your point but when is most mathematical progress, or almost all mathematical progress, happening by AI? If you find out this year a Millennium Prize Problem has been solved, you would put 95% odds that an AI did it autonomously.

**1:19:49** · Surely there will be such a year. I guess I do believe that hybrid human plus AIs will dominate mathematics for a lot longer. It will depend. It will require some additional breakthroughs beyond what we already have, so it's going to be stochastic.

**1:20:11** · I think AIs currently are very good at certain things, but really terrible at others.

**1:20:16** · While you can add more and more frameworks on top to reduce the error rates and make them work with each other a bit more, it feels like we don't have all the ingredients to really have a truly satisfactory replacement for all intellectual tasks. It is complementary currently. It's not a replacement. Because current level AIs will accelerate science in so many ways, hopefully new discoveries and new breakthroughs will happen more quickly.

**1:21:01** · It's also possible that by destroying serendipity we actually inhibit certain types of progress.

**1:21:07** · Anything is possible at this point. I think the world is very, very unpredictable at this point in time. What is your advice to somebody who would consider a career in math or is early in a career in math, especially in light of AI progress?

**1:21:25** · How should they be thinking about their career differently, if at all, as a result of AI progress? We live in a time of change.

**1:21:32** · As I said, we live in a particularly unpredictable era.

**1:21:41** · Things that we've taken for granted for centuries may not hold anymore.

**1:21:48** · The way we do everything, and not just mathematics, will change.

**1:21:59** · In many ways, I would prefer the much more boring, quiet era where things are much the same as they were 10 years ago, 20 years ago. But I think one just has to embrace that there's going to be a lot of change. The things that you study, some of them may become obsolete or revolutionized, but some things will be retained.

**1:22:26** · You always have to keep an eye on opportunities for things that you wouldn't be able to do before.

**1:22:37** · In math, you previously had to go through years and years of education and be a math PhD before you could contribute to the frontier of math research.

**1:22:46** · But now it's quite possible at the high school level, or whatever, that you could get involved in a math project and actually make a real contribution because of all these AI tools, Lean, and everything else. There will be a lot of non-traditional opportunities to learn, so you need a very adaptable mindset.

**1:23:06** · There will be room for pursuing things just for curiosity and for playing around.

**1:23:11** · You still need to get your credentials. For a while it will still be important to go through traditional education and learn math and science the old-fashioned way.

**1:23:28** · But you should also be open to very different ways of doing science, some of which don't exist yet.

**1:23:37** · It's a scary time, but also very exciting. That's a great note to close on. Terence, thanks so much. Pleasure.
