---
type: Reference
title: "Lazy loading"
description: "Lazy loading enables pages to load faster, reduces resource consumption and"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Lazy loading

# Lazy loading

Lazy loading enables pages to load faster, reduces resource consumption and
contention, and improves viewability rate by pausing the requesting and
rendering of ads until they approach the user's viewport.

With lazy loading in SRA, when the first ad slot comes within the viewport
specified by the [`fetchMarginPercent`](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.fetchMarginPercent) property,
the call for that ad and all other ad slots is made.

