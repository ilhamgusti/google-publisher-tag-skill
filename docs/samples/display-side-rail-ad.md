# Display a side rail ad

# Display a side rail ad

This example displays side rail ads using the Google Publisher Tag (GPT)
library. Learn more about side rail ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/10452255).

## Preview side rail ads

You can display a demo side rail ad on any page that shows ads with GPT by
adding `#gamLeftSideRailDemo` or `#gamRightSideRailDemo` to the URL. For
example, `https://www.example.com/#gamLeftSideRailDemo`.

This can be used to preview side rail ads on your site with no code changes
required. This is especially useful to quickly validate how side rails will
look and behave on different devices and in different operating environments.

## Usage notes

- **To ensure an optimal user experience, side rail ads are only requested on
  pages that properly support the format.** Because of this,
  `defineOutOfPageSlot()` might return null. Check for this case to
  ensure you're not doing unnecessary work. Side rail ads are
  supported when the following conditions are met:

  - GPT is running in the top window.
  - Viewport dimensions are at least `1200x650` pixels.
- **Only request side rail ads on pages and environments where you want a side
  rail ad to appear.** Side rail ads are eligible to serve to all devices.

- **Side rail ads generate their own ad container.** You don't need a
  `<div>` for side rail ads. Side rail ads
  automatically create and insert their own container into the page when an ad
  fills. These containers are positioned as close as possible to the main
  page content.

- **Side rail ads are optimized to fit the space available.** Side rail ads
  require a minimum of `120x500` pixels of empty space to the left or right
  of the main page content to display. Once displayed, if the page is resized
  causing the empty space to fall below this minimum, the slot is temporarily
  hidden until space becomes available again.

- **If using single-request architecture (SRA) on a page with multiple slots,
  don't call `display()` until static ad slots divs are created.** As
  explained in [Ad Best Practices](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly), the first call to `display()`
  requests every ad slot defined prior to that point. Although side rail ad
  slots don't require a predefined `<div>`, static ad slots do. Calling
  `display()` before these elements are present on the page can result in
  lower quality signals, reducing monetization. Because of this, we recommend
  delaying the initial call until after the static slots are defined.

- **Only refresh visible side rail ads.** When an side rail ad slot
  is collapsed or not visible, all calls to `refresh()` are ignored. If you're
  using `googletag.setConfig({ disableInitialLoad: true })` to manually
  [control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading), the first call
  to `refresh()` will trigger an ad request regardless of the slot visibility.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-side-rail-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-side-rail-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-side-rail-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-side-rail-ad)

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
    <meta name="description" content="Display a GPT-managed side rail ad." />
    <title>Display a side rail ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let leftSideRail;
      let rightSideRail;

      googletag.cmd.push(() => {
        // Define left and right side rail ad slots.
        leftSideRail = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe",
          googletag.enums.OutOfPageFormat.LEFT_SIDE_RAIL,
        );
        rightSideRail = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe",
          googletag.enums.OutOfPageFormat.RIGHT_SIDE_RAIL,
        );

        // Side rail slots return null if the page or device does not support
        // side rails.
        if (leftSideRail) leftSideRail.addService(googletag.pubads());
        if (rightSideRail) rightSideRail.addService(googletag.pubads());

        if (leftSideRail && rightSideRail) {
          document.getElementById("status").textContent = "Side rail ads are initialized.";
        } else if (leftSideRail || rightSideRail) {
          document.getElementById("status").textContent =
            `${leftSideRail ? "Left" : "Right"} side rail ad is initialized.`;
        } else {
          document.getElementById("status").textContent =
            "Side rail ads are not supported on this page.";
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
    <style>
      .content-area {
        height: 100vh;
        width: calc(100% - 400px);
        margin: auto;
      }
    </style>
  </head>
  <body>
    <div id="page-content" class="content-area">
      <h1 id="status">Side rail ads are initializing.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        if (leftSideRail || rightSideRail) {
          googletag.display(leftSideRail || rightSideRail);
        }
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
    <meta name="description" content="Display a GPT-managed side rail ad." />
    <title>Display a side rail ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var leftSideRail;
      var rightSideRail;

      googletag.cmd.push(function () {
        // Define left and right side rail ad slots.
        leftSideRail = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe",
          googletag.enums.OutOfPageFormat.LEFT_SIDE_RAIL,
        );
        rightSideRail = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe",
          googletag.enums.OutOfPageFormat.RIGHT_SIDE_RAIL,
        );

        // Side rail slots return null if the page or device does not support
        // side rails.
        if (leftSideRail) leftSideRail.addService(googletag.pubads());
        if (rightSideRail) rightSideRail.addService(googletag.pubads());

        if (leftSideRail && rightSideRail) {
          document.getElementById("status").textContent = "Side rail ads are initialized.";
        } else if (leftSideRail || rightSideRail) {
          document.getElementById("status").textContent = "".concat(
            leftSideRail ? "Left" : "Right",
            " side rail ad is initialized.",
          );
        } else {
          document.getElementById("status").textContent =
            "Side rail ads are not supported on this page.";
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
    <style>
      .content-area {
        height: 100vh;
        width: calc(100% - 400px);
        margin: auto;
      }
    </style>
  </head>
  <body>
    <div id="page-content" class="content-area">
      <h1 id="status">Side rail ads are initializing.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        if (leftSideRail || rightSideRail) {
          googletag.display(leftSideRail || rightSideRail);
        }
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
    <meta name="description" content="Display a GPT-managed side rail ad." />
    <title>Display a side rail ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .content-area {
        height: 100vh;
        width: calc(100% - 400px);
        margin: auto;
      }
    </style>
  </head>
  <body>
    <div id="page-content" class="content-area">
      <h1 id="status">Side rail ads are initializing.</h1>
      <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    </div>
  </body>
</html>
```

`ts/sample.ts`:


```typescript
/**
 * @license
 * Copyright 2024 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

// Using @types/google-publisher-tag
// https://www.npmjs.com/package/@types/google-publisher-tag

window.googletag = window.googletag || { cmd: [] };

let leftSideRail: googletag.Slot | null;
let rightSideRail: googletag.Slot | null;

googletag.cmd.push(() => {
  // Define left and right side rail ad slots.
  leftSideRail = googletag.defineOutOfPageSlot(
    "/6355419/Travel/Europe",
    googletag.enums.OutOfPageFormat.LEFT_SIDE_RAIL,
  );
  rightSideRail = googletag.defineOutOfPageSlot(
    "/6355419/Travel/Europe",
    googletag.enums.OutOfPageFormat.RIGHT_SIDE_RAIL,
  );

  // Side rail slots return null if the page or device does not support
  // side rails.
  if (leftSideRail) leftSideRail.addService(googletag.pubads());
  if (rightSideRail) rightSideRail.addService(googletag.pubads());

  if (leftSideRail && rightSideRail) {
    document.getElementById("status")!.textContent = "Side rail ads are initialized.";
  } else if (leftSideRail || rightSideRail) {
    document.getElementById("status")!.textContent =
      `${leftSideRail ? "Left" : "Right"} side rail ad is initialized.`;
  } else {
    document.getElementById("status")!.textContent =
      "Side rail ads are not supported on this page.";
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
  if (leftSideRail || rightSideRail) {
    googletag.display((leftSideRail || rightSideRail)!);
  }
});
```
