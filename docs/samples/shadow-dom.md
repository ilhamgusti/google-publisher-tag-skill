# Display ads in the shadow DOM

# Display ads in the shadow DOM

The [shadow DOM](https://developer.mozilla.org/docs/Web/API/Web_components/Using_shadow_DOM) lets you attach a DOM tree to an element, and have
the internals of that tree isolated from the rest of the page. By default, any
elements created inside of the shadow DOM are inaccessible to JS and CSS running
on the main page.

When the Google Publisher Tag (GPT) library is loaded on the main page, it's
capable of rendering ads into containers within the shadow DOM, if the following
requirements are met:

1. The shadow DOM is attached in [open mode](https://developer.mozilla.org/docs/Web/API/Web_components/Using_shadow_DOM#element.shadowroot_and_the_mode_option).
2. Calls to [`googletag.display()`](https://developers.google.com/publisher-tag/reference#googletag.display) provide a reference to an ad container element, instead of a DOM ID string.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/shadow-dom/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/shadow-dom/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/shadow-dom](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/shadow-dom)

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
    <meta name="description" content="Use GPT to request and render ads in the shadow DOM." />
    <title>Display ads in the shadow DOM</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      let adSlot;

      googletag.cmd.push(() => {
        // Define an ad slot for the "ad-slot" div.
        adSlot = googletag
          .defineSlot("/6355419/Travel/Europe", [300, 250], "ad-slot")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });

      document.addEventListener("DOMContentLoaded", (event) => {
        // Register click handlers.
        document.querySelector("#clear").addEventListener("click", (event) => {
          googletag.cmd.push(() => {
            googletag.pubads().clear([adSlot]);
          });
        });

        document.querySelector("#refresh").addEventListener("click", (event) => {
          googletag.cmd.push(() => {
            googletag.pubads().refresh([adSlot]);
          });
        });
      });
    </script>
    <style>
      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        row-gap: 10px;
      }
    </style>
  </head>
  <body>
    <div id="host"></div>
    <div class="controls">
      <button id="clear">Clear ad</button>
      <button id="refresh">Refresh ad</button>
    </div>
    <script>
      // Attach a shadow DOM to the host element and insert an ad container.
      // Ensure the shadow DOM is in open mode, to allow GPT access.
      const shadow = document.querySelector("#host").attachShadow({ mode: "open" });
      const adContainer = document.createElement("div");
      adContainer.id = "ad-slot";
      adContainer.style.cssText = "height: 250px; width: 300px;";
      shadow.appendChild(adContainer);

      googletag.cmd.push(() => {
        // Locate the ad container in the shadow DOM and display an ad in it.
        const shadowRoot = document.querySelector("#host").shadowRoot;
        googletag.display(shadowRoot.querySelector("#ad-slot"));
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
    <meta name="description" content="Use GPT to request and render ads in the shadow DOM." />
    <title>Display ads in the shadow DOM</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      var adSlot;

      googletag.cmd.push(function () {
        // Define an ad slot for the "ad-slot" div.
        adSlot = googletag
          .defineSlot("/6355419/Travel/Europe", [300, 250], "ad-slot")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });

      document.addEventListener("DOMContentLoaded", function (event) {
        // Register click handlers.
        document.querySelector("#clear").addEventListener("click", function (event) {
          googletag.cmd.push(function () {
            googletag.pubads().clear([adSlot]);
          });
        });

        document.querySelector("#refresh").addEventListener("click", function (event) {
          googletag.cmd.push(function () {
            googletag.pubads().refresh([adSlot]);
          });
        });
      });
    </script>
    <style>
      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        row-gap: 10px;
      }
    </style>
  </head>
  <body>
    <div id="host"></div>
    <div class="controls">
      <button id="clear">Clear ad</button>
      <button id="refresh">Refresh ad</button>
    </div>
    <script>
      // Attach a shadow DOM to the host element and insert an ad container.
      // Ensure the shadow DOM is in open mode, to allow GPT access.
      const shadow = document.querySelector("#host").attachShadow({ mode: "open" });
      const adContainer = document.createElement("div");
      adContainer.id = "ad-slot";
      adContainer.style.cssText = "height: 250px; width: 300px;";
      shadow.appendChild(adContainer);

      googletag.cmd.push(function () {
        // Locate the ad container in the shadow DOM and display an ad in it.
        var shadowRoot = document.querySelector("#host").shadowRoot;
        googletag.display(shadowRoot.querySelector("#ad-slot"));
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
    <meta name="description" content="Use GPT to request and render ads in the shadow DOM." />
    <title>Display ads in the shadow DOM</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        row-gap: 10px;
      }
    </style>
  </head>
  <body>
    <div id="host"></div>
    <div class="controls">
      <button id="clear">Clear ad</button>
      <button id="refresh">Refresh ad</button>
    </div>
    <script>
      // Attach a shadow DOM to the host element and insert an ad container.
      // Ensure the shadow DOM is in open mode, to allow GPT access.
      const shadow = document.querySelector("#host").attachShadow({ mode: "open" });
      const adContainer = document.createElement("div");
      adContainer.id = "ad-slot";
      adContainer.style.cssText = "height: 250px; width: 300px;";
      shadow.appendChild(adContainer);
    </script>
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

let adSlot: googletag.Slot;

googletag.cmd.push(() => {
  // Define an ad slot for the "ad-slot" div.
  adSlot = googletag
    .defineSlot("/6355419/Travel/Europe", [300, 250], "ad-slot")!
    .addService(googletag.pubads());

  // Enable the PubAdsService.
  googletag.enableServices();

  // Locate the ad container in the shadow DOM and display an ad in it.
  const shadowRoot = document.querySelector("#host")!.shadowRoot!;
  googletag.display(shadowRoot.querySelector("#ad-slot")!);
});

document.addEventListener("DOMContentLoaded", (event) => {
  // Register click handlers.
  document.querySelector("#clear")!.addEventListener("click", (event) => {
    googletag.cmd.push(() => {
      googletag.pubads().clear([adSlot]);
    });
  });

  document.querySelector("#refresh")!.addEventListener("click", (event) => {
    googletag.cmd.push(() => {
      googletag.pubads().refresh([adSlot]);
    });
  });
});
```
