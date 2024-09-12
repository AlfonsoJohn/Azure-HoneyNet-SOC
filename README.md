# SOC + Honeynet in Azure (Live Traffic)
![Cloud Honeynet / SOC](https://imgur.com/l6sf2uN.jpg)


## Introduction
Introducing a comprehensive approach to building a HoneyNet via Microsoft Azure. This project aims to create a visual representation of real-world cyber attacks from around the globe by gathering data from various IP addresses. By collecting log sources from diverse resources and ingesting them into a Log Analytics workspace, we can leverage Microsoft Sentinel to construct attack maps, trigger alerts, and generate incidents.

In this project, I have established a mini HoneyNet in Azure and integrated log sources from multiple resources into a Log Analytics workspace. This setup allows us to measure security metrics in an insecure environment for 24 hours, apply security controls to harden the environment, and then measure metrics for another 24 hours. The results will be presented below.

## Azure Resources Deployed, Technologies, and Regulations used:
- [Azure Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) (VNet)
- [Azure Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) (NSG)
- [Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/overview) (2x Windows 10 Pro, 1x Linux Server)
- [Log Analytics Workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview) with Kusto Query Language (KQL) Queries
- [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts) for Secure Secrets Management
- [Azure Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) for Data Storage
- [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview) for Security Information and Event Management (SIEM)
- [Microsoft Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) for Cloud to Protect Cloud Resources
- [Windows Remote Desktop](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c) for Remote Access
- [Command Line Interface](https://www.w3schools.com/whatis/whatis_cli.asp) (CLI) for System Management
- [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.3) for Automation and Configuration Management
- [NIST SP 800-53 Revision 4](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) for Security Controls
- [NIST SP 800-61 Revision 2](https://www.nist.gov/privacy-framework/nist-sp-800-61) for Incident Handling Guidance

## Course of Action
- ***Establishing the honeynet:*** To start, I created the vulnerable environment with the Virtual Machines. This was done by disabling the firewall inside of the VM as well as allowing all ports and traffic to be received by the Network Security Group (NSG).

- ***Tracking and examination:*** The Azure infrastructure was meticulously configured to seamlessly ingest log sources from a multitude of resources into a dedicated log analytics workspace. Leveraging the advanced capabilities of Microsoft Sentinel, sophisticated attack maps were meticulously constructed, meticulously triggering highly precise alerts and meticulously generating comprehensive incidents, all meticulously derived from the meticulously collected and meticulously analyzed data.

- ***Tracking and evaluating security metrics:*** I monitored the unsecured environment for a full day, noting important security measurements during that time. This served as a starting point for comparison once I applied security improvements.

- ***Addressing and resolving security incidents:*** Following the resolution of incidents and identification of vulnerabilities, I proceeded to fortify the environment by implementing security best practices and incorporating Azure-specific recommendations.

- ***Analysis after implementing remediation measures:*** An additional 24-hour period was dedicated to the meticulous re-observation of the environment, facilitating a comprehensive evaluation of the security metrics. The resulting data was then meticulously juxtaposed with the initial baseline, enabling a rigorous comparative analysis.

The metrics we will show are:
- SecurityEvent (Windows Event Logs)
- Syslog (Linux Event Logs)
- SecurityAlert (Log Analytics Alerts Triggered)
- SecurityIncident (Incidents created by Sentinel)
- AzureNetworkAnalytics_CL (Malicious Flows allowed into our honeynet)


## Architecture Before Hardening / Security Controls

![Architecture Diagram](https://i.imgur.com/pllH1Aq.jpg)

In the "BEFORE" measurement phase, it was observed that all resources were initially provisioned with direct internet exposure. The Virtual Machines were configured with open Network Security Groups and permissive built-in firewalls, while other resources were deployed with publicly accessible endpoints, thereby rendering the usage of Private Endpoints unnecessary.

## Architecture After Hardening / Security Controls

![Architecture Diagram](https://i.imgur.com/0Pbsm6T.jpg)

In the "AFTER" evaluation stage, the Network Security Groups underwent fortification measures whereby all traffic, with the exception of my administrative workstation, was comprehensively blocked. Additionally, other resources were fortified by leveraging their built-in firewalls alongside the implementation of Private Endpoint functionality.

The architecture of the mini honeynet in Azure consists of the following components:

- Virtual Network (VNet)
- Network Security Group (NSG)
- Virtual Machines (2 windows, 1 linux)
- Log Analytics Workspace
- Azure Key Vault
- Azure Storage Account
- Microsoft Sentinel

For the "BEFORE" metrics, all resources were originally deployed, exposed to the internet. The Virtual Machines had both their Network Security Groups and built-in firewalls wide open, and all other resources are deployed with public endpoints visible to the Internet; aka, no use for Private Endpoints.

For the "AFTER" metrics, Network Security Groups were hardened by blocking ALL traffic with the exception of my admin workstation, and all other resources were protected by their built-in firewalls as well as Private Endpoint

## Attack Maps Before Hardening / Security Controls

### MS SQL Server Authentication Failures
The visual representation presented below provides an overview of the assault endeavors targeted at a publicly accessible Microsoft SQL server throughout a span of 24 hours. The plotted data points on the map delineate the precise origins of these attacks or attempted logins. 

![MSSQL Allowed Access](https://imgur.com/DlLCSQM.png) <br />

### Linux SSH Authentication Failures
The depicted attack map elucidates the multitude of syslog authentication failures encountered by the Linux server I provisioned, elucidating the presence of unsanctioned endeavors to gain entry from external sources beyond the confines of the local network. This serves as an emphatic reminder underscoring the indispensability of fortifying Linux servers with robust authentication protocols and diligently scrutinizing system logs to detect and thwart potential intrusions.

![Linux Syslog Auth Fail](https://imgur.com/bDQGz0U.png) <br />

### Windows RDP/SMB Authentication Failures
The exhibited attack map encapsulates a multitude of RDP (Remote Desktop Protocol) and SMB (Server Message Block) failures, vividly exemplifying the unrelenting endeavors of potential assailants to exploit these specific protocols. The visual depiction accentuates the imperative nature of fortifying remote access and file-sharing services as a means to safeguard against illicit entry and mitigate the looming cyber threats that may ensue.

![Windows RDP/SMB Auth Fail](https://imgur.com/sHqFcdA.png) <br />

### NSG Allowed Malicious Inbound Flows
The illustrated attack map serves as a compelling showcase of the ramifications stemming from the act of leaving the Network Security Group (NSG) unrestricted, thereby facilitating the unhindered ingress of malicious network traffic. This visualization effectively emphasizes the criticality of deploying robust security protocols, including the imposition of stringent NSG rules, as a means to thwart unauthorized entry and mitigate the inherent risks posed by potential threats.

![NSG Allowed Inbound Malicious Flows](https://imgur.com/YdgSfyS.png)<br>

## Metrics Before Hardening / Security Controls

The following table shows the metrics we measured in our insecure environment for 24 hours:
Start Time 2024-03-15 17:04:29
Stop Time 2024-03-16 17:04:29

| Metric                   | Count
| ------------------------ | -----
| SecurityEvent            | 19470
| Syslog                   | 3028
| SecurityAlert            | 10
| SecurityIncident         | 348
| AzureNetworkAnalytics_CL | 843

## Attack Maps After Hardening / Security Controls

```All map queries actually returned no results due to no instances of malicious activity for the 24 hour period after hardening.```

## Metrics After Hardening / Security Controls

The following table shows the metrics we measured in our environment for another 24 hours, but after we have applied security controls:
Start Time 2024-03-18 15:37
Stop Time	2024-03-19 15:37

| Metric                               | Count
| ------------------------------------ | -----
| SecurityEvent                        | 8778
| Syslog                               | 25
| SecurityAlert                        | 0
| SecurityIncident                     | 0
| AzureNetworkAnalytics_CL             | 0
| NSG Inbound Malicious Flows Allowed  | 0

## Reflection
The process of setting up and analyzing a honeynet within the Microsoft Azure platform has provided valuable insights into the potential vulnerabilities of a network and the effectiveness of security controls in mitigating these risks. By integrating various log sources into a dedicated Log Analytics workspace, we were able to generate comprehensive metrics on the security posture of the environment before and after the implementation of security measures.One of the most notable outcomes of this project was the significant reduction in security events and incidents observed after the enforcement of security controls. This was particularly evident in the absence of any allowed traffic from malicious actors on the public internet, highlighting the efficacy of the implemented measures.

It is also important to consider that the results may have been influenced by the specific usage patterns of the network during the 24-hour assessment period. Further investigation into the behavior of regular users and potential impact on security event generation would be valuable for refining our understanding of the network's security posture.

## Conclusion
This project demonstrates the potential of a mini honeynet within the Microsoft Azure platform, along with the integration of Microsoft Sentinel, to provide proactive alerting and incident management based on ingested log data. The establishment of a baseline for security metrics before and after the implementation of security controls has provided valuable insights into the effectiveness of these measures in mitigating potential risks.

By further exploring the nuances of network usage patterns and security event generation, we can refine our understanding of the network's security posture and optimize the implementation of security controls to maximize their efficacy.
