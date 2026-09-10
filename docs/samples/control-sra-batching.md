# Control SRA batching

# Control SRA batching

The Google Publisher Tag (GPT) library's Single Request Architecture (SRA) mode
batches multiple ad slots into a single ad request. This provides performance
benefits, but is also necessary to guarantee that
[competitive exclusions and roadblocks](https://support.google.com/admanager/answer/177277) are honored.

By default, all ad slots defined prior to calling `display()` or `refresh()`
will be batched and requested together when SRA mode is active. There are some
situations where you may want more control over this batching behavior, however.
For example, to [prioritize the loading of specific slots](https://developers.google.com/publisher-tag/guides/ad-best-practices#prioritize_important_ad_slots) or
to avoid exceeding the
[maximum number of slots in a single SRA request](https://developers.google.com/publisher-tag/guides/publisher-console-messages#TOO_MANY_SLOTS_IN_SRA_REQUEST).

> [!WARNING]
> **Warning:** Roadblocks are not guaranteed across multiple SRA batches.

This example demonstrates how to apply techniques for
[controlling ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading) to SRA requests.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/control-sra-batching/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/control-sra-batching/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/control-sra-batching](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/control-sra-batching)

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
      content="Precisely control which ad slots are requested when in Single Request Architecture (SRA) mode."
    />
    <title>Control SRA batching</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      // Number of seconds to wait before making the second SRA request.
      let waitSeconds = 5;

      googletag.cmd.push(() => {
        // Define ad slots.
        const slots = [
          googletag
            .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-1")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-2")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-3")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-4")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-5")
            .addService(googletag.pubads()),
        ];

        // Disable initial load and enable SRA to precisely control when ads are
        // requested.
        googletag.setConfig({
          disableInitialLoad: true,
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();

        // Issue first SRA request (slots 1 and 2) immediately.
        googletag.pubads().refresh(slots.slice(0, 2));

        // Issue second SRA request (slots 3, 4, and 5) after a delay.
        const interval = setInterval(() => {
          document.getElementById("seconds").textContent = (--waitSeconds).toString();

          if (waitSeconds === 0) {
            googletag.pubads().refresh(slots.slice(2));
            clearInterval(interval);
          }
        }, 1000);
      });
    </script>
    <style>
      .ad-slot {
        border-style: solid;
        display: block;
        margin: 1px;
      }

      .row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
    </style>
  </head>
  <body>
    <div class="row">
      <p>SRA request #1</p>
    </div>

    <div class="row">
      <div id="slot-1" class="ad-slot" style="height: 90px; width: 728px"></div>
      <div id="slot-2" class="ad-slot" style="height: 90px; width: 728px"></div>
    </div>

    <div class="row">
      <p>SRA request #2 in <span id="seconds">5</span> seconds...</p>
    </div>

    <div class="row">
      <div id="slot-3" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-4" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-5" class="ad-slot" style="height: 250px; width: 300px"></div>
    </div>
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
      content="Precisely control which ad slots are requested when in Single Request Architecture (SRA) mode."
    />
    <title>Control SRA batching</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      // Number of seconds to wait before making the second SRA request.
      var waitSeconds = 5;

      googletag.cmd.push(function () {
        // Define ad slots.
        var slots = [
          googletag
            .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-1")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-2")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-3")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-4")
            .addService(googletag.pubads()),
          googletag
            .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-5")
            .addService(googletag.pubads()),
        ];

        // Disable initial load and enable SRA to precisely control when ads are
        // requested.
        googletag.setConfig({
          disableInitialLoad: true,
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();

        // Issue first SRA request (slots 1 and 2) immediately.
        googletag.pubads().refresh(slots.slice(0, 2));

        // Issue second SRA request (slots 3, 4, and 5) after a delay.
        var interval = setInterval(function () {
          document.getElementById("seconds").textContent = (--waitSeconds).toString();

          if (waitSeconds === 0) {
            googletag.pubads().refresh(slots.slice(2));
            clearInterval(interval);
          }
        }, 1000);
      });
    </script>
    <style>
      .ad-slot {
        border-style: solid;
        display: block;
        margin: 1px;
      }

      .row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
    </style>
  </head>
  <body>
    <div class="row">
      <p>SRA request #1</p>
    </div>

    <div class="row">
      <div id="slot-1" class="ad-slot" style="height: 90px; width: 728px"></div>
      <div id="slot-2" class="ad-slot" style="height: 90px; width: 728px"></div>
    </div>

    <div class="row">
      <p>SRA request #2 in <span id="seconds">5</span> seconds...</p>
    </div>

    <div class="row">
      <div id="slot-3" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-4" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-5" class="ad-slot" style="height: 250px; width: 300px"></div>
    </div>
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
      content="Precisely control which ad slots are requested when in Single Request Architecture (SRA) mode."
    />
    <title>Control SRA batching</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .ad-slot {
        border-style: solid;
        display: block;
        margin: 1px;
      }

      .row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
    </style>
  </head>
  <body>
    <div class="row">
      <p>SRA request #1</p>
    </div>

    <div class="row">
      <div id="slot-1" class="ad-slot" style="height: 90px; width: 728px"></div>
      <div id="slot-2" class="ad-slot" style="height: 90px; width: 728px"></div>
    </div>

    <div class="row">
      <p>SRA request #2 in <span id="seconds">5</span> seconds...</p>
    </div>

    <div class="row">
      <div id="slot-3" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-4" class="ad-slot" style="height: 250px; width: 300px"></div>
      <div id="slot-5" class="ad-slot" style="height: 250px; width: 300px"></div>
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

// Number of seconds to wait before making the second SRA request.
let waitSeconds = 5;

googletag.cmd.push(() => {
  // Define ad slots.
  const slots = [
    googletag
      .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-1")!
      .addService(googletag.pubads()),
    googletag
      .defineSlot("/6355419/Travel/Europe", [728, 90], "slot-2")!
      .addService(googletag.pubads()),
    googletag
      .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-3")!
      .addService(googletag.pubads()),
    googletag
      .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-4")!
      .addService(googletag.pubads()),
    googletag
      .defineSlot("/6355419/Travel/Europe", [300, 250], "slot-5")!
      .addService(googletag.pubads()),
  ];

  // Disable initial load and enable SRA to precisely control when ads are
  // requested.
  googletag.setConfig({
    disableInitialLoad: true,
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Issue first SRA request (slots 1 and 2) immediately.
  googletag.pubads().refresh(slots.slice(0, 2));

  // Issue second SRA request (slots 3, 4, and 5) after a delay.
  const interval = setInterval(() => {
    document.getElementById("seconds")!.textContent = (--waitSeconds).toString();

    if (waitSeconds === 0) {
      googletag.pubads().refresh(slots.slice(2));
      clearInterval(interval);
    }
  }, 1000);
});
```
