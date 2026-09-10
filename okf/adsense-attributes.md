---
type: Reference
title: "AdSense Attributes in GPT"
description: "Reference for AdSense attributes configurable through Google Publisher Tag."
resource: "https://developers.google.com/publisher-tag/adsense-attributes"
tags: [gpt, adsense, attributes, reference]
timestamp: 2026-09-10T00:00:00Z
---

# AdSense Attributes

The table below lists the attributes that can be set with the
`
https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_set`
or
`https://developers.google.com/publisher-tag/reference#googletag.Slot_set`
methods. These AdSense attributes are typically set when creating or editing ad slots in
Google Ad Manager. These methods allow the publisher to override these server-side settings
on a per-request basis.

| **New attribute** | **Legacy attribute** | **Example** | **Allowed values** |
|---|---|---|---|
| `adsense_channel_ids` | `google_ad_channel` | `271828183+314159265` | Valid AdSense channel IDs, separated by '+' |
| `adsense_ad_types` | `google_ad_type` | `text_image` | `text, image, text_image` |
| `adsense_ad_format` | `google_ad_format` | `250x250_as` | `468x60_as, 234x60_as, 125x125_as, 120x600_as, 160x600_as, 180x150_as, 120x240_as, 200x200_as, 250x250_as, 300x250_as, 336x280_as, 728x90_as` |
| `adsense_background_color` | `google_color_bg` | `#000000` | hexadecimal colors |
| `adsense_border_color` | `google_color_border` | `#000000` | Hexadecimal colors |
| `adsense_link_color` | `google_color_link` | `#000000` | Hexadecimal colors |
| `adsense_test_mode` | `N/A` | `on` | `on` Set `on` to indicate the tag is used for testing and should not be included in counting or billing. Omit this setting for production, non-test traffic. |
| `adsense_text_color` | `google_color_text` | `#000000` | Hexadecimal colors |
| `adsense_url_color` | `google_color_url` | `#000000` | Hexadecimal colors |
| `adsense_ui_features` | `google_ui_features` | `rc:10` | `rc:10` for very rounded corners, `rc:6` for slightly rounded corners, `rc:0` for square corners (default) |
| `document_language` | `N/A` | `en` | A valid [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| `page_url` | `N/A` | `www.mysite.com` | Valid URLs |