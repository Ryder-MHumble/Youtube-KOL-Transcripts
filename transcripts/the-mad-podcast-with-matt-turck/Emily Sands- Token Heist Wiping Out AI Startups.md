---
title: The "Token Heist" Wiping Out AI Startups | Emily Sands (Stripe)
source_url: https://www.youtube.com/watch?v=6opo7LnZajM
video_id: 6opo7LnZajM
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/emily-sands|Emily Sands]]'
published: 2026-07-09
created: 2026-07-17
language: en
speaker_attribution: contextual
description: Is the internet ready for AI agents to take over our wallets and run their own businesses? In this episode of The MAD Podcast, Stripe's Emily Sands reveals how agentic commerce is rapidly shifting fro
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=6opo7LnZajM)

Is the internet ready for AI agents to take over our wallets and run their own businesses? In this episode of The MAD Podcast, Stripe's Emily Sands reveals how agentic commerce is rapidly shifting from a hypothetical concept to deployed financial infrastructure. From combating the rising existential threat of token theft to solving the bottleneck of "vibe deployment", Emily unpacks the shared payment tokens and real-time billing systems required to securely scale autonomous digital buyers and highlights a near future where agents operate as independent, end-to-end micro-firms.  
  
Emily Sands  
LinkedIn - https://www.linkedin.com/in/egsands  
X/Twitter - https://x.com/emilygsands  
  
Stripe  
Website - https://stripe.com  
X/Twitter - https://x.com/stripe  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id168623872  
  
00:00 — Cold open & Intro  
01:24 — The rise of agentic e-commerce  
02:11 — The spectrum of agent-led purchases  
03:16 — How merchants adapt to AI-driven commerce  
05:50 — Defining the levels of autonomy in AI shopping  
07:08 — What is the Agent E-Commerce Protocol (AEP)?  
08:49 — Shared payment tokens and secure AI transactions  
09:58 — Who is adopting the Agent E-Commerce Protocol?  
11:38 — Can agents negotiate and sell products?  
13:32 — The macroeconomic impact of AI agents  
14:46 — The boom of solopreneurs and AI-driven business creation  
16:56 — Why building trust is the biggest roadblock for AI commerce  
20:19 — How link wallets improve payment security  
21:21 — Improving the user experience in AI shopping apps  
23:16 — How the Link Wallet sets guardrails for AI agents  
25:40 — One-time use virtual cards vs flexible AI wallets  
28:03 — Unpacking the shared payment token primitive  
29:59 — How stablecoins enable profitable AI microtransactions  
35:03 — Managing liability: Who is at fault if an agent goes haywire?  
36:38 — Why agent payments might be safer than human transactions  
37:41 — What is Vibe Deployment?  
40:13 — Why Stripe built Stripe Projects for agent deployment  
41:22 — Why Stripe cares about orchestrating app deployments  
42:50 — How tokens break the traditional SaaS billing model  
44:34 — Why AI companies are moving to hybrid and usage-based billing  
47:15 — Streaming payments and real-time token tracking  
48:42 — The massive data challenge for AI company accountants  
50:41 — Token theft: The fastest-growing fraud in the AI economy  
52:04 — The cottage industry of free trial and multi-account abuse  
54:16 — How fraudsters monetize stolen AI tokens on the dark web  
01:00:06 — How Stripe Radar uses network density to fight AI fraud  
01:01:15 — Tempo's role in the Agent E-Commerce Protocol  
01:04:12 — The AI startup ecosystem is accelerating business creation  
01:09:01 — The token cost shock: Are buyers getting carried away?  
01:11:19 — 2026 Predictions: Agents running businesses end-to-end

## Transcript

### Cold open & Intro

**0:00** · fraudsters have figured out that in AI you actually don't really need to steal money or credentials. You can just steal tokens. And the scale of this actually shocked me when I looked at the data. So more than one in six signups at AI companies are this kind of abuse.

**0:16** · Whatever the dine and dash, but it's for token. When I go and ask my friends and family whether they'd be comfortable letting an agent buy things on their behalf, they usually jump straight to like, well, is it going to overspend and is it going to buy the wrong thing and can I stop it? And those are actually all legitimate concerns. And it's not Emily permissioning an agent to buy on her behalf. It's Emily has an agent who's tasked with running a business and that includes buying some things and selling some things and making some profits. And that would be the world that I would like to be talking about 12 months from now.

**0:45** · Hi, I'm Matt Turk. Welcome back to the Matt podcast. Today I'm excited to be joined again by Emily Sense, head of data and AI at Stripe. The rise of agent commerce has only \[music\] accelerated since Emily and I talked about it last year. And in this conversation, we go deep on the economic stack for AI agents. How agents buy and sell on your behalf, why perceive pricing is breaking, token monetization, token theft, which Emily calls the most under discussed topic in all of AI, and finally, whether agents may eventually run entire businesses on their own.

**1:18** · Please enjoy my conversation with the always excellent Emily Sense. All right, so welcome back. You and I chatted about a year ago and the theme of the discussion uh we had was all about the rise of a gentic commerce.

### The rise of agentic e-commerce

**1:34** · Keeping in mind that obviously this is a long-term trend that's going to take a while to play out. I'm curious about what you've observed over the last 12 months. What has become reality and what is yet to be built?

**1:49** · Yeah, I mean a year ago we were talking about agents as buyers in a pretty hypothetical way. Um I think that the canonical experiences, the consumer experiences, for example, uh weren't defined. We were largely reasoning kind of from first principles about what this might look like. Um fast forward a year, as you know, like still early innings, still a lot to do, but we have actual infrastructure deployed. We have real companies building on it. We have real patterns to learn from.

### The spectrum of agent-led purchases

**2:16** · Um and to be clear like the the shape of how this unfolds um has become more clear and it's going to continue to evolve. So specifically what we've come to believe is there's a full spectrum of how agentic commerce plays out and that's actually really important for businesses in how they think about it.

**2:36** · So at one end, and this is where our machine payments protocol lives, but basically you have agents that are out autonomously discovering a service and deciding to buy it and handling the transactions like entirely on their own, right? Like no human in the loop. And that's maybe what people think of when they say agent commerce, but that's just one end of the spectrum.

**2:56** · There's also the whole other end of the spectrum where like people are looking for shoes for flatfooted runners inside an AI surface and the AI surface gives you an answer and increasingly um you know that was true also in sort of traditional search but now increasingly that answer comes with a buy button. Um and so you know this is already how a huge number of people are discovering products. if you're a business, you need to show up there.

### How merchants adapt to AI-driven commerce

**3:21** · And we've been building the infrastructure to make it a easy for businesses to show up and b easy for agents uh to execute those those transactions. So, um you asked about sort of what's become more concrete. We recently partnered with Google um so merchants can sell um right inside AI mode and the Gemini app. Uh so, you know, maybe you shop at JD Sports because I was on the topic of running shoes or Fanatics or Quint. Um those were all early adopters. Uh Microsoft and OpenAI, we're doing something similar with them, like helping businesses make their products discoverable inside Copilot and ChatgPT.

**3:54** · Um Meta is another example, a little bit of a different flavor, but we're powering checkout right inside ads. So, uh there's the discovery and then the one click and the agent actually goes and executes the transaction on your behalf. Um, but really I'd say like what we've learned over the last year, the through line is like whether we're talking about like fully agent-led transactions with MPP or these very sort of um human-led purchases inside AI

**4:20** · services. um there's just a new set of infrastructure that needs to work um no matter where you are in the spectrum and and that includes I mean it's the premise behind our agentic commerce suite but briefly like businesses need to be able to expose their products and their cataloges and their prices um and then consumers need to be able to authorize agents to pay on their behalf and then agents need to be able to safely execute um that transaction. So um that is the infrastructure we have built. Those are some of the partners that we've been working with.

**4:52** · Um, and I would say like, you know, the companies building on it probably give you a good read of where commerce is headed, right?

**5:00** · So, companies like Wix and Shopify and Big Commerce and Commerce tools sort of on the platform side and then uh on the brand side like Best Buy and Coach and URBN and Kate Spade. Um, but again, it's still early and what the interaction patterns will be and how they'll evolve.

**5:15** · And I'm particularly interested in like how quickly consumers will give up more of the decisioning process and really move from consumer happening over here where AI helps you find the product and the agent is the one sort of uh helping you avoid going through cumbersome checkout flows uh to a time when we say like I don't know I have a $500 budget for back to school shopping and you already know everything about my kids and their school and where I live so like get it done or I don't even tell you and just go do it for me.

**5:45** · Um but but I think we will need to learn that over the coming year or two.

### Defining the levels of autonomy in AI shopping

**5:50** · Is there a framework for urgent e-comic commerce that you guys came up with like somebody in the industry came up with that? So that would almost be like the levels of autonomy for self-driving cars like you know L1 you discover.

**6:03** · We do literally. Yes. Oh my gosh. It's like we had like level one, level two, level three. Basically, if if you think about it, it's just like the the highest level is sort of the the MPP version that I talked about where the agent is like truly autonomous and sort of the level one is uh the human does basically all of the decisioning themselves and it's the simple execution of the transaction. And I would say sort of on the consumer side, we're mostly hovering level two.

**6:29** · You know, people are de delegating a little bit of the selection or leaning hard on the AI to help find the product. maybe a hint of level three, but like you know, we're not in the world where you're booking your summer vacation oneshotting it with an LLM.

**6:45** · And what what would you describe from a vendor standpoint? That's that would be sort of like level three. So that that's a reality as of today, right? So you can already get a recommendation and then you you press the the the button. That's sort of where we are. And an example of this would be JGPD instant checkout, for example, where you get the recommendation.

**7:04** · Totally. or you're in Gemini or you know yeah exactly you touch uh upon some some important developments uh that happened since we last chatted in terms of like overall maturation of the uh industry you mentioned the agentic commerce protocol which I think came out last fall what is that I think that's something that you guys built in partnership with openai yes we built it in partnership with openai the agentic commerce protocol is just a a standardized way for businesses to work

### What is the Agent E-Commerce Protocol (AEP)?

**7:35** · with agents and there's a couple different components of it. Um, and this is sort of wrapped in our broader agentic commerce suite. Uh, one is how do businesses expose their product catalog, their inventory, their prices to agents? Um, and you know, you could argue, oh, the agents could go out and uh, you know, search or infer, but sort of inventory is a thing that you want like deterministically known.

**8:00** · Um, and we don't want businesses to need to kind of register their product catalog or register their inventory with every single new agent that comes online because in the same way you and I like to work with a lot of different model providers uh or a lot of different models within those model providers, in many cases both uh we we similarly are seeing businesses not want to place bets on just one agentic surface. Um they may be selling BTOC and B2B. They may be wanting to reach a wide swath of consumers across many different um surfaces. doesn't.

**8:31** · So, agentic commerce protocol lets them um expose their product catalog once um and then opt in to um all of the agents uh who who uh work with with that protocol. Um it also includes the the shared payment token.

### Shared payment tokens and secure AI transactions

**8:49** · And so this is about making sure that um in the moment of transaction, the agent can securely pass the buyer's credentials over to the seller to execute the the transactions. And these are just tokenized credentials. So, you know, the agent doesn't have um access to the credentials in the way that you and I probably wouldn't want an agent uh to have our credit card.

**9:10** · Um, and one thing I love about, you know, both the um, catalog component of this as well as the shared uh, payment token is it's uh, platform agnostic, payment processor agnostic. So all this works uh, you know, you mentioned that we co-created with OpenAI. It works with OpenAI but also other providers. It works if Stripe processes your payments, but you can also pass on that that shared payment token uh, to any other uh, PSP.

**9:33** · Um, and for us, this is really about making it easy for businesses to reach their customers where they are, which is increasingly through AI tools and to not have to reinvent their commerce infrastructure to do that. Right? We want to reinvent commerce infrastructure once and then they out of the box um can get these sort of uh new lines uh of demand.

### Who is adopting the Agent E-Commerce Protocol?

**9:58** · So ACP is a little bit like MCP but for commerce, right? That's hence the name with the status. So that was launched in uh at the end of uh September of last year. In terms of like overall adoption, is that kind of like a work in progress to get commerce companies to to embrace it or where are we?

**10:16** · We've actually seen a ton of demand from brands. So Best Buy's on it, Coaches on it, URBN's on it, Kate Spade's on it. Um we've seen uh Quint and Fanatics and JD Sports and a whole bunch more. Um, we've seen a ton of demand from platforms which sort of uh you've probably long thought of platforms like Wix or Shopify or Big Commerce or whatever. You've probably long thought of them as um you know building technology for small businesses to do commerce.

**10:41** · And now an important part of uh technology for small businesses to do commerce is making sure those small businesses um are appearing in AI tools and can engage in this wave of agentic commerce. And so Wix and Shopify and Big Commerce and Commerce tools on the platform side have all um adopted the protocol. And then on the AI side, on the agent side, we're working with all the all the big ones.

**11:04** · So uh with with Geminis and with Google, uh Microsoft, uh Open AI, uh and um lots more coming online in in all three dimensions. But we really think of like the this the supply side is a combination of the large brands and the platforms who have the small businesses.

**11:20** · Um and then on the um sort of agent side, it's what you would think of as the traditional agent pay players and then there's been some um interesting nuance as well for example with meta where like well maybe ads are just becoming agentic buying too. Um and so that's been an interesting extension and I think we talked mostly so far about agents buying at least like in the example we gave where the agent represents the the consumer.

### Can agents negotiate and sell products?

**11:44** · Presumably there's a concept of agent selling as well like what's the what does this look like in the future like if all technical problems has solved and adoptions happen is that basically two agents negotiating something what is the ultimate vision so when I when when I when I like step back with my economist brain I'm like that would be really efficient right agents are really good at discovery right we've already seen that um agents are really good at integration agents are pretty good at like finding optimal pricing matching, negotiating.

**12:15** · They're incredibly persistent. Uh their time is worth a lot less than human time and they can get those get those back and forths done um much more much more quickly. Um and then they're also actually really good with like integrating and actually adopting the thing. So, especially if you think of like B2B buying and maybe we can talk about um Stripe Projects a little bit later too, but just like actually like not just finding the service and negotiating it for the price and contracting on it and buying it, but actually like getting all the way to integrating and using the product.

**12:44** · Um I think agents are going to help with a lot. And so I'm I'm definitely um imagining an economy that is much more efficient because you have agents on the buy side and as you note also on the sell side and they're kind of hyperefficient on all of those dimensions uh which of course um you

**13:02** · know in the in the in the uh Ronald Coast Nobel Prize winner Ronald Coast version of the world would basically um just like remove frictions for firms to work with each other would make markets more efficient would make competition higher would serve consumers would spur growth. Um I will say today not a lot of agent agent transactions happening. So like you know you you asked at the top like what's become real and what's still in the future. I think that's still in the future. Um but I think you start with one side you add the other and and over time um we probably land with both.

### The macroeconomic impact of AI agents

**13:32** · Why does this matter so much? On the one hand it's it's it's kind of cool. I can be uh you know doing something and my agent does uh like look looks for a good product because it knows me. So it's personalized. So it's convenient. Uh but I think what you're saying is that it's it's much deeper than that. It's a it's a global kind of economy acceleration, productivity acceleration. Not to put words in your mouth, but like that's what's at stake ultimately.

**13:57** · Yes.

**13:57** · And actually that you know that is true on kind of the consumption side, right? If we make it easier for folks to discover and transact and integrate um uh then that will spur growth. And by the way, we're we're we're seeing I think uh some productivity uh in the global numbers from AI, but I think right now it's not primarily about consumption because like the numbers are still very small.

**14:22** · It's primarily about like oh we're flooding the economy with a bunch of AI capex like that's that's actually the consumption that's getting pumped into the economy. But I think that's that's definitely going to be um a driver over time. It is also true that um there there's a deeper change which is agents are making it easier not just to buy things but also to like start and run companies. Um that's a whole other other angle but we we see that very solidly in the macro data.

### The boom of solopreneurs and AI-driven business creation

**14:50** · Um you know I don't know if you've seen like US business formations over time but during the pandemic they surged. that wasn't super surprising. But then if you look, they like plateaued over time and then they're like accelerating again now over the last um couple quarters. And what's interesting to me isn't just that acceleration, but actually the composition.

**15:09** · Like what are all of those incremental new businesses being created um and the incremental growth is coming entirely from uh non-employer firms is the literal language that the Census Bureau uses, but you and I would just call them solopreneurs. And so, you know, the number of people, solarpreneurs, who are earning more than $100,000 a year, um, has just gone like this since 2022. And now there's in America alone 5 million people making their living running solo companies.

**15:37** · Not like, oh, I just said I was a solarreneur. Like literally, that is my income supporting my family. Um, and there are hundreds of thousands that are clearing a million a year. And so, you know, I I think that's kind of interesting because it's like, uh, with AI, can you build something? And then with AI, can you run the business around it? I think vibe coding and and vibe deploying, by the way, are are really important for can you build something?

**16:00** · And then there's a bunch happening in AI um domain domain specific agents that are really solving for like can you run that business um on the accounting side and the customer support side and and um and that's making these these smaller companies um very structurally viable.

**16:18** · So anyway, I think like the the economic enthusiasm I have around AI comes somewhat from the efficiency of sort of markets and growing consumption and better matching and so on, but just as much if not more from the effect AI is having on business dynamism and the ability for um individuals with an idea to get from an idea to a product that is in market um and and meeting real uh user needs.

**16:48** · So um anyway, I think I think they'll both I think they'll both play into the macro numbers increasingly over the coming years.

### Why building trust is the biggest roadblock for AI commerce

**16:56** · So as we close this kind of like overview introduction section just um on the the reality of a gentommerce and the impact in including the future impact of agendom. What are the biggest roadblocks right now? uh in in particular, do you think that the uh issue ultimately is more just like technical capabilities and we'll talk in a second about some of the stuff that you guys have built or is that a human question of like trust and

**17:23** · just accepting to have the machine do things for you especially when your money is your personal money is at stake? Yeah, I think the the two primary um blockers that you know we'll need to move through to really scale this up are um one trust and actually we've we've done a lot on the trust side. We talked about the shared payment token agent doesn't have any access to the credentials. Every shared payment token includes radar scores, right? Both is this a legitimate buyer and is this an agent acting in a legitimate way on behalf of the buyer.

**17:54** · Um maybe we'll talk a little bit about link as the wallet for agents, but we've done a lot so that consumers can set guard rails around what the agent can spend, right? So it's it's a little different than like a one-time use virtual card, which are like uh pretty maniacally scoped credentials, but in the case of a link wallet, you you very much have have the guard rails to set.

**18:14** · But even with the sort of trust layer from a from a technology or infrastructure perspective, like I just think it takes time for any market to build trust, especially when you're talking about um making decisions for, you know, what I buy and spending my money. Um I think it's very natural for humans to kind of want to build their way up to that.

**18:35** · And so, um, I think that's a that's a big reason why on the consumer side, what we're mostly seeing is people are discovering things inside AI apps, but they're still choosing the exact thing and they're still disproportionately buying low to mid-pric stuff. Um, and they'll need more trust and honestly also to some extent an evolution of um, the user experience uh, in some of those apps um, if they're going to get to a place where they're where they're handing off major decisions.

**19:04** · By the way, you know, I I I wasn't uh super close to how people moved their uh spending from stores to online, but I bet in the first few years of sending on spending online, nobody was saying like, you know, I'm going to go online and buy a couch or a mattress or a leather jacket, like a thing that I want to feel or I'm going to spend a lot of money on or where like uh quality is sort of hard to infer from things I can tell on the internet.

**19:30** · Um, and over time mechanisms built up for people to trust that that was the right product, that when they spent substantial money, it was going to arrive at their door in good shape. Um, and obviously today there's probably more mattresses bought online than than in person. So I I think we will get there, but I think trust is uh an important enabler and I would say again a lot of the technology foundations are in place, but it just takes reps. Like humans just need reps um for trust to be built. When it comes to financial stuff, basically nobody enters with an assumption of trust.

**20:00** · Uh you have to you have to earn it.

**20:03** · I'm not going to tell you that, but uh there was a a time when the idea of like entering a credit card on the uh internet was uh completely insane. Uh which of course led to the unbelievable rise of Stripe and and um and all the success. Um so okay, fantastic.

### How link wallets improve payment security

**20:19** · But that's interesting, right? it there is still a I mean it I still feel extremely uncomfortable entering my bank account details on the internet so I'm happy to enter my bank account details to my link wallet on stripe so that it

**20:35** · can make payments on my behalf but I am not happy to enter uh still today on the internet uh my my bank account number and you know and I think this is this is actually really interesting to reason about uh will the internet actually get safer to some extent as these

**20:53** · foundations that we are um sort of they're being pulled out of us because of agentic commerce but as you know stored balances and wallets and linked bank accounts and whatever become more of the norm I don't know I need my agent to like be able to burn down my stable coin balance with some guard rails like does that actually reduce at least the types of fraud that we've seen in um traditional uh traditional online commerce. Maybe maybe you talked about the uh user experience inside of the app not being great.

### Improving the user experience in AI shopping apps

**21:25** · Do you have is there anything specific that you have in mind in terms of like how it falls short?

**21:35** · I think there's a few things. um one and you know part of what we're um working on with the agentic commerce suite is it should be really easy for um these you know AI tools LLMs to accurately reflect and comprehensively reflect inventory um you know absent uh a standard

**22:00** · protocol it's actually like a little bit tricky to know exactly who's selling what and is it real and how's it priced and how much is left and what are the various parameters? And so um partly the experience I think just needs to evolve to actually have the right inventory set to read over and the right um deterministic metadata on that inventory set um that that the LLM can then do non-deterministic things on top of.

**22:22** · Um, but I think some of the experience is just uh, you know, we're all very familiar with uh, the the flow of going in and typing in search and getting some shopping results and choosing a thing.

**22:37** · But I think that whole like what part of consumption do we want to delegate and what experience do we need, which is a little bit of the discovery and a little bit of the guardrails and a little bit of the trust. um but also just like the depth of understanding of us um in order for that to be a great a

**22:58** · great customer experience and I you know there there's lots of great AI tools out there and there's lots of ways that they're accelerating you know the efficiency of consumption but I haven't yet seen I guess I what I was saying on experience is I haven't yet seen an experience where I'm like that is magical and I know exactly the end things that I'm ready to offload. I want to cover some of the stuff that um you mentioned in passing around what you all have built and released in 2026 um and especially around the concept of of giving agents money uh safely. You mentioned uh the link wallet.

### How the Link Wallet sets guardrails for AI agents

**23:31** · What is the link wallet for agents in simple terms?

**23:37** · Yes.

**23:37** · So maybe even before we get to agents, link is just Stripe's consumer wallet and 300 million um users uh use it today. Uh we're making that the wallet for agents. So the idea is you can authorize an agent to make payments on your behalf, but you get these built-in controls so you stay in the loop, right? So you're not giving the agent like a blank check or unlimited access to your checking account. You're very distinctly like defining what it can do. Um, and you can always uh pull it back.

**24:07** · And you know, we talked about trust a bit earlier. I actually think the trust dimension here is like as underrated or under discussed as the product challenge. Like when I go and ask my friends and family whether they'd be comfortable letting an agent buy things on their behalf, they usually jump straight to like, well, is it going to overspend and is it going to buy the wrong thing and can I stop it and what happens if it buys the wrong thing? And those are actually all legitimate concerns. And so um the controls within link wallet um are really what make the whole thing uh viable for for consumers.

**24:39** · Um I would also say that like uh you and I and others have many different payment credentials, right? Like we have uh bank accounts and we have uh credit cards and we may have debit cards and there are buy now pay laterers. Um and one of and stable coins and whatever else.

**24:56** · One of the nice things about um a single wallet that can be backed by balances and many different payment credentials, fiat and crypto and whatever else um is, you know, there's just there's just one like, you know, I don't like having a lot of uh things to reason over and I especially don't like having a lot of things to reason over when I am passing it off to an agent and need to monitor it and make sure that what I think is happening is actually happening.

**25:24** · Um, and so I think part of the beauty of the link wallet is also just the the consolidation. You can back it by whatever the payment credentials are, but at the end of the day, your agent wallet is just a single wallet. Um, which makes it much more uh streamlined to reason around.

### One-time use virtual cards vs flexible AI wallets

**25:40** · And technically, is that a one-time usage credit card or is that completely different?

**25:47** · Good question. Okay. So, the very like when we were talking 12 months ago, the very very first version of Agentic Commerce on Stripe and I think in the world was these one-time use cards. And uh actually the genesis of that was one-time use cards that we used um for like platforms and marketplaces, right?

**26:05** · Like when I order um a salad from Door Dash, the driver has a one-time use virtual card uh that can be used to pay for my salad. And that feels good to me because uh neither the driver nor the restaurant which I don't have any affiliation with needs to see my payment credentials. And so uh in the first version of agent commerce which for us uh I believe the very first uh meaningfully live volume was on perplexity shopping we used uh these these one-time use virtual cards.

**26:33** · And basically the the human consumer would say they wanted the thing. their payment credentials were used to basically buy this like onetime fund, this onetime use virtual card. The agent was handed this onetime use virtual card and then they went off on the internet and and and purchased with it. And that was uh very scoped uh by definition of being one time and it was generally um you know scoped to a single provider and scoped to a very fixed amount.

**27:01** · Uh I would think of uh link wallet as much more flexible, right? So I can set a budget uh to be used across a set of providers or set of providers in a domain. Um I can permission at the individual transaction level or I can permission sort of above some amount in aggregate or individually. And so um one time use virtual cards were super valuable for sort of getting us off the ground especially for these sort of singleuse consumer transactions. Um but the link wallet is much more flexible.

**27:34** · Now I still think that we will be a few months hence before folks are actually um agreeing to um you know agents using the wallet uh beyond a particular scoped transaction but making sure the infrastructure scales to that is really where we are with link wallet. Um and then as the consumers become ready for it the technology is already online uh and there's no hold up. You mentioned shared payment token. What what is that?

### Unpacking the shared payment token primitive

**28:06** · It's a new payment primitive. We built it u maybe six months ago specifically for agent commerce. Um it is a way for a consumer to authorize an AI agent to pay on their behalf um without handing over their actual card details. So the token encodes um exactly what the agent is allowed to do, right? Which merchants can be charged up to what amount, in what currency, for how long. Um the agent presents the token to the merchant at checkout. Um the agent never sees the underlying credentials.

**28:37** · Um and uh shared payment tokens, you know, cover more payment methods, including buy now pay later options like a firm and CLA. So it's not just cards. Um it can really represent like different payment methods uh depending on what uh the user has on file. And this is actually the payment primitive that makes links wallet for agents work. Um it also powers our machine uh payments work.

**29:01** · Uh it's really about okay how can agents transact uh without taking on risk and how can businesses remain in control uh as the merchant of record. And so I would think of like one-time use virtual cards were like a useful backs stop as we went and built the shared uh payment token. Shared payment token is a new payments primitive that is wallet agnostic and by the way also payment processor agnostic.

**29:24** · You can pass it over to Adion or whoever else you have. uh it doesn't have to be processed on Stripe. And then think of like link wallet as the consumer experience, the consumer wallet for agents um that leverages that same uh shared payments token primitive um but is more um fully featured for the consumer and it's software so it's fully programmable. So just to double click on some of what you just said, you can restrict certain categories of merchant or you can only buy from Amazon uh or you can only buy in the US or in France or Yes. Exactly.

### How stablecoins enable profitable AI microtransactions

**29:59** · Fantastic.

**29:59** · Or or you can or you can literally set it to say I need to approve every single transaction, right? Um and you know when people are making reasonable size transactions that's fine. I think we're going to move to a world very quickly sort of at the intersection of agent to commerce and what stable coins enable in terms of sort of microtransactions and then reasoning about agents as the buyers.

**30:23** · Agents are very you know microtransactions never actually really made that much sense even in the context of content because nobody wanted to put in even if it was only 5 cents no one wanted to put in their credit card to buy a 5 cents article like that was just too much friction. A and B, nobody wanted to process a credit card for 5 cents because you would have negative margins. But I think we enter a world where like the human is not doing any work to execute the transaction. You're not typing in any credentials. You're not navigating to any web pages. The agent's doing it for you. Um then microtransactions become viable.

**30:56** · And you pair that with okay and now it's you know uh burning down some stable coin balance. And we can talk about the work we're doing with Tempo there. um suddenly microtransactions become very viable and I think we're going to quickly move to a world where especially in buying inference or tokens or um sort of AI sassy products um there's going to be you know you are going to be using

**31:23** · your link wallet to um make a ton of microtransactions and not approve everyone. But yes, if today you want to approve everyone you can. that's not going to scale because no one's going to want to approve the the one cent transaction for the little bit of data, the little bit of research or the token um that I needed for for this job.

**31:40** · So, what's a current thinking in terms of like everything that can go wrong?

**31:45** · You know, you were saying like when you talk about this to your friends, they they say, well, what if the agent buys the wrong thing and so on and so forth.

**31:52** · Uh I mean, presumably that's a the frontier. Everybody's trying to figure it out, but what's the current thinking?

**31:59** · Yeah.

**31:59** · We're thinking about this in a few dimensions. One is um to your question on you know what if what if the wrong thing gets sent or the thing's not good or whatever. Um businesses have to remain the merchant of record. Like that's a core design principle for us.

**32:13** · Um which means like we see our job as having agentic transactions behave the way human transactions do. Now that doesn't mean that agents need to behave like humans or be constrained in the same way humans do. from the perspective of the business um they remain the merchant of records. They are selling you know they happen to have that sale facilitated through an agent but like the business is still um the business.

**32:40** · Uh another design principle which we've touched on a bit in different ways is always provide appropriate granular programmable controls and guardrails to enable commerce to happen at scale. And that's basically saying like no matter how scoped in and in control you want to be or how much you want it to be a free-for-all, like you shouldn't have to adopt a new tool, move to a new wallet, change, you know, the underlying payment uh rails, you shouldn't have to change your product catalog or where you expose it.

**33:10** · Like basically out of the box, um uh those those controls and guardrails should uh should eb and flow. And I think in the consumer case um that looks like consumers remaining in charge of how link authorizes agents to buy. Um

**33:27** · and in the business case um you know I touched on this briefly in the context of shared payment token but it looks like making sure that the information we have about the goodness of the underlying buyer and the agent operating on that buyer's behalf are passed fully to the business. um to action intelligently. And so, you know, Radar is our fraud uh protection product.

**33:52** · We've had it for uh over a decade. It used to be really about transaction fraud. Now, it looks at all kinds of um fraud and abuse and bought and multiple layers of goodness where there's not just the the the end customer, but also the agent operating on behalf of the customer. And so, those radar scores are actually included out of the box in the shared payment token uh for businesses to businesses to reason about But but basically I think business remains merchant of record.

**34:16** · Consumer has as fine grain guard rails and controls as they need and then in the ecosystem there is as much uh symmetric information as as we can create. I mean we now look across just about 2% of of global GDP. Um, in the context of AI, we look at a very very large share uh of that of that GDB because basically all AI buyers and all AI sellers are on link um and on Stripe.

**34:48** · Um, and so you know that that allows us to actually understand um when something is going sideways uh and we see uh very much our job to uh protect the ecosystem by by providing that information up front. It's really fascinating as one unpacks this entire line of thinking around agentic commerce because this what the technology can do that's what you can do as a responsible player in the ecosystem but like ultimately a lot of this will have to go to court one way or another.

### Managing liability: Who is at fault if an agent goes haywire?

**35:18** · I mean the legal system will need to uh adapt and evolve because if something goes terribly wrong you know large commerce transaction you know who's at fault. ultimately could could it be the the model provider underneath because like the agent went haywire. I guess all of this is going to take time to work its way through the ecosystem.

**35:37** · Yeah.

**35:37** · Not just in purchasing, right?

**35:39** · Like uh you know who is at fault for not just bad purchasing behavior but bad behavior of all types when when there's an agent involved. So so I do think uh the the landscape is changing there.

**35:51** · when it comes to sort of payments in particular, you you mentioned a bit ago that um uh back in the day people didn't really trust just like putting their credit card on on the internet. I think it's interesting to think like with things like shared payment tokens, agent never sees the underlying credentials.

**36:10** · Um each transaction is scored in real time by Stripe Radar. Um merchants go and handle the transactions. Credentials like never travel through untrusted services. the way they can when a human types a credit card number into a random website, not Stripe, but other random websites. Um, and so anyway, I think it's also interesting to ask like is there is there sort of meaningful payments trust and safety upside here?

**36:35** · Um, and and I could imagine yes.

### Why agent payments might be safer than human transactions

**36:38** · So to play it back, agent payments would eventually be safer than than human just typing cards in terms of fraud, in terms of mistake presumably as well, right?

**36:49** · Like if you type in the wrong number or something like that.

**36:52** · Yes.

**36:52** · Done like done right in the limit.

**36:55** · I believe it should be much safer. Today I think the first order effect is it's just more convenient. Like right \[laughter\] like usually it's not a fraudster on my credit card. It's like me fat fingering my own CBC. It's annoying and I'm frustrated. Um but you know right now I think most of what we're getting is is convenience. But in the limit, yeah, you could you could totally imagine, okay, now nobody's passing these random payment credentials uh over the internet.

**37:20** · And by the way, people also aren't really necessarily reasoning about transactions coming in through 10 different payment credentials they have, right? They really have a wallet. They see what happens in the wallet. Um and that wallet is used in a very tokenized uh secure way uh across sellers. So another really interesting topic I wanted to cover and that you mentioned briefly is vibe deployment.

### What is Vibe Deployment?

**37:47** · What does that mean?

**37:49** · It's what happens after you build the thing and it's actually not talked about enough but like the coding part uh a lot of people talked about AI for coding you know when we were talking a year ago that makes sense because it wasn't solved now that's basically solved um and we actually see that it's solved in our data. Um these are semi-random facts but I I find them interesting.

**38:07** · So like agent traffic to Stripe's documentation grew more than 10x since we talked a year ago. uh agent traffic is now about 40% of all our docs traffic and meaning meaning that the agents are trying to figure it out and they go to the stripe technical documentation to understand uh meaning the coders now are are almost as much agents as they are developers and in some segments they are basically all agents and and uh not at all developers

**38:38** · and another example actually is is our CLI our command line interface which historically was like a pretty niche tool used by like a pretty small group of developers. Um it now it just like exploded and we were like what is happening? And it's now um 70% of its API resource requests are from agents.

**38:57** · So like you could think of like the majorities the majority of entities that are using our CLI today like aren't people. So anyway, I think though you know those are just two like fun stripe anecdotes, but there's lots of them across the ecosystem you can look at that tells you like vibe coding is real, right? Just your own lived experience is the same, right? That part worked. But then what? So like an agent writes you like a complete working application in 20 minutes. Fabulous. Like we love it.

**39:24** · Okay. But you've still got this pretty big friction before that app is actually live, right? So you got to go like I don't I mean it depends what you're doing, but you got to probably create an account with your database provider, then your off provider, then your hosting service, and you're like bouncing around. You got all these dashboards. you're like I don't know how you do it like copy pasting stuff by hand and managing credentials and API keys and whatever else and and every one of those services has its own onboarding flow. So like a little different flavor than the payments flow we talked about but like it's a pretty inefficient fill out a bunch of steps.

**39:55** · Um and every one of them just like the payments flows was designed for like you and me as humans sitting down and clicking through this like weird setup wizard thing. Um, and I don't think it really bothered any of us that much because we weren't doing it that much because the hard part was the coding part. But now that like the app could be built in coded in 20 minutes like okay the long pole is deploying the thing. Um, and so anyway, vibe coding was easy. Vibe deployment um has become like more of the binding constraint.

### Why Stripe built Stripe Projects for agent deployment

**40:27** · Um, and so we actually we we recently like in the last couple months uh launched Stripe projects for this. Um, but basically it's like agents should be able to um well sign up for and configure and integrate all of the services they need to deploy an app and they should be able to do that like right from the command line. And it's not just Stripe services, right? was like a whole ecosystem of like you get like Verscell and Superbase and Cloudflare and Twilio like whatever you need Clerk.

**40:58** · Um I think we announced like 16 more partners a week or two ago now.

**41:03** · Um and anyway there's a lot of enthusiasm from the ecosystem because it turns out that everyone kind of has the same problem. Um uh developers all have the same problem which is now like the long pole is like the deployment and businesses have the same problem which is like their onboarding was designed for humans and now they need it uh to work for agents.

### Why Stripe cares about orchestrating app deployments

**41:22** · And to bring it home why does Stripe care?

**41:27** · Okay

**41:27** · so I think there's a lot of things that Stripe cares about that on paper you'd be like why does Stripe care? I'm the the honest answer is we care because it was becoming the bottleneck. like the barrier to building is gone, but the barrier to deploying is like a real friction. And if you just zoom back like okay, separate from being a payments company, our mission is to increase the GDP of the internet, a big part of that is how do we get more companies off the ground and how do we help them get kind of their first dollar faster and scale from there. And so if a person with an idea can create an app but can't deploy it, they can't sell.

**41:59** · And so removing deployment friction directly obviously like expands um the the internet economy and you know you can think of it primarily as um like ju just just like orchestration like all we're doing is orchestration. So, um, if someone else wanted to and could and did orchestration, we'd be cool with that.

**42:20** · But we were like looking at the developers trying to get the thing live and we were looking at the businesses trying to get the thing like used by developers and we're like, okay, I think we can we can make this market uh a little bit smoother.

**42:32** · Yeah.

**42:32** · And to play back orchestration because you have all these partners. So ultimately you do hosting observability uh email Q secrets all the things but that's provided by different uh vendors and you provide the glue to make sure that people can deploy their agents safely and efficiently.

**42:48** · Yes. Exactly. Exactly.

### How tokens break the traditional SaaS billing model

**42:50** · Very cool. All right. So that's vibe deployment. Tokens as money is uh also a fascinating topic. It's like taking it from the the the top. What does it mean to monetize tokens from a Stripe perspective? That's a big question because what does it mean to monetize tokens from a world perspective is kind of like okay actually how's the whole next generation of B2B and some B TOC

**43:11** · going to monetize look like the the the last kind of decade plus of SAS uh had like pretty beautiful and simple to monetize economics right and in particular with SAS like you build a product once and then you get one more customer and it costs you basically nothing to serve them like marginal costs are near zero and that's why SAS margins are really And that's why, you know, the fixed fee subscriptions or seatbased licenses work really well um in SAS.

**43:36** · Um AI, and I say AI generally because like you could literally be selling LLM, but you could also be selling, you know, some product that's a wrapper or on top of LMS or a product that's heavily powered by LM and and requires a lot of tokens. Um it breaks that model because obviously every prompt and every API call and every task um has a a real marginal cost all of a sudden, which it didn't have in SAS. the inference isn't free.

**44:00** · And so you now have all these businesses where how your customers use your product directly determines uh whether you make or lose money. And that's a very different game. Um and uh you know from from our vantage point like part of what that boils down to is the need for usage based billing as really critical for AI companies.

**44:22** · like you need to be able to meter what customers are actually consuming in real time and then charge them um in a way obviously that that aligns with your with your underlying costs.

### Why AI companies are moving to hybrid and usage-based billing

**44:34** · And do you see from your perspective pretty much all the players in the AI economy from a vendor startup standpoint uh use usage based billing at this stage or is that still a mix between per seat and per usage? I see very few scaling or scaled AI companies that are still exclusively subscriptions or seatbased.

**45:01** · And I believe from my conversations with them that that is for the simple reason that the economics there don't make sense because you know you have some people that are uh using a ton and some people that are not using very much and these people cost you a ton and these people cost you not very much and it is very hard to separate the sheep from the goats and price them appropriately without a usagebased meter. That said, um many of those businesses have a usagebased offering, but it is complementaryary to what you can think of as like a fixed fee subscription.

**45:32** · So like a great example is lovable. When they launched, they had like a simple subscription through Stripe billing makes total sense. They were early, they're moving fast, they wanted to monetize quickly.

**45:41** · Subscriptions are also very familiar and easy for consumers. Um, you know, if you think about a lovable, like some of their uh target users are like not very technical, like how are they going to feel about like, oh, how should I reason about a token or a credit, right? Okay.

**45:57** · So, so they they started with subscriptions, but then as the as the company grew and and some of their costs grew, their billing needs evolved and uh they needed to charge at least somewhat based on actual uh token consumption.

**46:08** · And so what they did is a hybrid billing model which which actually we're seeing a large number of businesses especially businesses that have a BTOC component do where they have usagebased billing on top of their subscriptions. So customers hit some threshold you know and by the way many people have premium thresholds but then above that they often have like a fixed fee you know $25 a month or $100 a month uh up to some number of credits and then above that uh you you have usage based billing.

**46:33** · So once customers hit the threshold, lovable in this case charges like precisely based on the number of tokens consumed above that and you know I think that that that alignment is going to get a bunch of people in the door comfortable with subscriptions but then sort of your at at any volumes that matter your revenue is scaling very directly with like how customers are using the product and correspondingly with like how much it is costing you to provide that product. Um so customers pay only for what they get and you make sure you monetize uh for um for the underlying cost that you're going to have to bear.

**47:01** · And 11 Labs is another example like they went through the exact same thing literally like started with subscriptions they recently moved to this sort of pay go plan um and and this is just a pattern that we see playing out pretty much everywhere in the AI space right now.

### Streaming payments and real-time token tracking

**47:15** · Does billing change much uh once you start charging agents?

**47:20** · So uh I think so uh for a couple reasons. One is agents can consume at machine speed. And so even if you're like um even if you're doing a usage based thing, but you're like charging at the end of the month, by the time you've gotten to the end of the month, an agent can have spent I bet a human can too to some extent with agents working for them, but like especially an agent can have spent like an egregious amount.

**47:48** · And so actually um I think in the world of agents what we're going to see more and more of is real time metering like what have you consumed and real time billing which is uh actually what we have co-built between metronome so real time metering usage based billing for very complex models and tempo uh blockchain where um you know agents are uh consuming tokens in real time and uh paying down uh for the cost of those tokens.

**48:20** · And that's important because agents can buy machine speed. It's viable because uh of uh a bunch of the the infrastructure between Tempo and Metronome. Um and uh agents are happy to just like pay as they go in a very literal way. Plus, businesses need them to be paying as they go so that they don't uh rack up a bunch of spend and then and then go dark. Yeah, it's it's fascinating also in terms of downstream consequences for what it means for like finance and accounting and like systems that need also to move at that speed.

### The massive data challenge for AI company accountants

**48:51** · Totally. I mean we have a a revenue recognition accounting product and it's and it's uh mostly needed by I mean we we provide it to a bunch of people who a bunch of businesses who have traditional subscriptions but where there's the most acute pain is actually like traditional accounting in spreadsheets like does not work when \[laughter\] you have this just like like proliferation of rows because these are like microtransactions are are truly happening. Um, I also think it's changing uh what it means to be an accountant.

**49:23** · I I I will uh avoid naming the company, but I was talking to the sort of number two in accounting at a pretty successful AI company, and couplings were interesting. One is they were like a hybrid accountant engineer, which they needed to be because of the scale of the data they were dealing with. And two, they weren't doing like accounting in the traditional you and me sense of like just close the books. like they have to close the books for sure, but their job was also to find like weird anomalous stuff happening and I

**49:53** · was talking to them because they were like identifying some fraud patterns and wanted help with them. Um, but anyway, just just very interesting like okay, what is actually what does it mean to do accounting at like one of these AI companies? Definitely needs new tools, definitely needs new systems, probably a different different skill set. And then like what you're accountable for really isn't just closing the books. like looking across the the whole Revre stack and saying, "What does this tell me about the health of our business? What does this tell me about fraud abuse in our business? And what does this tell me about breakages in our product?"

**50:22** · Yeah.

**50:22** · All of which becomes a massive data problem that needs to be treated in in in real time, right? Hence the rise of the clickous of the world like whoever can process massive amounts of data in real time becomes the core part of the required infrastructure.

**50:36** · Okay.

**50:36** · You wrote somewhere about token theft and I wanted to make sure that we cover that. So what is that? What is token theft as a new form of fraud, I guess?

### Token theft: The fastest-growing fraud in the AI economy

**50:45** · Yeah, it's it's a new form of fraud. It's I think one of the most underdised topics in AI right now, maybe by a lot.

**50:51** · Um fraudsters have figured out that in AI um you actually don't really need to steal money or credentials. Uh you can just steal tokens. And tokens have real value, right? You can use them to build things. Um you can resell them on marketplaces. um you can wrap a new product on top uh without paying a scent and go and sell that real that new product. So kind of like resell, but it doesn't doesn't look like you're selling the subscription to the thing.

**51:20** · It looks like you're selling this other product that you've come up with on your own, but really in the back end it's completely powered by someone else's thing. Um and for AI companies, maybe this is implied by our earlier conversation on SAS, but like the risk is existential, right? If someone stole a little bit of your SAS, like didn't matter because it didn't really cost you anything on the margin. um when someone steals your tokens, if your fraud rate is high enough, the economics of your product actually um break really fast.

**51:46** · So anyway, because we um work with basically all the all the AI companies, we have this interesting front row seat into um what's actually happening and the fraud patterns um playing out. And right now um there's three and I don't think these will be the three forever because we've already we've already largely burned down these three over the last three months. Uh but new ones will new ones will pop up. But I think these three are just um instructive for reasoning about sort of the breadth of the space. Um one is multi-account abuse.

### The cottage industry of free trial and multi-account abuse

**52:12** · So this is like bad actors just like hammering your sign up again and again and again and again so that they can get those like new user credits. Um and the scale of this actually shocked me when I looked at the data. So like more than one in six signups at AI companies are this kind of abuse. And by the way that's also very confusing for the company. Like are these good customers? Who are these people?

**52:32** · But it's very expensive for the company cuz like I've spent a bunch of tokens on these free products for you know a relatively small number of people who are spinning up a massive number of accounts and actually uh consuming quite a bit of tokens. Okay, so that's like very very top of funnel. Another example I think is interesting is is free trial abuse. So these are like fraudsters come in, they create a free trial, they put down a payment method, um they they drain through like all of the credits, but they never have any intent to convert.

**52:59** · Um, and you know, free trial abuse has always existed in various forms across the internet, AI or not, but it's more than doubled on Stripe in the last 6 months, and most of that doubling is coming from AI and uh AI businesses. And just to give you a sense like uh how lucrative this is, like there's whole cottage industries built around it. So, I don't know if you've ever been marketed a free trial card. I was recently marketed one. It's basically like literally it's like, "Oh, you can like spin up free trial cards.

**53:28** · They expire in 24 hours, so you'll never have to pay." And like if you or I had one, we'd probably use it for like some legitimate purpose to try out a service and just not have to go through the pain of cancelling, but like literally fraudsters can just like explode these things and spin up a bunch of free trials and spend a bunch of tokens um with no intent to convert. Um and then the third is is a little further downstream of this which is basically like we talked about the usage based uh billing. Folks are racking up like thousands of dollars of uh costs and then being build at the end of the month uh and never paying.

**53:59** · And so like whatever the dine and dash that happens in restaurants is like a d and dash um but it's but it's for for tokens and unfortunately at that point again this is AI not SAS so like the company has borne the cost uh of of those of those tokens and sorry if that's obvious and I guess I would be a terrible fraudster because it's not even super obvious to me. So uh if I get tokens for free what do I actually do with them?

### How fraudsters monetize stolen AI tokens on the dark web

**54:26** · So I guess if I get tokens from a general purpose LLM like claude or chat GPT I could see what I do with it. If I if I go to a cursor or lovable or 11 labs what is it that I actually do?

**54:41** · Yes.

**54:41** · Exactly. Okay. So what you do with it very much uh changes based on like what's the service like what exactly were these were these tokens uh meant for? Um you to you nail on the head for like oh yeah you just like get the tokens from the the underlying LLM.

**54:57** · Fine. um for those sort of um businesses that are a layer above that a bunch of resale abuse. So, uh you literally sell it sometimes in other markets uh for a slightly discounted price uh a discounted price on the base price that you should have paid but you didn't pay.

**55:13** · So, there's a dark like a dark web of marketplaces where you say like use a cursor or lovable for $2 but my my cost is zero therefore I make money.

**55:24** · Yeah.

**55:24** · Exactly. So, so just say I give you my login credentials whatever. Um there's also but but then there's just like there's just this like uh longtail makes it sound small but uh uh very domainspecific fraud patterns. So for example um people steal tokens to create content that they then use to extract money in all sorts of scammy ways.

**55:46** · So, a simple example, uh, we see people going in and like mass generating music tracks and then uploading them to Spotify and Apple Music and then getting fake streamers and then collecting royalties.

**55:59** · Um, or then for like basically all of the rapper businesses, there's this whole other layer of rapper on a rapper where like rather than just resell the subscription on places like Telbal, they'll like literally clone the AI company, right? You can just like vibe code a website. The back end is just like spitting out exactly what you got from the service that you're stealing from and then you like sell the product as yours. Uh but cheaper.

**56:21** · Are you gonna give it to people that they're creative? I mean that sounds almost harder than starting an actual company.

**56:27** · Yeah.

**56:27** · I I don't know. I mean a bunch Yeah, they they definitely they definitely put a lot of time into it.

**56:32** · Tokens are also very valuable. Um and you know what's been what's been interesting as we sort of started seeing these trends uh maybe at this point six nine months ago in various flavors but then they they escalated a bunch you know talking to AI companies AI company I mean the the large AI companies are all over this like it's like one of the most existential things for their margins they uh have been like in the trenches with us identifying the issues they have been like you know we we literally like we see a problem we build a model.

**57:03** · We like, you know, multi- account abuse. Okay, like at the time of login, there's an API. You send us what you know, we send you back a score, you block if they're bad. At the time of free trial start, same thing. As people are accumulating usage, uh, you send us all the metadata, we send you back whether they're fraudy, and you can require a top up or cut off service or whatever. Like literally each of those as we've seen them, we've like order of weeks gotten, you know, generally this isn't even like a full-fledged product.

**57:27** · It's like an API like you send us some stuff, we send you some stuff. Um and the adoption has just been like okay so that the AI companies are are are all over this. I think what's interesting is um there's like every company is going to become an AI company and I don't think the industry at large is thinking about this yet or has really even reasoned that like actually most of the fraud that's happening is not traditional like credential or payment fraud.

**57:53** · It's like what we would historically have called like firstparty abuse, right? like resale abuse or account sharing or multi-accounting or free trial. It's like first party abuse. Um, and I think it wasn't that first party abuse didn't happen before. It's just at least in sort of sassy stuff, first party abuse didn't cost you anything. And so, a, it wasn't that useful to get like a little bit of Salesforce for free for, you know, the examples we talked about wouldn't be relevant in in most SAS.

**58:22** · Um, and and B, uh, even if it was useful to figure out a way to like skim off the top, uh, and you could get a little bit of of profit for it as a fraudster, it didn't actually cost the business that much because their marginal cost was zero.

**58:37** · And so, you know, as every business becomes an AI business, I think uh we've we've been um in the context of our work on on radar really reasoning about our um fraud prevention product as moving from transaction to full customer life cycle and moving from traditional fraud to endtoend abuse. Um um but I don't think like the whole industry is is there yet. And you know, you and I talked about much of the economic upside of AI, but I think that'll really only be realized um if it can happen safely.

**59:09** · So, for example, six, nine months ago, when I talked to some of these AI companies, they they'd be like, "Oh, I know. I'm going to solve my free trial abuse problem by cutting off free trials." Like, I'm going to solve my free trial abuse problem by only having a sales sold motion and only going after enterprises and not having PLG and right. And like, you know, I hear less of that today. Why? Uh not because the fraud's totally solved, but because um everyone knows they need agents to also be their buyers.

**59:39** · And if agents are going to be their buyers, they better have a self-s served motion. They better have a PLG motion. Like there's no way they want to siphon off that source of growth. Um and sort of only double down on like a highly secure sales sold motion. But um it's been it's been interesting to see what's happened with token theft. I I totally agree. The fraudsters are are creative, but I think that's like a manifestation of how valuable the tokens are. Uh and so I actually don't think that creativity is is going anywhere.

### How Stripe Radar uses network density to fight AI fraud

**1:00:07** · And radar is one real time and two presumably entirely AI driven as well. It's like AI fighting AI kind of a kind of thing.

**1:00:14** · Yeah, it's real time, it's AIdriven. And then I actually like most importantly here uh for its like differentiation, it just looks across the stripe network. So like there's basically no good AI buyer.

**1:00:26** · we haven't seen before and there are very few bad AI buyers we haven't seen before and so uh that combination um you know it's it's yes the size of the network and this 2% of global GDP uh flowing through Stripe but really when it comes to AI it's the density of the network and we talked about link briefly but to give you a sense like uh lovable is a good example as an AI company 58% of lovable's volume flows through link like link is like uh you know link is an

**1:00:54** · extremely dense network when when it comes to AI and so you know you can sort of extrapolate away from there but if if we know who all the good buyers are uh and we've seen the bad guys be bad somewhere else um then combine that with yes AI and sort of these sort of real time um these real-time APIs and you get

**1:01:14** · uh pretty good fraud defenses you mentioned tempo at some point should we cover tempo like is is how relevant is tempo to the gentic commerce conversation so I think there's there's a couple um components of our work with Tempo that I think are uh really interesting. So um

### Tempo's role in the Agent E-Commerce Protocol

**1:01:32** · when you think about Egentic Commerce on the business side, we launched the machine payments protocol or MPP and we built it with tempo and it's an open standard and the way it works is um quite elegant, right? like an agent requests access to a service um and it can be whatever an API or an MCP server or whatever and then the service responds with a payment request and then the agent pays um and there's no kind of account creation or checkout UI or human in the loop or sort of the way you and I would traditionally um engage on the internet.

**1:02:02** · It's just this very kind of machine readable standardized way for agents to to buy from businesses. Um and that is really uh MPP is really the primary uh mechanism that we're seeing businesses use uh for kind of agents agents as buyer. Um the other uh collaboration with uh with Tempo that I am um super bullish on is is more related to to fraud.

**1:02:28** · Uh because you know agents are increasingly becoming the users of AI products and agents can burn through tokens very very quickly. And so we were talking a little bit about this like uh dichotomy that a business faces where either you can like siphon off self-s serve and be uh really safe but grow slowly or open it up including to agents but then like you know be putting yourself at risk of for quite a bit of abuse and uh monetary losses. Neither of those is great.

**1:03:00** · What you actually want to do especially when the agents are the buyers is you want to um track the tokens as they're consumed. And you mentioned the infrastructure. You want to track them in real time at sub substantial scale. And then as importantly, you don't just want to track them as they're consumed. You actually want to like collect payments as they're consumed. And so, uh, we call the streaming payments. Um, and it's what Metronome and Tempo, which is this, you know, blockchain optimized for payments that Stripe helped co-uild are are making possible together.

**1:03:28** · And so just metronome's job is like track the usage in real time and tempo's job is just enable this like fast lowcost highvol microp payments um that settle instantly obviously they settle in in stables and so put together it's like AI companies um can charge generally agent buyers as tokens are consumed um instead of having to choose between kind of um closing off business you know uh or or getting stiff on on the invoice.

**1:04:00** · So, um we we've uh yeah, we're we're very bullish about Tempo and stables in general in in the agent economy at large and for the purposes of uh of agent commerce.

### The AI startup ecosystem is accelerating business creation

**1:04:12** · Super interesting. All right. So, perhaps as the last topic, you guys have all sorts of interesting stats about the AI economy in general, but like in particular AI startups. Uh I think we covered some of that um la last time.

**1:04:25** · What have you seen in the last year in terms of AI startups? uh trends and facts and growth rates. What have you seen?

**1:04:33** · So, it's interesting when we when we talked last year, we talked about uh the growth of AI startups and uh how they looked different than traditional startups. And what I would say today is like, you know, there's definitely a delta between AI startups and non-AI startups. But what's more striking to me is how AI is just changing the startup ecosystem generally. Um and so you know in the vein of vibe coding and vibe deployment and all of that like uh new business registrations are um well so I think in general the the business formation story is underappreciated.

**1:05:05** · So um new business registrations are up basically around the world at least for advanced economies they're up um like 40% in the Netherlands and 70% in Finland and 80% in France. Um and so there's this sort of like surge in dynamism that like yes we see and feel in here in the US but it's happening um across advanced economies. When we look at this with the stripe lens um the pace of new businesses launching has doubled since we talked last year.

**1:05:32** · Um and not all those businesses are AI businesses but um many many of them were uh made possible because of because of AI. Um and they're not just getting started they're also scaling. So like Atlas is our um product for founders to incorporate and Atlas startups from the 2026 cohort and you know it's only June so it's early in their life cycle but they're tracking to like five times the revenue of last year's class at at these same um number of months. five times.

**1:06:04** · Five times. And some of that is there's more of them, but a bunch of it is they are getting to their first dollar faster and then they are scaling up more quickly and getting to their first dollar faster. A lot of that is for sure AI and then scaling up more quickly um uh that you know there a big part of this is actually how they're going global. And I don't know how much of that is AI or not, but like sort of the old model people had was you get big and then once you're big, you deserve to go global.

**1:06:33** · And what we're seeing with like increasingly over the last year is you literally go global from it doesn't lit necessarily literally mean every country, but it's like you're in dozens of countries on day one like your launch day. And that is how you get big. You get big by being global. And so uh I guess we're talking about AI. So I could use like emergent labs as an example. Um right AI platform for um you know you build and deploy these kind of full stack apps. So they were founded in 2024 in the US. Um 70% of their revenue um comes from international sales.

**1:07:07** · Uh and they do material business in um 16 countries. Like a substantial share of their revenue comes from many many countries. Anyway, I I think there's this sort of like yes, there's AI companies and, you know, it's moved from, you know, just being sort of the underlying providers to like a lot of rapper businesses, proliferation of rapper businesses across every single vertical. But I think what's kind of more interesting from the tops down macro perspective is just you used to have to be a developer to be a builder and therefore build a business.

**1:07:35** · Now you kind of have to have an idea plus vibe coding plus vibe deployment plus reasonable economic infrastructure. And then you know we see this proliferation of um new businesses and they um aren't

**1:07:52** · uh uh their their development is not easily arrested right like they even with one employee they uh you know start monetizing early they um grow quickly they uh expand across a bunch of markets and um I think that's almost certainly helped by all of the operational work that can also be done with AI which is less in sort of the day-to-day core wheelhouse of Stripe.

**1:08:15** · We help with some of that on the accounting or revick or whatever, but um you know much of the customer support and other operations are are obviously done by other businesses. Um but I think it's an interesting time and there's a lot of discussion of like is AI going to lead to a small number of firms um with heavy market share and not a lot of competition. And I think one of the reasons I'm bullish on the AI economy is at least so far for sure there are big guys who have things that are highly complimentary to AI. We \[laughter\] don't need to go through that list.

**1:08:46** · Everyone knows them. Um that are exploding but there's also an explosion of little guys coming in the market and uh not just being created but like reaching customers and growing quickly. And so I think that bodess well for for competition and for and for economic growth. All of this is obviously extremely exciting, but since we talked about um token costs and uh you know

### The token cost shock: Are buyers getting carried away?

**1:09:09** · usage base and all the things, do you worry that like a part of this is a little bit people uh on the on the on the buying side and on the usage side got a little carried away quite didn't quite realize the dollar amount that uh using AI represented and that there might be some kind of backlash against that hyperrowth. So, I mean, we've all read the stories of companies who have accidentally gone bananas on token spend because they had like no control over what their employees were doing.

**1:09:35** · I think the companies who have truly gone bananas are by and large the companies with pretty deep pockets, which isn't to say that it's not like going to be a problem in the economy if that spending continues. But there's smart companies that are well-run, well-managed. They can handle a month or two of poor decisions and runaway costs.

**1:09:51** · And um you know by and large I I don't exactly know what we're talking about at these companies but if we're talking about like I don't 2% 3% 4% of their headcount costs are going into tokens and uh 30% of that or 40% of that is inefficient I think they can like pretty quickly get back to an an efficient frontier and and it's not really anything existential.

**1:10:13** · Um for the little guys actually don't don't think that's happening. um you know many of them are sort of making fixed fee fixed fee purchases and they're still on small plans and and whatever. So I mean the stories are out there and by the way just to be clear like I think we have a

**1:10:31** · lot to learn about the efficient frontier of AI use and there's a component there around like model routing and what models you select for the job and there's a component around just like observability which I think many companies have find found themselves to be behind on and then there's just like um like norms and controls and guard rails and you know I think we all want high ROI uh usage of LLMs

**1:10:57** · Um, but we also want employees to know when they're, you know, racketing up really substantive costs and we want them to be able to tell us uh whether they anticipate the ROI of those costs is going to be there. So, yeah, I think there'll be like a little bit of uh uh recalibration, but I don't think anything existential has happened that's going to enol um the the sort of long run upside here.

### 2026 Predictions: Agents running businesses end-to-end

**1:11:19** · All right. So as a last question when we talk again in in a year from now where do you think we are uh in terms of agentic commerce maybe using uh you know L1 to L5 and I I won't hold you to the prediction but like directionally what do you think realistically is going to happen in the next 12 months?

**1:11:36** · I think the most interesting thing in the next 12 months is I mean I think we I think we'll move up and I don't know if it's going to be to four or to five but I I think the more interesting thing is actually that like we talked about agents as economic actors mostly in the context of buying but I think we'll start to see and I'm not saying this will be proliferated everywhere but I think we'll start to see agents that are like multiaceted economic actors.

**1:12:02** · They're buying and they're selling and they're provisioning infrastructure and they're running businesses. um and they're like doing the thing end to end.

**1:12:10** · And again, I don't know how many of these there will be or how they'll operate or whether it'll be like with each other or like in these like weird niche silos. Um but I think all of that's just going to continue to demand more purpose-built infrastructure including financial infrastructure versus just the sort of old um human centric commerce stack.

**1:12:28** · Um, and so that that's that's kind of where like what is what does it look like when okay I'm vibe deploying I'm I'm vibe coding and I'm vibe deploying and then uh my content \[clears throat\] is my offerings are default exposed and actually we just we just quietly uh went to to public preview on uh on Stripe directory which is just a really easy way for agents to um discover providers

**1:13:01** · s and then through stripe projects they can integrate them directly but like okay and then an agent's like also discovering everything and integrating it and buying it and then you know creating a service out of the combination of things it has provisioned and integrated and bought and is starting to sell a thing anyway like this this idea of like an agent as a micro firm um I think would probably be the most interesting uh thing to see 12

**1:13:29** · months from now And again, I don't think the median uh firm is going to be uh or forget a soloreneur, a what would it be?

**1:13:38** · A solo agent uh uh I don't think that's I don't think that's a world we'll live in. But I I think 12 months from now we could totally see some examples of that that sort of pave the path for hm like the the whole thing end to end. And you know this always happens with a new technology, right? You take like your current processes or market or whatever you have and you figure out how does the new technology make that 5% more efficient or 10% more efficient. It keeps me from having to type in my credit card number, right?

**1:14:05** · But like where it actually gets interesting is where um we start to reimag like how the system works. Um and it's not Emily permissioning an agent to buy on her behalf. It's Emily has an agent who's tasked with running a business and that includes buying some things and selling some things and making some profits and um that'll that'll be the world that I that I would like to be talking about 12 months from now.

**1:14:31** · Well, Emily, it's been another amazing conversation. Thank you so much. Really enjoyed it.

**1:14:36** · Thank you.

**1:14:38** · Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already, or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks, and see you at the next episode.
