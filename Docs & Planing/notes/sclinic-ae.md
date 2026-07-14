# SClinic.ae Evidence Notes

## Baseline technical proof

- `headers.txt` shows: `server: nginx`, `x-powered-by: PHP/7.4.33`, `x-powered-by: PleskLin`.
- Security headers are not present in the captured response headers: no `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `Permissions-Policy`, or `Referrer-Policy` were returned in the header capture.
- Session cookie evidence: `set-cookie: PHPSESSID=...; SameSite=None; Secure` with no `HttpOnly` flag visible in the capture.

## SEO / crawl proof

- `robots.txt` allows crawling for `*` and explicitly allows GPTBot, ChatGPT-User, OAI-SearchBot, PerplexityBot, ClaudeBot, anthropic-ai, Google-Extended, and Bingbot.
- `sitemap.xml` contains 62 unique URLs.
- The sitemap mixes English URLs with Turkish legacy URLs such as `s-clinic-eryaman-ankaraman`, `s-clinic-cayyolu`, `s-clinic-kocaeli`, `s-clinic-antalya`, and `s-clinic-ankara`, which suggests cross-market reuse or partial localization.

## Performance proof

- Lighthouse: Performance `0.65`, Accessibility `0.81`, Best Practices `0.54`, SEO `0.83`.
- Key metrics: FCP `2.5s`, LCP `3.5s`, Speed Index `4.7s`, TBT `170ms`, CLS `0.344`, Interactive `12.1s`.
- Lighthouse opportunities include unused JS savings `429 KiB`, cache lifetime savings `1,936 KiB`, and image delivery savings `422 KiB`.
- Lighthouse logged a runtime exception: `TypeError: Cannot read properties of null (reading 'addEventListener')` in `_dir/clinic/js/aliaygir.js?v=1.28:903`.

## UX / accessibility proof

- Browser snapshot shows repeated hero slides with the same CTA and duplicated messaging.
- Lighthouse failures include image alt issues, missing main landmark, links without discernible text, non-semantic list structure, and the page being blocked from back/forward cache restoration.

## Stack / architecture proof

- Browser console lists legacy assets: `jquery-1.7.1.min.js`, `owl.carousel.js`, `jquery.lightbox.min.js`, `jquery-ui.js`, `jquery.lazyload.js`, and custom `aliaygir.js`.
- Analytics / third-party scripts include Google Tag Manager, Google Ads, and Facebook Pixel.
