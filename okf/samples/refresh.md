---
type: Sample
title: "Refresh Ad Slots"
description: "Sample implementation showing how to refresh specific ad slots dynamically."
resource: "https://developers.google.com/publisher-tag/samples/refresh"
tags: [gpt, sample, refresh]
timestamp: 2026-09-10T00:00:00Z
---

# Refresh ad slots

# Refresh ad slots

You can use the refresh functionality of the Google Publisher Tag (GPT) library
to dynamically reload ads without having to refresh the entire contents of your
page.

> [!IMPORTANT]
> **Important:** To comply with Google policy and enable your inventory to compete on Ad Exchange, you must [declare which portions of your inventory refresh](http://support.google.com/admanager/answer/6286179).

In order to implement this functionality, you'll need to generate a GPT tag and
apply some modifications. This sample implementation features two ad slots and
corresponding buttons to refresh the slots with new ads.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/refresh/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/refresh/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/refresh](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/refresh)

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
    <meta name="description" content="Use GPT to dynamically reload ads." />
    <title>Refresh ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let adSlot1;
      let adSlot2;

      googletag.cmd.push(() => {
        // Define the first slot.
        adSlot1 = googletag
          .defineSlot("/6355419/Travel", [728, 90], "leaderboard1")
          .addService(googletag.pubads());

        // Define the second slot.
        adSlot2 = googletag
          .defineSlot("/6355419/Travel", [728, 90], "leaderboard2")
          .addService(googletag.pubads());

        // Enable SRA and set page-level targeting.
        googletag.setConfig({
          targeting: {
            test: "refresh",
          },
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });

      // Button action which refreshes the first slot
      function refreshFirstSlot() {
        if (!adSlot1) return;
        googletag.cmd.push(() => {
          googletag.pubads().refresh([adSlot1]);
        });
      }

      // Button action which refreshes the second slot
      function refreshSecondSlot() {
        if (!adSlot2) return;
        googletag.cmd.push(() => {
          googletag.pubads().refresh([adSlot2]);
        });
      }

      // Button action which refreshes all slots
      function refreshAllSlots() {
        googletag.cmd.push(() => {
          googletag.pubads().refresh();
        });
      }

      // Button action which clears all slots
      // Note: calling PubAdsService.clear() removes any currently displayed ads
      // and replaces them with blank content, leaving the slots intact so they
      // can be repopulated later.
      function clearAllSlots() {
        googletag.cmd.push(() => {
          googletag.pubads().clear();
        });
      }
    </script>
    <style></style>
  </head>
  <body>
    <div>
      <h1>GPT Training - Slot Refresh</h1>
      <div id="leaderboard1" style="width: 728px; height: 90px"></div>

      <div id="leaderboard2" style="width: 728px; height: 90px"></div>
    </div>

    <div>
      <!-- Refresh the first slot -->
      <button id="refreshTopButton">Refresh Top Ad</button>

      <!-- Refresh the second slot -->
      <button id="refreshBottomButton">Refresh Bottom Ad</button>

      <!-- Refresh both slots -->
      <button id="refreshAllButton">Refresh All Ads</button>

      <!-- Clear slots -->
      <button id="clearAllButton">Clear All Ads</button>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("leaderboard1");

        // Register click event handlers.
        document.getElementById("refreshTopButton").addEventListener("click", refreshFirstSlot);
        document.getElementById("refreshBottomButton").addEventListener("click", refreshSecondSlot);
        document.getElementById("refreshAllButton").addEventListener("click", refreshAllSlots);
        document.getElementById("clearAllButton").addEventListener("click", clearAllSlots);
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
    <meta name="description" content="Use GPT to dynamically reload ads." />
    <title>Refresh ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var adSlot1;
      var adSlot2;

      googletag.cmd.push(function () {
        // Define the first slot.
        adSlot1 = googletag
          .defineSlot("/6355419/Travel", [728, 90], "leaderboard1")
          .addService(googletag.pubads());

        // Define the second slot.
        adSlot2 = googletag
          .defineSlot("/6355419/Travel", [728, 90], "leaderboard2")
          .addService(googletag.pubads());

        // Enable SRA and set page-level targeting.
        googletag.setConfig({
          targeting: {
            test: "refresh",
          },
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });

      // Button action which refreshes the first slot
      function refreshFirstSlot() {
        if (!adSlot1) return;
        googletag.cmd.push(function () {
          googletag.pubads().refresh([adSlot1]);
        });
      }

      // Button action which refreshes the second slot
      function refreshSecondSlot() {
        if (!adSlot2) return;
        googletag.cmd.push(function () {
          googletag.pubads().refresh([adSlot2]);
        });
      }

      // Button action which refreshes all slots
      function refreshAllSlots() {
        googletag.cmd.push(function () {
          googletag.pubads().refresh();
        });
      }

      // Button action which clears all slots
      // Note: calling PubAdsService.clear() removes any currently displayed ads
      // and replaces them with blank content, leaving the slots intact so they
      // can be repopulated later.
      function clearAllSlots() {
        googletag.cmd.push(function () {
          googletag.pubads().clear();
        });
      }
    </script>
    <style></style>
  </head>
  <body>
    <div>
      <h1>GPT Training - Slot Refresh</h1>
      <div id="leaderboard1" style="width: 728px; height: 90px"></div>

      <div id="leaderboard2" style="width: 728px; height: 90px"></div>
    </div>

    <div>
      <!-- Refresh the first slot -->
      <button id="refreshTopButton">Refresh Top Ad</button>

      <!-- Refresh the second slot -->
      <button id="refreshBottomButton">Refresh Bottom Ad</button>

      <!-- Refresh both slots -->
      <button id="refreshAllButton">Refresh All Ads</button>

      <!-- Clear slots -->
      <button id="clearAllButton">Clear All Ads</button>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("leaderboard1");

        // Register click event handlers.
        document.getElementById("refreshTopButton").addEventListener("click", refreshFirstSlot);
        document.getElementById("refreshBottomButton").addEventListener("click", refreshSecondSlot);
        document.getElementById("refreshAllButton").addEventListener("click", refreshAllSlots);
        document.getElementById("clearAllButton").addEventListener("click", clearAllSlots);
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
    <meta name="description" content="Use GPT to dynamically reload ads." />
    <title>Refresh ad slots</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style></style>
  </head>
  <body>
    <div>
      <h1>GPT Training - Slot Refresh</h1>
      <div id="leaderboard1" style="width: 728px; height: 90px"></div>

      <div id="leaderboard2" style="width: 728px; height: 90px"></div>
    </div>

    <div>
      <!-- Refresh the first slot -->
      <button id="refreshTopButton">Refresh Top Ad</button>

      <!-- Refresh the second slot -->
      <button id="refreshBottomButton">Refresh Bottom Ad</button>

      <!-- Refresh both slots -->
      <button id="refreshAllButton">Refresh All Ads</button>

      <!-- Clear slots -->
      <button id="clearAllButton">Clear All Ads</button>
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

let adSlot1: googletag.Slot | null;
let adSlot2: googletag.Slot | null;

googletag.cmd.push(() => {
  // Define the first slot.
  adSlot1 = googletag
    .defineSlot("/6355419/Travel", [728, 90], "leaderboard1")!
    .addService(googletag.pubads());

  // Define the second slot.
  adSlot2 = googletag
    .defineSlot("/6355419/Travel", [728, 90], "leaderboard2")!
    .addService(googletag.pubads());

  // Enable SRA and set page-level targeting.
  googletag.setConfig({
    targeting: {
      test: "refresh",
    },
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Request and render all previously defined ad slots.
  googletag.display("leaderboard1");
});

// Button action which refreshes the first slot
function refreshFirstSlot() {
  if (!adSlot1) return;
  googletag.cmd.push(() => {
    googletag.pubads().refresh([adSlot1!]);
  });
}

// Button action which refreshes the second slot
function refreshSecondSlot() {
  if (!adSlot2) return;
  googletag.cmd.push(() => {
    googletag.pubads().refresh([adSlot2!]);
  });
}

// Button action which refreshes all slots
function refreshAllSlots() {
  googletag.cmd.push(() => {
    googletag.pubads().refresh();
  });
}

// Button action which clears all slots
// Note: calling PubAdsService.clear() removes any currently displayed ads
// and replaces them with blank content, leaving the slots intact so they
// can be repopulated later.
function clearAllSlots() {
  googletag.cmd.push(() => {
    googletag.pubads().clear();
  });
}

// Register click event handlers.
document.getElementById("refreshTopButton")!.addEventListener("click", refreshFirstSlot);
document.getElementById("refreshBottomButton")!.addEventListener("click", refreshSecondSlot);
document.getElementById("refreshAllButton")!.addEventListener("click", refreshAllSlots);
document.getElementById("clearAllButton")!.addEventListener("click", clearAllSlots);
```
