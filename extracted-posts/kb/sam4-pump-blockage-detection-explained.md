---
title: "SAM4 pump blockage detection explained"
slug: "sam4-pump-blockage-detection-explained"
date: "Tue, 24 Jan 2023 09:21:30 +0000"
category: "Knowledge base"
category_slug: "kb"
tags: []
original_url: "https://samotics.com/kb/sam4-pump-blockage-detection-explained"
images: 5
word_count: 1136
---

Find out how SAM4 assists water and wastewater companies detect pump blockages remotely with advanced analytics. Prevent pollution events, reduce maintenance costs, and optimize operational efficiency with automated blockage detection.
## Better pump blockage detection for wastewater companies


Resolving and preventing sewage pump blockages is a significant operational challenge for wastewater companies. Currently, thousands of on-site visits are required to preventively inspect and reactively unblock these pumps each year. Our customer expressed the need for a solution to reliably monitor pump blockages remotely to transform their maintenance strategies. With SAM4 Health already monitoring their pumps, we developed an automated blockage detection feature that tracks blockages events remotely.

Since it has been launched, SAM4's blockage detection feature has identified hundreds of pump blockages, allowing our customers to make data-driven changes to their operational strategies. Alongside our customer’s usage, we continuously develop our blockage detection feature to match their evolving needs. On this page, we explain how SAM4's blockage detection feature works and show a real-world example from September 2022.

[![](https://samotics.com/wp-content/uploads/2023/01/SAM4-blockage-deetection-explained.png)](https://samotics.com/wp-content/uploads/2023/01/SAM4-blockage-deetection-explained.png)
## How SAM4's blockage detection works


SAM4 Health is part of our SAM4 industrial analytics platform, powered by electrical signature analysis (ESA). ESA, developed in the 1980s, is a suite of tools used to monitor the health of critical equipment from a distance. SAM4 brings ESA into the 21st century using AI and wireless sensors that capture high-frequency data from motor control cabinets. This data provides early warnings of asset health degradation, such as the start of a blockage event. (Read more about how ESA works in our [ESA Explainer](https://3777718.fs1.hubspotusercontent-na1.net/hubfs/3777718/website-resources/esa-explainer.pdf?utm_source=samotics&utm_medium=pdf&utm_campaign=clogging-feature-explainer&utm_content=&utm_term=).)
## Machine learning in SAM4 to detect pump blockages


SAM4 Health uses machine learning to detect pump blockages by analyzing subtle changes in electrical signals (current and voltage). SAM4’s AI models identify the early stages of clogging and can even pinpoint which component is degrading. Both electrical and mechanical faults impact these signals, each producing a unique "signature." SAM4's AI is trained to recognize these distinct patterns, enabling precise and timely blockage detection.

In addition, SAM4 Health’s blockage detection model analyzes multiple features simultaneously to determine not only when a blockage is developing but also where it is occurring. With real-time monitoring, SAM4 provides alerts to customers, allowing them to intervene promptly and avoid more serious operational issues.
## Technical deep dive: inside SAM4’s pump blockage detection model


The data captured by SAM4’s current voltage sensors undergoes a feature extraction phase. For that basic signal processing calculates key metrics related to the mechanical and electrical health of both the pump and its motor. For example, one feature may isolate data components around the supply frequency, while another focuses on frequencies related to the motor’s rotational speed. Each of SAM4 Health’s fault detection models uses one or more of these features, depending on the fault it is designed to detect. These detection models are where the machine learning (or “artificial intelligence”) takes place, enabling precise and efficient identification of issues.

When a new pump is first connected to SAM4 Health, the system begins by collecting initial data to train SAM4’s detection models on what normal operating behavior looks like for that specific pump. In the case of the blockage detection model, this training helps define the key features of the pump's performance when no blockage is present. Once the model is fully trained, any deviations from these expected patterns will trigger SAM4 to generate an automated blockage alert, allowing for early detection and intervention.

Because the SAM4 pump blockage detection model analyzes multiple features simultaneously, it can accurately detect a developing blockage in its exact location.

For example, an increase in noise around the pump’s supply frequency combined with a drop in load indicates a blockage between the impeller and the motor. Whereas shifts in other indicators suggest a blockage in the volute. SAM4’s advanced blockage model processes all incoming data to determine not only when blockages occurs but also its precise location, ensuring efficient and targeted maintenance.

*![](https://samotics.com/wp-content/uploads/2023/01/Scherm­afbeelding-2024-10-30-om-14.04.52.png)*

Once the AI model flags a developing blockage, SAM4 then looks at the status of the entire pumping station to determine when and what severity it should report to the customer. For example, if one pump out of three is blocked and the other two are operating normally, SAM4 will issue a low-priority notification. However, if another pump starts showing signs of trouble, SAM4 will send a high-priority alert. This automated process streamlines notification prioritization, enabling customers to plan the most efficient and effective maintenance response.

![](https://samotics.com/wp-content/uploads/2023/01/Scherm­afbeelding-2024-10-30-om-14.05.05.png)

Note that blockages is only one of many issues the second pump might encounter — all of SAM4 Health’s other detection models are also continuously running, simultaneously tracking other electrical and mechanical faults such as voltage imbalance, impeller damage and misalignment. Detecting these problems at an early stage, does not onlz reduce total maintenance cost and environmental impact, but also extends machine lifetime and raises efficiency for the long term.
## Blockage feature in action: early alert for developing blockage incident across two pumps


At a sewage pumping station two co-located pumps operate in an alternating pattern to meet required demand and provide system redundancy. One night, one of the pumps (Pump 2), displayed characteristics of a pump blockage. This was indicated by continuously high blockage scores since the start of the incident as can be seen in Figure 3.

![](https://samotics.com/wp-content/uploads/2023/01/Scherm­afbeelding-2024-10-30-om-14.05.19.png)

With one other functioning pump at the station, this did not trigger an emergency response. The situation was monitored for 48 hours to determine if the blockage would clear on its own or require intervention. With no improvement seen at the end of this monitoring period, an orange alert was generated and sent to the customer indicating a blockage incident at the pump. The alert stated that same-day action was not required and that the situation could be resolved in the following week without disrupting pump station operations.

Approximately one week later, data revealed signs of developing blockages in the other pump at the station (Pump 1). With both pumps blocked, an emergency response was necessary due to the increased risk of a potential pollution event. Consequently, a red alert notification was sent to the customer, indicating the urgency of the situation.

A maintenance team was promptly dispatched to the site and removed both pumps from the pumping station. They confirmed that both pumps were partially blocked, validating the clogging detections made by SAM4 Health’s automated clogging feature. Once the blockages were cleared and the pumps were reinstalled, the blockage scores and other operational metrics returned to healthy levels, as shown in Figure 4.

![](https://samotics.com/wp-content/uploads/2023/01/Scherm­afbeelding-2024-10-30-om-14.05.31.png)

The SAM4 automated blockage detection feature successfully pinpointed the developing issues. It provided continuous insight into the severity of the situation and alerted to when action needed to be taken. **This enabled the customer to optimize maintenance planning and prevent a potential pollution event from occurring.**
