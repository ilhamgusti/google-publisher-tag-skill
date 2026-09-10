---
type: Support
title: "Browser Support Matrix"
description: "Supported browsers, environments, and compatibility requirements for GPT."
resource: "https://developers.google.com/publisher-tag/support/browser-support"
tags: [gpt, support, browsers, compatibility]
timestamp: 2026-09-10T00:00:00Z
---

# Browser support

The Google Publisher Tag (GPT) library supports the following
browsers and environments:

| Browser | Desktop | Mobile |
|---|---|---|
| [Apple Safari](https://www.apple.com/safari/download) | Yes | Yes |
| [Google Chrome](https://www.google.com/chrome) | Yes | Yes |
| [Microsoft Edge](https://www.microsoft.com/edge) | Yes |   |
| [Mozilla Firefox](https://www.mozilla.org/firefox/) | Yes |   |

All of the browsers that GPT supports release regularly and
update automatically. Due to this, we don't maintain a comprehensive list of
supported browser versions. Instead, we validate GPT against
the latest version of each browser, and commit to providing support for all
versions that are officially supported by the respective browser vendors.

## Unsupported browsers

The GPT library makes a best-effort attempt to serve ads to
any browser that loads it. This means that GPT works on
most browsers built to modern Web standards. However, browsers not expressly
listed in the preceding section are considered unsupported.

GPT hasn't been validated against unsupported browsers, and
they may lack features GPT needs to operate. In general,
GPT doesn't try to detect unsupported browsers or alter its
behavior to support them. If you use GPT with unsupported
browsers, you may encounter unexpected behavior like the following:

- Console errors originating from the GPT library.
- Functions registered with the [GPT CommandArray](https://developers.google.com/publisher-tag/reference#googletag.commandarray) not executing.
- Ads not appearing or rendering incorrectly.
- Impressions and clicks not being counted.

> [!CAUTION]
> **Caution:** We don't commit to addressing any issues encountered when using GPT on unsupported browsers.