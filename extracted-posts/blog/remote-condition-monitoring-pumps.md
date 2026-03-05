---
title: "Remote condition monitoring for submersible pumps"
slug: "remote-condition-monitoring-pumps"
date: "Wed, 02 Jun 2021 14:33:50 +0000"
category: "Blog"
category_slug: "blog"
tags: ["Wastewater"]
original_url: "https://samotics.com/blog/remote-condition-monitoring-pumps"
images: 2
word_count: 2555
---

Capturing monitoring data at a distance to enable predictive maintenance.






In most industries, it’s a struggle to collect reliable health data for submersible pumps. A technique called electrical signature analysis solves this problem by using sensors that install in the motor control cabinet, not on the pump itself. But how well does it perform? An in-depth look at ESA’s strengths, weaknesses and fault detection accuracy.









Submersible pumps present a unique [condition monitoring](/blog/what-is-condition-monitoring) challenge. They’re often found in hard-to-access places like the bottom of an oil wellbore or a water supply borehole. Lifting them is expensive; at a cost that runs to five and even six digits in some industries, stopping operations to pull the pump and take routine manual measurements is pretty much out of the question. In some applications (such as municipal sewage pumping stations) a company’s fleet of submerged pumps is also spread over a large geographical area, which turns travel time into a significant cost factor. Even in the relative cosiness of a single production plant, it can take hours to complete a route through every machine.

These points embody the first sense of remote: the need to avoid using valuable maintenance technician time to physically visit the pump and stop its operation in order to take readings. This need has largely been met by the rise of wireless sensing and the internet of things (IoT). Permanently installed sensors capture data while the pump continues to operate normally, then transmit it to a central location where your staff can use it to efficiently monitor all your pumps’ health from a distance and enable the switch from time-based maintenance to [predictive maintenance](/blog/predictive-maintenance-quick-start-guide).

But there’s also a second sense of remote. Wireless vibration sensors eliminate the need for recurring access, but they still have to be installed on the pump. When the pump goes back down into the wastewater or oil or sulfuric acid, so do the sensors. Sensors durable enough to withstand those conditions over the long term are either hugely expensive or nonexistent. The need embodied in this sense of remote applies to the sensors themselves: a way to capture accurate, usable asset health data at a distance, without touching or even seeing the pump itself.





## Sensors for remote condition monitoring


Capturing useable condition monitoring data without being anywhere near the pump may sound like wishful thinking, but there’s actually a robust fault detection technology that does exactly that. It’s called electrical signature analysis (ESA), and it was first developed by Oak Ridge National Laboratories in the 1980s to safely monitor motor-operated valves in a nuclear power plant. ESA measures the voltage and current being supplied to the motor driving the valve, pump or other equipment to accurately track the whole machine’s health. Because ESA captures electrical signals, its sensors are non-invasive current and voltage probes that install around the phase wires in the smooth, dry, pH-neutral safety of the motor control cabinet, not on the machine itself. That means ESA sensors will never be exposed to the corrosive, abrasive conditions a submerged pump operates in.

![](https://samotics.com/wp-content/uploads/2023/10/esa-system-installed-in-mcc-1.jpg) An ESA system installed in a motor control cabinet. The orange box is the data acquisition device, with connections to each of the three phases of current and voltage. The three units at right are the switch, the gateway, and the power supply. Source: Samotics.








## How well does ESA detect upcoming submersible pump failures?


Remote condition monitor certainly solves the “sensors are not big fans of sewage or hydrochloric acid” problem, but it’s only worthwhile if the resulting fault detection accuracy is good! Fortunately, it is. Electrical signature analysis has had nearly four decades to mature since Oak Ridge first developed it. Overall, ESA is on a par with other established condition monitoring technologies such as acoustic, thermal and [vibration analysis](/blog/should-you-use-vibration-analysis-condition-monitoring). Assuming each technology is being used in its Industry 4.0 incarnation—sampling the data source at a high frequency, day in day out, and analyzing the resulting terabytes of data using machine learning algorithms (you might also hear the term “artificial intelligence”)—then you’ll generally achieve robust fault detection accuracy, far enough in advance (think weeks to months) to schedule maintenance at a convenient time and avoid unplanned downtime altogether.

You may be wondering why we said “**overall**, ESA is on a par” with vibration analysis, etc. That’s because every condition monitoring technology has strong points and weak points. These are related to the natural characteristics of the underlying data source. (By the way, it’s a common misconception that electrical signature analysis can only see electrical faults, or can only see faults in the motor. [ESA also detects mechanical faults in the transmission and load](/blog/drive-train-insights-using-electric-motor-as-vibration-sensor). ESA does have weak points, but seeing only electrical faults isn’t one of them.)

Broadly speaking, all mature condition monitoring systems will detect a wide range of common developing faults. But If you zoom in on one specific failure mode, one system may do a fantastic job at spotting early damage while another struggles to see anything at all. (As an outsized example, acoustic emission analysis can instantly detect a developing crack in a water pipe, but no amount of lubricant analysis could ever help you there… because there isn’t any lubricant to analyze.)

That means there’s no “one technique to rule them all”; instead, think of asset health monitoring as a toolbox and the different technologies as your wrenches, hammers and screwdrivers.








> "Electrical signature analysis is the tool of choice for machinery like submersible pumps, where other remote condition monitoring techniques struggle to provide value."








## ESA’s unique strengths and weaknesses


We’ve already noted one of ESA’s major advantages over other condition monitoring technologies: the sensors don’t need to be near the pump. Here are three more.


 	- There’s no need to choose which faults to focus on (or install dozens of expensive sensors), because **every frequency of interest is contained in the electrical signals**: impeller frequencies, cavitation frequencies, gear and belt frequencies, motor fault frequencies and so on. As long as you provide the ESA system with the pump’s specifications, one sensor unit will detect fault signatures across the full spectrum.

 	- As you might expect from the name, **ESA excels at detecting electrical anomalies in both the motor and the power supply**. We’ll talk more about this below.

 	- **ESA can automatically handle varying speeds and loads**, which is critical to meaningful fault detection in systems that experience this kind of operational variance. (Read more about how this works in [our ESA explaine](/kb/the-esa-explainer)[r](https://www.samotics.com/the-esa-explainer).)



These are all significant benefits for not only submersible pumps, but industrial machinery in general. And that brings us to the first of ESA’s weaknesses: it only works on systems driven by electricity. In principle these can be AC or DC systems and (for AC) single or multiple phase, but in practice three-phase AC motors dominate the industrial landscape and that’s what most ESA systems on the market are designed for.

Second, it only works on systems *directly* driven by electricity. The longer and more complex a drive train is, the less information the electrical signal will contain about components that are far from the motor. (This loss of information to attenuation, distortion and noise as a signal travels through a non-perfect transmission medium is a physical principle affecting all condition monitoring systems—for example, it’s also why vibration sensors need to be placed close to the bearing or other component you want to monitor, and why a doctor puts the stethoscope over your chest and not your knee when he wants to listen to your heart.)








> "All the machine learning analysis in the world won’t help you if you aren’t getting quality data to start with."









That means ESA can’t monitor hydraulic submersible pumps (HSPs), for example: though the original source of power driving the hydraulic system is often electric, none of the HSP’s fault development information will make it through the intervening pump, valves and other components of the power unit. You could certainly install an ESA system on the electric motor in a hydraulic power unit, but it would only be able to tell you how the pump in the power unit is doing.

Third, even in electric submersible pumps this progressive loss of information can make it hard to isolate faults in very distant parts of the machine. Take a multistage submersible pump’s far-end bearing, for example. This is a situation where localized sensors would be a much better choice. For example, vibration sensors chosen so their frequency range includes the bearing’s natural frequencies (cage, inner race, outer race, etc.) and properly installed in a triaxial set near the bearing will always outperform an ESA system. By their nature, ESA systems can’t install localized sensors for distant parts of the drive train—current and voltage probes require access to electrical wires, which means they have to install between the power supply and the electric motor.

But the whole point is that most industries find it impossible to reliably monitor submersible pumps using vibration sensors—so electrical sensors are all we have. How much can reliable, high-quality electrical data tell us? An ESA system might not win any prizes for earliest brinelling or spalling detection, but is there any way it *can* help us keep bearings from bringing the pump to a halt? Thankfully, the answer is yes.
## Early detection of developing faults prevents collateral damage in bearings (and other components)


Bearing failure is not a standalone event, but rather the visible fallout of an indirect cause—some kind of stress in a different part of the system that’s put additional strain on the bearing and caused it to wear out faster than it should. ESA systems will catch many of these operational stresses that can lead to bearing failure down the line. For example, a motor experiencing rotor eccentricity or broken rotor bars can often continue to function “properly” for quite some time, but the uneven magnetic pull resulting from the fault creates mechanical vibrations that propagate down the drive train and put extra strain on the bearings. ESA systems excel at the early detection of rotor eccentricity and broken rotor bars. That means you’ll generally have plenty of time to plan your response; and when you decide it’s time to pull the pump to fix the motor, you can check the bearings for undue wear and replace them in the same maintenance window.
## Early detection of system stressors prevents future faults from developing


There’s just one problem in the rotor fault example above: we averted bearing-related pump failure, but we didn’t avoid having to eventually pull the pump for repairs. Months of advance notice is certainly helpful in planning the least disruptive, most efficient maintenance window, and in avoiding catastrophic, unplanned downtime. But what we’d really like our asset health monitoring system to do is help us stop damage from developing in the first place, to the extent that’s possible.

There are two ways an ESA system can help here. Both are a direct consequence of capturing electrical data, which means they are unique to ESA systems.


 	- **ESA directly measures power quality. **First, under- and overvoltages, harmonic distortion, voltage imbalance and other power quality problems are directly visible in electrical data, long before they cause overheating or vibrations. By immediately alerting you to these supply-side issues, an ESA system enables you to resolve them before they have a chance to degrade the motor’s insulation or windings. This is a major boon, [because stator winding burnout caused by these PQ issues is responsible for 80 percent of motor failures](https://franklin-electric.com.au/media/8446/06394_Franklin_AID_2x2pp_FE277.pdf). Especially in pumps controlled by a variable frequency drive (VFD), the ability to directly detect voltage distortion can dramatically improve the pump’s run life. These electrical issues are still problems that must be resolved, but at this early stage their resolution doesn’t require lifting the pump. Only if they go unnoticed until the pump’s motor begins to suffer will you have to pull the pump itself for repairs.

 	- **ESA can report on pump performance. **Second, the affinity laws enable ESA systems to transform their current and voltage measurements into accurate estimates of real-time power, head and flow. This means you can track the pump’s performance both instantaneously and over time. By comparing the pump’s actual operation to its desired operation—which occurs at or near its best efficiency point (BEP)—an ESA system can identify behavior that will lead to bearing, impeller and seal damage down the road if it becomes chronic. This real-time insight can enhance your decision-making, from immediate corrective actions (such as lowering the supply frequency to stop cavitation) to long-term process changes. All the while, this information is enabling you to keep the pump operating more healthily than it would otherwise, which means it’s preventing the opportunity for damage to accumulate.



![](https://samotics.com/wp-content/uploads/2023/10/1-SAM4-pump-dashboard-1.jpg) A pump performance dashboard in an ESA system. The pump's actual operation is plotted against its performance and power curves. Source: Samotics.







This ability to track a pump’s performance in real time also means ESA systems can identify when a pump would run more efficiently at a lower speed. In some industries, pumps are often overpowered for the average situation, because they must be bought to handle the peak situation, even if it only rarely occurs. If your pump is controlled by a VFD, this means an ESA system can give you the instantaneous data you need to dynamically match the pump’s speed to its current operating conditions. In pumps that are directly online (no VFD), this data can tell you if your process design is what keeps killing your pump—more painful to fix, but valuable to know.






To tie this back in to our far-end bearing example: because the hydraulic forces on the impeller are borne by the pump’s bearings and these forces are proportional to the square of the speed, lowering the speed lowers the strain on the bearings, again helping to prevent pump-death-by-bearing. Running at lower speeds also reduces wear in another top culprit of pump failure, the mechanical seal. As a bonus, reducing the speed also saves energy and cuts emissions—both of which are growing concerns for nearly every industry today.








> "Among fault detection technologies, ESA is unique in its ability to also provide performance and efficiency data that can be used to improve operations and reduce energy waste."








## Conclusion


We started this article by looking at a submersible pump owner’s need for a condition monitoring technology whose sensors can capture data from a distance, where they’re safe from the corrosive, abrasive conditions literally surrounding the average submerged pump. That brought us to electrical signature analysis, an established asset health monitoring technique with a 40-year history that started in nuclear power plants. From there, we determined that ESA could indeed detect developing faults with the kind of accuracy we’re used to from our best vibration, thermal, acoustic and other established systems. Like all these other systems, ESA is weak on a few failure modes, but we saw how the use of electrical data made it possible to detect something arguably even better: the initial conditions that give rise to these failures down the road. Our final verdict: ESA’s not a panacea, not a ring to rule them all, but its unique advantages make it the number-one tool to reach for in the submersible pump maintenance and reliability toolkit.
