# Event-based ad requests

# Event-based ad requests

You can request ads based on events using the Google Publisher Tag library. In
the example below, a new ad is not requested or rendered until the user clicks a
button.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/event-based-requests/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/event-based-requests/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/event-based-requests](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/event-based-requests)

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
    <meta name="description" content="Request GPT ads based on events." />
    <title>Event-based ad requests</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Define the ad slot.
        googletag
          .defineSlot("/6355419/Travel", [728, 90], "div-for-slot")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              test: "event",
            },
          });

        // Disable initial load to prevent GPT from automatically fetching ads when
        // display() is called.
        googletag.setConfig({
          disableInitialLoad: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="div-for-slot" style="width: 300px; height: 250px"></div>
    <button id="showAdButton">Show/Refresh Ad</button>
    <script>
      googletag.cmd.push(() => {
        // Register the ad slot.
        // An ad will not be fetched until refresh is called.
        googletag.display("div-for-slot");

        // Register click event handler.
        document.getElementById("showAdButton").addEventListener("click", () => {
          googletag.cmd.push(() => {
            googletag.pubads().refresh();
          });
        });
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
    <meta name="description" content="Request GPT ads based on events." />
    <title>Event-based ad requests</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Define the ad slot.
        googletag
          .defineSlot("/6355419/Travel", [728, 90], "div-for-slot")
          .addService(googletag.pubads())
          .setConfig({
            targeting: {
              test: "event",
            },
          });

        // Disable initial load to prevent GPT from automatically fetching ads when
        // display() is called.
        googletag.setConfig({
          disableInitialLoad: true,
        });

        // Enable services.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="div-for-slot" style="width: 300px; height: 250px"></div>
    <button id="showAdButton">Show/Refresh Ad</button>
    <script>
      googletag.cmd.push(function () {
        // Register the ad slot.
        // An ad will not be fetched until refresh is called.
        googletag.display("div-for-slot");

        // Register click event handler.
        document.getElementById("showAdButton").addEventListener("click", function () {
          googletag.cmd.push(function () {
            googletag.pubads().refresh();
          });
        });
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
    <meta name="description" content="Request GPT ads based on events." />
    <title>Event-based ad requests</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style></style>
  </head>
  <body>
    <div id="div-for-slot" style="width: 300px; height: 250px"></div>
    <button id="showAdButton">Show/Refresh Ad</button>
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
  // Define the ad slot.
  googletag
    .defineSlot("/6355419/Travel", [728, 90], "div-for-slot")!
    .addService(googletag.pubads())
    .setConfig({
      targeting: {
        test: "event",
      },
    });

  // Disable initial load to prevent GPT from automatically fetching ads when
  // display() is called.
  googletag.setConfig({
    disableInitialLoad: true,
  });

  // Enable services.
  googletag.enableServices();

  // Register the ad slot.
  // An ad will not be fetched until refresh is called.
  googletag.display("div-for-slot");
});

// Register click event handler.
document.getElementById("showAdButton")!.addEventListener("click", () => {
  googletag.cmd.push(() => {
    googletag.pubads().refresh();
  });
});
```
