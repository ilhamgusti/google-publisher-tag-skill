---
type: Reference
title: "Ad event listeners"
description: "The Google Publisher Tag (GPT) library allows you to register and call"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Ad event listeners

# Ad event listeners

The Google Publisher Tag (GPT) library allows you to register and call
JavaScript functions when specific GPT-related ad events occur. This sample
provides a demonstration of using the GPT event framework to monitor and report
on the following events.

| Event | Fired when... |
|---|---|
| [ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent) | An impression becomes viewable. |
| [SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent) | A creative iframe fires its onload event. |
| [SlotRenderEndedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent) | Creative code has been injected into an ad slot. |
| [SlotRequestedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent) | An ad has been requested for the ad slot. |
| [SlotResponseReceivedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived) | An ad response has been received for the ad slot. |
| [SlotVisibilityChangedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent) | The on-screen percentage of the ad slot changes. |

