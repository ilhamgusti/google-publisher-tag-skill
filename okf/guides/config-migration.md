---
type: Guide
title: "Config Migration to setConfig()"
description: "Guide for migrating legacy configuration settings to googletag.setConfig()."
resource: "https://developers.google.com/publisher-tag/guides/config-migration"
tags: [gpt, migration, setConfig, configuration]
timestamp: 2026-09-10T00:00:00Z
---

This guide provides examples for migrating from legacy configuration methods to
the new Google Publisher Tag (GPT) library `setConfig` and
`getConfig` APIs.

The `setConfig` and `getConfig` APIs provide a centralized way to manage
both page- and slot-level configuration.

## Set page-level configuration

The following table maps legacy `PubAdsService` configuration methods to their
`setConfig` replacements.

| Feature | Legacy method | `setConfig` replacement |
|---|---|---|
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#set-page-adsense) | `set(key, value)` | [`googletag.setConfig({ adsenseAttributes: { [key]: value } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes) |
| [Category exclusion](https://developers.google.com/publisher-tag/guides/config-migration#set-page-category) | `clearCategoryExclusions()` | [`googletag.setConfig({ categoryExclusion: null })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) |
| [Category exclusion](https://developers.google.com/publisher-tag/guides/config-migration#set-page-category) | `setCategoryExclusion(label)` | [`googletag.setConfig({ categoryExclusion: [label] })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) |
| [Centering](https://developers.google.com/publisher-tag/guides/config-migration#set-page-centering) | `setCentering(centerAds)` | [`googletag.setConfig({ centering: centerAds })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.centering) |
| [Collapse empty divs](https://developers.google.com/publisher-tag/guides/config-migration#set-page-collapse) | `collapseEmptyDivs(collapseBeforeFetch)` | [`googletag.setConfig({ collapseDiv: collapseBeforeFetch ? 'BEFORE_FETCH' : 'ON_NO_FILL' })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv) |
| [Initial load and Single Request Architecture (SRA)](https://developers.google.com/publisher-tag/guides/config-migration#set-page-sra) | `disableInitialLoad()` | [`googletag.setConfig({ disableInitialLoad: true })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad) |
| [Initial load and Single Request Architecture (SRA)](https://developers.google.com/publisher-tag/guides/config-migration#set-page-sra) | `enableSingleRequest()` | [`googletag.setConfig({ singleRequest: true })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) |
| [Lazy loading](https://developers.google.com/publisher-tag/guides/config-migration#set-page-lazyload) | `enableLazyLoad(config)` | [`googletag.setConfig({ lazyLoad: config })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad) |
| [Location](https://developers.google.com/publisher-tag/guides/config-migration#set-page-location) | `setLocation(address)` | [`googletag.setConfig({ location: address })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.location) |
| [SafeFrame](https://developers.google.com/publisher-tag/guides/config-migration#set-page-safeframe) | `setForceSafeFrame(force)` | [`slot.setConfig({ safeFrame: { forceSafeFrame: force } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) |
| [SafeFrame](https://developers.google.com/publisher-tag/guides/config-migration#set-page-safeframe) | `setSafeFrameConfig(config)` | [`slot.setConfig({ safeFrame: config })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#set-page-targeting) | `clearTargeting(key)` | [`googletag.setConfig({ targeting: { [key]: null } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#set-page-targeting) | `setTargeting(key, value)` | [`googletag.setConfig({ targeting: { [key]: value } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) |
| [Video ads](https://developers.google.com/publisher-tag/guides/config-migration#set-page-video) | `enableVideoAds()` | [`googletag.setConfig({ videoAds: { enableVideoAds: true } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) |
| [Video ads](https://developers.google.com/publisher-tag/guides/config-migration#set-page-video) | `setVideoContent(contentId, cmsId)` | [`googletag.setConfig({ videoAds: { videoContentId: contentId, videoCmsId: cmsId } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) |

### AdSense attributes

Legacy:

    googletag.pubads().set('document_language', 'en');

New:

    googletag.setConfig({
      adsenseAttributes: {
        document_language: 'en'
      }
    });

*** ** * ** ***

### Category exclusion

Legacy:

    googletag.pubads().setCategoryExclusion('AirlineAd');
    googletag.pubads().clearCategoryExclusions();

New:

    // Set category exclusion
    googletag.setConfig({
      categoryExclusion: ['AirlineAd']
    });

    // Clear category exclusions
    googletag.setConfig({
      categoryExclusion: null
    });

*** ** * ** ***

### Centering

Legacy:

    googletag.pubads().setCentering(true);

New:

    googletag.setConfig({
      centering: true
    });

*** ** * ** ***

### Collapse empty divs

Legacy:

    googletag.pubads().collapseEmptyDivs(true); // Collapse before fetch
    googletag.pubads().collapseEmptyDivs(false); // Collapse on no fill

New:

    // Collapse before fetch
    googletag.setConfig({
      collapseDiv: 'BEFORE_FETCH'
    });

    // Collapse on no fill
    googletag.setConfig({
      collapseDiv: 'ON_NO_FILL'
    });

    // Don't collapse
    googletag.setConfig({
      collapseDiv: 'DISABLED'
    });

*** ** * ** ***

### Initial load and Single Request Architecture (SRA)

Legacy:

    googletag.pubads().disableInitialLoad();
    googletag.pubads().enableSingleRequest();

New:

    googletag.setConfig({
      disableInitialLoad: true,
      singleRequest: true
    });

*** ** * ** ***

### Lazy loading

Legacy:

    googletag.pubads().enableLazyLoad({
      // Fetch slots within 5 viewports.
      fetchMarginPercent: 500,
      // Render slots within 2 viewports.
      renderMarginPercent: 200,
      // Double the above values on mobile.
      mobileScaling: 2.0,
    });

New:

    googletag.setConfig({
      lazyLoad: {
        // Fetch slots within 5 viewports.
        fetchMarginPercent: 500,
        // Render slots within 2 viewports.
        renderMarginPercent: 200,
        // Double the above values on mobile.
        mobileScaling: 2.0,
      },
    });

*** ** * ** ***

### Location

Legacy:

    googletag.pubads().setLocation('10001,US');

New:

    googletag.setConfig({
      location: '10001,US'
    });

*** ** * ** ***

### SafeFrame

Legacy:

    googletag.pubads().setForceSafeFrame(true);
    googletag.pubads().setSafeFrameConfig({sandbox: true});

New:

    googletag.pubads().setConfig({
      safeFrame: {
        forceSafeFrame: true,
        sandbox: true
      }
    });

*** ** * ** ***

### Targeting

Legacy:

    googletag.pubads().setTargeting('interests', 'sports');
    googletag.pubads().setTargeting('interests', ['sports', 'music']);
    googletag.pubads().clearTargeting('interests');
    googletag.pubads().clearTargeting();

New:

    // Set targeting
    googletag.setConfig({
      targeting: {
        interests: 'sports'
      }
    });

    // Set multiple values
    googletag.setConfig({
      targeting: {
        interests: ['sports', 'music']
      }
    });

    // Clear a specific key
    googletag.setConfig({
      targeting: {
        interests: null
      }
    });

    // Clear all targeting
    googletag.setConfig({
      targeting: null
    });

*** ** * ** ***

### Video ads

Legacy:

    googletag.pubads().enableVideoAds();
    googletag.pubads().setVideoContent('video123', 'cms456');

New:

    googletag.setConfig({
      videoAds: {
        enableVideoAds: true,
        videoContentId: 'video123',
        videoCmsId: 'cms456'
      }
    });

*** ** * ** ***

## Set slot-level configuration

The following table maps legacy `Slot` configuration methods to their
`setConfig` replacements.

| Feature | Legacy method | `setConfig` replacement |
|---|---|---|
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-adsense) | `set(key, value)` | [`Slot.setConfig({ adsenseAttributes: { [key]: value } })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes) |
| [Category exclusion](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-category) | `clearCategoryExclusions()` | [`Slot.setConfig({ categoryExclusion: null })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) |
| [Category exclusion](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-category) | `setCategoryExclusion(label)` | [`Slot.setConfig({ categoryExclusion: [label] })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) |
| [Click URL](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-clickurl) | `setClickUrl(url)` | [`Slot.setConfig({ clickUrl: url })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.clickUrl) |
| [Collapse empty divs](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-collapse) | `setCollapseEmptyDiv(collapse, collapseBeforeFetch)` | [`Slot.setConfig({ collapseDiv: collapse ? (collapseBeforeFetch ? 'BEFORE_FETCH' : 'ON_NO_FILL') : 'DISABLED' })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv) |
| [SafeFrame](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-safeframe) | `setForceSafeFrame(force)` | [`Slot.setConfig({ safeFrame: { forceSafeFrame: force } })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) |
| [SafeFrame](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-safeframe) | `setSafeFrameConfig(config)` | [`Slot.setConfig({ safeFrame: config })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-targeting) | `clearTargeting(key)` | [`Slot.setConfig({ targeting: { [key]: null } })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-targeting) | `setTargeting(key, value)` | [`Slot.setConfig({ targeting: { [key]: value } })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#set-slot-targeting) | `updateTargetingFromMap(config)` | [`Slot.setConfig({ targeting: config })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) |

### AdSense attributes

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.set('adsense_background_color', '#FFFFFF');

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');

    slot.setConfig({
      adsenseAttributes: {
        adsense_background_color: '#FFFFFF'
      }
    });

*** ** * ** ***

### Category exclusion

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setCategoryExclusion('AirlineAd');
    slot.clearCategoryExclusions();

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');

    // Set category exclusion
    slot.setConfig({
      categoryExclusion: ['AirlineAd']
    });

    // Clear category exclusions
    slot.setConfig({
      categoryExclusion: null
    });

*** ** * ** ***

### Click URL

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setClickUrl('http://www.example.com?original_click_url=');

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');

    slot.setConfig({
      clickUrl: 'http://www.example.com?original_click_url='
    });

*** ** * ** ***

### Collapse empty div

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setCollapseEmptyDiv(true, true); // Collapse before fetch

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');

    slot.setConfig({
      collapseDiv: 'BEFORE_FETCH'
    });

*** ** * ** ***

### SafeFrame

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setForceSafeFrame(true);
    slot.setSafeFrameConfig({sandbox: true});

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setConfig({
      safeFrame: {
        forceSafeFrame: true,
        sandbox: true
      }
    });

*** ** * ** ***

### Targeting

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    slot.setTargeting('allow_expandable', 'true');
    slot.clearTargeting('allow_expandable');
    slot.updateTargetingFromMap({
      color: 'red',
      interests: ['sports', 'music', 'movies']
    });

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');

    // Set targeting
    slot.setConfig({
      targeting: {
        allow_expandable: 'true'
      }
    });

    // Clear targeting
    slot.setConfig({
      targeting: {
        allow_expandable: null
      }
    });

    // Update targeting (only specified KVs are set/modified).
    slot.setConfig({
      targeting: {
        color: 'red',
        interests: ['sports', 'music', 'movies']
      }
    })

*** ** * ** ***

## Get page-level configuration

The following table maps legacy `PubAdsService` getter methods to their
`getConfig` replacements.

| Feature | Legacy method | `setConfig` replacement |
|---|---|---|
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#get-page-adsense) | `get(key)` | [`googletag.getConfig('adsenseAttributes')`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#get-page-adsense) | `getAttributeKeys()` | [`googletag.getConfig('adsenseAttributes')`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |
| [Initial load](https://developers.google.com/publisher-tag/guides/config-migration#get-page-initialload) | `isInitialLoadDisabled()` | [`googletag.getConfig('disableInitialLoad')`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#get-page-targeting) | `getTargeting(key)` | [`googletag.getConfig('targeting')`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#get-page-targeting) | `getTargetingKeys()` | [`googletag.getConfig('targeting')`](https://developers.google.com/publisher-tag/reference#googletag.getConfig) |

### AdSense attributes

Legacy:

    const documentLangauage = googletag.pubads().get('document_language');
    const adsenseAttributes = googletag.pubads().getAttributeKeys();

New:

    const adsenseConfig = googletag.getConfig('adsenseAttributes').adsenseAttributes;

    // Get the value of a single AdSense attribute.
    const documentLanguage = adsenseConfig.document_language || null;

    // Get all configured AdSense attribute keys.
    const adsenseAttributes = Object.keys(adsenseConfig);

*** ** * ** ***

### Initial load

Legacy:

    const isDisabled = googletag.pubads().isInitialLoadDisabled();

New:

    const isDisabled = googletag.getConfig('disableInitialLoad').disableInitialLoad;

*** ** * ** ***

### Targeting

Legacy:

    const targeting = googletag.pubads().getTargeting('interests');
    const keys = googletag.pubads().getTargetingKeys();

New:

    const targetingConfig = googletag.getConfig('targeting').targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig.interests || [];

    // Get all targeting keys.
    const keys = Object.keys(targetingConfig);

*** ** * ** ***

## Get slot-level configuration

The following table maps legacy `Slot` getter methods to their `getConfig`
replacements.

| Feature | Legacy method | `setConfig` replacement |
|---|---|---|
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#get-slot-adsense) | `get(key)` | [`Slot.getConfig('adsenseAttributes')`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |
| [AdSense attributes](https://developers.google.com/publisher-tag/guides/config-migration#get-slot-adsense) | `getAttributeKeys()` | [`Slot.getConfig('adsenseAttributes')`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |
| [Category exclusion](https://developers.google.com/publisher-tag/guides/config-migration#get-slot-category) | `getCategoryExclusions()` | [`Slot.getConfig('categoryExclusion')`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#get-slot-targeting) | `getTargeting(key)` | [`Slot.getConfig('targeting')`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |
| [Targeting](https://developers.google.com/publisher-tag/guides/config-migration#get-slot-targeting) | `getTargetingKeys()` | [`Slot.getConfig('targeting')`](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) |

### AdSense attributes

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const bgColor = slot.get('adsense_background_color');
    const adsenseAttributes = slot.getAttributeKeys();

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const adsenseConfig = slot.getConfig('adsenseAttributes').adsenseAttributes;

    // Get the value of a single AdSense attribute.
    const bgColor = adsenseConfig.adsense_background_color || null;

    // Get all configured AdSense attribute.
    const adsenseAttributes = Object.keys(adsenseConfig);

*** ** * ** ***

### Category exclusion

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const exclusions = slot.getCategoryExclusions();

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const exclusions = slot.getConfig('categoryExclusion').categoryExclusion || [];

*** ** * ** ***

### Targeting

Legacy:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const targeting = slot.getTargeting('allow_expandable');
    const keys = slot.getTargetingKeys();

New:

    const slot = googletag.defineSlot('/1234567/sports', [160, 600], 'div');
    const targetingConfig = slot.getConfig('targeting').targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig.allow_expandable || [];

    // Get all targeting keys.
    const keys = Object.keys(targetingConfig);

*** ** * ** ***