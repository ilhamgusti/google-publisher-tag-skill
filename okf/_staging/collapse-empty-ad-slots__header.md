---
type: Reference
title: "Collapse empty ad slots"
description: "By default, ad slots which are not filled are left visible, which may result in"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Collapse empty ad slots

# Collapse empty ad slots

By default, ad slots which are not filled are left visible, which may result in
blank space on your page. If you know ahead of time that one or more ad slots on
your page are unlikely to get filled, you can instruct the Google Publisher Tag
(GPT) library to collapse them.

> [!CAUTION]
> **Caution:** Incorrect use of this feature can cause additional reflow of the content of your page.

The optimal configuration of this feature will depend on how often you expect ad
slots to be filled:

1. If slots will be filled most of the time, use [`collapseDiv: 'ON_NO_FILL'`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv). In this configuration, ad slots are expanded by default and collapse only if they cannot be filled.
2. If slots will not be filled most of the time, use [`collapseDiv: 'BEFORE_FETCH'`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv). In this configuration, ad slots are collapsed by default and only expand if they can be filled.

Because `googletag` API calls have no effect until GPT begins to run, to
minimize reflow you will also need to configure the CSS on your page so that
slots which are collapsed by default have zero dimensions.

It's also possible to configure per-slot overrides, as shown in the example
below, if specific slots on your page are more or less likely to be filled.

