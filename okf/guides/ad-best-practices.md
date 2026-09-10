---
type: Best Practice
title: "Ad Placement and Viewability Best Practices"
description: "Recommendations for ad sizing, slot viewability, and user experience."
resource: "https://developers.google.com/publisher-tag/guides/ad-best-practices"
tags: [gpt, viewability, placement, best-practices]
timestamp: 2026-09-10T00:00:00Z
---

# Ad Best Practices

After you've integrated the Google Publisher Tag (GPT) library into
your site and become familiar with our
[general best practices](https://developers.google.com/publisher-tag/guides/general-best-practices), you're ready to
start issuing ad requests. In the following sections, we'll cover some
additional best practices you should keep in mind when configuring and working
with ad slots, to make the most of your ad space with minimal performance
impact.

## Prioritize "important" ad slots

Not all ad slots are created equal. For example, slots which are visible as soon
as your page loads (above the fold) are usually more "important" than those
which are not visible until scrolled into view (below the fold), in terms of
viewability and monetization. With this in mind, it's important that you
carefully consider the relative importance of every ad slot on your page and
prioritize loading the most important slots as quickly as possible.

### Load above the fold ads early

Ads that will be visible as soon as the page loads should be given the highest
priority. It's recommended that you define these slots in the `<head>` of your
document, and request them as early in the page load process as possible. This
helps to ensure that these ads are loaded early (maximizing viewability) and
that they won't unnecessarily slow down the initial page load.

### Load below the fold ads lazily

For ads that need to be scrolled into view, fetching and rendering should be
deferred until the slots are close to entering the viewport. This is a process
known as lazy loading. [Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading) separately
prioritizes requesting and rendering creative content for slots that are the
most likely to be viewed. This helps optimize page load performance by
conserving the browser's limited resources, which is especially important in
mobile environments where bandwidth and CPU are often heavily constrained.

## Refresh ads without refreshing the page

There are many scenarios in which it is optimal or even necessary to replace the
current ad content of a slot. In these cases, it is best to use the
GPT library's
[refresh functionality](https://developers.google.com/publisher-tag/guides/control-ad-loading#refresh) to do so dynamically.
This avoids a full page refresh and lets you precisely control the conditions
under which a slot or group of slots are updated.

When refreshing ad slots, it's important to be familiar with and adhere to
[`refresh()` best practices](https://developers.google.com/publisher-tag/guides/control-ad-loading#best_practices).
Refreshing ads inappropriately can lead to performance issues and negatively
impact viewability rates.

> [!IMPORTANT]
> **Important:** To comply with Google policy and enable your inventory to compete on Ad Exchange, you must [declare which portions of your inventory refresh](https://support.google.com/admanager/answer/6286179).

## Target ads effectively

When configuring [key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting), carefully
consider whether to use slot- or page-level targeting. For key-values shared
between multiple slots, it's most effective to use page-level targeting using
[`googletag.setConfig({ targeting: ... })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting). Slot-level
targeting should only be used to register key-values which differ or are not
included on all slots.

Note that both slot- and page-level targeting can be used at once, as seen in
the [set targeting example](https://developers.google.com/publisher-tag/guides/key-value-targeting#set_targeting). It is strongly recommended
that you configure targeting at the page-level first, then apply slot-level
overrides only where necessary. This approach not only makes efficient use of
the GPT API, it also simplifies code and helps in maintaining
a clear mental model of all targeting configured on the page.

## Use Single Request Architecture correctly

Single Request Architecture (SRA) is a GPT request mode which
bundles requests for multiple ad slots into a single ad request. This ensures
that competitive exclusions and roadblocks configured for your page will be
honored. Therefore, if your page makes use of these, it's recommended that you
enable SRA and understand how to use it correctly.

In its default configuration, SRA will request all ad slots defined on your
page the first time you call [`display()`](https://developers.google.com/publisher-tag/reference#googletag.display) (or `refresh()`, if
[initial load is disabled](https://developers.google.com/publisher-tag/guides/control-ad-loading)). Because of this
it's recommended that you define all of your page's ad slots in the `<head>` of
the document, before making the first call to `display()`.
[Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading) can be used in conjunction with this
approach to ensure slots located below the fold are
[not loaded immediately](https://developers.google.com/publisher-tag/guides/ad-best-practices#below-the-fold).

When using SRA, it's important to fully configure all ad slots (for example,
set targeting, category exclusion, etc.) prior to making the first call to
`display()`. Only values configured before this point will be included in the
initial SRA request.

Incorrect --- ad slot configuration is not included in SRA request

    <html>
      <head>
        <meta charset="utf-8">
        <title>Single Request Architecture Example</title>
        <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
        <script>
          window.googletag = window.googletag || {cmd: []};
          var adSlot1, adSlot2;

          googletag.cmd.push(function() {
            // Define ad slot 1.
            adSlot1 = googletag
                .defineSlot('/6355419/Travel/Europe/France',[728, 90], 'banner-ad-1')
                .addService(googletag.pubads());
            // Define ad slot 2.
            adSlot2 = googletag
                .defineSlot('/6355419/Travel/Europe/France',[728, 90], 'banner-ad-2')
                .addService(googletag.pubads());
            // Enable SRA and services.
            googletag.setConfig({ singleRequest: true });
            googletag.enableServices();
          });
        </script>
      </head>
      <body>
        <div id="banner-ad-1" style="width: 728px; height: 90px;">
          <script>
            googletag.cmd.push(function() {
              // This call to display requests both ad slots.
              googletag.display(adSlot1);
            });
          </script>
        </div>
        <div id="banner-ad-2" style="width: 728px; height: 90px;">
          <script>
            googletag.cmd.push(function() {
              // This call to display has no effect, since both ad slots have already
              // been fetched by the previous call to display.
              // Targeting configuration for ad slot 2 is ignored.
              adSlot2.setConfig({ targeting: { test: 'privacy' } });
              googletag.display(adSlot2);
            });
          </script>
        </div>
      </body>
    </html>

Correct --- ad slot configuration is included in SRA request

    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Single Request Architecture Example</title>
        <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
        <script>
          window.googletag = window.googletag || {cmd: []};
          var adSlot1, adSlot2;

          googletag.cmd.push(function() {
            // Define ad slot 1.
            adSlot1 = googletag
                .defineSlot('/6355419/Travel/Europe/France',[728, 90], 'banner-ad-1')
                .addService(googletag.pubads());
            // Define and configure ad slot 2.
            adSlot2 = googletag
                .defineSlot('/6355419/Travel/Europe/France',[728, 90], 'banner-ad-2')
                .addService(googletag.pubads());
            adSlot2.setConfig({ targeting: { test: 'privacy' } });
            // Enable SRA and services.
            googletag.setConfig({ singleRequest: true });
            googletag.enableServices();
          });
        </script>
      </head>
      <body>
        <div id="banner-ad-1" style="width: 728px; height: 90px;"></div>
        <div id="banner-ad-2" style="width: 728px; height: 90px;"></div>
        <script>
            googletag.cmd.push(function() {
              // This call to display requests both ad slots with all
              // configured targeting.
              googletag.display(adSlot1);
            });
          </script>
      </body>
    </html>

## Optimize your ad sizing

When defining your ad slots, consider not just the maximum size ad that could
serve, but also smaller sizes that could comfortably fit into the same space. In
general, the more sizes you specify when defining a slot, the more ads that will
be eligible to serve to it. This can translate to higher fill rates and
increased revenue.