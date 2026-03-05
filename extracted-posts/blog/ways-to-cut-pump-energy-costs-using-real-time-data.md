---
title: "Four quick ways to cut pump energy costs using real-time data"
slug: "ways-to-cut-pump-energy-costs-using-real-time-data"
date: "Tue, 06 Jun 2023 13:09:38 +0000"
category: "Blog"
category_slug: "blog"
tags: []
original_url: "https://samotics.com/blog/ways-to-cut-pump-energy-costs-using-real-time-data"
images: 7
word_count: 1832
---

Centrifugal pumps are a widespread industrial workhorse, accounting for roughly 16 percent of the energy consumed by industrial electric motors worldwide [1]. For the health of both the planet and your wallet, it’s vital to run them at peak efficiency. In this article, we’ll show you four fast, low-cost ways that real-time machine data can help you start lowering pump power consumption and emissions.

![](https://samotics.com/wp-content/uploads/2023/10/Energy-image-diagram-final.png) Energy costs represent a sizable portion of the lifetime cost of a pump.









There are several ways to lower a centrifugal pump’s energy consumption. Generally speaking, we can divide these strategies into two classes: short-term changes to existing machines, operations and practices, and long-term changes that focus on redesigning part or all of the system. These long-term changes can produce extensive savings, but they take months of planning and significant investments. In this blog post we’ll look at some short-term changes that don’t require large capital expenditures. All you’ll need to get started is a way to see how your pump is performing in real time — and chances are, you already have it.
## Step 1: Use real-time machine data you’re already collecting










There are three pump performance parameters you can use to identify inefficiencies — and you’re probably already tracking at least one of them. The readings from flow, power and pressure sensors can be used to calculate the pump’s energy consumption.
### Flow and pressure data


Flow meters and pressure meters do not directly track a pump’s energy consumption. However, they track two key parameters that enable you to estimate it pretty well. You don’t have to do the math yourself — in step 2, we’ll look at tools that will do it for you. But if you’re interested, [Neutrium’s engineering encyclopedia](https://neutrium.net/equipment/pump-power-calculation/) explains how you can turn pascals and liters-per-second into kilowatt-hours.
### Power data


If you’ve installed power sensors to directly measure the pump’s actual power consumption in real time, you’re in an even better position. While flow and pressure data can give you some high-level insight into a pump’s energy use, without power data they depend on static estimates of pump and motor efficiency. These are often idealized numbers that may or may not have been true when the pump was brand new, but are almost certainly no longer accurate as the pump ages.

What’s more, operational conditions can change the pump’s actual efficiency from one moment to the next, regardless of its rating. For example, periods of lower demand can put such a low load on the pump that it runs very inefficiently, even though its efficiency is fine at its usual load. It’s these operational factors that enable most of the quick, low-cost changes that will save energy. Sensors that directly measure the current and voltage being drawn by the system provide all the detail you need to track these factors.
## Step 2: Run energy analytics on that data


You might already have the expertise in house to analyze your flow, power and pressure data from an energy-savings perspective. If not, there are plenty of modern energy intelligence platforms that can ingest your existing data and analyze it to provide detailed recommendations.

If you decide to go with an external platform, here are some things to look for:


 	- **Clear, intuitive visualization and reporting.** Interactive dashboards, customized reports and concrete recommendations will help you understand energy consumption patterns, identify inefficiencies, and track the results from your energy-saving initiatives.

 	- **Energy performance metrics. **Look for an energy intelligence platform that provides key performance metrics, including those specific to pump systems. Your reports should include insights on where energy is lost along the drive train, pump performance curves, specific energy consumption (SEC), and industry benchmarks.

 	- **Clear guidance. **The platform should not only recommend energy-saving actions, but also help you prioritize them by business value and context.

 	- **Integration and scalability.** Consider whether the platform can integrate with your existing industrial automation systems, data storage systems, or other energy management systems already in use. Scalability is also crucial if you want to expand the platform’s coverage to include additional pumps or even other equipment down the road.

 	- **Support and service.** Assess the support and service provided by the platform vendor. Are you on your own once you install, or do they have industrial energy experts to help you identify, validate, and track initiatives? What do their customers say about them? A reliable supplier with a strong support system ensures a smooth implementation process and ongoing assistance when needed.



![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_image_2_dashboard.png) An energy intelligence dashboard showing a customer’s top energy consumers over time.

![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_image_3_insights_report.png) An insight report generated by an energy intelligence platform, detailing a potential energy optimization initiative.








## Step 3: Start saving energy


In this section, we’ll show you four simple process changes to cut energy cost and emissions, using real examples from our own [energy intelligence platform, SAM4](/products/sam4-energy).
### Example 1: Change the flow thresholds


At a wastewater pumping station, two of the three pumps often operated simultaneously at low-flow conditions. The real-time pump curve in the SAM4 platform showed that both pumps were operating well to the left of their best efficiency point (BEP), which wastes energy. Using a month’s worth of operational data, SAM4 calculated that a single pump could deliver the required flow 100 percent of the time, and in doing so would operate much closer to its BEP. Instead of needing 77.5 kW to deliver the required flow using both pumps, the station would need only 55 kW — a 30 percent reduction in power consumption.

The pump owner changed the station’s control logic to run only one pump in these low-flow conditions, by raising the threshold at which a second pump kicks in. For this pumping station, this simple process change is saving over € 10,000 in annual energy costs and reducing indirect CO2 emissions by 23.5 metric tons per year.

![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_table_one_last.png)















### Example 2: Change the pump’s speed


A raw water pumping station with two larger pumps and one smaller pump showed large operational efficiencies. SAM4’s analysis showed that the two larger pumps were often used inefficiently to supply flows that could be covered by the smaller pump. Two simple settings were changed to achieve more efficient pumping literally overnight.

We’ve already seen the first change in the previous example: a change in control logic. The flow threshold at which the larger pumps kicked in was increased, so that the smaller pump operated alone for longer. To avoid the need for physical testing (such as flow measurements), this increase in set point was made in small steps.

Second, the speed of the smaller pump was increased, to widen its useful operating range. This change was possible because the pump was driven by a variable frequency drive (VFD). The frequency supplied by the VFD was raised, without exceeding the motor’s nominal power and the pump’s capabilities.

The resulting flow, energy consumption and efficiency were subsequently tracked by the SAM4 platform. The effect of these two process changes was significant: all three pumps’ efficiency increased, raising the pumping station’s overall efficiency by 7.1 percent. The pump owner now spends € 2,500 less per year on energy thanks to these two quick, easy changes.

![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_table_two_last.png)















### Example 3: Open a valve


At a foul pump station, two submerged pumps operated continuously at very low flows, far from their BEP. After the SAM4 platform identified the issue, the pump owner investigated and found that both pumps were operating against partially closed discharge valves. They opened the valves and SAM4 tracked the effect in its real-time pump performance curve. After the change both pumps operated more efficiently, closer to BEP, and needed less runtime. This simple change is saving the pump owner approximately € 15,000 in energy and eliminating 30 metric tons of CO2 emissions annually.

![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_table_three_last.png)















### Example 4: Hydraulically rerate the pump


This one’s a little more involved than just opening a valve, but it’s still a relatively simple, low-cost fix that can deliver major savings.

At a very large booster pumping station, two 500 kW pumps were being operated at low loads. After analyzing the data, the SAM4 platform determined that changing the impeller size and adding a secondary volute would enable the pumps to deliver the required flow at lower power.

The pump owner made the changes and SAM4 tracked the results. The pumps’ efficiency more than doubled, from 23 to 55 percent, and the pump owner is spending € 100,000 less in energy and lowering their carbon footprint by 250 metric tons per year.

![](https://samotics.com/wp-content/uploads/2023/10/energy_blog_table_four_last.png)















## Willing to go a little further?


As we’ve seen above, energy intelligence systems can identify easy short-term changes that can save significant energy. And of course they’ll also recommend relevant longer-term, more expensive initiatives: replacing pumps with newer, more efficient versions, adding in VFDs or additional pumps, and so forth. But there are two additional strategies you might want to consider, which fall outside the scope of energy analytics.
### Implement a proactive maintenance program to keep your pumps in optimal condition


Pump health and pump efficiency go hand in hand. Changes that improve a pump’s efficiency also reduce wear and tear: for example, pumps operating near BEP experience less cavitation and put less stress on their mechanical seals. The reverse is also true: pumps that are well-maintained operate more efficiently. Bearing wear, misalignment and other common problems make the pump work harder, spending more energy to do the same job. The sooner you discover and fix these issues, the less energy the pump will waste. To minimize the time a pump spends silently wasting energy as its health degrades, consider moving to a [condition-based maintenance strategy](/blog/condition-monitoring-guide-to-the-5-major-technologies) based on real-time machine health data.
### Educate pump operators and maintenance personnel about energy-efficient practices


It only makes sense to train the people who spend the most time with your pumps on how to keep them at peak efficiency. In addition to the insights your energy intelligence platform will give them, consider incentivizing other opportunities such as pump optimization workshops, certification programs, conferences and seminars. You could also introduce performance-based recognition programs to motivate pump operators and maintenance personnel to adopt energy-efficient practices. These might include rewards, bonuses, or simply acknowledgment for individuals or teams that demonstrate outstanding commitment to energy conservation and optimization.

**Good luck!**

We hope this guide has given you some ideas you can start using today to lower your pumps’ energy consumption and emissions. Until we meet again on the road to Net Zero!

*[1] See *[*Energy efficiency in electric motor systems: Technology, saving potentials and policy options for developing countries*](https://downloads.unido.org/ot/99/28/9928083/WP11.pdf)* from the United Nations Industrial Development Organization. This paper reports that industrial pumps represent 20–25 percent of global industrial motor electricity consumption; we used the lower bound, 20 percent, in our calculation. Various sources report that centrifugal pumps represent 60–90 percent of all industrial pumps; most sources additionally report that the share of centrifugal pumps is growing. We used 80 percent in our calculation.*
