# 0x19. Postmortem

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.


## Resources

* [Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)
* [The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem#the-benefits-of-an-incident-postmortem)
* [What is an Incident Postmortem?](https://www.pagerduty.com/resources/learn/incident-postmortem/)


## Postmortem Format


* Issue Summary (that is often what executives will read) must contain:
   * duration of the outage with start and end times (including timezone)
   * what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
   * what was the root cause

*Timeline (format bullet point, format: ``time`` - ``keep it short, 1 or 2 sentences``) must contain:

   * when was the issue detected
   * how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
   * actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
   * misleading investigation/debugging paths that were taken
   * which team/individuals was the incident escalated to
   * how the incident was resolved

* Root cause and resolution must contain:
   * explain in detail what was causing the issue
   * explain in detail how the issue was fixed

* Corrective and preventative measures must contain:
   * what are the things that can be improved/fixed (broadly speaking)
   * a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
* Be brief and straight to the point, between 400 to 600 words

## Example

###                                                 Incident Report (Postmortem) on Bet Placing Issues

Customers were unable to place bets as a result of third-party package subscriptions expired, which lasted for up to an hour (i.e 07:30 am to 08:30 am Sunday 14, may 2023) after it was reported by a customer. As a result multiple client complaints were received, some users were very upset and frustrated but was promptly fixed.

The issue was assigned to christian, immediately the first complaint was received at about 07:45 am. Apparently the root cause was identified to be as a result of a third-party package subscriptions expired and  easily fixed by renewing our subscription for the package.

The root cause of the issue and how it affected the system is that before a bet is placed the system has to confirm if the user is able to place the bet, but the process that does the check and returns either true or false relies on BKownings package which checks if the client is owing. But was unable to get a response because our subscription to BKownings expired and BKownings was throwing this error “Operation Denied”. To fix, all we did was renew our subscription and all was fine again. Customers are now able to place bets.

Lastly, as a preventive measure, we have automated the subscription renewal process to avoid future occurrences.
