---
type: Reference
title: "Configure privacy settings"
description: "This example shows how to configure privacy settings for ad requests using the"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Configure privacy settings

This example shows how to configure privacy settings for ad requests using the
Google Publisher Tag (GPT) library. Learn more about available privacy settings
and [Publisher Privacy Treatments](https://support.google.com/admanager/answer/14323214) in the Google Ad Manager
help center.

- [Age treatment (TFAT)](https://support.google.com/admanager/answer/3671211)
- [Non-personalized ads (NPA)](https://support.google.com/admanager/answer/9005435)
- [Restricted data processing (RDP)](https://support.google.com/admanager/answer/9598414)

> [!IMPORTANT]
> **Important:** The tag for under age of consent (TFUA) and the tag for child-directed treatment (TFCD) are deprecated. Instead, use the Tag for age treatment (TFAT). You can mark your ad request using the TFAT setting to manage different age treatments for your ad requests. The TFAT "child" value is functionally equivalent to the TFCD or TFUA child treatment tags.

To learn about working with [Limited ads](https://support.google.com/admanager/answer/9882911) in GPT, see the
[Display a limited ad](https://developers.google.com/publisher-tag/samples/display-limited-ad) sample.

