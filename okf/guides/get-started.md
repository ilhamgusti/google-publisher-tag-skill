---
type: Guide
title: "Get Started with Google Publisher Tag"
description: "Quick start guide to displaying test ads and initializing GPT."
resource: "https://developers.google.com/publisher-tag/guides/get-started"
tags: [gpt, getting-started, test-ad, basics]
timestamp: 2026-09-10T00:00:00Z
---

# Get Started with Google Publisher Tag

The Google Publisher Tag (GPT) is an ad tagging library for
Google Ad Manager.

You can use GPT to dynamically build ad requests.
GPT takes key details like the ad unit code, ad size, and
custom targeting, builds the request, and displays the ad on web pages.

For more details on GPT, see the
[Ad Manager help center](https://support.google.com/admanager/answer/181073).

Here are some samples you can use to get started with GPT. If
you need more help with GPT, see the [support
options](https://developers.google.com/publisher-tag/support/feedback-questions).

## Display a test ad

The following example walks you through creating a test page that
uses GPT to load a generic ad from Google's test network.

Full code for this example can be found on the
[display a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad) sample page.

1. Create a basic HTML document

   In a text editor, create a basic HTML document called `hello-gpt.html`.

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <meta name="description" content="Display a fixed-sized test ad." />
       <title>Display a test ad</title>
       <style></style>
     </head>
     <body>
     </body>
   </html>
   ```
2. Load the GPT library

   Load the GPT library by adding the following to the
   `<head>` of the HTML document.

   This code loads the GPT library from
   <https://securepubads.g.doubleclick.net/tag/js/gpt.js>. Once the library has
   fully loaded, it processes any queued commands in the
   [`googletag`](https://developers.google.com/publisher-tag/reference#googletag) object.

   > [!IMPORTANT]
   > **Important:** Only [load GPT from a Google domain](https://developers.google.com/publisher-tag/guides/general-best-practices#load_from_an_official_source).

   ```html
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
     <style></style>
   </head>
   ```
3. Define an ad slot

   Define an ad slot and initialize GPT using the
   [`googletag.enableServices()`](https://developers.google.com/publisher-tag/reference#googletag.enableServices) method.

   This code first ensures the googletag object is available, then queues a
   command which constructs an ad slot and enables GPT.

   The ad slot in this example will load an ad of size `300x250` from the ad
   unit specified by path `/6355419/Travel/Europe/France/Paris`. The ad will be
   displayed in a `<div id="banner-ad">` element in the body of the page, which
   will be added next.

   <br />

   > [!IMPORTANT]
   > Ad unit path follows the format `/network-code/[parent-ad-unit-code/.../]ad-unit-code`, where:
   >
   > <br />
   >
   > - <var translate="no">network-code</var> is a [unique identifier](https://support.google.com/admanager/answer/7674889#network-code) for the Ad Manager network the ad unit belongs to
   > - <var translate="no">parent-ad-unit-code</var> are the codes of all parent ad units (only applies to non-top level ad units)
   > - <var translate="no">ad-unit-code</var> is the code for the ad unit to be displayed
   >
   > Note that all ad unit codes included in the ad unit path must adhere to the
   > [formatting rules](https://support.google.com/admanager/answer/1628457#ad-unit-codes) specified by
   > Ad Manager.

   <br />

   ```html
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
   ```
4. Specify where the ad will appear

   Specify where the ad will appear on the page by adding the following code to
   the `<body>` of the HTML document.

   Note that the ID of this `<div>` matches the ID specified when defining the
   ad slot.

   ```html
   <body>
     <div id="banner-ad" style="width: 300px; height: 250px"></div>
     <script>
       googletag.cmd.push(() => {
         // Request and render an ad for the "banner-ad" slot.
         googletag.display("banner-ad");
       });
     </script>
   </body>
   ```
5. Preview the test page

   Save the `hello-gpt.html` file and open it in a web browser. Once loaded,
   the page will display a test ad in the body of the web page.

   > [!CAUTION]
   > **Caution:** If you don't see an ad, ensure that the div ID specified in the `<head>` of the page matches the ID of the `<div>` element you added to the `<body>` of the page.

## Display your own ad

To display your own ad, use the `hello-gpt.html` file from [Display a test
ad](https://developers.google.com/publisher-tag/guides/get-started#generic-ad), then replace the code in the header with code specifying
inventory from your own Ad Manager network.

> [!NOTE]
> **Note:** Before you can display an ad from your Ad Manager network, you need to make sure there's an active line item already trafficked in the "Ready" status. Learn more about creating line items in the [Ad Manager help center](https://support.google.com/admanager/answer/82236).

1. Generate an ad tag for the ad unit you'd like to display. Learn more about
   generating ad tags in the
   [Ad Manager help center](https://support.google.com/admanager/answer/177207).

2. Copy the ad tag code provided in the **Document header** section and use it
   to replace the corresponding code in the `<head>` of your HTML document.

   > [!CAUTION]
   > **Caution:** ensure that the width, height, and ID of the `<div>` declared in the body of the page matches the width, height, and ID of the ad slot defined in the ad tag code.

       <head>
         <meta charset="utf-8">
         <title>Hello GPT</title>
         <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
         \<script\>
       window.googletag = window.googletag \|\| {cmd: \[\]};
       googletag.cmd.push(function() {
       googletag
       .defineSlot("ad-unit-path", \[width, height\], "div-id")
       .addService(googletag.pubads());
       googletag.enableServices();
       });
       \</script\>
       </head>

3. Save the updated `hello-gpt.html` file and open it in a web browser.