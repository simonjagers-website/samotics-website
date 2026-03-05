---
title: "How SAM4 detects developing faults in industrial pumps"
slug: "how-sam4-detects-developing-faults-in-industrial-pumps"
date: "Tue, 27 Aug 2024 15:24:40 +0000"
category: "Knowledge base"
category_slug: "kb"
tags: ["Knowledge Base"]
original_url: "https://samotics.com/kb/how-sam4-detects-developing-faults-in-industrial-pumps"
images: 29
word_count: 3028
---

SAM4 is an asset health monitoring system based on AI-driven voltage and current analysis. In this report, we explain how SAM4 detects common faults in industrial pumps using actual results from anonymized SAM4 data, to help engineers evaluate SAM4’s value for their own operations.
## How SAM4 works


SAM4 performs AI-driven electrical signature analysis (ESA). ESA is based on the fact that subtle changes in a machine’s operation affect the connected motor’s magnetic field, which then affects the supply voltage and operating current. Using a variety of analytical techniques, ESA provides a detailed picture of what’s going on across the drive train, from motor to transmission to load.

[![](https://samotics.com/wp-content/uploads/2024/08/Visual-about-how-SAM4-works.png)](https://samotics.com/wp-content/uploads/2024/08/Visual-about-how-SAM4-works.png)

SAM4 uses the first four weeks of current and voltage measurements to build a model of the connected asset’s normal operating behavior. When a fault begins to develop, the current & voltage signals will change. By analyzing this change, SAM4 can determine:


 	- the **presence** of a developing fault.

 	- the specific **type** of fault.

 	- **how long you have** until that fault causes a failure.



Once SAM4 detects a developing fault, we will alert you in two ways: through a traffic-light analysis in the online dashboard, and through an email with details on the changes we have observed. These alerts will also recommend next steps to resolve the specific fault at play.
## SAM4's traffic light notification system


SAM4 uses a four-color traffic light on the customer dashboard to represent the asset’s current condition, with a detailed analysis.

1. **Green** means the asset is operating normally. The customer is not contacted.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-operating-normally.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-operating-normally.png)

2. **Yellow** means an early-stage anomaly has been detected. No immediate action is required. The customer is contacted by email and notified of the new situation. This notification will be repeated once a month as long as the asset’s status remains yellow.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-early-stage-anomaly-detected.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-early-stage-anomaly-detected.png)

3. **Orange** means the anomaly has reached a severity that requires action. The failure mechanism should now be detectable upon inspection. The customer is contacted by email and advised to inspect the asset. This notification will be repeated once a week as long as the asset’s status remains orange.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-anomaly-reached-severity.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-anomaly-reached-severity.png)

4. **Red** means the anomaly has reached a severity that requires immediate action. The customer receives an email and a phone call advising them to service the asset as soon as possible. This notification will be repeated daily as long as the asset’s status remains red.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-immediate-action-required.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-traffic-light-immediate-action-required.png)
## SAM4's pump performance dashboard


Because SAM4 measures current and voltage, it can calculate a pump’s instantaneous head and flow using the affinity laws and the reference curve supplied by the customer. SAM4’s calculated metrics include a real-time pump performance curve, which shows the pump’s actual operation relative to its best efficiency point (BEP), and a real-time power curve. This information also informs SAM4’s fault prediction and energy insights.

[![SAM4's pump performance dashboard](https://samotics.com/wp-content/uploads/2024/08/SAM4-pump-performance-dashboard.jpg)](https://samotics.com/wp-content/uploads/2024/08/SAM4-pump-performance-dashboard.jpg) SAM4’s pump performance dashboard displays a pump’s actual operation relative to its best efficiency point for any desired time range, enabling early intervention (for example, to stop cavitation) as well as long-term insights to help save energy and extend pump lifespan.
## What SAM4 can detect


SAM4 can detect electrical and mechanical failures in each stage of the transmission path, from electrical supply through load.
### Power grid & VFDs


SAM4 can detect and discriminate between changes related to the electrical grid and changes related to the variable frequency drive (if present).


 	- Voltage / Current unbalance

 	- Voltage / Current harmonic distortion

 	- Voltage drops* / overvoltage

 	- Power quality issues



Because SAM4 samples the data stream at discrete intervals, very short sags (dips) and surges may not always be detected.
### AC motors


SAM4 detects both electrical & mechanical faults arising in 3-phase AC motors of any voltage.


 	- Interturn / Turn-to-turn stator shorts

 	- Stator winding looseness

 	- Electrical unbalance

 	- Broken / Loose rotor bars

 	- Rotor eccentricities

 	- Misalignment

 	- Soft foot

 	- Bearing degradation

 	- Mechanical unbalance



### Transmission


SAM4 detects mechanical faults arising in the power transmission device.


 	- Coupling eccentricity / unbalance

 	- Broken / Cracked gear teeth

 	- Gear misalignment / eccentricities

 	- Pulley unbalance

 	- Belt / Chain wear



### Load


SAM4 works on a wide variety of applications including the following common asset types:


 	- Centrifugal & vane pumps

 	- Conveyors

 	- Fans & blowers

 	- Mixers & agitators

 	- Rolls



SAM4 also works on many industry-specific applications, such as paper folding machines, centrifuges, cranes, blowout preventers, churners and so forth. (Please ask if you don’t see yours in the list.)

SAM4 can detect the following common machine faults:


 	- Cavitation

 	- Impeller damage

 	- Mechanical unbalance

 	- Misalignment



(Note that these faults relate to the machine itself; coupling/gearbox/etc. faults are covered under Transmission, and electrical faults are covered under AC motors.)
For many applications, SAM4 can detect additional failure modes of interest.
## What SAM4 can't do


SAM4 is designed for synchronous* and asynchronous 3-phase AC motors of any voltage**. It cannot be used for systems driven by other means, including:


 	- DC motors

 	- Servo motors

 	- Steam turbines



(VFDs are fine—SAM4 works very well with the pulse-width modulated signals produced by variable frequency drives to synthesize AC current.)

To monitor components beyond the motor, SAM4 must be able to measure their impact in the current and voltage signals. The farther down the drive train a component is, the less information SAM4 will have. Assets like pumps, conveyors, rolls and fans generally have relatively short drive trains with a limited number of rotating components and simple drive systems.

Assets like compressors, presses and packaging machines generally have relatively long drive trains with multiple rotating components and complex drive systems. Sometimes all SAM4 needs is more time to analyze the situation; sometimes there just isn’t enough information for SAM4 to work with. We’re happy to help you determine how suitable SAM4 is for the specific systems and failure modes you need to monitor.

In general, systems that use localized on-asset sensors (such as vibration, acoustic emission and temperature sensors) may be a better choice for components connected to the motor through a flexible coupling that absorbs shock and components that are many steps away from the motor.

Of particular importance for higher-voltage motors: SAM4 does not currently detect partial discharge.

* Other systems are better for two-pole synchronous motors, where the electrical harmonics align with and overwhelm the mechanical fault frequencies.

** As long as the voltage transformer has a low voltage ( **DID YOU KNOW?**
> 
> By incorporating industry- and customer-specific configuration details, SAM4 can tailor its diagnosis and recommendations to the specific situation in which the connected asset is running.


## Examples of developing faults in industrial pumps


### Cavitation


While cavitation is not an immediate cause of pump failure, over time it will damage impellers, bearings and seals. This root cause of component degradation can typically be identified by an increase in the current spectrum’s noise floor, particularly around the supply frequency. Real-time assessment of the pump’s operation relative to its best efficiency point (BEP) is a supporting metric.

[![](https://samotics.com/wp-content/uploads/2024/08/Spectral-energy-healthy-vs-cavitating-pump.png)](https://samotics.com/wp-content/uploads/2024/08/Spectral-energy-healthy-vs-cavitating-pump.png) The spectral energy for a healthy (black) vs. cavitating (blue) pump.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-cavitating-pump-heat-map.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-cavitating-pump-heat-map.png)

**For the image above and below:** sample SAM4 dashboard analyses for a cavitating pump. The use of either high flow or low flow depends on the location of the real-time data points on the pump’s associated performance curve.

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-cavitating-pump-current-noise-floor.png)
](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-cavitating-pump-current-noise-floor.png)
#### Example 1: Cavitating condensate pump


Changes in this motor’s spectral energy at the fundamental train frequency (FTF, also called the bearing cage frequency) ultimately led SAM4 to diagnose cavitation. Figure 2 shows the pump’s energy over time at two operating points: at a higher power (black) and at a lower power (blue). The elevated readings at the lower (blue) operating point indicate possible cavitation and/or bearing degradation. Our data scientists then examined SAM4’s real-time pump curve and the frequency domain noise floor to confirm cavitation.

[![](https://samotics.com/wp-content/uploads/2024/08/The-spectral-energy-at-the-FTF-at-two-operating-points.png)](https://samotics.com/wp-content/uploads/2024/08/The-spectral-energy-at-the-FTF-at-two-operating-points.png)

Figure 3. The spectral energy at the FTF at two operating points. The graph records abnormal values at the blue (lower power) operating point but not the black (higher power) one, indicating possible cavitation at the blue operating point. A comparison in the frequency domain revealed an elevated noise floor around the supply frequency, also indicative of cavitation. (Note: the graphs in this report have been anonymized. Actual SAM4 graphs include values on both axes.)

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-real-time-pump-curve.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-real-time-pump-curve.png)

Figure 4. SAM4’s real-time pump curve for this pump, with its best efficiency point (BEP) at 100% speed marked by the green triangle. The green swath marks the window of acceptable performance. The data points when the pump is operating at lower power fall well to the left of this window, in an area known to be sensitive to cavitation.
#### Example 1: Cavitating product pump


A temporary increase in the noise floor prompted us to alert the customer. SAM4 continued to detect intermittent periods of increased energy in the noise floor, across multiple operating points. The customer inspected the pump and discovered a clogged filter. Once the filter was cleaned, the pump stopped cavitating.

[![](https://samotics.com/wp-content/uploads/2024/08/Heat-map-showing-changed-in-energy.jpg)](https://samotics.com/wp-content/uploads/2024/08/Heat-map-showing-changed-in-energy.jpg)

Figure 5. A heat map showing changes in energy related to cavitation in the pump. The horizontal axis is frequency; the vertical axis is time, from oldest date at the top to most recent date at the bottom. The color indicates energy, from high in red to low in blue. The blurry areas reveal cavitation, which was intermittent at first (top of graph) and grew more frequent over time (center of graph). Inspection revealed a clogged filter; once it was cleaned, the cavitation stopped (bottom of graph).
#### Example 3: Cavitating submersible cooling tower pump


SAM4 observed a sudden increase in energy at the motor’s rotational frequency for one of the pump’s operating points. Over the next few days the energy gradually continued to rise at the rotational frequency. An inspection of the full frequency spectrum revealed that the noise floor around the supply frequency had also increased. We alerted the customer to probable cavitation. The customer closed the valve slightly in response, which stopped the cavitation. Energy levels subsequently returned to normal. The customer noted that SAM4’s analysis was particularly helpful for this pump, whose permanently underwater location makes inspection difficult.

[![](https://samotics.com/wp-content/uploads/2024/08/Pump-spectral-energy-during-healthy-operation.png)](https://samotics.com/wp-content/uploads/2024/08/Pump-spectral-energy-during-healthy-operation.png)

Figure 6. The pump’s spectral energy during healthy operation (black) and cavitating (blue). Note the increased noise floor around the supply frequency (the largest peak in the graph).

[![](https://samotics.com/wp-content/uploads/2024/08/Unhealthy-cavitating-behavior-returned-to-normal.png)](https://samotics.com/wp-content/uploads/2024/08/Unhealthy-cavitating-behavior-returned-to-normal.png)

Figure 7. After the customer adjusted the valve, the pump’s unhealthy cavitating behavior (blue) returned to normal healthy behavior (black).
#### Example 4: Pump vanes damaged by prolonged cavitation


SAM4 observed an increased noise floor in the current spectrum and alerted the customer that the pump was cavitating. The noise floor continued to gradually rise. Three months after SAM4’s first warning, the customer replaced the pump’s vanes, which had been damaged by the cavitation.

[![](https://samotics.com/wp-content/uploads/2024/08/Pump-spectral-energy-noise-floor-increase.png)](https://samotics.com/wp-content/uploads/2024/08/Pump-spectral-energy-noise-floor-increase.png)

Figure 8. The pump’s spectral energy when the noise floor first began to increase (blue), two months later (black), and three months later (green), just before the customer replaced the vanes.
#### Example 5: Mechanical seal damaged by prolonged cavitation


SAM4 began flagging occasional cavitation five months before a sustained increase in the current spectrum noise floor and a drop in active power indicated that a more acute problem was developing. The customer inspected the pump and found that its mechanical seal was beginning to leak. They replaced the seal and the pump’s performance returned to normal.

[![](https://samotics.com/wp-content/uploads/2024/08/Spectral-energy-for-healthy-pump-when-seal-began-to-leak.png)](https://samotics.com/wp-content/uploads/2024/08/Spectral-energy-for-healthy-pump-when-seal-began-to-leak.png)

Figure 9. The spectral energy for the healthy pump (blue) and five months later (black), when the seal began to leak.[![](https://samotics.com/wp-content/uploads/2024/08/Heat-map-showing-changes-in-energy-related-to-cavitation-in-the-pump.jpg)](https://samotics.com/wp-content/uploads/2024/08/Heat-map-showing-changes-in-energy-related-to-cavitation-in-the-pump.jpg)

Figure 10. A heat map showing changes in energy related to cavitation in the pump. The horizontal axis is frequency; the vertical axis is time, from oldest date at the top to most recent date at the bottom. The color indicates energy, from high in red to low in blue. The areas circled in red are when the pump was cavitating.
### Mechanical indicators (not related to cavitation)


Failing components leave distinct signatures in the current and voltage signals at frequencies related to their geometry. For example, roller bearing issues can be identified by changes in energy at the bearing’s ball pass, ball spin, and cage frequencies, which depend in part on the number of rollers and their size.

[![](https://samotics.com/wp-content/uploads/2024/08/Spikes-around-supply-frequency-indicate-developing-bearing-damage.png)](https://samotics.com/wp-content/uploads/2024/08/Spikes-around-supply-frequency-indicate-developing-bearing-damage.png)

Figure 11. Spikes around the supply frequency at this bearing’s characteristic frequencies indicate developing bearing damage (blue = healthy, black = bearing damage, green = after replacement).

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-analyses-for-two-different-mechanical-faults.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-analyses-for-two-different-mechanical-faults.png)

Figure 12. Sample SAM4 dashboard analyses for two different mechanical faults.
#### Example 6: Multiple mechanical faults


SAM4 observed an increase in energy at multiple harmonics of the pump’s rotational frequency, as well as an increased noise floor. The customer found three degraded components upon inspection a month later: a spider coupling was worn out, vanes were stuck, and the foundation bolts were loose.

[![](https://samotics.com/wp-content/uploads/2024/08/Comparing-pump-spectral-energy-when-healthy-and-unhealthy.png)](https://samotics.com/wp-content/uploads/2024/08/Comparing-pump-spectral-energy-when-healthy-and-unhealthy.png)

Figure 13. Comparing the pump’s spectral energy when healthy (blue) and unhealthy (black). Note the periodic nature of the increases; these peaks correspond to the pump’s rotational frequency and its harmonics. Note also the increased noise floor throughout the spectrum.
#### Example 7: Gearbox-motor misalignment on circulator pump


SAM4 flagged a sudden increase at the rotational frequency of the gearbox’s outgoing axle, which is indicative of misalignment. We notified the customer and put the pump on orange alert, for close tracking by our data science team. We updated the customer weekly as the energy gradually continued to rise.

Seven months after our first alert, the customer’s preventive maintenance cycle confirmed radial and axial misalignment between the gearbox and the motor, plus badly degraded coupling blocks. No problems were found on other pumps during this preventive check, which also concurred with SAM4’s assessment. The customer noted that this accuracy in both true positives (faults) and true negatives (no faults) was the evidence they needed that SAM4 could help them move away from time-based inspections and preventive parts replacement.

[![](https://samotics.com/wp-content/uploads/2024/08/A-sudden-rise-in-energy-at-the-outgoing-axles-rotational-frequency.png)](https://samotics.com/wp-content/uploads/2024/08/A-sudden-rise-in-energy-at-the-outgoing-axles-rotational-frequency.png)

Figure 14. A sudden rise in energy at the outgoing axle’s rotational frequency (orange arrow), followed by 7 months of gradual increase. The green arrow indicates where the customer serviced the pump. The blue dots to the right of the green arrow indicate the pump’s return to normal operation.
#### Example 8: Missing bolt on pump coupling


SAM4 flagged a slow rise in energy at the pump’s rotational frequency. We notified the customer and put the pump on orange alert, for close tracking by our data science team. We updated the customer weekly as the energy gradually continued to rise. Three weeks after our first alert, the energy began to spike rapidly, and we moved the pump to red alert. The customer inspected the running pump three days later and reported that manual vibration measurements indicated mild misalignment and unbalance. Stroboscope inspection revealed that the coupling was missing one of its bolts. The customer scheduled the pump for repairs at its next planned stop.

[![](https://samotics.com/wp-content/uploads/2024/08/The-rise-in-energy-at-the-circled-points-corresponds-to-the-pumps-rotational-frequency.png)](https://samotics.com/wp-content/uploads/2024/08/The-rise-in-energy-at-the-circled-points-corresponds-to-the-pumps-rotational-frequency.png)

Figure 15. The rise in energy at the circled points corresponds to the pump’s rotational frequency.

[![](https://samotics.com/wp-content/uploads/2024/08/The-evolution-of-the-rise-in-energy-at-the-pumps-rotational-frequency-over-time.png)](https://samotics.com/wp-content/uploads/2024/08/The-evolution-of-the-rise-in-energy-at-the-pumps-rotational-frequency-over-time.png)

Figure 16. The evolution of the rise in energy at the pump’s rotational frequency over time. We alerted the customer at the orange and red lines; they performed maintenance at the green line.
### Electrical indicators


Developing electrical issues instantly affect the motor’s magnetic field and leave distinct signatures in the current and voltage signals. For example, a broken rotor bar creates an electrical asymmetry in the rotor which produces a counter-rotating magnetic field, inducing stator currents at multiples of twice the slip frequency around the supply frequency.

[![](https://samotics.com/wp-content/uploads/2024/08/Another-broken-rotor-bar-indicator.png)](https://samotics.com/wp-content/uploads/2024/08/Another-broken-rotor-bar-indicator.png)

Figure 17. Another broken rotor bar indicator: the resulting thermal rotor deformations induce spikes at the motor’s rotational frequency (arrows) modulated around harmonics of the supply frequency (vertical lines).

[![](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-analyses-for-two-different-electrical-faults.png)](https://samotics.com/wp-content/uploads/2024/08/SAM4-dashboard-analyses-for-two-different-electrical-faults.png)

Figure 18. Sample SAM4 dashboard analyses for two different electrical faults.
#### Example 9: Broken rotor bar(s)


SAM4 detected an increase in energy at the pump motor’s rotational frequency. There was no increase in the noise floor around the supply frequency, nor any decrease in load, ruling out cavitation. Further analysis indicated likely broken rotor bars inside the motor, creating thermal deformation of the rotor. The customer has allowed the motor to continue operation without servicing for four months since our first alert (orange dot in figure 10), during which time the degrading pattern has intensified.

[![](https://samotics.com/wp-content/uploads/2024/08/The-spectral-energy-at-the-motors-rotational-frequency.png)](https://samotics.com/wp-content/uploads/2024/08/The-spectral-energy-at-the-motors-rotational-frequency.png)

Figure 19. The spectral energy at the motor’s rotational frequency, showing a clear and intensifying rise. The elapsed time from SAM4’s first customer alert (orange dot) to the righthand side of the graph is approximately four months.

[![](https://samotics.com/wp-content/uploads/2024/08/Further-analysis-revealed-spikes-in-energy.png)](https://samotics.com/wp-content/uploads/2024/08/Further-analysis-revealed-spikes-in-energy.png)

Figure 20. Further analysis revealed spikes in energy at frequencies consistent with the presence of broken rotor bars. (Healthy motor in blue, degrading motor in black.)
#### Example 10: Current unbalance


SAM4 detected an ongoing unbalance in the current phases for this pump’s motor. Further investigation revealed that the absolute difference remained essentially constant across different loads, and that three other motors in the same electrical group were exhibiting similar trends. This suggested that a single-phase load elsewhere in the system might be the reason for the unbalance. We informed the customer of this and other possible causes (voltage unbalance in the power grid, motor coil unbalance, a leakage path to ground). The customer meggered the motor and confirmed the unbalance, but no damage. We recommended the customer investigate possible causes to avoid future damage from long-term unbalance.

[![](https://samotics.com/wp-content/uploads/2024/08/Current-difference-in-pump-motor-phases.png)](https://samotics.com/wp-content/uploads/2024/08/Current-difference-in-pump-motor-phases.png)

Figure 21. The pump motor’s second phase (black) drew noticeably more current than the other two phases.

[![](https://samotics.com/wp-content/uploads/2024/08/The-current-unbalance-rose-as-the-motors-load-dropped.png)](https://samotics.com/wp-content/uploads/2024/08/The-current-unbalance-rose-as-the-motors-load-dropped.png)

Figure 22. The current unbalance rose as the motor’s load dropped. (The unbalance is the relative difference in current drawn between the phases. The absolute difference, plotted on the vertical axis, is basically constant, but as the load drops and the motor draws less current, it represents a greater percentage of the current drawn.)
## Conclusion


We hope these examples of actual SAM4 fault detections help you assess whether SAM4 can be a useful addition to your condition monitoring toolkit. If you would like to see SAM4 in action, please contact
us for a no-obligation demo at your convenience. We’re also happy to answer any questions you may have about SAM4’s value for your specific situation.
