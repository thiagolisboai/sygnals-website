# Terms of Service — Sygnals

**Version:** 1.0
**Last updated:** July 12, 2026
**Controlling language:** For customers billed in Brazil, the Portuguese-language version of these Terms controls in the event of any conflict. For all other customers, this English version controls.


---

## Table of Contents

1. [Parties and Acceptance](#1-parties-and-acceptance)
2. [Definitions](#2-definitions)
3. [Description of the Service](#3-description-of-the-service)
4. [Eligibility, Account, and Registration](#4-eligibility-account-and-registration)
5. [B2B Nature of This Agreement](#5-b2b-nature-of-this-agreement)
6. [Acceptable Use](#6-acceptable-use)
7. [Customer Responsibility Regarding Third-Party Platforms (LinkedIn)](#7-customer-responsibility-regarding-third-party-platforms-linkedin)
8. [Third-Party Integrations](#8-third-party-integrations)
9. [Credits, Plans, and Billing](#9-credits-plans-and-billing)
10. [Cancellation and Refunds](#10-cancellation-and-refunds)
11. [Term, Suspension, and Termination](#11-term-suspension-and-termination)
12. [Intellectual Property](#12-intellectual-property)
13. [Third-Party Content and Infringement Notices](#13-third-party-content-and-infringement-notices)
14. [Confidentiality](#14-confidentiality)
15. [Data Protection](#15-data-protection)
16. [Warranties and Disclaimers](#16-warranties-and-disclaimers)
17. [Limitation of Liability](#17-limitation-of-liability)
18. [Indemnification](#18-indemnification)
19. [Service Level](#19-service-level)
20. [Changes to These Terms](#20-changes-to-these-terms)
21. [Governing Law and Jurisdiction](#21-governing-law-and-jurisdiction)
22. [General Provisions](#22-general-provisions)

---

## 1. Parties and Acceptance

These Terms of Service ("**Terms**") form an agreement between **TLA DIGITAL LTDA - ME**, registered under Brazilian company registration number (CNPJ) **54.958.502/0001-59**, with registered address at **Av. Paulista, 1106, Sala 01, Bela Vista, São Paulo/SP, CEP 01310-914** ("**Sygnals**," "**we**," "**us**") and the business entity or self-employed professional entering into this agreement to use the Service ("**Customer**," "**you**").

By creating an account, checking the acceptance box at signup, or otherwise using the Service, you confirm that you have read, understood, and agree to be bound by these Terms and by our [Privacy Policy](/legal/privacy). If you are accepting these Terms on behalf of a company, you represent that you have the authority to bind that company.

We log acceptance events (date, time, IP address, and version of these Terms accepted) for evidentiary purposes.

## 2. Definitions

- **Service**: the Sygnals platform, including the web application, public API, MCP server, and any related functionality.
- **Workspace**: a logically isolated environment within the Service, associated with a Customer, where Signals, credits, and integrations are configured.
- **Signal**: a monitoring configuration for a public LinkedIn profile, created by the Customer within the Service.
- **Engager**: an individual who has publicly interacted on LinkedIn (via a reaction, comment, profile visit, new follow, or connection request) with a profile monitored by a Signal, whose data is captured, enriched, and made available to the Customer through the Service. An Engager is not a customer of Sygnals and has no contractual relationship with us.
- **Engager Profile**: a data record about an Engager, including public LinkedIn data and attributes inferred by the Service (e.g., job title, seniority, function, location, Intent Score).
- **Credits**: the Service's unit of consumption, deducted per Engager processed, pooled at the Workspace level according to the Customer's plan.
- **Connected LinkedIn Account**: a personal or Sales Navigator LinkedIn account that the Customer authorizes the Service to access through a third-party provider (Unipile) for account-based signal collection (e.g., profile visitors, new followers).
- **Data Providers**: third-party vendors used by Sygnals to collect and enrich public or authorized LinkedIn data, including without limitation Apify and Unipile.
- **Intent Score**: a score calculated by the Service based on internal rules (engagement frequency, seniority, engagement type, and recency), intended to help the Customer prioritize outreach.

## 3. Description of the Service

Sygnals is a B2B sales-intelligence platform that monitors public LinkedIn profiles designated by the Customer, captures engagement events (reactions, comments, profile visits, new followers, connection requests), enriches this data with inferred attributes, calculates an Intent Score, and delivers the resulting Engager Profiles to the Customer via an in-app table, CSV export, Clay integration, or generic webhook.

The Service **does not send automated messages, likes, comments, or connection requests on the Customer's behalf**. Sygnals only collects, organizes, and prioritizes engagement signals that already exist publicly, or on accounts the Customer has authorized.

For publicly sourced signals, Sygnals does not use LinkedIn session cookies or browser extensions, relying instead on specialized third-party public-data providers (Apify). For account-based signals (e.g., profile visitors), the Service depends on a Connected LinkedIn Account that the Customer itself authorizes through a third-party provider (Unipile).

## 4. Eligibility, Account, and Registration

To use the Service, you must: (a) have full legal capacity to contract; (b) be entering into this agreement as a business, self-employed professional, or authorized representative of a legal entity, for professional purposes and not as a consumer; (c) provide truthful, complete, and current registration information; and (d) be responsible for keeping your access credentials confidential.

You are fully responsible for all activity under your account, including that of team members invited to your Workspace. Notify us immediately of any unauthorized use.

## 5. B2B Nature of This Agreement

These Terms govern a **business-to-business** relationship. Customer represents that it is entering into this agreement for professional, commercial, or business purposes, and not as an end consumer.

Where local consumer-protection law nonetheless grants the Customer consumer-style withdrawal rights (for example, a sole trader or micro-entrepreneur who qualifies as a consumer under applicable Brazilian law), the withdrawal terms in Clause 10.3 apply.

## 6. Acceptable Use

When using the Service, you agree **not** to:

- use the Service for unlawful, discriminatory, defamatory purposes, or in a way that infringes third-party rights;
- attempt to gain unauthorized access to other Workspaces, accounts, or other Customers' data;
- reverse-engineer, decompile, or attempt to extract the source code of the Service;
- resell, sublicense, or make the Service available to third parties without our prior written authorization;
- use Engager data obtained through the Service for purposes incompatible with legitimate B2B commercial prospecting, including without limitation: harassment, discrimination, automated decision-making with legal effects on the Engager, or any form of individualized surveillance unrelated to a good-faith commercial opportunity;
- use the Service to send unsolicited bulk communications (spam) to identified Engagers;
- deliberately overload the Service's infrastructure (e.g., excessive calls to the public API beyond stated rate limits).

Breach of this clause authorizes immediate suspension or termination of the account, without prejudice to any other available remedy.

## 7. Customer Responsibility Regarding Third-Party Platforms (LinkedIn)

**This clause is central and should be read carefully.**

7.1. Sygnals relies on public LinkedIn data and, for certain features, on a Connected LinkedIn Account authorized by the Customer through a third-party provider (Unipile). Customer acknowledges that:

(a) the use of automated data-collection tools and the connection of LinkedIn accounts to third-party services may conflict with LinkedIn's own Terms of Service, depending on how they are used;

(b) **Customer is solely responsible** for assessing whether its use of the Service — particularly the Connected LinkedIn Account feature — complies with the terms Customer itself has agreed to with LinkedIn;

(c) Sygnals is not affiliated with, sponsored by, or endorsed by LinkedIn Corporation;

(d) by connecting a LinkedIn account to the Service, Customer represents that it has legitimate authority to authorize such access, and assumes full responsibility for any restriction, suspension, or ban that LinkedIn applies to the connected account.

7.2. Sygnals does not warrant, and expressly disclaims liability for: restriction, suspension, or termination of Customer's LinkedIn accounts; unilateral changes by LinkedIn to its API, data structure, or terms of use that affect the Service's availability; or unavailability of data resulting from anti-automation measures adopted by LinkedIn.

7.3. Sygnals reserves the right to suspend, without prior notice, any specific feature if it identifies an elevated risk of third-party terms violation or legal exposure, including preventive suspension of specific Connected LinkedIn Accounts.

## 8. Third-Party Integrations

The Service allows integration with third-party platforms chosen by the Customer, including without limitation Clay (via webhook) and generic webhooks to destinations configured by the Customer. Customer is responsible for:

- keeping the credentials and destination URLs it configures valid and secure;
- ensuring that the integration destination complies with the data-protection legislation applicable to Customer;
- any processing carried out by the destination platform after Sygnals delivers the data, over which we have no control and bear no responsibility.

Sygnals does not warrant the availability, accuracy, or security of third-party platforms integrated at Customer's choice.

## 9. Credits, Plans, and Billing

9.1. **Credit model.** The Service is billed through a credit system, deducted per Engager processed, pooled at the Workspace level ("organizational credit pooling"), subject to the limits of the Customer's plan (Signals, connectable LinkedIn accounts, Workspaces).

9.2. **Plans.** Available plans, prices, credit limits, Signal limits, and Connected LinkedIn Account limits are described on Sygnals' public pricing page, which may be updated from time to time with notice under Clause 20. Plans are billed exclusively on a **recurring monthly** basis (no annual plan in this version of the Service).

9.3. **One-time credit packs.** Customer may purchase additional, non-recurring credit packs as made available on the platform.

9.4. **LinkedIn account add-on.** Additional Connected LinkedIn Accounts beyond the plan limit may be purchased as an additional recurring per-account charge, per the then-current pricing table.

9.5. **Payment processing.** Payments are processed by a third-party provider (Stripe). By providing payment information, Customer agrees to that payment provider's terms. Sygnals does not store full credit card data.

9.6. **Currency.** Prices are presented in Brazilian Reais (BRL) or US Dollars (USD) depending on the Customer's billing market, at fixed amounts (no dynamic currency conversion).

9.7. **Credit exhaustion.** Upon reaching the Workspace credit limit, or a Signal-specific cap configured by the Customer, the Service may — depending on Customer's configuration — pause new data collection or simply notify, until the billing cycle renews or an additional credit pack is purchased.

9.8. **Taxes.** Prices may not include applicable taxes, which will be added in accordance with applicable law.

## 10. Cancellation and Refunds

10.1. **Cancellation.** Customer may cancel its subscription at any time directly from the Service dashboard, effective at the end of the current billing cycle. Cancellation does not generate a pro-rata refund of the period already in progress, except as set out in Clause 10.3.

10.2. **Credits are non-refundable.** Credits consumed or made available within a billing cycle are non-refundable, except in the case of a proven Service failure that prevents delivery of the contracted functionality (e.g., prolonged, unscheduled downtime), in which case Sygnals may, at its discretion, credit equivalent Credits for the affected period.

10.3. **Withdrawal right (where applicable).** Where Customer qualifies as a consumer under applicable Brazilian consumer-protection law (Art. 49, Código de Defesa do Consumidor), Customer may exercise a withdrawal right within 7 (seven) calendar days of contracting, by request to support, with a full refund of amounts paid during that period.

10.4. **One-time credit packs** that have been purchased and used (in whole or in part) are non-refundable.

## 11. Term, Suspension, and Termination

11.1. These Terms take effect upon acceptance and remain in force while Customer maintains an active subscription or otherwise uses the Service.

11.2. Sygnals may suspend or terminate Customer's access to the Service, upon notice, in the event of: (a) payment default; (b) breach of these Terms, in particular Clause 6 (Acceptable Use) or Clause 7 (Responsibility Regarding Third-Party Platforms); (c) use that exposes Sygnals to material legal or regulatory risk; or (d) a request from a competent authority.

11.3. Either party may terminate this agreement for convenience upon 30 (thirty) days' prior notice, without prejudice to amounts already owed.

11.4. **Effects of termination.** Upon account closure, Workspace data (including Signals and Engager Profiles) is retained for up to 30 (thirty) days after deletion of a specific Signal, and up to 90 (ninety) days after full Workspace cancellation, for data-recovery purposes at Customer's request and to meet legal obligations, after which it is permanently deleted, as detailed in the [Privacy Policy](/legal/privacy).

## 12. Intellectual Property

12.1. Sygnals owns all intellectual property rights in the Service, including software, trademarks, design, the Intent Score calculation algorithm, and other proprietary technology. Nothing in these Terms transfers such rights to Customer.

12.2. Customer receives a limited, non-exclusive, non-transferable, revocable license to use the Service during the subscription term, solely for its own internal business purposes.

12.3. Data exported by Customer (Engager Profiles, CSV exports) may be freely used by Customer for its own commercial prospecting purposes, subject to the limitations in Clause 6 and applicable data-protection law.

## 13. Third-Party Content and Infringement Notices

If Customer identifies content made available through the Service that infringes copyright or other intellectual property rights, it should notify Sygnals at **[support@sygnals.ai]**, identifying the material, the right holder, and its location within the Service, so that we can take appropriate action.

## 14. Confidentiality

Each party agrees to keep confidential any confidential information of the other party obtained in connection with this agreement, using it solely for the purposes contemplated herein, for the term of this agreement and for 2 (two) years thereafter. Information is not considered confidential if it: (a) is or becomes public through no breach of this agreement; (b) was already known to the receiving party before disclosure; or (c) must be disclosed under law or court order.

## 15. Data Protection

Processing of personal data by Sygnals — both Customer account data and Engager data captured through Signals — is governed by our [Privacy Policy](/legal/privacy), which forms an integral part of these Terms.

Customer acknowledges that: (a) Sygnals acts as controller of Engager data at the point of collection and enrichment, as described in the Privacy Policy; (b) once data is delivered to Customer (via table, CSV export, Clay, or webhook), **Customer becomes an independent controller** of that data for its own prospecting purposes, and is solely responsible for any processing it carries out from that point forward, including compliance with the LGPD, the GDPR (where EU-based data subjects are involved), and any other data-protection law applicable to its activities.

Customer agrees to process Engager data received through the Service in a manner consistent with the purpose that legitimizes its collection (legitimate B2B commercial prospecting), and to honor any deletion or objection requests submitted by Engagers.

## 16. Warranties and Disclaimers

THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE," WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, UNINTERRUPTED AVAILABILITY, OR ABSENCE OF ERRORS.

Sygnals does not warrant: (a) the absolute accuracy of Engager data, inferred attributes, or the Intent Score, which depend on third-party data and internal heuristics subject to error; (b) that the Service will result in any particular volume of leads, conversions, or business outcomes; (c) the continuous availability of third-party Data Providers (Apify, Unipile) on which the Service depends.

## 17. Limitation of Liability

To the maximum extent permitted by applicable law, Sygnals' total aggregate liability to Customer arising out of or related to these Terms or use of the Service is limited to the amount Customer actually paid to Sygnals in the 12 (twelve) months immediately preceding the event giving rise to the claim.

In no event will Sygnals be liable for lost profits, data loss, lost business opportunity, or indirect, incidental, special, or consequential damages, even if advised of the possibility of such damages.

This limitation does not apply to damages arising from willful misconduct, fraud, or breach of confidentiality or data-protection obligations, to the extent such limitation is prohibited by law.

## 18. Indemnification

Customer agrees to indemnify and hold harmless Sygnals, its officers, and personnel, from any claims, losses, damages, or expenses (including reasonable attorneys' fees) arising from: (a) use of the Service in breach of these Terms; (b) Customer's breach of the terms of use of any third-party platform, including LinkedIn; (c) Customer's misuse of Engager data obtained through the Service, including violations of the LGPD, the GDPR, or other data-protection laws applicable to Customer's role as controller of that data.

## 19. Service Level

Sygnals uses commercially reasonable efforts to keep the Service available and operational, but does not warrant any specific uptime percentage (SLA) in this version of the Service, unless separately contracted in writing. Scheduled maintenance will be communicated with reasonable advance notice whenever possible.

## 20. Changes to These Terms

Sygnals may update these Terms from time to time, publishing the updated version on this page with a revised "last updated" date. Material changes will be communicated to Customer by email or in-app notice at least 15 (fifteen) days before taking effect. Continued use of the Service after changes take effect constitutes acceptance of those changes.

## 21. Governing Law and Jurisdiction

These Terms are governed by the laws of the Federative Republic of Brazil. The courts of **São Paulo/SP, Brazil** shall have exclusive jurisdiction to resolve any dispute arising from these Terms, and the parties expressly waive any other jurisdiction, however privileged.

## 22. General Provisions

22.1. If any provision of these Terms is held invalid or unenforceable, the remaining provisions will remain in full force and effect.

22.2. Any failure by either party to enforce any provision will not constitute a waiver of the right to enforce it later.

22.3. Customer may not assign or transfer its rights and obligations under these Terms without Sygnals' prior written consent. Sygnals may assign this agreement in connection with a corporate reorganization, merger, or sale of assets, upon notice to Customer.

22.4. These Terms, together with the Privacy Policy, constitute the entire agreement between the parties regarding their subject matter, superseding any prior understandings, written or oral.

22.5. Formal communications between the parties must be made in writing, to the email addresses registered on the platform.

---

**Contact:** [support@sygnals.ai] · **Data Protection Officer:** [privacy@sygnals.ai]
