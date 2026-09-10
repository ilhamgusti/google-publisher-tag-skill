---
type: Sample
title: "Display Out-of-Page Ad"
description: "Sample demonstrating generic out-of-page ad unit definition."
resource: "https://developers.google.com/publisher-tag/samples/display-out-of-page-ad"
tags: [gpt, sample, display out of page ad]
timestamp: 2026-09-10T00:00:00Z
---

# Display an out-of-page ad

# Display an out-of-page ad

This example displays an out-of-page ad using the Google Publisher Tag library.
Learn more about out-of-page ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/6088046).


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-out-of-page-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-out-of-page-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-out-of-page-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-out-of-page-ad)

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
    <meta name="description" content="Display a pop-up, pop-under, or floating ad." />
    <title>Display an out-of-page ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Use defineOutOfPageSlot instead of defineSlot when working with
        // out-of-page ads.
        googletag
          .defineOutOfPageSlot("/6355419/Travel", "out-of-page-ad")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              test: "outofpage",
            },
          });

        // Enable the PubAdsService.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="out-of-page-ad"></div>
    <script>
      googletag.cmd.push(() => {
        // Request and render an ad for the "out-of-page-ad" slot.
        googletag.display("out-of-page-ad");
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
    <meta name="description" content="Display a pop-up, pop-under, or floating ad." />
    <title>Display an out-of-page ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Use defineOutOfPageSlot instead of defineSlot when working with
        // out-of-page ads.
        googletag
          .defineOutOfPageSlot("/6355419/Travel", "out-of-page-ad")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              test: "outofpage",
            },
          });

        // Enable the PubAdsService.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="out-of-page-ad"></div>
    <script>
      googletag.cmd.push(function () {
        // Request and render an ad for the "out-of-page-ad" slot.
        googletag.display("out-of-page-ad");
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
    <meta name="description" content="Display a pop-up, pop-under, or floating ad." />
    <title>Display an out-of-page ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style></style>
  </head>
  <body>
    <div id="out-of-page-ad"></div>
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
  // Use defineOutOfPageSlot instead of defineSlot when working with
  // out-of-page ads.
  googletag
    .defineOutOfPageSlot("/6355419/Travel", "out-of-page-ad")!
    .addService(googletag.pubads())
    .setConfig({
      targeting: {
        test: "outofpage",
      },
    });

  // Enable the PubAdsService.
  googletag.enableServices();

  // Request and render an ad for the "out-of-page-ad" slot.
  googletag.display("out-of-page-ad");
});
```
