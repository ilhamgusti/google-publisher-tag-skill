---
type: Reference
title: "GPT Production Release Notes"
description: "Changelog and historical release notes for Google Publisher Tag production releases."
resource: "https://developers.google.com/publisher-tag/release-notes"
tags: [gpt, release-notes, changelog, versions]
timestamp: 2026-09-10T00:00:00Z
---

This page documents production updates to the Google Publisher Tag
(GPT) library. You can periodically check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

To have updates delivered to you, add the URL of this page to your
[feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) of choice, or use a direct link to the release notes
feed in either
[Atom 1.0](https://developers.google.com/static/publisher-tag/feeds/release-notes-atom.xml)![feed icon](https://developers.google.com/static/publisher-tag/images/feed-icon.png) or
[RSS 2.0](https://developers.google.com/static/publisher-tag/feeds/release-notes-rss.xml)![feed icon](https://developers.google.com/static/publisher-tag/images/feed-icon.png) format.

> [!NOTE]
> **Note:** Only releases which contain user-visible changes are documented here. For a complete list of GPT releases, including maintenance releases, see the [version history](https://developers.google.com/publisher-tag/versions) page.

#### About release dates

All changes to the GPT library are thoroughly tested before
release. Additionally, releases are rolled out to users gradually to further
protect against unexpected regressions. If a regression is spotted at any point
during a rollout, the entire release can be quickly abandoned before it reaches
all users.

Due to this, release dates are not exact; a release can can take anywhere from a
few days to a few weeks to release completely. This means that users will
encounter changes at different times. The dates provided in these release notes
reflect the start of the week in which a change finished rolling out to *all*
users.

## Week of May 18, 2026

Announcement
Sunset of the 'Backwards' Web Interstitial Trigger


Starting June 15, 2026, navigating backward using a browser's back button will no longer trigger an Ad Manager web interstitial across any supported browsers (including Chrome, Edge, and Opera). This update applies automatically to all publishers opted into the "Backwards" trigger and requires no publisher action. The change ensures compliance with Google Search's new policy against "back button hijacking." <https://developers.google.com/search/blog/2026/04/back-button-hijacking>

## Week of April 27, 2026

Fixed
We have addressed an issue within the automatic refresh feature where ads
could refresh multiple times in rapid succession after a Chrome Heavy Ad
Intervention. A mitigation has been put in place to limit refreshes, and we
are actively working on a more permanent solution to prevent this behavior
and improve the feature's robustness.

## Week of April 20, 2026

Feature
Added support for configuring publisher-initiated age treatments. This allows
publishers to signal child or teen privacy protections for ad requests.


Publishers can now use the `tagForAgeTreatment` setting in
`https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig`
to enforce child treatment (equivalent to TFCD) or teen treatment (equivalent to TAP).

| New in GPT ||
|---|---|
| Enum | `https://developers.google.com/publisher-tag/reference#googletag.enums.TagForAgeTreatment` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.tagForAgeTreatment` |

## Week of March 9, 2026

Announcement
When Chrome's [Heavy Ad Intervention](https://developer.chrome.com/docs/web-platform/heavy-ads-intervention)
feature removes an ad for using excessive resources, GPT will now automatically
refresh the empty slot with another ad. This helps ensure the ad space remains
utilized. This behavior is expected to increase ad impressions, particularly
in desktop Chrome environments.


**Note on targeting and key-values:** This automatic refresh
will reuse the slot's existing targeting configuration. If your integration
relies on updating key-values before every refresh, this may result in
sending stale targeting data. Publishers who prefer to manage this logic
manually can opt-out using [`googletag.config.AutoRefreshConfig`](https://developers.google.com/publisher-tag/reference#googletag.config.AutoRefreshConfig).

## Week of October 6, 2025

Announcement
[Interstitial ads](https://support.google.com/admanager/answer/9840201)
now [speculatively prerender](https://developer.chrome.com/docs/web-platform/prerender-pages) same-site destinations for navigation triggers
on Chrome. This improves the user experience by enabling faster page loads
when interstitial ads are dismissed.

## Week of July 28, 2025

Announcement
A number of existing page- and slot-level settings have been migrated to the
new, unified GPT config API. This migration brings several improvements:

- **Improved discovery**: Settings are grouped together in documentation and type definitions.
- **More intuitive**: You can configure settings individually or all at once using a single interface.
- **Clearer errors**: Configuration errors provide more detail and use standardized language to streamline troubleshooting.


Legacy configuration methods continue to function, but are updated to use
the new config framework internally. As a result, you might encounter error
messages referencing properties of the new config API, even when using
legacy methods.
Feature

| New in GPT ||
|---|---|
| Object | [`googletag.config.AdSenseAttributesConfig`](https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig) [`googletag.config.LazyLoadConfig`](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig) [`googletag.config.VideoAdsConfig`](https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig) |
| Property | [`PageSettingsConfig.adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes) [`PageSettingsConfig.categoryExclusion`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) [`PageSettingsConfig.centering`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.centering) [`PageSettingsConfig.collapseDiv`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv) [`PageSettingsConfig.disableInitialLoad`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad) [`PageSettingsConfig.lazyLoad`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad) [`PageSettingsConfig.location`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.location) [`PageSettingsConfig.safeFrame`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) [`PageSettingsConfig.singleRequest`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) [`PageSettingsConfig.targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) [`PageSettingsConfig.videoAds`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) [`SafeFrameConfig.forceSafeFrame`](https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.forceSafeFrame) [`SlotSettingsConfig.adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes) [`SlotSettingsConfig.categoryExclusion`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) [`SlotSettingsConfig.clickUrl`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.clickUrl) [`SlotSettingsConfig.collapseDiv`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv) [`SlotSettingsConfig.safeFrame`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) [`SlotSettingsConfig.targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) |

Change
The `SafeFrameConfig` object has been moved from the
`googletag` namespace to the `googletag.config`
namespace.
Deprecated
The following table lists deprecated legacy configuration methods,
alongside their recommended config API replacements.

| Legacy configuration method(s) | GPT config API replacement |
|---|---|
| `PubAdsService.set()` | [`PageSettingsConfig.adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes) |
| `PubAdsService.clearCategoryExclusions()` `PubAdsService.setCategoryExclusion()` | [`PageSettingsConfig.categoryExclusion`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) |
| `PubAdsService.setCentering()` | [`PageSettingsConfig.centering`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.centering) |
| `PubAdsService.collapseEmptyDivs()` | [`PageSettingsConfig.collapseDiv`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv) |
| `PubAdsService.disableInitialLoad()` | [`PageSettingsConfig.disableInitialLoad`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad) |
| `PubAdsService.enableLazyLoad()` | [`PageSettingsConfig.lazyLoad`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad) |
| `PubAdsService.setLocation()` | [`PageSettingsConfig.location`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.location) |
| `PubAdsService.setForceSafeFrame()` `PubAdsService.setSafeFrameConfig()` | [`PageSettingsConfig.safeFrame`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) |
| `PubAdsService.enableSingleRequest()` | [`PageSettingsConfig.singleRequest`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) |
| `PubAdsService.clearTargeting()` `PubAdsService.setTargeting()` | [`PageSettingsConfig.targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) |
| `PubAdsService.enableVideoAds()` `PubAdsService.setVideoContent()` | [`PageSettingsConfig.videoAds`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) |
| `PubAdsService.isInitialLoadDisabled()` `PubAdsService.get()` `PubAdsService.getAttributeKeys()` `PubAdsService.getTargeting()` `PubAdsService.getTargetingKeys()` | [`googletag.getConfig()`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |
| `Slot.set()` | [`SlotSettingsConfig.adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes) |
| `Slot.clearCategoryExclusions()` `Slot.setCategoryExclusion()` | [`SlotSettingsConfig.categoryExclusion`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) |
| `Slot.setClickUrl()` | [`SlotSettingsConfig.clickUrl`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.clickUrl) |
| `Slot.setCollapseEmptyDiv()` | [`SlotSettingsConfig.collapseDiv`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv) |
| `Slot.setForceSafeFrame()` `Slot.setSafeFrameConfig()` | [`SlotSettingsConfig.safeFrame`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) |
| `Slot.clearTargeting()` `Slot.setTargeting()` `Slot.updateTargetingFromMap()` | [`SlotSettingsConfig.targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) |
| `Slot.get()` `Slot.getAttributeKeys()` `Slot.getCategoryExclusions()` `Slot.getTargeting()` `Slot.getTargetingKeys()` | [`Slot.getConfig()`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |

## Week of July 21, 2025

Change
The `threadYield` feature has been updated to also yield
the JS thread before generating an ad request URL, for requests which
contain only below-the-fold slots. This has been shown to positively affect
[Core Web Vitals](https://web.dev/explore/learn-core-web-vitals),
with no negative impact on impressions.

| Updated in GPT ||
|---|---|
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.threadYield` |

## Week of June 2, 2025

Announcement Web interstitials now fully support single-page applications (SPA)


GPT users can now seamlessly display web interstitial ads within SPA-enabled
websites, without needing full page reloads. This enhancement can:

- Improve user experience: Deliver ads at natural break points within your SPA, resulting in smooth transitions and less disruption.
- Boost monetization: Unlock new revenue opportunities by effectively serving interstitial ads on dynamic, SPA-driven content.
- Maintain Better Ads Standards: Continue to deliver high-quality ad experiences with clear exit options and configurable frequency caps, adhering to industry best practices.


No changes are required to your existing SPA implementation. GPT will
automatically detect and manage interstitial display for page changes within
your SPA. For more details on implementing GPT-managed web interstitials and
optional interstitial triggers, see the
[Display a web interstitial ad](https://developers.google.com/publisher-tag/samples/display-web-interstitial-ad) sample.

## Week of May 26, 2025

Announcement
The frequency cap for
[H5 gaming interstitial ads](https://support.google.com/admanager/answer/14640119) has been reduced from 120
to 30 seconds.

## Week of April 28, 2025

Feature

| New in GPT ||
|---|---|
| Property | [`SlotRenderEndedEvent.responseIdentifier`](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.responseIdentifier) |

## Week of January 27, 2025

Breaking
The following
[`ComponentAuctionConfig.auctionConfig`](https://developers.google.com/publisher-tag/reference#googletag.config.ComponentAuctionConfig.auctionConfig)
properties have been renamed, to align with the
[Protected Audience API](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#21-initiating-an-on-device-auction) spec.

| Old property name | New property name |
|---|---|
| `decisionLogicUrl` | `decisionLogicURL` |
| `trustedScoringSignalsUrl` | `trustedScoringSignalsURL` |

## Week of October 21, 2024

Change
Modify `threadYield` to use Scheduler.yield over
Scheduler.postTask where available. See
[yield documentation](https://developer.mozilla.org/en-US/docs/Web/API/Scheduler/yield)
for details.

| Updated in GPT ||
|---|---|
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.threadYield` |

## Week of September 2, 2024

Feature
Added support for [gaming interstitial](https://support.google.com/admanager/answer/14640119) ads.

| New in GPT ||
|---|---|
| Enum | `https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat_GAME_MANUAL_INTERSTITIAL` |
| Event | `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent` `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent` |
| Method | `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent_makeGameManualInterstitialVisible` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap_gameManualInterstitialSlotClosed` `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap_gameManualInterstitialSlotReady` |

## Week of August 19, 2024

Change
The setting for controlling GPT thread yield behavior has been renamed from
`adYield` to `threadYield` to clarify the feature is
focused on yielding the JS thread rather than optimizing ad yield. The
behavior of the feature and it's associated API (other than name) remains
unchanged. The `adYield` property will be removed in a future GPT
release.


The default thread yield behavior may be disabled with
`googletag.setConfig({threadYield: 'DISABLED'});`
or applied to all slots independent of their location relative to viewport
with `googletag.setConfig({threadYield: 'ENABLED_ALL_SLOTS'});`.

| Updated in GPT ||
|---|---|
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.threadYield` |

## Week of July 29, 2024

Feature
GPT now yields the JS thread using
[Scheduler.postTask](https://developer.mozilla.org/docs/Web/API/Scheduler/postTask)
(where available) with priority: 'user-blocking' just prior to rendering
creatives. This has been shown to have extremely small impact on
impressions while meaningfully benefiting
[Core Web Vitals](https://web.dev/explore/learn-core-web-vitals).
By default, GPT will yield only if the slot is outside of the viewport.


The default behavior may be disabled with
`googletag.setConfig({adYield: 'DISABLED'});`
or applied to all slots independent of their location relative to viewport
with `googletag.setConfig({adYield: 'ENABLED_ALL_SLOTS'});`.

| New in GPT ||
|---|---|
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adYield` |

## Week of February 12, 2024

Feature
Added support for configuring
[publisher provided signals (PPS)](https://support.google.com/admanager/answer/12451124).

| New in GPT ||
|---|---|
| Object | `https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig` `https://developers.google.com/publisher-tag/reference#googletag.config.TaxonomyData` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.pps` `https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig.taxonomies` `https://developers.google.com/publisher-tag/reference#googletag.config.TaxonomyData.values` |
| Type | `https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy` |

Fixed
Fixed a bug where
`https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent_slotContentChanged`
was always `true`. Going forward, this property will only be `true` if the
content of the slot changed, and `false` otherwise (for example, if an ad did not fill).

## Week of January 29, 2024

Feature
Network failures for ad requests will mimic a no fill by firing a
`https://developers.google.com/publisher-tag/reference#googletag.events.slotrenderendedevent`
with
`https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent_isEmpty`
set to `true`. See
[Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
for example of how to listen to this event. Change includes automatically
collapsing the slot when using
`https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_collapseEmptyDivs`.
Feature
Added support for configuring ad expansion on
[desktop/tablet](https://support.google.com/admanager/answer/9384852) and
[mobile web (partial screen)](https://support.google.com/admanager/answer/9117822).

| New in GPT ||
|---|---|
| Object | `https://developers.google.com/publisher-tag/reference#googletag.config.adexpansionconfig` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.AdExpansionConfig_enabled` `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig_adExpansion` `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig_adExpansion` |

## Week of December 11, 2023

Feature
Added support for
[side rail anchor ads](https://support.google.com/admanager/answer/10452255#side-rail-anchor-ads).

| New in GPT ||
|---|---|
| Enum | `https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat_LEFT_SIDE_RAIL` `https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat_RIGHT_SIDE_RAIL` |

## Week of November 13, 2023

Feature Added support for configuring publisher privacy treatments.

| New in GPT ||
|---|---|
| Function | `https://developers.google.com/publisher-tag/reference#googletag.setConfig`[](https://developers.google.com/publisher-tag/reference#googletag.setConfig) |
| Object | ` https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig ` ` https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatmentsConfig ` |
| Property | ` https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig_privacyTreatments ` ` https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatmentsConfig_treatments ` |
| Type | `https://developers.google.com/publisher-tag/reference#googletag.config_PrivacyTreatment` |

Feature
Added support for [Chrome prerendering](https://developer.chrome.com/docs/web-platform/prerender-pages).
When GPT detects the page is in a prerender state, the ad request will be delayed until the page becomes visible to the user.

## Week of October 23, 2023

Feature Added support for optional web interstitial [triggers](https://support.google.com/admanager/answer/9840201#triggers).

| New in GPT ||
|---|---|
| Object | `https://developers.google.com/publisher-tag/reference#googletag.config.interstitialconfig` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig_interstitial` |
| Type | `https://developers.google.com/publisher-tag/reference#googletag.config_InterstitialTrigger` |

## Week of July 24, 2023

Announcement
The
[Protected Audience API](https://privacysandbox.com/news/protected-audience-api-our-new-name-for-fledge)
(formerly known as FLEDGE) is
[transitioning to general availability](https://privacysandbox.com/news/the-next-stages-of-privacy-sandbox-general-availability)
with the July release of Chrome. With this, component auction-related
functionality in GPT is now considered stable.
Change

| Moved from experimental to stable ||
|---|---|
| Object | `https://developers.google.com/publisher-tag/reference#googletag.config_ComponentAuctionConfig` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig_componentAuction` |

## Week of June 19, 2023

Announcement
Update: Beginning on or after July 5, 2023, GPT will no longer serve
outdated versions of its Javascript library, **nor serve ads to those
versions** . See the [previous announcement](https://developers.google.com/publisher-tag/release-notes#2023-06-06)
for details.  

<br />


Publishers serving from www.googletagservices.com/tag/js/gpt.js may continue
to do so. However, switching to the preferred domain is recommended, as it
may improve performance and serving of gpt.js on www.googletagservices.com
may be discontinued in the future.

## Week of June 6, 2023

Announcement
Beginning on or after July 5, 2023, GPT will no longer serve outdated
versions of its JavaScript library. There is no impact to publishers loading
GPT from an
[official URL](https://developers.google.com/publisher-tag/guides/general-best-practices#load_from_an_official_source).
Publishers who are serving a cached version of gpt.js, pubads_impl.js, or
any libraries they load must update their pages to use the official
URLs. For more information, see the [Get started](https://developers.google.com/publisher-tag/guides/get-started) guide.

## Week of May 22, 2023

Change
Negative and zero size values provided to [`googletag.defineSlot()`](https://developers.google.com/publisher-tag/reference#googletag.defineSlot)
and [`SizeMappingBuilder.addSize()`](https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder_addSize)
are now automatically removed, as they are invalid. As a result, existing integrations that provide such invalid values may see an
increase in [publisher console messages](https://developers.google.com/publisher-tag/guides/publisher-console-messages#INVALID_SLOT_SIZE_FIXED).
However, this will have no effect on existing, valid ad requests.

## Week of May 18, 2023

Fixed
Installation of [Secure Signals](https://support.google.com/admanager/answer/10488752) bidder scripts by GPT will now be done earlier in GPT's execution. This may result in improved signal coverage across ad requests.

## Week of May 1, 2023

Fixed
Fixed a bug where creative could appear truncated when refreshing multi-size [anchor slots](https://developers.google.com/publisher-tag/samples/display-anchor-ad).

## Week of March 27, 2023

Change GPT no longer supports viewability based features on browsers that don't natively support the [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API). Note that all [supported browsers](https://developers.google.com/publisher-tag/support/browser-support) natively support this API.

| Method or Event ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.impressionviewableevent` |
| `https://developers.google.com/publisher-tag/reference#googletag.events.slotvisibilitychangedevent` |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_enableLazyLoad` |

## Week of February 6, 2023

Feature
Added support for [sharing secure signals](https://support.google.com/admanager/answer/10488752).

| New in GPT ||
|---|---|
| Object | `https://developers.google.com/publisher-tag/reference#googletag.securesignals.biddersignalprovider` `https://developers.google.com/publisher-tag/reference#googletag.securesignals.publishersignalprovider` `https://developers.google.com/publisher-tag/reference#googletag.securesignals.securesignalprovidersarray` |
| Type | `https://developers.google.com/publisher-tag/reference#googletag.secureSignals_SecureSignalProvider` |
| Variable | `https://developers.google.com/publisher-tag/reference#googletag.secureSignalProviders` |

## Week of January 30, 2023

Fixed The behavior of
[Service.addEventListener()](https://developers.google.com/publisher-tag/reference#googletag.Service_addEventListener) has been changed so that when an event occurs all of the associated listeners execute before processing a later event. Prior to this change, slot render start and end event listeners for the same slot could execute out of order.

## Week of August 15, 2022

Change Return type of
[Service.removeEventListener()](https://developers.google.com/publisher-tag/reference#googletag.Service_removeEventListener) has been changed from `boolean` to `void`.

## Week of July 25, 2022

Feature
Added experimental support for
[FLEDGE](https://developer.chrome.com/docs/privacy-sandbox/fledge/)
component auctions, to enable early testing of
[FLEDGE with multiple sellers](https://github.com/google/ads-privacy/tree/master/proposals/fledge-multiple-seller-testing).

| New in GPT ||
|---|---|
| Method | `https://developers.google.com/publisher-tag/reference#googletag.Slot_setConfig` |
| Object | `https://developers.google.com/publisher-tag/reference#googletag.config.componentauctionconfig` `https://developers.google.com/publisher-tag/reference#googletag.config.slotsettingsconfig` |

## Week of July 18, 2022

Deprecated
The `ContentService` API has been sunset. Calling `googletag.content().setContent` now has no effect besides logging a warning. The `googletag.content` property will soon be removed entirely; after that, attempting to call it will throw an exception. Use the browser's built-in DOM APIs to directly add content to div elements instead.

## Week of May 23, 2022

Feature
Added support for configuring ad request
[traffic source](https://support.google.com/admanager/answer/11233407).

| GPT support for traffic source ||
|---|---|
| Enum | `https://developers.google.com/publisher-tag/reference#googletag.enums.TrafficSource_ORGANIC` `https://developers.google.com/publisher-tag/reference#googletag.enums.TrafficSource_PURCHASED` |
| Property | `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig_trafficSource` |

## Week of March 7, 2022

Announcement
Rewarded ads for web have launched. Visit the [Ad Manager help center](https://support.google.com/admanager/answer/9116812) for details.
Feature

| GPT support for rewarded ads for web ||
|---|---|
| Enum | `https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat_REWARDED` |
| Event | `https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotclosedevent` |
| Event | `https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotgrantedevent` |
| Event | `https://developers.google.com/publisher-tag/reference#googletag.events.rewardedslotreadyevent` |
| Object | `https://developers.google.com/publisher-tag/reference#googletag.rewardedpayload` |

## Week of February 28, 2022

Change
[CommandArray.push](https://developers.google.com/publisher-tag/reference#googletag.CommandArray_push) now
explicitly binds provided functions to [`globalThis`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/globalThis) instead of its own
`arguments` object.

## Week of December 8, 2021

Feature
[Enums](https://developers.google.com/publisher-tag/reference#enum-types) now also expose a reverse mapping
of values to keys in order to match behavior of TypeScript enums. APIs that
take enum values remain unchanged, and these new reverse mappings shouldn't
be used.

## Week of August 9, 2021

Feature
Added the [removeEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service_removeEventListener) method.
Change
Calling [addEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service_addEventListener)
multiple times with the same eventType and callback function instance is now
a no-op. In other words if a single callback function instance is registered
n times for the same event type, it will only execute once when the event
occurs, rather than n times.

## Week of July 29, 2021

Change
GPT's viewability events: [`ImpressionViewableEvent`](https://developers.google.com/publisher-tag/reference#googletag.events.impressionviewableevent)
and [`SlotVisibilityChangedEvent`](https://developers.google.com/publisher-tag/reference#googletag.events.slotvisibilitychangedevent)
will now continue to fire on long page sessions. Previously, they had shut
down after one hour from page load.

## Week of May 03, 2021

Change
GPT no longer sets space for slots before fetching ads. This change reduces
[Cumulative Layout Shift (CLS)](https://web.dev/cls/) on sites
that have not reserved space using CSS.

To further reduce CLS on your site, we recommend reserving nonzero area for
the ad using CSS. [Learn more](https://developers.google.com/publisher-tag/guides/minimize-layout-shift)

## Week of March 22, 2021

Change
Updated the behavior of [`enableLazyLoad()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_enableLazyLoad) to also delay rendering of below-the-fold slots on background tabs.

## Week of February 23, 2021

Change
The `googletag.pubads().set` and `Slot.set` methods may now be called at any time before `display` or `refresh`. Previously `set` only applied when called before `googletag.enableServices`.

## Week of February 16, 2021

Change
The `googletag.pubads().setPublisherProvidedId` API may now be called at any time. Previously it only worked if called before `googletag.enableServices`.

## Week of January 4, 2021

Change
The `googletag.pubads().collapseEmptyDivs` API may be called repeatedly now to change settings. Previously repeated calls would be ignored.

## Week of October 12, 2020

Feature
Launched web interstitial open beta, see [help center](https://support.google.com/admanager/answer/9840201).

## Week of August 31, 2020

Deprecated
Deprecated `definePassback()` and `defineOutOfPagePassback()`. See [passback docs](https://developers.google.com/publisher-tag/guides/passback-tags#construct_passback_tags) for how to correctly create a passback.

## Week of June 15, 2020

Fixed
Updated the behavior of [`enableLazyLoad()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_enableLazyLoad) to be compatible with [`collapseEmptyDivs(true)`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_collapseEmptyDivs).

## Week of May 25, 2020

Change
GPT will no longer support precise GPS location set by publishers. Specifically, [`googletag.pubads().setLocation()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setLocation) will no longer support latitude, longitude, or radius parameters, but will instead take a freeform address.

## Week of April 27, 2020

Announcement
GPT rendering logic is no longer modularized into separate files. This means that GPT will fetch fewer files in its execution, and thus slightly reduces latency, but has no net impact on user bandwidth.
Change
When a request is triggered in GPT (by calling [`googletag.display()`](https://developers.google.com/publisher-tag/reference#googletag.display) or [`googletag.pubads().refresh()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_refresh)), we will now internally freeze all publisher provided state so that it cannot be mutated before the request is sent. Therefore, when a request triggers, only the state added up until that point will be used for that request. Any state which is modified after that will only apply to the following requests.

## Week of November 11, 2019

Announcement
There is now a new recommended snippet for creating GPT passbacks. Use of [`definePassback()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_definePassback)
and [`defineOutOfPagePassback()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_defineOutOfPagePassback) is discouraged, since these functions behave synchronously and may be blocked by certain browsers. [Learn more](https://support.google.com/admanager/answer/2811375).
Feature
Added [`Slot.updateTargetingFromMap()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_updateTargetingFromMap) method.
Feature
Added [`PubAdsService.setPrivacySettings()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setPrivacySettings) as a new method of enabling privacy settings. Additional settings will be available here in the future.

## Week of March 25, 2019

Fixed
Pubads service is now fully operational immediately after calling [`googletag.enableServices()`](https://developers.google.com/publisher-tag/reference#googletag.enableServices) instead of being initialized asynchronously. This means that [`googletag.pubadsReady`](https://developers.google.com/publisher-tag/reference#googletag.pubadsReady) is now guaranteed to be true right after calling `googletag.enableServices()`. Polling to check the value of `googletag.pubadsReady` should no longer be necessary.

## Week of February 4, 2019

Change
Updated the behavior of [`enableLazyLoad()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_enableLazyLoad) to allow changes to lazy loading config after calling [`enableServices()`](https://developers.google.com/publisher-tag/reference#googletag.enableServices), with lazy loading config frozen for each slot when that slot is displayed.

## Week of January 21, 2019

Feature
Added a new supported event, [`SlotResponseReceived`](https://developers.google.com/publisher-tag/reference#googletageventsslotresponsereceived), which fires when an ad response is received for a slot.
Feature
Added a new field, [`creativeTemplateId`](https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation_creativeTemplateId) to [`googleTag.ResponseInformation`](https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation).

## Week of January 14, 2019

Feature
Added a new supported event, [`SlotRequestedEvent`](https://developers.google.com/publisher-tag/reference#googletageventsslotrequestedevent), which fires when an ad request is made for a slot.

## Week of August 27, 2018

Change
Modified [`googletag.display()`](https://developers.google.com/publisher-tag/reference#googletag.display) to accept a [`googletag.Slot`](https://developers.google.com/publisher-tag/reference#googletag.Slot) as an argument.

## Week of August 6, 2018

Feature
Adds [`googletag.PubAdsService.enableLazyLoad()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_enableLazyLoad) for lazy loading ads in GPT.

## Week of June 18, 2018

Fixed
Fixed a bug which caused the [`googletag.events.SlotOnloadEvent`](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent) to not trigger.

## Week of April 30, 2018

Feature
Adds [`googletag.PubAdsService.setTagForUnderAgeOfConsent()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setTagForUnderAgeOfConsent) for controlling ads for users under the age of consent, and [`googletag.PassbackSlot.setTagForUnderAgeOfConsent()`](https://developers.google.com/publisher-tag/reference#googletag.PassbackSlot_setTagForUnderAgeOfConsent) for marking the passback slot as coming from a user under the age of consent.

## Week of April 23, 2018

Feature
Adds [`googletag.PubAdsService.setRequestNonPersonalizedAds()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setRequestNonPersonalizedAds) for controlling ads personalization.

## Week of March 12, 2018

Fixed
Rolled back change which stopped removing existing content inside of slots prior to refreshing, if that content was not placed there by GPT. Contents will now be cleared.

## Week of February 19, 2018

Announcement
When asynchronous rendering mode is used: Request ads using XMLHttpRequest with the `HTTP GET` method where possible for all ad requests, up to the 8,192 character limit. Previously, the `HTTP POST `method would have been used for ad requests exceeding 4,096 characters, up to the 8,192 character limit.
Change
Stopped removing existing content inside of slots prior to refreshing, if that content was not placed there by GPT.
This note is incorrect; see entry for [Week of March 12, 2018](https://developers.google.com/publisher-tag/release-notes#2018-03-12)

## Week of January 8, 2018

Change
Support alternate syntax of `[..., ['fluid'], ...]` as a [`NamedSized`](https://developers.google.com/publisher-tag/reference#googletag.NamedSize) within a multi-size array. Previously only `[..., 'fluid', ...]` was considered valid.

## Week of July 10, 2017

Deprecated
Removed labelIds field from [googleTag.ResponseInformation](https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation).

## Week of June 5, 2017

Change
Modified [`googletag.display()`](https://developers.google.com/publisher-tag/reference#googletag.display) and [`googletag.pubads().display`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_display) to accept a div element as well as a div ID. This allows rendering slots inside divs which are in a shadow DOM.

## Week of February 27, 2017

Feature
Added [`sourceAgnosticCreativeId`](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent_sourceAgnosticCreativeId) and [`sourceAgnosticLineItemId`](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent_sourceAgnosticLineItemId) to [`SlotRenderEndedEvent`](https://developers.google.com/publisher-tag/reference#googletageventsslotrenderendedevent).

## Week of November 7, 2016

Feature
Released [`getSlots()`](https://developers.google.com/publisher-tag/reference#googletag.Service_getSlots) API on Service for retrieving the list of slots associated with a service.

## Week of October 17, 2016

Change
Modified both [`Slot.clearTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_clearTargeting) and [`PubAdsService.clearTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_clearTargeting) to take an optional key parameter.

## Week of September 5, 2016

Change
Errors caught in `googletag.cmd.push()` are no longer invisible, and will be printed to the console.

## Week of August 8, 2016

Feature
Released [`SlotOnloadEvent`](https://developers.google.com/publisher-tag/reference#googletageventsslotonloadevent) API to allow listening for a creative to finish loading.

## Week of July 25, 2016

Feature
Released [`getTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_getTargeting) and [`getTargetingKeys()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_getTargetingKeys) APIs on PubAdsService for retrieving custom service-level targeting parameters.

## Week of June 20, 2016

Feature
Released [`openConsole()`](https://developers.google.com/publisher-tag/reference#googletag.openConsole) API to open the Google Publisher Console without the need for a page refresh.

## Week of June 6, 2016

Feature
Released [`getTargeting()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_getTargeting) and [`getTargetingKeys()`](https://developers.google.com/publisher-tag/reference#googletag.Slot_getTargetingKeys) APIs for retrieving custom targeting parameters.
Feature
Adding configuration option where Safeframe should allow expand by pushing content: [`allowPushExpansion`](https://developers.google.com/publisher-tag/reference#googletag.SafeFrameConfig_allowPushExpansion).

## Week of May 16, 2016

Feature
Support [fluid size](https://developers.google.com/publisher-tag/reference#googletag.NamedSize) in multi-size ad requests.

## Week of April 18, 2016

Feature
Released [`getResponseInformation`](https://developers.google.com/publisher-tag/reference#googletag.Slot_getResponseInformation) API which returns ad response information for the ad slot.
Feature
Released [`setAdIframeTitle`](https://developers.google.com/publisher-tag/reference#googletag.setAdIframeTitle) API which sets the input as the title of any ad container iframes that are created after.

## Week of April 4, 2016

Announcement
Increased `HTTP GET` ad request max length to 4,096 characters.

## Week of March 28, 2016

Feature
Adding configuration option where Safeframe should allow expand by overlaying content: [`allowOverlayExpansion`](https://developers.google.com/publisher-tag/reference#googletag.SafeFrameConfig_allowOverlayExpansion).
Feature
Adding configuration option where SafeFrame should use the HTML5 sandbox attribute to prevent top level navigation: [`sandbox`](https://developers.google.com/publisher-tag/reference#googletag.SafeFrameConfig_sandbox).

## Week of February 22, 2016

Feature
Adding ability to set titles for ad container iframes: [`setAdIframeTitle()`](https://developers.google.com/publisher-tag/reference#googletag.setAdIframeTitle).
Feature
Adding an API to configure SafeFrame properties on page and slot level: [`setSafeFrameConfig()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setSafeFrameConfig).

## Week of February 15, 2016

Feature
Adding ability to destroy a slot and re-use the div: [`destroySlots()`](https://developers.google.com/publisher-tag/reference#googletag.destroySlots).
Feature
Adding an API to force the use of safeframe on ad slots with granular controls: [`setForceSafeFrame()`](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_setForceSafeFrame).

## Week of December 7, 2015

Feature
Adding slot visibility events ([`SlotVisibilityChangedEvent`](https://developers.google.com/publisher-tag/reference#googletageventsslotvisibilitychangedevent)).

## Week of October 26, 2015

Feature
Adding impression viewability ([`ImpressionViewableEvent`](https://developers.google.com/publisher-tag/reference#googletageventsimpressionviewableevent)).
Feature
Update passback targeting from a JSON map ([`Passback.updateTargetingFromMap()`](https://developers.google.com/publisher-tag/reference#googletag.PassbackSlot_updateTargetingFromMap)).
Feature
Support of [`set()`](https://developers.google.com/publisher-tag/reference#googletag.PassbackSlot_set) and [`get()`](https://developers.google.com/publisher-tag/reference#googletag.PassbackSlot_get) AdSense attribute `page_url` for passback slots.

## Week of October 12, 2015

Feature
Support for [out-of-page passback](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService_defineOutOfPagePassback).

## Week of August 31, 2015

Announcement
Restructuring GPT architecture into a thin loader and a bigger implementation.
Feature
Support for [fluid size](https://developers.google.com/publisher-tag/reference#googletag.NamedSize) in GPT.