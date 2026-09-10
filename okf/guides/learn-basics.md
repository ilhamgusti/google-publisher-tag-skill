---
type: Guide
title: "Learn Basic GPT Concepts"
description: "Fundamental concepts of GPT including ad slots, services, targeting, and lifecycle."
resource: "https://developers.google.com/publisher-tag/guides/learn-basics"
tags: [gpt, basics, lifecycle, architecture]
timestamp: 2026-09-10T00:00:00Z
---

The following guide expands on [displaying a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad),
and introduces more basic concepts to make the most of the
Google Publisher Tag (GPT) library. These concepts include:

- Ad sizing
- Key-value targeting
- Single request architecture

## Load the GPT library

Start by loading and initializing the GPT library. Add the
following to the `<head>` of the HTML document:

```html
<script
  async
  src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
  crossorigin="anonymous"
></script>
<script>
  window.googletag = window.googletag || { cmd: [] };

  googletag.cmd.push(() => {

  });
</script>
```

This loads the GPT library and initializes both the `googletag`
and `CommandArray` objects. Initializing these objects lets you start
using the [GPT command array](https://developers.google.com/publisher-tag/reference#googletag.commandarray) immediately. Add the
JavaScript code that follows to the body of the empty function defined in this
snippet.

## Define ad slots

After loading GPT, you can define ad slots. The following
example defines three ad slots with different ad formats, sizing, and
targeting options.

### Fixed-size ad slot

Here's a simple, fixed-size ad slot:

```javascript
// Define a fixed size ad slot, customized with key-value targeting.
googletag
  .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad")
  .addService(googletag.pubads())
  .setConfig({
    targeting: {
      color: "red",
      position: "atf",
    },
  });
```

In addition to the ad unit path, size, and container `<div>` ID, this
snippet also specifies a number of targeting options. These options restrict and
differentiate the ads that are eligible to serve to this slot. Learn more about
[key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting).

> [!TIP]
> **Tip:** Try removing these targeting options one-by-one to see how the ad slot behaves.

### Anchor ad slot

Here's an anchor ad slot, attached to the bottom of the viewport:

```javascript
// Define an anchor ad slot that sticks to the bottom of the viewport.
const anchorSlot = googletag.defineOutOfPageSlot(
  "/6355419/Travel",
  googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR,
);

// The slot will be null if the page or device does not support anchors.
if (anchorSlot) {
  anchorSlot.setTargeting("test", "anchor").addService(googletag.pubads());

  document.getElementById("status").textContent =
    "Anchor ad is initialized. Scroll page to activate.";
}
```

Anchor slots are a type of out-of-page format, which are defined
using the [`defineOutOfPageSlot`](https://developers.google.com/publisher-tag/reference#googletag.defineOutOfPageSlot) method, rather than the usual
`defineSlot` method. Learn more about [out-of-page creatives](https://support.google.com/admanager/answer/6088046).

Out-of-page formats often have restrictions on the sorts of pages and
devices they're eligible to serve to. Due to these restrictions, you must
verify that the slot is successfully defined before interacting with it. See
the [Display an anchor ad](https://developers.google.com/publisher-tag/samples/display-anchor-ad) sample for details.

### Fluid ad slot

Here's a fluid ad slot for a native ad:

```javascript
// Define a fluid ad slot that fills the width of the enclosing column and
// adjusts the height as defined by the native creative delivered.
googletag
  .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
  .addService(googletag.pubads());
```

Fluid ad slots don't have a fixed size. Fluid ad slots adjust to fit the
creative content from the ad. You define fluid ad slots with the `fluid` size
option. Learn more about
[ad sizing and the available sizing options](https://developers.google.com/publisher-tag/guides/ad-sizes).

## Configure page-level settings

Certain GPT configuration options apply globally, rather than
to specific ad slots. These are referred to as page-level settings.

Here's an example of how to configure page-level settings:

```javascript
// Configure page-level targeting and enable SRA.
googletag.setConfig({
  targeting: {
    interests: "basketball",
  },
  singleRequest: true,
});

// Enable services.
googletag.enableServices();
```

This snippet does three things:

1. Configures [page-level targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting#set_targeting) options, which are applied to every ad slot on the page.
2. Turns on Single Request Architecture (SRA) mode, which bundles requests for multiple ad slots into a single ad request. SRA improves performance, and is necessary to guarantee that competitive exclusions and roadblocks are honored, so we recommend that you always turn on SRA. Learn more about [using SRA correctly](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly).
3. Enables the services attached to our ad slots that allow ad requests to be made.

## Display ads

Finally, add the following snippet to the `<body>` of the page:

```html
<div class="page-content centered">
  <div id="banner-ad" style="width: 728px; height: 90px"></div>
  <!--
  If the following status is displayed when the page is rendered, try
  loading the page in a new window or on a different device.
-->
  <h1 id="status">Anchor ads are not supported on this page.</h1>
  <!--
  Spacer used for example purposes only. This positions the native ad
  container below the fold to encourage scrolling.
-->
  <div class="spacer"></div>
  <div id="native-ad" class="native-slot"></div>
</div>
<script>
  googletag.cmd.push(() => {
    // Request and render all previously defined ad slots.
    googletag.display("banner-ad");
  });
</script>
```

This defines two ad slot containers: `banner-ad` and `native-ad`. These
container `id` values correspond to the values you provided when you defined the
ad slots earlier in this example.

> [!NOTE]
> **Note:** No container is defined for the anchor ad slot. The anchor ad format automatically creates and inserts its own container into the page.

After all ad slots are defined, a call to display the `banner-ad` is made. Since
SRA is enabled, this single display call requests and renders all ad slots
defined up to this point. If necessary, you can more precisely
[control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading) and
[batching behavior](https://developers.google.com/publisher-tag/samples/control-sra-batching) with SRA enabled.

## Complete example

The following is the full source code for the sample page this guide is based
on. You can also view an [interactive demo of this page](https://googleads.github.io/google-publisher-tag-samples/basic-concepts/js/demo.html).

### JavaScript

<iframe src="https://developers.devsite.google/frame/publisher-tag/guides/learn-basics_3c93339904f5a98c39ae4775173aa0bb53a8b355c01c2f64507108dd3ed3334d.frame" class="framebox inherit-locale " allow="clipboard-write https://developers.devsite.google" allowfullscreen is-upgraded></iframe>

### TypeScript

<iframe src="https://developers.devsite.google/frame/publisher-tag/guides/learn-basics_b384c1c7b6d89daaa76abcc36a355582dec1ebec1db3dea7b9edf1cc343f5f11.frame" class="framebox inherit-locale " allow="clipboard-write https://developers.devsite.google" allowfullscreen is-upgraded></iframe>