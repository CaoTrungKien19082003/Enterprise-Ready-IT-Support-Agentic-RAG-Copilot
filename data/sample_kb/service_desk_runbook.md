---
doc_id: KB-IT-002
title: IT Service Desk Runbook
owner: IT Service Desk Lead
audience: IT Service Desk staff only
classification: Internal - IT only
version: 2.0
last_reviewed: 2026-10-08
review_cycle: every 6 months
related: KB-IT-001 (IT Support Handbook, employee guide)
---

# IT Service Desk Runbook

This runbook defines how Service Desk staff triage, troubleshoot, document and escalate IT issues. Employee-facing guidance is in the IT Support Handbook (KB-IT-001). Priority targets, team names and contact extensions below are examples and must match the organization's real SLA and escalation contacts.

## 1. Core Principles

### Rules that always apply
- Verify the user's identity before any account-affecting action (unlock, password reset, MFA reset, access change).
- Never ask a user for their password or MFA codes, and never accept them if offered.
- Never disable security agents (endpoint protection, firewall, device management) as a troubleshooting shortcut.
- Record every step in the ticket.
- Escalate early for security incidents and for issues affecting many users.

## 2. Ticket Intake and Triage

### Triage steps
1. Identify the user and a reliable contact method.
2. Capture the details: exact error or screenshot, asset tag, location (office or remote), start time, and business impact.
3. Determine scope. Check the service status dashboard and recent tickets for the same symptom. Decide whether one user or many are affected.
4. Assign a priority using the table below.
5. Categorize the ticket, then troubleshoot or route it to the right team.

### Ticket priority and response targets
| Priority | Definition | Response target | Resolution target |
|---|---|---|---|
| P1 | Company-wide outage or critical security incident | 15 minutes | 4 hours |
| P2 | Major team blocked with no workaround | 30 minutes | 8 business hours |
| P3 | Individual user blocked or degraded, with limited workaround | 4 business hours | 3 business days |
| P4 | Standard request, information request, or low-impact issue | 1 business day | 5 business days |

### Choosing between priorities
Base the priority on business impact and availability of a workaround, not on how urgently the user asks. When two priorities seem possible, choose the higher one and adjust after investigation. For any suspected security incident, notify Security immediately and let the Security lead confirm the final priority.

## 3. Identity Verification

### When verification is required
Verify identity before password resets, account unlocks, MFA changes, access changes and device lock or wipe requests.

### Accepted verification methods
Confirm at least two of the following: a callback to the phone number registered in the directory, confirmation from the user's manager recorded in the ticket, employee ID plus a detail confirmed by HR records, or a video call where the user is recognized. Do not act on a request that arrives only by email from an unverified sender, and increase the verification level when the request involves a lost MFA device or privileged access.

## 4. Account Lockout and Password Reset

### Handling a lockout or reset request
1. Confirm the user already tried self-service unlock or reset.
2. Check the lockout status and recent failed sign-ins in the directory.
3. Verify identity (see Identity Verification).
4. Unlock the account and guide the user to reset the password through the self-service portal. The password must be at least 14 characters.
5. If a temporary password is unavoidable, make it one-time with a forced change at next sign-in, and share it only through an approved secure channel, never in plain email or chat.
6. Log the verification method and actions in the ticket.

### Repeated lockouts
If the same account locks three or more times in 24 hours, look for old credentials saved on phones, mail apps or mapped drives. If failures come from unfamiliar locations or devices, treat it as a possible compromise and notify Security.

## 5. MFA Issues

### User does not receive MFA prompts
Check the phone's network connection and clock settings, confirm the authenticator app is the registered method, and ask the user to re-register through the identity portal. SMS can be used only when it is enabled as a recovery method for that account.

### Lost or replaced MFA device
Verify identity at the higher level, including manager confirmation. Remove the old registered method, issue a short-lived temporary access method, and require the user to enroll a new authenticator app or hardware key. Record all steps in the ticket.

### Unexpected MFA prompts reported by a user
Treat this as a possible password compromise. Notify Security, reset the password after identity verification, and revoke active sessions.

## 6. VPN Connectivity

### Triage for VPN problems
1. Determine whether one user or many are affected, and check the VPN gateway health on the service status dashboard.
2. Confirm the user's account is not locked and MFA works.
3. Ask the user for a screenshot of the error, the gateway selected and the type of network used.
4. Check the VPN client version and the device's compliance status, because a non-compliant device can be blocked.
5. Walk the user through the handbook steps: confirm internet, restart the client, try another gateway.

### Escalation for VPN issues
If several users or several gateways fail at the same time, escalate to the Network team as a service incident. Never ask a user to disable endpoint security or firewall settings.

## 7. Email Troubleshooting

### Step 1: determine the scope
If a user cannot send or receive email, confirm whether the issue affects one user or many users. Check network connectivity and the service status dashboard.

### Single user
Ask the user to sign out and back in, verify the mailbox quota, and test the web client. If the web client works but the desktop client does not, the problem is local to the device. Also check mail rules, forwarding and sync settings.

### Widespread incident
Do not ask each user to reinstall software or rebuild their profile. Escalate the suspected service incident to the Messaging team, link all related tickets to one incident record, and communicate status updates through the status page.

## 8. Laptop Performance

### First checks for a slow laptop
Check CPU use, memory use, free storage space, startup applications, pending operating system updates, how long since the last restart, and endpoint security scan status. A scan that is currently running can slow the device, so let it finish before judging performance.

### What not to do
Do not disable security agents as a troubleshooting shortcut.

### When to escalate
Escalate to Desktop Support when hardware diagnostics report a failure or when repeated shutdowns continue after software remediation. Confirm the user's files are backed up to company storage before any reimage or hardware swap.

## 9. Lost or Stolen Device

### Immediate actions
1. Treat the report as a security incident and notify Security straight away. Security confirms the final priority.
2. Record the asset tag, the last known location and time, the encryption status, and what data the device may hold.
3. Check the last check-in time and location in device management.
4. Lock the device remotely.
5. Revoke the user's active sessions and tokens, disable VPN access for that device, and reset the account password after verifying the user's identity.

### Wipe and replacement
Initiate a remote wipe in coordination with Security, as defined by the incident plan. Start the replacement request, and record every action with times in the ticket. Tell the user not to try recovering the device.

## 10. Phishing Reports

### Handling a reported email
Ask the user to send the message as an attachment, and tell them not to click links or open attachments. Search mail logs to find who else received it, block the sender or URL through the email security tool if authorized, and notify Security.

### User entered credentials or clicked a link
Reset the password after verifying identity, revoke active sessions, check recent sign-in activity, and notify Security immediately. Treat it as a security incident until Security says otherwise.

## 11. Escalation Matrix

| Situation | Escalate to | Contact |
|---|---|---|
| Security incident, compromised account, lost or stolen device | Security team | Hotline ext. 4999 (24/7) |
| Email or collaboration service incident | Messaging team | Incident queue |
| VPN gateway or network outage | Network team | Incident queue |
| Hardware failure or repeated shutdowns | Desktop Support | Hardware queue |
| Software not in the portal | Security review and Software Asset Management | Software request queue |
| P1 incident or multi-team outage | Incident Manager | On-call phone |

## 12. Ticket Documentation Standard

### What every ticket must contain
Summary of the problem, impact and number of users affected, troubleshooting steps taken with results, identity verification method used when relevant, next action and owner, resolution and root cause, and the user's confirmation that the issue is fixed.

### Closing tickets
Close a ticket after the user confirms the fix. If the user does not respond, send a reminder and close after 3 business days. Never close a security or P1 ticket without sign-off from the owning team.
