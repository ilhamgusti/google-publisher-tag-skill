---
type: Guide
title: "Control Ad Loading and Refresh"
description: "Managing ad request batching, initial load, and refresh behavior."
resource: "https://developers.google.com/publisher-tag/guides/control-ad-loading"
tags: [gpt, loading, refresh, sra]
timestamp: 2026-09-10T00:00:00Z
---

# Control ad loading and refresh

In our getting started and basic concept examples, the Google Publisher Tag
(GPT) library's [`display()`](https://developers.google.com/publisher-tag/reference#displayadunitpath,-size,-opt_div,-opt_clickurl) method is used
to register and display an ad slot. However, there are times when it may be
preferable or even necessary to separate these actions, in order to more
precisely control when ad content is loaded. For example, when working with a
consent management platform or requesting ad content as the result of a user
action.

In this guide we'll explore the mechanisms provided by GPT to
control the loading of ad content and fetch new ad content on demand. Full code
for this example can be found on the [event based requests](https://developers.google.com/publisher-tag/samples/event-based-requests)
sample page.

## Control ad loading

By default, the behavior of the [`display()`](https://developers.google.com/publisher-tag/reference#displayadunitpath,-size,-opt_div,-opt_clickurl) method is to
register, request, and render ad content into an ad slot. The automatic
requesting and rendering of ad content can be disabled using
[`googletag.setConfig({ disableInitialLoad: true })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad).

With initial load disabled, calls to `display()` will only register the ad slot.
No ad content will be loaded until a second action is taken. This lets you
precisely control when ad requests are made.

To avoid making unintentional ad requests,
`googletag.setConfig({ disableInitialLoad: true })` must be called before
enabling the service and before calling `display()`.

```html
<!DOCTYPE html>
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
    <script>
      googletag.cmd.push(() => {
        // Register the ad slot.
        // An ad will not be fetched until refresh is called.
        googletag.display("div-for-slot");
      });
    </script>
  </body>
</html>
```

In this example, initial load is disabled ensuring that no ad request is made
and no ad content is rendered when `display()` is called. The slot is ready to
accept and display an ad, but an ad request won't be made until the slot is
refreshed.

## Refresh

The [`PubAdsService.refresh()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_refresh) method is used to populate a
slot or slots with new ad content. This method can be used on slots that have
yet to load any content (due to
`googletag.setConfig({ disableInitialLoad: true })`), or to replace the contents
of an already populated slot. However, only slots which have been registered by
calling `display()` are eligible to be refreshed.

> [!IMPORTANT]
> **Important:** To comply with Google policy and enable your inventory to compete on Ad Exchange, you must [declare which portions of your inventory refresh](https://support.google.com/admanager/answer/6286179).

```html
<!DOCTYPE html>
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

In this modified example, when a user clicks the "Show/Refresh Ad" button, the
`refresh()` method is called. This triggers a request to fetch new ad content
and load it into the registered slot, overwriting any pre-existing content.

Note that in the preceding example the `refresh()` method is called with no
parameters, which has the effect of refreshing **all** registered ad slots.
However, it's also possible to refresh specific ad slots by passing an array of
slots to the `refresh()` method. See the [Refresh ad slots](https://developers.google.com/publisher-tag/samples/refresh)
sample for an example of this.

### Best practices

When working with `refresh()`, there are some best practices that should be
adhered to.

1. Don't refresh too quickly.

   Refreshing ad slots too quickly may cause your ad requests to be throttled.
   To prevent this, avoid refreshing slots more frequently than once every 30
   seconds.
2. Don't call `clear()` unnecessarily

   When refreshing an ad slot, don't call
   [`PubAdsService.clear()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_clear) first. This is unnecessary, since
   `refresh()` replaces the contents of the specified slot, regardless of
   whether any ad content was previously loaded. Calling `clear()` immediately
   before calling `refresh()` will only increase the amount of time a blank slot
   is visible to the user.
3. Only refresh viewable ad slots

   Using `refresh()` to replace the contents of ad slots that are never viewable
   can significantly lower your ActiveView rate. The
   [ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.impressionviewableevent) can be used to
   determine when an ad slot has become viewable, as shown in the following
   example:

       googletag.cmd.push(function() {
         var REFRESH_KEY = 'refresh';
         var REFRESH_VALUE = 'true';

         const slot = googletag.defineSlot('/6355419/Travel',[728, 90], 'div-for-slot')
             .addService(googletag.pubads());
         slot.setConfig({
           targeting: {
             [REFRESH_KEY]: REFRESH_VALUE,
             'test': 'event'
           }
         });

         // Number of seconds to wait after the slot becomes viewable.
         var SECONDS_TO_WAIT_AFTER_VIEWABILITY = 60;

         googletag.pubads().addEventListener('impressionViewable', function(event) {
           var slot = event.slot;
           if (slot.getTargeting(REFRESH_KEY).indexOf(REFRESH_VALUE) > -1) {
             setTimeout(function() {
               googletag.pubads().refresh([slot]);
             }, SECONDS_TO_WAIT_AFTER_VIEWABILITY * 1000);
           }
         });

         googletag.enableServices();
       });