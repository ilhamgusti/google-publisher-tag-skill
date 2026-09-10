---
type: Reference
title: "Display a rewarded ad"
description: "This example demonstrates using the Google Publisher Tag (GPT) library to"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Display a rewarded ad

# Display a rewarded ad

This example demonstrates using the Google Publisher Tag (GPT) library to
request and render a rewarded ad. Rewarded ad formats let app and web users
receive rewards for viewing ads. Learn more about rewarded ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/9116812).

You can use the following GPT events to display and interact with rewarded ads:

| Event | Fired when... |
|---|---|
| [RewardedSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotclosedevent) | A rewarded ad slot has been closed. |
| [RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotgrantedevent) | A reward has been granted for viewing an ad. |
| [RewardedSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotreadyevent) | A rewarded ad slot is ready to be displayed. |
| [RewardedSlotVideoCompletedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotvideocompletedevent) | A rewarded ad slot has finsihed playing a video. |

For the purpose of this example, a simple modal dialog is used to both prompt
the user to view the rewarded ad and to display the reward upon completion. In
practice, it is the responsibility of the publisher to implement their own
interface to accomplish these tasks.

> [!IMPORTANT]
> **Important:** Before you display a rewarded ad, you must comply with the [policies for ad units that offer rewards](https://support.google.com/admanager/answer/7496282) and obtain user consent.

## Usage notes

- **To ensure an optimal user experience, rewarded ads are only requested on
  pages that properly support the format.** Because of this,
  `defineOutOfPageSlot()` may return `null`; you should check for this case to
  ensure you're not doing any unnecessary work. Currently, rewarded ads are
  only supported on mobile optimized pages where zoom is neutral. Typically
  this means the publisher has `<meta name="viewport"
  content="width=device-width, initial-scale=1">` or similar in the `<head>`
  of the page.

- **Rewarded ads generate their own ad slot.** Unlike other ad types, it's not
  necessary to define a `<div>` for rewarded ads. Rewarded ads automatically
  create and insert their own container into the page when an ad fills.

