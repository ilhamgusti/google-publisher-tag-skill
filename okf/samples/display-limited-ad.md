---
type: Sample
title: "Display Limited Ads"
description: "Sample implementing limited ads mode when cookie/personalization consent is absent."
resource: "https://developers.google.com/publisher-tag/samples/display-limited-ad"
tags: [gpt, sample, display limited ad]
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


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-limited-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-limited-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-limited-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-limited-ad)

### JavaScript

```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content="Display an ad in the absence of consent for the use of cookies or other local identifiers."
    />
    <title>Display a limited ad</title>
    <!---
     Load GPT from the limited ads URL to enable manual control of limited ads.
    --->
    <script async src="https://pagead2.googlesyndication.com/tag/js/gpt.js"></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Define an ad slot for div with id "banner-ad".
        googletag
          .defineSlot("/6355419/Travel", [728, 90], "banner-ad")
          .setTargeting("test", "privacy")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });

      let ltdEnabled = false;
      function toggleLimitedAds() {
        const button = this;

        // Set to true to enable, false to disable.
        ltdEnabled = !ltdEnabled;

        googletag.cmd.push(() => {
          googletag.pubads().setPrivacySettings({
            limitedAds: ltdEnabled,
          });

          // Refresh all ads on the page.
          googletag.pubads().refresh();

          button.setAttribute("data-enabled", ltdEnabled.toString());
        });
      }
    </script>
    <style>
      button::after {
        content: "OFF";
        color: red;
        font-weight: bold;
      }

      button[data-enabled="true"]::after {
        content: "ON";
        color: green;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <div id="banner-ad" style="width: 728px; height: 90px"></div>
    <div>
      <button id="ltdButton">Limited Ads</button>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render an ad for the "banner-ad" slot.
        googletag.display("banner-ad");

        // Register click event handlers.
        document.getElementById("ltdButton").addEventListener("click", toggleLimitedAds);
      });
    </script>
  </body>
</html>
```

### JavaScript (legacy)

```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content="Display an ad in the absence of consent for the use of cookies or other local identifiers."
    />
    <title>Display a limited ad</title>
    <!---
     Load GPT from the limited ads URL to enable manual control of limited ads.
    --->
    <script async src="https://pagead2.googlesyndication.com/tag/js/gpt.js"></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Define an ad slot for div with id "banner-ad".
        googletag
          .defineSlot("/6355419/Travel", [728, 90], "banner-ad")
          .setTargeting("test", "privacy")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });

      var ltdEnabled = false;
      function toggleLimitedAds() {
        var button = this;

        // Set to true to enable, false to disable.
        ltdEnabled = !ltdEnabled;

        googletag.cmd.push(function () {
          googletag.pubads().setPrivacySettings({
            limitedAds: ltdEnabled,
          });

          // Refresh all ads on the page.
          googletag.pubads().refresh();

          button.setAttribute("data-enabled", ltdEnabled.toString());
        });
      }
    </script>
    <style>
      button::after {
        content: "OFF";
        color: red;
        font-weight: bold;
      }

      button[data-enabled="true"]::after {
        content: "ON";
        color: green;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <div id="banner-ad" style="width: 728px; height: 90px"></div>
    <div>
      <button id="ltdButton">Limited Ads</button>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render an ad for the "banner-ad" slot.
        googletag.display("banner-ad");

        // Register click event handlers.
        document.getElementById("ltdButton").addEventListener("click", toggleLimitedAds);
      });
    </script>
  </body>
</html>
```

### TypeScript

`ts/index.html`:


```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content="Display an ad in the absence of consent for the use of cookies or other local identifiers."
    />
    <title>Display a limited ad</title>
    <!---
     Load GPT from the limited ads URL to enable manual control of limited ads.
    --->
    <script async src="https://pagead2.googlesyndication.com/tag/js/gpt.js"></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      button::after {
        content: "OFF";
        color: red;
        font-weight: bold;
      }

      button[data-enabled="true"]::after {
        content: "ON";
        color: green;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <div id="banner-ad" style="width: 728px; height: 90px"></div>
    <div>
      <button id="ltdButton">Limited Ads</button>
    </div>
  </body>
</html>
```

`ts/sample.ts`:


```typescript
/**
 * @license
 * Copyright 2022 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

// Using @types/google-publisher-tag
// https://www.npmjs.com/package/@types/google-publisher-tag

window.googletag = window.googletag || { cmd: [] };

googletag.cmd.push(() => {
  // Define an ad slot for div with id "banner-ad".
  googletag
    .defineSlot("/6355419/Travel", [728, 90], "banner-ad")!
    .setTargeting("test", "privacy")
    .addService(googletag.pubads());

  // Enable the PubAdsService.
  googletag.enableServices();

  // Request and render an ad for the "banner-ad" slot.
  googletag.display("banner-ad");
});

let ltdEnabled = false;
function toggleLimitedAds(this: HTMLButtonElement) {
  const button = this;

  // Set to true to enable, false to disable.
  ltdEnabled = !ltdEnabled;

  googletag.cmd.push(() => {
    googletag.pubads().setPrivacySettings({
      limitedAds: ltdEnabled,
    });

    // Refresh all ads on the page.
    googletag.pubads().refresh();

    button.setAttribute("data-enabled", ltdEnabled.toString());
  });
}

// Register click event handlers.
document.getElementById("ltdButton")!.addEventListener("click", toggleLimitedAds);
```
