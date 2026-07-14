# SClinic.com.tr Evidence Notes

## Baseline technical proof

- `headers.txt` shows: `server: nginx`, `x-powered-by: PHP/7.4.33`, `x-powered-by: PleskLin`.
- Security headers are not present in the captured response headers: no `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `Permissions-Policy`, or `Referrer-Policy` were returned in the header capture.
- Session cookie evidence: `set-cookie: PHPSESSID=...; SameSite=None; Secure` with no `HttpOnly` flag visible in the capture.

## SEO / crawl proof

- `robots.txt` allows crawling for `*` and explicitly allows GPTBot, ChatGPT-User, OAI-SearchBot, PerplexityBot, ClaudeBot, anthropic-ai, Google-Extended, and Bingbot.
- `sitemap.xml` contains 60 unique URLs, all Turkish/`com.tr`-oriented.

## Performance proof

- Lighthouse: Performance `0.71`, Accessibility `0.61`, Best Practices `0.54`, SEO `0.83`.
- Key metrics: FCP `2.2s`, LCP `2.2s`, Speed Index `3.9s`, TBT `230ms`, CLS `0.434`, Interactive `9.9s`.
- Lighthouse opportunities include unused JS savings `311 KiB`, cache lifetime savings `2,172 KiB`, and image delivery savings `522 KiB`.
- Lighthouse logged a runtime exception: `TypeError: Cannot read properties of null (reading 'addEventListener')` in `_dir/clinic/js/aliaygir.js?v=1.25:903`.

## UX / accessibility proof

- Browser snapshot shows repeated hero slides with the same CTA and duplicated messaging.
- Browser console showed no live console messages during one direct browser capture, but Lighthouse still flagged a runtime JS exception.
- Lighthouse failures include: buttons without accessible names, insufficient color contrast, missing image alt attributes, missing main landmark, links without discernible names, and touch targets that are too small.

## Stack / architecture proof

- Browser console lists legacy assets: `jquery-1.7.1.min.js`, `owl.carousel.js`, `jquery.lightbox.min.js`, `jquery-ui.js`, `jquery.lazyload.js`, and custom `aliaygir.js`.
- Analytics / third-party scripts include Google Tag Manager, Google Ads, and Facebook Pixel.
