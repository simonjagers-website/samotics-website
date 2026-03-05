---
title: "SAM4's hardware architect talks about medium-voltage monitoring"
slug: "sam4s-hardware-architect-talks-about-medium-voltage-monitoring"
date: "Tue, 13 Apr 2021 14:18:07 +0000"
category: "Blog"
category_slug: "blog"
tags: []
original_url: "https://samotics.com/blog/sam4s-hardware-architect-talks-about-medium-voltage-monitoring"
images: 0
word_count: 913
---

We recently spoke with our hardware architect, Ate Kleijn, about the expansion of our condition monitoring system SAM4 to cover AC motors at higher voltages. Watch the video to hear how the project went from idea to implementation. Then check out the notes below for parts of the conversation that didn’t make it into the video.




## Cut for time: customers, copper and critical complexity






Not everything we covered made it into the video. Here's the rest of our interview with Ate.
### So tell us how the medium-voltage project got started.


Our medium-voltage project started because of our clients. We had a lot of inquiries from our customers about whether we could deliver the same condition monitoring service for medium-voltage machines as we do for low-voltage ones. That led us to start researching whether we could add the same value with SAM4 as we do for low-voltage machines.
### Why is it important for our customers to monitor medium-voltage assets?


Medium-voltage machines are important to monitor because they’re typically in a very critical part of the process. And these machines are typically very big. They’re expensive, they’re expensive to maintain, they’re expensive to replace. And the knowledge and expertise you need to work on these types of assets is different from what you need for low-voltage equipment.
### What made you excited about this project?


It was exciting to get to explore this new territory. This was a field that was unknown to us before we started the medium-voltage project. It was really nice to talk with clients and get to know their systems, really sort of dive in and know how things work in ways specific to medium voltage. What are the do’s and don’ts? How are they being used? What’s possible, in a technical sense?
### What role did our customers play in the process?


Without our clients, we wouldn’t have been able to test our findings, what we had figured out on paper or tested in our lab. By setting up a pilot project with clients, we really had the opportunity to frequently check our measurements against what’s being recorded by the client. It was a really intense iterative process of exchanging information, basically, just to get a grip on the quality of the condition monitoring that we could supply for medium voltage. Feedback on the state of the machine, but also internal measurements that aren’t normally available to us.
### Were customers excited to be part of this development?


Our customers were very excited to be part of it. First and foremost, because they requested it (laughs). But even so, even though they have the need to continuously monitor their medium-voltage machines, not every customer will step into a pilot with you. It’s asking a lot. So, for example, with Nouryon, we were given access to measurement data that was internal to Nouryon. Electrical data, but also hydraulic data for pumps, that really helped us to validate and assess our measurements.
### What was the biggest challenge you encountered in this project?


Ironically, the biggest challenge was that it was very difficult to get a time slot to install our equipment. Which is of course the problem that we’re tyring to solve with our system, to make the available time for medium-voltage machines as effective as possible. What you see with medium-voltage machines is that typically there’s only one opportunity each year, or even every two years, for maintenance, And you want to make use of that window as much as you can, make sure you do all the maintenance you want to do and get everything done within that week or so. For us to find a window to install our equipment for a pilot—that was challenging. Luckily, they made some room for us.
### What benefits does it provide our customers that SAM4 can now also monitor equipment running at higher voltages?


I think there are mainly two great benefits for our clients, the first one being that by continuously monitoring your asset and keeping an eye on developing failure modes, you have a much clearer picture of what you really need to do within those very rare maintenance windows. So I think that’s one part. The second part is that it’s very easy to install. We don’t physically and directly take current and voltage measurements on the medium-voltage lines and phase wires. Instead we use the secondaries of the available current and voltage transformers, which means we only need access to the low-voltage compartment, and we don’t need to interfere with any medium-voltage parts. So this makes it a very hassle-free installation.
### One last question, Ate. What was it like to be on site and see our customers' medium-voltage machines?


For me, it was pretty cool because I have a background in electrical engineering. So basically anything that’s made of copper and electrons gets me going (laughs). And it’s pretty impressive to see this big machine, say a couple of megawatts, especially when it’s doing its job. I mean, those forces are immense, you know, these voltages, they’re actually quite dangerous. They have to run a tight ship to make sure that everything is in order, and you really cannot afford any mistakes there. So it’s really good to face the reality of our customers and see what they need to do on a day-to-day basis to ensure production uptime. And it’s always more involved and complicated than you’d think in the first place.
