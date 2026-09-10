---
type: Best Practice
title: "General GPT Best Practices"
description: "Core best practices for performance, tag placement, and script execution."
resource: "https://developers.google.com/publisher-tag/guides/general-best-practices"
tags: [gpt, best-practices, performance, optimization]
timestamp: 2026-09-10T00:00:00Z
---

Integrating the Google Publisher Tag (GPT) library into your website
is in many ways the same as integrating any other third-party script. However,
there are some unique aspects of working with GPT that must be
considered to ensure you make the most of your ad space with minimal impact to
site performance. After all, [fast ads matter](https://web.dev/fast-ads-matter/).

The following sections cover the best practices to use when working on your
integration.

## Load GPT from an official source

To ensure you have access to the latest features and privacy safeguards, always
request the GPT library from an official source by using one of the URLs listed
in the following table. The URL to use depends on whether you plan to
manually enable Limited Ads (LTD) mode.

| Integration type | Script tag |
|---|---|
| **Standard** Including publishers integrated with the [IAB Europe TCF](https://support.google.com/admanager/answer/9805023). | ```html <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script> ``` |
| **Manual Limited Ads** If you want to manually enable [Limited Ads (LTD)](https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig_limitedAds). | ```html <script src="https://pagead2.googlesyndication.com/tag/js/gpt.js" async></script> ``` |

> [!NOTE]
> **Note:** Only use the googlesyndication.com URL if you intend to manually enable limited ads using the API. Using it for standard integrations may cause unnecessary network overhead and slow down ad loading.

> [!NOTE]
> **Note:** To help you comply with regulations (such as GDPR) and Google's [EU
> user consent policy](https://www.google.com/about/company/user-consent-policy/), GPT may be loaded from the standard URL with the [`crossorigin="anonymous"`](https://developer.mozilla.org/docs/Web/HTML/Attributes/crossorigin) attribute to prevent cookies from being sent with the script request.

[Limited Ads (LTD)](https://support.google.com/admanager/answer/9882911) mode enables GPT to serve ads
without accessing client-side storage (such as cookies or local identifiers).
Limited ads can be enabled in one of two ways:

1. Standard (Automatically): A Consent Management Provider (CMP) informs GPT
   that the user has not provided consent for storage access, typically using
   an IAB TCF v2.0 signal. If you use a Google-certified CMP to manage user
   consent, GPT will automatically enter Limited Ads mode based on the user's
   preferences.

   - **URL**: Load GPT from the Standard URL (doubleclick.net).
   - **No Manual Action Needed** : It is not necessary to manually call `setPrivacySettings({limitedAds: true})` when a CMP is in use, as the signals are handled automatically by the library.
2. Manually: You explicitly call the [GPT API](https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig_limitedAds) to
   request limited ads.

   - **URL** : If you intend to manually enable limited ads using the [`googletag.pubads().setPrivacySettings({limitedAds: true})`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setPrivacySettings) API, you **must** load GPT from the Limited Ads URL `googlesyndication.com`.
   - **Why** : Loading GPT from the `googlesyndication.com` domain allows additional safeguards against accessing client-side storage by default.
   - **Consequence of misconfiguration**: If GPT is loaded from the standard URL and the manual API is called, the request to enable Limited Ads will be ignored, and a warning will be logged in the Publisher Console.

### Don't serve cached versions of GPT

Never serve versions of `gpt.js`, `pubads_impl.js`, or any libraries they load
from your own server or load them from an unofficial source.

Using a locally cached version of the GPT library may not
always work in newer versions of browsers or operating systems and may not be
updated with new features and improvements. Earlier versions of the
GPT library may stop working at any time and may lead to
loss of ad revenue if ads stop serving to your tags.

This also applies to [service workers](https://developer.mozilla.org/docs/Web/API/Service_Worker_API). If you use service
workers to cache or modify responses to HTTP requests coming from your site, use
a [network-only strategy](https://developer.chrome.com/docs/workbox/caching-strategies-overview/#network-only) when handling requests for `gpt.js` in
order to fetch an up-to-date version.

## Load GPT early

The GPT library (`gpt.js`) contains only a small fraction of
the code necessary to load ads. The majority of that code is contained in
separate files (such as `pubads_impl_XX.js`), which are loaded by `gpt.js` as
needed.

By loading the core GPT library early, these dependent scripts
are also able to be loaded earlier. This avoids any extra latency related to
fetching these scripts (if uncached) and allows for ads to be loaded more
quickly. All of this contributes to lowering the
[time to render first ad metric](https://developers.google.com/publisher-ads-audits/reference/audits/first-ad-render), which in turn increases
the viewability of your ads.

### Use preload when appropriate

Sometimes you may not be in direct control of when or how GPT
is loaded. For example, when using a third-party ads script which loads
GPT on your behalf. In these cases, it may be appropriate to
preload the request for `gpt.js`. [Preloading a request](https://developers.google.com/web/tools/lighthouse/audits/preload) instructs the
browser to immediately download a specified asset that is critical to the
loading of your page. When the specified asset is a JavaScript file, the script
contents are fetched immediately but execution is deferred until the script is
needed.

#### Example preload request for standard integrations

    <link rel="preload" href="https://securepubads.g.doubleclick.net/tag/js/gpt.js" as="script">

#### Example preload request for limited ads integrations

    <link rel="preload" href="https://pagead2.googlesyndication.com/tag/js/gpt.js" as="script">

> [!NOTE]
> **Note:** preload links are not respected by all browsers. See [Can I Use link-rel-preload?](https://caniuse.com/#feat=link-rel-preload) for an overview of browser support.

### Use `fetchpriority` to prioritize script loading

You can use the [`fetchpriority`](https://developer.mozilla.org/docs/Web/HTML/Reference/Attributes/fetchpriority) attribute to signal to the
browser the relative priority of fetching GPT resources. By
default, `gpt.js` automatically requests its core implementation script
(`pubads_impl.js`) with `fetchpriority="high"` to optimize network scheduling
and reduce ad loading latency. Increasing priority may impact loading of other
resources on the page and
[Core Web Vitals metrics](https://developers.google.com/publisher-tag/guides/minimize-layout-shift#measure). To maximize
latency impact of `fetchpriority` set to high, we recommend setting on `gpt.js`
directly.

To prioritize fetching the `gpt.js` loader script itself (or to configure the
inherited priority of `pubads_impl.js`), you can add the `fetchpriority`
attribute directly to the `gpt.js` `<script>` tag:

    <script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" fetchpriority="high"></script>

When you specify the `fetchpriority` attribute on the `gpt.js` loader
`<script>` tag, the dynamically inserted implementation script automatically
inherits the specified `fetchpriority` value (such as `"high"`, `"low"`, or
`"auto"`).

### Use GPT on prerendered pages

[Prerendering](https://developer.chrome.com/blog/prerender-pages/) instructs the browser to preemptively download and
render pages that users have yet to request, but are likely to visit. When
loaded on a prerendered page, the GPT library only requests
ads if and when the page is made visible.

## Load GPT statically

Avoid injecting the GPT library into your page dynamically or
loading it from an external script. Instead, load the library statically in the
`<head>` of your page as illustrated in
[Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started). This prevents other
resources from delaying the fetching and loading of the GPT
library, which in turn would delay the loading of ads.

For more details, see the Publisher Ads Audits for Lighthouse
[load ad scripts statically](https://developers.google.com/publisher-ads-audits/reference/audits/script-injected-tags) audit documentation.

## Load GPT asynchronously

Include the `async` keyword in your script tag definition, as illustrated in
[Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started). This instructs the
browser to load the GPT library in parallel with other
resources and page content, rather than blocking execution until the script is
done loading.

For more details, see the Publisher Ads Audits for Lighthouse
[load ad tag asynchronously](https://developers.google.com/publisher-ads-audits/reference/audits/async-ad-tags) audit documentation.

## Load GPT securely

Always load the GPT library over HTTPS, as illustrated in
[Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started). This not only
provides better security for your users, it also improves performance. Since ad
requests issued by GPT always use HTTPS, loading the library
itself using HTTPS ensures that the browser only needs to open 1 connection for
all requests related to ad serving.

For more details, see the Publisher Ads Audits for Lighthouse
[load ad tag over HTTPS](https://developers.google.com/publisher-ads-audits/reference/audits/loads-ad-tag-over-https) and
[load GPT from recommended host](https://developers.google.com/publisher-ads-audits/reference/audits/loads-gpt-from-sgdn)
audit documentation.

## Practice good page performance

While the best practices in this guide focus specifically on optimizing your
GPT integration, many other factors contribute to the overall
performance of your page. When making changes to your site (especially those
based on broad recommendations, such as the ones in this guide), it's important
to evaluate the impact of those changes on all aspects of your page's
performance. It's recommended that you regularly run tools like
[Lighthouse](https://developers.google.com/web/tools/lighthouse) and
[Publisher Ads Audits for Lighthouse](https://developers.google.com/publisher-ads-audits) to identify and address
performance issues, and find the right balance of optimizations for your site.