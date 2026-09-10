---
type: Sample
title: "GPT React / Next.js Integration"
description: "Guide and sample for integrating GPT into React and Next.js applications."
resource: "https://developers.google.com/publisher-tag/samples/react"
tags: [gpt, sample, react]
timestamp: 2026-09-10T00:00:00Z
---

# GPT and React

This sample showcases a basic single-page application (SPA) implementation
utilizing Google Publisher Tag (GPT), [React](https://react.dev/), and [Next.js](https://nextjs.org/).

Some important points to be aware of when working with GPT in SPAs:

1. Ensure that GPT is only loaded once.
2. Use [`disableInitialLoad()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_disableInitialLoad) and [`refresh()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_refresh) to control when ad requests are made. See [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading) for details.
3. Use [`setTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_setTargeting) and [`clearTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_clearTargeting) to control the targeting applied to ad slots. See [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting) for details.
4. Use [`destroySlots()`](https://developers.google.com/publisher-tag/reference#googletag.destroySlots) to clean up ad slots that are no longer needed (for example, when ad slot containers are removed due to a component being unloaded).

> [!NOTE]
> **Note:** If you encounter any issues with the following embedded sample, try opening the [sample](https://stackblitz.com/edit/gpt-react) in a new window. If the problem persists, click **Report an issue**.

## Sample implementation

<iframe loading="lazy" src="https://stackblitz.com/edit/gpt-react?embed=1&amp;file=pages%2Findex.js,pages%2Fsamples%2F%5Bid%5D.js,components%2Fgoogle-publisher-tag.js" style="height: 800px; width: 100%"> </iframe> [Report an issue](https://github.com/googleads/google-publisher-tag-samples/issues/new?labels=documentation&template=sample-feedback.md&title=Sample+feedback:+integrations/react)