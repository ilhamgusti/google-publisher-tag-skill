---
type: Sample
title: "Display Anchor Ad"
description: "Sample implementing sticky top or bottom anchor ads for mobile and desktop."
resource: "https://developers.google.com/publisher-tag/samples/display-anchor-ad"
tags: [gpt, sample, display anchor ad]
timestamp: 2026-09-10T00:00:00Z
---

# Display an anchor ad

# Display an anchor ad

This example displays an anchor ad using the Google Publisher Tag (GPT) library.
Learn more about anchor ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/10452255).

## Preview anchor ads

You can display a demo anchor ad on any page that shows ads with GPT by adding
`#gamTopAnchorDemo` or `#gamBottomAnchorDemo` to the URL. For example,
`https://www.example.com/#gamTopAnchorDemo`.

This functionality can be used to preview anchor ads on your site with no code
changes required. This is especially useful to quickly validate how anchors will
look and behave on different devices and in different operating environments.

## Usage notes

- **To ensure an optimal user experience, anchor ads are only requested on
  pages that properly support the format.** Because of this,
  `defineOutOfPageSlot()` may return null; you should check for this case to
  ensure you're not doing any unnecessary work. Currently, anchor ads are
  supported if the following conditions are met:

  - GPT is running in the top window.
  - On a mobile optimized page where zoom is neutral; typically this means the publisher has `<meta name="viewport" content="width=device-width,
    initial-scale=1">` or similar in the `<head>` of the page.
  - Viewport is in a portrait orientation with a width between `320px` and `1000px`.
- **Only request anchor ads on pages/environments where you want an anchor to
  appear.** Anchor ads are eligible to serve to desktop, tablet, and mobile
  devices.

  > [!NOTE]
  > **Note:** You can use Chrome DevTools [mobile simulation](https://developers.google.com/web/tools/chrome-devtools/device-mode#viewport) to test anchor ads on mobile from a desktop environment.

- **Anchor ads generate their own ad container.** Unlike other ad types, it's
  not necessary to define a `<div>` for anchor ads. Anchor ads automatically
  create and insert their own container into the page when an ad fills. These
  containers may overlap or occlude other elements using absolute or fixed
  positioning, so it's recommended to avoid placing such elements in areas
  where anchors are meant to appear.

- **If using single-request architecture (SRA) on a page with multiple slots,
  don't call `display()` until static ad slots divs are created.** As
  explained in [Ad Best Practices](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly), the first call to `display()`
  requests every ad slot defined prior to that point. Although anchor ad slots
  do not require a predefined `<div>`, static ad slots do. Calling `display()`
  before these elements are present on the page can result in lower quality
  signals, reducing monetization. Because of this, we recommend delaying the
  initial call until after the static slots are defined.

- **Only visible anchor ads may be refreshed.** When an anchor ad slot is
  collapsed or not yet scrolled into view, all calls to `refresh()` are
  ignored. If you're using `googletag.setConfig({ disableInitialLoad: true })`
  to manually [control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading), however, the
  first call to `refresh()` will trigger an ad request regardless of the slot
  visibility.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-anchor-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-anchor-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-anchor-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-anchor-ad)

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
    <meta name="description" content="Display a GPT-managed anchor ad." />
    <title>Display an anchor ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let anchorSlot;

      googletag.cmd.push(() => {
        // Define an anchor ad slot at the top of the viewport.
        // Note: a single anchor ad slot may be defined per page, at either the
        // top or bottom of the viewport.
        //
        // Be aware that anchor ads are not limited to mobile devices. If you
        // serve the same code to both mobile and non-mobile users, it is
        // recommended to explicitly define when and where anchor ads should be
        // shown for each environment. Here we use a basic check of viewport
        // width to create a top anchor on mobile and a bottom anchor on
        // non-mobile devices.
        anchorSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel",
          document.body.clientWidth <= 500
            ? googletag.enums.OutOfPageFormat.TOP_ANCHOR
            : googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
        );

        // Anchor slots return null if the page or device does not support anchors.
        if (anchorSlot) {
          anchorSlot.addService(googletag.pubads()).setConfig({
            targeting: {
              test: "anchor",
            },
          });

          document.getElementById("status").innerText =
            "Anchor ad is initialized. Scroll page to activate.";
        }

        // Define static ad slots.
        googletag
          .defineSlot("/6355419/Travel/Europe", [100, 100], "static-ad-1")
          .addService(googletag.pubads());

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="page-content" style="height: 900vh">
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        googletag.display(anchorSlot);
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
    <meta name="description" content="Display a GPT-managed anchor ad." />
    <title>Display an anchor ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var anchorSlot;

      googletag.cmd.push(function () {
        // Define an anchor ad slot at the top of the viewport.
        // Note: a single anchor ad slot may be defined per page, at either the
        // top or bottom of the viewport.
        //
        // Be aware that anchor ads are not limited to mobile devices. If you
        // serve the same code to both mobile and non-mobile users, it is
        // recommended to explicitly define when and where anchor ads should be
        // shown for each environment. Here we use a basic check of viewport
        // width to create a top anchor on mobile and a bottom anchor on
        // non-mobile devices.
        anchorSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel",
          document.body.clientWidth <= 500
            ? googletag.enums.OutOfPageFormat.TOP_ANCHOR
            : googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
        );

        // Anchor slots return null if the page or device does not support anchors.
        if (anchorSlot) {
          anchorSlot.addService(googletag.pubads()).setConfig({
            targeting: {
              test: "anchor",
            },
          });

          document.getElementById("status").innerText =
            "Anchor ad is initialized. Scroll page to activate.";
        }

        // Define static ad slots.
        googletag
          .defineSlot("/6355419/Travel/Europe", [100, 100], "static-ad-1")
          .addService(googletag.pubads());

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="page-content" style="height: 900vh">
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        googletag.display(anchorSlot);
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
    <meta name="description" content="Display a GPT-managed anchor ad." />
    <title>Display an anchor ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style></style>
  </head>
  <body>
    <div id="page-content" style="height: 900vh">
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
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

let anchorSlot: googletag.Slot | null;

googletag.cmd.push(() => {
  // Define an anchor ad slot at the top of the viewport.
  // Note: a single anchor ad slot may be defined per page, at either the
  // top or bottom of the viewport.
  //
  // Be aware that anchor ads are not limited to mobile devices. If you
  // serve the same code to both mobile and non-mobile users, it is
  // recommended to explicitly define when and where anchor ads should be
  // shown for each environment. Here we use a basic check of viewport
  // width to create a top anchor on mobile and a bottom anchor on
  // non-mobile devices.
  anchorSlot = googletag.defineOutOfPageSlot(
    "/6355419/Travel",
    document.body.clientWidth <= 500
      ? googletag.enums.OutOfPageFormat.TOP_ANCHOR
      : googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
  );

  // Anchor slots return null if the page or device does not support anchors.
  if (anchorSlot) {
    anchorSlot.addService(googletag.pubads()).setConfig({
      targeting: {
        test: "anchor",
      },
    });

    document.getElementById("status")!.innerText =
      "Anchor ad is initialized. Scroll page to activate.";
  }

  // Define static ad slots.
  googletag
    .defineSlot("/6355419/Travel/Europe", [100, 100], "static-ad-1")!
    .addService(googletag.pubads());

  // Enable SRA.
  googletag.setConfig({
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Ensure the first call to display comes after static ad slot
  // divs are defined. If you do not have any static ad slots, this
  // call can be made immediately after services are enabled.
  googletag.display(anchorSlot!);
});
```
