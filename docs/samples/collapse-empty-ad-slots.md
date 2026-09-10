# Collapse empty ad slots

# Collapse empty ad slots

By default, ad slots which are not filled are left visible, which may result in
blank space on your page. If you know ahead of time that one or more ad slots on
your page are unlikely to get filled, you can instruct the Google Publisher Tag
(GPT) library to collapse them.

> [!CAUTION]
> **Caution:** Incorrect use of this feature can cause additional reflow of the content of your page.

The optimal configuration of this feature will depend on how often you expect ad
slots to be filled:

1. If slots will be filled most of the time, use [`collapseDiv: 'ON_NO_FILL'`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv). In this configuration, ad slots are expanded by default and collapse only if they cannot be filled.
2. If slots will not be filled most of the time, use [`collapseDiv: 'BEFORE_FETCH'`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv). In this configuration, ad slots are collapsed by default and only expand if they can be filled.

Because `googletag` API calls have no effect until GPT begins to run, to
minimize reflow you will also need to configure the CSS on your page so that
slots which are collapsed by default have zero dimensions.

It's also possible to configure per-slot overrides, as shown in the example
below, if specific slots on your page are more or less likely to be filled.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/collapse-empty-ad-slots/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/collapse-empty-ad-slots/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/collapse-empty-ad-slots](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/collapse-empty-ad-slots)

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
      content="Automatically show/hide ad slots when certain criteria are met."
    />
    <title>Collapse empty ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Configure all ad slots on the page to be expanded by default, but
        // collapse slots that are unable to be filled with an ad. Also enables
        // SRA.
        googletag.setConfig({
          collapseDiv: "ON_NO_FILL",
          singleRequest: true,
          targeting: {
            test: "responsive",
          },
        });

        // The above setting assumes all ad slots are likely to be filled.
        // If ad slots are not likely to be filled, 'BEFORE_FETCH' can be used
        // instead. In this configuration, slots will be collapsed by default and
        // expanded only if they are able to be filled.
        // googletag.setConfig({
        //   collapseDiv: 'BEFORE_FETCH',
        //   singleRequest: true,
        // });

        // This slot will use the page-level settings configured above.
        googletag
          .defineSlot("/6355419/Travel", [300, 250], "ad-slot-1")
          .addService(googletag.pubads());

        // Configure per-slot overrides.
        // This slot will be expanded by default, but collapse if it cannot be
        // filled.
        googletag
          .defineSlot("/6355419/Travel", [250, 200], "ad-slot-2")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "ON_NO_FILL" });

        // This slot will be expanded by default and never collapse.
        googletag
          .defineSlot("/6355419/Travel", [200, 150], "ad-slot-3")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "DISABLED" });

        // This slot will be collapsed by default and only expand if it can be
        // filled.
        googletag
          .defineSlot("/6355419/Travel", [150, 100], "ad-slot-4")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "BEFORE_FETCH" });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      div.ad-container {
        border: solid;
      }

      div.ad-slot {
        border-style: dashed;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <div class="ad-container">
      <p>Ad slot #1</p>
      <div id="ad-slot-1" class="ad-slot"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #2</p>
      <div id="ad-slot-2" class="ad-slot" style="width: 250px; height: 200px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #3</p>
      <div id="ad-slot-3" class="ad-slot" style="width: 200px; height: 150px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #4</p>
      <div id="ad-slot-4" class="ad-slot"></div>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Request and render all previously defined ad slots.
        googletag.display("ad-slot-1");
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
      content="Automatically show/hide ad slots when certain criteria are met."
    />
    <title>Collapse empty ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Configure all ad slots on the page to be expanded by default, but
        // collapse slots that are unable to be filled with an ad. Also enables
        // SRA.
        googletag.setConfig({
          collapseDiv: "ON_NO_FILL",
          singleRequest: true,
          targeting: {
            test: "responsive",
          },
        });

        // The above setting assumes all ad slots are likely to be filled.
        // If ad slots are not likely to be filled, 'BEFORE_FETCH' can be used
        // instead. In this configuration, slots will be collapsed by default and
        // expanded only if they are able to be filled.
        // googletag.setConfig({
        //   collapseDiv: 'BEFORE_FETCH',
        //   singleRequest: true,
        // });

        // This slot will use the page-level settings configured above.
        googletag
          .defineSlot("/6355419/Travel", [300, 250], "ad-slot-1")
          .addService(googletag.pubads());

        // Configure per-slot overrides.
        // This slot will be expanded by default, but collapse if it cannot be
        // filled.
        googletag
          .defineSlot("/6355419/Travel", [250, 200], "ad-slot-2")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "ON_NO_FILL" });

        // This slot will be expanded by default and never collapse.
        googletag
          .defineSlot("/6355419/Travel", [200, 150], "ad-slot-3")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "DISABLED" });

        // This slot will be collapsed by default and only expand if it can be
        // filled.
        googletag
          .defineSlot("/6355419/Travel", [150, 100], "ad-slot-4")
          .addService(googletag.pubads())
          .setConfig({ collapseDiv: "BEFORE_FETCH" });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style>
      div.ad-container {
        border: solid;
      }

      div.ad-slot {
        border-style: dashed;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <div class="ad-container">
      <p>Ad slot #1</p>
      <div id="ad-slot-1" class="ad-slot"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #2</p>
      <div id="ad-slot-2" class="ad-slot" style="width: 250px; height: 200px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #3</p>
      <div id="ad-slot-3" class="ad-slot" style="width: 200px; height: 150px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #4</p>
      <div id="ad-slot-4" class="ad-slot"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("ad-slot-1");
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
      content="Automatically show/hide ad slots when certain criteria are met."
    />
    <title>Collapse empty ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      div.ad-container {
        border: solid;
      }

      div.ad-slot {
        border-style: dashed;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <div class="ad-container">
      <p>Ad slot #1</p>
      <div id="ad-slot-1" class="ad-slot"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #2</p>
      <div id="ad-slot-2" class="ad-slot" style="width: 250px; height: 200px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #3</p>
      <div id="ad-slot-3" class="ad-slot" style="width: 200px; height: 150px"></div>
    </div>

    <div class="ad-container">
      <p>Ad slot #4</p>
      <div id="ad-slot-4" class="ad-slot"></div>
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
  // Configure all ad slots on the page to be expanded by default, but
  // collapse slots that are unable to be filled with an ad. Also enables
  // SRA.
  googletag.setConfig({
    collapseDiv: "ON_NO_FILL",
    singleRequest: true,
    targeting: {
      test: "responsive",
    },
  });

  // The above setting assumes all ad slots are likely to be filled.
  // If ad slots are not likely to be filled, 'BEFORE_FETCH' can be used
  // instead. In this configuration, slots will be collapsed by default and
  // expanded only if they are able to be filled.
  // googletag.setConfig({
  //   collapseDiv: 'BEFORE_FETCH',
  //   singleRequest: true,
  // });

  // This slot will use the page-level settings configured above.
  googletag.defineSlot("/6355419/Travel", [300, 250], "ad-slot-1")!.addService(googletag.pubads());

  // Configure per-slot overrides.
  // This slot will be expanded by default, but collapse if it cannot be
  // filled.
  googletag
    .defineSlot("/6355419/Travel", [250, 200], "ad-slot-2")!
    .addService(googletag.pubads())
    .setConfig({ collapseDiv: "ON_NO_FILL" });

  // This slot will be expanded by default and never collapse.
  googletag
    .defineSlot("/6355419/Travel", [200, 150], "ad-slot-3")!
    .addService(googletag.pubads())
    .setConfig({ collapseDiv: "DISABLED" });

  // This slot will be collapsed by default and only expand if it can be
  // filled.
  googletag
    .defineSlot("/6355419/Travel", [150, 100], "ad-slot-4")!
    .addService(googletag.pubads())
    .setConfig({ collapseDiv: "BEFORE_FETCH" });

  // Enable services.
  googletag.enableServices();

  // Request and render all previously defined ad slots.
  googletag.display("ad-slot-1");
});
```
