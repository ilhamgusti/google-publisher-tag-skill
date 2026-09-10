# Display a test ad

# Display a test ad

This example displays a test ad using the Google Publisher Tag library. See
[Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started) to learn more about how
this sample works.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/display-test-ad/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/display-test-ad/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-test-ad](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/display-test-ad)

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
    <meta name="description" content="Display a fixed-sized test ad." />
    <title>Display a test ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(() => {
        // Define an ad slot for div with id "banner-ad".
        googletag
          .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "banner-ad")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="banner-ad" style="width: 300px; height: 250px"></div>
    <script>
      googletag.cmd.push(() => {
        // Request and render an ad for the "banner-ad" slot.
        googletag.display("banner-ad");
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
    <meta name="description" content="Display a fixed-sized test ad." />
    <title>Display a test ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      window.googletag = window.googletag || { cmd: [] };

      googletag.cmd.push(function () {
        // Define an ad slot for div with id "banner-ad".
        googletag
          .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "banner-ad")
          .addService(googletag.pubads());

        // Enable the PubAdsService.
        googletag.enableServices();
      });
    </script>
    <style></style>
  </head>
  <body>
    <div id="banner-ad" style="width: 300px; height: 250px"></div>
    <script>
      googletag.cmd.push(function () {
        // Request and render an ad for the "banner-ad" slot.
        googletag.display("banner-ad");
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
    <meta name="description" content="Display a fixed-sized test ad." />
    <title>Display a test ad</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style></style>
  </head>
  <body>
    <div id="banner-ad" style="width: 300px; height: 250px"></div>
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
  // Define an ad slot for div with id "banner-ad".
  googletag
    .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "banner-ad")!
    .addService(googletag.pubads());

  // Enable the PubAdsService.
  googletag.enableServices();

  // Request and render an ad for the "banner-ad" slot.
  googletag.display("banner-ad");
});
```
