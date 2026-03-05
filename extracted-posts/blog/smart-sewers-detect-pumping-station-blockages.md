---
title: "Smarter sewers: Detecting pumping station blockages with real-time asset health data"
slug: "smart-sewers-detect-pumping-station-blockages"
date: "Wed, 10 Apr 2024 08:10:01 +0000"
category: "Blog"
category_slug: "blog"
tags: ["Wastewater"]
original_url: "https://samotics.com/blog/smart-sewers-detect-pumping-station-blockages"
images: 3
word_count: 1505
---

Blockages in sewage pumping stations are a prime root cause of pollution incidents. A recent analysis of combined sewer overflow events in England found that almost one in five of all incidents took place at pumping stations [1]. That means that detecting and preventing blockages at pumping stations offers a huge opportunity to reduce pollution events. 
## Sewage pump blockages


Sewage pumps play a vital role in the wastewater distribution network. Unfortunately, it's all too easy for these important assets to become blocked. One of the major culprits are blockages from non-biodegradable items like wet wipes, diapers, cotton swabs and hardened oil. These items, mistakenly flushed or poured down drains, accumulate and form "fatbergs" that restrict the flow of wastewater. Another culprit is that sometimes hard objects like stones, toys or even twigs can damage the pump’s components. In other cases, a blockage can lead to a motor tripping or pump breaking down unexpectedly. In any case of clogging or equipment failure, there is a danger that wastewater, instead of being transported away, will build up inside the well and flood the surrounding area, leading to a pollution incident.
## Direct and indirect solutions


There are several direct and indirect solutions available to water utilities today that would help prevent pumping station blockages. Many water companies around the world are already investing a lot of resources in increasing the resilience of the wastewater system by building new infrastructure, redesigning the network to separate stormwater from sewage, investing in green infrastructure and much more. Likewise, a concerted consumer education campaign could lower the number of these incidents by reducing the amount of inappropriate materials being flushed down the toilets and drains, causing sewage pipes and sewage pumps to become clogged. Until consumers change their behavior, the only direct option available for wastewater utilities is to detect and resolve pump blockages before they cause an overflow. That’s where real-time asset health monitoring and analytics solutions are already playing a big part today, enabling water companies to deal with blockages in a timely manner.
## Electrical signature analysis (ESA) monitoring


Traditionally, wastewater companies undertake thousands of visits per year to preventively lift, inspect and unblock sewage pumps. This creates a significant operational and logistical challenge, with a high risk of unexpected failures occurring in between the visits. But what if there was a way to reliably track pump clogging from afar, even for submerged pumps in wet wells? 

This may sound like wishful thinking, but there's a robust fault detection technology that does exactly that. It's called electrical signature analysis (ESA). As its name suggests, ESA measures the voltage and current being supplied to the motor driving the pump or other equipment to accurately track the whole machine’s health. Because ESA captures electrical signals, its sensors are non-invasive current and voltage probes that install around the phase wires in the safety of the motor control cabinet, not on the pump itself. That means ESA sensors will never be exposed to the corrosive, abrasive conditions a submerged pump operates in. This technology makes it possible to provide accurate and usable insights into equipment that was difficult or even impossible to monitor before. Combined with wireless sensors and machine learning, 21st-century ESA solutions have the potential to spot early asset health degradation and pump clogging. 
## ESA and blockage detection


Both electrical and mechanical faults affect the current and voltage signals, and each fault has its own characteristic "signature." The same applies to pump clogging, which also produces a specific signature in the electrical data. When this is combined with knowledge of the motor's characteristics and machine learning algorithms, it can help ESA systems detect as well as localize pump blockages at an early stage.

**RELATED READING: **[Use advanced analytics to detect pump clogging remotely, preventing pollution incidents and leading to optimized maintenance planning .](https://samotics.com/kb/sam4-clogging-explainer/)
## Three benefits of clogging detection technology


At the request and with contributions from our customers, we co-engineered a [blockage detection feature](https://samotics.com/features/pump-blockage-detection/) as part of our [SAM4 Health](https://samotics.com/products/sam4-health) solution to provide early warnings of clogging events. Since the feature's launch, our customers have used the resulting system alarms to prevent numerous potential pollution incidents. This blog will explore how these three real-world situations demonstrate the benefits of blockage detection technology on the road to zero pollution incidents. 
### Benefit 1: Prioritize maintenance based on the status of the whole pumping station


One customer had a sewage pumping station with two co-located pumps operating in an alternating duty-standby regime. One night, the SAM4 data detected signs of a blockage forming in one of the pumps. Analysis confirmed that one pump had a persistent partial blockage while the other was fine. After 48 hours of close monitoring, the customer received a medium-priority alert that notified them of the ongoing clogging and recommended maintenance the following week.

A week later, the other pump began to show signs of clogging. As this could risk a pollution event, a red alert was sent to the customer. They confirmed what the SAM4 clogging detection feature had found: both pumps were partially blocked. This reliable insight into ongoing developments, taking into account the setup of the whole pumping station, allowed the customer to plan its maintenance, as well as take emergency action when it was necessary. ​​These detections also avoided €40k in maintenance costs and an estimated €150k pollution fine.

[*](https://samotics.com/wp-content/uploads/2024/02/YW_case_visual_2-2-e1708358612408.png) From the graph below, it is clear to see the resolution of both clogging incidents. Once the maintenance crew removed the blockages, the continuously high clogging scores on pump 2 and the signs of developing clogging on pump 1 dissipated reverting to healthy clogging score levels.
### Benefit 2: Pinpoint exactly where the blockage is forming


The SAM4 Health system noted increased clogging scores on a pump at another two-pump station. When the clogging scores remained consistent over a long monitoring period, the customer scheduled a full inspection by the OEM engineers. Prior to the visit, our expert analysts did a deep dive into the data and were able to pinpoint the problem.

Analysis indicated a consistent increase in the spectral energy around the supply frequency and a sudden change in active power, which are indicators for cavitation. Based on this data, we advised that the blockage was forming outside of the pump and recommended the customer to check the inlet and the discharge side of the pumping station for any obstruction. The inspection confirmed that the inlet of the pump was blocked. The asset was shut down for maintenance. After the customer cleaned the well and the inlet of the pump, Samotics' system confirmed that the pump had returned to healthy behavior.

[![Clogging scores when Yorkshire Water is inspecting pump 2. Only scores of pump 1 show](https://samotics.com/wp-content/uploads/2024/04/YW_case_visual_3-1-e1712737687164.png)](https://samotics.com/wp-content/uploads/2024/04/YW_case_visual_3-1.png) Plot of pump 1 and 2 showing normal clogging scores resuming following well cleaning. *
### Benefit 3: Ensure reliable asset insight


A sewage pumping station had two co-located pumps that were monitored by telemetry systems as well as Samotics' asset monitoring solution. One day, the telemetry systems showed one of the pumps had tripped. This would not normally constitute an emergency, as the other pump could maintain operations at the site until maintenance could be planned.

However, SAM4 Health detected clogging in both pumps. This prompted an emergency response, as a blockage in both pumps was a severe risk for a pollution event. The emergency maintenance team confirmed that both pumps were clogged and that the telemetry systems had experienced a transient issue that led the customer to believe that the pumping station reached the desired flow when it didn't.

[![High clogging scores detected by SAM4 at pump 1(green) and pump 2 (pink) which return to normal after maintenance.](https://samotics.com/wp-content/uploads/2024/04/YW_case_visual_4-1-e1712737509903.png)](https://samotics.com/wp-content/uploads/2024/04/YW_case_visual_4-1-e1712737509903.png) Plot of pump 1 and 2 showing normal clogging scores resuming following maintenance intervention.

According to our customer, they would have experienced a pollution event at this station without the clogging detection feature. This would have caused significant environmental and reputational damage, in addition to around €40k in maintenance costs and an estimated €150k pollution fine. 
## Pollution prevention


Water companies need every tool in their arsenal to combat their growing challenges. Pollution prevention is an especially stark challenge, both on a business and community level. Sewage pumping stations play a crucial role in preventing these events, which makes their maintenance crucial.

Pumping station equipment is also difficult to reach, due to the remoteness of the stations or the fact that the pumps are submerged. That makes accurate insight into the pumps’ real-time status a game changer. Not only can pollution events be averted, but maintenance resources can also be optimized and used more efficiently. 

Clogging detection technology can be key to preventing these emergencies while more efficiently maintaining pumping stations. If you’re curious about how this works in practice, why not [take a tour of our technology](https://samotics.com/tour) or [read more about ESA](https://samotics.com/kb/the-esa-explainer/)?
## Footnotes


[1] T. Giakoumis and N. Voulvoulis, [Combined sewer overflows: relating event duration monitoring data to wastewater systems’ capacity in England](https://pubs.rsc.org/en/content/articlepdf/2023/ew/d2ew00637e) (Environ. Sci.: Water Res. Technol., 2023, 9, 707).
