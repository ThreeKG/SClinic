# IDEA.md Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Produce a client-ready technical audit of `https://www.sclinic.com.tr` and `https://www.sclinic.ae`, then turn the audit into a commercial redevelopment proposal.

**Architecture:** This work is a documentation pipeline, not a code feature. The implementation should collect evidence from both sites, normalize findings into a structured audit, and then synthesize those findings into a proposal with prioritized recommendations, business impact, and a migration/rebuild strategy.

**Tech Stack:** Browser inspection, curl-based HTTP checks, Lighthouse, security header analysis, manual UX review, and markdown deliverables.

---

## Assumptions

- This repository is currently a documentation/workplan space, not an app codebase.
- Final deliverables should be written as professional markdown documents that can be exported to PDF or presented to the client.
- The audit should be evidence-based for both domains and should distinguish findings per site where behavior differs.

## Proposed Deliverables

Create the following files as the project matures:

- `deliverables/01-technical-audit-report.md`
- `deliverables/02-website-rebuild-proposal.md`
- `evidence/` for screenshots, headers, Lighthouse exports, and raw notes
- `notes/` for working observations and site-specific findings

---

## Task 1: Set up the audit workspace

**Objective:** Create a clean structure for evidence, notes, and final documents so all findings are traceable.

**Files:**
- Create: `deliverables/`
- Create: `evidence/`
- Create: `notes/`
- Create: `.hermes/plans/2026-07-14_113414-idea-md-implementation-plan.md`

**Step 1: Create the project folders**

Use the repository root as the workspace and ensure the deliverable directories exist.

**Step 2: Define naming conventions**

Use consistent naming for site-specific evidence:
- `evidence/sclinic-com-tr/`
- `evidence/sclinic-ae/`
- `notes/sclinic-com-tr.md`
- `notes/sclinic-ae.md`

**Step 3: Confirm the structure**

Verify the directory layout before beginning data collection.

**Validation:**
- Each site has its own evidence folder
- Each site has its own notes file
- Final documents have stable output paths

---

## Task 2: Collect baseline technical evidence for both sites

**Objective:** Gather reproducible baseline data from each website.

**Files:**
- Create: `evidence/sclinic-com-tr/headers.txt`
- Create: `evidence/sclinic-ae/headers.txt`
- Create: `evidence/sclinic-com-tr/robots.txt`
- Create: `evidence/sclinic-ae/robots.txt`
- Create: `evidence/sclinic-com-tr/sitemap.xml`
- Create: `evidence/sclinic-ae/sitemap.xml`
- Create: `notes/sclinic-com-tr.md`
- Create: `notes/sclinic-ae.md`

**Step 1: Capture HTTP response headers**

Record the response headers for the homepage and any key landing pages.

**Step 2: Capture robots and sitemap behavior**

Check whether `robots.txt` and `sitemap.xml` exist, are accessible, and point to expected resources.

**Step 3: Record redirect behavior**

Note canonical domain behavior, HTTPS redirects, trailing slash conventions, and any redirect chains.

**Step 4: Write raw notes**

Summarize initial observations in each site-specific notes file.

**Validation:**
- Headers are saved for both domains
- robots.txt and sitemap status are documented
- Redirect behavior is clear and comparable across both sites

---

## Task 3: Run performance analysis on both sites

**Objective:** Produce a measurable performance assessment grounded in Lighthouse and browser observations.

**Files:**
- Create: `evidence/sclinic-com-tr/performance/lighthouse.json`
- Create: `evidence/sclinic-ae/performance/lighthouse.json`
- Create: `evidence/sclinic-com-tr/performance/screenshots/`
- Create: `evidence/sclinic-ae/performance/screenshots/`
- Update: `notes/sclinic-com-tr.md`
- Update: `notes/sclinic-ae.md`

**Step 1: Measure Lighthouse metrics**

Capture Performance, Accessibility, Best Practices, and SEO scores for representative pages.

**Step 2: Inspect render-blocking resources**

Identify CSS, JavaScript, fonts, and third-party resources that delay first render or interactivity.

**Step 3: Review mobile and desktop behavior**

Record differences in loading, layout stability, and interaction readiness between device classes.

**Step 4: Save screenshots and traces**

Keep visual evidence for any obvious issues such as layout shifts, broken assets, or delayed content.

**Validation:**
- Lighthouse output exists for both sites
- Evidence points to concrete bottlenecks, not generic guesses
- Mobile and desktop notes differ where relevant

---

## Task 4: Run security review on both sites

**Objective:** Assess the public security posture and document likely risks.

**Files:**
- Create: `evidence/sclinic-com-tr/security/headers-analysis.md`
- Create: `evidence/sclinic-ae/security/headers-analysis.md`
- Create: `evidence/sclinic-com-tr/security/findings.md`
- Create: `evidence/sclinic-ae/security/findings.md`
- Update: `notes/sclinic-com-tr.md`
- Update: `notes/sclinic-ae.md`

**Step 1: Review security headers**

Check for CSP, HSTS, X-Frame-Options or frame-ancestors, X-Content-Type-Options, referrer policy, permissions policy, and cookie flags where observable.

**Step 2: Inspect exposed surface area**

Look for directory listing, publicly exposed admin paths, version leakage, and third-party script exposure.

**Step 3: Review transport security**

Check HTTPS behavior, certificate configuration, and obvious TLS issues.

**Step 4: Document risks using OWASP framing**

Categorize issues by severity and likely impact.

**Validation:**
- Each finding has evidence or a reproducible check
- Security issues are separated into confirmed vs inferred
- Risk language is specific and client-friendly

---

## Task 5: Run SEO and content-structure review

**Objective:** Evaluate technical SEO, metadata quality, crawlability, and semantic structure.

**Files:**
- Create: `evidence/sclinic-com-tr/seo/findings.md`
- Create: `evidence/sclinic-ae/seo/findings.md`
- Create: `evidence/sclinic-com-tr/seo/page-samples.md`
- Create: `evidence/sclinic-ae/seo/page-samples.md`
- Update: `notes/sclinic-com-tr.md`
- Update: `notes/sclinic-ae.md`

**Step 1: Check crawlability and indexability**

Review robots directives, canonical tags, sitemap coverage, and indexation signals.

**Step 2: Inspect on-page metadata**

Capture title tags, meta descriptions, heading hierarchy, ALT text patterns, and structured data.

**Step 3: Assess internal linking and URL structure**

Look for duplicate paths, broken links, weak anchor text, and inconsistent URL patterns.

**Step 4: Record SEO opportunities**

Identify fixes that would improve discoverability and click-through.

**Validation:**
- Findings are tied to sample pages and specific tags
- Technical SEO and on-page SEO are both covered
- Recommendations are tied to search impact

---

## Task 6: Run UI / UX and accessibility review

**Objective:** Evaluate the experience on desktop and mobile with a healthcare-trust lens.

**Files:**
- Create: `evidence/sclinic-com-tr/ux/review.md`
- Create: `evidence/sclinic-ae/ux/review.md`
- Create: `evidence/sclinic-com-tr/ux/screenshots/`
- Create: `evidence/sclinic-ae/ux/screenshots/`
- Update: `notes/sclinic-com-tr.md`
- Update: `notes/sclinic-ae.md`

**Step 1: Inspect navigation and information architecture**

Evaluate whether primary user journeys are obvious and low-friction.

**Step 2: Review responsive behavior**

Check mobile menus, text scaling, image cropping, spacing, and CTA visibility.

**Step 3: Assess accessibility basics**

Review contrast, heading order, focus visibility, form labels, keyboard reachability, and semantic structure.

**Step 4: Assess trust and conversion quality**

Check for healthcare trust signals, consistent branding, clear contact paths, and strong calls to action.

**Validation:**
- Each issue is visible in screenshots or verifiable in page markup
- Mobile-specific and desktop-specific concerns are separated
- Accessibility observations are practical, not theoretical

---

## Task 7: Synthesize the technical audit report

**Objective:** Convert raw findings into a polished client-facing audit document.

**Files:**
- Create: `deliverables/01-technical-audit-report.md`
- Read from: `notes/sclinic-com-tr.md`
- Read from: `notes/sclinic-ae.md`
- Read from: `evidence/**`

**Step 1: Write the executive summary**

Summarize the biggest opportunities, risks, and why the current state matters.

**Step 2: Add site-by-site overview sections**

Cover the current technology stack, major performance blockers, security posture, SEO issues, and UX gaps.

**Step 3: Prioritize findings**

Group issues into critical, high, medium, and low priority.

**Step 4: Add business impact language**

Translate technical issues into operational, marketing, and conversion consequences.

**Validation:**
- The report reads cleanly without needing the raw evidence folder
- Findings are organized by severity and business effect
- Every major claim is supported by collected evidence

---

## Task 8: Write the redevelopment proposal

**Objective:** Turn the audit into a persuasive proposal for rebuilding the websites.

**Files:**
- Create: `deliverables/02-website-rebuild-proposal.md`
- Read from: `deliverables/01-technical-audit-report.md`

**Step 1: State the problem and why a rebuild is justified**

Explain the current limitations and why incremental fixes are insufficient.

**Step 2: Propose the solution architecture**

Recommend the CMS, frontend approach, hosting, security model, performance strategy, SEO strategy, and analytics setup.

**Step 3: Define phases and timeline**

Break the rebuild into discovery, design, development, content migration, QA, launch, and post-launch stabilization.

**Step 4: Estimate effort and assumptions**

Make assumptions explicit so the client can evaluate scope and budget.

**Validation:**
- The proposal is commercially persuasive
- Technical choices map back to audit findings
- Timeline and scope are realistic

---

## Task 9: Final quality pass

**Objective:** Make the two deliverables presentation-ready.

**Files:**
- Update: `deliverables/01-technical-audit-report.md`
- Update: `deliverables/02-website-rebuild-proposal.md`

**Step 1: Review for clarity and consistency**

Ensure naming, tone, and severity levels are consistent across both documents.

**Step 2: Check for unsupported claims**

Remove or qualify anything not backed by evidence.

**Step 3: Improve readability**

Use tables, bullet points, and concise section summaries where helpful.

**Step 4: Prepare for export**

Verify markdown structure is clean enough to convert to PDF or DOCX later.

**Validation:**
- No contradictions between audit and proposal
- Recommendations align with findings
- Both documents are client-ready

---

## Risks and Tradeoffs

- Site behavior may vary by locale, device, or cookies, so evidence should be gathered in a controlled browser session and noted carefully.
- Some security and performance issues will be inferred rather than directly proven; those should be labeled as such.
- The quality of the final proposal depends on the completeness of the audit evidence.

## Open Questions

- Should the final deliverables be markdown only, or also exported to PDF/DOCX?
- Should the audit include screenshots embedded inline, or remain as linked evidence?
- Is the client expecting a single combined report for both sites, or separate sections per domain?

## Success Criteria

- The audit identifies the major technical issues on both sites.
- The proposal clearly explains why redevelopment is warranted.
- Findings are backed by evidence and organized in a client-friendly way.
- The deliverables are professional enough to present directly to stakeholders.
