---
title: "Infinity, Paradoxes, Gödel Incompleteness & the Mathematical Multiverse"
source: "https://www.youtube.com/watch?v=14OPT6CcsH4"
transcript_source: "https://lexfridman.com/joel-david-hamkins-transcript/"
episode_url: "https://lexfridman.com/joel-david-hamkins/"
author:
  - "[[Lex Fridman]]"
guest:
  - "[[Joel David Hamkins]]"
guest_title: "Mathematician & Philosopher"
published: 2025-12-31
created: 2026-07-24
description: "This is a transcript of Lex Fridman Podcast #488 with Joel David Hamkins. The timestamps in the transcript are clickable links that take you directly to that point in the main video. Please note that the transcript is human generated, and may have errors. Here are some useful links: Go back to this episode’s main page Watch the full YouTube version of the podcast Table of Contents Here are the loose “chapters” in the conversation. Click link to jump approximately to that part in the transcript: "
analysis_report: '[[Lex Fridman - Joel David Hamkins：Infinity, Paradoxes, Gödel Incompleteness & the Mathematical Multiverse]]'
tags:
  - "transcript"
---
![](https://www.youtube.com/watch?v=14OPT6CcsH4)

This is a transcript of Lex Fridman Podcast #488 with Joel David Hamkins. The timestamps in the transcript are clickable links that take you directly to that point in the main video. Please note that the transcript is human generated, and may have errors. Here are some useful links: Go back to this episode’s main page Watch the full YouTube version of the podcast Table of Contents Here are the loose “chapters” in the conversation. Click link to jump approximately to that part in the transcript: 

Timestamps:
0:00 - Introduction
2:17 - Infinity & paradoxes
49:27 - Russell’s paradox
1:02:35 - Gödel’s incompleteness theorems
1:20:06 - Truth vs proof
1:31:30 - The Halting Problem
1:47:23 - Does infinity exist?
2:04:57 - MathOverflow
2:08:49 - The Continuum Hypothesis
2:18:36 - Hardest problems in mathematics
2:28:03 - Mathematical multiverse
2:46:55 - Surreal numbers
2:57:33 - Conway’s Game of Life
2:59:49 - Computability theory
3:09:41 - P vs NP
3:12:58 - Greatest mathematicians in history
3:26:43 - Infinite chess
3:45:01 - Most beautiful idea in mathematics

## Transcript


### Introduction

**0:00** · Lex Fridman: The following is a conversation with Joel David Hamkins, a mathematician and philosopher specializing in set theory, the foundation of mathematics, and the nature of infinity. He is the number one highest rated user on MathOverflow, which I think is a legendary accomplishment. MathOverflow, by the way, is like StackOverflow but for research mathematicians. He is also the author of several books, including Proof in The Art of Mathematics and Lectures on the Philosophy of Mathematics. And he has a great blog, infinitelymore.xyz. This is a super technical and super fun conversation about the foundation of modern mathematics and some mind-bending ideas about infinity, nature of reality, truth, and the mathematical paradoxes that challenged some of the greatest minds of the 20th century.

**1:02** · Lex Fridman: I have been hiding from the world a bit, reading, thinking, writing, soul-searching, as we all do every once in a while. But mostly, just deeply focused on work and preparing mentally for some challenging travel I plan to take on in the new year. Through all of it, a recurring thought comes to me, how damn lucky I am to be alive and to get to experience so much love from folks across the world. I want to take this moment to say thank you from the bottom of my heart for everything, for your support, for the many amazing conversations I’ve had with people across the world. I got a little bit of hate and a whole lot of love, and I wouldn’t have it any other way. I’m grateful for all of it. This is the Lex Fridman Podcast.

**2:00** · Lex Fridman: To support it, please check out our sponsors in the description, where you can also find ways to contact me, ask questions, give feedback, and so on. And now, dear friends, here’s Joel David Hamkins.


### Infinity & paradoxes

**2:17** · Lex Fridman: Some infinities are bigger than others. This idea from Cantor at the end of the 19th century, I think it’s fair to say, broke mathematics before rebuilding it. I also read that this was a devastating and transformative discovery for several reasons. So one, it created a theological crisis, because infinity is associated with God, how could there be multiple infinities? Also, Cantor was deeply religious himself. Second, there’s a kind of mathematical civil war. The leading German mathematician, Kronecker, called Cantor a corrupter of youth and tried to block his career.

**2:57** · Lex Fridman: Third, many fascinating paradoxes emerged from this, like Russell’s paradox, about the set of all sets that don’t contain themselves, and those threatened to make all of mathematics inconsistent. Finally, on the psychological and personal side, Cantor’s own breakdown. He literally went mad, spending his final years in and out of sanatoriums, obsessed with proving the continuum hypothesis. So laying that all out on the table, can you explain the idea of infinity, that some infinities are larger than others, and why was this so transformative to mathematics?

**3:35** · Joel David Hamkins: Well, that’s a really great question. I would want to start talking about infinity and telling the story much earlier than Cantor actually, because, I mean, you can go all the way back to Ancient Greek times when Aristotle emphasized the potential aspect of infinity as opposed to the impossibility, according to him, of achieving an actual infinity. Archimedes’ method of exhaustion where he is trying to understand the area of a region by carving it into more and more triangles, say, and sort of exhausting the area and thereby understanding the total area in terms of the sum of the areas of the pieces that he put into it. And it proceeded on this kind of potential understanding of infinity for hundreds, thousands of years.

**4:25** · Joel David Hamkins: Almost all mathematicians were potentialists only and thought that it was incoherent to speak of an actual infinity at all. Galileo is an extremely prominent exception to this, though he argued against this sort of potentialist orthodoxy in The Dialogue of Two New Sciences. Really lovely account there that he gave. In many ways, Galileo was anticipating Cantor’s developments, except he couldn’t quite push it all the way through and ended up throwing up his hands in confusion, in a sense. The Galileo paradox is the idea or the observation that if you think about the natural numbers, I would start with zero, but I think maybe he would start with one.

**5:17** · Joel David Hamkins: The numbers one, two, three, four, and so on, and you think about which of those numbers are perfect squares. So zero squared is zero and one squared is one and two squared is four, three squared is nine, 16, 25, and so on. And Galileo observed that the perfect squares can be put into a one-to-one correspondence with all of the numbers. I mean, we just did it. I associated every number with its square. And so it seems like on the basis of this one-to-one correspondence that there should be exactly the same number of squares, perfect squares, as there are numbers, and yet there are all the gaps in between the perfect squares, right?

**6:03** · Joel David Hamkins: And this suggests that there should be fewer perfect squares, more numbers than squares because the numbers include all the squares plus a lot more in between them, right? And Galileo was quite troubled by this observation because he took it to cause a kind of incoherence in the comparison of infinite quantities, right? Another example is, if you take two line segments of different lengths, and you can imagine drawing a kind of foliation, a fan of lines that connect them. So the endpoints are matched from the shorter to the longer segment, and the midpoints are matched and so on. So spreading out the lines as you go. And so every point on the shorter line would be associated with a unique, distinct point on the longer line in a one-to-one way.

**6:57** · Joel David Hamkins: And so it seems like the two line segments have the same number of points on them because of that, even though the longer one is longer. And so it makes, again, a kind of confusion over our ideas about infinity. Also, with two circles, if you just place them concentrically and draw the rays from the center, then every point on the smaller circle is associated with a corresponding point on the larger circle, in a one-to-one way. And again, that seems to show that the smaller circle has the same number of points on it as the larger one, precisely because they can be put into this one-to-one correspondence.

**7:36** · Joel David Hamkins: Now, of course, the contemporary attitude about this situation is that those two infinities are exactly the same, and that Galileo was right in those observations about the equinumerosity. The way we would talk about it now is to appeal to what I call the Cantor-Hume principle, or some people just call it Hume’s principle, which is the idea that if you have two collections, whether they’re finite or infinite, then we want to say that those two collections have the same size, they’re equinumerous, if and only if there’s a one-to-one correspondence between those collections. And so Galileo was observing that line segments of different lengths are equinumerous, and the perfect squares are equinumerous with the whole…

**8:17** · Joel David Hamkins: All of the natural numbers, and any two circles are equinumerous and so on. The tension between the Cantor-Hume principle and what could be called Euclid’s principle, which is that the whole is always greater than the part, is a principle that Euclid appealed to in the Elements. Many times when he’s calculating area and so on, he wants… It’s a kind of basic idea that if something is just a part of another thing, then the whole is greater than the part. And so what Galileo was troubled by was this tension between what we call the Cantor-Hume principle and Euclid’s principle.

**8:59** · Joel David Hamkins: It really wasn’t fully resolved, I think, until Cantor. He’s the one who really explained so clearly about these different sizes of infinity and so on in a way that was so compelling. So he exhibited two different infinite sets and proved that they’re not equinumerous; they can’t be put into one-to-one correspondence. It’s traditional to talk about the uncountability of the real numbers. So Cantor’s big result was that the set of all real numbers is an uncountable set. Maybe if we’re going to talk about countable sets, then I would suggest that we talk about Hilbert’s Hotel, which really makes that idea perfectly clear.

**9:39** · Lex Fridman: Yeah, let’s talk about Hilbert’s Hotel.

**9:41** · Joel David Hamkins: Hilbert’s Hotel is a hotel with infinitely many rooms. Each room is a full floor suite. So there’s floor zero… I always start with zero because for me, the natural numbers start with zero, although that’s maybe a point of contention for some mathematicians. The other mathematicians are wrong.

**9:58** · Lex Fridman: Like I mentioned, I’m a programmer, so starting at zero is a wonderful place to start.

**10:01** · Joel David Hamkins: Exactly. So there’s floor zero, floor one, floor two, or room zero, one, two, three, and so on, just like the natural numbers. So Hilbert’s Hotel has a room for every natural number, and it’s completely full. There’s a person occupying room N for every N. But meanwhile, a new guest comes up to the desk and wants a room. “Can I have a room, please?” And the manager says, “Hang on a second, just give me a moment.” You see, when the other guests had checked in, they had to sign an agreement with the hotel that maybe there would be some changing of the rooms during their stay.

**10:39** · Joel David Hamkins: And so the manager sent a message up to all the current occupants and told every person, “Hey, can you move up one room, please?” So the person in room five would move to room six, and the person in room six would move to room seven and so on. And everyone moved at the same time. Of course, we never want to be placing two different guests in the same room, and we want everyone to have their own private room. But when you move everyone up one room, then the bottom room, room zero, becomes available, of course. So he can put the new guest in that room. So even when you have infinitely many things, then the new guest can be accommodated. And that’s a way of showing how the particular infinity of the occupants of Hilbert’s Hotel, it violates Euclid’s principle.

**11:25** · Joel David Hamkins: It exactly illustrates this idea because adding one more element to a set didn’t make it larger, because we can still have a one-to-one correspondence between the total new guests and the old guests by the room number, right?

**11:40** · Lex Fridman: So to just say one more time, the hotel is full.

**11:45** · Joel David Hamkins: The hotel is full.

**11:46** · Lex Fridman: And then you could still squeeze in one more, and that breaks the traditional notion of mathematics and breaks people’s brains about when they try to think about infinity, I suppose. This is a property of infinity.

**11:59** · Joel David Hamkins: It’s a property of infinity that sometimes when you add an element to a set, it doesn’t get larger. That’s what this example shows. But one can go on with Hilbert’s Hotel, for example. I mean, maybe the next day, 20 people show up all at once. We can easily do the same trick again, just move everybody up 20 rooms. Then we would have 20 empty rooms at the bottom, and those new 20 guests could go in. But on the following weekend, a giant bus pulled up, Hilbert’s bus. And Hilbert’s bus has, of course, infinitely many seats. There’s Seat Zero, Seat One, Seat Two, Seat Three, and so on. So one wants to… You know, all the people on the bus want to check into the hotel, but the hotel is completely full. So what is the manager going to do?

**12:50** · Joel David Hamkins: And when I talk about Hilbert’s Hotel in class, I always demand that the students provide the explanation of how to do it. So maybe I’ll ask you. Can you tell me, yeah, what is your idea about how to fit them all in the hotel, everyone on the bus, and also the current occupants?

**13:08** · Lex Fridman: You separate the hotel into even and odd rooms, and you squeeze in the new Hilbert bus people into the odd rooms, and the previous occupants go into the even rooms.

**13:20** · Joel David Hamkins: That’s exactly right. So, I mean, that’s a very easy way to do it. If you just tell all the current guests to double their room number, so in Room N, you move to Room 2 times N. So they’re all going to get their own private room, the new room, and it will always be an even number because 2 times N is always an even number. And so all the odd rooms become empty that way. And now we can put the bus occupants into the odd-numbered rooms.

**13:42** · Lex Fridman: And by doing so, you have now shoved an infinity into another infinity.

**13:47** · Joel David Hamkins: That’s right. So what it really shows, I mean, another way of thinking about it is that, well, we can define that a set is countable if it is equinumerous with a set of natural numbers. And a kind of easy way to understand what that’s saying in terms of Hilbert’s Hotel is that a set is countable if it fits into Hilbert’s Hotel, because Hilbert’s Hotel basically is the set of natural numbers in terms of the room numbers. So to be equinumerous with a set of natural numbers is just the same thing as to fit into Hilbert’s Hotel. And so what we’ve shown is that if you have two countably infinite sets, then their union is also countably infinite. If you put them together and form a new set with all of the elements of either of them, then that union set is still only countably infinite.

**14:34** · Joel David Hamkins: It didn’t get bigger. And that’s a remarkable property for a- a notion of infinity to have, I suppose. But if you thought that there was only one kind of infinity, then it wouldn’t be surprising at all, because if you take two infinite sets and put them together, then it’s still infinite. And so if there were only one kind of infinity, then it shouldn’t be surprising- … that the union of two countable sets is countable. So there’s another way to push this a bit harder, and that is when when Hilbert’s train arrives, and Hilbert’s train has infinitely many train cars- … and each train car has infinitely many seats.

**15:13** · Joel David Hamkins: And so we have an infinity of infinities of the train passengers together with the current occupants of the hotel, and everybody on the train wants to check in to Hilbert’s Hotel. So the manager can, again, of course, send a message up to all the rooms telling every person to double their room number again. And so that will occupy all the even-numbered rooms again and free up again the odd-numbered rooms. So somehow, we want to put the train passengers into the odd-numbered rooms. And so while every train passenger is on some car, let’s say Car C and Seat S, somehow, we have to take these two coordinates, you know, C, S, the car number and the seat number, and produce from it an odd number in a one-to-one way. And that’s actually not very difficult.

**16:10** · Joel David Hamkins: In fact, one can just use, say… An easy way to do it is to just use the number 3 to the C times 5 to the S. 3 to the C, 3 to the car number, so 3 x 3 x 3, you know, the number of the car. You multiply 3 by itself the number of the train car, and then you multiply 5 by itself the seat number of times, and then you multiply those two numbers together. So 3 to the C times 5 to the S. That’s always an odd number, because the prime factorization has only 3s and 5s in it. There’s no 2 there. So therefore, it’s definitely an odd number, and it’s always different because of the uniqueness of prime factorization. So every number can be factored uniquely into primes. So if you have a number of that form, then you can just factor it, and that tells you the exponent on 3 and the exponent on 5.

**17:06** · Joel David Hamkins: And so you know exactly which person it was, which car they came from, and which seat they came from.

**17:10** · Lex Fridman: And prime factorization is every single number can be decomposed into the atoms of mathematics, which is the prime numbers. You can multiply them together to achieve that number.

**17:23** · Joel David Hamkins: That’s, uh-

**17:23** · Lex Fridman: And that’s prime factorization. You’re showing 3 and 5 are both prime numbers, odd. So through this magical formula, you can deal with this train, an infinite number of cars, with each car having an infinite number of seats.

**17:41** · Joel David Hamkins: Exactly right. We’ve proved that if you have countably many countable sets, then the union of those sets, putting all those sets together into one giant set, is still countable. You know, because the train cars are each countable, plus the current hotel. It’s sort of like another train car, if you want to think about it that way. The current occupants of the hotel could, you know, have the same number as any of the train cars. So putting countably many countable sets together to make one big union set is still countable. It’s quite remarkable, I think. When I first learned this many, many years ago, I was completely shocked by it and transfixed by it.

**18:20** · Joel David Hamkins: It was quite amazing to me that this notion of countable infinity could be closed under this process of infinitely many infinities adding up still to the very same infinity, which is a strong instance, a strong violation of Euclid’s principle once again, right? So, the new set that we built is… has many more elements than the old set in the sense that there’s additional elements, but it doesn’t have many more elements in terms of its size because it’s still just a countable infinity and it fits into Hilbert’s Hotel.

**18:53** · Lex Fridman: Have you been able to sort of internalize a good intuition about countable infinity? ‘Cause that is a pretty weird thing. You can have a countably infinite set of countably infinite sets, and you can shove it all in and it still is a countable infinite set.

**19:11** · Joel David Hamkins: Yeah, that’s exactly right. I mean, I guess, of course when you work with these notions that the argument of Hilbert’s Hotel becomes kind of clear, there are many, many other ways to talk about it too. For example, let’s think about, say, the integer lattice, the grid of points that you get by taking pairs of natural numbers, say, so the upper right quadrant of the integer lattice, yeah? So there’s the, you know, row zero, row one, row two and so on, column zero, column one, column two and so on, and each row and column has a countable infinity of points on it, right? So those dots, if you think about them as dots, are really the same as the train cars if you think about each column in the integer lattice, it’s a countable infinity.

**20:01** · Joel David Hamkins: It’s like one train car and then there’s the next train car next to it, and then the next column next to that, the next train car. And so… But if we think about it in this grid manner, then I can imagine a- a kind of winding path winding through these grid points, like up and down the diagonals- … winding back and forth. So I start at the corner point and then I go down, up and to the left, and then down and to the right, up and to the left, down and to the right, and so on, in such a way that I’m gonna hit every grid point in- on this path. So, this gives me a way of assigning room numbers to the points.

**20:38** · Joel David Hamkins: Because every grid point is going to be the Nth point on that path for some N. And that gives a correspondence between the grid points and the natural numbers themselves. So it’s a kind of different picture. I mean, before we used this 3 to the C, 5 times 5 to the S, which is a kind of, you know, overly arithmetic way to think about it. But there’s a kind of direct, you know, way to understand that it’s still a countable infinity when you have countably many countable sets because you can just start putting them on this list. And as long as you give each of the infinite collections a chance to add one more person to the list, then you’re going to accommodate everyone in any of the sets in one list.

**21:20** · Lex Fridman: Yeah, it’s a really nice visual way to think about it. You just zigzag your way across the grid to make sure everybody’s included, that gives you kind of an algorithm for including everybody. So can you speak to the uncountable infinities?

**21:33** · Joel David Hamkins: Yeah, absolutely.

**21:33** · Lex Fridman: What are the integers and the real numbers-

**21:35** · Joel David Hamkins: Correct

**21:36** · Lex Fridman: … and what is the line that Cantor was able to find?

**21:38** · Joel David Hamkins: Maybe there’s one more step I want to insert before doing that.

**21:43** · Lex Fridman: Right

**21:43** · Joel David Hamkins: which is the rational numbers. So we did pairs of natural numbers. Right? That’s the train car, basically. But maybe it’s a little bit informative to think about the rational, the fractions, the set of fractions, or rational numbers, because a lot of people maybe have an expectation that maybe this is a bigger infinity because the rational numbers are densely ordered; between any two fractions you can find another fraction, right? The average of two fractions is another fraction. And so sometimes people, it seems to be a different character than the integers, which are discretely ordered, right? From any integer, there’s a next one and a previous one and so on, but that’s not true in the rational numbers. And yet, the rational numbers are also still only a countable infinity.

**22:35** · Joel David Hamkins: And the way to see that is actually it’s just exactly the same as Hilbert’s train again, because every fraction consists of two integers, the numerator and the denominator. And so if I tell you two natural numbers, then you know what fraction I’m talking about. I mean, plus the sign issue, I mean if it’s positive or negative. But if you just think about the positive fractions, then you know, you have the numbers of the form P over Q, where Q is not zero. So you can still do 3 to the P times 5 to the Q; the same idea works with the rational numbers. So this is still a countable set. And you might think, well, every set is going to be countable because there’s only one infinity.

**23:21** · Joel David Hamkins: I mean if that’s a kind of perspective maybe that you’re adopting, but it’s not true, and that’s the profound achievement that Cantor made is proving that the set of real numbers is not a countable infinity. It’s a strictly larger infinity, and therefore there’s more than one concept of infinity, more than one size of infinity.

**23:40** · Lex Fridman: So let’s talk about the real numbers. What are the real numbers? Why do they break infinity?

**23:44** · Joel David Hamkins: Right.

**23:44** · Lex Fridman: The countable infinity.

**23:45** · Joel David Hamkins: Right.

**23:46** · Lex Fridman: Looking it up on Perplexity, real numbers include all the numbers that can be represented on the number line, encompassing both rational and irrational numbers. We’ve spoken about the rational numbers, and the rational numbers, by the way, are, by definition, the numbers that can be represented as a fraction of two integers.

**24:05** · Joel David Hamkins: That’s right. So with the real numbers, we have the algebraic numbers. We have of course all the rational numbers. The integers and the rationals are all part of the real number system, but then also we have the algebraic numbers like the square root of 2 or the cube root of 5 and so on. Numbers that solve an algebraic equation over the integers, those are known as algebraic numbers. It was an open question for a long time whether that was all of the real numbers or whether there would exist numbers that are the transcendental numbers. The transcendental numbers are real numbers that are not algebraic.

**24:38** · Lex Fridman: And we won’t even go to the surreal numbers, about which you have a wonderful blog post. We’ll talk about that a little bit later.

**24:43** · Joel David Hamkins: Oh, great. So it was Liouville who first proved that there are transcendental numbers, and he exhibited a very specific number that’s now known as the Liouville constant, which is a transcendental number. Cantor also famously proved that there are many, many transcendental numbers. In fact, it follows from his argument on the uncountability of the real numbers that there are uncountably many transcendental numbers. So most real numbers are transcendental.

**25:12** · Lex Fridman: And again, going to Perplexity, “Transcendental numbers are real or complex numbers; they are not the root of any non-zero polynomial with integer or rational coefficients. This means they cannot be expressed as solutions to algebraic equations with integer coefficients, setting them apart from algebraic numbers.”

**25:29** · Joel David Hamkins: That’s right. So some of the famous transcendental numbers would include the number pi, you know, the 3.14159265 and so on. So that’s a transcendental number. Also, Euler’s constant, the e, like e to the x, the exponential function.

**25:47** · Lex Fridman: So you could say that some of the sexiest numbers in mathematics are all transcendental numbers?

**25:51** · Joel David Hamkins: Absolutely. That’s true. Yeah, yeah. Although, you know, I don’t know, square root of two is pretty.

**25:56** · Lex Fridman: Square root. All right. So it depends. Let’s not. Beauty can be found in-

**26:00** · Joel David Hamkins: That’s right

**26:00** · Lex Fridman: …in all the different kinds of sets, but yeah.

**26:02** · Joel David Hamkins: That’s right. And if you have a kind of simplicity attitude, then, you know, zero and one are looking pretty good too, so… And they’re definitely not.

**26:07** · Lex Fridman: Sorry to take that tangent, but what is your favorite number? Do you have one?

**26:10** · Joel David Hamkins: Oh, gosh. You know-

**26:12** · Lex Fridman: Is it zero?

**26:13** · Joel David Hamkins: Did you know there’s a proof that every number is interesting? You can prove it, because…

**26:22** · Lex Fridman: Yeah? What’s that proof look like?

**26:23** · Joel David Hamkins: Yeah, okay.

**26:23** · Lex Fridman: How do you even begin?

**26:24** · Joel David Hamkins: I’m gonna prove to you-

**26:25** · Lex Fridman: Okay

**26:26** · Joel David Hamkins: … that every natural number is interesting.

**26:28** · Lex Fridman: Okay.

**26:29** · Joel David Hamkins: Yeah. I mean, zero’s interesting because, you know, it’s the additive identity, right? That’s pretty interesting. And one is the multiplicative identity, so when you multiply it by any other number, you just get that number back, right? And two is, you know, the f- the first prime number. That’s super interesting, right? Okay. So… …One can go on this way and give specific reasons, but I want to prove as a general principle that every number is interesting. And this is the proof. Suppose, toward contradiction, that there were some boring numbers. Okay?

**27:03** · Lex Fridman: Okay.

**27:04** · Joel David Hamkins: But if, if there was an uninteresting number- … then there would have to be a smallest uninteresting number. But that’s a contradiction, because the smallest uninteresting number is a super interesting property to have. So therefore-

**27:23** · Lex Fridman: Ah, that’s good

**27:24** · Joel David Hamkins: …there cannot be any boring numbers.

**27:26** · Lex Fridman: I’m going to have to try to find a hole in that proof, because there’s a lot of baked in in the word interesting, but yeah, that’s beautiful.

**27:33** · Joel David Hamkins: Right.

**27:34** · Lex Fridman: That doesn’t say anything about the transcendental numbers, about the real numbers that you just…

**27:38** · Joel David Hamkins: That’s right

**27:38** · Lex Fridman: … proved from just-

**27:39** · Joel David Hamkins: That’s right

**27:39** · Lex Fridman: … four natural numbers.

**27:40** · Joel David Hamkins: Yeah. Okay, so should we get back to Cantor’s argument, or?

**27:42** · Lex Fridman: Sure.

**27:42** · Joel David Hamkins: Okay.

**27:43** · Lex Fridman: You’ve masterfully avoided the question. Well, you basically said, “I love all numbers.”

**27:47** · Joel David Hamkins: Yeah, basically.

**27:48** · Lex Fridman: Is that what you said? Okay. All right.

**27:49** · Joel David Hamkins: That was my intention.

**27:49** · Lex Fridman: Back to Cantor’s argument. Let’s go.

**27:51** · Joel David Hamkins: Okay, so Cantor wants to prove that the infinity of the real numbers is different and strictly larger than the infinity of the natural numbers. So the natural numbers are the numbers that start with zero and add one successively, so zero, one, two, three, and so on. And the real numbers, as we said, are the numbers that come from the number line, including all the integers and the rationals and the algebraic numbers and the transcendental numbers and all of those numbers altogether. Now obviously, since the natural numbers are included in the real numbers, we know that the real numbers are at least as large as the natural numbers. And so the claim that we want to prove is that it’s strictly larger.

**28:36** · Joel David Hamkins: So suppose that it wasn’t strictly larger, then they would have the same size. But to have the same size, remember, means by definition that there’s a one-to-one correspondence between them. So we suppose that the real numbers can be put into one-to-one correspondence with the natural numbers. So therefore, for every natural number N, we have a real number, let’s call it R sub N. R sub N is the Nth real number on the list. Basically, our assumption allows us to think of the real numbers as having been placed on a list, R1, R2, and so on. Okay, and now I’m going to define the number Z, and it’s going to be… The integer part is going to be a zero, and then I’m going to put a decimal place, and then I’m going to start specifying the digits of this number Z, D1, D2, D3, and so on.

**29:28** · Joel David Hamkins: And what I’m going to make sure is that the Nth digit after the decimal point of Z is different from the Nth digit of the Nth number on the list.

**29:40** · Joel David Hamkins: Okay? So, to specify the Nth digit of Z, I go to the Nth number on the list, R sub N, and I look at its Nth digit after the decimal point. And whatever that digit is, I make sure that my digit is different from it. Okay? And then I want to do something a little bit more, and that is I’m going to make it different in a way that I’m never using the digits zero or nine. I’m just always using the other digits and not zero and. It would form a kind of diagonal going down and to the right, and for that reason, this argument is called the diagonal argument because we’re looking at the Nth digit of the nth number, and those exist on a kind of diagonal going down. And we’ve made our number Z so that the Nth digit of Z is different from the Nth digit of the nth number.

**30:58** · Joel David Hamkins: But now it follows that Z is not on the list because Z is different from R1 because, well, the first digit after the decimal point of Z is different from the first digit of R1 after the decimal point. That’s exactly how we built it. And the second digit of Z is different from the second digit of R2 and so on. The Nth digit of Z is different from the Nth digit of R7 for every end. So therefore, Z is not equal to any of these numbers R7. But that’s a contradiction because we had assumed that we had every real number on the list, but yet here is a real number Z that’s not on the list, okay? And so that’s the main contradiction.

**31:43** · Lex Fridman: And so it’s a kind of proof by construction.

**31:45** · Joel David Hamkins: Exactly. So, given a list of numbers, Cantor is proving… It’s interesting that you say that, actually, because there’s a kind of philosophical controversy that occurs in connection with this observation about whether Cantor’s construction is constructive or not. Given a list of numbers, Cantor gives us a specific means of constructing a real number that’s not on the list, is a way of thinking about it. There’s this one aspect, which I alluded to earlier, but some real numbers have more than one decimal representation, and it causes this slight problem in the argument. For example, the number one, you can write it as 1.0000 forever, but you can also write it as 0.999 forever. Those are two different decimal representations of exactly the same number.

**32:38** · Lex Fridman: You beautifully got rid of the zeros and the nines. Therefore, we don’t need to even consider that, and the proof still works.

**32:44** · Joel David Hamkins: Exactly, because the only kind of case where that phenomenon occurs is when the number is eventually zero or eventually nine. Since our number Z never had any zeros or nines in it, it wasn’t one of those numbers. So actually, in those cases, we didn’t need to do anything special to diagonalize. The mere fact that our number has a unique representation already means that it’s not equal to those numbers. So maybe it was controversial in Cantor’s day, more than 100 years ago, but I think it’s most commonly looked at today as, you know, one of the initial main results in set theory, and it’s profound and amazing and insightful and the beginning point of so many later arguments.

**33:24** · Joel David Hamkins: And this diagonalization idea has proved to be an extremely fruitful proof method, and almost every major result in mathematical logic is using in an abstract way the idea of diagonalization. It was really the start of so many other observations that were made, including Russell’s paradox and the halting problem and the recursion theorem. So many other principles are using diagonalization at their core.

**33:56** · Lex Fridman: Can we just step back a little bit?

**33:58** · Joel David Hamkins: Sure.

**33:58** · Lex Fridman: This infinity crisis led to a kind of rebuilding of mathematics. So it’d be nice if you lay out the things it resulted in. One is set theory became the foundation of mathematics. All mathematics could now be built from sets, giving math its first truly rigorous foundation. The axiomatization of mathematics, the paradoxes forced mathematicians to develop ZFC and other axiomatic systems, and mathematical logic emerged. Gödel, Turing, and others created entirely new fields. So, can you explain what set theory is and how does it serve as a foundation of modern mathematics, and maybe even the foundation of truth?

**34:43** · Joel David Hamkins: That’s a great question. Set theory really has two roles that it’s serving. There are two ways that set theory emerges. On the one hand, set theory is its own subject of mathematics, with its own problems and questions and answers and proof methods. So really, from this point of view, set theory is about the transfinite recursive constructions or well-founded definitions and constructions. Those ideas have been enormously fruitful, and set theorists have looked into them and developed so many ideas coming out of that. But set theory has also happened to serve in this other foundational role. It’s very common to hear things said about set theory that really aren’t taking account of this distinction between the two roles that it’s serving.

**35:38** · Joel David Hamkins: It’s its own subject, but it’s also serving as a foundation of mathematics. So in its foundational role, set theory provides a way to think of a collection of things as one thing. That’s the central idea of set theory. A set is a collection of things, but you think of the set itself as one abstract thing. So when you form the set of real numbers, then that is a set. It’s one thing. It’s a set, and it has elements inside of it. So it’s sort of like a bag of objects. A set is kind of like a bag of objects. So we have a lot of different axioms that describe the nature of this idea of thinking of a collection of things as one thing itself, one abstract thing.

**36:20** · Lex Fridman: And axioms are, I guess, facts that we assume are true, based on which we then build the ideas of mathematics. So there’s a bunch of facts, axioms about sets that we can put together, and if they’re sufficiently powerful, we can then build on top of that a lot of really interesting mathematics.

**36:42** · Joel David Hamkins: Yeah, I think that’s right. So, the history of the current set theory axioms, known as the Zermelo-Fraenkel axioms, came out in the early 20th century with Zermelo’s idea. The history is quite fascinating because Zermelo in 1904 offered a proof that what’s called the axiom of choice implies the well-order principle. So he described his proof, and that was extremely controversial at the time. There was no theory, there weren’t any axioms there. Cantor was not working in an axiomatic framework. He didn’t have a list of axioms in the way that we have for set theory now, and Zermelo didn’t either. And his ideas were challenged so much with regard to the well-order theorem—

**37:29** · Joel David Hamkins: that he was pressed to produce the theory in which his argument could be formalized, and that was the origin of what’s known as Zermelo set theory.

**37:39** · Lex Fridman: And going to Perplexity, the axiom of choice is a fundamental principle in set theory which states that for any collection of non-empty sets, it is possible to select exactly one element from each set, even if no explicit rule to make the choices is given. This axiom allows the construction of a new set containing one element from each original set, even in cases where the collection is infinite or where there is no natural way to specify a selection rule. So this was controversial, and this was described before there’s even a language for axiomatic systems.

**38:14** · Joel David Hamkins: That’s right. So on the one hand, the axiom of choice principle is completely obvious that we want this to be true, that it is true. A lot of people take it as a law of logic. If you have a bunch of sets, then there’s a way of picking an element from each of them. There’s a function. If I have a bunch of sets, then there’s a function that when you apply it to any one of those sets, gives you an element of that set. It’s a completely natural principle. It’s called the axiom of choice, which is a way of anthropomorphizing the mathematical idea. It’s not like the function is choosing something. It’s just that if you were to make such choices, there would be a function that consisted of the choices that you made.

**39:01** · Joel David Hamkins: And the difficulty is that when you can’t specify a rule or a procedure by which you’re making choices, then it’s difficult to say what the function is that you’re asserting exists. You want to have the view that, well, there is a way of choosing. I don’t have an easy way to say what the function is, but there definitely is one. This is the way of thinking about the axiom of choice.

**39:28** · Lex Fridman: So we’re going to say the three letters of ZFC may be a lot in this conversation. You already mentioned—

**39:33** · Joel David Hamkins: Right

**39:33** · Lex Fridman: Zermelo-Fraenkel set theory. The Z and the F and the C in that come from this axiom of choice.

**39:41** · Joel David Hamkins: That’s right.

**39:42** · Lex Fridman: So ZFC sounds like a super technical thing, but it is the set of axioms that’s the foundation of modern mathematics.

**39:49** · Joel David Hamkins: Yeah, absolutely. So one should be aware also that there are huge parts of mathematics that pay attention to whether the axiom of choice is being used, and they don’t want to use the axiom of choice, so they work out the consequences that are possible without the axiom of choice or with weakened forms of Zermelo-Fraenkel set theory, and so on. And there’s quite a vibrant amount of work in that area. But going back to the axiom of choice for a bit, it’s maybe interesting to give Russell’s description of how to think about the axiom of choice. So Russell describes this rich person who has an infinite closet.

**40:31** · Joel David Hamkins: In that closet, he has infinitely many pairs of shoes, and he tells his butler, “Please go and give me one shoe from each pair.” And the butler can do this easily because for any pair of shoes, he can just always pick the left shoe. There’s a way of picking that we can describe. We always take the left one or always take the right one, or take the left one if it’s a red shoe and the right one if it’s a brown shoe, you know. We can invent rules that would result in these kinds of choice functions so we can describe explicit choice functions. For those cases, you don’t need the axiom of choice to know that there’s a choice function.

**41:14** · Joel David Hamkins: When you can describe a specific way of choosing, then you don’t need to appeal to the axiom to know that there’s a choice function. But the problematic case occurs when you think about the infinite collection of socks that the person has in their closet. And if we assume that socks are indistinguishable within each pair, you know, they match each other, but they’re indiscernible, then the butler wouldn’t have any kind of rule for which sock in each pair to pick. And so it’s not so clear that he has a way of producing one sock from each pair, right?

**41:56** · Joel David Hamkins: So that’s what’s at stake, is the question of whether you can specify a rule by which the choice function, you know, a rule that it obeys that defines the choice function, or whether there’s sort of this arbitrary choosing aspect to it. That’s when you need the axiom of choice to know that there is such a function. But of course, as a matter of mathematical ontology, we might find attractive the idea that, well, look, I mean, not every way of choosing the socks has to be defined by a rule. Why should everything that exists in mathematical reality follow a rule or a procedure of that sort? If I have the idea that my mathematical ontology is rich with objects, then I think that there are all kinds of functions and ways of choosing.

**42:45** · Joel David Hamkins: Those are all part of the mathematical reality that I want to be talking about, and so I don’t have any problem asserting the axiom of choice. Yes, there is a way of choosing, but I can’t necessarily tell you what it is. But in a mathematical argument, I can assume that I fix the choice function because I know that there is one. So it’s a… The philosophical difference between working when you have the axiom of choice and when you don’t is the question of this constructive nature of the argument. So if you make an argument and you appeal to the axiom of choice, then maybe you’re admitting that the objects that you’re producing in the proof are not going to be constructive. You’re not going to be able to necessarily say specific things about them.

**43:30** · Joel David Hamkins: But if you’re just claiming to make an existence claim, that’s totally fine. Whereas if you have a constructive attitude about the nature of mathematics, and you think that mathematical claims maybe are only warranted when you can provide an explicit procedure for producing the mathematical objects that you’re dealing with, then you’re probably going to want to deny the axiom of choice and maybe much more.

**43:51** · Lex Fridman: Can we maybe speak to the axioms that underlie ZFC? So ZFC, or Zermelo-Fraenkel set theory with the axiom of choice, as we mentioned, is the standard foundation for most modern mathematics. It consists of the following main axioms: axiom of extensionality, axiom of empty set, axiom of pairing, axiom of union, axiom of power set, axiom of infinity, axiom of separation, axiom of replacement, axiom of regularity, and axiom of choice. Some of these are quite basic, but it would be nice to give people a sense…

**44:28** · Joel David Hamkins: Sure

**44:28** · Lex Fridman: of what it means to be an axiom. Like, what kind of basic facts we can lay on the table on which we can build some beautiful mathematics.

**44:37** · Joel David Hamkins: Yeah, so the history of it is really quite fascinating. So, Zermelo introduced most of these axioms, as part of what’s now called Zermelo set theory, to formalize his proof from the axiom of choice to the well-order principle, which was an extremely controversial result. So in 1904, he gave the proof without the theory, and then he was challenged to provide the theory. And so in 1908, he produced the Zermelo set theory and gave the proof that in that theory, you can prove that every set admits a well ordering. And so the axioms on the list, these things like extensionality, express the most fundamental principles of the understanding of sets that he wanted to be talking about. So for example, extensionality says if two sets have the same members, then they’re equal.

**45:26** · Joel David Hamkins: So it’s this idea that the sets consist of the collection of their members, and that’s it. There’s nothing else that’s going on in the set. So it’s just if two sets have the same members, then they are the same set. So it’s maybe the most primitive axiom in some respect.

**45:44** · Lex Fridman: Well, there’s also, just to give a flavor, there exists a set with no elements called the empty set. For any two sets, there’s a set that contains exactly those two sets as elements. For any set, there’s a set that contains exactly the elements of the elements of that set, so the union set. And then there’s the power set. For any set, there’s a set whose elements are exactly the subsets of the original set, the power set. And the axiom of infinity, there exists an infinite set, typically a set that contains the empty set and is closed under the operation of adding one more element. Back to our hotel example.

**46:22** · Joel David Hamkins: That’s right.

**46:23** · Lex Fridman: And there’s more, but it’s kind of fascinating to put yourself in the mindset of people at the beginning of this, of trying to formalize set theory. It’s fascinating that humans can do that.

**46:37** · Joel David Hamkins: I read some historical accounts by historians about that time period, specifically about Zermelo’s axioms and his proof of the well-order theorem. And the historians were saying, never before in the history of mathematics has a mathematical theorem been argued about so publicly and so vociferously as that theorem of Zermelo’s. And it’s fascinating also because the axiom of choice was widely regarded as a kind of, you know, basic principle at first, but then people were very suspicious of the well-order theorem because no one could imagine a well ordering, say, of the real numbers. And so this was a case when Zermelo seemed to be, from principles that seemed quite reasonable, proving this obvious untruth. And so people, mathematicians, were objecting.

**47:30** · Joel David Hamkins: But then Zermelo and others actually looked into the mathematical papers and so on of some of the people who had been objecting so vociferously, and found, in many cases, that they were implicitly using the axiom of choice in their own arguments, even though they would argue publicly against it. Because it’s so natural to use it, because it’s such an obvious principle in a way. I mean, it’s easy to just use it by accident if you’re not critical enough and you don’t even realize that you’re using the axiom of choice. That’s true now, even. People like to pay attention to when the axiom of choice is used or not used in mathematical arguments, up until this day. It used to be more important.

**48:13** · Joel David Hamkins: In the early 20th century it was very important because people didn’t know if it was a consistent theory or not, and there were these antinomies arising, and so there was a worry about consistency of the axioms. But then, of course, eventually, with the result of Gödel and Cohen and so on, this consistency question specifically about the axiom of choice sort of falls away. We know that the axiom of choice itself will never be the source of inconsistency in set theory. If there’s inconsistency with the axiom of choice, then it’s already inconsistent without the axiom of choice. So it’s not the cause of inconsistency. And so in that…

**48:49** · Joel David Hamkins: from that point of view, the need to pay attention to whether you’re using it or not from a consistency point of view is somehow less important. But still, there’s this reason to pay attention to it on the grounds of these constructivist ideas that I had mentioned earlier.

**49:05** · Lex Fridman: And we should say, in set theory, consistency means that it is impossible to derive a contradiction from the axioms of the theory. So it means that there are no contradictions. That’s a…

**49:15** · Joel David Hamkins: That’s right

**49:15** · Lex Fridman: a consistent axiomatic system is that there are no contradictions.

**49:19** · Joel David Hamkins: A consistent theory is one for which you cannot prove a contradiction from that theory.


### Russell’s paradox

**49:23** · Lex Fridman: Maybe a quick pause, a quick break, quick bathroom break. You mentioned to me offline we were talking about Russell’s paradox and that there’s another kind of anthropomorphizable proof of uncountability. I was wondering if you can lay that out.

**49:41** · Joel David Hamkins: Oh yeah, sure. Absolutely.

**49:42** · Lex Fridman: Both Russell’s paradox and the proof.

**49:44** · Joel David Hamkins: Right. So we talked about Cantor’s proof that the real numbers, the set of real numbers is an uncountable infinity, it’s a strictly larger infinity than the natural numbers. But Cantor actually proved a much more general fact, namely that for any set whatsoever, the power set of that set is a strictly larger set. So the power set is the set containing all the subsets of the original set. So if you have a set and you look at the collection of all of its subsets, then Cantor proved that this is a bigger set. They’re not equinumerous. Of course, there’s always at least as many subsets as elements because for any element, you can make the singleton subset that has only that guy as a member, right? So there’s always at least as many subsets as elements.

**50:36** · Joel David Hamkins: But the question is whether it’s strictly more or not. And so Cantor reasoned like this. It’s very simple. It’s a kind of distilling the abstract diagonalization idea without being encumbered by the complexity of the real numbers. So we have a set X and we’re looking at all of its subsets. That’s the power set of X. Suppose that X and the power set of X have the same size, suppose towards contradiction, they have the same size. So that means we can associate to every individual of X a subset. And so now let me define a new set. I mean, another set, I’m going to define it. Let’s call it D. And D is the subset of X that contains all the individuals that are not in their set.

**51:28** · Joel David Hamkins: Every individual was associated with a subset of X, and I’m looking at the individuals that are not in their set. Maybe nobody’s like that. Maybe there’s no element of X that’s like that, or maybe they’re all like that, or maybe some of them are and some of them aren’t. It doesn’t really matter for the argument. I defined a subset D consisting of the individuals that are not in the set that’s attached to them, but that’s a perfectly good subset. And so because of the equinumerosity, it would have to be attached to a particular individual, you know? And- Let’s call that person, it should be a name starting with D, so Diana.

**52:10** · Joel David Hamkins: And now we ask, is Diana an element of D or not? But if Diana is an element of D, then she is in her set. So she shouldn’t be because the set D was the set of individuals that are not in their set. So if Diana is in D, then she shouldn’t be. But if she isn’t in D, then she wouldn’t be in her set. And so she should be in D. That’s a contradiction. So therefore, the number of subsets is always greater than the number of elements for any set. And the anthropomorphizing idea is the following. I’d like to talk about it this way. For any collection of people, you can form more committees from them than there are people, even if you have infinitely many people.

**53:03** · Joel David Hamkins: Suppose you have an infinite set of people, and what’s a committee? Well, a committee is just a list of who’s on the committee basically, the members of the committee. So there’s all the two-person committees and there’s all the one-person committees and there’s the universal, the worst committee, the one that everyone is on. Okay. The best committee is the empty committee. With no members and never meets and so on. Or is the empty committee meeting all the time? I’m not sure.

**53:29** · Lex Fridman: Yeah. That’s… wow, that’s a profound question. And does a committee with just one member meet also?

**53:35** · Joel David Hamkins: Yeah. Maybe it’s always in session. I don’t know. So the claim is that there are more committees than people. Okay. Suppose not. Well, then we could make an association between the people and the committees. So we would have a kind of… every committee could be named after a person in a one-to-one way. And I’m not saying that the person is on the committee that’s named after them or not on it, whatever. Maybe sometimes that happens, sometimes it doesn’t. I don’t know. It doesn’t matter. But let’s form what I call committee D, which consists of all the people that are not on the committee that’s named after them.

**54:16** · Joel David Hamkins: Okay. Maybe that’s everyone, maybe it’s no one, maybe it’s half the people. It doesn’t matter. That’s a committee, it’s a set of people. And so it has to be named after someone. Let’s call that person Daniella. So now we ask, is Daniella on the committee that’s named after her? Well, if she is, then she shouldn’t be because it was the committee of people who aren’t on their own committee. And if she isn’t, then she should be. So again, it’s a contradiction. So when I was teaching at Oxford, one of my students came up with the following different anthropomorphization of Cantor’s argument. Let’s consider all possible fruit salads. We have a given collection of fruits.

**55:07** · Joel David Hamkins: You know, apples and oranges and grapes, whatever. And a fruit salad consists of some collection of those fruits. So there’s the banana, pear, grape salad and so on. There’s a lot of different kinds of salad. Every set of fruits makes a salad, a fruit salad. Okay… And we want to prove that for any collection of fruits, even if there are infinitely many different kinds of fruit, for any collection of fruits, there are more possible fruit salads than there are fruits. So if not, then you can put a one-to-one correspondence between the fruits and the fruit salads, so you could name every fruit salad after a fruit. That fruit might not be in that salad, it doesn’t matter. We’re just… it’s a naming, a one-to-one correspondence.

**55:53** · Joel David Hamkins: And then, of course, we form the diagonal salad, which consists… Of all the fruits that are not in the salad that’s named after them. And that’s a perfectly good salad. It might be a kind of diet salad, if it was the empty salad, or it might be the universal salad…

**56:12** · Joel David Hamkins: which had all fruits in it, if all the fruits were in it. Or it might have just some and not all. So that diagonal salad would have to be named after some fruit. So let’s suppose it’s named after durian, meaning that it was associated with durian in the one-to-one correspondence. And then we ask, well, is durian in the salad that it’s named after? And if it is, then it shouldn’t be. And if it isn’t, then it should be. And so it’s, again, the same contradiction. So all of those arguments are just the same as Cantor’s proof that the power set of any set is bigger than the set.

**56:48** · Joel David Hamkins: And this is exactly the same logic that comes up in Russell’s paradox, because Russell is arguing that the class of all sets can’t be a set because if it were, then we could form the set of all sets that are not elements of themselves. So basically, what Russell is proving is that there are more collections of sets than elements. Because we can form the diagonal class, you know, the class of all sets that are not elements of themselves. If that were a set, then it would be an element of itself if and only if it was not an element of itself. It’s exactly the same logic in all four of those arguments. So there can’t be a class of all sets, because if there were, then there would have to be a class of all sets that aren’t elements of themselves.

**57:40** · Joel David Hamkins: But that set would be an element of itself if and only if it’s not an element of itself, which is a contradiction. So this is the essence of the Russell paradox. I don’t call it the Russell paradox. Actually, when I teach it, I call it Russell’s theorem. There’s no universal set. And it’s not really confusing anymore. At the time, it was very confusing, but now we’ve absorbed this nature of set theory into our fundamental understanding of how sets are, and it’s not confusing anymore. I mean, the history is fascinating though, about the Russell paradox, because before that time, Frege was working on his monumental work undertaking, implementing the philosophy of logicism, which is the attempt to reduce all of mathematics to logic.

**58:30** · Joel David Hamkins: So Frege wanted to give an account of all of mathematics in terms of logical notions, and he was writing this monumental work and had formulated his basic principles. And those principles happened to imply that for any property whatsoever, you could form the set of objects with that property. This is known as the general comprehension principle. And he was appealing to the principles that support that axiom throughout his work. I mean, it was really… It wasn’t just an incidental thing, he was really using this principle.

**59:11** · Joel David Hamkins: And Russell wrote him a letter when he observed the work in progress, that there was this problem, because if you accept the principle that for any property whatsoever you can make a set of objects with that property, then you could form the set of all sets that are not members of themselves. That’s just an instance of the general comprehension principle. And… But the set of all sets that aren’t elements of themselves can’t be a set, because if it were, then it would be an element of itself if and only if it’s not a member of itself, and that’s a contradiction. And so Russell wrote this letter to Frege, and it was just at the moment when Frege was finishing his work. It was already at the publishers and, you know, in press basically. But it’s completely devastating.

**59:58** · Joel David Hamkins: I mean, it must have been such a horrible situation for Frege to be placed in, because he’s finished this monumental work, you know, years of his life dedicated to this, and Russell finds this basically one-line proof of a contradiction in the fundamental principles of the thesis that completely destroys the whole system. And Frege had put in the appendix of his work a response to Russell’s letter in which he explained what happened, and he wrote very gracefully, “Hardly anything more unwelcome can befall a scientific writer than to have one of the foundations of his edifice shaken after the work is finished. This is the position into which I was put by a letter from Mr.

**1:00:46** · Joel David Hamkins: Bertrand Russell as the printing of this volume was nearing completion.” And then he goes on to explain the matter, it concerns his basic law five and so on.

**1:00:54** · Lex Fridman: It’s heartbreaking. I mean, there’s nothing more traumatic to a person who dreams of constructing mathematics all from logic, to get a very clean, simple contradiction. I mean, that’s just…

**1:01:08** · Joel David Hamkins: You devote your life to… This work, and then it’s shown to be contradictory, and that must have been heartbreaking.

**1:01:16** · Lex Fridman: What do you think about the Frege project, the philosophy of logic, the dream of the power of logic… To construct a mathematical universe?

**1:01:24** · Joel David Hamkins: So, of course, the project of logicism did not die with Frege, and it was continued, and, you know, there’s a whole movement, the neologicists and so on, in contemporary times even. But my view of the matter is that really, we should view the main goals of logicism are basically completely fulfilled in the rise of set-theoretic foundationalism. I mean, when you view ZFC as the foundation of mathematics, and in my view, the principles of ZFC are fundamentally logical in character, including the axiom of choice, as I mentioned, as a principle of logic. This is a highly disputed point of view, though, because a lot of people take even the axiom of infinity as mathematical, inherently mathematical and not logical and so on.

**1:02:14** · Joel David Hamkins: But I think if you adopt the view that the principles of ZFC have to do with the principles of abstract, you know, set formation, which is fundamentally logical in character, then it’s complete success for logicism. So the fact that set theory is able to serve as a foundation means that mathematics can be founded on logic.


### Gödel’s incompleteness theorems

**1:02:35** · Lex Fridman: I think this is a good moment to talk about Gödel’s incompleteness theorems. So, can you explain them and what do they teach us about the nature of mathematical truth?

**1:02:47** · Joel David Hamkins: Absolutely. It’s one of the most profound developments in mathematical logic. I mean, the incompleteness theorems are when mathematical logic, in my view, first became sophisticated. It’s a kind of birth of the subject of mathematical logic. But to understand the theorems, you really have to start a little bit earlier with Hilbert’s program because at that time, you know, with the Russell Paradox and so on, there were these various contradictions popping up in various parts of set theory and the Burali-Forti paradox and so on. And Hilbert was famously supportive of set theory.

**1:03:25** · Joel David Hamkins: I mean, there’s this quote of him saying, “No one shall cast us from the paradise that Cantor has created for us.” And what I take him to mean by that is he was so captured by the idea of using set theory as a foundation of mathematics, and it was so powerful and convenient and unifying in a way that was extremely important. And he didn’t want to give that up, despite the danger of these paradoxes, these contradictions, basically, is how some people viewed them. And so, it’s…

**1:03:58** · Lex Fridman: This minefield of paradoxes. Yeah.

**1:04:00** · Joel David Hamkins: Right. A minefield. That’s a really good way of describing the situation. And so Hilbert said, “Well, look, we have to fix this problem, you know. We want to use the set theory foundations, but we want to do it in a way that is trustworthy and reliable. We can’t allow that the foundations of mathematics are in question, you know.” This is a kind of attitude, I think, that underlies Hilbert and the Hilbert program. And so he proposed, “Look, we’re going to have this strong theory, this set theory that we want to be proving our theorems in. But on the one hand, we want it to be as strong as possible.

**1:04:40** · Joel David Hamkins: We would like it to answer all the questions.” There’s another famous quote of Hilbert in his retirement address where he proclaims, “Wir müssen wissen, wir werden wissen,” so, “We must know, we will know,” in which he’s very optimistic about the ability of mathematics to answer all of the questions of mathematics that we have posed. We have all these problems we want to solve, and he is saying, “We’re going to do it. We’re going to solve all these problems.” So we want to propose this strong theory, and one has the sense that he had in mind set theory in which all the questions are going to be answered. Okay?

**1:05:21** · Joel David Hamkins: But secondly, we want to combine that with a very weak arithmetic, purely finitistic theory; we want to prove that the reasoning process of the strong theory is safe. Okay? So in order to make sense of that point of view, you basically have to invent the philosophy of formalism where we can look at what a proof is, what is the nature of mathematical reasoning. And on Hilbert’s way of thinking about this, a proof is basically itself a finitistic kind of object. It’s a sequence of… If you think about the nature of what a proof is, it’s a sequence of assertions which can be viewed as sort of sequences of symbols that conform with certain rules of logical reasoning. And this is a formalist way of understanding the nature of proof.

**1:06:16** · Joel David Hamkins: So we think about a proof in a kind of syntactic, formal way. Even though the contents of those statements might be referring to infinite uncountable objects, the statements themselves are not infinite uncountable objects. The statements themselves are just finite sequences of symbols.

**1:06:33** · Lex Fridman: So when you kind of think of proof as… Maybe it’s fair to say almost, like, outside of math? It’s, like, tools operating on math. And then for Hilbert, he thought proof is inside the axiomatic system. Something like this.

**1:06:45** · Joel David Hamkins: Yeah, that’s helpful.

**1:06:46** · Lex Fridman: That’s wild.

**1:06:48** · Joel David Hamkins: The main thing about formalism is that you think of the process of doing mathematics. You divorce it from the meaning of the mathematical assertions, right? So the meaning of the mathematical assertions that you make in this infinitary theory has to do with these huge uncountable infinities and so on, possibly. And that’s a very sort of uncertain realm, maybe, and the source of the paradoxes and so on in some people’s minds. But the reasoning process itself consists of writing down sequences of symbols on your page and, you know, undertaking an argument with them which is following these finitary rules. And so, if we divorce the meaning of the symbols from just the process of manipulating the symbols, it’s a way of looking at the nature of mathematics as a kind of formal game in which…

**1:07:43** · Joel David Hamkins: the meaning may be totally absent. I don’t think it’s necessarily part of the formalist view that there is no meaning behind, but rather it’s emphasizing that we can divorce the meaning of the sentences from the process of manipulating those sentences. And then Hilbert wanted to prove in this purely finitary theory that if we follow the rules of that game, we’re never going to get a contradiction. So those were the two aims of the Hilbert program: to found the strong infinitary theory, probably set theory, which is going to answer all the questions. And then secondly, prove in the finitary theory that the strong theory is safe. In other words, consistent, yeah?

**1:08:31** · Lex Fridman: What does the word “finitary” in finitary theory mean?

**1:08:34** · Joel David Hamkins: Yeah. Well, this is, of course, philosophically contentious, and people have different ideas about what exactly it should mean. And so there’s hundreds of papers on exactly that question. But I like to take it just kind of informally. I mean, it means that we’re talking about finite sequences of symbols, and we’re going to have a theory, you know, finite strings of symbols. And a finitary theory would be one whose subject matter is about those kinds of things so that we can conceivably argue about the nature of these finite strings.

**1:09:05** · Joel David Hamkins: So a- a proof is just a finite sequence of statements, so that every statement is either one of the axioms or follows by the laws of logic from the earlier statements in some specified manner, like using modus ponens or some other law of logic like that. And such that the last line on the list is, you know, the theorem that you’re proving. So that’s what a proof is in this kind of way of thinking.

**1:09:29** · Joel David Hamkins: To take a specific example, I mean, I always conceive of the, perhaps the most natural finitary theory that one would be called upon to exhibit would be Peano arithmetic, the theory of Peano arithmetic, which is a first order theory of the nature of arithmetic. But okay, so some people say, “Well, Peano arithmetic has these strong first order induction axioms, and there’s much, much weaker versions of arithmetic, like I-sigma-naught or I-sigma-1 and so on, which are even more finitary than Peano arithmetic.” So different philosophical positions take different attitudes about what does it take to be finitary? How finitary do you have to be to be truly finitary?

**1:10:10** · Lex Fridman: So according to Perplexity, Peano arithmetic is a foundational system for formalizing the properties and operations of natural numbers using a set of axioms called the Peano axioms. Peano arithmetic provides a formal language and axioms for arithmetic operations, such as addition and multiplication over the natural numbers. The axioms define the existence of a first natural number, usually zero or one; the concept of successor function, which generates the next natural number; rules for addition and multiplication built from these concepts; the principle of induction allowing proofs around all natural numbers. And it goes on. So it’s a very particular kind of arithmetic that is a finitary.

**1:10:51** · Joel David Hamkins: You know, I view it as finitary, but this is a contentious view. Not everyone agrees with that. That’s what I was trying to hint at.

**1:10:58** · Lex Fridman: Okay. I got it. All right.

**1:10:58** · Joel David Hamkins: Peano arithmetic is one of the hugely successful theories of the natural numbers and elementary number theory. Essentially, all of classical number theory, whatever kind of theorems you want to be proving about the prime numbers or factorization or any kind of finitary reasoning about finite combinatorial objects, all of it can be formalized in Peano arithmetic. That’s the basic situation. Of course, one has to qualify those statements in light of Gödel’s incompleteness theorem, but for the most part, the classical number theoretic analysis of the finite numbers is almost entirely developable inside Peano arithmetic.

**1:11:45** · Joel David Hamkins: So if we go back to the Hilbert program, Hilbert has these two goals: produce a strong theory which is going to answer all the questions, and then prove by purely finitary means that that theory will never lead into contradiction. And one can think about, well, the incompleteness theorem should be viewed as a decisive refutation of the Hilbert program. It defeats both of those goals decisively, completely. But before explaining that, maybe one should think about, you know, what if Hilbert had been right? What would be the nature of mathematics in the world that Hilbert is telling us to search for?

**1:12:24** · Lex Fridman: And if I may, going to Perplexity’s definition of Hilbert’s program, it was David Hilbert’s early 20th-century project to give all of classical mathematics a completely secure finitary foundation. In essence, the goal was to formalize all of mathematics in precise axiomatic systems and then prove using only very elementary finitary reasoning about symbols that these systems are free of contradiction.

**1:12:51** · Joel David Hamkins: Right, exactly right. Let’s imagine what it would be like if he had been right. So we would have this finitary theory, and it would prove that the strong theory was free of contradiction. So we could start enumerating proofs from the strong theory. I mean, right now, we can write a computer program that would systematically generate all possible proofs from a given theory. And so we could have this theorem enumeration machine that just spit out theorems all day long in such a manner that every single theorem would eventually be produced by this device. And so if you had a mathematical question of any kind, you could answer it by just waiting for either the answer to come out yes or the answer to come out no.

**1:13:51** · Joel David Hamkins: So the nature of mathematical investigation in Hilbert’s world is one of just turning the crank of the theorem enumeration machine. Devoid of creative thinking or imagination, it’s just getting the answer by rote procedure. So Hilbert, in effect, is telling us, with his program, that the fundamental nature of mathematics is rote computation. I mean, the way I think about the Hilbert program seems extremely attractive in the historical context of being worried about the antinomies, the inconsistencies, and so how can we kind of block them. And so-

**1:14:31** · Joel David Hamkins: It seems natural, first of all, to have a strong theory that’s going to answer all the questions, because the idea of logical independence and pervasiveness that we now know exists just wasn’t, you know, there was no known… They didn’t know anything like that happening ever. And so it’s natural to think that it wouldn’t happen, and also that they would be able to guard against this inconsistency. So it seems like the goals of the Hilbert program are quite natural in that historical context. But, you know, when you think a little more about what the nature of it would be like, it shows you this kind of rote procedure.

**1:15:09** · Joel David Hamkins: And now you’re saying, well, that doesn’t seem so unlikely maybe, in the light of increasing computer power and so on, it’s actually maybe turning into our everyday experience, where the machines are calculating more and more for us and in a way that could be alarming. Okay, but to talk about the alternative to the Hilbert point of view, I mean, if he’s wrong, then what is the nature of mathematical reality? Well, it would mean that we couldn’t ever maybe, for the first goal, we couldn’t ever write down a theory that answered all the questions. So we would always be in a situation where our best theory, even the infinitary theories, would have questions that they stumble with and are unable to answer. Independence would occur.

**1:16:02** · Joel David Hamkins: But then also, because of the failure of the second goal, we would also have to be constantly worrying about whether our theories were consistent or not, and we wouldn’t have any truly convincing means of saying that they were free from contradiction. And the fact of Gödel’s Incompleteness Theorem shows that that is exactly the nature of mathematical reality, actually. Those are the two incompleteness theorems. So the first incompleteness theorem says you cannot write down a computably axiomatizable theory that answers all the questions. Every such theory will be incomplete, assuming it includes a certain amount of arithmetic. And secondly, no such theory can ever prove its own consistency.

**1:16:47** · Joel David Hamkins: So not only is it the case that the finitary theory can’t prove the consistency of the strong infinitary theory, but even the infinitary theory can’t prove its own consistency, right? That’s the second incompleteness theorem. And so it’s, in that sense, a decisive takedown of the Hilbert program, which is really quite remarkable, the extent to which his theorem just really answered that whole puzzle. It’s quite amazing. There’s another aspect, kind of easy to think about. I mean, if you’re wondering about theories that prove their own consistency, then would you trust a theory that proves of itself that it’s consistent? I mean, that’s like…

**1:17:35** · Joel David Hamkins: It’s like the used car salesman telling you, “Oh, I’m trustworthy.” I mean, it’s not a reason to trust the used car salesman, is it? Just because he says that. So similarly, if you have a theory that proves its own consistency, well, I mean, even an inconsistent theory would prove its own consistency. And so it doesn’t seem to be a logical reason to believe in the consistency, if you have a theory that proves itself consistent.

**1:17:59** · Lex Fridman: Just for clarification, you used the word theory. Is it, in this context, synonymous with axiomatic system?

**1:18:07** · Joel David Hamkins: Right. So in mathematical logic, “theory” is a technical term. And it means any set of sentences in a formal language. And so if you say “axiomatic system,” it’s basically synonymous to my usage with theory. So a theory means, you know, the consequences of a set of axioms or… People are sometimes unclear on whether they just mean the axioms or the consequences of the axioms, but…

**1:18:29** · Lex Fridman: So theory includes both the axioms and the consequences of the axioms, and you use it interchangeably and the context is supposed to help you figure out which of the two you’re talking about? The axioms or the consequences? Or maybe to you, they’re basically the same?

**1:18:44** · Joel David Hamkins: Yeah, well, they’re so closely connected, although, you know, all the features aren’t the same. So if you have a computable list of axioms for a theory, then you can start enumerating the consequences of the axioms, but you won’t be able to computably decide whether a given statement is a consequence or not. You can enumerate the consequences, so you can semi-decide the consequences, but you won’t be able to decide yes or no whether a given statement is a consequence or not. So it’s the distinction between a problem being computably decidable and a problem being computably enumerable, which was made clear following the work of Turing and others that came from that. I mean, it…

**1:19:30** · Joel David Hamkins: So that’s one difference between the list of axioms of the theory and the theory itself. The axioms could be… You can decide, maybe computably, whether something is an axiom or not, but that doesn’t mean that you can decide computably whether or not something is a theorem or not. Usually, you only get to decide the positive instances. If something is a theorem, you will eventually come to recognize that, but if something isn’t a theorem, maybe at no point will you be able to say, “No, that’s not a theorem.”

**1:19:56** · Lex Fridman: And that’s of course connected to the halting problem- … and all of these-… all of these contradictions and paradoxes are all nicely beautifully interconnected.

**1:20:04** · Joel David Hamkins: That’s right. Absolutely.


### Truth vs proof

**1:20:06** · Lex Fridman: So, can we just linger on Gödel’s incompleteness theorem?

**1:20:09** · Joel David Hamkins: Sure.

**1:20:09** · Lex Fridman: You mentioned the two components there. You know, there are so many questions to ask. Like, what is the difference between provability and truth? What is true and what is provable? Maybe that’s a good line to draw.

**1:20:21** · Joel David Hamkins: Yeah, this is a really core distinction that it’s fascinating to me to go back and read even the early 20th-century people before Gödel and Tarski, and they were totally sloppy about this distinction between truth and proof. It wasn’t clear at all until Gödel, basically. Although even as late as Bourbaki has a kind of confusion in this foundational work, so this standard graduate-level textbooks used in France in the presentation of logic, they are conflating truth and proof. To be true for them means to be provable. So in the early days, maybe it wasn’t clear enough that the concept of truth needed a mathematical investigation or analysis. Maybe it was already taken to be fully clear.

**1:21:19** · Joel David Hamkins: But because of the incompleteness theorem, we realized that actually there are quite subtle things happening, right? And so why don’t we talk about this distinction a bit? To me, it’s absolutely core and fundamental to our understanding of mathematical logic now.

**1:21:34** · Joel David Hamkins: …this distinction between truth and proof. So truth is on the semantic side of the syntax-semantics dichotomy. Truth has to do with the nature of reality. I mean, okay, when I talk about reality, I’m not talking about physical reality. I’m talking about mathematical reality. So we have a concept of something being true in a structure, a statement being true in a mathematical structure. Like maybe you have the real field or something, and you want to know, does it satisfy this statement or that statement? Or you have a group of some kind, or maybe you have a graph. This is a particular kind of mathematical structure that has a bunch of vertices and edges, and you want to know, does this graph satisfy that statement?

**1:22:19** · Joel David Hamkins: And Tarski gave this absolutely wonderful account of the nature of truth in what’s now known as the disquotational theory of truth. And what Tarski says is the sentence, quote, “Snow is white,” unquote, is true if and only if snow is white. And what he means by that is… Look, to say truth is a property of an assertion, so we can think of the assertion as it syntactically. So the sentence is true if and only if the content of the sentence is the case, you know? So the sentence, “Snow is white,” you know, in quotations, is true. That just means that snow is white, and that’s why it’s called the disquotational theory because we remove the quotation marks.

**1:23:16** · Joel David Hamkins: …from the assertion, right? And you can use this idea of disquotation to give a formal definition of truth in a mathematical structure of a statement in a formal language. So for example, if I have a formal language that allows me to make atomic statements about the objects and relations of the structure, and I can build up a formal language with, you know, with the logical connectives of and, and or, and implies, and not, and so on, and maybe I have quantifiers, right? Then, for example, to say that the structure satisfies phi and psi, that that single statement, phi and psi, I’m thinking of that as one statement, just means that it satisfies phi and it satisfies psi. And if you notice what happened there, I…

**1:24:06** · Joel David Hamkins: At first, the “and” was part of the sentence inside the sentence, but then in the second part, I was using the word “and” to refer to the conjunction of the two conditions. So…

**1:24:17** · Lex Fridman: Yeah, it has the disquotation.

**1:24:18** · Joel David Hamkins: Yeah, it has the disquotation. And so this idea can be done for all the logical connectors and quantifiers and everything. You’re applying Tarski’s idea of disquotation, and it allows you to define by induction the truth of any assertion in a formal language inside any mathematical structure. And so to say that a sentence is true, first of all, it’s ambiguous unless you tell me which structure you’re talking about it being true in. And so maybe we have in mind the standard model of arithmetic or something with the natural numbers and the arithmetic structure, and I want to know is a given statement true in that structure. Then we have a formal definition of what that means according to the Tarski recursive definition of truth. Okay, that’s truth.

**1:25:04** · Joel David Hamkins: Proof, on the other hand, is, you know, in this Hilbert way of thinking, we can develop proof theory. What is a proof for a mathematician, for a mathematical logician? A proof is a certain sequence or arrangement of sentences in the formal language that accord with the logical rules of a proof system. So there are certain modes of reasoning that are allowed. So if you know A and you know A implies B in the proof, then at a later step you’re allowed to write B as a consequence. So if you know A and you know A implies B, those are both two statements that are known, then you can deduce B as a consequence according to the rule of modus ponens. This is the rule of modus ponens. And, you know, there are a lot of other rules. Some people would call this implication elimination.

**1:25:56** · Joel David Hamkins: There are different kinds of proof systems. There are a lot of different formal proof systems that exist that are studied by the proof theorists, and all of them have the property that they’re sound, which means that if the premises of the argument are all true in a structure and you have a proof to get a conclusion, then the conclusion is also true in that structure. So that’s what it means to be sound. That proofs preserve truth. They’re truth-preserving arguments. Okay? But also the proof systems are also generally complete.

**1:26:35** · Joel David Hamkins: They’re both sound and complete, and complete means that whenever a statement is a consequence, a logical consequence of some other statements, which means that whenever the assumptions are true, then the consequence is also true in the structure. So whenever you have a logical consequence, then there is a proof of it. Okay? And the proof systems generally have both of those properties; they’re sound and complete. There’s a third property, a lot of logicians talk about sound and complete this, sound and complete that. But actually, there’s a hidden third adjective that they should always be talking about in any such case, which is that you should be able to recognize whether or not something is a proof or not.

**1:27:19** · Joel David Hamkins: So there’s a computable aspect to the proof systems. We want to be able to recognize whether something is a proof. It should be computably decidable whether a given sequence of statements is a proof or not. So we don’t want a proof system in which someone claims to have a proof, but we can’t check that fact whether it’s a proof or not. We want to be able to, you know, to correctly adjudicate all claims to having a proof.

**1:27:46** · Lex Fridman: Yeah, a mathematician comes to mind that said he has a proof, but the margins are too small…

**1:27:51** · Joel David Hamkins: That’s right

**1:27:51** · Lex Fridman: … to continue.

**1:27:52** · Joel David Hamkins: Exactly. So…

**1:27:53** · Lex Fridman: So that doesn’t count as a proof.

**1:27:55** · Joel David Hamkins: Yeah. So generally, all the classical proof systems that are used are sound and complete, and also computably decidable in the sense that we can decide whether something is a proof or not.

**1:28:04** · Lex Fridman: So what is, again, the tension between truth and proof? Which is more powerful, and how do the two interplay with the contradictions that we’ve been discussing?

**1:28:15** · Joel David Hamkins: Right. So the incompleteness theorem is the question whether we could, say, write down a theory for arithmetic. Say, for the standard model of arithmetic where we have the natural numbers and plus and times and zero, one, and less than, and so on. In that formal language, we can express an enormous number of statements about the nature not only of arithmetic, but actually by various coding methods, we can express essentially all of finite mathematics in that structure. So the question would be, can we write down a computable list of axioms that will answer all those questions by proof? In other words, we want to have a complete theory, a theory of arithmetic that proves all and only the true statements. That would be the goal. Hilbert would love that.

**1:29:03** · Joel David Hamkins: I mean, that would be supportive of Hilbert’s program to have such a complete theory of arithmetic, and Godel proved that this is impossible. You cannot write down a computable list of axioms that is complete in that sense. There will always be statements… if the theory is consistent, there will always be statements that you cannot prove and you cannot refute. So they are independent of that theory.

**1:29:26** · Lex Fridman: How traumatic is that, that there’s statements that are independent from the theory?

**1:29:30** · Joel David Hamkins: I mean, my view is that, yeah, this isn’t traumatic at all. This is rather completely eye-opening in terms of our understanding of the nature of mathematical reality. I mean, we’re not… we understand this profound fact about our situation with regard to mathematical truth. The incompleteness theorem tells us, look, we just can’t write down a list of axioms that is going to be consistent and it’s going to answer all the questions. It’s impossible. And so I don’t think of it as trauma. I just think, look, this is the nature of mathematical reality, and it’s good that we know it, and so now we need to move on from that and, you know, do what we can in light of that.

**1:30:19** · Lex Fridman: Is it fair to say that in general it means if I give you a statement, you can’t know if your axiomatic system would be able to prove it?

**1:30:31** · Joel David Hamkins: That’s right. In general, you cannot… the provability problem, we can formulate it as a decision problem. Given a theory and given a statement, is that statement a consequence of that theory? Yeah. This is one of the most famous decision problems. In fact, the very first one, because it’s equivalent to the Hilbert-Ackermann Entscheidungsproblem, which is also appearing in the title of Turing’s 1936 paper that was so important for computability theory. So it’s a formulation of the Entscheidungsproblem. Does a given theory have a given statement as a logical consequence?

**1:31:08** · Joel David Hamkins: Which, because of Godel’s completeness theorem, not his incompleteness theorem, but his earlier completeness theorem, Godel had proved that the proof systems that they studied did have this completeness property that I mentioned. So provability is the same as logical consequence, so… and this is an undecidable decision problem. Turing proved, and we now know it’s equivalent to the halting problem.


### The Halting Problem

**1:31:30** · Lex Fridman: Can you describe the halting problem? Because it’s a thing that shows up in a very useful and, again, traumatic way through a lot of computer science, through a lot of mathematics.

**1:31:39** · Joel David Hamkins: Yeah. The halting problem is expressing a fundamental property of computational processes. So given a program, or maybe we think of it as a program together with its input, but let me just call it a program. So given a program, we could run that program, but I want to pose it as a decision problem. Will this program ever complete its task? Will it ever halt? And the halting problem is the question, given a program, will it halt? Yes or no? And of course, for any one instance, the answer’s either yes or no. That’s not what we’re talking about. We’re talking about whether there’s a computable procedure to answer all instances of this question.

**1:32:23** · Joel David Hamkins: So it’s a decision problem given as a scheme of instances for all possible programs that you could ask about. What I want to know is, is there a computable procedure that will answer those questions? And it turns out the answer’s no. The halting problem is computably undecidable. There is no computable procedure that will correctly answer all instances of whether a given program will halt. And of course, we can get half the answers in the sense that you give me a program and you say, “Will this halt?” And I could take that program and I could run it.

**1:32:59** · Joel David Hamkins: And I could keep running it, and maybe in a week, it would halt. And at that time, I could say, “Yes, it halted.” So I can get the yes answers correctly for halting, all the yes answers. But the problem is if it didn’t halt yet, like maybe I waited, you know, a thousand years and it still hasn’t halted, I don’t seem entitled to say, “No, it’s not going to halt” yet, because maybe in a thousand and one years, it’ll halt. And so at no point can I seem to say no. In order to say, “No, it won’t ever halt,” it seems like I would have to really understand how the program worked and what it was doing. So giving the yes answers was sort of trivial. You didn’t have to understand it; you just needed to run it, which is a kind of rote task.

**1:33:48** · Joel David Hamkins: But to give the no answers, you need to have a kind of deep insight into the nature of the program and what it’s doing in such a way that you would understand it and be able to see, “Oh, no, I can see this program is never going to halt.” Because, you know, it’s a much more difficult task to say, “No, it won’t halt,” than it is to say, “Yes, it halted because I ran it and it halted.” And it turns out to be impossible to have a computable procedure that gives the no answers, you know? And the argument is not very difficult. Should we do it?

**1:34:18** · Lex Fridman: Yes, let’s do it.

**1:34:19** · Joel David Hamkins: Okay. Suppose toward contradiction, I mean, all these proofs are by contradiction, and this argument is going to be a diagonal argument in the same style as the Russell argument and the Cantor argument and Godel’s argument that we haven’t talked about yet. So many diagonal arguments come in. So suppose towards contradiction that we had a procedure for determining whether a given program halted on a given input. Now, let me describe. I’m going to use that procedure as a subroutine in the following process. And my process, let’s call it Q, process Q, and it takes as input a program P, okay? And the first thing it does is it asks that subroutine, “Hey, would P halt if I ran it on P itself?” Okay. That’s the diagonal part, because we’re applying P to P, right?

**1:35:14** · Joel David Hamkins: Okay, so I’m describing program Q, and program Q takes as input P, which is itself a program. And the first thing it does is it asks the halting subroutine program, “Would P halt on P?” And if the answer comes back from the subroutine, “Yeah, that would halt,” then what I do in program Q is I immediately jump into an infinite loop. So I don’t halt. If P halts on P, I don’t halt. But if the answer came back, “No, P is never going to halt on P,” then I halt immediately. Okay, and that’s it. I’ve described what Q does.

**1:35:53** · Joel David Hamkins: And the thing about Q is that Q’s behavior on P was the opposite of P’s behavior on P. I mean, that’s how we designed Q specifically so that Q on P had the opposite behavior as P on P. Okay, so now, of course, what do we do? Well, the same thing that Russell did, and so forth, and Cantor, we ask, “Well, what would Q do on Q?” And because of this opposite behavior, Q would halt on Q if and only if Q does not halt on Q, which is a contradiction, because Q has to have the opposite behavior on Q than Q does, but that’s just contradictory.

**1:36:38** · Lex Fridman: What a beautiful proof. Simple.

**1:36:39** · Joel David Hamkins: It’s absolutely beautiful. I agree. It’s following the same logic of Russell and Cantor. I mean, going back to Cantor basically, because Russell is also quoting Cantor in his letter to Frege. Therefore, the conclusion is that the halting problem is not computably decidable. Now we can immediately prove Godel’s theorem using this, actually. It’s an immediate consequence. So why don’t we just do that? I view this as the simplest proof of Godel’s theorem. You don’t need the Godel sentence to prove Godel’s theorem. You can do it with the halting problem. So suppose that we could write down a computable axiomatization of all of the true facts of elementary mathematics, meaning arithmetic and finite combinatorial things such as Turing machine computations and so on.

**1:37:35** · Joel David Hamkins: So in fact, all those finite combinatorial processes are formalizable inside arithmetic with the standard arithmetization coding process. But let me just be a little bit informal and say suppose we could write down a complete theory of elementary finite mathematics. So we have an axiomatization of that theory. Then we could produce all possible theorems from those axioms in the way that I was describing earlier with Hilbert’s program. If we had a complete theory of elementary mathematics, we could construct a theorem enumeration machine that produced all the theorems and only the theorems from that theory. So now, I have this theorem enumeration device on my desk, and I announce that I’m open for business to solve the halting problem.

**1:38:25** · Joel David Hamkins: So you give me a program and input that you want to run that program on, and I’m going to answer the halting problem. The way I’m going to do it is I’m just going to wait for the statement coming out of the theorem enumeration device that asserts either that P does halt on that input, or I wait for the statement that P does not halt on that input. But one of them’s going to happen because it was a complete theory that was enumerating all the true statements of elementary mathematics. So therefore, if I had such a system, I could solve the halting problem, but we already proved that you cannot solve the halting problem, so therefore you cannot have such a complete theory of arithmetic. So that proves Godel’s theorem.

**1:39:05** · Lex Fridman: Maybe to take a little bit of a tangent, can you speak… You’ve written a wonderful book about proofs and the art of mathematics. So what can you say about proving stuff in mathematics? What is the process of proof? What are the tools? What is the art? What is the science of proving things in mathematics?

**1:39:22** · Joel David Hamkins: This is something that I find so wonderful to teach young mathematicians who are learning how to become mathematicians and learning about proof, and I wrote that book when I was teaching such a proof-writing class in New York.

**1:39:37** · Joel David Hamkins: Many universities have such a course, the proof-writing course, which is usually taken by students who have learned some mathematics. Usually, they’ve completed maybe the calculus sequence and are making the kind of transition to higher mathematics, which tends to involve much more proof, and it’s a kind of challenging step for them. So many math departments have this kind of course on proof-writing where the students would get exposed to how to write proofs. I wasn’t happy with most of the other books that exist for those kind of courses, and the reason was that they were so often so dull because they would concentrate on these totally uninteresting parts of what it’s like to write a proof, these kind of mechanistic procedures about how to write a proof.

**1:40:28** · Joel David Hamkins: You know, if you’re going to prove an implication, then you assume the hypothesis and argue for the conclusion, and so on. All of that is true and fine, and that’s good to know, except if that’s all that you’re saying about the nature of proof, then I don’t think you’re really learning very much. So I felt that it was possible to have a much better kind of book, one that was much more interesting and that had interesting theorems in it that still admitted elementary proof. So I wrote this book and tried to fill it with all of the compelling mathematical statements with very elementary proofs that exhibited lots of different proof styles in it. So, I found that the students appreciated it a lot.

**1:41:12** · Lex Fridman: We should say, “We dedicate the book to my students, may all their theorems be true, proved by elegant arguments that flow effortlessly from hypothesis to conclusion while revealing fantastical mathematical beauty.” Is there some interesting proofs that maybe illustrate, for people outside of mathematics or for people who just take math classes…

**1:41:37** · Joel David Hamkins: Right

**1:41:37** · Lex Fridman: …in high school and so on?

**1:41:39** · Joel David Hamkins: Yeah, let’s do a proof. There’s one in the book. We can talk about it. I think it’s a nice problem. It’s in discrete math, yeah, the 5.1, that one, more pointed at than pointing. Okay. So this is the following problem. Suppose you’re gathered with some friends, you know, in a circle, and you can point at each other however you want, or yourself, whatever, it doesn’t matter, and you can point at more than one person, you know, use all your fingers or your feet or whatever you want. So maybe you point at three of your friends or something and they point at two or three of their friends or whatever, and one person is pointing at 10 people and somebody isn’t pointing at anybody maybe, and various people are pointed at also, right?

**1:42:20** · Joel David Hamkins: So the question is, could we arrange a pattern of pointing so that everyone was more pointed at than they are pointing at others? So in other words, maybe there’s seven people pointing at me, but I’m only pointing at five people and maybe there’s, you know, 20 people pointing at you, but you’re only pointing at 15 people or something like that, right? So I want to know. There’s a similar question on Twitter. For a group of people on Twitter, could you arrange that everyone has more followers than following? Yeah, it’s the same question. Mathematically, it’s identical. Although, I don’t know, it’s not identical, because I said you could point at yourself, and I think that’s not… Can you follow yourself?

**1:43:09** · Lex Fridman: No, I don’t think so, no.

**1:43:10** · Joel David Hamkins: I don’t think you can. Okay. So can you arrange it so that everyone is more pointed at than pointing? In my book, I give a couple of different proofs of this. I think I give an induction proof and then there’s another proof. I think there’s three different proofs in there. But why don’t we just talk about my favorite proof? Suppose it were possible to arrange that we’re all more pointed at than pointing, okay? Now what we’re going to do, we’re going to agree, we’re going to give a dollar to everyone that we’re pointing at.

**1:43:40** · Joel David Hamkins: Okay? So what happens? Everybody made money, because I was pointed at by more people than I’m pointing, so I got $10 but I only paid out $7. And similarly, you got paid $20 but you only paid out $15. So if everyone is more pointed at than pointing, then everyone makes money. But it’s obviously impossible for us to make money as a group by just trading money with ourselves. And therefore, it can’t be possible that we’re all more pointed at than pointing. And this proof illustrates something. It’s one of my habits that I suggest in the book: to anthropomorphize your mathematical ideas. So,

**1:44:22** · Joel David Hamkins: you should imagine that the mathematical objects that are playing a role in your question are people, or active, somehow, animals or something that maybe have a will and a goal and so on. This is this process of anthropomorphizing. And it often makes the problems easier to understand, because we all are familiar with the fact that it’s difficult to make money, and the proof is totally convincing because of our knowledge that we can’t make money as a group by trading dollars between us, without any new money coming into the group.

**1:45:01** · Joel David Hamkins: But that by itself is actually a difficult mathematical claim. I mean, if someone had to prove that you can’t make money by trading within a group, you know, it can’t be that everyone in the group makes money just by shifting money around in the group. Maybe you think that’s obvious, and it is obvious if you think about money. But if you had asked the question about mathematical functions of a certain kind and so on, then maybe it wouldn’t be as clear as it is when you’re talking about this money thing, because we can build on our human experience about the difficulty of getting money and other resources. It doesn’t have to be money; it could be candy, whatever. You know, we just know that you can’t easily get more things in that kind just by trading within a group.

**1:45:48** · Lex Fridman: And we should say that sometimes the power of proof is such that the non-obvious can be shown, and then over time that becomes obvious. So, in the context of- money or social systems, there’s a bunch of things that are non-obvious. And the whole point is that proof can guide us to the truth, to the accurate description of reality. We just proved a property of money.

**1:46:14** · Joel David Hamkins: It’s interesting to think about, well, what if there were infinitely many people in your group? Then it’s not true anymore. The theorem fails. In fact, you can arrange that everyone is strictly more pointed than pointing. And also, if everyone has even just one dollar bill-

**1:46:35** · Joel David Hamkins: then you can arrange that afterwards everyone has infinitely many dollar bills. Because in terms of cardinality, that’s the same. It’s just, say, countable infinity in each case. If you had countably many friends and everyone has one dollar bill, then you can arrange a pattern of passing those dollar bills amongst each other so that afterwards everyone has infinitely many dollar bills. What you need is for each person to be attached to, you know, one of the train cars or something. So, think of everyone as coming from Hilbert’s train, but also think of them as fitting into Hilbert’s Hotel. So, just have everyone on the Nth car give all their money to the person who ends up in the Nth room. So, they each give one dollar to that person.

**1:47:16** · Joel David Hamkins: So afterwards, that person has infinitely many dollars, but everyone only paid out one dollar. So it’s a way of making it happen.


### Does infinity exist?

**1:47:23** · Lex Fridman: To what degree, sticking on the topic of infinity, should we think of infinity as something real?

**1:47:33** · Joel David Hamkins: That’s an excellent question. I mean, a huge part of the philosophy of mathematics is about this kind of question, that what is the nature of the existence of mathematical objects, including infinity? But I think asking about infinity specifically isn’t that different than asking about the number five. What is- what does it mean for the number five to exist? What are the numbers really, right?

**1:47:58** · Joel David Hamkins: This, this is maybe one of the fundamental questions of mathematical ontology. I mean, there’s many different positions to take on the question of the nature of the existence of mathematical objects or abstract objects in general. And there’s a certain kind of conversation that sometimes happens when you do that. And it goes something like this: sometimes people find it problematic to talk about the existence of abstract objects such as numbers, and there seems to be a kind of wish that we could give an account of the existence of numbers or other mathematical objects or abstract objects that was more like, you know, the existence of tables and chairs and rocks and so on.

**1:48:42** · Joel David Hamkins: And so there seems to be this desire to reduce mathematical existence to something, you know, that we can experience physically in the real world. But my attitude about this attempt is that it’s very backward, I think, because I don’t think we have such a clear existence of the nature of physical objects, actually. I mean, we all have experience about existing in the physical world, as we must, because we do exist in the physical world, but I don’t know of any satisfactory account of what it means to exist physically.

**1:49:28** · Joel David Hamkins: I mean, if I ask you, say, “Imagine, you know, a certain kind of steam locomotive,” you know, and I describe the engineering of it and the weight of it and the nature of the gear linkages, and, you know, and I show you schematic drawings of the whole design and so on, and, you know, we talk in detail about every single detailed aspect of this steam locomotive. But then suppose after all that conversation, I say, “Okay, now I would like you to tell me what would it mean for it to exist physically, I mean, as opposed to just being an imaginary steam locomotive?” Then what, what could you possibly say about it? I mean, except by saying, “Oh, I just mean that it exists in the physical world.” But what does that mean? That’s the question, right? It’s not an answer to the question.

**1:50:18** · Joel David Hamkins: That is the question. So I don’t think that there’s anything sensible that we can say about the nature of physical existence. It is a profound mystery. In fact, it becomes more and more mysterious the more physics we know. I mean, back in, say, Newtonian physics, one had a picture of the nature of physical objects as, you know, little billiard balls or something, or maybe they’re infinitely divisible or something like that. Okay, but then this picture is upset with the atomic theory of matter. But then that picture’s upset when we realize that the atoms actually can be split and consist of electrons and protons and neutrons and so on.

**1:50:56** · Joel David Hamkins: But then that picture’s upset when we realize that those things themselves are built out of quarks and leptons and so on, and who knows what’s coming. And furthermore, all of those things, the nature of their existence is actually as wave functions in some cloud of probability and so on. And so it just becomes more and more mysterious the more we learn, and not at all clarifying. And so the nature of what it means to say that there’s an apple on my desk, and to give an account of what that physical existence really is at bottom, I think, is totally absent. Whereas we do seem to have a much more satisfactory account of the nature of abstract existence. I mean, I can talk about the nature of the empty set.

**1:51:43** · Joel David Hamkins: You know, this is the predicate which is never true or something like that. I can talk about those kind of logical properties or the singleton of the empty set and so on. I mean, of course, it’s very difficult if you go very far with it, but the point is that it doesn’t get more and more mysterious. The more that you say, it becomes only more and more clear. And so it seems to me that we don’t really have any understanding of what the physical world is as opposed to the abstract world, and it’s the abstract world where existence is much more clear.

**1:52:19** · Lex Fridman: It is very true that we don’t know anything about the soda bottle or the steam locomotive just because we can poke at it. Again, we anthropomorphize, and that actually gets us into trouble sometimes because I’m not feeling the quantum mechanics when I’m touching it.

**1:52:34** · Joel David Hamkins: That’s right.

**1:52:34** · Lex Fridman: And therefore, it’s easy to forget and feel like this is real and mathematical objects are not, but you’re making the opposite argument. When you draw a distinction between numerals and numbers, which numerals are the representation of the number on the page and so on, could you say that a number is real? Do numbers exist?

**1:52:57** · Joel David Hamkins: I happen to think so. I mean, I’m on the side of realism in mathematics, and I think that these abstract objects do have a real existence in a way that we can give an account of, in a way I just tried to describe.

**1:53:10** · Lex Fridman: So, like, you would describe it as the size of a set with four elements in it?

**1:53:14** · Joel David Hamkins: Well, there are different ways to understand the nature of four. I mean, actually, this gets into the question of structuralism, which is maybe a good place to talk about it.

**1:53:24** · Lex Fridman: What is structuralism?

**1:53:25** · Joel David Hamkins: Structuralism is a philosophical position in mathematics, or the philosophy of mathematics, by which one emphasizes that what’s important about mathematical objects is not what they’re made out of or what their substance or essence is, but rather how they function in a mathematical structure. And so, what I call the structuralist attitude in mathematics is that we should only care about our mathematical structures up to isomorphism.

**1:53:53** · Joel David Hamkins: If I have a mathematical structure of a certain kind and I make an exact copy of it using different individuals to form the elements of that structure, then the isomorphic copy is just as good mathematically, and there’s no important mathematical difference that would ever arise from working with this isomorphic copy instead of the original structure. And so, therefore, that’s another way of saying that the substance of individuals in a mathematical structure is irrelevant with regard to any mathematical property of that structure. And so…

**1:54:33** · Joel David Hamkins: So to ask a question like, “What is the number four really?” is an anti-structuralist thing, because if you have a structure, say, the natural numbers, with all the numbers in it, 0, 1, 2, 3, 4, and so on, then I could replace the number four with something else, like, you know, this bottle of water could play the role of the number four in that structure, and it would be isomorphic. And it wouldn’t matter at all for any mathematical purpose to use this alternative mathematical system, you know? That’s to say that we don’t care what the number four is really. That is irrelevant. What…

**1:55:12** · Joel David Hamkins: The only thing that matters is what are the properties of the number four in a given mathematical system, and recognizing that there are other isomorphic copies of that system, and the properties of that other system’s number four are going to be identical to the properties of this system’s number four with regard to any question that’s important about the number four. But those questions won’t be about essence. So in a sense, structuralism is anti-essential in mathematics.

**1:55:42** · Lex Fridman: So is it fair to think of numbers as a kind of pointer to a deep underlying structure?

**1:55:48** · Joel David Hamkins: Yeah, I think so, because I guess part of the point of structuralism is that it doesn’t make sense to consider mathematical objects or individuals in isolation. What’s interesting and important about mathematical objects is how they interact with each other and how they behave in a system, and so maybe one wants to think about the structural role that the objects play in a larger system, a larger structure. There’s a famous question that Frege had asked actually when he was looking into the nature of numbers, because in his logicist program, he was trying to reduce all of mathematics to logic.

**1:56:26** · Joel David Hamkins: And in that process, he was referring to the Cantor-Hume principle that, whenever two sets are equinumerous, then they have the same number of elements, if and only if. And he founded his theory of number on this principle, but he recognized that there was something that dissatisfied him about that situation, which is that the Cantor-Hume principle does not seem to give you criteria for which things are numbers. It only tells you a kind of identity criteria for when are two numbers equal to each other. Well, two numbers are equal just in case the sets of those sizes are equinumerous, so that’s the criteria for number identity. But it is not a criteria for what is a number.

**1:57:12** · Joel David Hamkins: And so this problem has become known as the Julius Caesar problem because Frege said we don’t seem to have any way of telling from the Hume principle whether Julius Caesar is a number or not. So he’s asking about the essence of number and whether… Of course, one has a sense that he picked maybe what he was trying to present as a ridiculous example… …Because maybe you have the idea that, well, obviously Julius Caesar is not a number, and there’s a lot of philosophical writing that seems to take that line also, that obviously the answer is that Julius Caesar is not a number. But the structuralists disagree with that position. The structuralist attitude is, “Look, you give me a number system. If Julius Caesar isn’t a number, then I can just…

**1:58:01** · Joel David Hamkins: Let’s take the number 17 out of that system and plug in Julius Caesar for that role, and now I’ve got a new number system, and now Julius Caesar happens to be the number 17.” And that’s totally fine, you know. So the point of structuralism is that the question of whether Julius Caesar is a number or not is irrelevant to mathematics. It is irrelevant because it is not about structure, it’s about this essence of the mathematical objects. So that’s the structuralist criticism of Frege’s point.

**1:58:35** · Lex Fridman: You’ve kind of made the case that you can say more concrete things about the existence of objects in mathematics than you can in our physical reality, about which to us human brains, things are obvious or not. So what’s more real, the reality we see with our eyes or the reality we can express in mathematical theorems?

**1:58:59** · Joel David Hamkins: I’m not quite sure. I mean… I live entirely in the platonic realm, and I don’t really understand the physical universe at all. So I don’t have strong views.

**1:59:13** · Lex Fridman: Let’s talk about the platonic realm. Is it… Like, because you live there, is it real? Or-

**1:59:19** · Joel David Hamkins: Oh yeah, totally, yeah. This is the realist position in mathematics is that abstract objects have a real existence. And okay, what’s meant by that is that there’s some sense of existence in which those objects can be regarded as real.

**1:59:32** · Lex Fridman: How should we think about that? How should we try to visualize that? What does it mean to live amongst abstract objects? Because life is finite. We’re all afraid of death. We fall in love with other physical manifestations of objects. And you’re telling me that maybe reality actually exists elsewhere, and this is all just a projection…

**1:59:59** · Joel David Hamkins: Well, I mean-

**1:59:59** · Lex Fridman: …from the abstract realm?

**2:00:02** · Joel David Hamkins: Do abstract objects exist in a place and at a time? That’s very debatable, I think.

**2:00:07** · Lex Fridman: Right. And what does place and time mean?

**2:00:08** · Joel David Hamkins: All time, yeah, so…

**2:00:10** · Lex Fridman: So what’s more real: physics or the mathematical Platonic space?

**2:00:16** · Joel David Hamkins: Well, the mathematical Platonic realm is… I’m not sure I would say it’s more real, but I’m saying we understand the reality of it in a much deeper and more— …a more convincing way. I don’t think we understand the nature of physical reality very well at all, and I think most people aren’t even scratching the surface of the question as I intend to be asking it. So, you know, obviously we understand physical reality. I mean, I knock on the table— …and so on, and we know all about what it’s like to, you know, have a birthday party or to drink a martini or whatever. And so we have a deep understanding of existing in the physical world. But maybe understanding is the wrong word. We have an experience of living in the world—

**2:01:01** · Lex Fridman: Yeah, experience.

**2:01:01** · Joel David Hamkins: …and riding bicycles and all those things, but I don’t think we actually have an understanding at all, I mean, very, very little of the nature of physical existence. I think it’s a profound mystery. Whereas I think that we do have something a little better of an understanding of the nature of mathematical existence and abstract existence. So that’s how I would describe the point.

**2:01:26** · Lex Fridman: Somehow it feels like we’re approaching some deep truth from different directions, and we just haven’t traveled as far in the physics world as we have in the mathematical world.

**2:01:41** · Joel David Hamkins: Maybe I could hope that someone will give, you know, the convincing account, but it seems to be a profound mystery to me. I, I can’t even imagine what it would be like to give an account of physical existence.

**2:01:52** · Lex Fridman: Yeah, I wonder, like a thousand years from now as physics progresses- … what this same conversation would look like.

**2:01:59** · Joel David Hamkins: Right. That would be quite interesting.

**2:02:00** · Lex Fridman: Do you think there’s breakthroughs a thousand years from now on the mathematics side? ‘Cause we’ve just discussed, and we’ll return to a lot of turmoil a century ago. Do you think there’s more turmoil to be had?

**2:02:14** · Joel David Hamkins: It’s interesting to me because I have my feet in two worlds: mathematics and philosophy, and to compare the differences between these subjects. One of the big cultural differences is towards the idea of progress in the subject, because mathematics has huge progress. We simply understand the mathematical ideas much, much better, continually improving our understanding, and there’s growth in knowledge. We understand the nature of infinity now better than they did 100 years ago. I mean, definitely better. And they understood it better 100 years ago than they did, you know, for the previous thousands of years, and so on.

**2:02:57** · Joel David Hamkins: So, in almost every part of mathematics, there’s improved understanding of the core issues, so much so that the questions at hand become totally different, and the field sort of moves on to more difficult, interesting questions. Whereas in philosophy, that’s a little bit true that there’s progress. But meanwhile, it’s also true that there are these eternal questions that have been with us for thousands of years, and in fact, so much so that you can find a lot of philosophers arguing the important contribution of philosophy is in asking the questions rather than answering them, because it’s hopeless to answer them. I mean, the nature of these deep philosophical questions is so difficult. Less of a sense of progress is what I’m trying to say.

**2:03:48** · Joel David Hamkins: I don’t see any reason to think that the progress in mathematics, in the growth in our mathematical understanding and knowledge, won’t simply continue. And so, a thousand years from now, maybe the mathematics that they will be doing at that time would probably be completely unrecognizable to me. I maybe wouldn’t even begin to understand what they’re talking about, even without sort of witnessing the intervening developments. So if you bring someone from ancient times to today, they maybe wouldn’t even understand what we’re talking about with some of the questions. But I feel that, you know, if Archimedes came and we were able to communicate, I think I would be able to tell him about some of the things that are going on in mathematics now, and maybe, you know…

**2:04:43** · Joel David Hamkins: Or anyone from that time, I mean. So I think it is possible to have this kind of progress, even when the subject kind of shifts away from the earlier concerns as a result of the progress, basically.


### MathOverflow

**2:04:57** · Lex Fridman: To take a tangent on a tangent, since you mentioned philosophy, maybe potentially more about the questions, and maybe mathematics is about the answers, I have to say you are a legend on MathOverflow, which is like Stack Overflow but for math. You’re ranked number one all time on there with currently over 246,000 reputation points. How do you approach answering difficult questions on there?

**2:05:24** · Joel David Hamkins: Well, MathOverflow has really been one of the great pleasures of my life. I’ve really enjoyed it. And I’ve learned so much from interacting on MathOverflow. I’ve been on there since 2009, which was shortly after it started. I mean, it wasn’t exactly at the start, but a little bit later. And I think it gives you the stats for how many characters I typed, and I don’t know how many million it is, but this enormous amount of time that I’ve spent thinking about those questions, and it has really just been amazing to me.

**2:06:06** · Lex Fridman: How do you find the questions that grab you and how do you go about- … answering them?

**2:06:11** · Joel David Hamkins: So, I’m interested in any question that I find interesting. So… And it’s not all questions. Sometimes certain kinds of questions just don’t appeal to me that much.

**2:06:21** · Lex Fridman: So you go outside of set theory as well?

**2:06:23** · Joel David Hamkins: When I first joined MathOverflow, I was basically one of the few people in logic who was answering. I mean, there were other people who know some logic, particularly from category theory and other parts of mathematics that aren’t in the most traditional parts of logic, but they were answering some of the logic questions. So I really found myself able to make a contribution in those very early days by engaging with the logic-related questions. But there weren’t many logic people asking questions either. But what I found was that there was an enormous amount of interest in topics that were logic-adjacent.

**2:07:04** · Joel David Hamkins: So a question would arise, you know, in group theory, but it had a logic aspect or an analysis or whatever, and there would be some logic angle on it. And what I found was that I was often able to figure out an answer by learning enough about that other subject matter. This is what was so rewarding for me, is because basically I had to learn enough. My main expertise was logic, but someone would ask a question, you know, that was about, say, the axiom of choice in this other subject matter or the continuum hypothesis or something like that in the other subject matter. And I would have to learn enough about that other subject and the context of the question in order to answer, and I was often able to do that. And so I was quite happy to do that.

**2:07:50** · Joel David Hamkins: And also I learned a lot by doing that, because I had to learn about these other problem areas. And so it really allowed me to grow enormously as a mathematician.

**2:08:01** · Lex Fridman: To give some examples of questions you’ve answered: What are some reasonable sounding statements that are independent of ZFC? What are the most misleading alternate definitions in taught mathematics? Is the analysis as taught in universities in fact the analysis of definable numbers? Solutions to the continuum hypothesis? Most unintuitive application of the axiom of choice? Non-trivial theorems with trivial proofs? Reductio ad absurdum or the contrapositive? What is a chess piece mathematically? We should say you worked quite a bit on infinite chess, which we should definitely talk about. It’s awesome. You’ve worked on so many fascinating things. Has philosophy ever clarified mathematics? Why do we have two theorems when one implies the other?


### The Continuum Hypothesis

**2:08:48** · Lex Fridman: And, of course, just as an example, you’ve given a really great, almost historical answer on the topic of the continuum hypothesis. Maybe that’s a good place to go. We’ve touched on it a little bit, but it would be nice to lay out what is the continuum hypothesis that Cantor struggled with. And I would love to also speak to the psychology of his own life story, his own struggle with it. The human side of mathematics is also fascinating. So what is the continuum hypothesis?

**2:09:16** · Joel David Hamkins: The continuum hypothesis is the question that arises so naturally whenever you prove that there’s more than one size of infinity. So Cantor proved that the infinity of the real numbers is strictly larger than the infinity of the natural numbers. But immediately when you prove that, one wants to know, “Well, is there anything in between?” I mean, what could be a more natural question to ask immediately after that? And so Cantor did ask it, and he spent his whole life thinking about this question. The continuum hypothesis is the assertion that there is no infinity in between the natural numbers and the real numbers. And, of course, Cantor knew many sets of real numbers. Everything in between…

**2:10:01** · Joel David Hamkins: I mean, everything that’s in that interval would be equinumerous with some set of real numbers. But we know lots of sets of real numbers. I mean, there are all these various closed sets, Cantor sets, and so on. There’s Vitali set. We have all kinds of sets of real numbers. And so you might think, “Well, if the continuum hypothesis is false, then we’ve probably seen the set already. We just have to prove that it’s strictly in between.” But it turned out that for all the sets that anyone ever could define or pick out or observe, for all the sets of real numbers, it was always the case either that they were countable, in which case they’re equinumerous with the natural numbers or else finite, or they were fully equinumerous with the whole real line.

**2:10:44** · Joel David Hamkins: And so they were never strictly in between. I mean, you’re in this situation and you have hundreds, thousands of sets that are candidates to be in between, but in every single case, you can prove it’s on one side or the other and not strictly in between. And so in every situation where you’re able to figure out whether it’s in between or not, it’s always never strictly in between.

**2:11:09** · Lex Fridman: Now, Cantor was obsessed with this.

**2:11:11** · Joel David Hamkins: I think he was. Yeah, I’m not a historian, so I don’t know the exact history.

**2:11:15** · Lex Fridman: Well, everything I’ve seen, it seems to be the question that broke him, huh? I mean, just struggling with different opinions on the hypothesis within himself and- …desperately chasing, trying to prove it.

**2:11:29** · Joel David Hamkins: So he had a program for proving it, which has been affirmed in a certain respect. Of course, the continuum hypothesis holds for open sets. That’s easy to see. If you have an open interval, then this is fully equinumerous with the whole real line. Any interval is equinumerous with the whole line because all you would need is a function, you know, like the arctangent function or something that maps the whole real line into an interval. And that’s a one-to-one function. So we know the open sets have the property that they’re non-trivial open sets are all fully equinumerous with the whole real line. So never strictly in between. But remarkably, Cantor proved it also for the closed sets, and that is using what’s called the Cantor-Bendixson theorem.

**2:12:15** · Joel David Hamkins: So it’s quite a remarkable result. It’s definitely not obvious. And this theorem actually was the origin of the ordinals. Cantor had to invent the ordinals in order to make sense of his Cantor-Bendixson process.

**2:12:31** · Lex Fridman: Can you define the open and the closed set in this context?

**2:12:34** · Joel David Hamkins: Oh, yeah. Sure. So a set of reals is open if every point that it contains is surrounded by a little interval of points, the whole tiny little interval. But that tiny little interval is already just by itself equinumerous with the whole line. So that’s why that question is sort of easy for open sets. A closed set is a complement of an open set, and there are a lot of closed sets that are really complicated, of varying sizes. So of course, any closed interval is a closed set, but it’s not only those. There are also things like the Cantor set, which you get by omitting middle thirds. Maybe some people have seen this construction. Or you can imagine sort of randomly taking a lot of little tiny open intervals, you know, all over the line and so on.

**2:13:18** · Joel David Hamkins: So that altogether would be an open set, and the complement of it would be a closed set. So you can imagine just kind of tossing down these open intervals, and what’s left over is the closed set. Those sets can be quite complicated, and they can have isolated points, for example, if the two open intervals were just kissing and leaving only the one point between them. But also you could have sequences that are converging to a point that would also be a closed set, or convergent sequences of convergent sequences and so on. That would be a closed set also.

**2:13:50** · Lex Fridman: The Cantor set is constructed by iteratively removing open intervals, middle thirds, like you mentioned, from the interval, and trying to see can we do a thing that- that goes in between?

**2:14:00** · Joel David Hamkins: Right. So the question would be, “Can you produce a set that has an intermediate size-” …an intermediate cardinality, right?” And Cantor proved with the closed set, “No, it’s impossible. Every closed set is either countable or equinumerous with the whole real line.”

**2:14:18** · Joel David Hamkins: And what the Cantor program for solving the continuum hypothesis was, was a sort of working up. So you did it for open sets and for closed sets, and you sort of work up. Maybe he wants to go into what are called the Borel sets, which are sort of combinations of open and closed sets. And there’s a vast hierarchy of Borel complexity. And it turns out that the continuum hypothesis has been proved also for the Borel sets in this hierarchy. And, but then one wants to go beyond. What about more complicated sets? So there’s this hierarchy of complexity for sets of real numbers.

**2:14:53** · Joel David Hamkins: And Cantor’s idea was to sort of work your way up the hierarchy by proving that the continuum hypothesis was more and more true for those more and more complicated sets, based on our understanding of the earlier cases. And that has been carried out to a remarkable degree. It turns out that one needs, one begins to need large cardinal assumptions though in order to get to the higher realms, even at the level of projective hierarchy, which are sets that you can define by using quantifiers over the real numbers themselves. So you get this hierarchy on top of the Borel hierarchy, the hierarchy of projectively definable sets.

**2:15:35** · Joel David Hamkins: And it turns out that if you have enough large cardinals, then the projective sets also are always either countable or equinumerous with the whole real line. And then one can try to go beyond this and so on. So I view all of those results, which came, you know, in the past 50 years, the later ones, as fulfilling this Cantor idea that goes back, you know, 120 years to his idea that we would prove the continuum hypothesis by establishing more and more instances for greater and greater complexity of sets. But of course, even with what we know now, it hasn’t fully succeeded and it can’t because the hierarchy of complexity doesn’t include all sets of real numbers. Some of them are sort of transcending this hierarchy completely in a way.

**2:16:27** · Joel David Hamkins: And so the program can’t ever fully be successful, especially in light of the independence result.

**2:16:34** · Lex Fridman: Yeah. Well, spoiler alert, can you go to the independence result?

**2:16:38** · Joel David Hamkins: Sure.

**2:16:39** · Lex Fridman: So what does that mean? So the continuum hypothesis was shown to be independent from the ZFC axioms of mathematics?

**2:16:46** · Joel David Hamkins: Right. So the ZFC axioms were the axioms that were put forth first by Zermelo in 1908 in regard to his proof of the well-order theorem using the axiom of choice. That wasn’t fully ZFC. At that time, it was just Zermelo theory because he sort of… There was a kind of missing axiom, the replacement axiom and the foundation axiom were added later, and that’s what makes the Zermelo-Fraenkel axiomatization, which became sort of standard. Actually, there’s another aspect, which is Zermelo’s original theory allowed for the existence of ur-elements, or these atoms, mathematical objects that are not sets but out of which we build the set theoretic universe, whereas set theorists today generally don’t use ur-elements at all.

**2:17:34** · Joel David Hamkins: I argue that it’s really the philosophy of structuralism that leads them to omit the ur-elements because it turns out that if you adopt ZFC axioms with ur-elements, ZFCU it’s called, or ZFA, then any structure that exists, any mathematical structure that exists in that set theoretic universe with the atoms is isomorphic to a structure that doesn’t use the atoms at all. And you don’t need the atoms if you’re a structuralist because you only care about the structures up to isomorphism anyway, and the theory is simply more elegant and clear without the atoms. They’re just not needed. And so that’s why today when we talk about set theory, generally we talk about the atom-free version, and ZFC has no ur-elements. Okay. So we formulate the ZFC axioms of set theory.


### Hardest problems in mathematics

**2:18:26** · Joel David Hamkins: These are expressing the main principle ideas that we have about the nature of sets and set existence. And Cantor had asked about the continuum hypothesis in the late 19th century, and it remained open, totally open until 1938.

**2:18:50** · Lex Fridman: We should mention, I apologize, that it was the number one problem in the Hilbert’s 23 set of problems formulated at the beginning of the century.

**2:18:59** · Joel David Hamkins: That’s right.

**2:18:59** · Lex Fridman: Maybe you can comment on why he put that as number one.

**2:19:02** · Joel David Hamkins: So, right. So Hilbert had introduced at his famous address at the turn of the century this list of problems that he thought could guide or were important to consider in the coming century of mathematics. I mean, that’s how people talk about it now, although I’m not sure at all… Of course, I can’t really speak for Hilbert at all, but if you were a very prominent mathematician, I find it a little hard to believe that Hilbert would have conceived of his list in the same way that we now take his lists. I mean, having observed the century unfold, we know that that list of 23 problems did in fact guide whole research programs, and it was extremely important and influential.

**2:19:46** · Joel David Hamkins: But at the time, Hilbert would have no reason to think that that would be true, and he was just giving a lecture and had a list of problems that he thought were very important. And so I would find it more reasonable to think that he was just making a list of problems that he thought were extremely interesting and important and fundamental in a way without the heavy burden of guiding this 20th century research. Although it turns out that, in fact, that’s exactly what they did.

**2:20:18** · Joel David Hamkins: And we already discussed Hilbert’s views on the nature of set theory and the fundamental character, that quote where he said, “No one will cast us from the paradise that Cantor has created for us.” So I think Hilbert was convinced by Cantor on the importance and the fundamental nature of the continuum hypothesis for the foundations of mathematics, which was a critically important development for the unity of mathematics. I mean, before set theory emerged as a foundation of mathematics, there were… you know, there are different subjects in mathematics. There’s algebra and there’s analysis, real analysis, and topology and geometry, and so on. There’s all these disparate subjects with their own separate axioms, right?

**2:21:03** · Joel David Hamkins: And, but sometimes it happens, like when you’re proving, say, the fundamental theorem of algebra, you know, that the complex numbers are an algebraically closed field that you can solve any polynomial equation in. But the proof methods for that theorem come from other parts of mathematics, you know, those topological proofs and so on. And so how does that work? I mean, if you have totally different axiom systems, but you’re using results from one subject in another subject, it’s somehow incoherent unless there’s one underlying subject. So the unity of mathematics was provided by the existence of a mathematical foundation like set theory. And at the time, it was set theory.

**2:21:47** · Joel David Hamkins: And so it’s critically important to be able to have a single theory in which one views all of mathematics as taking place to resolve that kind of transfer and borrowing phenomenon that was definitely happening. So that must have been part of Hilbert’s thinking about why it’s so important to have a uniform foundation, and set theory was playing that role at the time. Now, of course, we have other possible foundations coming from category theory or type theory, and there’s univalent foundations now. So there are competing foundations now. There’s no need to just use one set theoretic foundation.

**2:22:25** · Joel David Hamkins: Although set theory continues to, in my view, have an extremely successful metamathematical analysis as a foundation, I think is much more successful than set theory for any of those other foundations, but it’s much less amenable to things like computer proof and so on, which is part of the motivation to find these alternative foundations. So, yeah, just to talk about Hilbert, I think he was motivated by the need for unifying foundation of mathematics and set theory was playing that role, and the continuum hypothesis is such a core fundamental question to ask, so it seems quite natural that he would put it on the list. There were other logic-related questions, though, like Hilbert’s tenth problem is also related to logic.

**2:23:08** · Joel David Hamkins: This is the question about Diophantine equations, and he asked to provide an algorithm to decide whether a given Diophantine equation has a solution in the integers. So a Diophantine equation is just… I mean, it’s a, maybe a fancy way of talking about something that’s easy to understand, a polynomial equation, except it’s not just one variable, many variables. So you have polynomials in several variables over the integers, and you want to know, can you solve it? So the problem is, as stated by Hilbert, provide an algorithm for answering the question whether a given polynomial equation has a solution in the integers. So he’s sort of presuming that there is an algorithm, but he wants to know what it is. What is the algorithm?

**2:23:55** · Joel David Hamkins: But the problem was solved by proving that there is no algorithm. It’s an undecidable problem, like the halting problem. There is no computable procedure that will correctly decide whether a given polynomial equation has a solution in the integers. So that’s quite a remarkable development, I think. So there were also a few other logic-related questions on the list.

**2:24:20** · Lex Fridman: And so eventually, the continuum hypothesis was shown to be independent from ZFC axioms, as we’ve mentioned. So what… How does that make you feel? What is independence and what does that mean?

**2:24:30** · Joel David Hamkins: But once you tell the story, the historical story-

**2:24:32** · Lex Fridman: Yes

**2:24:32** · Joel David Hamkins: … is really quite dramatic-

**2:24:34** · Lex Fridman: Yeah, that’s great

**2:24:34** · Joel David Hamkins: I think. Because Cantor poses the question in the late 19th century. And then it’s totally open. Hilbert asks about it, you know, at the turn of the 20th century. Nobody has any clue. There’s no answer coming. Until 1938, this is four decades later, right? So a long time, and Godel, Kurt Godel proved half of it. What he proved is that if the axioms of set theory are consistent, then there is a set theoretic world where both the axiom of choice and the continuum hypothesis are true. So what he’s doing is showing, this is called the constructible universe, Godel’s L. So he solved this… this is the same result where he answers the safety question of the axiom of choice, but also for the continuum hypothesis. They’re true in the same set theoretic universe we get.

**2:25:38** · Joel David Hamkins: So if ZF, without the axiom of choice, is consistent, then so is ZFC plus the continuum hypothesis is the result, 1938. It’s such a beautiful argument. It’s just incredible, I think, because he’s building an alternative mathematical reality. That’s the structure of the proof is that, okay, if there’s any mathematical reality, if there’s any set theoretic world, then we’re going to build another one, a separate one, a different one, maybe different. Maybe it’s the same as the original one. It could be. If we started already in the one that he built, then it would be the same. But there’s no reason to assume it was the same.

**2:26:15** · Joel David Hamkins: So he has this kind of model construction method to build this alternative set theoretic reality, the constructible universe, and then he proves that the axiom of choice is true there and also the continuum hypothesis is true there, and it’s just amazing. Really beautiful argument. Okay, so then for the other part of the independence, that’s only half of it, because Godel shows basically that you can’t refute the continuum hypothesis, but that’s not the same thing as proving that it’s true. He showed that if set theory is consistent without the continuing hypothesis, then it’s consistent with the continuing hypothesis. So that’s not the same thing as proving that it’s true. Yeah.

**2:26:59** · Joel David Hamkins: And then it didn’t come until 1963 when Paul Cohen invented the method of forcing and proved that if there’s a model of set theory, then there’s a model of set theory in which the continuum hypothesis is false. So Cohen also is giving us this extremely powerful tool for building alternative mathematical realities, is how I think about it. He’s explained to us how to take any set theoretic world and build another different one in which the continuum hypothesis is false. The forcing extension.

**2:27:37** · Lex Fridman: It’s such a fascinating technique, a tool of forcing. Maybe I’m anthropomorphizing it, but it seems like a way to escape one mathematical universe into another, or to expand it or to alter it. So you travel between mathematical universes. Can you explain the technique of forcing?

**2:27:57** · Joel David Hamkins: Yeah, exactly. It’s all those things. It’s so wonderful. I mean, that’s exactly how I think about it. I mean…


### Mathematical multiverse

**2:28:03** · Lex Fridman: And we should mention, maybe this is a good place to even give a bigger picture. One of your more controversial ideas in mathematics, as laid out in the paper, “The Set-Theoretic Multiverse,” you describe that there may not be one true mathematics, but rather multiple mathematical universes, and forcing is one of the techniques that gets you from one to the other, so… Can you explain the whole shebang? The whole…

**2:28:27** · Joel David Hamkins: Yeah, sure, let’s get into it. So the lesson of Cohen’s result and Gödel’s result and so on, these producing these alternative set theoretic universes. We’ve observed that the continuum hypothesis is independent and the axiom of choice is independent of the other axioms, but it’s not just those two. We have thousands of independence results. Practically every non-trivial statement of infinite combinatorics is independent of ZFC. I mean, this is the fact. It’s not universally true. There are some extremely difficult prominent results where people proved things in ZFC, but for the most part, if you ask a non-trivial question about infinite cardinalities, then it’s very likely to be independent of ZFC.

**2:29:15** · Joel David Hamkins: And we have these thousands of arguments, these forcing arguments that are used to establish that. And so how should we take that? I mean, on the one hand, if you have a theory and it doesn’t answer any of the questions that you’re interested in, okay, so what does that mean? If you’re following what I call the universe view or the monist view, you might naturally say, “Well, look, ZFC is a weak theory, and there’s the true set theoretic reality out there, and we need a better theory because the current theory isn’t answering the questions. Everything’s independent.” And so that seems like a quite reasonable thing to take if you think that there is…

**2:29:59** · Joel David Hamkins: that every set theoretic question has a definite answer, and there’s a unique set theoretic truth or a unique fact of the matter, right? This is the universe view.

**2:30:09** · Lex Fridman: And by the way, to reiterate, independent means it cannot be proved or disproved within this axiomatic system, within this theory.

**2:30:16** · Joel David Hamkins: Right, exactly. So to be independent means you can’t prove it, and also you can’t prove that it’s false. You can’t refute it.

**2:30:22** · Lex Fridman: And you’re saying that’s why the statement is so traumatic or sad, that most of the interesting stuff, as you said, has been shown to be independent. Of ZFC.

**2:30:31** · Joel David Hamkins: But that’s an interesting way to put it, I think, because it reminds me of this… When I was a graduate student in Berkeley, there was another graduate student who was working with a non-logic professor in C*-algebras or something like this. So it’s a part of analysis or functional analysis, and they were looking at a question, and it turned out to be independent of ZFC, right? And the attitude of this other professor was that, “Oh, I guess I asked the wrong question.” But my attitude and the attitude of all the set theorists was when you ask a question that turns out to be independent, then you asked exactly the right question because this is the one… You know, it’s carving nature at its joints.

**2:31:18** · Joel David Hamkins: You’re adjudicating the nature of set theoretic reality by finding these two realms. You find one of these dichotomies. You know, there are the worlds where it’s true and the worlds where it’s false. And so when you ask that question, that’s to be celebrated. It means you asked exactly the right, interesting, fascinating question. So it’s not a kind of bleak thing that you can’t prove it and you can’t refute it, and that’s such a disaster. Rather, it means that you found this cleavage in mathematical reality, and it’s good to know about those when they happen, you know?

**2:31:52** · Lex Fridman: Carving nature at its joints. So what can you do about the things that are shown to be independent from ZFC?

**2:32:00** · Joel David Hamkins: Right. So…

**2:32:00** · Lex Fridman: What are the techniques?

**2:32:01** · Joel David Hamkins: So one thing is that because of the incompleteness theorem, we know that there’s going to be… For any theory that we can write down, there’s going to be true things we can’t prove in it. So those things are going to be independent. And so we’re already aware of the fact that there will always be these independent phenomena for any theory that we write. And furthermore, some of those theories we won’t even be able to prove that they’re consistent, you know, like the consistency of their own theory. So that’s called the consistency-strength hierarchy.

**2:32:37** · Joel David Hamkins: So it’s a direct consequence of Gödel’s second incompleteness theorem that for any theory we can write down, then towering over it is this incredibly tall tower of consistency strength, where the strength in theories aren’t just adding another axiom, but they’re adding another axiom even whose consistency was not provable in the previous layers of the hierarchy. And so how lucky we are to find the large cardinal axioms that instantiate exactly this feature of increasing consistency strength, this unending and extremely tall hierarchy of consistency strength of axioms. And it exactly fulfills the prediction that Gödel’s theorem makes about that kind of thing.

**2:33:28** · Joel David Hamkins: Except, the axioms in the large cardinal hierarchy aren’t, you know, metalogical self-referential statements of the form that sometimes arise in the Gödel analysis, but rather they’re professing existence of big infinities, these large cardinal axioms. And so it’s such a welcome development, and yet it’s also known that the continuum hypothesis is independent of all of the known large cardinal axioms. So none of the large cardinal axioms can settle the continuum hypothesis. So the independence phenomenon is still there for things like the continuum hypothesis and the cardinal combinatorics that I mentioned.

**2:34:17** · Lex Fridman: So you’re building this incredible hierarchy of axiomatic systems that are more powerful than ZFC.

**2:34:24** · Joel David Hamkins: More powerful than ZFC and then more powerful than that, more powerful than that, and so on. It keeps going forever, and it will never be finished.

**2:34:32** · Lex Fridman: And still, to this day, the continuum hypothesis does not…

**2:34:36** · Joel David Hamkins: It’s not settled by any of the large cardinal axioms.

**2:34:39** · Lex Fridman: Wow. Wow. How does that make you feel? Will it ever be settled?

**2:34:47** · Joel David Hamkins: Well, it’s part of my multiverse view, I guess. We started by describing the universe view, which is the view that there are facts about all of these questions, and it will turn out—if you’re a universe view person, which I’m not, but if you are—then you will hold that there is a right answer to the continuum hypothesis question, and there’s a right answer to the large cardinal questions, and so on. And that what we should be aiming to do is figure out this one true set theory. In contrast, I take the developments of set theory over the past half-century or more as evidence that there isn’t such a unique set-theoretic reality.

**2:35:33** · Joel David Hamkins: Rather, what we’ve been doing for decades now is producing more and more alternative set-theoretic universes in which the fundamental truths differ from one to the other. And that is the answer to the continuum hypothesis question: the fact that given any model of set theory, there’s a forcing extension where the continuum hypothesis is true, and another one where it’s false. You can sort of turn it on and off like a light switch. And that’s the fundamental nature of the continuum hypothesis, that you can have it or you can have the negation as you like within a very closely related set-theoretic world. Wherever you happen to be living, there’s a closely related one where CH is true, where the continuum hypothesis is true, and one where it’s false.

**2:36:23** · Joel David Hamkins: And that itself is a kind of answer. It’s not a singularist answer, a universe view answer. It’s a pluralist answer. And this led me to my views on the multiverse view of set theory and pluralist truth, namely the fundamental nature of set-theoretic truth has this plural character in that there isn’t a singular meaning to the fundamental terms, but rather there’s this choice of alternative set-theoretic universes that have different truths.

**2:36:55** · Lex Fridman: So what does the multiverse view of mathematics enable you to do? What does it empower you to do, and what are the limitations? What are the things it breaks about mathematics as a field, as a space of knowledge, and what does it enable?

**2:37:10** · Joel David Hamkins: First of all, I guess one should say that these different philosophical positions that you might take in the philosophy of set theory, like the multiverse view or the universe view, we don’t ever disagree about the mathematics. We’re all agreeing on what the theorems are. It’s a question of philosophical perspective on the underlying meaning or the context, or really what is a philosophy of mathematics for? And I mean, if you look back in history, for example, to the time of calculus with Newton and Leibniz, right?

**2:37:44** · Joel David Hamkins: They famously developed the ideas of calculus using their concepts of infinitesimals, and those foundations were roundly mocked by Bishop Berkeley and so on, who talked about, you know, “What are these same evanescent increments? And shall we not call them the ghosts of departed quantities?” But the foundations really were kind of completely suspect, I think, at the time. And the foundations of infinitesimal calculus really only became rigorous in the 1950s or so with the development of non-standard analysis and Robinson’s work. Okay, so the point I’m trying to make is that, do you need a robust, rigorous foundation of mathematics to make enduring insights in mathematics?

**2:38:34** · Joel David Hamkins: And the answer, regrettably, is apparently not because in calculus, even with that lousy, creaky foundation of infinitesimals not even well understood that Newton and Leibniz had, they proved all the fundamental theorems of calculus and, you know, they had all the main insights in those early days with that extremely bad foundation. And so that shows you something about the relevance of the kind of foundational views on mathematics and how important they are for mathematical developments and progress and insight. I mean, because I view those early mathematical developments in calculus as genuinely mathematical and extremely important and insightful, even though the foundations weren’t any good by contemporary perspectives. Okay. So, rather…

**2:39:32** · Joel David Hamkins: So when it comes to the philosophy of set theory and the dispute between the universe view and pluralism, my view is that the choice of the philosophical perspective doesn’t actually have to do with the mathematical developments directly at all. Rather, it tells us, “Where should set theory go? What kind of set theory should we be looking at? What kind of questions should we be asking?” So if you have a universe mentality, the universe view, then you’re going to be pushed to try to find and articulate the nature of the one true set-theoretic universe. And I think that remark is really well borne out by the developments with Hugh Woodin, who’s one of the most prominent mathematicians and philosophers with the universe view and his theory of ultimate L and so on. And he’s really striving.

**2:40:26** · Lex Fridman: Who was also your advisor.

**2:40:28** · Joel David Hamkins: He was also my supervisor, yeah, my graduate supervisor.

**2:40:30** · Lex Fridman: Which is a personal story as well.

**2:40:32** · Joel David Hamkins: This fundamental dispute, yeah, on this question. But he is a very strong and successful research program, sort of trying to give legs to finding the nature of the one true set-theoretic universe. And it’s driving the questions that he’s asking and the mathematical programs that he’s pursuing. Whereas if you have a pluralist view, as I do, then you’re going to be led and attracted to questions that have to do with the interaction of different set-theoretic universes, or maybe you want to understand the nature of how are the models of set theory related to their forcing extensions and so on. And so this led to things that I call, say, set-theoretic potentialism, where you think about a set-theoretic universe in a potentialist way.

**2:41:21** · Joel David Hamkins: Not in the sense of potential infinity directly, because all of these universes have infinite sets inside them already, but they’re potentialist in the sense that we could have more sets. The universe could be wider and taller and so on, by forcing or by extending upward. And so we want to understand the nature of this realm of set-theoretic universes. And that’s quite some exciting work. And so with Benedikt Loewe and I, we proved some theorems on the modal logic of forcing and set-theoretic potentialism under end extension. I’ve done a bunch of work on this topic. And also I mounted, together with Gunter Fuchs and Jonas Riets, who was one of my own PhD students, the topic of set-theoretic geology, which is studying…

**2:42:11** · Joel David Hamkins: It’s taking the metaphor of forcing. I mean, in forcing, you have the ground model and the forcing extension. And when I was first working with Jonas, he said, “I want to undo forcing. I want to go backward.” And I at first said, “But Jonas, it doesn’t work that way. You start in the model, in the ground model, and you go out, you go to the bigger one. You know, that’s how forcing works.” And he said, “No, no, I want to go backward.” And so he was quite persistent, actually. And so finally, I said, “Okay, let’s do it.” Let’s take it seriously.” And so we sat down and started thinking more precisely and carefully and deeply about the nature of taking a set-theoretic universe and seeing where did it come from by forcing, which was a new way of thinking about forcing at the time.

**2:42:58** · Lex Fridman: Like reverse-engineering the forcing?

**2:43:00** · Joel David Hamkins: Yeah, something like that. Forcing is a way of producing a new universe. And so you could start somewhere and go to that new universe, or you could look where you are and say, “Well, look, I got here by doing that already in the past.”

**2:43:12** · Joel David Hamkins: So we defined models of the bedrock model and ground, sort of undoing the forcing. And really, it was quite fruitful. And I view this as part of the pluralist perspective, except the difference is that set-theoretic geology is amenable to the universe view. So even though the work was inspired by this philosophical view on the multiverse view, nevertheless, the central ideas of geology have now been picked up by the people with the research program in the universe view, because it turns out that set-theoretic geology is helping them or us to discover the nature of the one true universe relates to its mantle. There’s this concept of the set-theoretic mantle that I had introduced in a way that is extremely interesting.

**2:44:01** · Joel David Hamkins: And so it’s historically quite funny, I think, because this research program that grew entirely out of the pluralist point of view ended up being picked up by the universe point of view research program in a way that is quite important.

**2:44:20** · Lex Fridman: Can you prove something in the world that you arrived at through forcing and then take some of that back to the ground model?

**2:44:30** · Joel David Hamkins: Yeah, absolutely. And that’s a really powerful argument method, actually. People often want to do that. Suppose you’re in some set-theoretic context. You know, you could think about it as living in a set-theoretic universe, and you want to prove something in that universe only. But maybe one way to do it is to first construct this forcing extension and then use the features about this forcing extension to realize that certain things must have already been true in the ground model. And then you throw the forcing extensions away and you-

**2:45:01** · Lex Fridman: Oh, cool

**2:45:01** · Joel David Hamkins: Yeah. So this can happen. To pick a more elementary example, if you think about the early days of people reasoning with the complex numbers before they really understood them. So they would have these algebraic equations that they’re trying to solve. They would have the tools and methods of doing it, but then in the course of, you know, they would have to do things to the polynomial and change the factors and so on, and produce other polynomials and solve them and so on. Sometimes, they could produce solutions. In the middle of their construction, they were led to, like, the square root of minus five or something in the construction. And they didn’t have any meaning for that, but they would just do it symbolically, you know.

**2:45:48** · Joel David Hamkins: And eventually, it would turn out, because of the methods that they had, they would combine and they would cancel and so on, and all the complex parts would cancel out and they’d end up with this actual answer, you know, three plus square root of 17 or whatever. And they could check it and it worked. It was a solution of the original equation. And so it must have been bewildering to them because they would start with this question purely in the real numbers, an algebraic question, and they would march on their method and proceed through the land of nonsense, you know, with these square roots of negative numbers and then end up with an answer that was real again that they could verify was correct.

**2:46:29** · Joel David Hamkins: And so I view this kind of forcing argument that I was just describing in a similar way. You start in set theory and you go to this land of nonsense in the forcing extension, this imaginary world. And you argue and you come back. I mean, you make a consequence in the ground model, and it’s such a beautiful way of arguing.


### Surreal numbers

**2:46:47** · Lex Fridman: So speaking of the land of nonsense, I have to ask you about surreal numbers, but first, I need another bathroom break. All right, we’re back, and there’s this aforementioned wonderful blog post on the surreal numbers and that there’s quite a simple surreal number generation process that can basically construct all numbers. So maybe this is a good spot to ask what are surreal numbers and what is the way we can generate all numbers?

**2:47:20** · Joel David Hamkins: So the surreal number system is an amazing, an amazingly beautiful mathematical system that was introduced by John Conway.

**2:47:30** · Lex Fridman: Rest in peace, one of the great mathematicians ever on this earth.

**2:47:33** · Joel David Hamkins: Yes, absolutely. And I really admire his style of mathematical thinking and working in mathematics and the surreal number system is a good instance of this. So the way I think about the surreal numbers system is what it’s doing is providing us a number system that unifies all the other number systems. So it extends the real numbers. Well, not only does it extend the integers, the natural numbers, the rational numbers, and the real numbers, but also the ordinals and the infinitesimals. So they’re all sitting there inside the surreal numbers, and it’s this colossal system of numbers. It’s not a set even. It’s a proper class, it turns out, because it contains all the ordinal numbers.

**2:48:19** · Joel David Hamkins: But it’s generated from nothing by a single rule, and the rule is, so we’re going to generate the numbers in stages, in a transfinite sequence of stages. And at every stage, we take the numbers that we have so far and in all possible ways, we divide them into two sets, a lower set and an upper set, or a left set and a right set. So we divide them into these two sets so that everything in the left set is less than everything in the right set, and then at that moment, we create a new number that fits in the gap between L and R. Okay? That’s it. That’s all we do. So let me say it again.

**2:49:05** · Joel David Hamkins: The rule is we proceed in stages, and at any stage, in all possible ways, we divide the numbers we have into two collections, the left set and the right set, so that everything in the left set is less than everything in the right set. And we create a new number, a new surreal number that will fit in that gap. Okay. So for example, we could start… Well, at the beginning, we don’t have any numbers. We haven’t created anything yet, and so, we could take nothing and we could divide it into two sets, the empty lower set and the empty upper set. I mean, the two empty sets. And everything in the empty set is less than everything in the empty set because that’s a vacuous statement.

**2:49:48** · Joel David Hamkins: So we’re, we satisfy the conditions and we apply the number generation rule, which says we should create a new number. And this is what I call the big bang of numbers, the surreal genesis when the number zero is born. Zero is the firstborn number that is bigger than everything in the empty set and less than everything in the empty set. Okay, but now we have this number zero, and so therefore, we now can define new gaps. Because if we put zero into the left set and have an empty right set, then we should create a new number that’s bigger than zero and less than everything in the empty set, and that number is called the number one.

**2:50:30** · Joel David Hamkins: And similarly, at that same stage, we could have put zero into the right set, and so that would be the firstborn number that’s less than zero, which is called minus one. So now we have three numbers, minus one, zero, and one, and they have four gaps because there could be a number below minus one or between minus one and zero or between zero and one or above one, and so we create those four new numbers. The first number above one is called two. The first number between zero and one is called 1/2, and then on the negative side, we have minus 1/2 and minus two and so on. So now we have, what is that, seven numbers. So there’s eight gaps between them.

**2:51:10** · Joel David Hamkins: So at the next birthday, they call them, the next stage will be born all the numbers between those gaps, and then between those and between those and so on. And as the days progress, we get more and more numbers. But those are just the finite birthdays, because as I said, it’s a transfinite process. So at day omega, that’s the first infinite day, we’re going to create a lot of new surreal numbers. So every real number will be born at that stage, because every real number fills a gap in the previously born rational numbers that we had just talked about. It’s not all the rationals, because actually the rational numbers that are born at the finite stages are just the rationals whose denominator is a power of two, it turns out. Those are called the dyadic rationals.

**2:51:57** · Joel David Hamkins: So the real numbers are all born on day omega, but also some other numbers are born on day omega. Namely, the ordinal omega itself is the firstborn number that’s bigger than all those finite numbers, and minus omega is the firstborn number that’s less than all those finite numbers. But also, we have the number epsilon, which is the firstborn number that’s strictly bigger than zero and strictly less than all the positive rational numbers. So that’s going to be an infinitesimal number in that gap, and so on. On day omega plus one, we get more numbers, and then omega plus two and so on. And the numbers just keep coming forever. So, this is how you build the surreal number system.

**2:52:39** · Joel David Hamkins: And then it turns out you can define the arithmetic operations of addition and multiplication in a natural way that is engaging with this recursive definition. So we have sort of recursive definitions of plus and times for the surreal numbers. And it turns out you can prove that they make the surreal numbers into what’s called an ordered field. So they satisfy the field axioms, which means that you have distributivity and commutativity of addition and multiplication, and also you have reciprocals for every non-zero number. You can divide by the number. So you can add and multiply and divide and subtract. And furthermore, you can take square roots.

**2:53:21** · Joel David Hamkins: And furthermore, every odd degree polynomial has a root, which is true in the real numbers, because if you think about, say, a cubic or a fifth degree polynomial, then you know it’s going to cross the axis, because it has opposite behaviors on the two infinities, because it’s an odd degree polynomial. So on the positive side, it’s going to the positive infinity. On the negative side, it would be going to minus infinity. So it has to cross. So we know in the real numbers, every odd degree polynomial has a root. And that’s also true in the surreal numbers. So that makes it what’s called a real closed field which is a very nice mathematical theory. So it’s really quite interesting how we can find copies of all these other number systems inside the surreal numbers.

**2:54:09** · Lex Fridman: But the surreal numbers are fundamentally discontinuous as you’re worried about. What are the consequences of this?

**2:54:14** · Joel David Hamkins: Right. So the surreal numbers have a property that they form a non-standard model of the real field, which means that they provide a notion of infinitesimality that one can use to develop calculus on the grounds of Robinson’s non-standard theory that I had mentioned earlier. But they don’t have the least upper bound property for subcollections. There’s no set of surreal numbers, no non-trivial set of surreal numbers has at least upper bound, and there are no convergent sequences in the surreal numbers. And so for the sort of ordinary use in calculus based on limits and convergence, that method does not work in the surreal numbers at all. So that’s what I mean when I say the surreal numbers are fundamentally discontinuous. They have a fundamental discontinuity going on.

**2:55:07** · Joel David Hamkins: But you can still do calculus with them, because you have infinitesimals if you use these non-standard methods, the infinitesimal based methods to calculus. And people do that. I once organized a conference in New York, and we had John Conway as a speaker at that conference. And there was a question session, and someone asked him, I mean, it’s a bit of a rude question, I think, but they asked it and the question was, “What is your greatest disappointment in life?” I mean, I would never ask a question like that at a conference in a very public setting.

**2:55:41** · Joel David Hamkins: But Conway was extremely graceful and he answered by saying that, “The surreal numbers…” Not the numbers themselves, but the reception of the surreal numbers, because he had ambition that the surreal numbers would become a fundamental number system used throughout mathematics and science, because it was able to do non-set analysis, it was able to do calculus, it unified the ordinals and so on. And it’s such a unifying, amazing structure, beautiful structure with elegant proofs and sophisticated ideas all around it. And he was disappointed that it never really achieved that unifying status that he had the ambition for. And this, he mentioned as his greatest disappointment.

**2:56:32** · Lex Fridman: Yeah, Donald Knuth tried to celebrate it, but it never quite took hold.

**2:56:36** · Joel David Hamkins: So I don’t want to give the impression, though, that the surreal numbers are not widely studied, because there are thousands of people who are…

**2:56:41** · Lex Fridman: Sure

**2:56:42** · Joel David Hamkins: …studying it. In fact, Philip Ehrlich, who is one of the world experts on the surreal numbers, mentioned to me once that Conway was his own worst enemy with regard to that very issue because in the Conway style, everything is a game. And he treated the surreal numbers as a kind of plaything, a toy, and maybe that makes people not take it seriously. Although my view is that it is extremely serious and useful and profound, and I’ve been writing a whole series of essays on the surreal numbers for my Substack at Infinitely More. And I just find the whole subject so fascinating and beautiful. I mean, it’s true. I’m not applying it in engineering, which maybe was part of this Conway ambition.


### Conway’s Game of Life

**2:57:30** · Lex Fridman: And I just wanted to, before I forget, mention Conway turning everything into a game. It is a fascinating point that I didn’t quite think about, which I think the Game of Life is just an example of exploration of cellular automata. I think cellular automata is one of the most incredible, complicated, fascinating… It feels like an open door into a world we have not quite yet explored. And it’s such a beautiful illustration of that world, the Game of Life, but calling it a game… Maybe life balances it, because that’s your powerful word, but it’s not quite a game. It’s a fascinating invitation to an incredibly complicated and fascinating mathematical world.

**2:58:09** · Lex Fridman: I think every time I see cellular automata and the fact that we don’t quite have mathematical tools to make sense of that world, it fills me with awe. Speaking of a thousand years from now, it feels like that is a world we might make some progress on.

**2:58:23** · Joel David Hamkins: The Game of Life is a sort of playground for computably undecidable questions because, in fact, you can prove that the question of whether a given cell will ever become alive is computably undecidable. In other words…

**2:58:39** · Lex Fridman: Yeah

**2:58:39** · Joel David Hamkins: …given a configuration, and you ask, “Will this particular cell ever, you know, be alive—” …in the evolution?” And you can prove that that question is equivalent to the halting problem. It’s computably undecidable. It’s semi-decidable in the sense that if it will become alive, then you will know it at a finite stage because you could just run the Game of Life algorithm and let it run. And if it ever did come alive, you could say, “Yeah, it was alive.” But if you’ve run it for a thousand years and it hasn’t come alive yet, then you don’t necessarily seem to have any basis for saying, “No, it won’t ever come alive,” if the behavior was very complicated.

**2:59:18** · Joel David Hamkins: Maybe if you have a complete understanding of the evolution of the behavior, then you can say no, but you can prove you won’t always have that understanding— …precisely because the problem is equivalent to the halting problem.

**2:59:28** · Lex Fridman: And nevertheless, when you sit back and look and visualize the thing, some little mini cellular automata civilizations are born and die quickly, and some are very predictable and boring, but some have this rich, incredible complexity. And maybe that speaks to a thing I wanted to ask on the halting problem and decidability. You’ve mentioned this thing where if you understand the program deeply, you might be able to say something. So can we say something interesting about, maybe, how many programs, statistically, we know something about in terms of whether they halt or not? Or what does it mean to understand a program deeply enough—


### Computability theory

**3:00:09** · Joel David Hamkins: Right

**3:00:09** · Lex Fridman: …to be able to make a prediction?

**3:00:11** · Joel David Hamkins: The main lesson of computability theory, in my view, is that it’s never the case that you can have a thorough understanding of the behavior of a program by looking at the program, and that the content of what you learn from a program, I mean, in the most general case, is always obtained just by running it and looking at the behavior. And the proof of that is there’s a theorem called Rice’s Theorem, which makes that idea completely robust. But I want to just take a little detour towards another question riffing on something that you just said. Namely, one can ask the question, what is the behavior of a random program? So you have some formal computing language, you know, and you want to look at the collection of all programs of a certain size.

**3:01:06** · Joel David Hamkins: Maybe there are only finitely many. And can you say something about the behavior of a randomly chosen one, like with a certain likelihood it will have a certain behavior? And the answer turns out to be extremely interesting. Once, years ago, Alexey Myasnikov asked me a question. He had this concept of a decision problem with a black hole, and what that means is it’s a decision problem which is possibly difficult in the worst case, but the difficulty was concentrated in a very tiny region called the black hole. And outside of that black hole, it was very easy.

**3:01:42** · Joel David Hamkins: And so, for example, this kind of problem is a terrible problem to use if you’re basing your encryption scheme. You don’t want to use a black hole problem because if someone can rob the bank 95% of the time, then that’s not what you want, or even any nontrivial percent of the time is too dangerous. So you don’t want to use problems that are almost every case is easily solved as the basis of your encryption. And the question Alexey asked me was, “Does the halting problem have a black hole?”

**3:02:17** · Joel David Hamkins: And so if we take, say, the standard model of Turing machines—it’s one-way infinite tape with zeros and ones on the tape and so on, the head moving back and forth, and it stops when it gets into the halt state—then it turns out we proved that there is a black hole. And what that means is there’s a computer procedure that decides correctly almost every instance of the halting problem. Even though the halting problem is not decidable, we can decide almost every instance. So more precisely, there’s a collection of Turing machine programs such that we can easily decide whether a program’s in that collection or not. And for the programs in the collection, we can decide the halting problem for those programs easily.

**3:03:03** · Joel David Hamkins: And furthermore, almost every program is in the collection in the sense that as the number of states becomes large, the proportion of programs in the collection goes to 100%. So the asymptotic density of the programs is one. And the proof was quite fascinating because it’s one of these situations where the theorem sounds really surprising, I think, to many people when I first tell it, I mean, to computability experts. Then it’s sort of intriguing to think that you can solve almost every instance of a halting problem. But then when they hear the proof, it’s completely a letdown. Unfortunately, nobody likes the theorem after the proof.

**3:03:47** · Joel David Hamkins: And so the proof is so simple, though. If you know how a Turing machine operates, there’s this infinite paper tape on which the machine writes zeros and ones, and the head moves back and forth according to rigid instructions. And the instructions are all of the form: if the machine is in such and such a state and it’s reading such and such a symbol on the tape, then it should write this symbol on the tape, it should change to this new state specified, and it should either move left or right as specified. So a program consists of instructions like that. If you look at a program, one of the states is the halt state, and that’s when the program halts.

**3:04:30** · Joel David Hamkins: But you can calculate how many programs don’t have any instruction that transitions to the halt state. You can easily calculate the proportion. And in the limit, it goes to 1 over E squared, 13 and a half percent. If you calculate the limit, the proportion of programs with end states that don’t ever halt because they don’t have any instruction saying halt— —those programs obviously never halt because they can’t halt. They don’t have any instruction that says halt.

**3:05:04** · Lex Fridman: So 13% of programs, you could say—

**3:05:06** · Joel David Hamkins: 13%, you can say they don’t halt because you just look at them and you can understand them.

**3:05:10** · Lex Fridman: There’s no halt state.

**3:05:11** · Joel David Hamkins: They never change to the halt state, so they can’t halt.

**3:05:13** · Lex Fridman: I mean, that nevertheless is beautiful to know. To show.

**3:05:17** · Joel David Hamkins: So that’s a kind of trivial reason for non-halting. And when I first made that observation, I thought, “Okay, this is the proof strategy.” Because I wanted to say at first the goal was, “Look, that’s a stupid reason for a program not to halt. And I just want to pile up as many stupid reasons as I can think of—” —until it gets more than 50%, and then I can say most.

**3:05:43** · Lex Fridman: That was brilliant.

**3:05:43** · Joel David Hamkins: Yeah, that was my goal.

**3:05:44** · Lex Fridman: I love this.

**3:05:45** · Joel David Hamkins: Yeah, so we thought more about it, though, and we hit the jackpot because we found one gigantic stupid reason that converged to 100%, in the limit. And so, the stupid reason for a program not to halt is that, well, if you think about the behavior: the head is sitting there. It’s on the leftmost cell of the tape at the very beginning. It’s in the start state, and the head is following an instruction. And the instruction says, “When you’re in the start state,” which it is, “and you’re reading something on the tape, then you should write something and you should change to a new state, and you should either move left or right.” But half of them move left. But if you move left and you are already at the end, then the head falls off.

**3:06:32** · Joel David Hamkins: And so the computation stops because the head fell off the tape. That’s a pretty stupid reason. Okay, but that’s half of them already, just like that. And then some of them went right and they changed to a new state. And amongst those, the new state, half of those ones are going left and half are going right from that place. And then most of those are changing to a new state. When there are a lot of states, it’s very likely that the next state that you transition to is new. And so you get this random walk behavior, if you know what that means, where half go left and half go right at each step.

**3:07:04** · Joel David Hamkins: And there’s a theorem due to Pólya, which is called the Pólya recurrence theorem, which says when you have a random walk, a one-dimensional random walk, then it’s very likely to come back to where you started. And when that happens for us, then half of them from that place fall off on the next step. And so you can show, using this kind of analysis, that the probability one behavior of a random Turing machine is that the head falls off the tape before it repeats a state. And that is the stupid proof that shows how to solve the halting problem.

**3:07:40** · Joel David Hamkins: Because when that happens, we can answer the halting problem saying, “No, the computation stopped because the machine crashed, not because it halted, so therefore it doesn’t count as halting on some accounts.” Or, you know, if you want to define that as halting, crashing as halting, then… But in any case, however it is that you set up your formalism, you’re going to be able to answer the question for the behavior of the machine when the head falls off.

**3:08:03** · Lex Fridman: So statistically, in the limit, you solve the halting problem.

**3:08:08** · Joel David Hamkins: Yes, exactly. Computably solve it.

**3:08:11** · Lex Fridman: What do we take from that? Because you didn’t solve the halting problem.

**3:08:15** · Joel David Hamkins: No, it’s impossible to fully solve…

**3:08:17** · Lex Fridman: Right

**3:08:17** · Joel David Hamkins: …the halting problem correctly in all cases.

**3:08:20** · Lex Fridman: That’s pretty cool. That’s kind of… I mean, I don’t know. This is…

**3:08:22** · Joel David Hamkins: It’s a probabilistic way… I mean, it’s probabilistic in the sense that we’re solving almost all instances… …Computably. There are versions of this that are maybe more interesting from the point of view of complexity theory and actually useful. I mean, there’s the whole P-NP problem and so on. And there’s this genre of NP-complete problems, which are problems that are infeasible. They would take exponential time to solve them in the ordinary way. And they’re not known to be polynomial time solvable, although in these cases it’s an open question whether there is a polynomial time algorithm, a feasible algorithm. And for most of the NP-complete problems, you can prove that there’s a polynomial time approximation that solves almost all instances…

**3:09:09** · Joel David Hamkins: …in a feasible amount of time. So like the knapsack problem, you know, packing problems, and so on, other kinds of problems, the satisfaction problem when… Depending on how you set up the formalism, you can prove, and I’ve proven many instances of this, but also I think it’s widespread for almost all the NP-complete problems, the difficult problems, and these are important problems for industrial application when these are problems… …That we actually want to solve. We can have feasible algorithms that solve almost every instance of them.


### P vs NP

**3:09:42** · Lex Fridman: The amount of fields and topics you’ve worked on is truly incredible. I have to ask about P versus NP. This is one of the big open problems in complexity theory. So for people who don’t know, it’s about the relation between computation time and problem complexity. Do you think it will ever be solved? And is there any chance the weird counterintuitive thing might be true, that P equals NP?

**3:10:06** · Joel David Hamkins: Yeah, that’s an interesting question. Sometimes people ask about whether it could be independent, which I think is-

**3:10:11** · Joel David Hamkins: …an interesting question for logicians. And of course, well, one has to say if you’re entertaining the idea of independence, you know, over which theory? Because every statement is going to be independent over an extremely weak theory. So that’s, you know, it doesn’t make sense to say it’s independent all by itself. You’re only independent relative to a theory, right? So the way I think about P-NP is that… I mean, of course it’s a theoretical question about the asymptotic behavior of these problems. I mean, for a problem to be in P means that there is a computable decision procedure that runs in time bounded by some polynomial. But the coefficients on that polynomial could be enormous, and the degree could be incredibly high.

**3:10:59** · Joel David Hamkins: And so for small values of inputs, then it doesn’t make sense to talk about this polynomial time feasibility with respect to, say, the range of problem inputs that we will ever give it in our lifetime or in the span of human civilization or whatever. I mean, because it’s an asymptotic property, it’s really in the limit as the size of the inputs goes to infinity, that’s the only time that polynomial or NP becomes relevant. And so maybe it’s important to keep that in mind when… Sometimes you find kind of overblown remarks made about, you know, if P equals NP, then this will be incredibly important for human civilization because it means that we’ll have feasible algorithms for solving these incredibly important…

**3:11:45** · Joel David Hamkins: …problems in NP. You know, that it would cause immense wealth for human societies and so on because we would be able to solve these otherwise intractable problems, and that would be the basis of new technology and industry and so forth. I mean, people make these kinds of remarks, but…

**3:12:03** · Lex Fridman: Of course.

**3:12:04** · Joel David Hamkins: …you have to temper those remarks by the realization that P and P equal NP or P not equal NP are not about these practical things at all because of the asymptotic nature of the question itself. Okay, that’s on the one hand. But on the second hand, we already have the algorithm, so we could use it already, except it’s a terrible algorithm because it involves this incredible amount of coding and so on.

**3:12:30** · Lex Fridman: And on the third hand, like you said, we already have approximation algorithms that…

**3:12:34** · Joel David Hamkins: Yes.

**3:12:34** · Lex Fridman: …that from a pragmatic perspective, solve all the actual real engineering problems of human civilization.

**3:12:42** · Joel David Hamkins: Like the SAT solvers work amazingly well, you know, in lots and lots of cases, even though we can prove we don’t expect… If P is not equal to NP, then there won’t be a polynomial time SAT solver. But actually, the SAT solver approximations are really quite amazing.


### Greatest mathematicians in history

**3:12:59** · Lex Fridman: Sorry to ask the ridiculous question, but who is the greatest mathematician of all time? Who are the possible candidates? Euler, Gauss, Newton, Ramanujan, Hilbert. We mentioned Gödel, Turing, if you throw him into the bucket.

**3:13:14** · Joel David Hamkins: So this is, I think, an incredibly difficult question to answer. Personally, I don’t really think this way about ranking mathematicians by greatness. Um…

**3:13:28** · Lex Fridman: So you don’t have, like… You know, some people have a Taylor Swift poster in their dorm room. You don’t have it.

**3:13:33** · Joel David Hamkins: I mean, if you forced me to pick someone, it would probably be Archimedes because…

**3:13:37** · Lex Fridman: Archimedes

**3:13:37** · Joel David Hamkins: …he had such incredible achievements in such an early era, which totally transcended the work of the other people in his era. But I also have the view that I want to learn mathematics and gain mathematical insight from whoever can provide it and wherever I can find it. And this isn’t always just coming from the greats. Sometimes the greats are doing things that are just first and not… You know, somebody else could have easily been first. So there’s a kind of luck aspect to it when you go back and look at the achievements. And because of this progress issue in mathematics that we talked about earlier, namely we really do understand things much better now than they used to.

**3:14:22** · Joel David Hamkins: And when you look back at the achievements that had been made, then maybe you can imagine thinking, “Well, somebody else could’ve had that insight also.” And maybe they would have… It’s already a known phenomenon that disparate mathematicians end up proving essentially similar results at approximately the same time. But, okay, the person who did it first is getting the credit and so on.

**3:14:48** · Lex Fridman: What do you make of that? Because I see that sometimes when mathematicians… This also applies in physics and science, where completely separately, discoveries are made…

**3:14:58** · Joel David Hamkins: Right. Yeah.

**3:14:58** · Lex Fridman: …maybe at a very similar time. What does that mean?

**3:15:01** · Joel David Hamkins: It’s relatively common. I mean, I think it’s like certain ideas are in the air and being thought about but not fully articulated, and so this is the nature of growth in knowledge.

**3:15:13** · Lex Fridman: Do you understand where ideas come from?

**3:15:16** · Joel David Hamkins: Not really.

**3:15:17** · Lex Fridman: I mean, what’s your own process when you’re thinking through a problem?

**3:15:22** · Joel David Hamkins: Yeah, that’s another difficult question. I suppose it has to do with… My mathematical style, my style as a mathematician, is that I don’t really like difficult mathematics. What I love is simple, clear, easy-to-understand arguments that prove a surprising result. That’s my favorite situation. And actually, the question of whether it’s a new result or not is somehow less important to me. And so that has to do with this question of the greats and so on, whoever does it first. Because I think, for example, if you prove a new result with a bad argument or a complicated argument, that’s great because you proved something new. But I still want to see the beautiful, simple, because that’s what I can understand.

**3:16:16** · Joel David Hamkins: Also, I’m kind of naturally skeptical about any complicated argument because it might be wrong. And… …If I can’t really understand it fully, like every single step all at once in my head, then I’m just worried maybe it’s wrong. And so these different styles, sometimes mathematicians get involved with these enormous research projects that involve huge numbers of working parts and… …Different technology coming together. I mean, mathematical technology, not physical technology.

**3:16:48** · Lex Fridman: And sometimes it actually involves now more and more something like the Lean programming language where some parts are automated, so you have this gigantic…

**3:16:54** · Joel David Hamkins: Yeah, yeah, I see. Well, that’s another issue because maybe those things are less subject to skepticism when it’s validated…

**3:17:02** · Lex Fridman: Sure

**3:17:02** · Joel David Hamkins: …by Lean. But I’m thinking about the case where the arguments are just extremely complicated, and so I sort of worry whether it’s right or not, whereas you know, I like the simple thing. So I tend to have often worked on things that are a little bit off the beaten path from what other people are working on from that point of view.

**3:17:23** · Lex Fridman: Your curiosity draws you towards simplicity.

**3:17:25** · Joel David Hamkins: Yeah. I want to work on the things that I can understand and that are simple. Luckily, I’ve found that I’ve been able to make contributions that other people seem to like, in this way, in this style. So I’ve been fortunate from that point of view. My process always, though, and I’ve recommended this always to my students, is just a kind of playful curiosity. So whenever I have…

**3:17:55** · Joel David Hamkins: Whenever there’s an idea or a topic then I just play around with it and change little things or understand a basic case and then make it more complicated or press things a little bit on this side or apply the idea to my favorite example that’s relevant, and see what happens, or you just play around with ideas, and this often leads to insights that then lead to more methods or more, then pretty soon you’re making progress on the problem. So this is basically my method, is I just fool around with the ideas until I can see a path through towards something interesting… …And then prove that, and that’s worked extremely well for me. So I’m pretty pleased with that method.

**3:18:47** · Lex Fridman: You do like thought experiments where you anthropomorphize like you mentioned?

**3:18:51** · Joel David Hamkins: Yeah, yeah. So this is a basic tool. I mean, I use this all the time. You imagine a set-theoretic model, a model of ZFC, as like a place where you’re living, and you might travel to distant lands by forcing. This is a kind of metaphor for what’s going on. Of course, the actual arguments aren’t anything like that because there’s not land and you’re not traveling and you’re not…

**3:19:13** · Lex Fridman: But you allow your mind to visualize that kind of thing-

**3:19:15** · Joel David Hamkins: Yeah

**3:19:15** · Lex Fridman: … in the natural real world.

**3:19:16** · Joel David Hamkins: And it helps you to understand. Particularly when there are parts of the argument that are in tension with one another, then you can imagine that people are fighting or something. And those kinds of metaphors, or you imagine it in terms of a game theoretic, you know, two players trying to win. So that’s kind of tension. And those kinds of metaphorical ways of understanding a mathematical problem often are extremely helpful in realizing, aha, the enemy is going to pick this thing to be like that because, you know, it makes it more continuous or whatever, and then we should do this other thing in order to… So it makes you realize mathematical strategies for finding the answer and proving the theorem that you want to prove because of the ideas that come out of that anthropomorphization.

**3:20:01** · Lex Fridman: What do you think of somebody like Andrew Wiles, who spent seven years grinding at one of the hardest problems in the history of mathematics? And maybe contrasting that a little bit with somebody who’s also brilliant, Terence Tao, who basically says if he hits a wall, he just switches to a different problem and he comes back and so on. So it’s less of a focused grind for many years without any guarantee that you’ll get there, which is what Andrew Wiles went through.

**3:20:30** · Joel David Hamkins: Right.

**3:20:30** · Lex Fridman: Maybe Grigori Perelman did the same.

**3:20:32** · Joel David Hamkins: I mean, Wiles proved an amazing theorem, Fermat’s Last Theorem result is incredible. This is a totally different style than my own practice, though, of working in isolation. For me, mathematics is often a kind of social activity. I have… I counted, I mean, it’s pushing towards a hundred collaborators, co-authors on various papers and so on. And, you know, if anybody has an idea they want to talk about with me, if I’m interested in it, then I’m going to want to collaborate with them and we might solve the problem and have a joint paper or whatever. You want to have a joint paper? Let me-

**3:21:06** · Lex Fridman: Yeah, exactly. Let’s go.

**3:21:08** · Joel David Hamkins: So my approach to making mathematical progress tends to involve working with other people quite a lot rather than just working on my…

**3:21:17** · Joel David Hamkins: …own, and I enjoy that aspect very much. So I, personally, I couldn’t ever do what Wiles did. Maybe I’m missing out. Maybe if I locked myself, you know, in the bedroom and just worked on whatever, then I would solve it. But I tend to think that no, actually, being on MathOverflow so much and I’ve gotten so many ideas, so many papers have grown out of the MathOverflow conversations and back and forth. Someone posts a question and I post an answer on part of it, and then someone else has an idea and it turns into a full solution, and then we have a three-way paper coming out of that. That’s happened many times. And so for me, I enjoy this kind of social aspect to it. And it’s not just the social part.

**3:22:01** · Joel David Hamkins: Rather, that’s the nature of mathematical investigation as I see it, is putting forth mathematical ideas to other people and they respond to it in a way that helps me learn, helps them learn, and I think that’s a very productive way of undertaking mathematics.

**3:22:20** · Lex Fridman: I think it’s when you work solo on mathematics, from my outsider perspective, it seems terrifyingly lonely. And because you’re, especially if you do stick to a single problem, especially if that problem has broken many brilliant mathematicians in the past, that you’re really putting all your chips in. And just the torment… …The rollercoaster of day to day. Because I imagine you have these moments of hopeful break, mini breakthroughs, and then you have to deal with the occasional realization that, no, it was not a breakthrough, and that disappointment.

**3:23:00** · Lex Fridman: And then you have to go, like, a weekly, maybe daily disappointment where you hit a wall, and you have no other person to brainstorm with. You have no other avenue to pursue. And it’s, I don’t know, the mental fortitude it takes to go through that. But everybody’s different. Some people are recluse and just really find solace in that lone grind. I have to ask about Grisha Grigori Perelman. What do you think of him famously declining the Fields Medal and the Millennial Prize? So he stated, “I’m not interested in money or fame. The prize is completely irrelevant to me. If the proof is correct, then no other recognition is needed.” What do you think of him turning down the prize?

**3:23:52** · Joel David Hamkins: I guess what I think is that mathematics is full of a lot of different kinds of people. And my attitude is that, hey, it doesn’t matter. Maybe they have a good math idea, and so I want to talk to them and interact with them. And so I think the Perelman case is maybe an instance where, you know, he’s such a brilliant mind and he solved this extremely famous and difficult problem, and that is a huge achievement. But he also had these views about, you know, prizes and somehow, I don’t really fully understand why he would turn it down.

**3:24:33** · Lex Fridman: I do think I have a similar thing, just observing Olympic athletes that are, in many cases, don’t get paid very much, and they nevertheless dedicate their entire lives for the pursuit… … Of the gold medal. I think his case is a reminder that some of the greatest mathematicians, some of the greatest scientists and human beings do the thing they do, take on these problems for the love of it, not for the prizes or the money or any of that. Now, as you’re saying, if the money comes, you could use it for stuff. If the prizes come, and the fame, and so on, that might be useful. But the reason fundamentally the greats do it is because of the art itself.

**3:25:13** · Joel David Hamkins: Sure, I totally agree with that. I mean, I share the view. That’s, you know, that’s why I’m a mathematician is because I find the questions so compelling and I’ve spent my whole life thinking about these problems. But, you know, but like if I won an award…

**3:25:32** · Lex Fridman: Yeah, it’s great. It’s great. I mean, I’m pretty sure you don’t contribute to MathOverflow for the wealth and the power. That you gain. I mean, it’s, yeah, genuine curiosity.

**3:25:46** · Joel David Hamkins: Well, you asked who the greatest mathematician is, and of course if we want to be truly objective about it, we would need a kind of an objective criteria…

**3:25:55** · Lex Fridman: Criteria, yeah.

**3:25:55** · Joel David Hamkins: …about how to evaluate the relative, you know, strength and the reputation of various mathematicians. And so, of course, we should use MathOverflow score… …Because…

**3:26:06** · Lex Fridman: That you’re definitively… I mean, nobody’s objectively the greatest mathematician of all time.

**3:26:10** · Joel David Hamkins: Yes, that’s true. I’ve also argued that tenure and promotion decisions should be based…

**3:26:15** · Lex Fridman: Based on MathOverflow.

**3:26:16** · Joel David Hamkins: …Yeah. So my daughter introduced me to her boyfriend. …And told me that she had a boyfriend. And I, um…

**3:26:25** · Lex Fridman: Asked him what his MathOverflow…

**3:26:26** · Joel David Hamkins: I wanted to know, first of all, what is his chess rating, and secondly, what is his MathOverflow score?


### Infinite chess

**3:26:34** · Lex Fridman: Oh, man. Well, that’s the only way to judge a person, I think. That’s, I think, objectively correct. Yeah. I mean, since you bring up chess, I’ve got to ask you about infinite chess. I can’t let you go. You’ve, I mean, you’ve worked on a million things, but infinite chess is one of them. Somebody asked on MathOverflow for the mathematical definition of chess.

**3:26:54** · Joel David Hamkins: Right.

**3:26:54** · Lex Fridman: So can we talk about the math of chess and the math of infinite chess? What is infinite chess?

**3:26:59** · Joel David Hamkins: Oh, yeah, absolutely. Infinite chess is fantastic. Chess ordinarily is played on this tiny, tiny board. It’s an eight by eight board, right? So when you play chess, normally it’s on the eight by eight board. But we want to play infinite chess, so on the integer board. It’s infinite in all four directions, you know, but it still has the chessboard pattern, and maybe there are pieces on this board, maybe infinitely many pieces we allow. But one difference from finite ordinary chess, in infinite chess, we don’t play from a standard starting position. Rather, you…

**3:27:36** · Joel David Hamkins: The interesting situation is that you present a position where there’s a lot of pieces already on the board in a complicated way, and you say, “What would it be like to start from this position or from that one?” You know, and we want to produce positions that have interesting features, meaning mathematically interesting features. And so I can tell you for example… probably a lot of people are familiar with, say, the mate in two genre of chess problem. You know, you have a chess problem and it’s white to mate in two, which means that white is going to make two moves, but the second move is going to be a checkmate.

**3:28:15** · Joel David Hamkins: Or maybe mate in three or mate in five or whatever. We can have mate in N positions for any N. In infinite chess, you can create a position which is not mate in N for any N, but white has a winning strategy that will win in infinitely many moves. In other words, Let me say it again. There are positions in infinite chess that white can definitely win. In infinitely many moves, white is going to make checkmate, but there’s no particular N for which white can guarantee to win in N moves.

**3:28:56** · Lex Fridman: There’s no N?

**3:28:57** · Joel David Hamkins: No N. So it’s not mate in N for any N, but it’s a white win, infinitely many. The way to think about it is white is going to win, but black controls how long it takes.

**3:29:09** · Lex Fridman: Ah, got it.

**3:29:10** · Joel David Hamkins: But it’s doomed. Black can say, “Well, I know you’re going to win, but this time it’s going to… you’re going to take a thousand moves at least.” And… Or maybe in a different way of playing, black can say, “Well, I know you’re going to win, but this time you’re going to have to take a million moves.” For any number, black can say that. So these are really interesting positions. There’s a position in my first infinite chess paper. So it’s black to play in this position, and if black doesn’t move that rook there, then white is going to checkmate pretty quickly.

**3:29:41** · Lex Fridman: By the way, can we describe the rules of infinite chess?

**3:29:44** · Joel David Hamkins: Right. So the rules of infinite chess are the… there’s just the ordinary pieces, and they move on this infinite board, which is just a chessboard, but extended in all directions.

**3:29:53** · Joel David Hamkins: Infinitely, with no edge. So there’s no boundary. But the pieces move just like you’d expect. So the knights move just the same and the rooks move, you know, on the ranks and files, and the bishops move on the same color diagonals and… just like you would expect, except they can move as far as they want, you know, if there’s no intervening piece in the way. The one thing is that… Okay, so the white pawns always move upwards and the black pawns always move downwards, but when they’re capturing, the pawns, you know, capture on the diagonal. So I think the piece movement is pretty clear. There are a couple of differences that you have to pay attention to from ordinary chess.

**3:30:32** · Joel David Hamkins: For example, there’s this threefold repetition rule in ordinary chess, but we just, we just get rid of this for infinite chess because, of course, threefold repetition is just a proxy for infinite play. The real rule is infinite play is a draw, not threefold repetition is a draw. That’s just a kind of convenient approximation to what I view as the actual rule, which is that infinite play is a draw. So the only way to win is to make checkmate on the board at a finite stage of play. And if you play infinitely, you haven’t done that, and so it’s a draw.

**3:31:05** · Lex Fridman: And the pawns can’t be converted into something else?

**3:31:06** · Joel David Hamkins: And there’s no promotion because there’s no edge. Right, exactly. And this position that we were just talking about is a position with game value omega, which means that because it has an ordinal value, white is going to win, but black can play as though counting down from omega. What is the nature of counting down from omega? If you’re black and you need to count down from omega, then you have to say a finite number.

**3:31:33** · Joel David Hamkins: … and then after that, it’s going to be at most that many numbers afterwards to count down, right? So the nature of counting down from omega is that you take this giant step on the first count, and then after that, you subtract one each time. You can’t subtract one from omega because that’s not an ordinal. So if you count down from omega, you have to go to some finite number, and then if you just subtract one each time, then that’s how many more moves you get. So that’s the sense in which black can make it take as long as he wants because he can pick his initial number to be whatever he wants.

**3:32:05** · Lex Fridman: By the way, I, I just noticed that you were citing a MathOverflow question, which is really cool.

**3:32:10** · Joel David Hamkins: That’s right, yeah. My interest in infinite chess was born on MathOverflow because someone asked this question.

**3:32:15** · Lex Fridman: Noam Elkies asked this question. That’s so cool to see a MathOverflow citation in a, in an arXiv paper. That’s cool. How do you construct the position-

**3:32:28** · Joel David Hamkins: Right

**3:32:28** · Lex Fridman: …that satisfies this? Is there an algorithm for construction?

**3:32:31** · Joel David Hamkins: No. This is an act of mathematical creativity, really, to come up with… I had a co-author, my co-author, Corey Evans. He’s a U.S. national master chess player. Very strong chess player. He’s also a philosophy professor of law.

**3:32:49** · Lex Fridman: Your collaborations are wonderful. That’s great.

**3:32:53** · Joel David Hamkins: So I met him because he was a grad student at CUNY, where I was at the time in New York. And also he was my son’s chess coach for when my son was… …Playing chess competitively in elementary school. Corey was the coach. And so we knew him that way. That was right around the time when I was getting interested in infinite chess, and I knew I needed a chess-knowledgeable partner. Corey was invaluable for the paper because the proofs in infinite chess are extremely finicky because you create these positions, but the details of the argument have to do with chess reasoning, you know? My chess reading wasn’t quite up to it because I would create the positions… Almost all the positions are ones that I made, but this is like after many generations…

**3:33:50** · Joel David Hamkins: …of being corrected by Corey because Corey would come and say, “Hey, you know, this pawn is hanging, and it breaks your argument, and…” “…or, or, you know, this bishop can leak out…” …of the cage,” or whatever. And so the process was I knew kind of in terms of these ordinals what we needed to create with…

**3:34:10** · Joel David Hamkins: …the position, and I would struggle to do it and create something that sort of had the features that I wanted, and then I would show it to Corey and he would say, “Look, it doesn’t work because of this and that,” and so on. This kind of back and forth was extremely helpful to me, and eventually we, you know, converged on arguments that were correct. So, yeah, it’s quite interesting. Also, maybe another thing to say is the follow-up paper to this one was a three-way paper with Corey, myself, and my PhD student, Norman Perlmutter, in which we improved the bound. So we were aiming to produce more and more chess positions with higher and higher ordinal values.

**3:34:52** · Joel David Hamkins: The initial position was value omega, and then we made omega-squared and omega-cubed in the first paper, and then in this three-way collaboration, we made omega to the fourth.

**3:35:03** · Lex Fridman: The title of the paper is “The Position in Infinite Chess with Game Value Omega to the 4th.”

**3:35:09** · Joel David Hamkins: Right. And so at the time, this was the best-known result, the state of the art, but since that time, it’s been improved now dramatically. And in fact, we know now that every countable ordinal arises as the game value of a position in infinite chess, so it’s a fantastic result.

**3:35:28** · Lex Fridman: Before I forget, let me ask about your views on AI and LLMs that are getting better and better at mathematics. We’ve spoken about collaborators, and you have so many collaborators. Do you see AI as a potential great collaborator to you as a mathematician, and what do you think the future role of those… …Kinds of AI systems is?

**3:35:52** · Joel David Hamkins: I guess I would draw a distinction between what we have currently and what might come in future years. I’ve played around with it and I’ve tried experimenting, but I haven’t found it helpful at all, basically zero. It’s not helpful to me. And, you know, I’ve used various systems and so on, the paid models and so on, and my typical experience interacting with AI on a mathematical question is that it gives me garbage answers that are not mathematically correct. And so I find that not helpful and also frustrating. If I was interacting with a person, the frustrating thing is when you have to argue about whether or not the argument they gave you is right, and you point out exactly the error—

**3:36:47** · Joel David Hamkins: …in the AI saying, “Oh, it’s totally fine.” If I were having such an experience with a person, I would simply refuse to talk to that person again. But okay, one has to overlook these kind of flaws. And so I tend to be a skeptic about the current value of the current AI systems as far as mathematical reasoning is concerned. It seems not reliable. But I know for a fact that there are several prominent mathematicians who I have enormous respect for who are saying that they are using it in a way— …that’s helpful, and I’m often very surprised to hear that based on my own experience, which is quite the opposite. Maybe my process isn’t any good, although I use it for other things like programming or image generation and so on. It’s amazingly powerful and helpful.

**3:37:50** · Joel David Hamkins: But for mathematical arguments, I haven’t found it helpful, and maybe I’m not interacting with it in the right way— …yet, or it could be. And so maybe I just need to improve my skill. But also maybe I wonder, like, these examples that are provided by other people maybe involve quite a huge amount of interaction, and so I wonder if maybe the mathematical ideas are really coming from the person, you know, these great mathematicians—

**3:38:21** · Joel David Hamkins: …who are doing it rather than the AI. And so I tend to be skeptical. But also, I’m skeptical for another reason, and that is because of the nature of the large language model approach to AI doing mathematics. I recognize that the AI is trying to give me an argument that sounds like a proof rather than an argument that is a proof. The motivation is misplaced. And so I worry that this is a very dangerous source of error because it often happens in mathematics that… I mean, if I think back to when I was an undergrad, here at Caltech, I was a math major eventually, and at that time, LaTeX was a pretty new thing and I was learning LaTeX, and so I was typing up my homeworks in LaTeX and they looked beautiful. Actually, they looked like garbage. From my current standards—

**3:39:28** · Joel David Hamkins: …I’m sure it was terrible. Except at the time, I didn’t know anything. I was an undergrad and LaTeX was sort of unheard of, and so I was producing these beautifully typeset, you know— …problem sets, solutions, and so on. And I would print it up and submit it and so on, and the grades would come back, terrible grades, and I realized what was happening— The copy was so beautiful, mathematically typeset in this way, it looked like the kind of mathematics you find in a book. Because basically, that’s the only time you saw that kind of mathematical typesetting was in a professional, published book. And that mathematics was almost always correct. …In a book, right? And so I had somehow lost my…

**3:40:20** · Joel David Hamkins: …because it was so beautiful, and I’m used to only seeing that kind of typesetting when an argument was totally right. I wasn’t critical enough and was making these bonehead mistakes in the proofs. So, okay, I corrected this, of course.

**3:40:36** · Lex Fridman: But this kind of effect is very much real with the modern LLM system.

**3:40:39** · Joel David Hamkins: Yes.

**3:40:40** · Lex Fridman: That’s right.

**3:40:40** · Joel David Hamkins: And so I think that the chat programs and so on are producing these arguments that look really… That’s what they’re striving to do, that’s what they’re designed to do. They’re not designed to make a logically correct argument. They’re designed to make something that looks like a logically correct argument. And it’s easy to get fooled if you’re not skeptical. And so that’s why I worry a bit when people rely on AI for mathematical arguments. I mean, using… Tying them to Lean in the formal proof verification systems and so on, this is a totally different…

**3:41:17** · Joel David Hamkins: …way of operating. But for the ordinary person sitting down and using chat to come up with a mathematical argument, I think it’s a dangerous source of error if you’re not especially attuned to this very issue that the AI is going to produce something that’s not grounded in mathematical understanding, but rather something that is trying to look like something that is grounded…

**3:41:41** · Joel David Hamkins: …in mathematical understanding. And those are not the same thing at all. And furthermore, I really wonder if one can make a kind of system for producing genuine mathematical insight that isn’t based in what I would view as mathematical understanding as opposed to the text generation systems. The methods that are used, they don’t seem close enough grounded in understanding of the underlying mathematical concepts, but rather grounded in the way words appear on a page in arguments about those concepts, which are not the same.

**3:42:17** · Lex Fridman: So there’s a couple of things to say there. One, I think there is a real skill in providing the LLM system with enough information to be a good collaborator. Because you really are dealing with a different… It’s not a human being. You really have to load in everything you possibly can from your body of work, from the way you’re thinking, and that’s a real skill. And then the other thing is, for me, if it’s at all anything like programming, because I have a lot of colleagues and friends who are programmers who feel similarly to you. And for me, I’ve gotten better and better at giving as much information as possible to the systems in a really structured way, maybe because I just like natural language as a way to express my thinking.

**3:43:08** · Lex Fridman: And then the benefit comes from the inspiration that the system can provide by its ability to know a lot of things and make connections between disparate fields and between disparate concepts. And in that way, it provides not the answer but the inspiration, the handholding, the camaraderie that helps me get to the answer, because it does know a lot more than me, like knowledge. And if you give it a lot of information and ask the broader questions, it can make some really beautiful connections. But I do find that I have to be extremely patient, like you said. The amount of times I’ll do something dumb where I feel like, “You don’t get this at all, do you?” That’s a source of a lot of frustration for us humans. Like, “This…

**3:44:04** · Lex Fridman: …Wait, this thing doesn’t understand at all.” If you can have the patience to look past that, there might be some brilliant little insights that it can provide.

**3:44:16** · Joel David Hamkins: Right.

**3:44:16** · Lex Fridman: At least for me in the realm of programming. I should say programming, there’s just so much training data. There’s so much there. At least I see the light at the end of the tunnel of promising possibilities of it being a good collaborator, versus something that gives you really true genius-level insights.

**3:44:39** · Joel David Hamkins: Right. It’s probably true. I also find it likely that a lot of the, as far as mathematical training data is concerned, I just have to assume that MathOverflow answers are part of the training data.

**3:44:52** · Lex Fridman: Yes, of course.

**3:44:53** · Joel David Hamkins: It’s so…

**3:44:54** · Lex Fridman: And you’re…

**3:44:56** · Joel David Hamkins: So-

**3:44:56** · Lex Fridman: I mean, you’re talking to yourself, essentially.

**3:44:57** · Joel David Hamkins: Yeah, maybe.


### Most beautiful idea in mathematics

**3:45:00** · Lex Fridman: Sorry for the ridiculously big question, but what idea in mathematics is most beautiful to you? We’ve talked about so many.

**3:45:10** · Joel David Hamkins: The most beautiful idea in mathematics is the transfinite ordinals. These were the number system invented by Georg Cantor about counting beyond infinity, just the idea of counting beyond infinity. I mean, you count through the ordinary numbers, the natural numbers, zero, one, two, three, and so on, and then you’re not done because after that comes omega and then omega plus one and omega plus two and so on. And you can always add one. And so of course after you count through all those numbers of the form omega plus N, then you get to omega plus omega, the first number after all those. And then comes omega plus omega plus one and so on. You can always add one. And so you can just keep counting through the ordinals. It never ends.

**3:45:59** · Joel David Hamkins: Eventually, you get to omega times three, omega times four, and so on, and then the limit of those numbers, the first number that comes after all those numbers will be omega squared. And this one is the first compound limit ordinal because it’s a… A limit ordinal is one of these numbers, an ordinal, that doesn’t have an immediate predecessor like omega and omega times two, omega times three. Those are all limit ordinals. But-… by omega squared is a limit ordinal, but it’s also a limit of limit ordinals because the omega times three, omega times four, and so on, those are all limit ordinals that limit up to omega squared. And then, of course, you form omega squared plus one, and then omega squared plus two, and so on, and it never stops.

**3:46:43** · Joel David Hamkins: And it’s just absolutely beautiful and amazing, and furthermore, forms the foundation for these transfinite recursive constructions that came later. I mean starting with the Cantor-Bendixson theorem that I mentioned. And continuing with the construction of the, of the V hierarchy and Godel’s constructible universe is built this way, and Zermelo’s proof of the well-order principle using the axiom of choice is a transfinite recursive construction. And, and so the idea of just counting past infinity is so simple and elegant, and has led to so much fascinating mathematics.

**3:47:27** · Lex Fridman: Yeah, the infinity’s not the end. And what about philosophy? What to you is the most beautiful idea in philosophy?

**3:47:35** · Joel David Hamkins: So I d- I have a foot in both fields, philosophy and mathematics, and in some contexts I seem to be required to choose whether I’m a mathematician or a philosopher. I mean, my training is in mathematics. My PhD, all my degrees are mathematics. But somehow I turned myself into a philosopher over the years because my mathematical work was engaging with these philosophical issues. And so when I went… In New York, I had appointments first in mathematics only, but then eventually I was also joining the philosophy faculty at the graduate center. And when I went to Oxford for the first time, my main appointment was in philosophy, and that’s also true now at Notre Dame although I’m also a concurrent professor in mathematics.

**3:48:20** · Joel David Hamkins: And I have math PhD students still and philosophy PhD students. And so I don’t really care to decide whether I’m a mathematician or a philosopher. And my work is engaging with mathematics and with philosophical issues in mathematics and with plain philosophy, and there’s this ample region between these re- between these two subjects. So it’s not necessary to choose. I remember when I first went to Oxford and I told my daughter that I was going to become professor of philosophy in Oxford and she looked at me plaintively and said, “Uh, but, but Papa, you’re not a philosopher.” Because in her mind, you know, her father was the mathematician and her mother was the philosopher ’cause my wife, Barbara, is a philosopher. Now also at Notre Dame. We’re together there.

**3:49:13** · Joel David Hamkins: And okay, but fortunately I don’t really have to choose be- between them. So you ask about the most beautiful idea in philosophy, and I would have to say that I think it’s the distinction between truth and proof, the one that we discussed already. It’s so profound and gets at the heart of so many philosophical issues. I mean, of course, this is a distinction that’s maybe born in mathematics or mathematical logic, but that’s already philosophical to a degree, and it’s fundamentally a philosophical distinction. The truth is about the nature of the world and the way things are. It’s about objective reality in a sense, whereas proof is about our understanding of the world and about how we come to know the things that we know about the world.

**3:50:18** · Joel David Hamkins: And so to focus on proof is to focus on the interaction that we have with the objective reality. And okay, I’m talking about the reality of mathematics, not the physical world, because as I said, I live in the platonic realm and I interact with mathematical reality, and so proof is about the interaction and how we come to know the facts that are true in this mathematical reality, whereas truth is about what’s really the case, sort of apart from our knowledge of it. And and this is I think a… such a core way that I have of understanding the world and and the nature of logic and reasonings.

**3:51:03** · Lex Fridman: And the gap between the two is full of fascinating mysteries, both in the platonic realm, but also in the physics realm, in I would even say in the, in the human psychology, sociology, politics, geopolitics, all of it, if you think about proof more generally, which is the process of discovery versus the truth itself. And that’s our journey whatever field we’re in. Well, I, for one, am grateful for… … For how marvelous of a philosopher, mathematician, and human being you are. It’s truly an honor to speak with you today.

**3:51:43** · Joel David Hamkins: Well, thank you so much. It’s such a pleasure to be here, and thank you for inviting me.

**3:51:47** · Lex Fridman: Thanks for listening to this conversation with Joel David Hamkins. To support this podcast, please check out our sponsors in the description where you can also find links to contact me, ask questions, get feedback, and so on. Thank you for listening. As always, happy New Year. I love you all.
