2.1 Concept of Cloud Storage
Cloud storage buckets are logical containers used for storing and managing objects in cloud environments. Google Cloud describes buckets as the primary resource used to organize and manage objects in cloud storage systems. Amazon S3 similarly relies on buckets as the fundamental storage unit for managing data assets. (About Cloud Storage buckets | Google Cloud Documentation 2026)
Modern organizations increasingly store critical business workloads in cloud buckets because of scalability, cost efficiency, and availability benefits. However, these same advantages create attractive targets for attackers when security controls are improperly implemented. (2024 State of Multicloud Security Report)

2.2 Cloud Security Theory
Cloud security operates under the Shared Responsibility Model, where cloud service providers secure infrastructure while customers remain responsible for configuring access controls, storage permissions, encryption settings, and monitoring solutions. AWS emphasizes that customers retain responsibility for securing data stored within their cloud environments. (Amazon S3 Security Features – Amazon Web Services)
This model explains why cloud storage breaches frequently result from human error and misconfiguration rather than provider failures. (Cloud Misconfiguration: The #1 Cause of Data Breaches 2025)

2.3 Cloud Security Threats (2024-2026)
Recent cloud security literature consistently identifies several major threats:
1.	Misconfiguration
The Cloud Security Alliance Top Threats to Cloud Computing 2024 report ranked misconfiguration and inadequate change control among the most significant cloud security concerns. (Cloud Security Alliance Releases Top Threats to Cloud, CSA 2026)
2.	Identity and Access management (IAM) weaknesses
Weak IAM configurations remain a leading cause of unauthorized access incidents. Excessive privileges and poor identity governance increase attack surfaces across cloud environments. (Cloud Security Alliance Releases Top Threats to Cloud, CSA 2026)
3.	Insecure APIs
Cloud management interfaces and APIs can expose sensitive information if improperly secured. (2024 Orca Security report)
4.	Data Exposure
The 2024 State of Cloud Security Report identified publicly exposed data assets and sensitive data exposure among key organizational risks. (2024 Orca Security Report)

2.4 Review of Contemporary Research
Tenable Cloud Risk Report (2024)
Tenable’s analysis of millions of cloud resources revealed persistent risks associated with publicly exposed assets, excessive privileges, and cloud storage exposure. The report introduced the concept of the “toxic cloud trilogy,” describing cloud workloads that are publicly exposed, critically vulnerable, and highly privileged. (Report Tenable Cloud Risk Report 2024 – event.foundryco.com)
Cloud Security Alliance (2024)
CSA reported that misconfiguration, IAM weaknesses, accidental cloud data disclosure, and limited cloud visibility remain dominant cloud security concerns. (Cloud Security Alliance Releases Top Threats to Cloud)
Orca Security State of Cloud Security Report (2024)
Orca Security highlighted exposed sensitive data, public writing permissions, weak authentication controls, and unused privileged accounts as recurring vulnerabilities within cloud infrastructures. (2024 State of Cloud Security Report)
IBM Cost of a Data Breach Report (2024)
IBM reported that the average cost of a data breach reached a record USD $4.88 million globally in 2024. Breaches involving multiple cloud environments were among the most expensive and required the longest remediation time. [Surging data breach disruption drives costs to record highs – IBM]
