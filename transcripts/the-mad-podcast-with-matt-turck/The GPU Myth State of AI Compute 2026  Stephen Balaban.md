---
title: 'The GPU Myth: State of AI Compute 2026 | Stephen Balaban'
source_url: https://www.youtube.com/watch?v=0NttU4CbyVs
video_id: 0NttU4CbyVs
account: '[[accounts/the-mad-podcast-with-matt-turck|The MAD Podcast with Matt Turck]]'
account_name: The MAD Podcast with Matt Turck
account_url: https://www.youtube.com/@DataDrivenNYC
featured_people:
- '[[people/stephen-balaban|Stephen Balaban]]'
published: 2026-06-18
created: 2026-07-23
language: en
speaker_attribution: contextual
description: Many people said GPU compute would become a commodity. The opposite happened — and a new category of "neoclouds" is now racing to build the physical backbone of the AI boom. Stephen Balaban, co-founde
tags:
- transcript
- kol
---
![](https://www.youtube.com/watch?v=0NttU4CbyVs)

Many people said GPU compute would become a commodity. The opposite happened — and a new category of "neoclouds" is now racing to build the physical backbone of the AI boom. Stephen Balaban, co-founder and CTO of Lambda, explains why the conventional wisdom was exactly wrong, why we're still massively underbuilding compute, and what it actually takes to stand up a gigawatt-scale AI factory: land, power, cooling, networking, and a financing stack most people have never heard of. We go deep on the physics of how energy becomes tokens, NVIDIA's real moat, why a 2023 GPU can lease for more today than the day it shipped, and Stephen's provocative vision of "neural software." Plus the wild Lambda origin story — from a facial recognition startup to a camera in a baseball cap to a near-billion-dollar cloud business. This is the state of AI compute in 2026, from inside one of the companies building it.  
  
Stephen Balaban  
LinkedIn - https://www.linkedin.com/in/sbalaban  
X/Twitter - https://x.com/stephenbalaban  
  
Lambda  
Website - https://lambda.ai  
X/Twitter - https://x.com/LambdaAPI  
  
Matt Turck (Managing Director)  
Blog - https://mattturck.com  
LinkedIn - https://www.linkedin.com/in/turck/  
X/Twitter - https://x.com/mattturck  
  
FirstMark  
Website - https://firstmark.com  
X/Twitter - https://x.com/FirstMarkCap  
  
Listen on:  
Spotify - https://open.spotify.com/show/7yLATDSaFvgJG80ACcRJtq  
Apple - https://podcasts.apple.com/us/podcast/the-mad-podcast-with-matt-turck/id1686238724  
  
00:00 — Cold open  
01:21 — Why GPU compute was never a commodity  
02:45 — The H100 price index and what it gets wrong  
04:02 — The real moat: technology or financing?  
05:57 — Winner-take-all, or room for many neoclouds?  
06:48 — Are we overbuilding or underbuilding AI compute?  
09:26 — What if AI gets 10x more compute-efficient?  
10:44 — The real bottleneck: land, power, and shell  
11:38 — The backlash against data centers — and the misinformation  
15:00 — Opening the hood: from photons to tokens  
17:11 — Extracting more value from the same chip  
19:26 — Frontier inference and distributed training, explained  
23:26 — What actually drives compute cost  
25:21 — Lambda's chip stack and the NVIDIA relationship  
26:17 — A multi-silicon world? CUDA, CUDNN, and NVIDIA's real moat  
28:59 — Networking, storage, and the one-click cluster  
34:46 — Renting vs. owning, and full vertical integration  
36:24 — How global is Lambda? Does location still matter?  
38:44 — The financing stack: off-take agreements, SPVs, and credit  
41:16 — Why a 2023 GPU leases for more today  
42:36 — A futures market for compute?  
43:54 — Origin story: facial recognition, Perceptio, and Apple  
47:03 — The Lambda hat and Dream Scope  
48:59 — The $60K bet that became a cloud business  
52:00 — Holding the team together through the hard times  
54:30 — Bringing on a new CEO; Stephen as CTO  
57:33 — Matching xAI on high-velocity deployment  
59:29 — "AI won't write software — it will become the software"  
01:01:30 — Neural software vs. vibe coding  
01:04:25 — Do agents change the compute layer?  
01:06:14 — Self-assembling software inside Lambda  
01:08:18 — Gigawatt-scale AI factories  
01:08:57 — One person, one GPU  
01:12:04 — Hot takes: overrated and underrated in AI

## Transcript

### Cold open

**0:00** · It's pretty clear that we have an amazing system that can take in money and output software. The people who are the naysayers, you're going to throw these GPUs out in 5 years, are completely wrong. They're completely wrong and they've been wrong the entire time. We continue to be generally underbuilding. Most people that are sort of in leadership positions at neo clouds or within the market have been recognizing this insatiable amount of demand for large language models to do everything from being to code generation.

**0:32** · We continue to see no end to the scaling laws.

**0:36** · Hi, I'm Matt Turck from FirstMark.

**0:37** · Welcome to the Matt Podcast. My guest today is Steven Balaban, co-founder and CTO of Lambda, one of the top neo clouds powering the AI boom. This episode goes deep on the physical layer that everything else in AI runs on. We get into why GPU compute was never actually a commodity, how you finance billions \[music\] of dollars of data centers and chips, why a 2023 H100 can be more expensive to lease today than when it was bought, and \[music\] what it actually takes to stand up a gigawatt scale AI factory.

**1:05** · We also cover Lambda's wild origin story, from a facial recognition startup to a baseball cap with a camera in it, to a near billion-dollar cloud business today. Please enjoy this amazing and very educational conversation with Steven.

### Why GPU compute was never a commodity

**1:21** · There was a moment in time in Silicon Valley a few years ago if you had asked most people they would have said that neo clouds were going to be uh a commodity uh in particular because GPU compute was going to get commoditized.

**1:35** · Uh and if you fast forward to today, it seems to be exactly the opposite. Both Lambda, uh but several of your competitors seems to be uh absolutely ripping. So, what is it that uh naysayers got wrong then and continue to get wrong today?

**1:49** · The big thing is that cloud compute is not a commodity service. It is a very complicated highly vertically integrated type of service that spans everything from land land entitlement construction HPC high-performance computing design

**2:11** · software virtualization cloud services on top and there's a reason why the biggest companies in the world these multi-trillion dollar market cap businesses whether it's Amazon Microsoft Google Oracle are all in the cloud computing business is because it's a great business. And so I think that's like probably the fundamental thing that was misunderstood is that oh this is somehow a little bit different than a normal cloud service but really what it was was it's a cloud service designed for the age of AI.

### The H100 price index and what it gets wrong

**2:45** · But there is some element of commoditization right the price of rental of a GPU is going down but what you're saying is that to some extent it doesn't matter because it's only one layer of the cake.

**2:57** · Yeah

**2:57** · so when you look at for example I I think it's like actually worth doing is to try to like kind of dig into some of the methodology on for example an index like there's there's the there's the index that's on Bloomberg for H100 rental prices and

**3:14** · what we're actually seeing in the market is that first of all there's two different rates there's a public cloud on-demand rate and then there's a long-term rental rate and I think that some of these in indices don't properly take that into account because what we're actually seeing is a very consistent if not increasing

**3:36** · long-term rental rate and very consistent and increasing on-demand rental rates and so what happens is if if if the index mix for example if the methodology in the index biases towards long-term contracts being a bigger part of the volume, that will look like a decline in the index when the reality is it's just a decline in the mix of the index is is method you know, the index is covering.

### The real moat: technology or financing?

**4:02** · Fascinating.

**4:03** · So, I'm curious about your thoughts as a key leading player in the neo cloud ecosystem about how you see the market evolve. How much of the competitive advantage that you guys are building and other players are building is based on technology versus a financing uh race?

**4:24** · There's a few different layers on it, which is there's a lot of differentiation and work that's being put into, for example, the cloud software orchestration layer, which allows us to, for example, take a very large-scale GPU cluster and partition it up for our customers. So, we've got, for example, our one-click cluster product that allows us to do that, and that's something that's like quite unique in the neo cloud space.

**4:48** · Most of the other neo clouds either don't have the ability to launch a cluster from their website or max out at, I'll say, 32 GPUs, whereas Lambda's designed a piece of software that allows us to give you anywhere from 16 up to, you know, 4,000 GPUs in a web interface. And um then there's innovation on the data center construction and design side of things, which is also really important, right? Because that's like the physical layer um underneath the high-performance computing equipment.

**5:19** · And you know, we're working on a lot of different ways to dramatically reduce the time it takes to construct and stand up new megawatts.

**5:30** · And then there's as you mentioned, innovation on the finance side of things, where, you know, we're coming up with new and unique ways to uh finance, underwrite, package these these these large-scale capital projects, really. And um so, I think it's like innovation happening on every layer of the stack and it's a it's a very complex coordination style business.

### Winner-take-all, or room for many neoclouds?

**5:57** · Yeah. And do you think that ultimately the new cloud ecosystem becomes a winner take all or is there room for multiple very large players?

**6:06** · I think it's I think it's absolutely room for multiple very large players just like the traditional cloud business has shown that there's room for multiple large winners and multiple large players. And I think that the fundamental reason for that kind of going back to well what drives I guess market structure and I'd say generally speaking when you have an industry that is has like technology modes and capital formation modes and economic modes that tends to be all the capitalistic in its market structure.

**6:37** · When you have markets that have more sort of network effect modes those tend to be a little bit more you know, single winner take all.

### Are we overbuilding or underbuilding AI compute?

**6:48** · What are the various scenarios in your head as you think about the future but how it all play out are we are we over building are we under building nobody knows how do you think about it?

**7:00** · I I think that we continue to be generally under building and and the most people that are sort of in leadership positions at neo clouds or within the market have been recognizing this you know, sort of insatiable amount of demand for large language models to do everything from you know, being an assistant to code generation.

**7:26** · You know, you you can kind of look back to some of the talks that I've that I've given in the past around I kind of called hey in a couple of you know, months to years we're going to be at a point in time where you can put money in and get software out the other end. And now at the at that point in time when you're predicting when I was predicting that, it was maybe not wide not as widely held of a belief.

**7:54** · Um but now with, you know, let's say with the release of Opus 4 or 5, I think it's pretty clear that we have an amazing system that can take in money and output software.

**8:06** · And the I think the the part which makes me feel so confident that there's going to continue to be demand is that we continue to see no end to the scaling laws, which are like the underlying idea that you put more compute in and you get better intelligence levels out of your models, you know, as you increase the capacity of the model and train it with more compute, train it with more data, you get more intelligence out.

**8:31** · And as long as that continues to hold, I think that we still have in store for us, it's hard to predict exactly when scaling laws might start to reach sort of a diminishing marginal return type of part of the curve. But um right now, it's very clear that we're going to continue to see more and more and more capable models that is a kind of expanding the cone of the addressable market, right? Like originally the cone of the addressable market was, all right, this is going to be helpful for customer support.

**9:04** · It's a sort of substitute good for Google search and for other search um online. And then now it's like, well, this is a substitute for a lot of software engineering roles or a huge augment to software engineering roles. And so as that cone expands, the total market and the demand for compute expands. And I think that we're continuing to underestimate it.

### What if AI gets 10x more compute-efficient?

**9:26** · Do you worry about model training and model inference becoming, I don't know, 10x more compute efficient and what that would mean in terms of the build-up?

**9:33** · I think that generally speaking, what you're seeing is that if if let's say you do become 10 times more efficient, I think that that just means that everybody is able to process 10 times more tokens and there's there's still the same fixed amount of compute in the world at any given point in time.

**9:50** · And so in the early days, it's funny, we used to talk a lot about this back in let's say 2017. Oh, well, maybe there's going to be a some new type of model, let's say, that will look more like a random forest model, which the audience might some some members of the audience may know. You can kind of train a random forest model on a MacBook, right? And there was there was this concern that was kind of persistently raised around like, well, okay, what happens if the you have this sort of like um adjacent disruption on the model side of things.

**10:20** · And so far we haven't seen that and again, everything that we're building towards is sort of based on these scaling laws, which is really about scaling up at the this architecture. So um I don't really foresee a very likely outcome where we have this huge model disruption that would cause uh a a decline in the demand for compute.

### The real bottleneck: land, power, and shell

**10:44** · Where's the main bottleneck these days uh that you're experiencing uh building Lambda Lambda Labs? Is that uh GPU power, electricity?

**10:54** · So um I \[clears throat\] always say that bottlenecks are always like kind of local before they're global in terms of, you know, one one development might be bottlenecked on, let's say, generators or on UPS systems. And that's a function of like the sort of idiosyncrasies of the site.

**11:10** · But broadly in the industry, the thing that is the main bottleneck is basically land power shell, which is basically land that is entitled to have a certain amount of megawatt commitment from a utility and um then of course the data center and the mechanical, electrical, and plumbing equipment, the MEP equipment that goes into that data center. Um and so that's the main bottleneck that we're seeing in the industry right now, I'd say, across the board.

### The backlash against data centers — and the misinformation

**11:38** · How real is the movement against data centers from the the the global community and how do you think about uh how to respond to it?

**11:47** · Well, it's certainly it's like very popular in the news right now. I'd say that um it's definitely very real. I mean, I think that rightfully communities that host any type of large capital project, whether it's a power plant or a uh solar farm or a data center or a distribution center, right?

**12:11** · Those communities want to have a seat at the table. I'd say in general though, I spend a lot of time reading through a lot of the comments from communities and people want jobs, they want tax revenue.

**12:25** · Any major capital development is going to bring a lot of tax revenue and it's going to bring a lot of jobs and it's going to bring investment into their community. And what they really are voicing, I think, is one is having a seat at the table while while this stuff is, you know, being developed. I think that's an important thing is just to have their voices heard and that that the developers coming in and actually understanding the community. The other thing is to kind of I think keep in mind is that there's a lot of misinformation out there.

**12:57** · So, for example, every single modern deployment of, let's say, a Blackwell class or uh Reuben class GPU, you know, the VR GBNVR GPUs, um these are often times in a closed directorship liquid cooling system that's connected to a dry cooler, which means that there's almost zero evaporation. It's not using evaporative cooling. It's using a dry cooler system that does not consume a lot of water.

**13:28** · Um and on top of that, most of these data center developments are bringing a ton of power to the grid. They're either standing up behind the meter power, they're standing up and bringing battery electric storage systems to the grid, and they're bringing all these like sort of ancillary benefits that strengthen and fortify the grid and also, you know, eventually in the long term will maintain the costs that are being experienced by the community.

**13:50** · And so, I actually think that there's a very clear path towards, um you know, maybe spreading more of that the facts around what does a data center bring, um because there's just a lot of misinformation. You'll see people talking about how data centers consume a lot of water. Well, an evaporative cooling tower might evaporate a lot of water, but practically no new builds in the United States are using evaporative cooling uh for doing the these closed-loop direct-to-chip liquid cooling systems.

**14:23** · Do you think we do a terrible job as an industry explaining this to the broader world? Cuz like these things keep coming back and they seem to be accelerating, but then when you have the discussion, this from a technical standpoint, a lot of this is just simply based on the misinformation, as you just said.

**14:39** · I think that everybody's trying to get better at that kind of communication. Um and it just takes some clear thinking, writing down what are the benefits, writing down what are the costs, and presenting that clearly and plainly to a community so they can make a good decision about, you know, what kind of jobs and what kind of development they want in their communities.

### Opening the hood: from photons to tokens

**15:00** · Let's open the the hood for a minute.

**15:03** · People talk about things like flops and GPU hours and tokens and MFU. What is the the best way to think about a compute unit?

**15:13** · Yeah, it's interesting, you know, you said a few different terms, and I I always like to kind of break it down from like a physics perspective into like the SI terms. So, okay, on the the left-hand side is all of the energy production and then on the, you know, my right-hand side is sort of tokens being consumed by by by somebody. And um you know, maybe you can even have the application layer on on the far right of that that's using the token.

**15:38** · So, on the left-hand side you've got either photons coming in per second or molecules of natural gas coming in per second. And then that through a power plant or a solar farm gets converted into joules per second, which is um a measure of electrical power production.

**15:59** · And then the joules per second, obviously, in engines there's a level of an efficiency and that's a engine efficiency. It's interesting because like the MFU percentage is kind of like an efficiency up on the higher end of that chain. The power plant or the solar plant then converts that into joules per second, which is watts, which is consumed by the entire data center. The data center itself, um you know, needs to cool itself and that's the PUE and that's actually the the efficiency metric that you can use to measure a data center on.

**16:32** · And then you put the servers and all of the different networking and storage gear in and that's producing floating point operations per second or flops per second, okay? That is what gets consumed, the flops per second capacity is what gets consumed by, let's say, a model builder when they're training a model or when they're inferencing a model. And that gets turned from flops per second into the tokens per second.

**16:56** · Then on top of that tokens per second you might have some level of efficiency that the end customer is actually, you know, turning those tokens into real actual intelligence. That's like the entire pipeline, I I would say from end to end.

### Extracting more value from the same chip

**17:11** · Uh super helpful. If two companies have the same chip fundamentally, how do they extract more value from it? What what needs to happen to maximize the usefulness of that chip?

**17:23** · If you look at the cost structure of let's say one GPU hour of time, you know, we we're talking about H100s, the the largest part of that cost structure is the depreciation that is associated with that GPU hour. And um basically you can think of a utilization metric as being like kind of a multiplicative factor on that. So one over the utilization.

**17:48** · So if you if you use your capital asset 50% of the time, you will have on a per hour basis twice one over 0.5 the amount of per hour depreciation expense associated with that. And so I think that the number one way that companies are you know, sort of gaining a unique advantage is well, how can I build a cloud product that is beloved by people that is going to drive a high utilization.

**18:19** · And um you know, in addition to that the market as we mentioned earlier for on-demand compute basically the retail pricing is obviously much higher than the wholesale pricing. So the retail is like on-demand spin up a GPU, spin down a GPU normal cloud service. The wholesale is sort of buy in 10,000 GPUs for 5 years for example.

**18:42** · And so one of the things that we do at Lambda is really try to figure out, hey, how can we sort of get the most dollar utilization and percentage utilization out of the capital deployments that we do. And that's that's by making great cloud software that makes it easy for somebody to spin it up and down. So for example, if you don't have that cloud software, you can't rent, you can't extract a retail pricing, Right?

**19:10** · You know, you cannot rent it out to somebody for an hour because you just simply don't have the means to be able to do that. And actually, a lot of Neo Cloud are in that position where they they don't even have the infrastructure to be able to run a real Cloud service.

**19:25** · So, you have GPUs, but like a a big part of how those data centers work is transforming GPUs into networks of GPUs.

### Frontier inference and distributed training, explained

**19:34** · Do you want to explain at a high level how that works?

**19:37** · The general idea is that you've got a large-scale high-performance computing cluster of a bunch of you know, let's say Nvidia GB300 NVL72 racks. That's 72 GPUs all networked together via NVLink. And then, there's a connection between the racks that's either InfiniBand or, you know, high-speed Ethernet.

**20:00** · And that is a essentially what's called a spine-leaf topology, which is basically a way to say, "Hey, this is a completely non-blocking. Every port on every GPU can talk with every other GPU in the network. It's fully connected and it's able to provide maximum bandwidth between every individual GPU. And that cluster is useful for training large models.

**20:31** · It's also useful for inferencing. So, frontier inference, as we sometimes refer to it at Lambda, is basically, you know, very much a distributed inferencing problem where they actually will, you know, fragment or shard the model. There'll be some sort of sharding strategy for the model where it can be essentially run on multiple GPUs and it uses and that high-speed InfiniBand or Ethernet interconnect to to do that communication.

**21:03** · And so, what is a frontier inference? Is that inference for the most advanced reasoning models like the more demanding jobs.

**21:11** · Yeah, well well you know, it's not necessarily associated with reasoning models so much as like just a very large frontier model that is, you know, kind of the domain of let's say three companies in the world or four companies in the world when they're doing their inference. It's a very complicated thing that is is fully utilizing all of the interconnection that's available.

**21:33** · And what you described for frontier inference is that conceptually the same thing as what happens for training this concept of just distributing a task massively across a bunch of GPUs. What happens during a training run from a compute standpoint?

**21:48** · Generally speaking when you're doing a training run, you might think there might be some sort of split between the backwards pass and the forward pass on the model. And the backwards pass might be let's say 2/3 or more of the compute and the forward pass which is basically the same thing as inferencing is, you know, the remainder.

**22:05** · And one of the realizations that I think has been made over the last bit of time is that the type of infrastructure that you'd want for uh doing a large-scale training run can be reused to do the inferencing of that model.

**22:23** · And um what I mean by the sort of frontier inference and the fact that the inferencing is being done in a distributed way, you know, you'll have like a mixture of experts model and they'll be a different basically starting strategies for how you put those experts onto different servers and to different GPUs.

**22:46** · Um and you know, the models can be very large. They may not fit on one single uh rack or you know, they may not fit on one single server. They they might they might need to be distributed across different servers to even just do the forward inference pass. And so, that's where sort of distributed frontier inference kind of comes into the picture. Right? Because like if you're doing a small model, let's say Llama, that the users might be, you know, familiar with or uh so some of the quantized small models can fit on a single GPU.

**23:19** · Mhm. Mhm.

**23:19** · Okay? Well, let's just say that like Opus and ChatGPT 5.5 can't fit on a single GPU.

### What actually drives compute cost

**23:26** · And when we think about compute costs, what what costs the most money? Is that model size? Is that memory bandwidth? Is that latency?

**23:37** · Does context window and like those very very large context window do they change anything to the compute cost? What what costs the most money?

**23:44** · As I mentioned, like the biggest component of the unit cost for a cloud service like this is the depreciation expense.

**23:52** · And within that, you know, is basically some sort of bill of materials for the servers that are in the data center, which is by far and away the biggest portion of the cost. If you were to talk about the capital stack, let's say, you can go back down to power generation, 2 to 3 million dollars a megawatt, 2 to 3 billion dollars a gigawatt for power plant.

**24:18** · The data center is between 10 and 15 billion dollars a gigawatt for building the data center. And then the compute, the servers can be anywhere from 35 to 45 billion dollars a gigawatt. And within that that so so you can see the server portion is obviously by far and away the largest. And that's like a big part of the depreciation expense.

**24:45** · And then the within that, obviously, you have um the sort of server and cluster bill of materials, which is primarily the GPUs.

**24:58** · Um if you were to kind of break down Nvidia's bill of materials, then, you know, you can kind of get better allocation towards where those costs are coming from. But certainly in the most recent period of time, memory expenses, you know, memory has gone up a lot in price. And you know, there's there's very few vendors, right? You know, for HBM memory, it's Samsung, Hynix.

### Lambda's chip stack and the NVIDIA relationship

**25:21** · So you guys are a big Nvidia shop.

**25:25** · To precise level, you mentioned some of the names, but like which chips do you use mostly? What's your kind of chip stack?

**25:32** · Yeah, so Lambda really loves Nvidia's products. I mean, they're the the only server provider, the only chip provider that is available in every single major cloud platform, which is a huge platform advantage. And we stuck with the Nvidia sort of ecosystem for all of the chips we've deployed. And we've got everything from V100s, A100s, H100s, H200s, B200s, GH200s, or GB200, B300s, and VR200s coming soon.

**26:10** · And so we, you know, use everything in the in the in the ecosystem.

### A multi-silicon world? CUDA, CUDNN, and NVIDIA's real moat

**26:17** · Do you think that today or in the near future we're going to be in a multi-silicon kind of world? Is there like room for different players beyond Nvidia?

**26:27** · Well, I mean, I think that we're already in a world where there's a huge amount of competition from massive, massive multi-trillion-dollar companies, and they're all trying to fight for the same thing, which is to be the best chip in the world for running and training neural networks, essentially. Nvidia's built a great product that has gotten a lot of distribution and has a great platform of developers who love what what do. And you have to take into account not just the cost of the chip, right?

**26:55** · The price of the chip is one aspect, but, you know, you have to take into account the entire software ecosystem and what's been developed. So, one of the big People talk about like what's Nvidia's moat. One of the big moats they've got is just the cuDNN stack. It's not just CUDA.

**27:11** · It's, you know, CUDA is, sure, that's like the water we all swim, but like cuDNN has got so many, you know, matrix multiplication routine optimizations baked into it.

**27:22** · What is cuDNN for everyone to understand?

**27:24** · So, cuDNN is the It's CUDA deep neural network library, and it's basically Nvidia's You can think of it like a highly tuned engine for matrix multiplication. And basically, if you were to just sort of naively implement the matrix multiplication algorithm, you would maybe get a certain level of floating-point floating points uh per second.

**27:49** · But, they've gone and tuned every single aspect of it, and, you know, come in and do Winograd filtering or, you know, a bunch of different algorithms that you would apply to speed up matrix multiplication.

**28:02** · And cuDNN means that, you know, you don't have to go and do the optimization yourself. And so, like that's that's one aspect. The other one is uh NCCL, which is their networking optimization library, where it will sense the topology and the connected nature of your um network, your InfiniBand or your Ethernet network, and it will suggest an optimized sort of routine for doing

**28:31** · uh you know, reduce all and broadcast the different what what are called OpenMPI primitives, which are used for that sharding that we were talking about for both training and for inference. And so, that's like the kind of software stack that I think really is hard for a lot of the new entrants in the chip space to overcome. I think we're already, like I said, we're already in a world where there are multiple options for silicon, you know, the biggest labs in the world are using multiple different types of chips to do their inferencing and training on.

### Networking, storage, and the one-click cluster

**28:59** · What would be a plain English definition? We talked about the chips, but like the rest of the stack, the networking and the storage, just walk us through how it works.

**29:09** · When you're running a cloud service, one of the things, you know, you'll you'll train your model or you'll upload your trained model and you're you're ready to start doing large-scale inferencing. Well, you're going to need a place to put your data, whether it's the data that you're using to train with or whether it's the data that's coming in and streaming in from your end customers. And so, having high-speed storage is like a really important part of it.

**29:34** · And so, Lambda offers the the basically AI-optimized file system service that is significantly faster than like your standard, let's say, cloud file system, which is maybe more of a traditional NFS type of thing. This is like a highly optimized parallel file system that's designed for high-performance read and writes, and mostly high-performance reads, so that's like the kind of most of the workload.

**30:01** · And that's something you built in-house completely?

**30:03** · We have I mean, it was in-house completely.

**30:07** · Right, it's like you have to ask the question of like, what what is the definition of in-house completely, right? You know, like we've never spun a PCB at this company. We have not authored, for example, you know, we use KVM QEMU for our virtualization, for example, right? And so, you know, well, we we have both commodity off-the-shelf hardware that has software installed on top of it for our some more storage.

**30:30** · We have some storage partners that we work with as well, but, you know, generally speaking, everything that we do on the cloud, I would generally say is is something that is like we we rolled it ourselves with the help of the broader ecosystem because again, there's no such thing as rolling it yourself unless you're like, you know, mining um you know, ultra-pure silicon from some \[laughter\] like, you know, and then coming up with your own ASML. You know, it's like it's it's funny.

**31:02** · Yeah, yeah. That's the highly optimized storage. What else?

**31:08** · The networking part and what other pieces?

**31:10** · so I was talking about this one flow cluster product that we've got and the the way it is for everybody to think about this is like, okay, well, look, you've got a bunch of GPUs. Let's say you've got a cluster of 10,000 GPUs.

**31:26** · Well, I want to partition that cluster up and so what it is is it's a bunch of GPUs, it's some CPU servers as well cuz you need to have an orchestration fleet as well. And then you've got some storage.

**31:40** · And um all of the CPU servers and the storage servers and the GPU servers are interconnected with the the storage so they can quickly read and write from it. And so there's and and that that communication happens over what's called, you know, the in-band network. And then there's the compute fabric which is where I was talking about where all of the sort of weights and feature activations are being shared throughout that compute fabric.

**32:08** · And then there's an out-of-band monitoring network where you've got access to whether it's BMC or some of your DPUs and when you are trying to create a sub-partition of a 10,000 GPU cluster, you need to simultaneously partition the in-band, the out-of-band, and the compute fabric.

**32:28** · Okay, so like that complex coordination between we've got a bunch of bare metal systems to hey, we've got a virtualized system that has you know, what's called RDMA, you know, RDMA remote direct memory access that allows them to read and write quickly not just from the disks, but from each other's memory.

**32:49** · The GPUs uh sort of HBM memory and allow them to do that um that sort of direct memory access allowing it to go directly from a GPU to another GPU without getting copied to the CPU, for example.

**33:05** · Having that all work is a immense immense software undertaking. And um And and and this is I going \[clears throat\] back to the original question is like, well, what are the people not getting about neo clouds?

**33:19** · Well, first of all, the answer is that most neo clouds don't have this kind of technology. Most neo clouds have not made the really it's like kind of high tens to hundreds of millions of dollars of software investment that you need to make to build a real cloud system that can partition a high performance computing environment like this.

**33:40** · And um so like that is um and then to have it all work with the storage. Anyways, I guess that that sort of summarizes the steps that you need and kind of you can think about all the different moving parts of a modern like how does an AI data center work? People tell I what AI data center, but really you have to kind of go down that one next level down which is cuz if you were to By the way, if you were to ask an AI data center landlord a traditional one Yeah.

**34:11** · what what's going on inside of the data center? They'd be like, well, look, we're real estate people and you know, we well, you know, we we really outsource this to the GC, but like the GC doesn't know, of course, anything that's going inside and this is then they it's their tenants who know. So, this is what's actually happening inside of an AI data center. And then it serves the the result. Like, also going back to the community stuff, if people knew a lot more about like, well, this AI data center is actually just serving the chat GPT requests that I'm that I'm giving it, right?

**34:41** · Like, sometimes they don't even realize that that's actually what an AI data center does.

### Renting vs. owning, and full vertical integration

**34:46** · So, you mentioned tenant. Do you rent them? Do you also own some, building some? And where does that fit in the overall strategy?

**34:55** · Yes, so, you know, initially we we started off as being primarily a renter, and we've actually started to get into the business of uh financing some of them the construction of them ourselves, as well as, you know, we're going now into full

**35:11** · vertical integration, where we are identifying land, coming to the table with a basis of design, which is basically all the engineering diagrams to construct the data center, financing and constructing that data center, putting the servers in, and then associating that with like a long-term off-take agreement with one of the major compute consumers in the world, and financing it all.

**35:37** · So, like, we're getting into full vertical integration at Lambda, and it's been it's been great, because we've been able to kind of, again, bring that engineering mindset to this problem, which was historically mostly run by people in real estate.

**35:51** · In your own data centers, are you the sole tenant, or is part of the idea that you can also rent some to others?

**35:58** · In a lot of our data centers, we are the sole tenant. In terms of the data centers that we're planning on constructing, we don't yet have any plans to lease that space to others. So, we're not trying to get into the the leasing data center business. Um maybe that's something that you can imagine down the road. I wouldn't write it out completely, but, you know, for now, we have to focus on providing Lambda with the compute that we need to service the market.

### How global is Lambda? Does location still matter?

**36:24** · How international are you, by the way?

**36:26** · You know, I'd say that we're very much focused on North America. And so, we have data centers in Canada, United States, and Mexico. We're very much, like I say, primarily focused on North America, but really within, you know, that the United States, obviously.

**36:44** · And um we we haven't had this desire internally to try to go and expand into Europe or or uh too far into Asia. We've done some partnerships with some of our great investors like uh SK Telecom. And we have a data center uh that we've operated in Korea, in Seoul. And so, we have some experience with international. Um but right now, we're just like, "Look, let's focus on the US market. It's where the opportunity is."

**37:15** · Do you need for performance reasons to be close to the customer the way you you need to have regions in cloud?

**37:21** · You know, it's super interesting. A lot I get this question a lot. And people they're like, "Well, uh does latency matter? Does" So, I'll tell you what what matters and what doesn't matter.

**37:32** · You can look at your own utilization of whether it's ChatGPT or Claude or Grok or Gemini, and you can see, "Hey, a lot of the things that I'm doing, I kind of shoot it off, I come back later, and there's a research report for me. Maybe it's a long-running agent workflow." In those cases, latency doesn't matter at all. The only thing that matters is your cost per token. That's all that matters.

**37:57** · And um so, that that's been a really interesting change I think that, you know, the old-school traditional legacy cloud business was so latency-focused because of some of the applications.

**38:12** · But this new fleet of AI applications are far less latency-sensitive, so that's one. But there is the caveat, which is this: governance and data governance is becoming an important thing and a lot of countries are wanting to have the AI compute that their citizens are using be run out of their own country so that they can, you know, at least have their own their perception of control or whatever. And the, you know, that is that is another that is an element to it, but I'd say that from the latency and there's no technical reasons.

### The financing stack: off-take agreements, SPVs, and credit

**38:44** · Let's talk about the financing stack.

**38:47** · So, presumably it's a combination of equity and and debt. How does it all work?

**38:52** · Yeah, so the way that it works is that you you know, you can really fragment it into these two parts which is like financing your on-demand cloud versus financing an off-take agreement which is like a longer term commitment. And on the on-demand cloud, you're kind of looking at Lambda's credit quality. On the off-take agreement, you're kind of looking at the credit quality of the the end customer who's paying the bill.

**39:21** · And so, what you do is you just, you know, take your off-take agreement, you take this chunk of GPUs that you're deploying, you take a lease or the the property and you kind of put it into a box and you can go to the private credit markets and you can come up with, you know, an asset-based loan. You can you can get a a variety There's a variety of different methodologies for financing it.

**39:46** · Most of it is just some sort of like special purpose vehicle that's designed to finance this particular deployment with a very known and easy to underwrite, which is basically just a fancy way of saying the, you know, finance term for just under set assessing the risks and the downsides of a particular credit investment. And there's there's a there's a vibrant private and you know, there's a there's a there's a vibrant credit market for that.

**40:16** · On the on-demand cloud side of things, it's, you know, not quite as mature as when there's a, for example, an investment-grade off-taker agreement. Um but it's becoming more and more mature and in general, creditors and lenders are really starting to understand the value of an Nvidia chip.

**40:37** · Because, you know, you actually look at the chips that we deployed in 2023, H100s, we are now leasing those out at a higher rate now than we were originally in 2023. So So these creditors are starting to look at these assets and say, "Wow, this is an asset that is very valuable and also easy for us to underwrite."

**41:00** · And of course, while they are underwriting towards the actual cash flows that are coming out of that agreement, just as an asset class overall, people are realizing that this is a really great opportunity. And so creditors are starting to flock to these deals.

### Why a 2023 GPU leases for more today

**41:16** · You rent an H100 at a higher rate because why? Because the demand for compute is so rapid that people will take any or the technical depreciation of the of the product is slower than people thought. What what what drives that?

**41:32** · Well, what's driving it, I mean, it's certainly it's the the demand being high increases the price that you're able to get in the market. There's no question about that fundamental law. Again, going back to what people didn't understand about this market. There is people who are saying, "Oh, well, there's a, you know, there's a five-year lifetime or three-year lifetime." I've even heard some people say three-year life lifetime for these GPUs. It's completely false.

**42:00** · You know, we have GPUs that we've commissioned and we're one of the earliest neo clouds. In fact, we we're we're probably the only one only neo cloud that actually has GPUs in our fleet that are fully depreciated from an accounting perspective, right? Which is most people are adopting around a 6-year accounting depreciation schedule. But, that's not the usable life. The usable life is longer than the accounting depreciation schedule. And what really matters is the economic usable life. And so, what we're starting to see is that like the people who are the naysayers, oh, this is going to be you're going to throw these GPUs out in 5 years, are completely wrong.

**42:32** · They're completely wrong, and they've been wrong the entire time.

### A futures market for compute?

**42:36** · Do you think there is going to be or do you already see um happening some kind of uh financial market for compute units, you know, with trading and derivatives?

**42:47** · Is that Is that happening?

**42:49** · I'm starting to see some people, you know, start to examine what a maybe vibrant spot market, you know, first you need to have a spot market for something before then you can establish, you know, um a derivative like a future or or other other more exotic things.

**43:05** · Um I'm starting to see that, but fundamentally, I think that the the the asset class is just starting to mature, and creditors are starting to become very comfortable with in investing in the credit side of buying Nvidia GPUs and deploying them into data centers.

**43:23** · And uh we don't need to get too fancy with it. That's kind of like my part of my opinion is that like I think that the that market is starting to mature. That that that may be an eventuality is having more complex securities that surround GPUs, but um uh I think for for for right now, people are starting to realize that it's a it's a great credit investment, and that's that's what's changed, I'd say, over the last year is that people have started to really uh treat it like a a more mature asset class.

### Origin story: facial recognition, Perceptio, and Apple

**43:54** · Maybe quickly just go back to the very origin because I I think you've been in the effectively in the AI world the whole time, but are coming from a very different angle uh with multiple pivots. What What did you start with and and when?

**44:06** · Well, you know, with the complexity of the business, you can now see you know, the complexity of the capital intensity, just the sort of not fitting into a box, and you can see why we've oftentimes not had a lot of traditional venture investors in in Lambda. And uh you know, all of all of our investors have done exceptionally well, but but they've they've kind of come from more often than not outside of traditional this same mainline Silicon Valley VCs.

**44:34** · And um so, just going back to the origin story, I started Lambda in 2012, and we were a facial recognition software company. So, I was training convolutional neural networks to do face and image recognition, and we eventually hosted that on API.

**44:52** · I was training those convnets on a 4x Nvidia uh uh GTX 580 workstation that I had uh that I bought from a friend who had built it, actually. And um and this was, you know, really pretty avant-garde stuff at the time. Most people didn't really believe in what was called the the field called deep learning at the time.

**45:19** · And that was inspired by the ImageNet 2012 moment, or that was even before that?

**45:23** · The ImageNet moment, you know, I I I pulled the CUDA convnet repo off of Google Code. That's how you know how old Lambda is is that Google Code was still around. And I pulled the CUDA convnet code base and was like playing around with it. I got very lucky that the AlexNet paper had been published the same year that Lambda was founded. It's not a coincidence at all. It's not a coincidence at all.

**45:48** · We launched this face recognition API, got a couple thousand users, but it wasn't really generating a ton of cash. And um uh sort of as part of that the complex story of startups, you know, in parallel I was sort of I found these guys who had just graduated from their PhD programs.

**46:10** · Uh the gentlemen Zach and Nico and they had said, "Hey, we're going to start a company." I said, "Hey, you know, let me help you guys out. I'm going to work with you for a year. I'm going to learn a little bit more about neural networks." And um uh we I helped them out on this company how helped them get a company called Perceptio started. And I was the first employee there while I was running Lambda. And we were we were running these convnets locally on the iPhone.

**46:38** · And again, this is 2013. So, we were we were using the GPU image library and just straight OpenGL ES shaders. Like the shaders that are used for rendering. We were using those to run the convnets on the iPhone.

**46:53** · And um eventually I kind of left to go continue to work on Lambda full-time and then probably about a year or so later they got acquired by Apple. And so, if you know the feature on your iPhone where you swipe up on an image and you can, you know, recognize faces and search your library. That's maybe some of the stuff that eventually got integrated into iOS through that acquisition. And then Lambda, you know, we continued on I had a we had a variety of different products.

### The Lambda hat and Dream Scope

**47:17** · Everything from Lambda hat, which was a baseball cap that took a camera every 10 sec took a picture every 10 seconds with a camera embedded in the tip of the brim for gathering data sets for image and face recognition.

**47:30** · Which is fascinating because fast forward to today and that's a whole segment, right? Like capturing everyday life to train the AI.

**47:37** · It goes to show you have to, you know, it's one it's important to be able to see the future. It's also important to get your timing right as well, right?

**47:46** · Um and now it it all worked out, right? Despite maybe that Lambda hat product not being great, but it taught me a lot about how to build hardware. I was I lived in Shenzhen for a little bit uh working on the PCB and spinning the PCB and designing the actual hardware product.

**48:03** · And you know, it taught me how to make consumer electronics. And that was actually a huge huge skill cuz it totally opened my mind to new ways of doing business that aren't just making apps, right? And um eventually we had this product called Dreamscope, which became really popular in 20 um 15 16, and it was basically using the Google Deep Dream uh methodology of using a convnet to generate images. It's like an early version of Midjourney or whatever.

**48:37** · And um Deep Dream uh and the Leon Gatys style transfer algorithm. A lot of you turn a photo into a painting, basically. And we got like a million users on that, processed tens of millions of images, maybe 15 million images or something like this. And um that caused us to have a huge AWS bill.

### The $60K bet that became a cloud business

**48:59** · It was like $40,000 a month or something. And so to replace that, we'd ended up building a little cluster out of workstations. And uh then there was a $60,000 CAPEX that we were terrified to make, by the way. We were so so scared that doing this CAPEX was going to put us out of business. We made it out of workstations because we thought, "Oh well, worst-case scenario, we can just sell them." And so lo and behold, we did end up, you know, turn it online and it brought the bill down to zero. So it paid itself back in a month and a half.

**49:28** · And we thought, "Oh, this is like we're we're saving more money than we're making. Maybe we should be in the business of providing compute to other AI researchers." And thus, we started selling workstations and servers and started developing our cloud platform. Maybe did $3 million of revenue in 2017 that first year selling workstations, then 10 million in 2018, then 30 million in 2019.

**49:49** · Um we grew the hardware business over the next couple years to probably about $200 million run rate. And then the cloud business we really started in 2019. And you know, we started development before then, but we started really marketing it. And it kind of was slow to grow, to be honest, because you know, not a lot of people in 2018 and 19 and 2020 wanted a bunch of AI compute. There was a pretty niche market for it.

**50:16** · But eventually, you know, our cloud business continued to grow and now it's at, you know, a little bit under a billion dollar revenue run rate. We've fully exited the hardware business. And so, yeah, Lambda's got a absolutely wild founding story to summarize.

**50:34** · Are some of the people that were there at the beginning still around? I think you started the company with your brother. Is that right? And your brother is is still at the company?

**50:42** · Yeah, and so in terms of like the early people, basically it's not I mean, not even basically, of the four people who are making Dreamscope, me, Michael Balaban, my co-founder and fraternal twin brother, Shuang Li, who's our chief scientific officer, and then Steve Clarkson, who's an engineering leader at the company and you know, has a bunch of folks reporting into him. Now, you know, they're all still at the company.

**51:10** · The next hire, one of those gentlemen named Mitesh Agrawal, who was one of the the next hires in that team, he was with the company for maybe eight years or something like this. Um Five, six Yeah, something like eight years. And then he eventually left and joined another former Lambda team member, Thomas Summers, to start Positron, which is an accelerator company. And they're like now valued at over a billion dollars.

**51:43** · And so uh not only has like the original team stuck around, but we've already started to kind of see what like a Lambda uh alumni a Lambda mafia network looks like in in the world. Lambda lab member alumni.

### Holding the team together through the hard times

**52:00** · How did you keep the the band together during the difficult times?

**52:05** · Just when you're running a startup company that's this capital intensive, working capital intensive as well, like it's just you get a lot of shocks to the system as you're growing. Um and then COVID. What COVID I mean in April of COVID software companies were feeling great because they could ship software and there was so much to more demand.

**52:26** · Hardware companies the docks were closed. You couldn't ship revenue in April and March. And um so I mean I remember all these things really distinctly. I I I think I remember just getting in front of the team like, "Hey look, it it's it's really tough right now and

**52:45** · um you know, there's certainly a feeling that like we're not sure if we're going to make it through this, but the only thing to do is just to like suck it up and enjoy the pain, run through it and come up with a solutions to the problems that you're presented with all in the service of delighting customers because fundamentally I mean the big thing is just aligning people towards the only reason we're all here is to build something that people want and they love so much they friends about it and they give you money.

**53:18** · And then everything else it just fall follows from that customer experience of delighting customers with what you do.

**53:24** · When we do onboarding for example, I used to do this thing in what we called Lambda 101 and we would show a picture of like a Linux penguin and he was like on a Lambda workstation and he was reading the GPT 2 paper and training and had a loss curve which is like what you see and you look at as your if you're doing machine learning research. I was like, "Look, just put yourselves in the shoes of the penguin who's training using this workstation or cloud service to train a neural network, and just think about what's going to delight them.

**53:56** · You know, whether it's you know, uh people on our shipping team who said, "Hey, let's put some t-shirts inside of the boxes." And so every workstation came with the a lambda t-shirt. You know, or members of the data center operations team said, "Hey, you know what?

**54:10** · We should do a white rack because that that'll kind of like set us apart and make make everything look good, and we'll be really proud to showcase that." And you know, those are the types of things that as you kind of imbue your company with the kind of delight the customer-first mentality, that I think helps you get through the hard times.

### Bringing on a new CEO; Stephen as CTO

**54:30** · Recent evolution in that journey is that you just brought on a new CEO, and my fellow French countryman, Michel Combes, to run the business. Uh walk us through the thinking and what led you to make the decision and how that equips the company for the next chapter.

**54:46** · It's a huge honor as a founder to get to the point where the company can um afford to bring on amazing talent like Michel you know, in that seat, right?

**54:58** · Just because if you think about it, I'd say most companies it it's not uncommon for somebody to say, "Hey, look, a lot of people sometimes maybe there's a comp there's a component of ego involved where they have to be the founder CEO." I've never really personally had that. I I care about the technology, as you can tell. I care about like building a great generational company, and uh I think there's so many different seats to do that from.

**55:26** · And so, you know, getting to the point of maturity where we could afford to bring on a a CEO like Michel who has experience like he, you know, obviously previously SoftBank International CEO, Sprint CEO.

**55:40** · Alcatel.

**55:42** · Um Alcatel, he's on the board of some like really amazing companies, um you know, including McLaren, which is a kind of a fun one. I always did the sort of like fundraising and capital formation and day-to-day business management as a a necessity and not like because that's what I really love doing, for example, right? And I think there's plenty of founder CEOs who absolutely love every aspect of their CEO job.

**56:10** · I think that privately, and you you'll be very hard for you to get this out of any founder CEO often times, but like secretly, when I talk with founder CEOs, I'm always like, "Yeah, so uh like how much do you hate \[laughter\] I find it shocking that people don't find speaking to VCs all day exciting, but I will definitely look \[laughter\] for that.

**56:33** · It's been like an amazing experience for me that I to be able to form a team around the company and to just see everybody flourishing in things that they love to focus on. So, for example, now that I'm the CTO, one of the main things I'm focused on is what does rapid

**56:51** · data center deployment look like at the company and, you know, kind of working to say like, "Hey, I want Lambda to be this sort of vertically integrated high-velocity powerhouse that So, when you look at the world, you say, "All right, there's two people in the world that can and two companies in the world that can do high-velocity deployments.

**57:08** · SpaceX AI and Lambda, where we're just extremely focused on how do you cut every little piece out of the process to stand up compute faster, um and that's like something I've just been diving into and really enjoying with my new uh time as uh uh CTO.

### Matching xAI on high-velocity deployment

**57:33** · What was like Cerebras' record? Like when did they launch the I think it was like 200 and something days.

**57:39** · Yes, and you think that can be matched or exceeded at a repeatable pace?

**57:44** · I think it it can be matched or beat, yeah.

**57:47** · And that's process mostly.

**57:49** · I think it's it's everything from like the site selection process, the set of constraints that use in a site selection process, the the the MEP pipeline, the way that you construct the data center, um you know, how do you make it so that the end customer will consume that compute, you know, and and how do you cut out a lot of stuff out of the process because often times, you know,

**58:13** · the people who've been designing these data centers have really kind of been real estate people as I mentioned who've been kind of grabbed by the scruff of their neck by a hyperscaler and they're like, go and build this design. Here, go go get a GC, run off, and they don't know anything about what goes inside of it. And so and and the hyperscalers on the other hand have been really building towards traditional cloud services. I mean, if you look at a modern region in any of the clouds, they have hundreds of services.

**58:42** · I mean, everything from satellite base stations to tape storage to spinning disk to face recognition APIs. I mean, these are all the services and each of those services requires a different SKU and has different parameters about what you're kind of servicing. And and in fact, you know, you might have somebody who's trying to run an ATM back end on one of these things.

**59:06** · That's a pretty different design space and design constraint than an AI data center that could maybe, you know, have a lower availability and uptime, right? And so that's kind of where I think Lambda is able to build a lot of really unique um value and you know, through this kind of targeted AI first approach.

### AI won't write software — it will become the software

**59:29** · You had a a quote where you said that AI won't write software, it will become the software. What What do you mean by that?

**59:37** · So, uh that's in my sort of like idea around what I call neural software. And or, you know, a neural computer neural operating systems.

**59:47** · And the best way to kind of get this experience is to go to your chat GPT or your Claude and say, "Hey, just um, you know, render for me an ASCII art desktop interface, okay?" So, you're you're working in purely in the domain of text, and I want you to just pretend to be an operating system for me. I'm going to say, "Click on this, you know, open up this." And I want you to just behave like a computer. So, give it that prompt, okay?

**1:00:17** · And um what you're going to see, I think, is that you're going to see that uh that sort of future of the large language model becoming the software and not generating the software.

**1:00:32** · And um this results in an extremely sort of squishy and flexible way of interfacing with a computer, where it's not possible to have a bug, only a misunderstanding about the prompt and what you've asked for. And I think that for a lot of the pieces of software on your computer, you might see that taking over where, you know, you can get the glimpse of the future with this ASCII art, and then eventually it'll also have a multimodal network that's generating every pixel on your screen.

**1:01:04** · As well as every audio waveform that comes out of your speakers. The advantage to this is that you can really sort of dream up software, the only the part that is being experienced by you, and uh you know, is actually implemented, right? If that makes sense. Um, you know, it could have whatever feature it is if you ask it. And that's like a really powerful way to interact with the computer, I think.

### Neural software vs. vibe coding

**1:01:30** · So, it's not like you you give simple instructions to the LLM, suddenly the LLM is the software.

**1:01:37** · I guess make the analogy like, you know, vibe coding takes in a prompt and then outputs human readable, writable, compilable code that runs on normal human software programming language. Substrate, right? You know, it outputs C code which gets put through a compiler or it outputs Python code which gets put through a Python interpreter.

**1:01:59** · That software is static. Once it's been generated, it can't change, right?

**1:02:04** · You could vibe code it again and maybe, you know, vibe code on the fly. There's like a couple different stages of the gradient between traditional human-written software and then you go to like maybe vibe coded software, then you go to just-in-time vibe coded software where like it's a live creation of the software application.

**1:02:21** · But it's still software.

**1:02:23** · But it's still software. But then you go to the next step which is just you're interacting with the LLM and it is emulating kind of how software might behave. And that's that's the difference um, between vibe coding and a neural operating system or neural software. Neural software, there is no code that's running. It's just modifications of the feature activation space and the context in the mind of the neural network.

**1:02:53** · And how far do you think we are from that? Is that something I mean, we we have prototypes of it today. So, we have prototypes of it today.

**1:03:01** · And when you say you, is that is that Lambda or is that is that obvious?

**1:03:04** · Yeah, Lamb- Lambda has developed a prototype. There are multiple other companies that developed prototypes of this. Um, there's academic research that is has, you know, outlined what this might look like.

**1:03:16** · And um, you know, how far are we from, you know, mass adoption?

**1:03:22** · I would say that generally speaking, when I'm early on something, I tend to be about a decade to a decade and a half early.

**1:03:30** · So, I would say that between a decade and 15 years, we will see mass adoption beginning or otherwise happening for neural software. I mean, you you already have it. So, here here's another example, by the way. You already have So, you can think of a Tesla self-driving car or, you know, any type of end-to-end neural network and end you know, end-to-end large model that's doing autonomy as a form of neural software. Right? And you know, people understand that aspect, right?

**1:04:03** · Which is it's seen video, it's making decisions about what to output. Now, the user experience is the driving experience. That said, that is an example of neural software, I would I would argue. And so, we already see that today. Now, the question is when is your everyone's computers going to adopt that? I'd say a decade.

### Do agents change the compute layer?

**1:04:25** · Do agents change anything from your perspective as a compute provider, and if so, in what way?

**1:04:32** · To understand what needs to change on the computer layer, we understand need to understand what's changing with the user. So, when you're doing live coding with agents, one of the things you'll notice is that your wall clock time, you know, in in the world is mostly spent on running tests, gathering data, searching through code base. A lot of the time is spent act not just inferencing a neural network, but it's actually spent doing other things.

**1:05:00** · And it it's actually very much not It's very much similar to how software engineers spend some of their time, right? You know, the old XKCD cartoon of compiling, where they're sword fighting on the office chairs and someone says, "What are you guys doing?"

**1:05:16** · They're compiling. And so so now there's a bunch of time spent compiling, there's a bunch of time spent running tests because uh the part of the way that that the agent 24/7 loops really work well is when you are constantly banging against a nice suite of automated tests to make sure that the code you're writing is good. And so well what does that mean?

**1:05:40** · It means that every single um cloud service needs to start doing a lot more um traditional CPU workloads. They need to do uh focus on a great uh environment, a secure environment to host your Claude code instance on. Um and then you need to think about security from the perspective of you need to think about how this massive influx of new applications are going to be secured.

### Self-assembling software inside Lambda

**1:06:14** · How do you use AI agents internally?

**1:06:17** · Well, I mean a lot of uh the engineers at Lambda are already, you know, doing a fully agent-driven workflow. I mean, if you just go to Claude code and say, "Hey, use advanced workflows" or you know, spin up agents, um you can do that. So that's like step one.

**1:06:35** · Um I've demoed internally and some folks have adopted what I kind of call self-assembling software. And so self-assembling software is this idea where you, you know, kind of tie in to a 24/7 running agent fleet um product requirements and constant user feedback that's coming off of the system. So you have a very clear and tight loop to go from submitting, "Hey, this is a bug" or "This is a feature request.

**1:07:06** · And there's a fleet of agents who are implementing that live for you, okay? And that sort of cycle I call self-assembling software is because you kind of say, "Hey, this is what the software's for." But most of the development for it's going to happen after the software is launched and the users start to interact with it and customize it for themselves collectively. And I think that that is kind of maybe the future paradigm of where a lot of the agent-driven development is going to go towards.

**1:07:32** · Um the the the the other side of that, eventually once the models get smarter, I think that they're quite not not not quite there yet, but you know, tying that back into, "Hey, I need help."

**1:07:48** · And I'm not talking about the human. I'm saying the agent's going, "Hey, I need a human to help me like I need to plug in a thousand GPUs for me or I need you to um give me an API key to a particular service. I need you to go sign up for something for me. Can you go please negotiate this?" And I think that that's actually how you're going to start to see it happen, which is product user feedback gets implemented by the agents. The agents then also ask the people at the company to go and do things for them, all in the service of, you know, delighting customers and making money.

### Gigawatt-scale AI factories

**1:08:18** · You've talked about gigawatt scale factories. Is that what you were describing earlier around like setting up beginning super good at creating data centers very quickly, but it's also making them bigger What what is that concept?

**1:08:32** · It's a an AI factory, which is a basically land, data center, servers inside that is generating tokens. And a gigawatt scale means that it's consuming a thousand megawatts or a a billion watts, which um is a lot of power. Sort of like maybe you can think of it for context, New York City is something like five gigawatts.

### One person, one GPU

**1:08:57** · You also talked about one person one GPU. Is that uh your your vision for the future? Unpack that for us.

**1:09:04** · So, um you know, before people really believed in the AI thesis, I you know, when I was pitching our series B and C, I would kind of talk a a lot about the similarities between, let's say, the computer industry and the AI industry. I really felt like AI was forming a set of generational companies, um and there was going to be a set of generational companies that got minted with the changes that were coming with AI. And this is like in 2020, 2021.

**1:09:35** · And if you read about the history of Apple, for example, in the early days, the motto and the the sort of the credo at Apple was one person, one computer. One person, one computer. And you know, there's a sense of humility that's embedded in this one person, one GPU, which is the one person, one computer. You think about how visionary Steve Jobs was.

**1:09:57** · That was, you know, Apple was, you know, what, founded in 1976 or something like this. The Macintosh came out in 1985, or 1984, excuse me. 1984, you know, whatever. Um 8 years or so after founding. Is that one person, one computer yet? No, not even close. All right, so 1984 to 1994.

**1:10:19** · All right, well, is it one person, one computer? Well, we're just starting to have the internet boom. So, we're we're we're we mean not quite there yet.

**1:10:26** · 2004, we finally have broadband internet access. And maybe for the first time in the United States, there's not quite one person, one computer, but there's certainly like one person, one family, one computer, you know, or you know, something like this. It's like getting close to it. You don't have until 20 14.

**1:10:44** · So, 74, 84, 94, 2004, 2014. 40 years after one person, one computer, do Do have probably truly one person, one computer and you get actually beyond one person one computer because people have laptops and cell phones and I would consider a cell phone a computer. So and then and then finally you don't even have e-commerce penetration until 2024.

**1:11:10** · 50 years after the founding or so of Apple computer when e-commerce starts to actually penetrate because of COVID. I think that the the reason I really wanted to choose that one person one GPU is because one I believe that in the future everybody in the United States will need the computational power of one GPU or more to just do their daily work you know, enjoy

**1:11:39** · life whether it's getting access to whether it's getting entertained, whether it's being productive, whether it's being creative. And I also recognize that it took Steve Jobs and Apple one of the best companies in the history of capitalism half a century to accomplish their goal. And so I I think this is not it's not just like an overnight let's you know, quickly get to one person one GPU. Um so that's that's that's what that means to me.

### Hot takes: overrated and underrated in AI

**1:12:04** · To close are you ready for a couple of quick hot takes?

**1:12:08** · Sure.

**1:12:08** · What is one idea in AI that is overhyped?

**1:12:13** · I think a lot of the sort of agented agentic workflows for things that are not software engineering I think tend to be overhyped and I'll tell you that the reason for that is because one of the ways that you get an agentic workflow working really well is it needs to have very concrete feedback mechanisms which are done brilliantly through automated testing. It's not at all done brilliantly for like going to buy a site.

**1:12:37** · There's no there's no traction to give a model to go and iterate over a long period of time on. So I think agentic workflows for things that aren't readily verifiable. Now I wouldn't say as far as everything that's not sovereign because there's plenty of readily verifiable fields.

**1:12:53** · CAD, uh computer-aided manufacturing, um finite element analysis, computational fluid dynamics. There's a bunch of fields where you can really do an a great agentic workflow. I mean, and and simulate it and then go and iterate. It's not the case for hey Claude, make me a billion dollars, make no mistakes, you know.

**1:13:14** · Sadly, or maybe not. Uh okay, fascinating. \[laughter\] What what inflation would be What it wouldn't be inflation. It would actually be just valuation in the economy.

**1:13:23** · Deflationary even.

**1:13:24** · What is one idea in AI that is underrated?

**1:13:27** · Yeah, I I really think that the neural OS thing and you know, also some of the aspects of self-assembling software. Like I still do think people through You know, the funny thing is I was going to give the same answer.

**1:13:39** · Agent-based workflows for software development. I think that most people don't understand. They literally don't understand because they've never tried it. They've never gone to Claude, go to Claude, go say maximum effort, uh use the latest model, and then go and build whatever you wanted to build and say, you know, spin up 10 agents to go and do it. I think a lot of people still haven't done it yet.

**1:14:00** · Well, Steven, it's been wonderful. Thank you so much for spending time with us.

**1:14:04** · Matt, thank you so much for having me.

**1:14:05** · Appreciate it.

**1:14:08** · Hi, it's Matt Turk again. Thanks for listening to this episode of The Mad Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't already or leaving a positive review or comment on whichever platform you're watching this or listening to this episode from. This really helps us build a podcast and get great guests. Thanks and see you at the next episode.
