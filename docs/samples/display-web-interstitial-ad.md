# Display a web interstitial ad

This example demonstrates how to display a web interstitial ad using the Google
Publisher Tag (GPT) library. Web interstitials are GPT-managed, full-page ads
that appear in response to user actions. For more information about web
interstitials, see [Traffic web interstitials](https://support.google.com/admanager/answer/9840201).

The following user actions are eligible to trigger a web interstitial ad:

| User action | [API name](https://developers.google.com/publisher-tag/reference#googletag.config.interstitialconfig) | Default | Configurable |
|---|---|---|---|
| Clicking on an anchor element. | N/A | Enabled | No |
| Scrolling to the end of the page's main `<article>` element. | `endOfArticle` | Disabled | Yes |
| Clicking, scrolling, or typing after being inactive for at least 30 seconds. | `inactivity` | Disabled | Yes |
| Clicking on the browser navigation bar. (Desktop only) | `navBar` | Disabled | Yes |
| Hiding and then returning to the page (for example, by switching tabs). | `unhideWindow` | Disabled | Yes |
| Clicking a GPT-created **View ad to continue** button. | `continueReading` | Disabled | Yes |

> [!IMPORTANT]
> **Important:** Default trigger states are [configurable in Google Ad Manager](https://support.google.com/admanager/answer/9840201). If these values have been modified for your Ad Manager account, they may not match the preceding table.

Support for additional user actions may be added in the future. Follow the
[GPT release notes](https://developers.google.com/publisher-tag/release-notes) for updates.

## Usage notes

- **To ensure an optimal user experience, GPT only requests web interstitial
  ads on pages that properly support the format.** Web interstitials are only
  supported when GPT is running in the top window. On pages that don't support
  web interstitials, `defineOutOfPageSlot()` may return null. Be sure to check
  for this to avoid errors.

- **Only request web interstitial ads on pages or environments where you want
  an interstitial to appear.** Web interstitial ads are eligible to serve to
  desktop, tablet, and mobile devices.

  > [!TIP]
  > **Tip:** For best results, use `<meta name="viewport" content="width=device-width, initial-scale=1" />` on mobile pages, or avoid setting fixed widths and heights on your document, as that can result in poorly scaled interstitial ads.

- **Web interstitial ads generate their own ad slot.** Unlike other ad types,
  you don't need to define a `<div>` for web interstitial ads. These ads
  automatically create and insert their own container into the page when an ad
  fills.

- **Web interstitial ads have a configurable
  [frequency cap](https://support.google.com/admanager/answer/9840201#frequency).** This prevents the same user from
  being shown an interstitial more than once per the specified window of time,
  per subdomain. The default frequency cap is 1 impression per 10 minutes, and
  the minimum allowed cap is 1 impression per 1 minute.

- **Web interstitial ads require access to local storage.** For publishers
  integrated with the
  [IAB Transparency and Consent Framework v2.0](https://support.google.com/admanager/answer/9805023), this means
  that consent for [Purpose 1](https://support.google.com/admanager/answer/9461778#purposes) is required for web
  interstitial ads to function.

- **Some links on a page might be ineligible to show web interstitial ads.**
  Interstitial ads won't show when a user clicks an ineligible link, for
  example, links to URLs without HTTP/HTTPS, and links that open in a new
  window.

  > [!NOTE]
  > **Note:** You can prevent specific links from triggering GPT-managed web interstitials by adding a `data-google-interstitial="false"` attribute to the anchor element or any ancestor of the anchor element.

- **If using single-request architecture (SRA) on a page with multiple slots,
  don't call `display()` until static ad slots divs are created.** As
  explained in [Ad Best Practices](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly), the first call to `display()`
  requests every ad slot defined prior to that point. Although web
  interstitial slots don't require a predefined `<div>`, static ad slots do.
  Calling `display()` before these elements are present on the page can result
  in lower quality signals, reducing monetization. Because of this, we
  recommend delaying the initial call until after the static slots are
  defined.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-web-interstitial-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-web-interstitial-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-web-interstitial-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-web-interstitial-ad)

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
    <meta name="description" content="Display a GPT-managed web interstitial ad." />
    <title>Display a web interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let interstitialSlot;

      googletag.cmd.push(() => {
        // Define a web interstitial ad slot.
        interstitialSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe/France/Paris",
          googletag.enums.OutOfPageFormat.INTERSTITIAL,
        );

        // Slot returns null if the page or device does not support interstitials.
        if (interstitialSlot) {
          // Enable optional interstitial triggers and register the slot.
          interstitialSlot.addService(googletag.pubads()).setConfig({
            interstitial: {
              triggers: {
                navBar: true,
                unhideWindow: true,
              },
            },
          });

          document.getElementById("status").textContent = "Interstitial is loading...";

          // Add event listener to enable navigation once the interstitial loads.
          // If this event doesn't fire, try clearing local storage and refreshing
          // the page.
          googletag.pubads().addEventListener("slotOnload", (event) => {
            if (interstitialSlot === event.slot) {
              document.getElementById("link").style.display = "block";
              document.getElementById("status").textContent = "Interstitial is loaded.";
            }
          });

          // By default, the detected language of the current page is used to render
          // interstitial UI elements. This behavior can be overridden by manually
          // specifying the document language:
          // googletag.pubads().set("document_language", "en");
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
      #link {
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
      <span id="status">Web interstitial is not supported on this page.</span>
      <p>
        <a id="link" href="https://www.example.com/">TRIGGER INTERSTITIAL</a>
      </p>
      <p>
        <!--
          You can prevent specific links from triggering GPT-managed web
          interstials by adding a data-google-interstitial="false" attribute to
          the anchor element or any ancestor of the anchor element.
        -->
        <a data-google-interstitial="false" href="https://www.example.com/">
          This link will never trigger an interstitial
        </a>
      </p>
    </div>
    <script>
      googletag.cmd.push(() => {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        googletag.display(interstitialSlot);
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
    <meta name="description" content="Display a GPT-managed web interstitial ad." />
    <title>Display a web interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var interstitialSlot;

      googletag.cmd.push(function () {
        // Define a web interstitial ad slot.
        interstitialSlot = googletag.defineOutOfPageSlot(
          "/6355419/Travel/Europe/France/Paris",
          googletag.enums.OutOfPageFormat.INTERSTITIAL,
        );

        // Slot returns null if the page or device does not support interstitials.
        if (interstitialSlot) {
          // Enable optional interstitial triggers and register the slot.
          interstitialSlot.addService(googletag.pubads()).setConfig({
            interstitial: {
              triggers: {
                navBar: true,
                unhideWindow: true,
              },
            },
          });

          document.getElementById("status").textContent = "Interstitial is loading...";

          // Add event listener to enable navigation once the interstitial loads.
          // If this event doesn't fire, try clearing local storage and refreshing
          // the page.
          googletag.pubads().addEventListener("slotOnload", function (event) {
            if (interstitialSlot === event.slot) {
              document.getElementById("link").style.display = "block";
              document.getElementById("status").textContent = "Interstitial is loaded.";
            }
          });

          // By default, the detected language of the current page is used to render
          // interstitial UI elements. This behavior can be overridden by manually
          // specifying the document language:
          // googletag.pubads().set("document_language", "en");
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
      #link {
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
      <span id="status">Web interstitial is not supported on this page.</span>
      <p>
        <a id="link" href="https://www.example.com/">TRIGGER INTERSTITIAL</a>
      </p>
      <p>
        <!--
          You can prevent specific links from triggering GPT-managed web
          interstials by adding a data-google-interstitial="false" attribute to
          the anchor element or any ancestor of the anchor element.
        -->
        <a data-google-interstitial="false" href="https://www.example.com/">
          This link will never trigger an interstitial
        </a>
      </p>
    </div>
    <script>
      googletag.cmd.push(function () {
        // Ensure the first call to display comes after static ad slot
        // divs are defined. If you do not have any static ad slots, this
        // call can be made immediately after services are enabled.
        googletag.display(interstitialSlot);
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
    <meta name="description" content="Display a GPT-managed web interstitial ad." />
    <title>Display a web interstitial ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      #link {
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
      <span id="status">Web interstitial is not supported on this page.</span>
      <p>
        <a id="link" href="https://www.example.com/">TRIGGER INTERSTITIAL</a>
      </p>
      <p>
        <!--
          You can prevent specific links from triggering GPT-managed web
          interstials by adding a data-google-interstitial="false" attribute to
          the anchor element or any ancestor of the anchor element.
        -->
        <a data-google-interstitial="false" href="https://www.example.com/">
          This link will never trigger an interstitial
        </a>
      </p>
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

let interstitialSlot: googletag.Slot | null;

googletag.cmd.push(() => {
  // Define a web interstitial ad slot.
  interstitialSlot = googletag.defineOutOfPageSlot(
    "/6355419/Travel/Europe/France/Paris",
    googletag.enums.OutOfPageFormat.INTERSTITIAL,
  );

  // Slot returns null if the page or device does not support interstitials.
  if (interstitialSlot) {
    // Enable optional interstitial triggers and register the slot.
    interstitialSlot.addService(googletag.pubads()).setConfig({
      interstitial: {
        triggers: {
          navBar: true,
          unhideWindow: true,
        },
      },
    });

    document.getElementById("status")!.textContent = "Interstitial is loading...";

    // Add event listener to enable navigation once the interstitial loads.
    // If this event doesn't fire, try clearing local storage and refreshing
    // the page.
    googletag.pubads().addEventListener("slotOnload", (event) => {
      if (interstitialSlot === event.slot) {
        document.getElementById("link")!.style.display = "block";
        document.getElementById("status")!.textContent = "Interstitial is loaded.";
      }
    });

    // By default, the detected language of the current page is used to render
    // interstitial UI elements. This behavior can be overridden by manually
    // specifying the document language:
    // googletag.pubads().set("document_language", "en");
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
  googletag.display(interstitialSlot!);
});
```
