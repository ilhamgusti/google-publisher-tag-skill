---
type: Troubleshooting
title: "Google Publisher Console"
description: "Debugging ad delivery and performance issues using Google Publisher Console."
resource: "https://developers.google.com/publisher-tag/guides/publisher-console"
tags: [gpt, debugging, console, troubleshooting]
timestamp: 2026-09-10T00:00:00Z
---

You can use the Google Publisher Console to inspect ad delivery on pages that
use the [Google Publisher Tag (GPT) library](https://support.google.com/admanager/answer/181073). You can use
this feature to troubleshoot ad loading issues and optimize the performance of
your page.

This guide explains how to access and use the Publisher Console. For details on
specific messages, see the full list of
[Publisher Console messages](https://developers.google.com/publisher-tag/guides/publisher-console-messages).

If you need more help with GPT, see the [support
options](https://developers.google.com/publisher-tag/support/feedback-questions).

## Access the console

You can access the Publisher Console from your browser on any page that uses
GPT. There are three ways to access the Publisher Console:

JavaScript console
:   From the JavaScript console in your browser's developer tools, run:
    `js
    googletag.openConsole()`

JavaScript bookmark

:   Create a new bookmark for the Publisher Console by dragging the following
    button to your bookmarks bar:

    <iframe src="https://developers.devsite.google/frame/publisher-tag/guides/publisher-console_22dac39ec776ddefd0d238ccbcca9806e591559b0cc80d884d667b6d92f246ed.frame" class="framebox inherit-locale " allow="clipboard-write https://developers.devsite.google" allowfullscreen is-upgraded></iframe>

:   You can then click the bookmark from any page that includes
    GPT to load the Publisher Console.

URL query parameters

:   Add `?google_console=1` to the end of the URL of any page that includes
    GPT. For example, `http://www.example.com?google_console=1`

    > [!NOTE]
    > **Note:** URL query parameters do not work for all pages.

After accessing the Publisher Console on a page, you can use the keyboard
shortcut **Ctrl+F10** (or **fn+control+F10** on a Mac) to show or hide it.

## Use the console

The Publisher Console has three tabs: **Ad Slots** , **Page Request** , and
**Configuration** . A button to troubleshoot delivery
issues with [Ad Manager Delivery Tools](https://support.google.com/admanager/answer/7449957) is
also provided.

### Ad overlays

The publisher console adds an overlay to every ad slot registered with
GPT. Each overlay contains information about the ad currently
loaded in that slot, and a link to view detailed delivery data in
[Ad Manager Delivery Tools](https://support.google.com/admanager/answer/7449957).
![Publisher console ad overlay screenshot](https://developers.google.com/static/publisher-tag/images/pub-console/ad-overlay.png)


| # | Field | Description |
|---|---|---|
| 1 | Ad source | The [source](https://support.google.com/admanager/answer/9248464) of the returned ad. Possible values: - **Direct Sold**: Reserved Inventory. - **Dynamic Allocation Sold**: Non-reserved inventory. - **Empty**: The ad slot has not been filled by GPT. |
| 2 | Ad unit path | The path to the ad unit, including the parent ad unit path. The name of the displayed ad unit appears on the line below the parent path. |
| 3 | Ad container | The ID of the `<div>` element the ad has been rendered into. |
| 4 | Creative | The ID of the Ad Manager creative that was returned. Clicking on this value will open the creative in Ad Manager. |
| 5 | Line Item | The ID of the Ad Manager line item to which the returned creative is associated. Clicking on this value will open the line item in Ad Manager. |

<br />

### Ad Slots tab

The ad slots tab contains detailed information about every ad slot currently
registered with GPT. Information is organized into cards, with
one card displayed per ad slot. Links to view the ad unit, creative, and
delivery diagnostics for the returned ad in Ad Manager are also
provided.
![Publisher console ad slots tab screenshot](https://developers.google.com/static/publisher-tag/images/pub-console/ad-slots-tab.png)


| # | Field | Description |
|---|---|---|
| 1 | Ad unit path | The path to the ad unit, including the parent ad unit path. The name of the displayed ad unit appears on the line below the parent path. |
| 2 | Div | The ID of the `<div>` element the ad has been rendered into. |
| 3 | Slot size | The size of the ad slot (pixel width x pixel height), as specified in the ad tag definition. For more information on slot sizes, see [Supported ad sizes](https://support.google.com/admanager/answer/1100453). |
| 4 | Out of Page | Indicates whether the ad unit displays an out of-the-page creative, such as for pop-up, pop-under, or floating ads. For more information, see [Serve out-of-page creatives](https://support.google.com/admanager/answer/6088046). Possible values: - **True** - **False** |
| 5 | Service | The [service](https://developers.google.com/publisher-tag/reference#googletag.service) used to serve the ad. GPT only supports Ad Manager. |
| 6 | Overlay status | Indicates whether the ad slot has an associated Publisher Console overlay. Ad slots that do not have overlays may not be included in the DOM or may be out-of-page slots. Possible values: - **Displayed** - **Not Displayed** |
| 7 | ms to fetch | The amount of time, in milliseconds, that it took to fetch the ad from Ad Manager. |
| 8 | Ad fetch count | The number of times the ad was fetched since the page was opened, including ad refreshes. |
| 9 | Iframe type | The type of Iframe within the creative was rendered. For more information on IFrame types, see [Render creatives using SafeFrame](https://support.google.com/admanager/answer/6023110). Possible values: - **FriendlyIframe** - **SafeFrame** |
| 10 | Line Item ID | The ID of the Ad Manager line item to which the returned creative is associated. |
| 11 | Creative ID | The ID of the Ad Manager creative that was returned. |
| 12 | Query ID | The ID of the query that returned this ad unit. Your Technical Account Manager (TAM) can use this ID to troubleshoot issues with the displayed creative. |
| 13 | Targeting info | An expandable section which lists the effective page- and slot-level [key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting) applied to the ad slot. |

<br />

### Page Request tab

The page request tab provides general information about the page and the
environment in which it is rendered, warnings encountered, and a timeline of
ad events.
![Publisher console page request tab screenshot](https://developers.google.com/static/publisher-tag/images/pub-console/page-request-tab.png)


| # | Field | Description |
|---|---|---|
| 1 | URL | The URL of the current page. |
| 2 | Browser | The user agent string of the browser used to load the page. |
| 3 | Browser viewport width and height | The current browser viewport dimensions (pixel width x pixel height). |
| 4 | Property Code | The network code, which is a unique, numeric identifier for the Ad Manager network that the ad unit belongs to. For more information, see [Find Ad Manager account information](https://support.google.com/admanager/answer/7674889#network-code). |
| 5 | ms to fetch ads | The amount of time, in milliseconds, that it took to fetch all of the GPT ads on the page from Ad Manager. |
| 6 | ms to render ads | The amount of time, in milliseconds, that it took to render all of the GPT ads on the page, after the creatives were returned from Ad Manager. |

<br />

#### Timeline

The **Timeline** section of the **Page Request** tab lists a chronological
sequence of events for each GPT ad displayed on the page, from
creating the ad slot to rendering the ad. The timeline also includes any
warnings or errors returned while requesting or displaying the ad.

### Configuration tab

The configuration tab displays the Google Ad Manager network-level settings
affecting ad delivery on the page.
![Publisher console configuration tab screenshot](https://developers.google.com/static/publisher-tag/images/pub-console/configuration-tab.png)

#### Ad Manager configuration

The Ad Manager configuration section identifies the primary Google Ad Manager
network associated with the page (when known) and any active experiments.


| # | Field | Description |
|---|---|---|
| 1 | Provided domain URL | The URL of the domain provided for the page-level Ad Manager configuration. |
| 2 | Provided network code | The network code provided for the page-level Ad Manager configuration. |
| 3 | Experiments | The number of active experiments running on the page, grouped by type (such as ad slot, ad rule, header bidding, or ad intents). For more information, see the [Run a manual experiment](https://support.google.com/admanager/answer/9799933) help center article. |

<br />

#### Network-level configuration

The network-level configuration section displays the effective settings for each
Google Ad Manager network referenced on the page.


| # | Field | Description |
|---|---|---|
| 4 | Network code | The network code of the associated Ad Manager network. For more information, see the [Locate your Network code and account IDs](https://support.google.com/admanager/answer/7674889) help center article. |
| 5 | Header bidding trafficking | Indicates whether header bidding trafficking is enabled. For more information, see the [Header bidding trafficking with the Prebid wrapper](https://support.google.com/admanager/answer/12273163) help center article. Possible values: - **Enabled** |
| 6 | Privacy \& messaging | Indicates whether the network is eligible for privacy and messaging scripts. For more information, see the [About Privacy \& messaging](https://support.google.com/admanager/answer/10075997) help center article. Possible values: - **Eligible** |
| 7 | Site status | The status of the site within Ad Manager. For more information, see the [Check your site status and fix issues](https://support.google.com/admanager/answer/10134384) help center article. Possible values: - **Approved** |
| 8 | Secure signals providers | A list of secure signals providers registered on the page. For more information, see the [Secure signals providers](https://support.google.com/admanager/answer/14750072) help center article. |

<br />