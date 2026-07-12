# Privacy Policy — Sygnals

**Version:** 1.0
**Last updated:** July 12, 2026
**Controlling language:** For data subjects and customers in Brazil, the Portuguese-language version of this Policy controls. For all other data subjects and customers, this English version controls.


---

## Table of Contents

1. [Who We Are](#1-who-we-are)
2. [Scope of This Policy](#2-scope-of-this-policy)
3. [Data We Collect](#3-data-we-collect)
4. [Where the Data Comes From](#4-where-the-data-comes-from)
5. [How We Use the Data](#5-how-we-use-the-data)
6. [Legal Bases for Processing](#6-legal-bases-for-processing)
7. [Legitimate Interest: Our Assessment](#7-legitimate-interest-our-assessment)
8. [Intent Score and Automated Decision-Making](#8-intent-score-and-automated-decision-making)
9. [Who We Share Data With](#9-who-we-share-data-with)
10. [International Data Transfers](#10-international-data-transfers)
11. [How Long We Keep Data](#11-how-long-we-keep-data)
12. [Information Security](#12-information-security)
13. [Notice for Monitored Individuals ("Engagers")](#13-notice-for-monitored-individuals-engagers)
14. [Your Rights as a Data Subject](#14-your-rights-as-a-data-subject)
15. [Cookies and Similar Technologies](#15-cookies-and-similar-technologies)
16. [Children](#16-children)
17. [Changes to This Policy](#17-changes-to-this-policy)
18. [Contact and Data Protection Officer](#18-contact-and-data-protection-officer)

---

## 1. Who We Are

This Privacy Policy is published by **TLA DIGITAL LTDA - ME**, registered under Brazilian company registration number (CNPJ) **54.958.502/0001-59**, with registered address at **Av. Paulista, 1106, Sala 01, Bela Vista, São Paulo/SP, CEP 01310-914** ("**Sygnals**," "**we**"), controller of the personal data described in this Policy. We process personal data in accordance with the Brazilian General Data Protection Law (LGPD, Law No. 13,709/2018) and, where applicable to EU/UK data subjects, the General Data Protection Regulation (GDPR).

## 2. Scope of This Policy

This Policy applies to **two distinct categories of data subjects**, addressed differently throughout this document:

- **(a) Sygnals customers and users** — people who create an account, configure Workspaces, and use the platform; and
- **(b) Engagers** — individuals who have publicly interacted on LinkedIn (reactions, comments, profile visits, new follows, connection requests) with a profile monitored by a Customer through Sygnals, and who **have never signed up for Sygnals and have no direct relationship with us**.

If you are an Engager and arrived at this page through a link in an email, from a Sygnals customer, or through a direct search, please go directly to **[Section 13](#13-notice-for-monitored-individuals-engagers)**, written specifically for you.

## 3. Data We Collect

### 3.1. Customer Data (platform users)

- Registration data: name, email, profile photo (via Google OAuth), password or authentication method.
- Workspace data: company name, Signal configurations, configured integrations (webhook URLs, configuration names).
- Billing data: processed by Stripe (we do not store full card data).
- Usage data: platform interactions, technical logs, support data.

### 3.2. Engager Data (monitored individuals)

For each Engager identified through a Signal configured by a Customer, we may process:

- **Public LinkedIn data**: name, declared headline/job title, public profile photo, profile URL, location (country/city where publicly available), public comment text (where applicable), reaction type, post/comment date.
- **Connected-account data** (only when a Customer connects its own LinkedIn account via Unipile): profile visitors, new followers, follow-detection timestamp.
- **Attributes we infer**: job title and company (derived by parsing the public headline), seniority (internal classification based on title), function/department (internal classification), geographic region (derived from country), and the **Intent Score** (a 0–100 score calculated from engagement frequency, inferred seniority, engagement type, and recency — see Section 8).

**We do not collect, and our product is designed to never infer,** special-category / sensitive data (racial or ethnic origin, religious belief, political opinion, trade union membership, health or sex-life data, genetic or biometric data).

## 4. Where the Data Comes From

- **From you directly** (if you are a Customer): at signup and through platform use.
- **From public LinkedIn sources**, collected through a specialized third-party public-data provider (Apify), without use of LinkedIn session cookies or a browser extension — this applies to Signals based on public posts, reactions, and comments.
- **From LinkedIn accounts the Customer itself connects**, through a third-party provider (Unipile), when the Customer authorizes access to its own account or Sales Navigator account to collect signals such as profile visitors and new followers. This collection is authorized and configured by the Customer, not by the Engager.

## 5. How We Use the Data

- Operate, maintain, and improve the Service.
- Process Signals configured by Customers and generate Engager Profiles.
- Calculate the Intent Score for commercial prioritization.
- Deliver data to Customers via in-app table, CSV export, Clay integration, or generic webhook.
- Process payments and manage subscriptions.
- Comply with legal and regulatory obligations.
- Support communications and operational notices.

We do not use Engager data for targeted advertising, sale to unauthorized third parties, or any purpose beyond delivery to the Customer that configured the corresponding Signal.

## 6. Legal Bases for Processing

| Data category | LGPD legal basis | GDPR legal basis (where applicable) |
|---|---|---|
| Customer data (registration, usage, billing) | Performance of a contract (Art. 7, V) | Performance of a contract (Art. 6(1)(b)) |
| Engager data — public collection via Apify | Legitimate interest (Art. 7, IX) | Legitimate interest (Art. 6(1)(f)) |
| Engager data — Customer-connected account via Unipile | Legitimate interest of the Customer and of Sygnals as operator (Art. 7, IX) | Legitimate interest (Art. 6(1)(f)) |
| Compliance with legal obligations (e.g., tax) | Legal obligation (Art. 7, II) | Legal obligation (Art. 6(1)(c)) |

## 7. Legitimate Interest: Our Assessment

Because Engagers never interact directly with Sygnals or give us consent, we process this data on the basis of **legitimate interest** under LGPD Art. 7, IX (and GDPR Art. 6(1)(f), where applicable). Before launching this processing, we ran a three-part balancing test, following the methodology set out in the Brazilian data protection authority's (ANPD) Guidance on Legitimate Interest and the GDPR three-step test:

**(a) Legitimate purpose.** The interest we pursue is concrete and specific: to help businesses identify, among people who have already publicly signaled interest in a topic (by reacting to or commenting on a post), those most likely to have genuine commercial interest — a practice already established in the B2B sales-intelligence industry (e.g., Clay, Trigify, and similar tools).

**(b) Necessity.** We collect only the data strictly necessary for this purpose: basic identification, public professional data, and the content of the engagement itself (comment/reaction). We do not collect special-category data, and we do not conduct continuous, unlimited collection — each Signal is scoped to a specific profile configured by a Customer, with per-run volume limits.

**(c) Balancing against the data subject's rights.** We recognize that Engagers do not have a specific prior expectation that their public data will be processed this way. To address this, we have implemented the following safeguards:
- we publish this Policy openly, including a **dedicated notice for Engagers** (Section 13), accessible without an account;
- we offer a **simple objection-and-deletion channel** that requires no signup (see Section 13);
- we limit processing to **professional data**, never special-category data;
- the Intent Score and inferred attributes are used only for the Customer's commercial prioritization — they **do not trigger any automated decision with legal or similarly significant effect on the Engager** (see Section 8);
- we keep an internal record of this legitimate-interest assessment, available to the ANPD or other competent authority upon request, per LGPD Art. 37 and GDPR Art. 5(2) accountability requirements.

We re-assess this balance whenever the product evolves in a way that expands the volume, sensitivity, or scope of the data processed.

## 8. Intent Score and Automated Decision-Making

The Intent Score is a 0–100 score, calculated through transparent internal rules based on four factors: (1) engagement frequency over the last 30 days; (2) inferred seniority based on the publicly declared job title; (3) engagement type (a comment weighs more than a reaction); and (4) time decay (older engagements score lower).

This calculation **does not constitute automated decision-making with legal or similarly significant effects** on the Engager under LGPD Art. 20 or GDPR Art. 22: it merely organizes and prioritizes, for the Customer, information that is already public or to which the Customer already has legitimate access, without producing any automatic effect (it does not block, deny, or grant access to anything, and is not used for credit, employment, or similar decisions). Any data subject may nonetheless request human review and information about the criteria behind their own Intent Score, per Section 14.

## 9. Who We Share Data With

We share data with the following sub-processors, strictly to operate the Service:

| Sub-processor | Purpose | Location |
|---|---|---|
| Apify | Public LinkedIn data collection | EU |
| Unipile | Access to signals based on Customer-connected LinkedIn accounts | EU |
| MongoDB Atlas | Database hosting | Per contracted region |
| Railway | Backend and worker hosting | USA |
| Vercel | Frontend hosting | USA |
| Cloudflare (R2) | CSV export file storage | Global (Cloudflare network) |
| Stripe | Payment processing | USA/Global |
| Resend | Transactional email delivery | USA |
| OpenAI | Job-title classification fallback (~5% of cases, no sensitive data) | USA |
| Sentry / PostHog | Error monitoring and product analytics | USA/EU |
| Clay / Customer webhook | Delivery of Engager Profiles, per the integration the Customer itself configures | Per Customer configuration |

We do not sell personal data to third parties. Sharing with the Customer that configured the corresponding Signal is the Service's core purpose; once delivered, the Customer becomes an independent controller of that data (see Clause 15 of the [Terms of Service](/legal/terms)).

## 10. International Data Transfers

Some of the sub-processors listed in Section 9 are located outside Brazil. Where this occurs, we rely on the international-transfer mechanisms available under LGPD Art. 33 and ANPD Resolution 19/2024 (Brazilian standard contractual clauses) with the relevant sub-processors. For EU/UK data subjects, we rely, where applicable, on the European Commission's Standard Contractual Clauses (SCCs) or the UK International Data Transfer Addendum (IDTA).

## 11. How Long We Keep Data

- **Customer data**: for as long as the account remains active, and for up to 90 (ninety) days after Workspace cancellation, for data-recovery purposes and to meet legal obligations.
- **Engager data**: for as long as the corresponding Signal remains active, and for up to 30 (thirty) days after deletion of a specific Signal, after which the data is permanently deleted, unless a longer retention period is legally required.
- **Engager deletion requests** (Section 13) are handled within a period consistent with applicable law, typically within 15–30 days depending on jurisdiction.

## 12. Information Security

We implement technical and organizational measures to protect personal data, including: encryption at rest (AES-256-GCM for webhook credentials, SHA-256 hashing for API keys), mandatory multi-tenant access control on all endpoints, and encrypted connections in transit (TLS). No system is completely secure; in the event of a relevant security incident, we will notify the ANPD, relevant EU/UK supervisory authorities, and affected data subjects as required by applicable law (including LGPD Art. 48 and GDPR Arts. 33–34).

## 13. Notice for Monitored Individuals ("Engagers")

> **This section is written directly for you, if you reacted to, commented on, visited a profile linked to, or followed someone on LinkedIn, and were identified by a Sygnals customer through our platform. You do not need a Sygnals account to exercise the rights described here.**

### What we do with your data

A Sygnals customer (a company doing B2B sales outreach) monitors a LinkedIn profile — possibly its own profile, or that of a competitor or partner. When you react to, comment on, visit, or follow a monitored profile, our system may identify your interaction, collect the associated public data (name, declared job title, comment text, etc.), and present it to that customer, along with an internal commercial-priority score (Intent Score).

### Why this is permitted

We process this data on the basis of **legitimate interest** (LGPD Art. 7, IX; GDPR Art. 6(1)(f), where applicable), as detailed in Section 7 above. Your interaction was already public at the moment it occurred; we are simply organizing that public information for legitimate B2B commercial prospecting purposes.

### What you can do

At any time, and **without needing to create an account**, you can:

- **Request access** to the data we hold about you;
- **Request deletion** of your data from our database;
- **Object** to processing based on legitimate interest, under LGPD Art. 18 §2 or GDPR Art. 21;
- **Request correction** of inaccurate data.

To exercise any of these rights, email **[admin@sygnals.in]** with a link to your LinkedIn profile so we can locate your data. We will respond within 30 days (or sooner where required by applicable law).

### What we don't do

We do not use your data for targeted advertising, we do not sell it to third parties unrelated to the Signal that generated the collection, and we do not make any automated decision about you with a legal or similarly significant effect.

## 14. Your Rights as a Data Subject

Under LGPD Art. 18 and, where applicable, the corresponding GDPR provisions, you have the right to:

- confirmation that processing is taking place;
- access to your data;
- correction of incomplete, inaccurate, or outdated data;
- anonymization, blocking, or deletion of unnecessary data, or data processed unlawfully;
- data portability to another service provider;
- deletion of data processed with consent (where applicable);
- information about public and private entities with which we share data;
- information about the possibility of not providing consent and the consequences of refusal (where consent is the applicable legal basis);
- withdrawal of consent (where applicable);
- **objection** to processing carried out on the basis of legitimate interest;
- review of decisions made solely through automated processing that affect your interests.

To exercise these rights, contact us at the email in Section 18. You also have the right to lodge a complaint with the Brazilian National Data Protection Authority (ANPD) or, where applicable, with your country's data protection authority (e.g., an EU supervisory authority or the UK ICO).

## 15. Cookies and Similar Technologies

We use cookies strictly necessary for authentication and platform functionality, plus product-analytics tooling (PostHog) to understand how authenticated Customers use the application. We do not use advertising-tracking cookies, either on our marketing site or within the application.

## 16. Children

The Service is intended solely for professional use by individuals aged 18 or older, acting as representatives of a business. We do not direct the Service at children and do not knowingly collect data from minors.

## 17. Changes to This Policy

We may update this Policy from time to time. Material changes will be communicated to Customers by email or in-app notice, with an updated effective date. We recommend reviewing this page periodically.

## 18. Contact and Data Protection Officer

To exercise your rights, ask questions about this Policy, or report a privacy concern:

**Data Protection Officer:** [NAME]
**Email:** [admin@sygnals.in]
**Address:** Av. Paulista, 1106, Sala 01, Bela Vista, São Paulo/SP, CEP 01310-914

Brazilian data subjects may also file a complaint with the Autoridade Nacional de Proteção de Dados (ANPD) at **gov.br/anpd**. EU/UK data subjects may file a complaint with their local supervisory authority.
