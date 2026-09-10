---
type: Reference
title: "Offerwall with custom choice"
description: "This example demonstrates how to display an Offerwall on your website and"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Offerwall with custom choice

# Display an Offerwall with Custom Choice

This example demonstrates how to display an Offerwall on your website and
present a custom choice to users. Learn more about Offerwall in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/13860694).

Adding a custom choice lets you implement your own monetization solution
as an additional user selectable option within your Offerwall. For example, you
might let visitors purchase a subscription to access more content. For more
information about custom choice, see
[Set up a "custom choice" user choice](https://support.google.com/admanager/answer/13566866).

## Usage notes

- You must write and deploy your own implementation of the [Offerwall Custom Choice API](https://developers.google.com/funding-choices/offerwall-custom-choice-docs) to use the custom choice feature. Enabling custom choice without a correct implementation will result in Offerwall not displaying to end users.
- The location and text of your custom choice is previewable in the [message builder in Privacy \& messaging](https://support.google.com/admanager/answer/11897778). However, you can't preview the custom UI that displays after users select your custom choice from Google Ad Manager. Your custom code defines the look and behavior of the UI.
- You can only add one custom choice to an Offerwall.

