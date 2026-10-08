---
doc_id: KB-IT-001
title: Lotus Retail IT Support Handbook (Employee Guide)
owner: IT Service Desk
audience: All employees and contractors with a company account
classification: Internal
version: 2.0
last_reviewed: 2026-10-08
review_cycle: every 6 months
related: KB-IT-002 (IT Service Desk Runbook, IT staff only)
---

# Lotus Retail IT Support Handbook (Employee Guide)

This handbook explains how employees use company IT systems securely and how to get help when something goes wrong. It applies to every employee and contractor who has a Lotus Retail account or company device. Step-by-step procedures for IT staff are in the IT Service Desk Runbook (KB-IT-002), not here.

## 1. Getting IT Support

### How to contact the IT Service Desk
- Self-service portal (preferred, creates a tracked ticket): https://helpdesk.lotusretail.example
- Email: servicedesk@lotusretail.example
- Phone for urgent issues: ext. 4000
- Hours: Monday to Friday, 08:00 to 18:00 local time.
- Security incidents (lost device, suspected account compromise) can be reported 24/7 on the Security hotline, ext. 4999.

### What to include when you open a ticket
Include what you were trying to do, the exact error message or a screenshot, the device asset tag, whether you are in the office or working remotely, when the problem started, whether colleagues are affected, and how the problem blocks your work. A complete ticket is resolved faster.

### Never share your credentials
Never share your password, MFA codes or recovery codes with anyone, including IT Service Desk staff and your manager. IT will never ask you for them.

## 2. VPN Access

### When the VPN is required
Employees working outside the office network (at home, travelling, or on public Wi-Fi) must connect to the company VPN before accessing internal systems such as the intranet, file shares and internal applications.

### How to install and connect
Install the SecureLink VPN client from the internal Software Portal. Sign in with your company email and password, complete MFA, and select the closest corporate gateway.

### VPN will not connect: what to try first
1. Confirm your internet connection works by opening a public website.
2. Close and restart the VPN client.
3. Try a different corporate gateway.
4. Restart your laptop and make sure the VPN client is up to date.
5. If the MFA prompt never arrives, see the Multi-Factor Authentication section.

Do not disable endpoint security, antivirus or firewall settings to make the VPN work, and do not use personal VPN tools to bypass the company VPN.

### When to open a VPN ticket
If the steps above do not fix the problem, open an IT ticket with a screenshot of the error, the gateway you selected, and the type of network you were using (home Wi-Fi, mobile hotspot, hotel or public Wi-Fi).

## 3. Passwords and Account Lockout

### Password requirements
Company passwords must be at least 14 characters long. A passphrase made of several unrelated words is easier to remember and stronger than a short complex password. Do not reuse passwords from personal accounts, and change your password immediately if you suspect it has been exposed.

### How to reset a forgotten password
Use the self-service identity portal for normal password resets. You will be asked to confirm your identity with MFA.

### Account locked after failed logins
After five failed login attempts the account may be temporarily locked (typically for about 15 minutes). Wait and try again, or use the self-service portal to unlock it. If self-service recovery fails, contact the IT Service Desk. You will be asked to verify your identity before IT makes any change to your account.

### Password safety rules
Never share your password or MFA codes with support personnel or colleagues. Do not write passwords in emails, chat messages or tickets.

## 4. Multi-Factor Authentication (MFA)

### Where MFA is required
MFA is mandatory for email, VPN, cloud administration consoles and other protected company systems.

### Approved MFA methods
The approved methods are the company authenticator app and registered hardware security keys. SMS codes should only be used when SMS has been explicitly enabled as a recovery method for your account.

### Replacing or losing your phone
Register your new device before you wipe or return the old one. If you have already lost the device with your authenticator app, contact the IT Service Desk. IT will verify your identity, and in most cases will need your manager's confirmation, before issuing temporary access.

### Unexpected MFA prompts
If you receive an MFA approval request that you did not start, do not approve it. Deny it, change your password, and report it to the Security hotline (ext. 4999) because it may mean someone has your password.

## 5. Software Installation

### Where to get software
Install business software only from the company Software Portal.

### Software that is not in the portal
Requests for software that is not listed in the portal require your manager's approval and an IT security review. Open a ticket with the software name, the business reason, how many users need it, and your manager's approval.

### Administrator rights
Administrator access is not granted simply to install unapproved applications. Do not install unapproved browser extensions, file-sharing tools or remote-access tools on a company device.

## 6. Lost or Stolen Laptop or Device

### What to do immediately
Report a lost or stolen company laptop, phone or hardware key straight away to the IT Service Desk and to your manager. Outside service hours, call the Security hotline (ext. 4999). Report it even if you think it may turn up, because every hour counts.

### Information to provide
Give the device asset tag if you have it, the last known location and time, whether the device was locked or encrypted, and what company data it may have contained.

### What IT and Security will do
IT will start the device lock or wipe procedure through device management, coordinate with Security, and secure your account (for example by ending active sessions and resetting your password). You will be told when a replacement is available.

### What you should not do
Do not try to recover the device yourself or confront anyone who may have taken it. If Security asks you to file a police report, give the report number to Security.

## 7. Phishing and Suspicious Emails

### How to report a suspicious email
Do not click links, open attachments or reply. Use the Report Phishing button in your email client, or forward the message as an attachment to security@lotusretail.example, then delete it.

### If you already clicked or entered your password
Call the Security hotline (ext. 4999) immediately and change your password from a trusted device. Acting quickly limits the damage. You will not be blamed for reporting honestly and promptly.

## 8. Hardware: Requests, Replacement and Repair

### Requesting new or replacement hardware
Open a ticket through the self-service portal and include your manager's approval. Standard laptops, monitors and accessories are issued from the approved hardware catalogue.

### Faulty or slow devices
Open a ticket describing the symptoms (for example slow performance, overheating or unexpected shutdowns). Do not open the device or attempt hardware repairs yourself. Back up work files to approved company storage before handing a device to IT.

## 9. Working Remotely: Data Protection Basics

### Safe remote working
Use company-managed devices for company data. Connect to the VPN before accessing internal systems. Lock your screen whenever you step away. Do not copy company data to personal email, personal cloud storage or unapproved USB drives.

## Quick Answers

| Question | Short answer |
|---|---|
| I forgot my password. | Use the self-service identity portal. |
| My account is locked. | Wait about 15 minutes or unlock it in the portal, then contact the Service Desk if that fails. |
| VPN will not connect. | Check internet, restart the client, try another gateway, then open a ticket with a screenshot. |
| Can I disable the firewall to fix VPN? | No. Never disable endpoint security or firewall settings. |
| Which MFA methods are allowed? | The company authenticator app or a registered hardware key. SMS only if enabled for recovery. |
| I need software that is not in the portal. | Open a ticket with manager approval for an IT security review. |
| My laptop was stolen. | Report it to the Service Desk and your manager at once, or call ext. 4999 outside hours. |
| I clicked a suspicious link. | Call the Security hotline (ext. 4999) immediately. |
| Will IT ask for my password? | Never. Do not share passwords or MFA codes with anyone. |
