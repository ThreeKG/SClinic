# Hermes Website Rebuild Proposal

**Prepared from:** `deliverables/01-technical-audit-report.md`

**Business goal:** Replace the legacy, hard-to-maintain website stack with a modern healthcare web platform that is faster, more secure, easier to manage, and more effective at converting visitors into consultations.

---

## Executive Summary

The audit shows a strong business case for a rebuild rather than incremental patching. Both sites share the same legacy technical foundation, runtime bugs, poor performance efficiency, accessibility defects, and a dense homepage structure that obscures the primary call to action.

A rebuild will deliver:

- faster pages and better Core Web Vitals
- cleaner Turkish / English market separation
- a more trustworthy healthcare UX
- stronger SEO foundations
- better security defaults
- easier content management for internal teams

---

## 1) Existing problems

### Proof-backed issues

1. **Legacy stack** — both sites run on `nginx + PHP/7.4.33 + PleskLin` with old jQuery-era assets.
2. **Runtime bug** — Lighthouse found a JS exception in `aliaygir.js` on both sites.
3. **Performance waste** — unused JS, cache inefficiency, image delivery inefficiency, and layout shifts are all material.
4. **UX clutter** — repeated hero slides and duplicated CTAs weaken message clarity.
5. **Accessibility gaps** — missing landmarks, alt text, button names, contrast issues, and link labeling issues.
6. **Localization drift** — the `.ae` sitemap still contains Turkish legacy routes.

### Business impact

These issues reduce trust, reduce consultation conversion potential, and make updates more expensive than they should be.

---

## 2) Proposed solution

Build a modern, component-based healthcare website platform with:

- a clean content model
- a reusable design system
- localized Turkish / English experiences
- clear booking and consultation funnels
- SEO-safe page templates
- performance budgets and accessibility standards baked in

The solution should be designed as a maintainable platform, not a one-off brochure site.

---

## 3) Recommended technology stack

### CMS recommendation

**Recommended:** WordPress with a custom block/theme architecture or a headless CMS if the team can support it.

**Why:**

- the business likely needs frequent content updates
- editorial speed matters for clinics and locations
- multilingual content is required
- SEO and landing page creation need to stay flexible

If the client already relies on WordPress workflows, use a custom WordPress implementation with strict performance and component standards rather than a page-builder-heavy setup.

### Frontend recommendation

- semantic HTML
- modern CSS architecture
- minimal JavaScript
- component-based UI system
- no old jQuery dependency for primary UI behavior

### Hosting recommendation

- managed hosting or a well-tuned cloud environment
- CDN enabled
- image optimization pipeline
- object caching / page caching where appropriate
- automated backups and rollback support

### Analytics recommendation

- Google Analytics 4
- Google Tag Manager with governance
- conversion events for consultation lead actions
- consent-aware tracking if required by market/legal constraints

---

## 4) Suggested architecture

### Page model

- Home
- About
- Scientific Approach
- Treatment / Process pages
- Locations / Clinics
- Blog / Knowledge center
- FAQ
- Contact / Consultation
- Legal pages

### Content architecture

- one shared design system
- locale-specific copy and routing
- location templates with structured data
- blog templates optimized for search intent
- CTA components reused consistently across the site

### Functional approach

- primary CTA: Book consultation
- secondary CTA: Learn more / contact / locations
- location-specific conversion paths
- clear trust blocks for medical credibility and patient reassurance

---

## 5) Feature list

### Core features

- consultation booking CTA system
- clinic/location pages
- services / treatments pages
- FAQ module
- blog / educational content area
- before/after or testimonial module if legally appropriate
- lead capture forms
- call / WhatsApp / contact actions
- multilingual routing
- analytics events

### Optional features

- patient journey content blocks
- downloadable treatment guide
- structured schema for locations and articles
- chatbot / support integration if truly needed

---

## 6) Functional requirements

- Users can find consultation actions within the first screen.
- Users can identify services, locations, and trust signals quickly.
- Editors can update content without code changes.
- Each locale can have separate metadata and URLs.
- Pages must be responsive and accessible by default.
- Core pages should be lightweight and cacheable.

---

## 7) Non-functional requirements

- target strong Core Web Vitals
- accessible to WCAG 2.1 AA standards where feasible
- secure by default with hardened headers and cookies
- search-friendly URL structure
- maintainable and version-controlled components
- fast image delivery and caching
- zero dependence on legacy JS for basic browsing

---

## 8) SEO strategy

### Must-haves

- clean metadata templates
- canonical tags
- per-locale sitemap strategy
- structured data for organization, clinic/location, and articles
- fast mobile performance
- internal linking plan
- content clusters for treatment education

### Migration note

The rebuild must preserve or intentionally redirect existing ranking URLs. The `.ae` legacy Turkish routes should be reviewed carefully so they either map to the right English equivalents or are retired with proper redirects.

---

## 9) Security strategy

- add a security header baseline
- use secure, modern cookie flags
- eliminate unnecessary third-party scripts
- remove legacy libraries where possible
- keep dependencies current
- set up backups and rollback procedures
- review forms and lead capture for spam protection

---

## 10) Performance strategy

- reduce JS payloads
- remove old jQuery/plugin dependencies where possible
- use modern image formats and responsive images
- defer non-critical scripts
- implement caching correctly
- minimize layout shift by reserving image and component dimensions
- create a performance budget for each template

---

## 11) Accessibility strategy

- semantic landmarks
- proper heading hierarchy
- descriptive link and button text
- alt text standards
- visible focus states
- sufficient color contrast
- keyboard-friendly navigation
- mobile touch-target sizing

---

## 12) Analytics strategy

- define conversion events before launch
- track consultation CTA clicks
- track form starts and form submits
- track phone and messaging clicks
- track location-page engagement
- keep tag governance documented so marketing changes do not break UX

---

## 13) Migration plan

### Phase 1: Discovery and content audit

- inventory current pages, routes, and assets
- decide which URLs must be preserved
- define the new content model
- map the Turkish and English site structures

### Phase 2: Design system and IA

- design reusable components
- establish visual hierarchy and CTA rules
- finalize mobile-first layouts

### Phase 3: Build

- implement templates
- migrate core content
- configure forms and analytics
- implement SEO and accessibility foundations

### Phase 4: QA and launch

- run browser QA
- verify redirects
- validate forms, analytics, and performance
- launch with rollback plan

### Phase 5: Post-launch stabilization

- monitor errors, rankings, and conversions
- fix edge cases
- optimize based on real usage

---

## 14) Risks

| Risk | Mitigation |
|---|---|
| URL/ranking loss during migration | Redirect mapping, sitemap control, Search Console monitoring |
| Content localization mistakes | Separate locale ownership and review workflow |
| Reintroducing performance bloat | Performance budget and code review gates |
| Form/lead tracking issues | Pre-launch analytics QA |
| Scope creep | Freeze requirements before build phase |

---

## 15) Timeline

A realistic delivery plan for a serious rebuild is:

| Phase | Estimated duration |
|---|---:|
| Discovery / content inventory | 1–2 weeks |
| IA / design system / UX | 2–3 weeks |
| Development / integration | 4–8 weeks |
| Content migration / SEO setup | 1–3 weeks |
| QA / launch prep | 1–2 weeks |
| Post-launch stabilization | 1–2 weeks |

**Total:** roughly 8–16 weeks depending on scope, approvals, and content readiness.

---

## 16) Estimated effort

This depends on whether the client wants:

- a modest marketing-site rebuild, or
- a fully structured, multilingual healthcare platform with reusable content and analytics governance.

A reasonable delivery estimate should be finalized after the content inventory and sitemap mapping step.

---

## 17) Assumptions

- The client wants a premium healthcare presence, not a quick cosmetic refresh.
- Existing content will be reused selectively, not copied blindly.
- Both locales need a coordinated but not identical experience.
- Consultation conversion is the primary business KPI.
- Search visibility and trust are equally important outcomes.

---

## 18) Recommendation

Proceed with a rebuild in phases. The evidence shows that the current sites are already functioning, but they are carrying enough technical and UX debt that patching them will likely cost more over time than replacing the foundation properly.

---

## 19) Success criteria

The rebuild is successful if:

- pages load faster and feel more stable
- consultation CTAs are clearer and more prominent
- accessibility failures are substantially reduced
- the `.ae` site is cleanly localized
- editors can manage content without developer help
- SEO and analytics are easier to control

---

## Appendix: Source files

- `deliverables/01-technical-audit-report.md`
- `notes/sclinic-com-tr.md`
- `notes/sclinic-ae.md`
- `evidence/sclinic.com.tr/performance/lighthouse.json`
- `evidence/sclinic.ae/performance/lighthouse.json`
