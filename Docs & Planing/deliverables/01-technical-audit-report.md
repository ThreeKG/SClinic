# Hermes Technical Audit Report

**Client scope:** `sclinic.com.tr` and `sclinic.ae`

**Evidence pack:**
- `evidence/sclinic.com.tr/headers.txt`
- `evidence/sclinic.ae/headers.txt`
- `evidence/sclinic.com.tr/robots.txt`
- `evidence/sclinic.ae/robots.txt`
- `evidence/sclinic.com.tr/sitemap.xml`
- `evidence/sclinic.ae/sitemap.xml`
- `evidence/sclinic.com.tr/performance/lighthouse.json`
- `evidence/sclinic.ae/performance/lighthouse.json`
- `notes/sclinic-com-tr.md`
- `notes/sclinic-ae.md`

---

## Executive Summary

Both sites are functional and already well-indexed, but they share the same core technical profile: a legacy PHP/nginx/Plesk stack, a heavy client-side dependency chain, repeated carousel-heavy homepage content, and weak best-practice/security posture. The websites are usable, but they are not currently operating at the level expected for a premium healthcare brand.

The strongest evidence points to three strategic problems:

1. **Legacy technical foundation** — both sites report `PHP/7.4.33`, `nginx`, and `PleskLin`, with a shared custom script stack centered around old jQuery and plugin-era components.
2. **Performance and UX inefficiency** — Lighthouse reports mediocre performance, large unused JavaScript, layout shifts, and a runtime JS exception on both sites.
3. **Localization / content architecture drift** — the `.ae` site still contains Turkish legacy URLs in its sitemap, and both homepages rely on repeated hero slides and duplicated CTAs instead of a clear information hierarchy.

**Bottom line:** the evidence supports a full rebuild proposal rather than incremental patching.

---

## Method and proof standard

This report is based on direct live-site evidence from:

- HTTP response headers
- robots.txt and sitemap.xml captures
- Browser snapshot / DOM inspection
- Browser console inspection
- Lighthouse JSON outputs

Any recommendation below is tied to at least one of those sources.

---

## 1) Website overview

### 1.1 `sclinic.com.tr`

- Title: `SCLINIC BEAUTY & WELLNESS`
- Home page is content-heavy and product-heavy.
- Browser snapshot shows repeated hero slides and multiple repeated CTAs.
- Lighthouse on the homepage detected runtime JavaScript errors and accessibility failures.

### 1.2 `sclinic.ae`

- Title: `S'Clinic | Non-Surgical Hair Restoration & Skin Care | Dubai`
- Home page is similar in structure to the Turkish site.
- The page still contains legacy language and URL patterns from the Turkish site in its sitemap.
- Lighthouse again detected runtime JavaScript errors and accessibility failures.

---

## 2) Current technology stack

### Proof

The response headers on both sites show:

```text
server: nginx
x-powered-by: PHP/7.4.33
x-powered-by: PleskLin
```

Browser console also shows these client assets on both sites:

- `jquery-1.7.1.min.js`
- `owl.carousel.js`
- `jquery.lightbox.min.js`
- `jquery-ui.js`
- `jquery.lazyload.js`
- custom `aliaygir.js`
- Google Tag Manager / Google Ads / Facebook Pixel

### Assessment

This is a legacy, plugin-driven web stack. It is not automatically bad, but it tends to accumulate technical debt quickly:

- hard to maintain
- hard to optimize for Core Web Vitals
- harder to secure
- more likely to break on small DOM changes
- often difficult to evolve into a modern design system

**Risk level: High**

---

## 3) Performance analysis

### 3.1 Lighthouse summary

| Site | Performance | Accessibility | Best Practices | SEO |
|---|---:|---:|---:|---:|
| `sclinic.com.tr` | 0.71 | 0.61 | 0.54 | 0.83 |
| `sclinic.ae` | 0.65 | 0.81 | 0.54 | 0.83 |

### 3.2 Core metrics

| Metric | `sclinic.com.tr` | `sclinic.ae` |
|---|---:|---:|
| First Contentful Paint | 2.2s | 2.5s |
| Largest Contentful Paint | 2.2s | 3.5s |
| Speed Index | 3.9s | 4.7s |
| Time to Interactive | 9.9s | 12.1s |
| Total Blocking Time | 230ms | 170ms |
| CLS | 0.434 | 0.344 |

### 3.3 Proof-backed findings

- **Layout instability is a real issue**: Lighthouse reports 15 layout shifts on both sites.
- **The sites carry excessive unused JavaScript**: savings of `311 KiB` on `.com.tr` and `429 KiB` on `.ae`.
- **Images are heavier than necessary**: Lighthouse reports image delivery savings of `522 KiB` on `.com.tr` and `422 KiB` on `.ae`.
- **Caching is weak**: Lighthouse reports estimated cache-lifetime savings of `2,172 KiB` on `.com.tr` and `1,936 KiB` on `.ae`.
- **A runtime JS exception exists on both sites** in `aliaygir.js` at line 903:
  - `TypeError: Cannot read properties of null (reading 'addEventListener')`

### 3.4 Interpretation

The performance bottlenecks are not just “speed tuning” issues. They are structural:

- repeated hero/carousel assets
- legacy JS
- large images without aggressive optimization
- layout shifts from image/content insertion
- likely server-side cache weaknesses

**Risk level: High**

---

## 4) Security assessment

### 4.1 Headers and transport

The captured response headers show **no visible security headers** such as:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options` or `frame-ancestors`
- `Referrer-Policy`
- `Permissions-Policy`
- `X-Content-Type-Options`

The sites do use HTTPS, but the header posture is minimal.

### 4.2 Cookie behavior

The session cookie appears as:

```text
set-cookie: PHPSESSID=...; SameSite=None; Secure
```

No `HttpOnly` flag is visible in the capture.

### 4.3 Runtime and ecosystem issues

Lighthouse reports:

- browser errors were logged to the console
- deprecated API usage
- third-party cookies

The console exception in `aliaygir.js` is evidence of an actively broken client script.

### 4.4 Interpretation

This is not a “breach” report. There is no proof of active compromise in the evidence collected. But the public hardening posture is below best practice for a healthcare brand.

**Risk level: Medium to High**

---

## 5) SEO audit

### 5.1 Crawlability and indexability

- `robots.txt` allows all crawlers.
- Both sites explicitly list a sitemap.
- `sitemap.xml` is reachable and populated on both domains.

### 5.2 Sitemap proof

- `sclinic.com.tr` sitemap contains **60 unique URLs** and they are all Turkish/`com.tr`-oriented.
- `sclinic.ae` sitemap contains **62 unique URLs** and still includes Turkish legacy URLs such as:
  - `s-clinic-eryaman-ankaraman`
  - `s-clinic-cayyolu`
  - `s-clinic-kocaeli`
  - `s-clinic-antalya`
  - `s-clinic-ankara`

### 5.3 Meaning

This suggests that the `.ae` site has partial localization rather than a clean market-specific content architecture. That can confuse users and weaken relevance signals.

### 5.4 On-page SEO observations

- Both sites have titles and meta descriptions.
- SEO Lighthouse score is `0.83` for both, so the foundation is not broken.
- However, the duplicated hero content and mixed-market sitemap structure are not ideal for search clarity.

**Risk level: Medium**

---

## 6) UI / UX review

### 6.1 Evidence from browser snapshot

The desktop homepage snapshot shows:

- repeated hero slides with the same CTA
- dense, stacked content blocks
- multiple product and promo sections competing for attention
- a long scroll before the user reaches the main utility sections

### 6.2 Accessibility / usability proof

Lighthouse flagged issues including:

- buttons without accessible names
- insufficient color contrast
- image elements missing `alt`
- missing main landmark
- links without discernible names
- touch targets too small
- non-semantic list structure

### 6.3 Interpretation

The UX is visually polished in places, but the hierarchy is weak:

- too many repeated messages
- carousel content obscures the primary action
- conversion paths are not clearly prioritized
- accessibility gaps will affect mobile usability and SEO quality

**Risk level: High**

---

## 7) Architecture review

### Inference backed by evidence

The sites appear to share a common codebase with locale-specific content layers. Evidence:

- same server stack
- same legacy JS stack
- same homepage structure
- same runtime exception in the same custom script
- same analytics and marketing tooling
- similar sitemap patterns and overlapping legacy routes

### Architectural concerns

- monolithic legacy frontend logic
- mixed content responsibilities in a single stack
- likely difficult to separate marketing, content, and booking logic cleanly
- heavy reliance on client-side plugins for presentation and interaction

**Risk level: High**

---

## 8) Priority matrix

| Priority | Issue | Proof | Why it matters |
|---|---|---|---|
| Critical | Runtime JS exception in `aliaygir.js` | Lighthouse console error | Broken UI behavior, unstable interactions |
| Critical | Missing security headers | Header capture | Reduces protection against common web attacks |
| High | Old PHP 7.4.33 stack | Header capture | EOL risk / security maintenance burden |
| High | Excess unused JS and caching waste | Lighthouse opportunities | Slower pages, more main-thread work |
| High | Large layout shifts | CLS and layout-shift audits | Poor user experience, poorer CWV |
| High | Repeated hero/carousel content | Browser snapshot | Weak hierarchy, visual clutter |
| Medium | Mixed localization in `.ae` sitemap | `sitemap.xml` | SEO and brand consistency issues |
| Medium | Accessibility failures | Lighthouse accessibility audits | Usability, compliance, conversion impact |
| Medium | Third-party cookie / analytics complexity | Lighthouse | Privacy and performance cost |

---

## 9) Recommendations

### Immediate fixes if the current stack must remain online

1. Patch the JS exception in `aliaygir.js`.
2. Add a security header baseline.
3. Optimize image sizes and formats.
4. Add cache headers for static assets.
5. Reduce duplicate hero content on the homepage.
6. Fix accessibility issues from Lighthouse.
7. Clean the `.ae` sitemap of Turkish legacy URLs or redirect them intentionally.

### Strategic recommendation

Do not invest in heavy incremental redevelopment on this architecture. The evidence supports a controlled rebuild with a modern CMS and a cleaner content model.

---

## 10) Conclusion

The sites are not broken, but they are **structurally expensive to maintain** and **underperforming relative to the brand goals**. The audit findings justify a rebuild proposal focused on:

- better performance
- stronger security defaults
- cleaner localization
- improved accessibility
- easier content maintenance
- a more professional conversion-oriented UX

---

## Appendix: Proof references

- Headers: `evidence/sclinic.com.tr/headers.txt`, `evidence/sclinic.ae/headers.txt`
- Crawl data: `evidence/sclinic.com.tr/robots.txt`, `evidence/sclinic.ae/robots.txt`
- Sitemap proof: `evidence/sclinic.com.tr/sitemap.xml`, `evidence/sclinic.ae/sitemap.xml`
- Performance proof: `evidence/sclinic.com.tr/performance/lighthouse.json`, `evidence/sclinic.ae/performance/lighthouse.json`
- UX / console proof: browser snapshots and console inspection during live page capture
