# Display an H5 gaming interstitial ad

# Display an H5 gaming interstitial ad

> [!IMPORTANT]
> **Important:** Gaming interstitial ads are a limited-access format. For more information, see [Display an H5 gaming interstitial ad](https://support.google.com/admanager/answer/14640119).

This example displays a gaming interstitial ad using the Google Publisher Tag
(GPT) library. Gaming interstitials are GPT-managed, full-page ads that you
display to users playing web-based games based on a manual trigger. For more
information about gaming interstitials, see
[Display an H5 gaming interstitial ad](https://support.google.com/admanager/answer/14640119).

To display and interact with gaming interstitial ads, use the following GPT
events:

| Event | Fired when... |
|---|---|
| [`GamingInterstitialSlotReady`](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent) | A gaming interstitial ad is ready to display to the user. To display the interstitial, call [`makeGameManualInterstitialVisible()`](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent.makeGameManualInterstitialVisible) on the provided event object. |
| [`GamingInterstitialSlotClosed`](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent) | The user closed a previously displayed gaming interstitial ad. Use this event to run custom logic whenever a gaming interstitial is closed. |

## Game structures

Gaming interstitial ads can display either fullscreen or inside the frame of
your game, depending on how your game is structured. For more details, see
[H5 Game structures](https://support.google.com/admanager/answer/14637831#h5-game-structures).

The sample implementation assumes that the H5 game renders directly into the
top-most window, using the **Fullscreen** structure. In this scenario, the
gaming interstitial ad also renders fullscreen.

However, this same code also works when placed inside of a child frame, using
the **iFrame/WebView** structure. To constrain the gaming interstitial ad to the
H5 game canvas, place the game in an iFrame, as shown in the following example:

    <!doctype html>
    <html>
      <head>
        <!-- The Google Publisher Tag here, if any, will only be responsible for serving ads outside of the H5 game. -->
        <title>Page for this example H5 game</title>
        <!-- Your <head> content here. -->
      </head>
      <body>
        <span id="example-text">Example H5 game</span>

        <!-- Sample code is served here. The Google Publisher Tag loaded in this frame will only be used within the H5 game. -->
        <iframe src="https://www.example.com" title="Example game" allow="autoplay"></iframe>
      </body>
    </html>

## Usage notes

- **To ensure an optimal user experience, GPT only requests gaming
  interstitial ads on pages that properly support the format.** Due to this
  restriction, `defineOutOfPageSlot()` may return null. You must check for
  this case to ensure you're not doing any unnecessary work.

- **Only request gaming interstitial ads on pages or environments where you
  want an interstitial to appear.** Gaming interstitial ads are eligible to
  serve to desktop, tablet, and mobile devices.

  > [!NOTE]
  > **Note:** You can use Chrome DevTools mobile simulation to test gaming interstitial ads on mobile from a desktop environment.

- **Gaming interstitial ads generate their own ad slot.** Unlike other ad
  types, it's not necessary to define a `<div>` for gaming interstitial ads.
  These ads automatically create and insert their own container into the page
  when an ad fills.

- **Gaming interstitial ads are one-time use.** You cannot refresh a gaming
  interstitial ad slot. Instead, you must destroy the slot and re-create it,
  as shown in the sample implementation.

- **Gaming interstitial ads have a fixed frequency cap.** The frequency cap
  prevents the `gamingInterstitialSlotReady` event from firing more than once
  every 30 seconds.

- **If using single-request architecture (SRA) on a page with multiple slots,
  don't call `display()` until static ad slots divs are created.** As
  explained in [Ads Best Practices](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly), the first call to `display()`
  requests every ad slot defined before that point. Although gaming
  interstitial slots don't require a predefined `<div>`, static ad slots do.
  Calling `display()` before these elements are present on the page can result
  in lower quality signals. We recommend delaying the initial call until after
  static slots are defined.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-gaming-interstitial-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-gaming-interstitial-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-gaming-interstitial-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-gaming-interstitial-ad)

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
    <meta name="description" content="Display a GPT-managed gaming interstitial ad." />
    <title>Display an H5 gaming interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let gamingInterstitialSlot;

      googletag.cmd.push(() => {
        // Define a gaming interstitial ad slot.
        defineGamingInterstitialSlot();

        // Add gaming interstitial event listeners.
        addGamingInterstitialListeners();

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

      function defineGamingInterstitialSlot() {
        document.getElementById("trigger").style.display = "none";

        gamingInterstitialSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe/France/Paris",
          googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
        );

        // Slot returns null if the page or device does not support interstitials.
        if (gamingInterstitialSlot) {
          gamingInterstitialSlot.addService(googletag.pubads());
          printStatus("Waiting for interstitial to be ready...");
          return true;
        } else {
          printStatus("This device does not support interstitials.");
          return false;
        }
      }

      function addGamingInterstitialListeners() {
        // Add event listener to register click handler once interstitial loads.
        // If this event doesn't fire, check the browser console for errors.
        googletag.pubads().addEventListener("gameManualInterstitialSlotReady", (slotReadyEvent) => {
          if (gamingInterstitialSlot === slotReadyEvent.slot) {
            printStatus("Interstitial is ready.");

            const button = document.getElementById("trigger");
            button.style.display = "block";
            button.addEventListener(
              "click",
              () => {
                pauseGame();

                slotReadyEvent.makeGameManualInterstitialVisible();
                printStatus("Interstitial is active.");
              },
              { once: true },
            );
          }
        });

        googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", () => {
          // Gaming interstitial ad slots are one-time use, so destroy the old slot
          // and create a new one.
          if (gamingInterstitialSlot) {
            googletag.destroySlots([gamingInterstitialSlot]);
          }

          if (defineGamingInterstitialSlot()) {
            googletag.display(gamingInterstitialSlot);
          }

          resumeGame();
        });
      }

      function pauseGame() {
        // Code to pause the game.
      }

      function resumeGame() {
        // Code to resume the game.
      }

      function printStatus(status) {
        document.getElementById("status").innerText = status;
      }
    </script>
    <style>
      button {
        display: none;
      }

      div.content {
        position: fixed;
        top: 50%;
      }
    </style>
  </head>
  <body>
    <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    <div class="content">
      <span id="status">Gaming interstitial is not supported on this page.</span>
      <p>
        <button id="trigger">TRIGGER INTERSTITIAL</button>
      </p>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        if (gamingInterstitialSlot) {
          googletag.display(gamingInterstitialSlot);
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
    <meta name="description" content="Display a GPT-managed gaming interstitial ad." />
    <title>Display an H5 gaming interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var gamingInterstitialSlot;

      googletag.cmd.push(function () {
        // Define a gaming interstitial ad slot.
        defineGamingInterstitialSlot();

        // Add gaming interstitial event listeners.
        addGamingInterstitialListeners();

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

      function defineGamingInterstitialSlot() {
        document.getElementById("trigger").style.display = "none";

        gamingInterstitialSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe/France/Paris",
          googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
        );

        // Slot returns null if the page or device does not support interstitials.
        if (gamingInterstitialSlot) {
          gamingInterstitialSlot.addService(googletag.pubads());
          printStatus("Waiting for interstitial to be ready...");
          return true;
        } else {
          printStatus("This device does not support interstitials.");
          return false;
        }
      }

      function addGamingInterstitialListeners() {
        // Add event listener to register click handler once interstitial loads.
        // If this event doesn't fire, check the browser console for errors.
        googletag
          .pubads()
          .addEventListener("gameManualInterstitialSlotReady", function (slotReadyEvent) {
            if (gamingInterstitialSlot === slotReadyEvent.slot) {
              printStatus("Interstitial is ready.");

              var button = document.getElementById("trigger");
              button.style.display = "block";
              button.addEventListener(
                "click",
                function () {
                  pauseGame();

                  slotReadyEvent.makeGameManualInterstitialVisible();
                  printStatus("Interstitial is active.");
                },
                { once: true },
              );
            }
          });

        googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", function () {
          // Gaming interstitial ad slots are one-time use, so destroy the old slot
          // and create a new one.
          if (gamingInterstitialSlot) {
            googletag.destroySlots([gamingInterstitialSlot]);
          }

          if (defineGamingInterstitialSlot()) {
            googletag.display(gamingInterstitialSlot);
          }

          resumeGame();
        });
      }

      function pauseGame() {
        // Code to pause the game.
      }

      function resumeGame() {
        // Code to resume the game.
      }

      function printStatus(status) {
        document.getElementById("status").innerText = status;
      }
    </script>
    <style>
      button {
        display: none;
      }

      div.content {
        position: fixed;
        top: 50%;
      }
    </style>
  </head>
  <body>
    <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    <div class="content">
      <span id="status">Gaming interstitial is not supported on this page.</span>
      <p>
        <button id="trigger">TRIGGER INTERSTITIAL</button>
      </p>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        if (gamingInterstitialSlot) {
          googletag.display(gamingInterstitialSlot);
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
    <meta name="description" content="Display a GPT-managed gaming interstitial ad." />
    <title>Display an H5 gaming interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      button {
        display: none;
      }

      div.content {
        position: fixed;
        top: 50%;
      }
    </style>
  </head>
  <body>
    <div id="static-ad-1" style="width: 100px; height: 100px"></div>
    <div class="content">
      <span id="status">Gaming interstitial is not supported on this page.</span>
      <p>
        <button id="trigger">TRIGGER INTERSTITIAL</button>
      </p>
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

let gamingInterstitialSlot: googletag.Slot | null;

googletag.cmd.push(() => {
  // Define a gaming interstitial ad slot.
  defineGamingInterstitialSlot();

  // Add gaming interstitial event listeners.
  addGamingInterstitialListeners();

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
  if (gamingInterstitialSlot) {
    googletag.display(gamingInterstitialSlot);
  }
});

function defineGamingInterstitialSlot(): boolean {
  document.getElementById("trigger")!.style.display = "none";

  gamingInterstitialSlot = googletag.defineOutOfPageSlot(
    "/6355419/Travel/Europe/France/Paris",
    googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
  );

  // Slot returns null if the page or device does not support interstitials.
  if (gamingInterstitialSlot) {
    gamingInterstitialSlot.addService(googletag.pubads());
    printStatus("Waiting for interstitial to be ready...");
    return true;
  } else {
    printStatus("This device does not support interstitials.");
    return false;
  }
}

function addGamingInterstitialListeners() {
  // Add event listener to register click handler once interstitial loads.
  // If this event doesn't fire, check the browser console for errors.
  googletag
    .pubads()
    .addEventListener(
      "gameManualInterstitialSlotReady",
      (slotReadyEvent: googletag.events.GameManualInterstitialSlotReadyEvent) => {
        if (gamingInterstitialSlot === slotReadyEvent.slot) {
          printStatus("Interstitial is ready.");

          const button = document.getElementById("trigger")!;
          button.style.display = "block";
          button.addEventListener(
            "click",
            () => {
              pauseGame();

              slotReadyEvent.makeGameManualInterstitialVisible();
              printStatus("Interstitial is active.");
            },
            { once: true },
          );
        }
      },
    );

  googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", () => {
    // Gaming interstitial ad slots are one-time use, so destroy the old slot
    // and create a new one.
    if (gamingInterstitialSlot) {
      googletag.destroySlots([gamingInterstitialSlot]);
    }

    if (defineGamingInterstitialSlot()) {
      googletag.display(gamingInterstitialSlot!);
    }

    resumeGame();
  });
}

function pauseGame() {
  // Code to pause the game.
}

function resumeGame() {
  // Code to resume the game.
}

function printStatus(status: string) {
  document.getElementById("status")!.innerText = status;
}
```
