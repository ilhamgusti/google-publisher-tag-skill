---
type: Reference
title: "Display a limited ad"
description: "This is an example of using the Google Publisher Tag (GPT) library to request"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Display a limited ad

# Display a limited ad

This is an example of using the Google Publisher Tag (GPT) library to request
and render a limited ad. Limited ads provide publishers a way to serve ads in
the absence of consent for the use of cookies or other local identifiers. Learn
more about the features and limitations of limited ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/9882911).

You can instruct GPT to request limited ads in
[two different ways](https://support.google.com/admanager/answer/9882911#implementation):

- Automatically, by using a signal from an [IAB TCF v2.0](https://iabeurope.eu/tcf-2-0/) consent management platform (CMP).
- Manually, by using the [GPT `PrivacySettings` API](https://developers.google.com/publisher-tag/reference#googletag.privacysettingsconfig).

> [!IMPORTANT]
> **Important:** it is not necessary to manually enable limited ads when a CMP is in use.

In order to manually control limited ads, you must load GPT from the
[limited ads URL](https://developers.google.com/publisher-tag/guides/general-best-practices#load_from_an_official_source). The version of GPT served from
this URL contains additional safeguards against accessing client-side storage by
default. To accomplish this, certain library operations are delayed until after
the first call to `display()`, leading to a slight decrease in performance
compared to the standard version of GPT.

You can't manually control limited ads on a per-request basis when GPT is loaded
from the standard URL. When you load GPT from the standard URL, all calls to
`setPrivacySettings({ limitedAds: ... })` are ignored and the library may
attempt to access client-side storage at any time. This allows GPT to more
effectively optimize the order of library operations. For example, GPT can
perform [secure signal](https://support.google.com/admanager/answer/10488752) collection earlier,
increasing the likelihood that gathered signals will be included in every ad
request.

