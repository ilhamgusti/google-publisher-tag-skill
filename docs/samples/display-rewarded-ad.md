# Display a rewarded ad

# Display a rewarded ad

This example demonstrates using the Google Publisher Tag (GPT) library to
request and render a rewarded ad. Rewarded ad formats let app and web users
receive rewards for viewing ads. Learn more about rewarded ads in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/9116812).

You can use the following GPT events to display and interact with rewarded ads:

| Event | Fired when... |
|---|---|
| [RewardedSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotclosedevent) | A rewarded ad slot has been closed. |
| [RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotgrantedevent) | A reward has been granted for viewing an ad. |
| [RewardedSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotreadyevent) | A rewarded ad slot is ready to be displayed. |
| [RewardedSlotVideoCompletedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotvideocompletedevent) | A rewarded ad slot has finsihed playing a video. |

For the purpose of this example, a simple modal dialog is used to both prompt
the user to view the rewarded ad and to display the reward upon completion. In
practice, it is the responsibility of the publisher to implement their own
interface to accomplish these tasks.

> [!IMPORTANT]
> **Important:** Before you display a rewarded ad, you must comply with the [policies for ad units that offer rewards](https://support.google.com/admanager/answer/7496282) and obtain user consent.

## Usage notes

- **To ensure an optimal user experience, rewarded ads are only requested on
  pages that properly support the format.** Because of this,
  `defineOutOfPageSlot()` may return `null`; you should check for this case to
  ensure you're not doing any unnecessary work. Currently, rewarded ads are
  only supported on mobile optimized pages where zoom is neutral. Typically
  this means the publisher has `<meta name="viewport"
  content="width=device-width, initial-scale=1">` or similar in the `<head>`
  of the page.

- **Rewarded ads generate their own ad slot.** Unlike other ad types, it's not
  necessary to define a `<div>` for rewarded ads. Rewarded ads automatically
  create and insert their own container into the page when an ad fills.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-rewarded-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-rewarded-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-rewarded-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-rewarded-ad)

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
    <meta name="description" content="Display a GPT-managed rewarded ad." />
    <title>Display a rewarded ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let rewardedSlot;
      let rewardPayload;

      googletag.cmd.push(() => {
        rewardedSlot = googletag.defineOutOfPageSlot(
          "/22639388115/rewarded_web_example",
          googletag.enums.OutOfPageFormat.REWARDED,
        );

        // Slot returns null if the page or device does not support rewarded ads.
        if (rewardedSlot) {
          rewardedSlot.addService(googletag.pubads());

          googletag.pubads().addEventListener("rewardedSlotReady", (event) => {
            updateStatus("Rewarded ad slot is ready.");

            document.getElementById("watchAdButton").onclick = () => {
              event.makeRewardedVisible();
              displayModal();
              updateStatus("Rewarded ad is active.");
            };

            displayModal("reward", "Watch an ad to receive a special reward?");
          });

          googletag.pubads().addEventListener("rewardedSlotVideoCompleted", (event) => {
            updateStatus("Video ad has finished playing.");
          });

          googletag.pubads().addEventListener("rewardedSlotClosed", dismissRewardedAd);

          googletag.pubads().addEventListener("rewardedSlotGranted", (event) => {
            rewardPayload = event.payload;
            updateStatus("Reward granted.");
          });

          googletag.pubads().addEventListener("slotRenderEnded", (event) => {
            if (event.slot === rewardedSlot && event.isEmpty) {
              updateStatus("No ad returned for rewarded ad slot.");
            }
          });

          googletag.enableServices();
          googletag.display(rewardedSlot);
        } else {
          updateStatus("Rewarded ads are not supported on this page.");
        }
      });

      function dismissRewardedAd() {
        if (rewardPayload) {
          // User was granted a reward and closed the ad.
          displayModal(
            "grant",
            `You have been rewarded ${rewardPayload.amount} ${rewardPayload.type}!`,
          );
          rewardPayload = null;
        } else {
          // User closed the ad without getting a reward.
          displayModal();
        }

        updateStatus("Rewarded ad has been closed.");

        if (rewardedSlot) {
          googletag.destroySlots([rewardedSlot]);
        }
      }

      function displayModal(type = "", message = "") {
        const modal = document.getElementById("modal");
        modal.removeAttribute("data-type");

        if (type) {
          document.getElementById("modalMessage").textContent = message;
          modal.setAttribute("data-type", type);
        }
      }

      function updateStatus(message) {
        document.getElementById("status").textContent = message;
      }
    </script>
    <style>
      .modal {
        display: none;
        position: fixed;
        z-index: 1;
        padding-top: 300px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
      }

      .modal[data-type] {
        display: block;
      }

      .modalDialog {
        margin: auto;
        padding: 25px;
        background-color: white;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }

      .grantButtons,
      .rewardButtons {
        display: none;
      }

      .modal[data-type="grant"] .grantButtons,
      .modal[data-type="reward"] .rewardButtons {
        display: block;
      }

      .modal input[type="button"] {
        padding: 0.5rem;
        background: blue;
        border: none;
        border-radius: 4px;
        margin: 4px;
        color: white;
      }
    </style>
  </head>
  <body>
    <h1 id="status"></h1>
    <div id="modal" class="modal">
      <div class="modalDialog">
        <p id="modalMessage"></p>

        <span class="grantButtons">
          <input id="closeButton" type="button" value="Close" />
        </span>

        <span class="rewardButtons">
          <input type="button" id="watchAdButton" value="Yes" />
          <input id="noRewardButton" type="button" value="No" />
        </span>
      </div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Register click event handlers.
        document.getElementById("closeButton").addEventListener("click", dismissRewardedAd);
        document.getElementById("noRewardButton").addEventListener("click", dismissRewardedAd);
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
    <meta name="description" content="Display a GPT-managed rewarded ad." />
    <title>Display a rewarded ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var rewardedSlot;
      var rewardPayload;

      googletag.cmd.push(function () {
        rewardedSlot = googletag.defineOutOfPageSlot(
          "/22639388115/rewarded_web_example",
          googletag.enums.OutOfPageFormat.REWARDED,
        );

        // Slot returns null if the page or device does not support rewarded ads.
        if (rewardedSlot) {
          rewardedSlot.addService(googletag.pubads());

          googletag.pubads().addEventListener("rewardedSlotReady", function (event) {
            updateStatus("Rewarded ad slot is ready.");

            document.getElementById("watchAdButton").onclick = function () {
              event.makeRewardedVisible();
              displayModal();
              updateStatus("Rewarded ad is active.");
            };

            displayModal("reward", "Watch an ad to receive a special reward?");
          });

          googletag.pubads().addEventListener("rewardedSlotVideoCompleted", function (event) {
            updateStatus("Video ad has finished playing.");
          });

          googletag.pubads().addEventListener("rewardedSlotClosed", dismissRewardedAd);

          googletag.pubads().addEventListener("rewardedSlotGranted", function (event) {
            rewardPayload = event.payload;
            updateStatus("Reward granted.");
          });

          googletag.pubads().addEventListener("slotRenderEnded", function (event) {
            if (event.slot === rewardedSlot && event.isEmpty) {
              updateStatus("No ad returned for rewarded ad slot.");
            }
          });

          googletag.enableServices();
          googletag.display(rewardedSlot);
        } else {
          updateStatus("Rewarded ads are not supported on this page.");
        }
      });

      function dismissRewardedAd() {
        if (rewardPayload) {
          // User was granted a reward and closed the ad.
          displayModal(
            "grant",
            "You have been rewarded "
              .concat(rewardPayload.amount, " ")
              .concat(rewardPayload.type, "!"),
          );
          rewardPayload = null;
        } else {
          // User closed the ad without getting a reward.
          displayModal();
        }

        updateStatus("Rewarded ad has been closed.");

        if (rewardedSlot) {
          googletag.destroySlots([rewardedSlot]);
        }
      }

      function displayModal(type, message) {
        if (type === void 0) {
          type = "";
        }
        if (message === void 0) {
          message = "";
        }
        var modal = document.getElementById("modal");
        modal.removeAttribute("data-type");

        if (type) {
          document.getElementById("modalMessage").textContent = message;
          modal.setAttribute("data-type", type);
        }
      }

      function updateStatus(message) {
        document.getElementById("status").textContent = message;
      }
    </script>
    <style>
      .modal {
        display: none;
        position: fixed;
        z-index: 1;
        padding-top: 300px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
      }

      .modal[data-type] {
        display: block;
      }

      .modalDialog {
        margin: auto;
        padding: 25px;
        background-color: white;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }

      .grantButtons,
      .rewardButtons {
        display: none;
      }

      .modal[data-type="grant"] .grantButtons,
      .modal[data-type="reward"] .rewardButtons {
        display: block;
      }

      .modal input[type="button"] {
        padding: 0.5rem;
        background: blue;
        border: none;
        border-radius: 4px;
        margin: 4px;
        color: white;
      }
    </style>
  </head>
  <body>
    <h1 id="status"></h1>
    <div id="modal" class="modal">
      <div class="modalDialog">
        <p id="modalMessage"></p>

        <span class="grantButtons">
          <input id="closeButton" type="button" value="Close" />
        </span>

        <span class="rewardButtons">
          <input type="button" id="watchAdButton" value="Yes" />
          <input id="noRewardButton" type="button" value="No" />
        </span>
      </div>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Register click event handlers.
        document.getElementById("closeButton").addEventListener("click", dismissRewardedAd);
        document.getElementById("noRewardButton").addEventListener("click", dismissRewardedAd);
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
    <meta name="description" content="Display a GPT-managed rewarded ad." />
    <title>Display a rewarded ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .modal {
        display: none;
        position: fixed;
        z-index: 1;
        padding-top: 300px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
      }

      .modal[data-type] {
        display: block;
      }

      .modalDialog {
        margin: auto;
        padding: 25px;
        background-color: white;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }

      .grantButtons,
      .rewardButtons {
        display: none;
      }

      .modal[data-type="grant"] .grantButtons,
      .modal[data-type="reward"] .rewardButtons {
        display: block;
      }

      .modal input[type="button"] {
        padding: 0.5rem;
        background: blue;
        border: none;
        border-radius: 4px;
        margin: 4px;
        color: white;
      }
    </style>
  </head>
  <body>
    <h1 id="status"></h1>
    <div id="modal" class="modal">
      <div class="modalDialog">
        <p id="modalMessage"></p>

        <span class="grantButtons">
          <input id="closeButton" type="button" value="Close" />
        </span>

        <span class="rewardButtons">
          <input type="button" id="watchAdButton" value="Yes" />
          <input id="noRewardButton" type="button" value="No" />
        </span>
      </div>
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

let rewardedSlot: googletag.Slot | null;
let rewardPayload: googletag.RewardedPayload | null;

googletag.cmd.push(() => {
  rewardedSlot = googletag.defineOutOfPageSlot(
    "/22639388115/rewarded_web_example",
    googletag.enums.OutOfPageFormat.REWARDED,
  );

  // Slot returns null if the page or device does not support rewarded ads.
  if (rewardedSlot) {
    rewardedSlot.addService(googletag.pubads());

    googletag.pubads().addEventListener("rewardedSlotReady", (event) => {
      updateStatus("Rewarded ad slot is ready.");

      document.getElementById("watchAdButton")!.onclick = () => {
        event.makeRewardedVisible();
        displayModal();
        updateStatus("Rewarded ad is active.");
      };

      displayModal("reward", "Watch an ad to receive a special reward?");
    });

    googletag.pubads().addEventListener("rewardedSlotVideoCompleted", (event) => {
      updateStatus("Video ad has finished playing.");
    });

    googletag.pubads().addEventListener("rewardedSlotClosed", dismissRewardedAd);

    googletag.pubads().addEventListener("rewardedSlotGranted", (event) => {
      rewardPayload = event.payload;
      updateStatus("Reward granted.");
    });

    googletag.pubads().addEventListener("slotRenderEnded", (event) => {
      if (event.slot === rewardedSlot && event.isEmpty) {
        updateStatus("No ad returned for rewarded ad slot.");
      }
    });

    googletag.enableServices();
    googletag.display(rewardedSlot);
  } else {
    updateStatus("Rewarded ads are not supported on this page.");
  }
});

function dismissRewardedAd() {
  if (rewardPayload) {
    // User was granted a reward and closed the ad.
    displayModal("grant", `You have been rewarded ${rewardPayload.amount} ${rewardPayload.type}!`);
    rewardPayload = null;
  } else {
    // User closed the ad without getting a reward.
    displayModal();
  }

  updateStatus("Rewarded ad has been closed.");

  if (rewardedSlot) {
    googletag.destroySlots([rewardedSlot]);
  }
}

function displayModal(type: string = "", message: string = "") {
  const modal = document.getElementById("modal")!;
  modal.removeAttribute("data-type");

  if (type) {
    document.getElementById("modalMessage")!.textContent = message;
    modal.setAttribute("data-type", type);
  }
}

function updateStatus(message: string) {
  document.getElementById("status")!.textContent = message;
}

// Register click event handlers.
document.getElementById("closeButton")!.addEventListener("click", dismissRewardedAd);
document.getElementById("noRewardButton")!.addEventListener("click", dismissRewardedAd);
```
