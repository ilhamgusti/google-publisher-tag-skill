---
type: Sample
title: "Ad Sizes Sample"
description: "Sample implementation using sizeMapping to support responsive ad slots."
resource: "https://developers.google.com/publisher-tag/samples/ad-sizes"
tags: [gpt, sample, ad sizes]
timestamp: 2026-09-10T00:00:00Z
---

# Ad sizes

# Ad sizes

This example demonstrates various ways of specifying which ad sizes are eligible
to serve to an ad slot using the Google Publisher Tag library. Learn more about
the available options in the [ad sizes guide](https://developers.google.com/publisher-tag/guides/ad-sizes).

> [!CAUTION]
> **Caution:** Be aware of [ad slot expansion](https://support.google.com/admanager/answer/9117822) and [contraction settings](https://support.google.com/admanager/answer/9433610), which can affect the range of sizes eligible to serve to your ad slots.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/ad-sizes/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/ad-sizes/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/ad-sizes](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/ad-sizes)

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
      content="Specify which ad sizes are eligible to serve to an ad slot."
    />
    <title>Ad sizes</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Define a fixed-size ad slot.
        // [START fixed_size_ad]
        googletag
          .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "fixed-size-ad")
          .addService(googletag.pubads());
        // [END fixed_size_ad]

        // Define a fluid ad slot.
        // [START fluid_ad]
        googletag
          .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
          .addService(googletag.pubads());
        // [END fluid_ad]

        // Define a multi-size ad slot.
        // [START multi_size_ad]
        googletag
          .defineSlot(
            "/6355419/Travel/Europe",
            [[300, 250], [728, 90], [750, 200], "fluid"],
            "multi-size-ad",
          )
          .addService(googletag.pubads());
        // [END multi_size_ad]

        // Define a responsive ad slot.
        // [START responsive_ad]
        const responsiveAdSlot = googletag
          .defineSlot(
            "/6355419/Travel/Europe",
            [
              [300, 250],
              [728, 90],
              [750, 200],
            ],
            "responsive-ad",
          )
          .addService(googletag.pubads());

        const mapping = googletag
          .sizeMapping()
          .addSize(
            [1024, 768],
            [
              [750, 200],
              [728, 90],
            ],
          )
          .addSize([640, 480], [300, 250])
          .addSize([0, 0], [])
          .build();

        responsiveAdSlot.defineSizeMapping(mapping);
        // [END responsive_ad]

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      .ad-container {
        border: solid;
        width: 100%;
      }

      .ad-slot {
        border-style: dashed;
        display: inline-block;
      }

      .native-slot {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <h1>Fixed size ad slot</h1>
    <p>This ad slot will display an ad sized 300x250.</p>
    <div class="ad-container">
      <div id="fixed-size-ad" class="ad-slot"></div>
    </div>

    <h1>Fluid ad slot</h1>
    <p>
      This ad slot will resize its height to fit the creative content being displayed. For this
      example, the slot is limited to 50% of the width of its parent container.
    </p>
    <div class="ad-container">
      <div id="native-ad" class="ad-slot native-slot"></div>
    </div>

    <h1>Multi-size ad slot</h1>
    <p>
      This ad slot will display an ad with any of the following dimensions: 300x250, 728x90,
      750x200, 'fluid'.
    </p>
    <div class="ad-container">
      <div id="multi-size-ad" class="ad-slot"></div>
    </div>

    <h1>Responsive ad slot</h1>
    <p>
      This ad slot will display different sized ads depending on the size of the browser viewport at
      page load time:
    </p>
    <ul>
      <li>When viewport &gt;= 1024x768, ads sized 750x200 or 728x90 may be displayed.</li>
      <li>When 1024x768 &gt; viewport &gt;= 640x480, ads sized 300x250 may be displayed.</li>
      <li>When viewport &lt; 640x480, no ads may be displayed.</li>
    </ul>
    <div class="ad-container">
      <div id="responsive-ad" class="ad-slot"></div>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Request and render all previously defined ad slots.
        googletag.display("responsive-ad");
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
      content="Specify which ad sizes are eligible to serve to an ad slot."
    />
    <title>Ad sizes</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Define a fixed-size ad slot.
        // [START fixed_size_ad]
        googletag
          .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "fixed-size-ad")
          .addService(googletag.pubads());
        // [END fixed_size_ad]

        // Define a fluid ad slot.
        // [START fluid_ad]
        googletag
          .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
          .addService(googletag.pubads());
        // [END fluid_ad]

        // Define a multi-size ad slot.
        // [START multi_size_ad]
        googletag
          .defineSlot(
            "/6355419/Travel/Europe",
            [[300, 250], [728, 90], [750, 200], "fluid"],
            "multi-size-ad",
          )
          .addService(googletag.pubads());
        // [END multi_size_ad]

        // Define a responsive ad slot.
        // [START responsive_ad]
        var responsiveAdSlot = googletag
          .defineSlot(
            "/6355419/Travel/Europe",
            [
              [300, 250],
              [728, 90],
              [750, 200],
            ],
            "responsive-ad",
          )
          .addService(googletag.pubads());

        var mapping = googletag
          .sizeMapping()
          .addSize(
            [1024, 768],
            [
              [750, 200],
              [728, 90],
            ],
          )
          .addSize([640, 480], [300, 250])
          .addSize([0, 0], [])
          .build();

        responsiveAdSlot.defineSizeMapping(mapping);
        // [END responsive_ad]

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      .ad-container {
        border: solid;
        width: 100%;
      }

      .ad-slot {
        border-style: dashed;
        display: inline-block;
      }

      .native-slot {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <h1>Fixed size ad slot</h1>
    <p>This ad slot will display an ad sized 300x250.</p>
    <div class="ad-container">
      <div id="fixed-size-ad" class="ad-slot"></div>
    </div>

    <h1>Fluid ad slot</h1>
    <p>
      This ad slot will resize its height to fit the creative content being displayed. For this
      example, the slot is limited to 50% of the width of its parent container.
    </p>
    <div class="ad-container">
      <div id="native-ad" class="ad-slot native-slot"></div>
    </div>

    <h1>Multi-size ad slot</h1>
    <p>
      This ad slot will display an ad with any of the following dimensions: 300x250, 728x90,
      750x200, 'fluid'.
    </p>
    <div class="ad-container">
      <div id="multi-size-ad" class="ad-slot"></div>
    </div>

    <h1>Responsive ad slot</h1>
    <p>
      This ad slot will display different sized ads depending on the size of the browser viewport at
      page load time:
    </p>
    <ul>
      <li>When viewport &gt;= 1024x768, ads sized 750x200 or 728x90 may be displayed.</li>
      <li>When 1024x768 &gt; viewport &gt;= 640x480, ads sized 300x250 may be displayed.</li>
      <li>When viewport &lt; 640x480, no ads may be displayed.</li>
    </ul>
    <div class="ad-container">
      <div id="responsive-ad" class="ad-slot"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("responsive-ad");
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
      content="Specify which ad sizes are eligible to serve to an ad slot."
    />
    <title>Ad sizes</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .ad-container {
        border: solid;
        width: 100%;
      }

      .ad-slot {
        border-style: dashed;
        display: inline-block;
      }

      .native-slot {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <h1>Fixed size ad slot</h1>
    <p>This ad slot will display an ad sized 300x250.</p>
    <div class="ad-container">
      <div id="fixed-size-ad" class="ad-slot"></div>
    </div>

    <h1>Fluid ad slot</h1>
    <p>
      This ad slot will resize its height to fit the creative content being displayed. For this
      example, the slot is limited to 50% of the width of its parent container.
    </p>
    <div class="ad-container">
      <div id="native-ad" class="ad-slot native-slot"></div>
    </div>

    <h1>Multi-size ad slot</h1>
    <p>
      This ad slot will display an ad with any of the following dimensions: 300x250, 728x90,
      750x200, 'fluid'.
    </p>
    <div class="ad-container">
      <div id="multi-size-ad" class="ad-slot"></div>
    </div>

    <h1>Responsive ad slot</h1>
    <p>
      This ad slot will display different sized ads depending on the size of the browser viewport at
      page load time:
    </p>
    <ul>
      <li>When viewport &gt;= 1024x768, ads sized 750x200 or 728x90 may be displayed.</li>
      <li>When 1024x768 &gt; viewport &gt;= 640x480, ads sized 300x250 may be displayed.</li>
      <li>When viewport &lt; 640x480, no ads may be displayed.</li>
    </ul>
    <div class="ad-container">
      <div id="responsive-ad" class="ad-slot"></div>
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
  // Define a fixed-size ad slot.
  // [START fixed_size_ad]
  googletag
    .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "fixed-size-ad")!
    .addService(googletag.pubads());
  // [END fixed_size_ad]

  // Define a fluid ad slot.
  // [START fluid_ad]
  googletag.defineSlot("/6355419/Travel", ["fluid"], "native-ad")!.addService(googletag.pubads());
  // [END fluid_ad]

  // Define a multi-size ad slot.
  // [START multi_size_ad]
  googletag
    .defineSlot(
      "/6355419/Travel/Europe",
      [[300, 250], [728, 90], [750, 200], "fluid"],
      "multi-size-ad",
    )!
    .addService(googletag.pubads());
  // [END multi_size_ad]

  // Define a responsive ad slot.
  // [START responsive_ad]
  const responsiveAdSlot: googletag.Slot = googletag
    .defineSlot(
      "/6355419/Travel/Europe",
      [
        [300, 250],
        [728, 90],
        [750, 200],
      ],
      "responsive-ad",
    )!
    .addService(googletag.pubads());

  const mapping: googletag.SizeMappingArray = googletag
    .sizeMapping()
    .addSize(
      [1024, 768],
      [
        [750, 200],
        [728, 90],
      ],
    )
    .addSize([640, 480], [300, 250])
    .addSize([0, 0], [])
    .build()!;

  responsiveAdSlot.defineSizeMapping(mapping);
  // [END responsive_ad]

  // Enable SRA.
  googletag.setConfig({
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Request and render all previously defined ad slots.
  googletag.display("responsive-ad");
});
```
