# Ad event listeners

# Ad event listeners

The Google Publisher Tag (GPT) library allows you to register and call
JavaScript functions when specific GPT-related ad events occur. This sample
provides a demonstration of using the GPT event framework to monitor and report
on the following events.

| Event | Fired when... |
|---|---|
| [ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent) | An impression becomes viewable. |
| [SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent) | A creative iframe fires its onload event. |
| [SlotRenderEndedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent) | Creative code has been injected into an ad slot. |
| [SlotRequestedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent) | An ad has been requested for the ad slot. |
| [SlotResponseReceivedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived) | An ad response has been received for the ad slot. |
| [SlotVisibilityChangedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent) | The on-screen percentage of the ad slot changes. |


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/ad-event-listeners/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/ad-event-listeners/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/ad-event-listeners](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/ad-event-listeners)

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
    <meta name="description" content="Monitor and report on ad events fired by GPT." />
    <title>Ad event listeners</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let requestedTimestamp = {};

      googletag.cmd.push(() => {
        // Define ad slots.
        googletag
          .defineSlot("/6355419/Travel/Europe", [728, 90], "ad-slot-1")
          .addService(googletag.pubads());
        googletag
          .defineSlot("/6355419/Travel/Europe", [750, 200], "ad-slot-2")
          .addService(googletag.pubads());

        // This listener will be called when an impression is considered viewable.
        googletag.pubads().addEventListener("impressionViewable", (event) => {
          const slotId = event.slot.getSlotElementId();
          printEventMessage("Impression has become viewable.", slotId);
        });

        // This listener will be called when a slot's creative iframe load event
        // fires.
        googletag.pubads().addEventListener("slotOnload", (event) => {
          const slotId = event.slot.getSlotElementId();
          printEventMessage("Creative iframe load event has fired.", slotId);
        });

        // This listener will be called when a slot has finished rendering.
        googletag.pubads().addEventListener("slotRenderEnded", (event) => {
          const slotId = event.slot.getSlotElementId();

          // Record details of the rendered ad.
          const details = {
            "Advertiser ID": event.advertiserId,
            "Campaign ID": event.campaignId,
            "Company IDs": event.companyIds,
            "Creative ID": event.creativeId,
            "Creative Template ID": event.creativeId,
            "Is backfill?": event.isBackfill,
            "Is empty?": event.isEmpty,
            "Line Item ID": event.lineItemId,
            "Response Identifier": event.responseIdentifier,
            Size: typeof event.size === "string" ? event.size : (event.size?.join("x") ?? null),
            "Slot content changed?": event.slotContentChanged,
            "Source Agnostic Creative ID": event.sourceAgnosticCreativeId,
            "Source Agnostic Line Item ID": event.sourceAgnosticLineItemId,
            "Yield Group IDs": event.yieldGroupIds,
          };

          printEventMessage("Slot has finished rendering.", slotId, details);
        });

        // This listener will be called when the specified service actually
        // sets an ad request for a slot. Each slot will fire this event, even
        // though they may be batched together in a single request if single
        // request architecture (SRA) is enabled.
        googletag.pubads().addEventListener("slotRequested", (event) => {
          const slotId = event.slot.getSlotElementId();
          requestedTimestamp[slotId] = Date.now();
          printEventMessage("Slot has been requested.", slotId);
        });

        // This listener will be called when an ad response has been received for
        // a slot.
        googletag.pubads().addEventListener("slotResponseReceived", (event) => {
          const slotId = event.slot.getSlotElementId();
          printEventMessage("Ad response has been received.", slotId);
        });

        // This listener will be called whenever the on-screen percentage of an ad
        // slot's area changes.
        googletag.pubads().addEventListener("slotVisibilityChanged", (event) => {
          const slotId = event.slot.getSlotElementId();

          // Record details of the event.
          const details = { "Visible area": `${event.inViewPercentage}%` };

          printEventMessage("Visibility has changed.", slotId, details);
        });

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });

      function printEventMessage(eventMessage, slotId, details = {}) {
        const row = document.getElementsByClassName("status-row")[0].cloneNode(true);

        const cells = row.getElementsByClassName("status-cell");
        cells[0].textContent = slotId;
        cells[1].textContent = eventMessage;
        for (const key in details) {
          if (!details.hasOwnProperty(key) || !details[key]) continue;

          const detailElem = document.createElement("p");
          detailElem.className = "status-detail";
          detailElem.textContent = `${key}: ${details[key]}`;
          cells[1].appendChild(detailElem);
        }
        cells[2].textContent = `${Date.now() - requestedTimestamp[slotId]}ms`;

        document.getElementsByClassName("status-container")[0].appendChild(row);
      }
    </script>
    <style>
      .status,
      .status-row {
        display: inline-table;
        width: 750px;
      }

      .status-container {
        height: 400px;
        overflow: scroll;
        width: 100%;
      }

      .status-row:nth-child(even) {
        background-color: lightsteelblue;
      }

      .status-cell {
        float: left;
        min-width: 15%;
      }

      .status-detail {
        margin: 0;
        padding-left: 1em;
      }

      .event {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <span>Ad slot 1</span>
    <div id="ad-slot-1" style="width: 728px; height: 90px"></div>

    <span>Ad slot 2</span>
    <div id="ad-slot-2" style="width: 750px; height: 200px"></div>

    <div class="status">
      <div class="status-row">
        <div class="status-cell"><b>Slot</b></div>
        <div class="status-cell event"><b>Event</b></div>
        <div class="status-cell"><b>Time from ad request</b></div>
      </div>

      <div class="status-container"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("ad-slot-2");
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
    <meta name="description" content="Monitor and report on ad events fired by GPT." />
    <title>Ad event listeners</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var requestedTimestamp = {};

      googletag.cmd.push(function () {
        // Define ad slots.
        googletag
          .defineSlot("/6355419/Travel/Europe", [728, 90], "ad-slot-1")
          .addService(googletag.pubads());
        googletag
          .defineSlot("/6355419/Travel/Europe", [750, 200], "ad-slot-2")
          .addService(googletag.pubads());

        // This listener will be called when an impression is considered viewable.
        googletag.pubads().addEventListener("impressionViewable", function (event) {
          var slotId = event.slot.getSlotElementId();
          printEventMessage("Impression has become viewable.", slotId);
        });

        // This listener will be called when a slot's creative iframe load event
        // fires.
        googletag.pubads().addEventListener("slotOnload", function (event) {
          var slotId = event.slot.getSlotElementId();
          printEventMessage("Creative iframe load event has fired.", slotId);
        });

        // This listener will be called when a slot has finished rendering.
        googletag.pubads().addEventListener("slotRenderEnded", function (event) {
          var _a, _b;
          var slotId = event.slot.getSlotElementId();

          // Record details of the rendered ad.
          var details = {
            "Advertiser ID": event.advertiserId,
            "Campaign ID": event.campaignId,
            "Company IDs": event.companyIds,
            "Creative ID": event.creativeId,
            "Creative Template ID": event.creativeId,
            "Is backfill?": event.isBackfill,
            "Is empty?": event.isEmpty,
            "Line Item ID": event.lineItemId,
            "Response Identifier": event.responseIdentifier,
            Size:
              typeof event.size === "string"
                ? event.size
                : (_b = (_a = event.size) === null || _a === void 0 ? void 0 : _a.join("x")) !==
                      null && _b !== void 0
                  ? _b
                  : null,
            "Slot content changed?": event.slotContentChanged,
            "Source Agnostic Creative ID": event.sourceAgnosticCreativeId,
            "Source Agnostic Line Item ID": event.sourceAgnosticLineItemId,
            "Yield Group IDs": event.yieldGroupIds,
          };

          printEventMessage("Slot has finished rendering.", slotId, details);
        });

        // This listener will be called when the specified service actually
        // sets an ad request for a slot. Each slot will fire this event, even
        // though they may be batched together in a single request if single
        // request architecture (SRA) is enabled.
        googletag.pubads().addEventListener("slotRequested", function (event) {
          var slotId = event.slot.getSlotElementId();
          requestedTimestamp[slotId] = Date.now();
          printEventMessage("Slot has been requested.", slotId);
        });

        // This listener will be called when an ad response has been received for
        // a slot.
        googletag.pubads().addEventListener("slotResponseReceived", function (event) {
          var slotId = event.slot.getSlotElementId();
          printEventMessage("Ad response has been received.", slotId);
        });

        // This listener will be called whenever the on-screen percentage of an ad
        // slot's area changes.
        googletag.pubads().addEventListener("slotVisibilityChanged", function (event) {
          var slotId = event.slot.getSlotElementId();

          // Record details of the event.
          var details = { "Visible area": "".concat(event.inViewPercentage, "%") };

          printEventMessage("Visibility has changed.", slotId, details);
        });

        // Enable SRA.
        googletag.setConfig({
          singleRequest: true,
        });

        // Enable services.
        googletag.enableServices();
      });

      function printEventMessage(eventMessage, slotId, details) {
        if (details === void 0) {
          details = {};
        }
        var row = document.getElementsByClassName("status-row")[0].cloneNode(true);

        var cells = row.getElementsByClassName("status-cell");
        cells[0].textContent = slotId;
        cells[1].textContent = eventMessage;
        for (var key in details) {
          if (!details.hasOwnProperty(key) || !details[key]) continue;

          var detailElem = document.createElement("p");
          detailElem.className = "status-detail";
          detailElem.textContent = "".concat(key, ": ").concat(details[key]);
          cells[1].appendChild(detailElem);
        }
        cells[2].textContent = "".concat(Date.now() - requestedTimestamp[slotId], "ms");

        document.getElementsByClassName("status-container")[0].appendChild(row);
      }
    </script>
    <style>
      .status,
      .status-row {
        display: inline-table;
        width: 750px;
      }

      .status-container {
        height: 400px;
        overflow: scroll;
        width: 100%;
      }

      .status-row:nth-child(even) {
        background-color: lightsteelblue;
      }

      .status-cell {
        float: left;
        min-width: 15%;
      }

      .status-detail {
        margin: 0;
        padding-left: 1em;
      }

      .event {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <span>Ad slot 1</span>
    <div id="ad-slot-1" style="width: 728px; height: 90px"></div>

    <span>Ad slot 2</span>
    <div id="ad-slot-2" style="width: 750px; height: 200px"></div>

    <div class="status">
      <div class="status-row">
        <div class="status-cell"><b>Slot</b></div>
        <div class="status-cell event"><b>Event</b></div>
        <div class="status-cell"><b>Time from ad request</b></div>
      </div>

      <div class="status-container"></div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Request and render all previously defined ad slots.
        googletag.display("ad-slot-2");
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
    <meta name="description" content="Monitor and report on ad events fired by GPT." />
    <title>Ad event listeners</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .status,
      .status-row {
        display: inline-table;
        width: 750px;
      }

      .status-container {
        height: 400px;
        overflow: scroll;
        width: 100%;
      }

      .status-row:nth-child(even) {
        background-color: lightsteelblue;
      }

      .status-cell {
        float: left;
        min-width: 15%;
      }

      .status-detail {
        margin: 0;
        padding-left: 1em;
      }

      .event {
        width: 50%;
      }
    </style>
  </head>
  <body>
    <span>Ad slot 1</span>
    <div id="ad-slot-1" style="width: 728px; height: 90px"></div>

    <span>Ad slot 2</span>
    <div id="ad-slot-2" style="width: 750px; height: 200px"></div>

    <div class="status">
      <div class="status-row">
        <div class="status-cell"><b>Slot</b></div>
        <div class="status-cell event"><b>Event</b></div>
        <div class="status-cell"><b>Time from ad request</b></div>
      </div>

      <div class="status-container"></div>
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

let requestedTimestamp: { [key: string]: number } = {};

googletag.cmd.push(() => {
  // Define ad slots.
  googletag
    .defineSlot("/6355419/Travel/Europe", [728, 90], "ad-slot-1")!
    .addService(googletag.pubads());
  googletag
    .defineSlot("/6355419/Travel/Europe", [750, 200], "ad-slot-2")!
    .addService(googletag.pubads());

  // This listener will be called when an impression is considered viewable.
  googletag.pubads().addEventListener("impressionViewable", (event) => {
    const slotId = event.slot.getSlotElementId();
    printEventMessage("Impression has become viewable.", slotId);
  });

  // This listener will be called when a slot's creative iframe load event
  // fires.
  googletag.pubads().addEventListener("slotOnload", (event) => {
    const slotId = event.slot.getSlotElementId();
    printEventMessage("Creative iframe load event has fired.", slotId);
  });

  // This listener will be called when a slot has finished rendering.
  googletag.pubads().addEventListener("slotRenderEnded", (event) => {
    const slotId = event.slot.getSlotElementId();

    // Record details of the rendered ad.
    const details = {
      "Advertiser ID": event.advertiserId,
      "Campaign ID": event.campaignId,
      "Company IDs": event.companyIds,
      "Creative ID": event.creativeId,
      "Creative Template ID": event.creativeId,
      "Is backfill?": event.isBackfill,
      "Is empty?": event.isEmpty,
      "Line Item ID": event.lineItemId,
      "Response Identifier": event.responseIdentifier,
      Size: typeof event.size === "string" ? event.size : (event.size?.join("x") ?? null),
      "Slot content changed?": event.slotContentChanged,
      "Source Agnostic Creative ID": event.sourceAgnosticCreativeId,
      "Source Agnostic Line Item ID": event.sourceAgnosticLineItemId,
      "Yield Group IDs": event.yieldGroupIds,
    };

    printEventMessage("Slot has finished rendering.", slotId, details);
  });

  // This listener will be called when the specified service actually
  // sets an ad request for a slot. Each slot will fire this event, even
  // though they may be batched together in a single request if single
  // request architecture (SRA) is enabled.
  googletag.pubads().addEventListener("slotRequested", (event) => {
    const slotId = event.slot.getSlotElementId();
    requestedTimestamp[slotId] = Date.now();
    printEventMessage("Slot has been requested.", slotId);
  });

  // This listener will be called when an ad response has been received for
  // a slot.
  googletag.pubads().addEventListener("slotResponseReceived", (event) => {
    const slotId = event.slot.getSlotElementId();
    printEventMessage("Ad response has been received.", slotId);
  });

  // This listener will be called whenever the on-screen percentage of an ad
  // slot's area changes.
  googletag.pubads().addEventListener("slotVisibilityChanged", (event) => {
    const slotId = event.slot.getSlotElementId();

    // Record details of the event.
    const details = { "Visible area": `${event.inViewPercentage}%` };

    printEventMessage("Visibility has changed.", slotId, details);
  });

  // Enable SRA.
  googletag.setConfig({
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();

  // Request and render all previously defined ad slots.
  googletag.display("ad-slot-2");
});

function printEventMessage(
  eventMessage: string,
  slotId: string,
  details: { [key: string]: boolean | number | number[] | string | null } = {},
) {
  const row = document.getElementsByClassName("status-row")[0].cloneNode(true) as HTMLDivElement;

  const cells = row.getElementsByClassName("status-cell");
  cells[0].textContent = slotId;
  cells[1].textContent = eventMessage;
  for (const key in details) {
    if (!details.hasOwnProperty(key) || !details[key]) continue;

    const detailElem = document.createElement("p");
    detailElem.className = "status-detail";
    detailElem.textContent = `${key}: ${details[key]}`;
    cells[1].appendChild(detailElem);
  }
  cells[2].textContent = `${Date.now() - requestedTimestamp[slotId]}ms`;

  document.getElementsByClassName("status-container")[0].appendChild(row);
}
```
