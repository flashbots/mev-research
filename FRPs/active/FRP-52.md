---
id: 52
title: "Trusted SILOs: Side-channel Isolated Logic Oases"
team: Andrea Waite & ml_sudo
created: 2025-07-09
status: active
---

## Background and Problem Statement

### Context
Adversarial glitching and side-channel data mining of secure data is a growing problem for business and identity, with market needs across all industries. This proposal is a potential solution for a persistent class of vulnerabilities that abuse on-chip power distribution networks. 

### The Problem
Power distribution on secure chips is a vector for increasingly sophisticated attacks that seek to monitor or affect the internal state of processes that are intended to be secret. Current mitigation techniques exist to address these attacks, especially at the logic level, and there are research groups actively working to secure power distribution networks, but such techniques are poorly publicized and require analog IC design skills to implement. 

### Hypothesis
We propose a review and systematization of existing techniques and design of new circuits and layouts to contain sensitive sections of a chip in power enclaves, or oases. Each oasis will have isolated power and ground networks connected to an active power regulator and glitch detector circuit, which protects the inhabiting systems of the oasis from power glitches and prevents fluctuations in their power consumption from leaking secret information out. Such protection can be made self-sufficient and localized for modular, scalable implementation in larger systems. We hypothesize that the proposed “SILO” architecture and toolkit can greatly attenuate the effectiveness of many invasive and most non-invasive attacks while offering drop-in compatibility with existing logic-level techniques like masking.

## Plan and Deliverables

* Perform literature review and collect data on published techniques to defend the power distribution network against data extraction and glitch injection.
* Quantify the SNR improvement of promising published techniques, and the effect of such improvement to modern data extraction and glitch injection attack resistance. 
* Systematize the existing defenses into a tradeoff table, and calculate the effect of process changes on size and power.
* Determine favorable directions to test in prototypes for a next step and write a report organizing all information systematically.

## Background

Trusted Execution Environments (TEEs) are fundamental components for modern secure computing, enabling sensitive code and data to execute with integrity and confidentiality, even when hosted on untrusted infrastructure such as cloud data centers. Realization of "trustless computing" is critical for secure management of highly sensitive data in multi-tenant environments.

However, as TEE adoption and the potential value they protect increases, attack vectors now focus on the physical realm, fundamentally altering the threat model and increasingly requiring the use of integrated-circuit design techniques previously confined to military and national security applications.

This proposal introduces the **SILO** *(Side-channel Isolated Logic Oasis)* hardware architecture toolkit as a way to harden TEEs and other secure ASICs against internal and external physical attacks involving power and ground networks to yield side-channel-isolated self-sufficient compute zones, or oases, hardened against as many semi- and non-invasive attack methodologies as possible. We plan to compare published and novel methods, and calculate efficacy and cost in area and power of such techniques, as groundwork for test chip fabrication and evaluation.

### The Threat: Physical Attacks and Multi-Tenant Risks

While today's TEEs effectively stop software attacks (like malware or hypervisor exploits), they remain vulnerable to sophisticated physical adversaries. In untrusted multi-tenant settings, these threats become even more complex:

* **Side-Channel Attacks (SCA):** These non-invasive methods exploit subtle physical emanations to steal secrets. Attackers attempt to gain information by statistically correlating monitored variations in:

    * **Execution timing.** The lowest-hanging fruit, one that infamously allowed remote timing attacks. Although current best practice attempts to eliminate timing variation, clock throttling and resource contention can convert nominally constant-time actions into timing effects, most notably Hertzbleed \[WAN22\]

    * **Power consumption.** Techniques like DPA (differential power analysis), which have become very sophisticated when combined with machine learning. \[TIM19\]
  
    * **Electromagnetic radiation and impedance.**  Electromagnetic analysis (EMA) allows observation of more localized logic activity over time, often from a significant distance. \[WAN20\] It can bypass many chip- and system-level protections. \[DAS20\]
  
    * **Cross-domain leakage.** A malicious user can modulate their activity to affect neighbors, as well as create structures like ring oscillators that are sensitive to the activity of their neighbors. In FPGAs this does not require local access. \[ZHA17\]


* **Fault Injection Attacks (FIA):** These techniques intentionally cause errors at controlled points in secure processes, often targeting cipher operations to weaken encryption or extract information:

    * **Voltage glitching** involves brief, controlled voltage changes outside the nominal voltage or timing limits \[KAZ20\].
    * **Optical glitching** or Laser Fault Injection (LFI) uses precisely aimed laser pulses to inject charge into very specific locations on an IC, or to heat specific devices in ways that affect timing \[AMI21\]
    * **EM glitching** is an emerging attack vector that uses capacitive or inductive coupling from microprobes to inject faults, often with the same apparatus used for EMA.

* **Denial-of-Service (DoS) Attacks:** Beyond stealing data, adversaries might aim to make a secure device unusable. In multi-tenant setups, a poorly designed TEE can be vulnerable to a malicious tenant causing degradation or complete denial of service to co-tenants. For critical services on shared hardware, resilience to DoS may be as vital as secrecy, as even a brief downtime can lead to significant financial and reputational damage to victim co-tenants and trusted compute provider. This possibility underscores the need to harden secure systems on a hardware level, rather than merely detecting faults and raising an alarm.

### Economics and Hardware Security  
Physical attack tools like DPA hardware and optical glitching apparatus are more affordable than ever, and attacks come from well-funded organizations. Nation-states typically breach secure ICs for political, espionage, or law-enforcement reasons, rather than financial. TEEs in the cryptocurrency industry will cause the most common adversary to be aiming for financial gain (individuals, organized crime, possibly competing firms). 

When money is the object, secrets protected by secure hardware become fungible. From a strategic view, security can then be modeled as an exercise in economic deterrence where defenses succeed when their presence makes the expected value of an attack negative to potential adversaries. An economic defense seeks to both reduce an attacker’s probability of success (walls) and to increase their cost of failure (traps). A good system will present multiple of both types of obstacles for minimum added cost to the defender. When considering the life-cycle of a secure IC like a TEE, this translates to design principles that emphasize modularity, composability, broad applicability, and efficiency.

SILO contributes to the security onion by offering a modular set of functional blocks designed to frustrate all the previously-mentioned physical attack vectors with both “walls” and “traps”. One can reduce the amount of chip area and power spent on SILO blocks to attain “good enough” levels of defense against less relevant threat vectors, or increase it to allow use of smaller or cheaper logic techniques that would not be safe to use alone.

## The Weak Point: On-Chip Power Delivery Networks (PDNs)

Modern System-on-Chips (SoCs) and CPUs, including TEEs, utilize intricate PDNs to distribute power across billions of transistors. Typically chip-spanning trees or meshes, these PDNs would ideally maintain perfectly stable voltage at all points, regardless of size and location of demand. Unfortunately real metals have resistance and even very small chip-scale packages have parasitic inductance. This means that changes in current flow cause varying amounts of voltage drop and ground bounce, manifesting as switching noise (SSN).

This switching noise can erode noise margin enough to cause logic faults, a common issue that worsens as clock speeds increase. An effective mitigation for this effect is to connect different blocks to separate power supply pins – for example, dividing IO drivers from the logic core. Unfortunately, while this improves the reliability situation, it also greatly improves the signal available for power side-channel attacks by providing more direct access to specific target subsystems.
In multi-tenant or multi-core architectures, this approach creates a cruel tradeoff: Even when processing units or secure zones are isolated by memory protection, if their power is supplied through common power planes or shared bond wires the shared medium makes them vulnerable to internal side-channel information leakage between ostensibly isolated systems. If one isolates processing units or secure zones from each other by supplying power independently to each from the outside, they can be targeted much more precisely with external power monitoring and glitching attacks.

## Our Solution: Side-channel Isolated Logic Oases (SILOs)

To break this cruel dilemma forced by purely passive power distribution, we propose the use of small distributed on-chip power regulator circuits to create power oases for select mission-critical hardware blocks. Such circuits can provide several desirable features that passive power distribution cannot:

* **Reliability.** Distributed regulation protects critical sections from power supply noise and voltage drop arising both externally and internally, limiting opportunities for poor design and hostile tenants to cause catastrophic security faults or denial of service.
* **Performance Monitoring.** Each active regulator gives the opportunity to monitor voltage, current, and temperature. This can be performed coarsely enough to render it useless as a side-channel while providing useful performance monitoring, especially during development testing.
* **Spatial Decoupling.** Power flows in one direction, thus each oasis is unaffected by the activity of others. This both blocks leakage to any malicious internal processes, and greatly reduces the effectiveness of external monitoring by pooling individual power fluctuations onto a single internal power network.
* **Temporal Decoupling.** Passive filtering or active “power airlocking” implemented with charge pumps, as discussed in \[GOR15\] & \[VOS19\] aggregate time-dependent changes in power consumption into regular pulses with no time information. This can be considered a form of masking and makes digital random masking techniques much more effective.
* **Power Glitch Detection & Defense.** A good regulator is designed to present a high input impedance, preventing glitch pulses from affecting the secure oasis.\[DAS17\]\[DAS20\] If either overvoltage or undervoltage occur outside defined limits of voltage and time, an alarm flag is raised. This part of the circuit can also be made to detect temperature changes. 
Failsafe Power. Part of the power glitch defense circuit is a capacitive reservoir that allows failsafe action to be taken in event of glitch attack or power loss. This can include secure randomized overwrites of any critical data-at-rest like keys, and setting of nonvolatile “compromised” flags to frustrate attempts to extract keys by freezing or to develop glitch attacks.
* **Optical Glitch Detection & Defense.** Detecting optical glitch injections is quite difficult. Circuits have been proposed like in \[MUT22\] but the overhead of separate sensors and the increasing precision of attacks makes reliable protection at the IC level difficult. While seemingly not directly involving power distribution, isolating power oases with regulator circuits makes detecting and reacting to optical glitching attacks much easier. Optical glitching creates voltages at chosen circuit points by inducing a photocurrent in diode junctions, generally those formed by transistor source/drain terminals and their bulk terminal. Under normal conditions there is no current through the bulk and it is connected to power or ground as an afterthought. If each oasis has its bulk terminals supplied by its regulator through special sense lines, photocurrent from optical glitch injection can be detected and an alarm raised.

Security-enhanced architectures inherently require engineering tradeoffs against cost and performance. While we expect the benefits in terms of enhanced security and robustness from the SILO architecture are substantial, achieving them with minimum added expense requires consideration of certain factors.

## Design Tradeoffs
The distributed nature of SILO's defenses means an increased silicon footprint and power consumption. 
* Each secure logic oasis requires a dedicated power regulator circuit sized by the load’s power demand. The difference between supply and demand voltage determines power wasted in linear regulation.
* If a switched-capacitor “power airlock” or local energy reservoir to increase temporal masking or increase the failsafe operation time is desired, area increases. 
* If the power consumption of logic in the protected oasis is greater, more area will be required to filter or power it for the same amount of time. 
* We expect the size of energy storage capacitors to be the dominant factor in added area, so carefully specifying the masking required and worst-case load power consumption will ensure best results.
* Optical glitch photocurrent detection circuitry and the routing of its bulk-contact lines will require more area and at least some modification of standard library digital cells to access the bulk terminals separately, which could be problematic if such cells are IP cores one does not have the ability to customize.

## Advantages Over Other Methods

* Modular & Scalable. As the whole point of SILO is to isolate oases, one can scale their number and size independent of all others. This is very amenable to distribution as a drop-in standard cell library rather than a technique to be used in the design phase.
* Logic Agnostic. One can use any kind of logic inside an oasis. It treats its contents as a black box and indeed one may be able to reclaim space and power spent on SILO by dropping the use of costly techniques like differential logic, mirrored & interlaced layouts, logic scrambling, parity, and voting circuits. It also allows multiplicative effectiveness against attacks when used with other complementary techniques that reduce signal in power consumption like constant-time crypto or increase noise like randomized masking.
* No Performance Impact. Unlike techniques that aim to validate data or eliminate variance in time and power consumption, SILO assumes such techniques will always be imperfect. Instead we attempt to utilize the omnipresent on-chip power distribution networks to shield oases in similar ways to military Secure Compartmented Information Facility (SCIF) rooms, yielding “SCIFs on a chip”.
* Configurable Response: A consequence of SILO’s modularity is the versatile response one can have to possible threats. While beyond the scope of this proposal, we imagine an architecture incorporating SILO modules will connect the provided alarm flag lines along with other inputs to a “meta-TEE” secure processor that allows programmable tradeoff of security against functionality for each tenant. It will handle functions like setting anomaly detection thresholds, whether “fail safe” means “self destruct” or “stay up”, verifying hardware trustedness, and communicating logs and crypto canary heartbeat messages.
  
## Design and Validation
While the effectiveness of SILO against diverse side-channel and fault injection attacks can be felt out qualitatively through simulation, as these attacks exploit imperfections in the physical properties of as-fabricated chips, accurately quantifying the true degree of threat attenuation will likely require construction of some custom test rigs in coordination with an expert hardware hacker, and subjecting a large enough number of test chips to that expert’s attacks for statistical analysis and correlation with process variation numbers. Such work can be performed as part of a longer-term study if preliminary results are promising.

## References

\[DAS17\] "High efficiency power side-channel attack immunity using noise injection in attenuated signature domain" (HOST 2017) - D. Das, S. Maity, S. Nasir et al

\[DAS20\] "Electromagnetic and Power Side-Channel Analysis: Advanced Attacks and Low-Overhead Generic Countermeasures through White-Box Approach" (Cryptography 2020) - D. Das, S. Sen 


\[SEC22\] "Exploiting On-Chip Voltage Regulators for Leakage Reduction in Hardware Masking" (Sensors 2022) - Seçkiner, S.; Köse, S.

\[WAN22\] "Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86" (USENIX Security 2022) - Y. Wang, R. Paccagnella, et al

\[ZHA17\] "FPGA-Based Remote Power Side-Channel Attacks" (SP 2018) -  M. Zhao, G. E. Suh

\[TIM19\] "Non-Profiled Deep Learning-based Side-Channel attacks with Sensitivity Analysis" (CHES 2019) - Timon, B.

\[WAN20\] "Far Field EM Side-Channel Attack on AES Using Deep Learning" (ASHES 2020) - R. Wang, H. Wang, E. Dubrava

\[GOR15\] "A Hardware-Based Countermeasure to Reduce Side-Channel Leakage: Design, Implementation, and Evaluation" (TCAD 34) - A. Gornik, J. Moradi et al

\[VOS19\] "Leveraging On-Chip Voltage Regulators Against Fault Injection Attacks" (GLSVLSI 19) - A. Vosoughi, S. Köse

\[KAZ20\] "A Review on Evaluation and Configuration of Fault Injection Attack Instruments to Design Attack Resistant MCU-Based IoT Applications" (Electronics 2020) - Z. Kazemi, D. Hely, M. Fazeli, V. Beroulle

\[AMI21\] "Special Session: Physical Attacks through the Chip Backside: Threats, Challenges, and Opportunities" (IEEE VTS 39) - E. Amini, K. Bartels, et al. 

\[MUT22\] "FTC: A Universal Sensor for Fault Injection Attack Detection" (HOST 22) - M. R. Muttaki, T. Zhang, M. Tehranipoor, F. Farahmandi
