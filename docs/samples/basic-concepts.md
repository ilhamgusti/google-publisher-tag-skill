# GPT basic concepts

# GPT basic concepts

This sample builds on the [Display a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad) sample,
introducing more basic GPT concepts. These concepts include:

- [Ad sizes](https://developers.google.com/publisher-tag/guides/ad-sizes)
- [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)
- [Single Request Architecture](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly)

[Learn the basics](https://developers.google.com/publisher-tag/guides/learn-basics) of how this
sample works.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/basic-concepts/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/basic-concepts/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/basic-concepts](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/basic-concepts)

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
    <meta name="description" content="Learn GPT basic concepts by example." />
    <title>GPT basic concepts</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Define a fixed size ad slot, customized with key-value targeting.
        googletag
          .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              color: "red",
              position: "atf",
            },
          });

        // Define an anchor ad slot that sticks to the bottom of the viewport.
        const anchorSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel",
          googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
        );

        // The slot will be null if the page or device does not support anchors.
        if (anchorSlot) {
          anchorSlot.setTargeting("test", "anchor").addService(googletag.pubads());

          document.getElementById("status").textContent =
            "Anchor ad is initialized. Scroll page to activate.";
        }

        // Define a fluid ad slot that fills the width of the enclosing column and
        // adjusts the height as defined by the native creative delivered.
        googletag
          .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
          .addService(googletag.pubads());

        // Configure page-level targeting and enable SRA.
        googletag.setConfig({
          targeting: {
            interests: "basketball",
          },
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
      }

      .native-slot {
        width: 33%;
      }

      .page-content {
        height: 900vh;
      }

      .spacer {
        height: 450vh;
      }
    </style>
  </head>
  <body>
    <div class="page-content centered">
      <div id="banner-ad" style="width: 728px; height: 90px"></div>
      <!--
      If the following status is displayed when the page is rendered, try
      loading the page in a new window or on a different device.
    -->
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <!--
      Spacer used for example purposes only. This positions the native ad
      container below the fold to encourage scrolling.
    -->
      <div class="spacer"></div>
      <div id="native-ad" class="native-slot"></div>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Request and render all previously defined ad slots.
        googletag.display("banner-ad");
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
    <meta name="description" content="Learn GPT basic concepts by example." />
    <title>GPT basic concepts</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Define a fixed size ad slot, customized with key-value targeting.
        googletag
          .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              color: "red",
              position: "atf",
            },
          });

        // Define an anchor ad slot that sticks to the bottom of the viewport.
        var anchorSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel",
          googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
        );

        // The slot will be null if the page or device does not support anchors.
        if (anchorSlot) {
          anchorSlot.setTargeting("test", "anchor").addService(googletag.pubads());

          document.getElementById("status").textContent =
            "Anchor ad is initialized. Scroll page to activate.";
        }

        // Define a fluid ad slot that fills the width of the enclosing column and
        // adjusts the height as defined by the native creative delivered.
        googletag
          .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
          .addService(googletag.pubads());

        // Configure page-level targeting and enable SRA.
        googletag.setConfig({
          targeting: {
            interests: "basketball",
          },
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
      }

      .native-slot {
        width: 33%;
      }

      .page-content {
        height: 900vh;
      }

      .spacer {
        height: 450vh;
      }
    </style>
  </head>
  <body>
    <div class="page-content centered">
      <div id="banner-ad" style="width: 728px; height: 90px"></div>
      <!--
      If the following status is displayed when the page is rendered, try
      loading the page in a new window or on a different device.
    -->
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <!--
      Spacer used for example purposes only. This positions the native ad
      container below the fold to encourage scrolling.
    -->
      <div class="spacer"></div>
      <div id="native-ad" class="native-slot"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("banner-ad");
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
    <meta name="description" content="Learn GPT basic concepts by example." />
    <title>GPT basic concepts</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
      }

      .native-slot {
        width: 33%;
      }

      .page-content {
        height: 900vh;
      }

      .spacer {
        height: 450vh;
      }
    </style>
  </head>
  <body>
    <div class="page-content centered">
      <div id="banner-ad" style="width: 728px; height: 90px"></div>
      <!--
      If the following status is displayed when the page is rendered, try
      loading the page in a new window or on a different device.
    -->
      <h1 id="status">Anchor ads are not supported on this page.</h1>
      <!--
      Spacer used for example purposes only. This positions the native ad
      container below the fold to encourage scrolling.
    -->
      <div class="spacer"></div>
      <div id="native-ad" class="native-slot"></div>
    </div>
  </body>
</html>
```

`ts/sample.ts`:


```typescript
/**
 * @license
 * Copyright 2023 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

// Using @types/google-publisher-tag
// https://www.npmjs.com/package/@types/google-publisher-tag

window.googletag = window.googletag || { cmd: [] };

googletag.cmd.push(() => {
  // Define a fixed size ad slot, customized with key-value targeting.
  googletag
    .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad")!
    .addService(googletag.pubads())
    .setConfig({
      targeting: {
        color: "red",
        position: "atf",
      },
    });

  // Define an anchor ad slot that sticks to the bottom of the viewport.
  const anchorSlot = googletag.defineOutOfPageSlot(
    "/6355419/Travel",
    googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
  );

  // The slot will be null if the page or device does not support anchors.
  if (anchorSlot) {
    anchorSlot.setTargeting("test", "anchor").addService(googletag.pubads());

    document.getElementById("status")!.textContent =
      "Anchor ad is initialized. Scroll page to activate.";
  }

  // Define a fluid ad slot that fills the width of the enclosing column and
  // adjusts the height as defined by the native creative delivered.
  googletag.defineSlot("/6355419/Travel", ["fluid"], "native-ad")!.addService(googletag.pubads());

  // Configure page-level targeting and enable SRA.
  googletag.setConfig({
    targeting: {
      interests: "basketball",
    },
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Request and render all previously defined ad slots.
  googletag.display("banner-ad");
});
```
