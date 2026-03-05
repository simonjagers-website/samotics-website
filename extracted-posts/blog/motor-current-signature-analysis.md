---
title: "Motor Current Signature Analysis (What And How?)"
slug: "motor-current-signature-analysis"
date: "Thu, 01 Aug 2019 11:24:53 +0000"
category: "Blog"
category_slug: "blog"
tags: []
original_url: "https://samotics.com/blog/motor-current-signature-analysis"
images: 2
word_count: 1301
---

For many years the condition monitoring industry relied on vibration analysis and other traditional techniques to identify developing faults in electric motors. In recent years, however, condition monitoring based on motor current signature analysis (MCSA) has begun to provide a more effective and efficient alternative to traditional techniques.

Using an electrical submersible pump as an example, this article will explain how MCSA is revolutionizing the condition monitoring industry.

Electrical submersible pumps (ESPs) play a crucial role in oil and gas operations. When a reservoir has insufficient energy to produce oil at economic rates, an artificial lift method is required to increase fluid flow. Electric submersible pumping is one of the most versatile and adaptable options for moderate to high fluid volumes.

Unfortunately, the conditions encountered in some wells can be very hostile and this often has an adverse effect on both a pump’s reliability and any monitoring sensors associated with it. ESP failures may be caused by the presence of solids (fine rock particles) from the reservoir, abrupt changes in well conditions, the presence of free gas in the pump, corrosion or elevated operating temperatures.

When an ESP fails it can have a catastrophic effect on operations, incurring the high costs associated with loss of production and the replacement of assets. It is critical, therefore, to mitigate these risks. MCSA uses advanced algorithms to analyze current and voltage data and provide early diagnosis of ESP problems.
## Monitoring and maintenance strategies


Most of the maintenance regimes currently used by the oil and gas industry revolve around time-based strategies or traditional [condition-based maintenance](https://www.samotics.com/condition-based-maintenance) techniques.

Time-based maintenance often creates additional costs (for example, unnecessary shutdowns when checks are made too early) and accepts unplanned downtime as a real possibility (component failure when checks are made too late).

In contrast, the aim of condition-based maintenance is to perform repair work before failure occurs, typically when a drop in ESP performance is recorded. Condition-based maintenance (CBM) is the optimal maintenance strategy for ESPs because it requires maintenance to be performed before breakdowns occur or when performance decreases, but not before. CBM requires accurate, reliable and cost-effective condition monitoring mechanisms. This is where traditional tools fall short. In traditional condition-based maintenance systems, vibration or temperature sensors are installed on or near the pump (which is located underground). These measure parameters such as motor temperature, pump discharge temperature, pump intake pressure, pump discharge pressure and motor vibration. However, installing sensors on a submerged pump that operates in harsh conditions below the surface of the earth is often challenging and expensive. It can be difficult to ensure the physical integrity of the components such as the sensors and the cables that transmit data from the ESP to a surface station.

Additionally, time-based and traditional condition-based maintenance both require a great deal of manual data analysis. This places the burden of interpretation on technical staff who will doubtless have many other demands on their time.

Fortunately, there is an alternative. [Online condition monitoring](https://www.samotics.com/what-is-condition-monitoring) tools based on a combination of motor current signature analysis and machine-learning algorithms offer an efficient and cost-effective solution that addresses the unique challenges facing oil and gas operators, as well as many other industries.
## Motor current signature analysis


The MCSA concept originated in the early 1970s when it was proposed as a tool for monitoring motors in hazardous areas or harsh environments within nuclear power plants. It is a condition monitoring technique that can diagnose problems in induction motors by analyzing current and voltage data . MCSA sensors are installed inside the motor control cabinet (MCC) and data is collected online without interrupting production.

![](https://samotics.com/wp-content/uploads/2019/08/Motor-Current-Signature-Analysis-Thumbnail.jpg)









For engineers the recognition of motor current fault signatures would require a considerable degree of expertise and experience, but modern MCSA tools take care of that. The online system delivers an automated interpretation using powerful artificial intelligence algorithms that detect and diagnose imminent failure in AC induction motors and pumps.














## A surface solution for downhole systems


In contrast to traditional ESP condition-monitoring tools, which place sensors downhole, all of the hardware for an MCSA system is installed in the motor control cabinet (MCC). This is a much more appropriate environment for precision instruments.

MCSA sensors can be installed in less than an hour per motor and will collect data under all operating conditions. This ensures the continuous streams of high-quality data that automated condition monitoring tools rely on.
## Basic principles


ESPs are powered by AC induction motors. Electrical power moves a rotor inside a stator to turn electrical energy into mechanical energy. The functioning motor will then create a set of vibration patterns which cause ripples on the current sine wave. Current sensors can pick up this analog signal and turn it into a digital data stream for further analysis.

Algorithms convert the data into a pattern of behavior that defines the range of sine wave shapes and ripples that occur under normal, healthy circumstances. Anomaly detection algorithms can then track changes over time and identify “unhealthy” deviations that cannot be explained by operational factors such as changes in load and power.
## Anomaly detection


When anomaly detection algorithms flag behavior outside the normal “healthy” pattern for the ESP it indicates behavior that warrants inspection of the motor and pump.

The commercial value of the MCSA approach is most obvious in a site where the engineering team has to monitor dozens or even hundreds of pumps. In a traditional scenario, this would require visits to each pump to conduct manual inspections. This is a labor-intensive process and an inefficient use of scarce technical staff resources (manual inspections can also carry additional safety risks). The MCSA-based system enables operators to avoid these issues.

Anomaly detection algorithms can indicate which pumps are behaving normally and which have shown the highest deviations from the expected patterns. This helps the maintenance team to prioritize the assets that are most likely to require urgent attention. But that’s not all; the MCSA-based system can also indicate the likely cause of a problem.

![](https://samotics.com/wp-content/uploads/2019/08/mcsa-condition-monitoring-blog-graph_1400w.jpg)








## Fault classification


MCSA classification algorithms recognize patterns associated with specific failure mechanisms. For example, pump cavitation shows a distinctly different pattern from bearing damage or stator failures. Different failure mechanisms leave distinct marks on the current sine wave, which can already point the maintenance team to the probable cause of the motor fault.

The major faults of electrical machines that can be identified by MCSA include:


 	- Air-gap eccentricity: a non-uniform air gap between the rotor and the stator

 	- Broken rotor bars that can cause sparking and overheating

 	- Bearing damage

 	- Cavitation

 	- Shorted turns in stator windings

 	- Load effects

 	- Equipment wear effects



The latest developments in artificial intelligence can leverage what is called “transfer learning” to apply failure patterns to different assets. This means that the fingerprint of stator failure in a large motor can be used to detect the same issue in a smaller system. In some cases it is even possible to use a failure mechanism pattern from one equipment type to identify the same issue in a different equipment category.
## Conclusion


An MCSA-based condition monitoring tool for ESPs can reduce unplanned downtime, lower maintenance costs and help operators minimize safety and environmental risks. The latest generation of MCSA-based condition monitoring tools offer unique monitoring capabilities for ESPs because the sensor system is installed inside the MCC, rather than on the asset.

The emergence of powerful artificial intelligence algorithms, improved data transfer protocols and cheap, powerful computing have made MCSA-based systems an attractive option.

MCSA-based systems have the potential to greatly improve data accuracy and reliability while lowering the costs of monitoring at scale. The elimination of unplanned downtime is now within reach.
## References


1. Brief review of motor current signature analysis, D. Miljković. (2015) [https://www.researchgate.net/publication 304094187_Brief_Review_of_Motor_Current_Signature_Analysis](https://www.researchgate.net/publication 304094187_Brief_Review_of_Motor_Current_Signature_Analysis) (Accessed 26.07.2018)
