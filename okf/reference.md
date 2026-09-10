---
type: API Reference
title: "Google Publisher Tag API Reference"
description: "Complete TypeScript API reference for googletag namespace, interfaces, enums, and events."
resource: "https://developers.google.com/publisher-tag/reference"
tags: [gpt, api, reference, typescript, googletag]
timestamp: 2026-09-10T00:00:00Z
---

This reference uses TypeScript notation to describe types. The following table provides a
brief explanation by example.

| Type expression ||
|---|---|
| `string` | The primitive string type. |
| `string[]` | An array type, where values may only be strings. |
| `number | string` | A union type, where the value may be either a number or a string. |
| `Array<number | string>` | An array type, where values are a complex (union) type. |
| `[number, string]` | A tuple type, where the value is a two-element array that must contain a number and a string in that order. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | An object type, where the value is an instance of `googletag.Slot`. |
| `() => void` | A function type with no defined arguments and no return value. |


To learn more about supported types and type expressions, refer to the
[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html).

#### Type annotations


A colon after a variable, parameter name, property name, or function signature denotes a
type annotation. Type annotations describe the types the element to the left of the colon
can accept or return. The following table shows examples of type annotations you may see in
this reference.

| Type annotation ||
|---|---|
| `param: string` | Indicates that `param` accepts or returns a string value. This syntax is used for variables, parameters, properties, and return types. |
| `param?: number | string` | Indicates that `param` is optional, but accepts either a number or a string when specified. This syntax is used for parameters and properties. |
| `...params: Array<() => void>` | Indicates that `params` is a [rest parameter](https://www.typescriptlang.org/docs/handbook/2/functions.html#rest-parameters) that accepts functions. Rest parameters accept an unbounded number of values of the specified type. |

*** ** * ** ***

## googletag

The global namespace the Google Publisher Tag uses for its API.

| Namespaces ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config` | Main configuration interface for page-level settings. |
| `https://developers.google.com/publisher-tag/reference#googletag.enums` | This is the namespace that GPT uses for enum types. |
| `https://developers.google.com/publisher-tag/reference#googletag.events` | This is the namespace that GPT uses for Events. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals` | This is the namespace that GPT uses for managing secure signals. |

| Interfaces ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.CommandArray` | The command array accepts a sequence of functions and invokes them in order. |
| `https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService` | Companion Ads service. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig` | Configuration object for privacy settings. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | Publisher Ads service. |
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation` | An object representing a single ad response. |
| `https://developers.google.com/publisher-tag/reference#googletag.RewardedPayload` | An object representing the reward associated with a [rewarded ad](https://support.google.com/admanager/answer/9116812). |
| `https://developers.google.com/publisher-tag/reference#googletag.Service` | Base service class that contains methods common for all services. |
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder` | Builder for size mapping specification objects. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | Slot is an object representing a single ad slot on a page. |

| Type Aliases ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.FluidSize` | The size string where the ad container takes 100% width of its parent div and then resizes its height to fit the creative content. |
| `https://developers.google.com/publisher-tag/reference#googletag.GeneralSize` | A valid size configuration for a slot, which can be one or multiple sizes. |
| `https://developers.google.com/publisher-tag/reference#googletag.MultiSize` | A list of single valid sizes. |
| `https://developers.google.com/publisher-tag/reference#googletag.NamedSize` | Named sizes that a slot can have. |
| `https://developers.google.com/publisher-tag/reference#googletag.SingleSize` | A single valid size for a slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray` | Array of two numbers representing \[width, height\]. |
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMapping` | A mapping of viewport size to ad sizes. |
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingArray` | A list of size mappings. |

| Variables ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.apiReady` | Flag indicating that the GPT API is loaded and ready to be called. |
| `https://developers.google.com/publisher-tag/reference#googletag.cmd` | Reference to the global command queue for asynchronous execution of GPT-related calls. |
| `https://developers.google.com/publisher-tag/reference#googletag.pubadsReady` | Flag indicating that [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService) is enabled, loaded and fully operational. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignalProviders` | Reference to the secure signal providers array. |

| Functions ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.companionAds` | Returns a reference to the [CompanionAdsService](https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService). |
| `https://developers.google.com/publisher-tag/reference#googletag.defineOutOfPageSlot` | Constructs an out-of-page ad slot with the given ad unit path. |
| `https://developers.google.com/publisher-tag/reference#googletag.defineSlot` | Constructs an ad slot with a given ad unit path and size and associates it with the ID of a div element on the page that will contain the ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.destroySlots` | Destroys the given slots, removing all related objects and references of those slots from GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.disablePublisherConsole` | Disables the Google Publisher Console. |
| `https://developers.google.com/publisher-tag/reference#googletag.display` | Instructs slot services to render the slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.enableServices` | Enables all GPT services that have been defined for ad slots on the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.getConfig` | Gets a frozen copy of the general configuration options for the page set by [setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig). |
| `https://developers.google.com/publisher-tag/reference#googletag.getVersion` | Returns the current version of GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.openConsole` | Opens the Google Publisher Console. |
| `https://developers.google.com/publisher-tag/reference#googletag.pubads` | Returns a reference to the [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService). |
| `https://developers.google.com/publisher-tag/reference#googletag.setAdIframeTitle` | Sets the title for all ad container iframes created by [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService), from this point onwards. |
| `https://developers.google.com/publisher-tag/reference#googletag.setConfig` | Sets general configuration options for the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.sizeMapping` | Creates a new [SizeMappingBuilder](https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder). |

### Type Aliases

*** ** * ** ***

#### FluidSize

`FluidSize: "fluid"`The size string where the ad container takes 100% width of its parent div and then resizes its height to fit the creative content. Similar to how regular block elements on a page behave. Used for native and banner ads (see [related article](https://support.google.com/admanager/answer/6366845)).

*** ** * ** ***

#### GeneralSize

`GeneralSize: https://developers.google.com/publisher-tag/reference#googletag.SingleSize | https://developers.google.com/publisher-tag/reference#googletag.MultiSize`A valid size configuration for a slot, which can be one or multiple sizes.

*** ** * ** ***

#### MultiSize

`MultiSize: https://developers.google.com/publisher-tag/reference#googletag.SingleSize[]`A list of single valid sizes.

*** ** * ** ***

#### NamedSize

`NamedSize: https://developers.google.com/publisher-tag/reference#googletag.FluidSize | [https://developers.google.com/publisher-tag/reference#googletag.FluidSize]`Named sizes that a slot can have. In most cases size is a fixed-size rectangle but there are some cases when we need other kinds of size specifications. Only the following are valid named sizes:

- **fluid** : the ad container takes 100% width of its parent div and then resizes its height to fit the creative content. Similar to how regular block elements on a page behave. Used for native and banner ads (see [related article](https://support.google.com/admanager/answer/6366845)). Note that both `fluid` and `['fluid']` are acceptable forms to declare a slot size as fluid.

*** ** * ** ***

#### SingleSize

`SingleSize: https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray | https://developers.google.com/publisher-tag/reference#googletag.NamedSize`A single valid size for a slot.

*** ** * ** ***

#### SingleSizeArray

`SingleSizeArray: [number, number]`Array of two numbers representing \[width, height\].

*** ** * ** ***

#### SizeMapping

`SizeMapping: [https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray, https://developers.google.com/publisher-tag/reference#googletag.GeneralSize]`A mapping of viewport size to ad sizes. Used for responsive ads.

*** ** * ** ***

#### SizeMappingArray

`SizeMappingArray: https://developers.google.com/publisher-tag/reference#googletag.SizeMapping[]`A list of size mappings.

### Variables

*** ** * ** ***

#### `Const` apiReady

`apiReady: boolean | undefined`Flag indicating that the GPT API is loaded and ready to be called. This property will be simply `undefined` until the API is ready.  

Note that the recommended way of handling async is to use [googletag.cmd](https://developers.google.com/publisher-tag/reference#googletag.cmd) to queue callbacks for when GPT is ready. These callbacks do not have to check googletag.apiReady as they are guaranteed to execute once the API is set up.

*** ** * ** ***

#### `Const` cmd

`cmd: ((this: typeof globalThis) => void)[] | https://developers.google.com/publisher-tag/reference#googletag.CommandArray`Reference to the global command queue for asynchronous execution of GPT-related calls.  

The `googletag.cmd` variable is initialized to an empty JavaScript array by the GPT tag syntax on the page, and `cmd.push` is the standard `Array.push` method that adds an element to the end of the array. When the GPT JavaScript is loaded, it looks through the array and executes all the functions in order. The script then replaces `cmd` with a [CommandArray](https://developers.google.com/publisher-tag/reference#googletag.CommandArray) object whose push method is defined to execute the function argument passed to it. This mechanism allows GPT to reduce perceived latency by fetching the JavaScript asynchronously while allowing the browser to continue rendering the page.

Example
:

    ### JavaScript

    ```javascript
    googletag.cmd.push(() => {
      googletag.defineSlot("/1234567/sports", [160, 600]).addService(googletag.pubads());
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.cmd.push(function () {
      googletag.defineSlot("/1234567/sports", [160, 600]).addService(googletag.pubads());
    });
    ```

    ### TypeScript

    ```typescript
    googletag.cmd.push(() => {
      googletag.defineSlot("/1234567/sports", [160, 600])!.addService(googletag.pubads());
    });
    ```

*** ** * ** ***

#### `Const` pubadsReady

`pubadsReady: boolean | undefined`Flag indicating that [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService) is enabled, loaded and fully operational. This property will be simply `undefined` until [enableServices](https://developers.google.com/publisher-tag/reference#googletag.enableServices) is called and [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService) is loaded and initialized.

*** ** * ** ***

#### secureSignalProviders

`secureSignalProviders: https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider[] | https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvidersArray | undefined`Reference to the secure signal providers array.  

The secure signal providers array accepts a sequence of signal-generating functions and invokes them in order. It is intended to replace a standard array that is used to enqueue signal-generating functions to be invoked once GPT is loaded.

Example
:

    ### JavaScript

    ```javascript
    window.googletag = window.googletag || { cmd: [] };
    googletag.secureSignalProviders = googletag.secureSignalProviders || [];
    googletag.secureSignalProviders.push({
      id: "collector123",
      collectorFunction: () => {
        return Promise.resolve("signal");
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    window.googletag = window.googletag || { cmd: [] };
    googletag.secureSignalProviders = googletag.secureSignalProviders || [];
    googletag.secureSignalProviders.push({
      id: "collector123",
      collectorFunction: function () {
        return Promise.resolve("signal");
      },
    });
    ```

    ### TypeScript

    ```typescript
    window.googletag = window.googletag || { cmd: [] };
    googletag.secureSignalProviders = googletag.secureSignalProviders || [];
    googletag.secureSignalProviders.push({
      id: "collector123",
      collectorFunction: () => {
        return Promise.resolve("signal");
      },
    });
    ```

See also
:
    - [Share secure signals with bidders](https://support.google.com/admanager/answer/10488752)

### Functions

*** ** * ** ***

#### companionAds

`companionAds(): https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService`Returns a reference to the [CompanionAdsService](https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService).

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService` | The Companion Ads service. |

*** ** * ** ***

#### defineOutOfPageSlot

`defineOutOfPageSlot(adUnitPath: string, div?: string | https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat): https://developers.google.com/publisher-tag/reference#googletag.Slot | null`Constructs an out-of-page ad slot with the given ad unit path.  

For custom out-of-page ads, `div` is the ID of the div element that will contain the ad. See the article on [out-of-page creatives](https://support.google.com/admanager/answer/6088046) for more details.  

For GPT managed out-of-page ads, `div` is a supported [OutOfPageFormat](https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat).

Example
:

    ### JavaScript

    ```javascript
    // Define a custom out-of-page ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", "div-1");

    // Define a GPT managed web interstitial ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", googletag.enums.OutOfPageFormat.INTERSTITIAL);
    ```

    ### JavaScript (legacy)

    ```javascript
    // Define a custom out-of-page ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", "div-1");

    // Define a GPT managed web interstitial ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", googletag.enums.OutOfPageFormat.INTERSTITIAL);
    ```

    ### TypeScript

    ```typescript
    // Define a custom out-of-page ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", "div-1");

    // Define a GPT managed web interstitial ad slot.
    googletag.defineOutOfPageSlot("/1234567/sports", googletag.enums.OutOfPageFormat.INTERSTITIAL);
    ```

See also
:
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)
    - [Display a web interstitial ad](https://developers.google.com/publisher-tag/samples/display-web-interstitial-ad)
    - [Display an anchor ad](https://developers.google.com/publisher-tag/samples/display-anchor-ad)
    - [Display an out-of-page ad](https://developers.google.com/publisher-tag/samples/display-out-of-page-ad)

| Parameters ||
|---|---|
| `adUnitPath: string` | Full [ad unit path](https://developers.google.com/publisher-tag/guides/get-started#ad-unit-path) with the network code and ad unit code. |
| `` `Optional` div: string | https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat `` | ID of the div that will contain this ad unit or OutOfPageFormat. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot | null` | The newly created slot, or `null` if a slot cannot be created. |

*** ** * ** ***

#### defineSlot

`defineSlot(adUnitPath: string, size: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize, div?: string): https://developers.google.com/publisher-tag/reference#googletag.Slot | null`Constructs an ad slot with a given ad unit path and size and associates it with the ID of a div element on the page that will contain the ad.

Example
:

    ### JavaScript

    ```javascript
    googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    ```

    ### TypeScript

    ```typescript
    googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    ```

See also
:
    - [Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started)

| Parameters ||
|---|---|
| `adUnitPath: string` | Full [ad unit path](https://developers.google.com/publisher-tag/guides/get-started#ad-unit-path) with the network code and unit code. |
| `size: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize` | Width and height of the added slot. This is the size that is used in the ad request if no responsive size mapping is provided or the size of the viewport is smaller than the smallest size provided in the mapping. |
| `` `Optional` div: string `` | ID of the div that will contain this ad unit. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot | null` | The newly created slot, or `null` if a slot cannot be created. |

*** ** * ** ***

#### destroySlots

`destroySlots(slots?: https://developers.google.com/publisher-tag/reference#googletag.Slot[]): boolean`Destroys the given slots, removing all related objects and references of those slots from GPT. This API does not support passback slots and companion slots.  

Calling this API on a slot clears the ad and removes the slot object from the internal state maintained by GPT. Calling any more functions on the slot object will result in undefined behavior. Note the browser may still not free the memory associated with that slot if a reference to it is maintained by the publisher page. Calling this API makes the div associated with that slot available for reuse.  

In particular, destroying a slot removes the ad from GPT's [long-lived pageview](https://support.google.com/admanager/answer/183281), so future requests will not be influenced by roadblocks or competitive exclusions involving this ad. Failure to call this function before removing a slot's div from the page will result in undefined behavior.

Example
:

    ### JavaScript

    ```javascript
    // The calls to construct an ad and display contents.
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to destroy only slot1.
    googletag.destroySlots([slot1]);

    // This call to destroy both slot1 and slot2.
    googletag.destroySlots([slot1, slot2]);

    // This call to destroy all slots.
    googletag.destroySlots();
    ```

    ### JavaScript (legacy)

    ```javascript
    // The calls to construct an ad and display contents.
    var slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    var slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to destroy only slot1.
    googletag.destroySlots([slot1]);

    // This call to destroy both slot1 and slot2.
    googletag.destroySlots([slot1, slot2]);

    // This call to destroy all slots.
    googletag.destroySlots();
    ```

    ### TypeScript

    ```typescript
    // The calls to construct an ad and display contents.
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1")!;
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2")!;
    googletag.display("div-2");

    // This call to destroy only slot1.
    googletag.destroySlots([slot1]);

    // This call to destroy both slot1 and slot2.
    googletag.destroySlots([slot1, slot2]);

    // This call to destroy all slots.
    googletag.destroySlots();
    ```

| Parameters ||
|---|---|
| `` `Optional` slots: https://developers.google.com/publisher-tag/reference#googletag.Slot[] `` | The array of slots to destroy. Array is optional; all slots will be destroyed if it is unspecified. |

| Returns ||
|---|---|
| `boolean` | `true` if slots have been destroyed, `false` otherwise. |

*** ** * ** ***

#### disablePublisherConsole

`disablePublisherConsole(): void`Disables the Google Publisher Console.

See also
:
    - [Google Publisher Console](https://developers.google.com/publisher-tag/guides/publisher-console)

*** ** * ** ***

#### display

`display(divOrSlot: string | Element | https://developers.google.com/publisher-tag/reference#googletag.Slot): void`Instructs slot services to render the slot. Each ad slot should only be displayed once per page. All slots must be defined and have a service associated with them before being displayed. The display call must not happen until the element is present in the DOM. The usual way to achieve that is to place it within a script block within the div element named in the method call.  

If single request architecture (SRA) is being used, all unfetched ad slots at the time this method is called will be fetched at once. To force an ad slot not to display, the entire div must be removed.

See also
:
    - [Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started)
    - [Display a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad)
    - [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading)

| Parameters ||
|---|---|
| `divOrSlot: string | Element | https://developers.google.com/publisher-tag/reference#googletag.Slot` | Either the ID of the div element containing the ad slot or the div element, or the slot object. If a div element is provided, it must have an 'id' attribute which matches the ID passed into [defineSlot](https://developers.google.com/publisher-tag/reference#googletag.defineSlot). |

*** ** * ** ***

#### enableServices

`enableServices(): void`Enables all GPT services that have been defined for ad slots on the page.

*** ** * ** ***

#### getConfig

`getConfig(keys: string | string[]): Readonly<Pick<https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig, "adsenseAttributes" | "disableInitialLoad" | "targeting">>`Gets a frozen copy of the general configuration options for the page set by [setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig).  

Not all `setConfig()` properties are supported by this method. Supported properties are:

- [`adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes)
- [`disableInitialLoad`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad)
- [`targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting)

Example
:

    ### JavaScript

    ```javascript
    // Get the value of the `targeting` setting.
    const targetingConfig = googletag.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `disableInitialLoad` settings.
    const config = googletag.getConfig(["adsenseAttributes", "disableInitialLoad"]);
    ```

    ### JavaScript (legacy)

    ```javascript
    // Get the value of the `targeting` setting.
    var targetingConfig = googletag.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `disableInitialLoad` settings.
    var config = googletag.getConfig(["adsenseAttributes", "disableInitialLoad"]);
    ```

    ### TypeScript

    ```typescript
    // Get the value of the `targeting` setting.
    const targetingConfig = googletag.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `disableInitialLoad` settings.
    const config = googletag.getConfig(["adsenseAttributes", "disableInitialLoad"]);
    ```

| Parameters ||
|---|---|
| `keys: string | string[]` | The keys of the configuration options to get. |

| Returns ||
|---|---|
| `Readonly<Pick<https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig, "adsenseAttributes" | "disableInitialLoad" | "targeting">>` | A frozen copy of the configuration options for the page. |

*** ** * ** ***

#### getVersion

`getVersion(): string`Returns the current version of GPT.

See also
:
    - [GPT version history](https://developers.google.com/publisher-tag/versions)

| Returns ||
|---|---|
| `string` | The currently executing GPT version string. |

*** ** * ** ***

#### openConsole

`openConsole(div?: string): void`Opens the Google Publisher Console.

Example
:

    ### JavaScript

    ```javascript
    // Calling with div ID.
    googletag.openConsole("div-1");

    // Calling without div ID.
    googletag.openConsole();
    ```

    ### JavaScript (legacy)

    ```javascript
    // Calling with div ID.
    googletag.openConsole("div-1");

    // Calling without div ID.
    googletag.openConsole();
    ```

    ### TypeScript

    ```typescript
    // Calling with div ID.
    googletag.openConsole("div-1");

    // Calling without div ID.
    googletag.openConsole();
    ```

See also
:
    - [Google Publisher Console](https://developers.google.com/publisher-tag/guides/publisher-console)

| Parameters ||
|---|---|
| `` `Optional` div: string `` | An ad slot div ID. This value is optional. When provided, the Publisher Console will attempt to open with details of the specified ad slot in view. |

*** ** * ** ***

#### pubads

`pubads(): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Returns a reference to the [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The Publisher Ads service. |

*** ** * ** ***

#### setAdIframeTitle

`setAdIframeTitle(title: string): void`Sets the title for all ad container iframes created by [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService), from this point onwards.

Example
:

    ### JavaScript

    ```javascript
    googletag.setAdIframeTitle("title");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setAdIframeTitle("title");
    ```

    ### TypeScript

    ```typescript
    googletag.setAdIframeTitle("title");
    ```

| Parameters ||
|---|---|
| `title: string` | The new title for all ad container iframes. |

*** ** * ** ***

#### setConfig

`setConfig(config: https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig): void`Sets general configuration options for the page.

| Parameters ||
|---|---|
| `config: https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig` |   |

*** ** * ** ***

#### sizeMapping

`sizeMapping(): https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder`Creates a new [SizeMappingBuilder](https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder).

See also
:
    - [Ad sizes: Responsive ads](https://developers.google.com/publisher-tag/guides/ad-sizes#responsive_ads)

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder` | A new builder. |

*** ** * ** ***

## googletag.CommandArray

The command array accepts a sequence of functions and invokes them in order. It is intended to replace a standard array that is used to enqueue functions to be invoked once GPT is loaded.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.CommandArray.push` | Executes the sequence of functions specified in the arguments in order. |

### Methods

*** ** * ** ***

#### push

`push(...f: ((this: typeof globalThis) => void)[]): number`Executes the sequence of functions specified in the arguments in order.

Example
:

    ### JavaScript

    ```javascript
    googletag.cmd.push(() => {
      googletag.defineSlot("/1234567/sports", [160, 600]).addService(googletag.pubads());
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.cmd.push(function () {
      googletag.defineSlot("/1234567/sports", [160, 600]).addService(googletag.pubads());
    });
    ```

    ### TypeScript

    ```typescript
    googletag.cmd.push(() => {
      googletag.defineSlot("/1234567/sports", [160, 600])!.addService(googletag.pubads());
    });
    ```

| Parameters ||
|---|---|
| `` `Rest` ...f: ((this: typeof globalThis) => void)[] `` | A JavaScript function to be executed. The runtime binding will always be [`globalThis`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/globalThis). Consider passing an arrow function to retain the `this` value of the enclosing lexical context. |

| Returns ||
|---|---|
| `number` | The number of commands processed so far. This is compatible with `Array.push`'s return value (the current length of the array). |

*** ** * ** ***

## googletag.CompanionAdsService

Extends `https://developers.google.com/publisher-tag/reference#googletag.Service`Companion Ads service. This service is used by video ads to show companion ads.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener` | Registers a listener that allows you to set up and call a JavaScript function when a specific GPT event happens on the page. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener` method |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.getSlots` | Get the list of slots associated with this service. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.getSlots` method |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener` | Removes a previously registered listener. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener` method |
| `https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.setRefreshUnfilledSlots` | Sets whether companion slots that have not been filled will be automatically backfilled. |

See also
:
    - [Companion ads for video and audio](https://support.google.com/admanager/answer/1191131)

### Methods

*** ** * ** ***

#### setRefreshUnfilledSlots

`setRefreshUnfilledSlots(value: boolean): void`Sets whether companion slots that have not been filled will be automatically backfilled.  

This method can be called multiple times during the page's lifetime to turn backfill on and off. Only slots that are also registered with the [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService) will be backfilled. Due to policy restrictions, this method is not designed to fill empty companion slots when an Ad Exchange video is served.

Example
:

    ### JavaScript

    ```javascript
    googletag.companionAds().setRefreshUnfilledSlots(true);
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.companionAds().setRefreshUnfilledSlots(true);
    ```

    ### TypeScript

    ```typescript
    googletag.companionAds().setRefreshUnfilledSlots(true);
    ```

| Parameters ||
|---|---|
| `value: boolean` | `true` to automatically backfill unfilled slots, `false` to leave them unchanged. |

*** ** * ** ***

## googletag.PrivacySettingsConfig

Configuration object for privacy settings.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.childDirectedTreatment` | Indicates whether the page should be [treated as child-directed](https://support.google.com/admanager/answer/3671211). |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.limitedAds` | Enables serving to run in [limited ads](https://support.google.com/admanager/answer/9882911) mode to aid in publisher regulatory compliance needs. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.nonPersonalizedAds` | Enables serving to run in [non-personalized ads](https://support.google.com/admanager/answer/9005435) mode to aid in publisher regulatory compliance needs. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.restrictDataProcessing` | Enables serving to run in [restricted processing mode](https://support.google.com/admanager/answer/9598414) to aid in publisher regulatory compliance needs. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.tagForAgeTreatment` | The age-restricted treatment, indicating whether the ad request should be treated as child, teen, or unspecified. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.trafficSource` | Indicates whether requests represent purchased or organic traffic. |
| `https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.underAgeOfConsent` | Indicates whether to mark ad requests as coming from users [under the age of consent](https://support.google.com/admanager/answer/9004919). |

See also
:
    - [Configure privacy settings](https://developers.google.com/publisher-tag/samples/configure-privacy)

### Properties

*** ** * ** ***

#### `Optional` childDirectedTreatment

`childDirectedTreatment?: boolean`Indicates whether the page should be [treated as child-directed](https://support.google.com/admanager/answer/3671211). Set to `null` to clear the configuration.

*** ** * ** ***

#### `Optional` limitedAds

`limitedAds?: boolean`Enables serving to run in [limited ads](https://support.google.com/admanager/answer/9882911) mode to aid in publisher regulatory compliance needs.  

You can instruct GPT to request limited ads in two ways:

- Automatically, by using a signal from an [IAB TCF v2.0](https://iabeurope.eu/tcf-2-0/) consent management platform.
- Manually, by setting the value of this field to `true`.

Manually configuring limited ads is only possible when GPT is loaded from the [limited ads URL](https://developers.google.com/publisher-tag/guides/general-best-practices#load_from_an_official_source). Attempting to modify this setting when GPT has been loaded from the standard URL will generate a [Publisher Console warning](http://developers.google.com/publisher-tag/guides/publisher-console-messages#147).  

Note that it is not necessary to manually enable limited ads when a CMP is in use.

Example
:

    ### JavaScript

    ```javascript
    // Manually enable limited ads serving.
    // GPT must be loaded from the limited ads URL to configure this setting.
    googletag.pubads().setPrivacySettings({
      limitedAds: true,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Manually enable limited ads serving.
    // GPT must be loaded from the limited ads URL to configure this setting.
    googletag.pubads().setPrivacySettings({
      limitedAds: true,
    });
    ```

    ### TypeScript

    ```typescript
    // Manually enable limited ads serving.
    // GPT must be loaded from the limited ads URL to configure this setting.
    googletag.pubads().setPrivacySettings({
      limitedAds: true,
    });
    ```

See also
:
    - [Display a limited ad](https://developers.google.com/publisher-tag/samples/display-limited-ad)

*** ** * ** ***

#### `Optional` nonPersonalizedAds

`nonPersonalizedAds?: boolean`Enables serving to run in [non-personalized ads](https://support.google.com/admanager/answer/9005435) mode to aid in publisher regulatory compliance needs.

*** ** * ** ***

#### `Optional` restrictDataProcessing

`restrictDataProcessing?: boolean`Enables serving to run in [restricted processing mode](https://support.google.com/admanager/answer/9598414) to aid in publisher regulatory compliance needs.

*** ** * ** ***

#### `Optional` tagForAgeTreatment

`tagForAgeTreatment?: https://developers.google.com/publisher-tag/reference#googletag.enums.TagForAgeTreatment`The age-restricted treatment, indicating whether the ad request should be treated as child, teen, or unspecified.  

Consult your own legal counsel to determine the age treatment settings for your users based on your legal and regulatory requirements. For more information on this setting, review this [Help Center article](https://support.google.com/adsense/answer/9007197).  

By setting this property, you certify that this notification is accurate and you are authorized to act on behalf of the owner of the site. You understand that abuse of this setting may result in termination of your Google account.

Example
:

    ### JavaScript

    ```javascript
    // Enable teen privacy treatment.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.TEEN,
    });

    // Clear age treatment configuration.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.UNSPECIFIED,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Enable teen privacy treatment.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.TEEN,
    });

    // Clear age treatment configuration.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.UNSPECIFIED,
    });
    ```

    ### TypeScript

    ```typescript
    // Enable teen privacy treatment.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.TEEN,
    });

    // Clear age treatment configuration.
    googletag.pubads().setPrivacySettings({
      tagForAgeTreatment: googletag.enums.TagForAgeTreatment.UNSPECIFIED,
    });
    ```

*** ** * ** ***

#### `Optional` trafficSource

`trafficSource?: https://developers.google.com/publisher-tag/reference#googletag.enums.TrafficSource`Indicates whether requests represent purchased or organic traffic. This value populates the [Traffic source](https://support.google.com/admanager/answer/11233407) dimension in Ad Manager reporting. If not set, traffic source defaults to `undefined` in reporting.

Example
:

    ### JavaScript

    ```javascript
    // Indicate requests represent organic traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.ORGANIC,
    });

    // Indicate requests represent purchased traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.PURCHASED,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Indicate requests represent organic traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.ORGANIC,
    });

    // Indicate requests represent purchased traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.PURCHASED,
    });
    ```

    ### TypeScript

    ```typescript
    // Indicate requests represent organic traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.ORGANIC,
    });

    // Indicate requests represent purchased traffic.
    googletag.pubads().setPrivacySettings({
      trafficSource: googletag.enums.TrafficSource.PURCHASED,
    });
    ```

*** ** * ** ***

#### `Optional` underAgeOfConsent

`underAgeOfConsent?: boolean`Indicates whether to mark ad requests as coming from users [under the age of consent](https://support.google.com/admanager/answer/9004919). Set to `null` to clear the configuration.

*** ** * ** ***

## googletag.PubAdsService

Extends `https://developers.google.com/publisher-tag/reference#googletag.Service`Publisher Ads service. This service is used to fetch and show ads from your Google Ad Manager account.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener` | Registers a listener that allows you to set up and call a JavaScript function when a specific GPT event happens on the page. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener` method |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.clear` | Removes the ads from the given slots and replaces them with blank content. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.clearCategoryExclusions` | **Deprecated.**Clears all page-level ad category exclusion labels. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.clearTargeting` | **Deprecated.**Clears custom targeting parameters for a specific key or for all keys. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.collapseEmptyDivs` | **Deprecated.**Enables collapsing of slot divs so that they don't take up any space on the page when there is no ad content to display. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.disableInitialLoad` | **Deprecated.** Disables requests for ads on page load, but allows ads to be requested with a [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh) call. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.display` | Constructs and displays an ad slot with the given ad unit path and size. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.enableLazyLoad` | **Deprecated.**Enables lazy loading in GPT as defined by the config object. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.enableSingleRequest` | **Deprecated.**Enables single request mode for fetching multiple ads at the same time. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.enableVideoAds` | **Deprecated.**Signals to GPT that video ads will be present on the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.get` | **Deprecated.**Returns the value for the AdSense attribute associated with the given key. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.getAttributeKeys` | **Deprecated.**Returns the attribute keys that have been set on this service. |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.getSlots` | Get the list of slots associated with this service. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.getSlots` method |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.getTargeting` | **Deprecated.**Returns a specific custom service-level targeting parameter that has been set. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.getTargetingKeys` | **Deprecated.**Returns the list of all custom service-level targeting keys that have been set. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.isInitialLoadDisabled` | **Deprecated.** Returns whether or not initial requests for ads was successfully disabled by a previous [PubAdsService.disableInitialLoad](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.disableInitialLoad) call. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh` | Fetches and displays new ads for specific or all slots on the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener` | Removes a previously registered listener. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener` method |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.set` | **Deprecated.**Sets values for AdSense attributes that apply to all ad slots under the Publisher Ads service. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setCategoryExclusion` | **Deprecated.**Sets a page-level ad category exclusion for the given label name. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setCentering` | **Deprecated.**Enables and disables horizontal centering of ads. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setForceSafeFrame` | **Deprecated.**Configures whether all ads on the page should be forced to be rendered using a SafeFrame container. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setLocation` | **Deprecated.**Passes location information from websites so you can geo-target line items to specific locations. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setPrivacySettings` | Allows configuration of all privacy settings from a single API using a config object. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setPublisherProvidedId` | Sets the value for the publisher-provided ID. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setSafeFrameConfig` | **Deprecated.**Sets the page-level preferences for SafeFrame configuration. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setTargeting` | **Deprecated.**Sets custom targeting parameters for a given key that apply to all Publisher Ads service ad slots. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setVideoContent` | **Deprecated.**Sets the video content information to be sent along with the ad requests for targeting and content exclusion purposes. |
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.updateCorrelator` | Changes the correlator that is sent with ad requests, effectively starting a new page view. |

### Methods

*** ** * ** ***

#### clear

`clear(slots?: https://developers.google.com/publisher-tag/reference#googletag.Slot[]): boolean`Removes the ads from the given slots and replaces them with blank content. The slots will be marked as unfetched.  

In particular, clearing a slot removes the ad from GPT's [long-lived pageview](https://support.google.com/admanager/answer/183281), so future requests will not be influenced by roadblocks or competitive exclusions involving this ad.

Example
:

    ### JavaScript

    ```javascript
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to clear only slot1.
    googletag.pubads().clear([slot1]);

    // This call to clear both slot1 and slot2.
    googletag.pubads().clear([slot1, slot2]);

    // This call to clear all slots.
    googletag.pubads().clear();
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    var slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to clear only slot1.
    googletag.pubads().clear([slot1]);

    // This call to clear both slot1 and slot2.
    googletag.pubads().clear([slot1, slot2]);

    // This call to clear all slots.
    googletag.pubads().clear();
    ```

    ### TypeScript

    ```typescript
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1")!;
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2")!;
    googletag.display("div-2");

    // This call to clear only slot1.
    googletag.pubads().clear([slot1]);

    // This call to clear both slot1 and slot2.
    googletag.pubads().clear([slot1, slot2]);

    // This call to clear all slots.
    googletag.pubads().clear();
    ```

| Parameters ||
|---|---|
| `` `Optional` slots: https://developers.google.com/publisher-tag/reference#googletag.Slot[] `` | The array of slots to clear. Array is optional; all slots will be cleared if it is unspecified. |

| Returns ||
|---|---|
| `boolean` | Returns `true` if slots have been cleared, `false` otherwise. |

*** ** * ** ***

#### clearCategoryExclusions

`clearCategoryExclusions(): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Clears all page-level ad category exclusion labels. This is useful if you want to refresh the slot.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.categoryExclusion](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) instead.

Example
:

    ### JavaScript

    ```javascript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Make ad requests. No ad with 'AirlineAd' label will be returned.

    // Clear category exclusions so all ads can be returned.
    googletag.setConfig({
      categoryExclusion: null,
    });

    // Make ad requests. Any ad can be returned.
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Make ad requests. No ad with 'AirlineAd' label will be returned.

    // Clear category exclusions so all ads can be returned.
    googletag.setConfig({
      categoryExclusion: null,
    });

    // Make ad requests. Any ad can be returned.
    ```

    ### TypeScript

    ```typescript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Make ad requests. No ad with 'AirlineAd' label will be returned.

    // Clear category exclusions so all ads can be returned.
    googletag.setConfig({
      categoryExclusion: null,
    });

    // Make ad requests. Any ad can be returned.
    ```

See also
:
    - [Custom labels to block ads](https://support.google.com/admanager/answer/3238504)

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### clearTargeting

`clearTargeting(key?: string): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Clears custom targeting parameters for a specific key or for all keys.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.targeting](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
        fruits: "apple",
      },
    });

    googletag.setConfig({
      targeting: {
        interests: null,
      },
    });
    // Targeting 'colors' and 'fruits' are still present, while 'interests'
    // was cleared.

    googletag.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
        fruits: "apple",
      },
    });

    googletag.setConfig({
      targeting: {
        interests: null,
      },
    });
    // Targeting 'colors' and 'fruits' are still present, while 'interests'
    // was cleared.

    googletag.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
        fruits: "apple",
      },
    });

    googletag.setConfig({
      targeting: {
        interests: null,
      },
    });
    // Targeting 'colors' and 'fruits' are still present, while 'interests'
    // was cleared.

    googletag.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

| Parameters ||
|---|---|
| `` `Optional` key: string `` | Targeting parameter key. The key is optional; all targeting parameters will be cleared if it is unspecified. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### collapseEmptyDivs

`collapseEmptyDivs(collapseBeforeAdFetch?: boolean): boolean`Enables collapsing of slot divs so that they don't take up any space on the page when there is no ad content to display. This mode must be set before the service is enabled.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.collapseDiv](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv) instead.

See also
:
    - [Collapse empty ad slots](https://developers.google.com/publisher-tag/samples/collapse-empty-ad-slots)
    - [Minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift)

| Parameters ||
|---|---|
| `` `Optional` collapseBeforeAdFetch: boolean `` | Whether to collapse the slots even before the ads are fetched. This parameter is optional; if not provided, `false` will be used as the default value. |

| Returns ||
|---|---|
| `boolean` | Returns `true` if div collapse mode was enabled and `false` if it is impossible to enable collapse mode because the method was called after the service was enabled. |

*** ** * ** ***

#### disableInitialLoad

`disableInitialLoad(): void`Disables requests for ads on page load, but allows ads to be requested with a [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh) call. This should be set prior to enabling the service. Async mode must be used; otherwise it will be impossible to request ads using `refresh`.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.disableInitialLoad](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad) instead.

See also
:
    - [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading)
    - [Control SRA batching](https://developers.google.com/publisher-tag/samples/control-sra-batching)

*** ** * ** ***

#### display

`display(adUnitPath: string, size: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize, div?: string | Element, clickUrl?: string): void`Constructs and displays an ad slot with the given ad unit path and size.  

This method is a shorthand equivalent to calling [googletag.defineSlot](https://developers.google.com/publisher-tag/reference#googletag.defineSlot) followed immediately by [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display).  

The behavior of this method depends on whether [Single Request Architecture (SRA)](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) is enabled:

- **SRA enabled:** All ad slots defined up to the point of this call will be batched and requested together.
- **SRA disabled (default):** The ad slot will be requested individually.

**Note:** When this method is called, a snapshot of the slot and page state is created to ensure consistency when sending the ad request and rendering the response. Any changes that are made to the slot or page state after this method is called (including targeting, privacy settings, force SafeFrame, etc.) will only apply to subsequent `display()` or `refresh()` requests.

Example
:

    ### JavaScript

    ```javascript
    googletag.pubads().display("/1234567/sports", [728, 90], "div-1");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.pubads().display("/1234567/sports", [728, 90], "div-1");
    ```

    ### TypeScript

    ```typescript
    googletag.pubads().display("/1234567/sports", [728, 90], "div-1");
    ```

See also
:
    - [Display a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad)
    - [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading)

| Parameters ||
|---|---|
| `adUnitPath: string` | The [ad unit path](https://developers.google.com/publisher-tag/guides/get-started#ad-unit-path) of slot to be rendered. |
| `size: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize` | Width and height of the slot. |
| `` `Optional` div: string | Element `` | Either the ID of the div containing the slot or the div element itself. |
| `` `Optional` clickUrl: string `` | The click URL to use on this slot. |

*** ** * ** ***

#### enableLazyLoad

`enableLazyLoad(config?: {
fetchMarginPercent?: number;
mobileScaling?: number;
renderMarginPercent?: number;
}): void`Enables lazy loading in GPT as defined by the config object. For more detailed examples, see the [Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading) sample.  

**Note:** Lazy fetching in SRA only works if all slots are outside the fetching margin.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.lazyLoad](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad) instead.

Example
:

    ### JavaScript

    ```javascript
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
    ```

    ### JavaScript (legacy)

    ```javascript
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
    ```

    ### TypeScript

    ```typescript
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
    ```

See also
:
    - [Ads best practices: Prioritize "important" ad slots](https://developers.google.com/publisher-tag/guides/ad-best-practices#prioritize_important_ad_slots)
    - [Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading)

| Parameters ||
|---|---|
| `` `Optional` config: { fetchMarginPercent?: number; mobileScaling?: number; renderMarginPercent?: number; } `` | Configuration object allows customization of lazy behavior. Any omitted configurations will use a default set by Google that will be tuned over time. To disable a particular setting, such as a fetching margin, set the value to `-1`. - `fetchMarginPercent` The minimum distance from the current viewport a slot must be before we fetch the ad as a percentage of viewport size. A value of 0 means "when the slot enters the viewport", 100 means "when the ad is 1 viewport away", and so on. - `renderMarginPercent` The minimum distance from the current viewport a slot must be before we render an ad. This allows for prefetching the ad, but waiting to render and download other subresources. The value works just like `fetchMarginPercent` as a percentage of viewport. - `mobileScaling` A multiplier applied to margins on mobile devices. This allows varying margins on mobile vs. desktop. For example, a value of 2.0 will multiply all margins by 2 on mobile devices, increasing the minimum distance a slot can be before fetching and rendering. |

*** ** * ** ***

#### enableSingleRequest

`enableSingleRequest(): boolean`Enables single request mode for fetching multiple ads at the same time. This requires all Publisher Ads slots to be defined and added to the PubAdsService prior to enabling the service. Single request mode must be set before the service is enabled.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.singleRequest](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) instead.

See also
:
    - [Ads best practices: Use Single Request Architecture correctly](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly)
    - [Control SRA batching](https://developers.google.com/publisher-tag/samples/control-sra-batching)

| Returns ||
|---|---|
| `boolean` | Returns `true` if single request mode was enabled and `false` if it is impossible to enable single request mode because the method was called after the service was enabled. |

*** ** * ** ***

#### enableVideoAds

`enableVideoAds(): void`Signals to GPT that video ads will be present on the page. This enables competitive exclusion constraints on display and video ads. If the video content is known, call [PubAdsService.setVideoContent](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.setVideoContent) in order to be able to use content exclusion for display ads.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.videoAds](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) instead.

*** ** * ** ***

#### get

`get(key: string): string`Returns the value for the AdSense attribute associated with the given key.

> [!WARNING]
> **Deprecated:** Use [googletag.getConfig](https://developers.google.com/publisher-tag/reference#googletag.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });

    const adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    const pageUrl = adsenseConfig?.page_url || null;
    // Returns 'http://www.example.com'.
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });

    var adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    var pageUrl =
      (adsenseConfig === null || adsenseConfig === void 0 ? void 0 : adsenseConfig.page_url) || null;
    // Returns 'http://www.example.com'.
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });

    const adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    const pageUrl = adsenseConfig?.page_url || null;
    // Returns 'http://www.example.com'.
    ```

See also
:
    - [AdSense Attributes](https://developers.google.com/publisher-tag/adsense_attributes)

| Parameters ||
|---|---|
| `key: string` | Name of the attribute to look for. |

| Returns ||
|---|---|
| `string` | Current value for the attribute key, or `null` if the key is not present. |

*** ** * ** ***

#### getAttributeKeys

`getAttributeKeys(): string[]`Returns the attribute keys that have been set on this service.

> [!WARNING]
> **Deprecated:** Use [googletag.getConfig](https://developers.google.com/publisher-tag/reference#googletag.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
        document_language: "en",
      },
    });

    const adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    const adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
        document_language: "en",
      },
    });

    var adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    var adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
        document_language: "en",
      },
    });

    const adsenseConfig = googletag.getConfig("adsenseAttributes").adsenseAttributes;
    const adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

| Returns ||
|---|---|
| `string[]` | Array of attribute keys set on this service. Ordering is undefined. |

*** ** * ** ***

#### getTargeting

`getTargeting(key: string): string[]`Returns a specific custom service-level targeting parameter that has been set.

> [!WARNING]
> **Deprecated:** Use [googletag.getConfig](https://developers.google.com/publisher-tag/reference#googletag.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    const targetingConfig = googletag.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig?.["interests"] || [];
    // Returns ['sports'].

    const ageTargeting = targetingConfig?.["age"] || [];
    // Returns [] (empty array).
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    var targetingConfig = googletag.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    var targeting =
      (targetingConfig === null || targetingConfig === void 0
        ? void 0
        : targetingConfig["interests"]) || [];
    // Returns ['sports'].

    var ageTargeting =
      (targetingConfig === null || targetingConfig === void 0 ? void 0 : targetingConfig["age"]) || [];
    // Returns [] (empty array).
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    const targetingConfig = googletag.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig?.["interests"] || [];
    // Returns ['sports'].

    const ageTargeting = targetingConfig?.["age"] || [];
    // Returns [] (empty array).
    ```

| Parameters ||
|---|---|
| `key: string` | The targeting key to look for. |

| Returns ||
|---|---|
| `string[]` | The values associated with this key, or an empty array if there is no such key. |

*** ** * ** ***

#### getTargetingKeys

`getTargetingKeys(): string[]`Returns the list of all custom service-level targeting keys that have been set.

> [!WARNING]
> **Deprecated:** Use [googletag.getConfig](https://developers.google.com/publisher-tag/reference#googletag.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
      },
    });

    const targetingConfig = googletag.getConfig("targeting").targeting;
    const keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'colors'].
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
      },
    });

    var targetingConfig = googletag.getConfig("targeting").targeting;
    var keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'colors'].
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      targeting: {
        interests: "sports",
        colors: "blue",
      },
    });

    const targetingConfig = googletag.getConfig("targeting").targeting;
    const keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'colors'].
    ```

| Returns ||
|---|---|
| `string[]` | Array of targeting keys. Ordering is undefined. |

*** ** * ** ***

#### isInitialLoadDisabled

`isInitialLoadDisabled(): boolean`Returns whether or not initial requests for ads was successfully disabled by a previous [PubAdsService.disableInitialLoad](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.disableInitialLoad) call.

> [!WARNING]
> **Deprecated:** Use [googletag.getConfig](https://developers.google.com/publisher-tag/reference#googletag.getConfig) instead.

| Returns ||
|---|---|
| `boolean` | Returns `true` if a previous call to [PubAdsService.disableInitialLoad](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.disableInitialLoad) was successful, `false` otherwise. |

*** ** * ** ***

#### refresh

`refresh(slots?: https://developers.google.com/publisher-tag/reference#googletag.Slot[], options?: {
changeCorrelator: boolean;
}): void`Fetches and displays new ads for specific or all slots on the page. Works only in asynchronous rendering mode.  

For proper behavior across all browsers, calling `refresh` must be preceded by a call to `display` the ad slot. If the call to `display` is omitted, refresh may behave unexpectedly. If desired, the [PubAdsService.disableInitialLoad](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.disableInitialLoad) method can be used to stop `display` from fetching an ad.  

Refreshing a slot removes the old ad from GPT's [long-lived pageview](https://support.google.com/admanager/answer/183281), so future requests will not be influenced by roadblocks or competitive exclusions involving that ad.

Example
:

    ### JavaScript

    ```javascript
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to refresh fetches a new ad for slot1 only.
    googletag.pubads().refresh([slot1]);

    // This call to refresh fetches a new ad for both slot1 and slot2.
    googletag.pubads().refresh([slot1, slot2]);

    // This call to refresh fetches a new ad for each slot.
    googletag.pubads().refresh();

    // This call to refresh fetches a new ad for slot1, without changing
    // the correlator.
    googletag.pubads().refresh([slot1], { changeCorrelator: false });

    // This call to refresh fetches a new ad for each slot, without
    // changing the correlator.
    googletag.pubads().refresh(null, { changeCorrelator: false });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1");
    googletag.display("div-1");
    var slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2");
    googletag.display("div-2");

    // This call to refresh fetches a new ad for slot1 only.
    googletag.pubads().refresh([slot1]);

    // This call to refresh fetches a new ad for both slot1 and slot2.
    googletag.pubads().refresh([slot1, slot2]);

    // This call to refresh fetches a new ad for each slot.
    googletag.pubads().refresh();

    // This call to refresh fetches a new ad for slot1, without changing
    // the correlator.
    googletag.pubads().refresh([slot1], { changeCorrelator: false });

    // This call to refresh fetches a new ad for each slot, without
    // changing the correlator.
    googletag.pubads().refresh(null, { changeCorrelator: false });
    ```

    ### TypeScript

    ```typescript
    const slot1 = googletag.defineSlot("/1234567/sports", [728, 90], "div-1")!;
    googletag.display("div-1");
    const slot2 = googletag.defineSlot("/1234567/news", [160, 600], "div-2")!;
    googletag.display("div-2");

    // This call to refresh fetches a new ad for slot1 only.
    googletag.pubads().refresh([slot1]);

    // This call to refresh fetches a new ad for both slot1 and slot2.
    googletag.pubads().refresh([slot1, slot2]);

    // This call to refresh fetches a new ad for each slot.
    googletag.pubads().refresh();

    // This call to refresh fetches a new ad for slot1, without changing
    // the correlator.
    googletag.pubads().refresh([slot1], { changeCorrelator: false });

    // This call to refresh fetches a new ad for each slot, without
    // changing the correlator.
    googletag.pubads().refresh(null, { changeCorrelator: false });
    ```

See also
:
    - [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading)
    - [Refresh ad slots](https://developers.google.com/publisher-tag/samples/refresh)

| Parameters ||
|---|---|
| `` `Optional` slots: https://developers.google.com/publisher-tag/reference#googletag.Slot[] `` | The slots to refresh. Array is optional; all slots will be refreshed if it is unspecified. |
| `` `Optional` options: { changeCorrelator: boolean; } `` | Configuration options associated with this refresh call. - `changeCorrelator` Specifies whether or not a new correlator is to be generated for fetching ads. Our ad servers maintain this correlator value briefly (currently for 30 seconds, but subject to change), such that requests with the same correlator received close together will be considered a single page view. By default a new correlator is generated for every refresh. **Note:** this option has no effect on GPT's [long-lived pageview](https://support.google.com/admanager/answer/183281), which automatically reflects the ads currently on the page and has no expiration time. |

*** ** * ** ***

#### set

`set(key: string, value: string): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Sets values for AdSense attributes that apply to all ad slots under the Publisher Ads service.  

Calling this more than once for the same key will override previously set values for that key. All values must be set before calling `display` or `refresh`.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.adsenseAttributes](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      adsenseAttributes: {
        page_url: "http://www.example.com",
      },
    });
    ```

See also
:
    - [AdSense Attributes](https://developers.google.com/publisher-tag/adsense_attributes)

| Parameters ||
|---|---|
| `key: string` | The name of the attribute. |
| `value: string` | Attribute value. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setCategoryExclusion

`setCategoryExclusion(categoryExclusion: string): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Sets a page-level ad category exclusion for the given label name.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.categoryExclusion](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion) instead.

Example
:

    ### JavaScript

    ```javascript
    // Label = AirlineAd.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Label = AirlineAd.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });
    ```

    ### TypeScript

    ```typescript
    // Label = AirlineAd.
    googletag.setConfig({
      categoryExclusion: ["AirlineAd"],
    });
    ```

See also
:
    - [Custom labels to block ads](https://support.google.com/admanager/answer/3238504)

| Parameters ||
|---|---|
| `categoryExclusion: string` | The ad category exclusion label to add. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setCentering

`setCentering(centerAds: boolean): void`Enables and disables horizontal centering of ads. Centering is disabled by default. In legacy gpt_mobile.js, centering is enabled by default.  

This method should be invoked before calling `display` or `refresh` because only ads that are requested after calling this method will be centered.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.centering](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.centering) instead.

Example
:

    ### JavaScript

    ```javascript
    // Make ads centered.
    googletag.setConfig({
      centering: true,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Make ads centered.
    googletag.setConfig({
      centering: true,
    });
    ```

    ### TypeScript

    ```typescript
    // Make ads centered.
    googletag.setConfig({
      centering: true,
    });
    ```

| Parameters ||
|---|---|
| `centerAds: boolean` | `true` to center ads, `false` to left-align them. |

*** ** * ** ***

#### setForceSafeFrame

`setForceSafeFrame(forceSafeFrame: boolean): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Configures whether all ads on the page should be forced to be rendered using a SafeFrame container.  

Please keep the following things in mind while using this API:

- This setting will only take effect for **subsequent** ad requests made for the respective slots.
- The slot level setting, if specified, will always override the page level setting.
- If set to `true` (at slot-level or page level), the ad will always be rendered using a SafeFrame container independent of the choice made in the Google Ad Manager UI.
- However, if set to `false` or left unspecified, the ad will be rendered using a SafeFrame container depending on the type of creative and the selection made in the Google Ad Manager UI.
- This API should be used with caution as it could impact the behaviour of creatives that attempt to break out of their iFrames or rely on them being rendered directly in a publishers page.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
      },
    });

    // The following slot will be opted-out of the page-level force
    // SafeFrame instruction.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        safeFrame: {
          forceSafeFrame: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will have SafeFrame forced.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
      },
    });

    // The following slot will be opted-out of the page-level force
    // SafeFrame instruction.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        safeFrame: {
          forceSafeFrame: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will have SafeFrame forced.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
      },
    });

    // The following slot will be opted-out of the page-level force
    // SafeFrame instruction.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")!
      .setConfig({
        safeFrame: {
          forceSafeFrame: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will have SafeFrame forced.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2")!.addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

See also
:
    - [Render creatives using SafeFrame](https://support.google.com/admanager/answer/6023110)

| Parameters ||
|---|---|
| `forceSafeFrame: boolean` | `true` to force all ads on the page to be rendered in SafeFrames and `false` to change the previous setting to false. Setting this to `false` when unspecified earlier, won't change anything. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setLocation

`setLocation(address: string): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Passes location information from websites so you can geo-target line items to specific locations.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.location](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.location) instead.

Example
:

    ### JavaScript

    ```javascript
    // Postal code:
    googletag.setConfig({
      location: "10001,US",
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Postal code:
    googletag.setConfig({
      location: "10001,US",
    });
    ```

    ### TypeScript

    ```typescript
    // Postal code:
    googletag.setConfig({
      location: "10001,US",
    });
    ```

| Parameters ||
|---|---|
| `address: string` | Freeform address. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setPrivacySettings

`setPrivacySettings(privacySettings: https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Allows configuration of all privacy settings from a single API using a config object.

Example
:

    ### JavaScript

    ```javascript
    googletag.pubads().setPrivacySettings({
      restrictDataProcessing: true,
    });

    // Set multiple privacy settings at the same time.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: true,
      underAgeOfConsent: true,
    });

    // Clear the configuration for childDirectedTreatment.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: null,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.pubads().setPrivacySettings({
      restrictDataProcessing: true,
    });

    // Set multiple privacy settings at the same time.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: true,
      underAgeOfConsent: true,
    });

    // Clear the configuration for childDirectedTreatment.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: null,
    });
    ```

    ### TypeScript

    ```typescript
    googletag.pubads().setPrivacySettings({
      restrictDataProcessing: true,
    });

    // Set multiple privacy settings at the same time.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: true,
      underAgeOfConsent: true,
    });

    // Clear the configuration for childDirectedTreatment.
    googletag.pubads().setPrivacySettings({
      childDirectedTreatment: null,
    });
    ```

See also
:
    - [Configure privacy settings](https://developers.google.com/publisher-tag/samples/configure-privacy)
    - [Display a limited ad](https://developers.google.com/publisher-tag/samples/display-limited-ad)

| Parameters ||
|---|---|
| `privacySettings: https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig` | Object containing privacy settings config. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the function was called. |

*** ** * ** ***

#### setPublisherProvidedId

`setPublisherProvidedId(ppid: string): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Sets the value for the publisher-provided ID.

Example
:

    ### JavaScript

    ```javascript
    googletag.pubads().setPublisherProvidedId("12JD92JD8078S8J29SDOAKC0EF230337");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.pubads().setPublisherProvidedId("12JD92JD8078S8J29SDOAKC0EF230337");
    ```

    ### TypeScript

    ```typescript
    googletag.pubads().setPublisherProvidedId("12JD92JD8078S8J29SDOAKC0EF230337");
    ```

See also
:
    - [About publisher provided identifiers](https://support.google.com/admanager/answer/2880055)

| Parameters ||
|---|---|
| `ppid: string` | An alphanumeric ID provided by the publisher. Must be between 32 and 150 characters. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setSafeFrameConfig

`setSafeFrameConfig(config: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Sets the page-level preferences for SafeFrame configuration. Any unrecognized keys in the config object will be ignored. The entire config will be ignored if an invalid value is passed for a recognized key.  

These page-level preferences will be overridden by slot-level preferences, if specified.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
        allowOverlayExpansion: true,
        allowPushExpansion: true,
        sandbox: true,
      },
    });

    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        safeFrame: {
          allowOverlayExpansion: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will inherit the page level settings, and hence
    // would allow for expansion by overlay.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
        allowOverlayExpansion: true,
        allowPushExpansion: true,
        sandbox: true,
      },
    });

    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        safeFrame: {
          allowOverlayExpansion: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will inherit the page level settings, and hence
    // would allow for expansion by overlay.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      safeFrame: {
        forceSafeFrame: true,
        allowOverlayExpansion: true,
        allowPushExpansion: true,
        sandbox: true,
      },
    });

    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")!
      .setConfig({
        safeFrame: {
          allowOverlayExpansion: false,
        },
      })
      .addService(googletag.pubads());

    // The following slot will inherit the page level settings, and hence
    // would allow for expansion by overlay.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2")!.addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

See also
:
    - [Render creatives using SafeFrame](https://support.google.com/admanager/answer/6023110)

| Parameters ||
|---|---|
| `config: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig` | The configuration object. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setTargeting

`setTargeting(key: string, value: string | string[]): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Sets custom targeting parameters for a given key that apply to all Publisher Ads service ad slots. Calling this multiple times for the same key will overwrite old values. These keys are defined in your Google Ad Manager account.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.targeting](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) instead.

Example
:

    ### JavaScript

    ```javascript
    // Example with a single value for a key.
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    // Example with multiple values for a key inside in an array.
    googletag.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Example with a single value for a key.
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    // Example with multiple values for a key inside in an array.
    googletag.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

    ### TypeScript

    ```typescript
    // Example with a single value for a key.
    googletag.setConfig({
      targeting: {
        interests: "sports",
      },
    });

    // Example with multiple values for a key inside in an array.
    googletag.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

| Parameters ||
|---|---|
| `key: string` | Targeting parameter key. |
| `value: string | string[]` | Targeting parameter value or array of values. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the method was called. |

*** ** * ** ***

#### setVideoContent

`setVideoContent(videoContentId: string, videoCmsId: string): void`Sets the video content information to be sent along with the ad requests for targeting and content exclusion purposes. Video ads will be automatically enabled when this method is called. For `videoContentId` and `videoCmsId`, use the values that are provided to the Google Ad Manager content ingestion service.

> [!WARNING]
> **Deprecated:** Use [PageSettingsConfig.videoAds](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds) instead.

See also
:
    - [VAST ad tag URL parameters](https://support.google.com/admanager/answer/1068325)

| Parameters ||
|---|---|
| `videoContentId: string` | The video content ID. |
| `videoCmsId: string` | The video CMS ID. |

*** ** * ** ***

#### updateCorrelator

`updateCorrelator(): https://developers.google.com/publisher-tag/reference#googletag.PubAdsService`Changes the correlator that is sent with ad requests, effectively starting a new page view. The correlator is the same for all the ad requests coming from one page view, and unique across page views. Only applies to async mode.  

**Note:** this has no effect on GPT's [long-lived pageview](https://support.google.com/admanager/answer/183281), which automatically reflects the ads actually on the page and has no expiration time.

Example
:

    ### JavaScript

    ```javascript
    // Assume that the correlator is currently 12345. All ad requests made
    // by this page will currently use that value.

    // Replace the current correlator with a new correlator.
    googletag.pubads().updateCorrelator();

    // The correlator will now be a new randomly selected value, different
    // from 12345. All subsequent ad requests made by this page will use
    // the new value.
    ```

    ### JavaScript (legacy)

    ```javascript
    // Assume that the correlator is currently 12345. All ad requests made
    // by this page will currently use that value.

    // Replace the current correlator with a new correlator.
    googletag.pubads().updateCorrelator();

    // The correlator will now be a new randomly selected value, different
    // from 12345. All subsequent ad requests made by this page will use
    // the new value.
    ```

    ### TypeScript

    ```typescript
    // Assume that the correlator is currently 12345. All ad requests made
    // by this page will currently use that value.

    // Replace the current correlator with a new correlator.
    googletag.pubads().updateCorrelator();

    // The correlator will now be a new randomly selected value, different
    // from 12345. All subsequent ad requests made by this page will use
    // the new value.
    ```

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.PubAdsService` | The service object on which the function was called. |

*** ** * ** ***

## googletag.ResponseInformation

An object representing a single ad response.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation.advertiserId` | The ID of the advertiser. |
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation.campaignId` | The ID of the campaign. |
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation.creativeId` | The ID of the creative. |
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation.creativeTemplateId` | The template ID of the ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation.lineItemId` | The ID of the line item. |

See also
:
    - [Slot.getResponseInformation](https://developers.google.com/publisher-tag/reference#googletag.Slot.getResponseInformation)

### Properties

*** ** * ** ***

#### advertiserId

`advertiserId: number`The ID of the advertiser.

*** ** * ** ***

#### campaignId

`campaignId: number`The ID of the campaign.

*** ** * ** ***

#### creativeId

`creativeId: number`The ID of the creative.

*** ** * ** ***

#### creativeTemplateId

`creativeTemplateId: number`The template ID of the ad.

*** ** * ** ***

#### lineItemId

`lineItemId: number`The ID of the line item.

*** ** * ** ***

## googletag.RewardedPayload

An object representing the reward associated with a [rewarded ad](https://support.google.com/admanager/answer/9116812)

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.RewardedPayload.amount` | The number of items included in the reward. |
| `https://developers.google.com/publisher-tag/reference#googletag.RewardedPayload.type` | The type of item included in the reward (for example, "coin"). |

See also
:
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)

### Properties

*** ** * ** ***

#### amount

`amount: number`The number of items included in the reward.

*** ** * ** ***

#### type

`type: string`The type of item included in the reward (for example, "coin").

*** ** * ** ***

## googletag.Service

Base service class that contains methods common for all services.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener` | Registers a listener that allows you to set up and call a JavaScript function when a specific GPT event happens on the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.getSlots` | Get the list of slots associated with this service. |
| `https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener` | Removes a previously registered listener. |

### Methods

*** ** * ** ***

#### addEventListener

`addEventListener<K extends keyof https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap>(eventType: https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.addEventListener.addEventListener.K, listener: ((arg: https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap[https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.addEventListener.addEventListener.K]) => void)): https://developers.google.com/publisher-tag/reference#googletag.Service`Registers a listener that allows you to set up and call a JavaScript function when a specific GPT event happens on the page. The following events are supported:

- [events.GameManualInterstitialSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent)
- [events.GameManualInterstitialSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent)
- [events.ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent)
- [events.RewardedSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotClosedEvent)
- [events.RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent)
- [events.RewardedSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent)
- [events.SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent)
- [events.SlotRenderEndedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent)
- [events.SlotRequestedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent)
- [events.SlotResponseReceived](https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived)
- [events.SlotVisibilityChangedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent)

An object of the appropriate event type is passed to the listener when it is called.

Example
:

    ### JavaScript

    ```javascript
    // 1. Adding an event listener for the PubAdsService.
    googletag.pubads().addEventListener("slotOnload", (event) => {
      console.log("Slot has been loaded:");
      console.log(event);
    });

    // 2. Adding an event listener with slot specific logic.
    // Listeners operate at service level, which means that you cannot add
    // a listener for an event for a specific slot only. You can, however,
    // programmatically filter a listener to respond only to a certain ad
    // slot, using this pattern:
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", (event) => {
      if (event.slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // 1. Adding an event listener for the PubAdsService.
    googletag.pubads().addEventListener("slotOnload", function (event) {
      console.log("Slot has been loaded:");
      console.log(event);
    });

    // 2. Adding an event listener with slot specific logic.
    // Listeners operate at service level, which means that you cannot add
    // a listener for an event for a specific slot only. You can, however,
    // programmatically filter a listener to respond only to a certain ad
    // slot, using this pattern:
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", function (event) {
      if (event.slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // 1. Adding an event listener for the PubAdsService.
    googletag.pubads().addEventListener("slotOnload", (event) => {
      console.log("Slot has been loaded:");
      console.log(event);
    });

    // 2. Adding an event listener with slot specific logic.
    // Listeners operate at service level, which means that you cannot add
    // a listener for an event for a specific slot only. You can, however,
    // programmatically filter a listener to respond only to a certain ad
    // slot, using this pattern:
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", (event) => {
      if (event.slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

| Parameters ||
|---|---|
| `eventType: https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.addEventListener.addEventListener.K` | A string representing the type of event generated by GPT. Event types are case sensitive. |
| `listener: ((arg: https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap[https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.addEventListener.addEventListener.K]) => void)` | Function that takes a single event object argument. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Service` | The service object on which the method was called. |

*** ** * ** ***

#### getSlots

`getSlots(): https://developers.google.com/publisher-tag/reference#googletag.Slot[]`Get the list of slots associated with this service.

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot[]` | Slots in the order in which they were added to the service. |

*** ** * ** ***

#### removeEventListener

`removeEventListener<K extends keyof https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap>(eventType: https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.removeEventListener.removeEventListener.K, listener: ((event: https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap[https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.removeEventListener.removeEventListener.K]) => void)): void`Removes a previously registered listener.

Example
:

    ### JavaScript

    ```javascript
    googletag.cmd.push(() => {
      // Define a new ad slot.
      googletag.defineSlot("/6355419/Travel", [728, 90], "div-for-slot").addService(googletag.pubads());

      // Define a new function that removes itself via removeEventListener
      // after the impressionViewable event fires.
      const onViewableListener = (event) => {
        googletag.pubads().removeEventListener("impressionViewable", onViewableListener);
        setTimeout(() => {
          googletag.pubads().refresh([event.slot]);
        }, 30000);
      };

      // Add onViewableListener as a listener for impressionViewable events.
      googletag.pubads().addEventListener("impressionViewable", onViewableListener);
      googletag.enableServices();
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.cmd.push(function () {
      // Define a new ad slot.
      googletag.defineSlot("/6355419/Travel", [728, 90], "div-for-slot").addService(googletag.pubads());

      // Define a new function that removes itself via removeEventListener
      // after the impressionViewable event fires.
      var onViewableListener = function (event) {
        googletag.pubads().removeEventListener("impressionViewable", onViewableListener);
        setTimeout(function () {
          googletag.pubads().refresh([event.slot]);
        }, 30000);
      };

      // Add onViewableListener as a listener for impressionViewable events.
      googletag.pubads().addEventListener("impressionViewable", onViewableListener);
      googletag.enableServices();
    });
    ```

    ### TypeScript

    ```typescript
    googletag.cmd.push(() => {
      // Define a new ad slot.
      googletag
        .defineSlot("/6355419/Travel", [728, 90], "div-for-slot")!
        .addService(googletag.pubads());

      // Define a new function that removes itself via removeEventListener
      // after the impressionViewable event fires.
      const onViewableListener = (event: googletag.events.ImpressionViewableEvent) => {
        googletag.pubads().removeEventListener("impressionViewable", onViewableListener);
        setTimeout(() => {
          googletag.pubads().refresh([event.slot]);
        }, 30000);
      };

      // Add onViewableListener as a listener for impressionViewable events.
      googletag.pubads().addEventListener("impressionViewable", onViewableListener);
      googletag.enableServices();
    });
    ```

| Parameters ||
|---|---|
| `eventType: https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.removeEventListener.removeEventListener.K` | A string representing the type of event generated by GPT. Event types are case sensitive. |
| `listener: ((event: https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap[https://developers.google.com/publisher-tag/reference#googletag.CompanionAdsService.removeEventListener.removeEventListener.K]) => void)` | Function that takes a single event object argument. |

*** ** * ** ***

## googletag.SizeMappingBuilder

Builder for size mapping specification objects. This builder is provided to help easily construct size specifications.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder.addSize` | Adds a mapping from a single-size array (representing the viewport) to a single- or multi-size array representing the slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder.build` | Builds a size map specification from the mappings added to this builder. |

See also
:
    - [Ad sizes: Responsive ads](https://developers.google.com/publisher-tag/guides/ad-sizes#responsive_ads)

### Methods

*** ** * ** ***

#### addSize

`addSize(viewportSize: https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray, slotSize: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize): https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder`Adds a mapping from a single-size array (representing the viewport) to a single- or multi-size array representing the slot.

Example
:

    ### JavaScript

    ```javascript
    // Mapping 1
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [728, 90])
      .addSize([640, 480], "fluid")
      .addSize([0, 0], [88, 31]) // All viewports &lt; 640x480
      .build();

    // Mapping 2
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [])
      .addSize([640, 480], [120, 60])
      .addSize([0, 0], [])
      .build();

    // Mapping 2 will not show any ads for the following viewport sizes:
    // [1024, 768] > size >= [980, 690] and
    // [640, 480] > size >= [0, 0]
    ```

    ### JavaScript (legacy)

    ```javascript
    // Mapping 1
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [728, 90])
      .addSize([640, 480], "fluid")
      .addSize([0, 0], [88, 31]) // All viewports &lt; 640x480
      .build();

    // Mapping 2
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [])
      .addSize([640, 480], [120, 60])
      .addSize([0, 0], [])
      .build();

    // Mapping 2 will not show any ads for the following viewport sizes:
    // [1024, 768] > size >= [980, 690] and
    // [640, 480] > size >= [0, 0]
    ```

    ### TypeScript

    ```typescript
    // Mapping 1
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [728, 90])
      .addSize([640, 480], "fluid")
      .addSize([0, 0], [88, 31]) // All viewports &lt; 640x480
      .build();

    // Mapping 2
    googletag
      .sizeMapping()
      .addSize([1024, 768], [970, 250])
      .addSize([980, 690], [])
      .addSize([640, 480], [120, 60])
      .addSize([0, 0], [])
      .build();

    // Mapping 2 will not show any ads for the following viewport sizes:
    // [1024, 768] > size >= [980, 690] and
    // [640, 480] > size >= [0, 0]
    ```

| Parameters ||
|---|---|
| `viewportSize: https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray` | The size of the viewport for this mapping entry. |
| `slotSize: https://developers.google.com/publisher-tag/reference#googletag.GeneralSize` | The sizes of the slot for this mapping entry. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder` | A reference to this builder. |

*** ** * ** ***

#### build

`build(): https://developers.google.com/publisher-tag/reference#googletag.SizeMappingArray`Builds a size map specification from the mappings added to this builder.  

If any invalid mappings have been supplied, this method will return `null`. Otherwise it returns a specification in the correct format to pass to [Slot.defineSizeMapping](https://developers.google.com/publisher-tag/reference#googletag.Slot.defineSizeMapping).  

Note: the behavior of the builder after calling this method is undefined.

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.SizeMappingArray` | The result built by this builder. Can be null if invalid size mappings were supplied. |

*** ** * ** ***

## googletag.Slot

Slot is an object representing a single ad slot on a page.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.addService` | Adds a [Service](https://developers.google.com/publisher-tag/reference#googletag.Service) to this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.clearCategoryExclusions` | **Deprecated.**Clears all slot-level ad category exclusion labels for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.clearTargeting` | **Deprecated.**Clears specific or all custom slot-level targeting parameters for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.defineSizeMapping` | Sets an array of mappings from a minimum viewport size to slot size for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.get` | **Deprecated.**Returns the value for the AdSense attribute associated with the given key for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getAdUnitPath` | Returns the full path of the ad unit, with the network code and ad unit path. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getAttributeKeys` | **Deprecated.**Returns the list of attribute keys set on this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getCategoryExclusions` | **Deprecated.**Returns the ad category exclusion labels for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig` | Gets a frozen copy of the general configuration options for the slot set by [setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig). |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getResponseInformation` | Returns the ad response information. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getSlotElementId` | Returns the ID of the slot `div` provided when the slot was defined. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getTargeting` | **Deprecated.**Returns a specific custom targeting parameter set on this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.getTargetingKeys` | **Deprecated.**Returns the list of all custom targeting keys set on this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.set` | **Deprecated.**Sets a value for an AdSense attribute on this ad slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setCategoryExclusion` | **Deprecated.**Sets a slot-level ad category exclusion label on this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setClickUrl` | **Deprecated.**Sets the click URL to which users will be redirected after clicking on the ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setCollapseEmptyDiv` | **Deprecated.** Sets whether the slot `div` should be hidden when there is no ad in the slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setConfig` | Sets general configuration options for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setForceSafeFrame` | **Deprecated.**Configures whether ads in this slot should be forced to be rendered using a SafeFrame container. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setSafeFrameConfig` | **Deprecated.**Sets the slot-level preferences for SafeFrame configuration. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.setTargeting` | **Deprecated.**Sets a custom targeting parameter for this slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.Slot.updateTargetingFromMap` | **Deprecated.**Sets custom targeting parameters for this slot, from a key:value map in a JSON object. |

### Methods

*** ** * ** ***

#### addService

`addService(service: https://developers.google.com/publisher-tag/reference#googletag.Service): https://developers.google.com/publisher-tag/reference#googletag.Slot`Adds a [Service](https://developers.google.com/publisher-tag/reference#googletag.Service) to this slot.

Example
:

    ### JavaScript

    ```javascript
    googletag.defineSlot("/1234567/sports", [160, 600], "div").addService(googletag.pubads());
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.defineSlot("/1234567/sports", [160, 600], "div").addService(googletag.pubads());
    ```

    ### TypeScript

    ```typescript
    googletag.defineSlot("/1234567/sports", [160, 600], "div")!.addService(googletag.pubads());
    ```

See also
:
    - [Get Started with Google Publisher Tags](https://developers.google.com/publisher-tag/guides/get-started)
    - [Display a test ad](https://developers.google.com/publisher-tag/samples/display-test-ad)

| Parameters ||
|---|---|
| `service: https://developers.google.com/publisher-tag/reference#googletag.Service` | The service to be added. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### clearCategoryExclusions

`clearCategoryExclusions(): https://developers.google.com/publisher-tag/reference#googletag.Slot`Clears all slot-level ad category exclusion labels for this slot.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.categoryExclusion](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) instead.

Example
:

    ### JavaScript

    ```javascript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());

    // Make an ad request. No ad with 'AirlineAd' label will be returned
    // for the slot.

    // Clear category exclusions so all ads can be returned.
    slot.setConfig({
      categoryExclusion: null,
    });

    // Make an ad request. Any ad can be returned for the slot.
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());

    // Make an ad request. No ad with 'AirlineAd' label will be returned
    // for the slot.

    // Clear category exclusions so all ads can be returned.
    slot.setConfig({
      categoryExclusion: null,
    });

    // Make an ad request. Any ad can be returned for the slot.
    ```

    ### TypeScript

    ```typescript
    // Set category exclusion to exclude ads with 'AirlineAd' labels.
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());

    // Make an ad request. No ad with 'AirlineAd' label will be returned
    // for the slot.

    // Clear category exclusions so all ads can be returned.
    slot.setConfig({
      categoryExclusion: null,
    });

    // Make an ad request. Any ad can be returned for the slot.
    ```

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### clearTargeting

`clearTargeting(key?: string): https://developers.google.com/publisher-tag/reference#googletag.Slot`Clears specific or all custom slot-level targeting parameters for this slot.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.targeting](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
          color: "red",
        },
      })
      .addService(googletag.pubads());

    slot.setConfig({
      targeting: {
        color: null,
      },
    });
    // Targeting 'allow_expandable' and 'interests' are still present,
    // while 'color' was cleared.

    slot.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
          color: "red",
        },
      })
      .addService(googletag.pubads());

    slot.setConfig({
      targeting: {
        color: null,
      },
    });
    // Targeting 'allow_expandable' and 'interests' are still present,
    // while 'color' was cleared.

    slot.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
          color: "red",
        },
      })
      .addService(googletag.pubads());

    slot.setConfig({
      targeting: {
        color: null,
      },
    });
    // Targeting 'allow_expandable' and 'interests' are still present,
    // while 'color' was cleared.

    slot.setConfig({
      targeting: null,
    });
    // All targeting has been cleared.
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

| Parameters ||
|---|---|
| `` `Optional` key: string `` | Targeting parameter key. The key is optional; all targeting parameters will be cleared if it is unspecified. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### defineSizeMapping

`defineSizeMapping(sizeMapping: https://developers.google.com/publisher-tag/reference#googletag.SizeMappingArray): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets an array of mappings from a minimum viewport size to slot size for this slot.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    const mapping = googletag
      .sizeMapping()
      .addSize([100, 100], [88, 31])
      .addSize(
        [320, 400],
        [
          [320, 50],
          [300, 50],
        ],
      )
      .build();

    slot.defineSizeMapping(mapping);
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    var mapping = googletag
      .sizeMapping()
      .addSize([100, 100], [88, 31])
      .addSize(
        [320, 400],
        [
          [320, 50],
          [300, 50],
        ],
      )
      .build();

    slot.defineSizeMapping(mapping);
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    const mapping = googletag
      .sizeMapping()
      .addSize([100, 100], [88, 31])
      .addSize(
        [320, 400],
        [
          [320, 50],
          [300, 50],
        ],
      )
      .build();

    slot.defineSizeMapping(mapping!);
    ```

See also
:
    - [Ad sizes: Responsive ads](https://developers.google.com/publisher-tag/guides/ad-sizes#responsive_ads)

| Parameters ||
|---|---|
| `sizeMapping: https://developers.google.com/publisher-tag/reference#googletag.SizeMappingArray` | Array of size mappings. You can use [SizeMappingBuilder](https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder) to create it. Each size mapping is an array of two elements: [SingleSizeArray](https://developers.google.com/publisher-tag/reference#googletag.SingleSizeArray) and [GeneralSize](https://developers.google.com/publisher-tag/reference#googletag.GeneralSize). |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### get

`get(key: string): string`Returns the value for the AdSense attribute associated with the given key for this slot. To see service-level attributes inherited by this slot, use [PubAdsService.get](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.get).

> [!WARNING]
> **Deprecated:** Use [googletag.Slot.getConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());

    const adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    const pageUrl = adsenseConfig?.page_url || null;
    // Returns 'http://www.example.com'.
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());

    var adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    var pageUrl =
      (adsenseConfig === null || adsenseConfig === void 0 ? void 0 : adsenseConfig.page_url) || null;
    // Returns 'http://www.example.com'.
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());

    const adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    const pageUrl = adsenseConfig?.page_url || null;
    // Returns 'http://www.example.com'.
    ```

See also
:
    - [AdSense Attributes](https://developers.google.com/publisher-tag/adsense_attributes)

| Parameters ||
|---|---|
| `key: string` | Name of the attribute to look for. |

| Returns ||
|---|---|
| `string` | Current value for the attribute key, or `null` if the key is not present. |

*** ** * ** ***

#### getAdUnitPath

`getAdUnitPath(): string`Returns the full path of the ad unit, with the network code and ad unit path.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    slot.getAdUnitPath();
    // Returns '/1234567/sports'.
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    slot.getAdUnitPath();
    // Returns '/1234567/sports'.
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    slot.getAdUnitPath();
    // Returns '/1234567/sports'.
    ```

| Returns ||
|---|---|
| `string` | Ad unit path. |

*** ** * ** ***

#### getAttributeKeys

`getAttributeKeys(): string[]`Returns the list of attribute keys set on this slot. To see the keys of service-level attributes inherited by this slot, use [PubAdsService.getAttributeKeys](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.getAttributeKeys).

> [!WARNING]
> **Deprecated:** Use [googletag.Slot.getConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
          document_language: "en",
        },
      })
      .addService(googletag.pubads());

    const adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    const adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
          document_language: "en",
        },
      })
      .addService(googletag.pubads());

    var adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    var adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
          document_language: "en",
        },
      })
      .addService(googletag.pubads());

    const adsenseConfig = slot.getConfig("adsenseAttributes").adsenseAttributes;
    const adsenseAttributes = Object.keys(adsenseConfig || {});
    // Returns ['page_url', 'document_language'].
    ```

| Returns ||
|---|---|
| `string[]` | Array of attribute keys. Ordering is undefined. |

*** ** * ** ***

#### getCategoryExclusions

`getCategoryExclusions(): string[]`Returns the ad category exclusion labels for this slot.

> [!WARNING]
> **Deprecated:** Use [googletag.Slot.getConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd", "TrainAd"],
      })
      .addService(googletag.pubads());

    const exclusions = slot.getConfig("categoryExclusion")?.categoryExclusion || [];
    // Returns ['AirlineAd', 'TrainAd'].
    ```

    ### JavaScript (legacy)

    ```javascript
    var _a;
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd", "TrainAd"],
      })
      .addService(googletag.pubads());

    var exclusions =
      ((_a = slot.getConfig("categoryExclusion")) === null || _a === void 0
        ? void 0
        : _a.categoryExclusion) || [];
    // Returns ['AirlineAd', 'TrainAd'].
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        categoryExclusion: ["AirlineAd", "TrainAd"],
      })
      .addService(googletag.pubads());

    const exclusions = slot.getConfig("categoryExclusion")?.categoryExclusion || [];
    // Returns ['AirlineAd', 'TrainAd'].
    ```

| Returns ||
|---|---|
| `string[]` | The ad category exclusion labels for this slot, or an empty array if none have been set. |

*** ** * ** ***

#### getConfig

`getConfig(keys: string | string[]): Readonly<Pick<https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig, "adsenseAttributes" | "targeting" | "categoryExclusion">>`Gets a frozen copy of the general configuration options for the slot set by [setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig).  

Not all `setConfig()` properties are supported by this method. Supported properties are:

- [`adsenseAttributes`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes)
- [`categoryExclusion`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion)
- [`targeting`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting)

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");

    // Get the value of the `targeting` setting.
    const targetingConfig = slot.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `categoryExclusion` settings.
    const config = slot.getConfig(["adsenseAttributes", "categoryExclusion"]);
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");

    // Get the value of the `targeting` setting.
    var targetingConfig = slot.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `categoryExclusion` settings.
    var config = slot.getConfig(["adsenseAttributes", "categoryExclusion"]);
    ```

    ### TypeScript

    ```typescript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div")!;

    // Get the value of the `targeting` setting.
    const targetingConfig = slot.getConfig("targeting");

    // Get the value of the `adsenseAttributes` and `categoryExclusion` settings.
    const config = slot.getConfig(["adsenseAttributes", "categoryExclusion"]);
    ```

| Parameters ||
|---|---|
| `keys: string | string[]` | The keys of the configuration options to get. |

| Returns ||
|---|---|
| `Readonly<Pick<https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig, "adsenseAttributes" | "targeting" | "categoryExclusion">>` | A frozen copy of the configuration options for the slot. |

*** ** * ** ***

#### getResponseInformation

`getResponseInformation(): https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation`Returns the ad response information. This is based on the last ad response for the slot. If this is called when the slot has no ad, `null` will be returned.

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.ResponseInformation` | The latest ad response information, or `null` if the slot has no ad. |

*** ** * ** ***

#### getSlotElementId

`getSlotElementId(): string`Returns the ID of the slot `div` provided when the slot was defined.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    slot.getSlotElementId();
    // Returns 'div'.
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    slot.getSlotElementId();
    // Returns 'div'.
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    slot.getSlotElementId();
    // Returns 'div'.
    ```

| Returns ||
|---|---|
| `string` | Slot `div` ID. |

*** ** * ** ***

#### getTargeting

`getTargeting(key: string): string[]`Returns a specific custom targeting parameter set on this slot. Service-level targeting parameters are not included.

> [!WARNING]
> **Deprecated:** Use [googletag.Slot.getConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
        },
      })
      .addService(googletag.pubads());

    const targetingConfig = slot.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig?.["allow_expandable"] || [];
    // Returns ['true'].

    const ageTargeting = targetingConfig?.["age"] || [];
    // Returns [] (empty array).
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
        },
      })
      .addService(googletag.pubads());

    var targetingConfig = slot.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    var targeting =
      (targetingConfig === null || targetingConfig === void 0
        ? void 0
        : targetingConfig["allow_expandable"]) || [];
    // Returns ['true'].

    var ageTargeting =
      (targetingConfig === null || targetingConfig === void 0 ? void 0 : targetingConfig["age"]) || [];
    // Returns [] (empty array).
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        targeting: {
          allow_expandable: "true",
        },
      })
      .addService(googletag.pubads());

    const targetingConfig = slot.getConfig("targeting").targeting;

    // Get targeting for a specific key.
    const targeting = targetingConfig?.["allow_expandable"] || [];
    // Returns ['true'].

    const ageTargeting = targetingConfig?.["age"] || [];
    // Returns [] (empty array).
    ```

| Parameters ||
|---|---|
| `key: string` | The targeting key to look for. |

| Returns ||
|---|---|
| `string[]` | The values associated with this key, or an empty array if there is no such key. |

*** ** * ** ***

#### getTargetingKeys

`getTargetingKeys(): string[]`Returns the list of all custom targeting keys set on this slot. Service-level targeting keys are not included.

> [!WARNING]
> **Deprecated:** Use [googletag.Slot.getConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.getConfig) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
        },
      })
      .addService(googletag.pubads());

    const targetingConfig = slot.getConfig("targeting").targeting;
    const keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'allow_expandable'].
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
        },
      })
      .addService(googletag.pubads());

    var targetingConfig = slot.getConfig("targeting").targeting;
    var keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'allow_expandable'].
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        targeting: {
          allow_expandable: "true",
          interests: ["sports", "music"],
        },
      })
      .addService(googletag.pubads());

    const targetingConfig = slot.getConfig("targeting").targeting;
    const keys = Object.keys(targetingConfig || {});
    // Returns ['interests', 'allow_expandable'].
    ```

| Returns ||
|---|---|
| `string[]` | Array of targeting keys. Ordering is undefined. |

*** ** * ** ***

#### set

`set(key: string, value: string): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets a value for an AdSense attribute on this ad slot. This will override any values set at the service level for this key.  

Calling this method more than once for the same key will override previously set values for that key. All values must be set before calling `display` or `refresh`.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.adsenseAttributes](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes) instead.

Example
:

    ### JavaScript

    ```javascript
    // Setting an attribute on a single ad slot.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());
    ```

    ### JavaScript (legacy)

    ```javascript
    // Setting an attribute on a single ad slot.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());
    ```

    ### TypeScript

    ```typescript
    // Setting an attribute on a single ad slot.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        adsenseAttributes: {
          page_url: "http://www.example.com",
        },
      })
      .addService(googletag.pubads());
    ```

See also
:
    - [AdSense Attributes](https://developers.google.com/publisher-tag/adsense_attributes)

| Parameters ||
|---|---|
| `key: string` | The name of the attribute. |
| `value: string` | Attribute value. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setCategoryExclusion

`setCategoryExclusion(categoryExclusion: string): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets a slot-level ad category exclusion label on this slot.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.categoryExclusion](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion) instead.

Example
:

    ### JavaScript

    ```javascript
    // Label = AirlineAd.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());
    ```

    ### JavaScript (legacy)

    ```javascript
    // Label = AirlineAd.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());
    ```

    ### TypeScript

    ```typescript
    // Label = AirlineAd.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        categoryExclusion: ["AirlineAd"],
      })
      .addService(googletag.pubads());
    ```

See also
:
    - [Custom labels to block ads](https://support.google.com/admanager/answer/3238504)

| Parameters ||
|---|---|
| `categoryExclusion: string` | The ad category exclusion label to add. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setClickUrl

`setClickUrl(value: string): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets the click URL to which users will be redirected after clicking on the ad.  

The Google Ad Manager servers still record a click even if the click URL is replaced. Any landing page URL associated with the creative that is served is appended to the provided value. Subsequent calls overwrite the value. This works only for non-SRA requests.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.clickUrl](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.clickUrl) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        clickUrl: "http://www.example.com?original_click_url=",
      })
      .addService(googletag.pubads());
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setConfig({
        clickUrl: "http://www.example.com?original_click_url=",
      })
      .addService(googletag.pubads());
    ```

    ### TypeScript

    ```typescript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setConfig({
        clickUrl: "http://www.example.com?original_click_url=",
      })
      .addService(googletag.pubads());
    ```

| Parameters ||
|---|---|
| `value: string` | The click URL to set. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setCollapseEmptyDiv

`setCollapseEmptyDiv(collapse: boolean, collapseBeforeAdFetch?: boolean): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets whether the slot `div` should be hidden when there is no ad in the slot. This overrides the service-level settings.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.collapseDiv](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot1 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        collapseDiv: "BEFORE_FETCH",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // when the page is loaded, before ads are requested.

    const slot2 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-2")
      .setConfig({
        collapseDiv: "ON_NO_FILL",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // only after GPT detects that no ads are available for the slot.
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot1 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setConfig({
        collapseDiv: "BEFORE_FETCH",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // when the page is loaded, before ads are requested.

    var slot2 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-2")
      .setConfig({
        collapseDiv: "ON_NO_FILL",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // only after GPT detects that no ads are available for the slot.
    ```

    ### TypeScript

    ```typescript
    const slot1 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")!
      .setConfig({
        collapseDiv: "BEFORE_FETCH",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // when the page is loaded, before ads are requested.

    const slot2 = googletag
      .defineSlot("/1234567/sports", [160, 600], "div-2")!
      .setConfig({
        collapseDiv: "ON_NO_FILL",
      })
      .addService(googletag.pubads());
    // The above will cause the div for this slot to be collapsed
    // only after GPT detects that no ads are available for the slot.
    ```

See also
:
    - [Collapse empty ad slots](https://developers.google.com/publisher-tag/samples/collapse-empty-ad-slots)
    - [Minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift)

| Parameters ||
|---|---|
| `collapse: boolean` | Whether to collapse the slot if no ad is returned. |
| `` `Optional` collapseBeforeAdFetch: boolean `` | Whether to collapse the slot even before an ad is fetched. Ignored if collapse is not `true`. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setConfig

`setConfig(slotConfig: https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets general configuration options for this slot.

| Parameters ||
|---|---|
| `slotConfig: https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig` | The configuration object. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setForceSafeFrame

`setForceSafeFrame(forceSafeFrame: boolean): https://developers.google.com/publisher-tag/reference#googletag.Slot`Configures whether ads in this slot should be forced to be rendered using a SafeFrame container.  

Please keep the following things in mind while using this API:

- This setting will only take effect for **subsequent** ad requests made for the respective slots.
- The slot level setting, if specified, will always override the page level setting.
- If set to `true` (at slot-level or page level), the ad will always be rendered using a SafeFrame container independent of the choice made in the Google Ad Manager UI.
- However, if set to `false` or left unspecified, the ad will be rendered using a SafeFrame container depending on the type of creative and the selection made in the Google Ad Manager UI.
- This API should be used with caution as it could impact the behaviour of creatives that attempt to break out of their iFrames or rely on them being rendered directly in a publishers page.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setForceSafeFrame(true)
      .addService(googletag.pubads());
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .setForceSafeFrame(true)
      .addService(googletag.pubads());
    ```

    ### TypeScript

    ```typescript
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .setForceSafeFrame(true)
      .addService(googletag.pubads());
    ```

See also
:
    - [Render creatives using SafeFrame](https://support.google.com/admanager/answer/6023110)

| Parameters ||
|---|---|
| `forceSafeFrame: boolean` | `true` to force all ads in this slot to be rendered in SafeFrames and `false` to opt-out of a page-level setting (if present). Setting this to `false` when not specified at the page-level won't change anything. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setSafeFrameConfig

`setSafeFrameConfig(config: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets the slot-level preferences for SafeFrame configuration. Any unrecognized keys in the config object will be ignored. The entire config will be ignored if an invalid value is passed for a recognized key.  

These slot-level preferences, if specified, will override any page-level preferences.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame) instead.

Example
:

    ### JavaScript

    ```javascript
    googletag.pubads().setForceSafeFrame(true);

    // The following slot will have a sandboxed safeframe that only
    // disallows top-level navigation.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setSafeFrameConfig({ sandbox: true })
      .addService(googletag.pubads());

    // The following slot will inherit page-level settings.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.pubads().setForceSafeFrame(true);

    // The following slot will have a sandboxed safeframe that only
    // disallows top-level navigation.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")
      .setSafeFrameConfig({ sandbox: true })
      .addService(googletag.pubads());

    // The following slot will inherit page-level settings.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2").addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

    ### TypeScript

    ```typescript
    googletag.pubads().setForceSafeFrame(true);

    // The following slot will have a sandboxed safeframe that only
    // disallows top-level navigation.
    googletag
      .defineSlot("/1234567/sports", [160, 600], "div-1")!
      .setSafeFrameConfig({ sandbox: true })
      .addService(googletag.pubads());

    // The following slot will inherit page-level settings.
    googletag.defineSlot("/1234567/news", [160, 600], "div-2")!.addService(googletag.pubads());

    googletag.display("div-1");
    googletag.display("div-2");
    ```

See also
:
    - [Render creatives using SafeFrame](https://support.google.com/admanager/answer/6023110)

| Parameters ||
|---|---|
| `config: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig` | The configuration object. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### setTargeting

`setTargeting(key: string, value: string | string[]): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets a custom targeting parameter for this slot. Calling this method multiple times for the same key will overwrite old values. Values set here will overwrite targeting parameters set at the service-level. These keys are defined in your Google Ad Manager account.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.targeting](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");
    slot.addService(googletag.pubads());

    // Example with a single value for a key.
    slot.setConfig({
      targeting: {
        allow_expandable: "true",
      },
    });

    // Example with multiple values for a key inside in an array.
    slot.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");
    slot.addService(googletag.pubads());

    // Example with a single value for a key.
    slot.setConfig({
      targeting: {
        allow_expandable: "true",
      },
    });

    // Example with multiple values for a key inside in an array.
    slot.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div")!;
    slot.addService(googletag.pubads());

    // Example with a single value for a key.
    slot.setConfig({
      targeting: {
        allow_expandable: "true",
      },
    });

    // Example with multiple values for a key inside in an array.
    slot.setConfig({
      targeting: {
        interests: ["sports", "music"],
      },
    });
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

| Parameters ||
|---|---|
| `key: string` | Targeting parameter key. |
| `value: string | string[]` | Targeting parameter value or array of values. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

#### updateTargetingFromMap

`updateTargetingFromMap(map: {
[adUnitPath: string]: string | string[];
}): https://developers.google.com/publisher-tag/reference#googletag.Slot`Sets custom targeting parameters for this slot, from a key:value map in a JSON object. This is the same as calling [Slot.setTargeting](https://developers.google.com/publisher-tag/reference#googletag.Slot.setTargeting) for all the key values of the object. These keys are defined in your Google Ad Manager account.  

**Notes:**

- In case of overwriting, only the last value will be kept.
- If the value is an array, any previous value will be overwritten, not merged.
- Values set here will overwrite targeting parameters set at the service-level.

> [!WARNING]
> **Deprecated:** Use [SlotSettingsConfig.targeting](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) instead.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");

    slot.updateTargetingFromMap({
      color: "red",
      interests: ["sports", "music", "movies"],
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag.defineSlot("/1234567/sports", [160, 600], "div");

    slot.updateTargetingFromMap({
      color: "red",
      interests: ["sports", "music", "movies"],
    });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag.defineSlot("/1234567/sports", [160, 600], "div")!;

    slot.updateTargetingFromMap({
      color: "red",
      interests: ["sports", "music", "movies"],
    });
    ```

| Parameters ||
|---|---|
| `map: { [adUnitPath: string]: string | string[]; }` | Targeting parameter key:value map. |

| Returns ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.Slot` | The slot object on which the method was called. |

*** ** * ** ***

## googletag.config

Main configuration interface for page-level settings.

| Interfaces ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdExpansionConfig` | Settings to control ad expansion. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig` | Settings to control the behavior of AdSense ads. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AutoRefreshConfig` | Auto refresh configuration settings. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig` | Settings to configure the continue button behavior. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialConfig` | An object which defines the behavior of a single interstitial ad slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig` | Settings to control the use of lazy loading in GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig` | Main configuration interface for page-level settings. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatmentsConfig` | Settings to control publisher privacy treatments. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig` | Publisher provided signals (PPS) configuration object. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig` | Settings to control [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig` | Main configuration interface for slot-level settings. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.TaxonomyData` | An object containing the values for a single [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy). |
| `https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig` | Settings to configure video ad related settings. |

| Type Aliases ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.CollapseDivBehavior` | Supported values for controlling the collapsing behavior of ad slots. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialTrigger` | Supported interstitial ad triggers. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatment` | Supported publisher privacy treatments. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy` | Supported taxonomies for [publisher provided signals (PPS)](https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig). |

### Type Aliases

*** ** * ** ***

#### CollapseDivBehavior

`CollapseDivBehavior: "DISABLED" | "BEFORE_FETCH" | "ON_NO_FILL"`Supported values for controlling the collapsing behavior of ad slots.

See also
:
    - [PageSettingsConfig.collapseDiv](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv)
    - [SlotSettingsConfig.collapseDiv](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv)

*** ** * ** ***

#### InterstitialTrigger

`InterstitialTrigger: "unhideWindow" | "navBar" | "inactivity" | "endOfArticle" | "continueReading" | "backward"`Supported interstitial ad triggers.  

**Note** : Beginning June 15, 2026, the `backward` trigger will no longer be supported and enabling it will have no effect. See the [GPT release notes](https://developers.google.com/publisher-tag/release-notes#2026-05-18) for more information.

*** ** * ** ***

#### PrivacyTreatment

`PrivacyTreatment: "disablePersonalization"`Supported publisher privacy treatments.

*** ** * ** ***

#### Taxonomy

`Taxonomy: "IAB_AUDIENCE_1_1" | "IAB_CONTENT_2_2"`Supported taxonomies for [publisher provided signals (PPS)](https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig).

See also
:
    - [IAB Audience Taxonomy 1.1](https://iabtechlab.com/standards/audience-taxonomy/)
    - [IAB Content Taxonomy 2.2](https://iabtechlab.com/standards/content-taxonomy/)

*** ** * ** ***

## googletag.config.AdExpansionConfig

Settings to control ad expansion.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdExpansionConfig.enabled` | Whether ad expansion is enabled or disabled. |

Example
:

    ### JavaScript

    ```javascript
    // Enable ad slot expansion across the entire page.
    googletag.setConfig({
      adExpansion: { enabled: true },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Enable ad slot expansion across the entire page.
    googletag.setConfig({
      adExpansion: { enabled: true },
    });
    ```

    ### TypeScript

    ```typescript
    // Enable ad slot expansion across the entire page.
    googletag.setConfig({
      adExpansion: { enabled: true },
    });
    ```

### Properties

*** ** * ** ***

#### `Optional` enabled

`enabled?: boolean`Whether ad expansion is enabled or disabled.  

Setting this value overrides the default configured in Google Ad Manager.

See also
:
    - [Expand ads on desktop and tablet](https://support.google.com/admanager/answer/9384852)
    - [Expand ads on mobile web (partial screen)](https://support.google.com/admanager/answer/9117822)

*** ** * ** ***

## googletag.config.AdSenseAttributesConfig

Settings to control the behavior of AdSense ads.  

These attributes can be used to override server-side settings on a per-request basis.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig.adsense_ad_format` | AdSense ad format. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig.adsense_channel_ids` | AdSense channel IDs. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig.adsense_test_mode` | Whether or not test mode is enabled. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig.document_language` | Language of the page on which ads are displayed. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig.page_url` | URL of the page on which ads are displayed. |

See also
:
    - [PageSettingsConfig.adsenseAttributes](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes)
    - [SlotSettingsConfig.adsenseAttributes](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes)

### Properties

*** ** * ** ***

#### `Optional` adsense_ad_format

`adsense_ad_format?: "120x240_as" | "120x600_as" | "125x125_as" | "160x600_as" | "180x150_as" | "200x200_as" | "234x60_as" | "250x250_as" | "300x250_as" | "336x280_as" | "468x60_as" | "728x90_as"`AdSense ad format.

*** ** * ** ***

#### `Optional` adsense_channel_ids

`adsense_channel_ids?: string`AdSense channel IDs.  

Allowed values are channel IDs separated by '+'.  

Example: `271828183+314159265`

See also
:
    - [Track ad unit performance with custom channels](https://support.google.com/adsense/answer/10078316)

*** ** * ** ***

#### `Optional` adsense_test_mode

`adsense_test_mode?: "on"`Whether or not test mode is enabled.  

When set to `on`, ads are marked as test-only, and won't be included in counting or billing. This setting must be unset for production, non-test traffic.

*** ** * ** ***

#### `Optional` document_language

`document_language?: string`Language of the page on which ads are displayed.  

Allowed values are valid ISO 639-1 language codes.  

Example: `en`

See also
:
    - [List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)

*** ** * ** ***

#### `Optional` page_url

`page_url?: string`URL of the page on which ads are displayed.  

Allowed values are valid URLs.  

Example: `http://www.example.com`

*** ** * ** ***

## googletag.config.AutoRefreshConfig

Auto refresh configuration settings.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.AutoRefreshConfig.backForwardCache` | Whether GPT will automatically refresh an actively viewed ad slot when the page is restored from the back/forward cache. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.AutoRefreshConfig.heavyAds` | Whether GPT will automatically refresh an ad slot if Chrome's Heavy Ad Intervention triggers on the slot's ad iframe. |

### Properties

*** ** * ** ***

#### `Optional` backForwardCache

`backForwardCache?: boolean`Whether GPT will automatically refresh an actively viewed ad slot when the page is restored from the back/forward cache. Defaults to `true`.

Example
:

    ### JavaScript

    ```javascript
    // Set the auto refresh configuration, disabling auto refresh on
    // back/forward cache restore.
    googletag.setConfig({ autoRefresh: { backForwardCache: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set the auto refresh configuration, disabling auto refresh on
    // back/forward cache restore.
    googletag.setConfig({ autoRefresh: { backForwardCache: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### TypeScript

    ```typescript
    // Set the auto refresh configuration, disabling auto refresh on
    // back/forward cache restore.
    googletag.setConfig({ autoRefresh: { backForwardCache: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

See also
:
    - [Back/forward cache](https://web.dev/articles/bfcache)

*** ** * ** ***

#### `Optional` heavyAds

`heavyAds?: boolean`Whether GPT will automatically refresh an ad slot if Chrome's Heavy Ad Intervention triggers on the slot's ad iframe. Defaults to `true`.

Example
:

    ### JavaScript

    ```javascript
    // Set the auto refresh configuration, disabling auto refresh on heavy
    // ad intervention.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set the auto refresh configuration, disabling auto refresh on heavy
    // ad intervention.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### TypeScript

    ```typescript
    // Set the auto refresh configuration, disabling auto refresh on heavy
    // ad intervention.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration, restoring to default behavior.
    googletag.setConfig({ autoRefresh: null });
    ```

See also
:
    - [Understand Chrome's Heavy Ad Interventions](https://developer.chrome.com/docs/web-platform/heavy-ads-intervention)

*** ** * ** ***

## googletag.config.ContinueButtonConfig

Settings to configure the continue button behavior.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig.backgroundColor` | The background color of the button. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig.font` | The font family of the button text. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig.fontColor` | The text color of the button. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig.freqCapIntervalMinutes` | The frequency capping interval in minutes. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig.targetId` | The ID of the HTML element on which to render/trigger the continue button. |

See also
:
    - [SlotSettingsConfig.continueButton](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.continueButton)

### Properties

*** ** * ** ***

#### `Optional` backgroundColor

`backgroundColor?: string`The background color of the button.  

Example: `'blue'`, `'#94B1FF'`

*** ** * ** ***

#### `Optional` font

`font?: string`The font family of the button text.  

Example: `'Arial'`

*** ** * ** ***

#### `Optional` fontColor

`fontColor?: string`The text color of the button.  

Example: `'white'`, `'#B73B87'`

*** ** * ** ***

#### `Optional` freqCapIntervalMinutes

`freqCapIntervalMinutes?: number`The frequency capping interval in minutes.  

Must be an integer greater than or equal to 1.

*** ** * ** ***

#### `Optional` targetId

`targetId?: string`The ID of the HTML element on which to render/trigger the continue button.

*** ** * ** ***

## googletag.config.InterstitialConfig

An object which defines the behavior of a single interstitial ad slot.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialConfig.requireStorageAccess` | Whether local storage consent is required to display this interstitial ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialConfig.triggers` | The interstitial trigger configuration for this interstitial ad. |

### Properties

*** ** * ** ***

#### `Optional` requireStorageAccess

`requireStorageAccess?: boolean`Whether local storage consent is required to display this interstitial ad.  

GPT uses local storage to enforce a [frequency cap](https://support.google.com/admanager/answer/9840201#frequency) for interstitial ads. However, users who have not provided local storage consent are still eligible to be served interstitial ads. Setting this property to `true` opts out of the default behavior, and ensures interstitial ads are only shown to users who have provided local storage consent.

Example
:

    ### JavaScript

    ```javascript
    // Opt out of showing interstitials to users
    // without local storage consent.
    const interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    );

    interstitialSlot.setConfig({
      interstitial: {
        requireStorageAccess: true, // defaults to false
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Opt out of showing interstitials to users
    // without local storage consent.
    var interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    );

    interstitialSlot.setConfig({
      interstitial: {
        requireStorageAccess: true, // defaults to false
      },
    });
    ```

    ### TypeScript

    ```typescript
    // Opt out of showing interstitials to users
    // without local storage consent.
    const interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    )!;

    interstitialSlot.setConfig({
      interstitial: {
        requireStorageAccess: true, // defaults to false
      },
    });
    ```

See also
:
    - [Traffic web interstitials](https://support.google.com/admanager/answer/9840201)

*** ** * ** ***

#### `Optional` triggers

`triggers?: Partial<Record<https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialTrigger, boolean>>`The interstitial trigger configuration for this interstitial ad.  

Setting the value of an interstitial trigger to `true` will enable it and `false` will disable it. This will override the default values [configured in Google Ad Manager](https://support.google.com/admanager/answer/9840201).

Example
:

    ### JavaScript

    ```javascript
    // Define a GPT managed web interstitial ad slot.
    const interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    );

    // Enable optional interstitial triggers.
    // Change this value to false to disable.
    const enableTriggers = true;

    interstitialSlot.setConfig({
      interstitial: {
        triggers: {
          navBar: enableTriggers,
          unhideWindow: enableTriggers,
        },
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Define a GPT managed web interstitial ad slot.
    var interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    );

    // Enable optional interstitial triggers.
    // Change this value to false to disable.
    var enableTriggers = true;

    interstitialSlot.setConfig({
      interstitial: {
        triggers: {
          navBar: enableTriggers,
          unhideWindow: enableTriggers,
        },
      },
    });
    ```

    ### TypeScript

    ```typescript
    // Define a GPT managed web interstitial ad slot.
    const interstitialSlot = googletag.defineOutOfPageSlot(
      "/1234567/sports",
      googletag.enums.OutOfPageFormat.INTERSTITIAL,
    )!;

    // Enable optional interstitial triggers.
    // Change this value to false to disable.
    const enableTriggers = true;

    interstitialSlot.setConfig({
      interstitial: {
        triggers: {
          navBar: enableTriggers,
          unhideWindow: enableTriggers,
        },
      },
    });
    ```

See also
:
    - [Display a web interstitial ad](https://developers.google.com/publisher-tag/samples/display-web-interstitial-ad)

*** ** * ** ***

## googletag.config.LazyLoadConfig

Settings to control the use of lazy loading in GPT.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.fetchMarginPercent` | The minimum distance from the current viewport a slot must be before we request an ad, expressed as a percentage of viewport size. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.mobileScaling` | A multiplier applied to margins on mobile devices. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.renderMarginPercent` | The minimum distance from the current viewport a slot must be before we render an ad, expressed as a percentage of viewport size. |

See also
:
    - [PageSettingsConfig.lazyLoad](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad)

### Properties

*** ** * ** ***

#### `Optional` fetchMarginPercent

`fetchMarginPercent?: number`The minimum distance from the current viewport a slot must be before we request an ad, expressed as a percentage of viewport size.  

Used in conjunction with [renderMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.renderMarginPercent), this setting allows for prefetching an ad, but waiting to render and download other subresources. As such, this value should always be greater than or equal to [renderMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.renderMarginPercent).  

A value of `0` means "when the slot enters the viewport", `100` means "when the ad is 1 viewport away", and so on.

*** ** * ** ***

#### `Optional` mobileScaling

`mobileScaling?: number`A multiplier applied to margins on mobile devices. This multiplier is applied to both [fetchMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.fetchMarginPercent) and [renderMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.renderMarginPercent).  

This allows for different margins on mobile vs. desktop, where viewport sizes and scroll speeds may be different. For example, a value of 2.0 will multiply all margins by 2 on mobile devices, increasing the minimum distance a slot can be from the viewport before fetching and rendering.

*** ** * ** ***

#### `Optional` renderMarginPercent

`renderMarginPercent?: number`The minimum distance from the current viewport a slot must be before we render an ad, expressed as a percentage of viewport size.  

Used in conjunction with [fetchMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.fetchMarginPercent), this setting allows for prefetching an ad, but waiting to render and download other subresources. As such, this value should always be less than or equal to [fetchMarginPercent](https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig.fetchMarginPercent).  

A value of `0` means "when the slot enters the viewport", `100` means "when the ad is 1 viewport away", and so on.

*** ** * ** ***

## googletag.config.PageSettingsConfig

Main configuration interface for page-level settings.  

Allows setting multiple features with a single API call.  

All properties listed below are examples and do not reflect actual features that utilize setConfig. For the set of features, see fields within the PageSettingsConfig type below.  

Examples:

- Only features specified in the [googletag.setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig) call are modified.

  ```
    // Configure feature alpha.
    googletag.setConfig({
        alpha: {...}
    });

    // Configure feature bravo. Feature alpha is unchanged.
    googletag.setConfig({
       bravo: {...}
    });
  ```
- All settings for a given feature are updated with each call to [googletag.setConfig](https://developers.google.com/publisher-tag/reference#googletag.setConfig).

  ```
    // Configure feature charlie to echo = 1, foxtrot = true.
    googletag.setConfig({
        charlie: {
            echo: 1,
            foxtrot: true,
        }
    });

    // Update feature charlie to echo = 2. Since foxtrot was not specified,
    // the value is cleared.
    googletag.setConfig({
        charlie: {
            echo: 2
        }
    });
  ```
- All settings for a feature can be cleared by passing `null`.

  ```
    // Configure features delta, golf, and hotel.
    googletag.setConfig({
        delta: {...},
        golf: {...},
        hotel: {...},
    });

    // Feature delta and hotel are cleared, but feature golf remains set.
    googletag.setConfig({
        delta: null,
        hotel: null,
    });
  ```

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adExpansion` | Settings to control ad expansion. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adsenseAttributes` | Setting to configure AdSense attributes. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.adYield` | **Deprecated.** |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.autoRefresh` | Setting to configure automatic ad refresh behavior. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.categoryExclusion` | Setting to configure ad category exclusions. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.centering` | Setting to control the horizontal centering of ads. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv` | Setting to control the collapsing behavior of ad slots. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.disableInitialLoad` | Setting to control when ads are requested. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.lazyLoad` | Settings to control the use of lazy loading in GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.location` | Setting to geo-target line items to geographic locations. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.pps` | Settings to control publisher provided signals (PPS). |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.privacyTreatments` | Settings to control publisher privacy treatments. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame` | Settings to control the use of [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest` | Setting to enable or disable Single Request Architecture (SRA). |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting` | Setting to control key-value targeting. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.threadYield` | Setting to control whether GPT should yield the JS thread when requesting and rendering creatives. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds` | Settings to control video ads. |

### Properties

*** ** * ** ***

#### `Optional` adExpansion

`adExpansion?: https://developers.google.com/publisher-tag/reference#googletag.config.AdExpansionConfig`Settings to control ad expansion.

*** ** * ** ***

#### `Optional` adsenseAttributes

`adsenseAttributes?: https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig`Setting to configure AdSense attributes.  

AdSense attributes configured via this setting will apply to all ad slots on the page. This setting may be called multiple times to define multiple attribute values, or overwrite existing values.  

AdSense attribute changes only apply to ads requested after this method has been called. For that reason, it is recommended to call this method before any calls to [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display) or [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh).

Example
:

    ### JavaScript

    ```javascript
    // Set the document language and page URL.
    googletag.setConfig({
      adsenseAttributes: { document_language: "en", page_url: "http://www.example.com" },
    });

    // Clear the page URL only.
    googletag.setConfig({ adsenseAttributes: { page_url: null } });

    // Clear all AdSense attributes.
    googletag.setConfig({ adsenseAttributes: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set the document language and page URL.
    googletag.setConfig({
      adsenseAttributes: { document_language: "en", page_url: "http://www.example.com" },
    });

    // Clear the page URL only.
    googletag.setConfig({ adsenseAttributes: { page_url: null } });

    // Clear all AdSense attributes.
    googletag.setConfig({ adsenseAttributes: null });
    ```

    ### TypeScript

    ```typescript
    // Set the document language and page URL.
    googletag.setConfig({
      adsenseAttributes: { document_language: "en", page_url: "http://www.example.com" },
    });

    // Clear the page URL only.
    googletag.setConfig({ adsenseAttributes: { page_url: null } });

    // Clear all AdSense attributes.
    googletag.setConfig({ adsenseAttributes: null });
    ```

*** ** * ** ***

#### `Optional` adYield

`adYield?: "DISABLED" | "ENABLED_ALL_SLOTS"`

> [!WARNING]
> **Deprecated:** Use [threadYield](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.threadYield) instead. This will be removed in the near future.

*** ** * ** ***

#### `Optional` autoRefresh

`autoRefresh?: https://developers.google.com/publisher-tag/reference#googletag.config.AutoRefreshConfig`Setting to configure automatic ad refresh behavior.

Example
:

    ### JavaScript

    ```javascript
    // Set the auto refresh configuration.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Set the auto refresh configuration.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration.
    googletag.setConfig({ autoRefresh: null });
    ```

    ### TypeScript

    ```typescript
    // Set the auto refresh configuration.
    googletag.setConfig({ autoRefresh: { heavyAds: false } });

    // Clear the auto refresh configuration.
    googletag.setConfig({ autoRefresh: null });
    ```

*** ** * ** ***

#### `Optional` categoryExclusion

`categoryExclusion?: string[]`Setting to configure ad category exclusions.

Example
:

    ### JavaScript

    ```javascript
    // Label = AirlineAd.
    googletag.setConfig({ categoryExclusion: ["AirlineAd"] });

    // Clearing category exclusion setting.
    googletag.setConfig({ categoryExclusion: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Label = AirlineAd.
    googletag.setConfig({ categoryExclusion: ["AirlineAd"] });

    // Clearing category exclusion setting.
    googletag.setConfig({ categoryExclusion: null });
    ```

    ### TypeScript

    ```typescript
    // Label = AirlineAd.
    googletag.setConfig({ categoryExclusion: ["AirlineAd"] });

    // Clearing category exclusion setting.
    googletag.setConfig({ categoryExclusion: null });
    ```

See also
:
    - [Custom labels to block ads](https://support.google.com/admanager/answer/3238504)

*** ** * ** ***

#### `Optional` centering

`centering?: boolean`Setting to control the horizontal centering of ads. Centering is disabled by default.  

Horizontal centering changes only apply to ads requested after this method has been called. For that reason, it is recommended to call this method before any calls to [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display) or [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh).

Example
:

    ### JavaScript

    ```javascript
    // Make ads centered.
    googletag.setConfig({ centering: true });

    // Clear the centering setting.
    googletag.setConfig({ centering: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Make ads centered.
    googletag.setConfig({ centering: true });

    // Clear the centering setting.
    googletag.setConfig({ centering: null });
    ```

    ### TypeScript

    ```typescript
    // Make ads centered.
    googletag.setConfig({ centering: true });

    // Clear the centering setting.
    googletag.setConfig({ centering: null });
    ```

*** ** * ** ***

#### `Optional` collapseDiv

`collapseDiv?: https://developers.google.com/publisher-tag/reference#googletag.config.CollapseDivBehavior`Setting to control the collapsing behavior of ad slots.  

A collapsed ad slot does not take up any space on the page.  

Supported values:

- `null` (default): The slot will not be collapsed.
- `DISABLED`: The slot will not collapse, whether or not an ad is returned.
- `BEFORE_FETCH`: The slot will start out collapsed, and expand when an ad is returned.
- `ON_NO_FILL`: The slot will start out expanded, and collapse if no ad is returned.

Example
:

    ### JavaScript

    ```javascript
    // Collapse the div for this slot if no ad is returned.
    googletag.setConfig({ collapseDiv: "ON_NO_FILL" });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    googletag.setConfig({ collapseDiv: "BEFORE_FETCH" });

    // Do not collapse the div for this slot.
    googletag.setConfig({ collapseDiv: "DISABLED" });

    // Clear the collapse setting.
    googletag.setConfig({ collapseDiv: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Collapse the div for this slot if no ad is returned.
    googletag.setConfig({ collapseDiv: "ON_NO_FILL" });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    googletag.setConfig({ collapseDiv: "BEFORE_FETCH" });

    // Do not collapse the div for this slot.
    googletag.setConfig({ collapseDiv: "DISABLED" });

    // Clear the collapse setting.
    googletag.setConfig({ collapseDiv: null });
    ```

    ### TypeScript

    ```typescript
    // Collapse the div for this slot if no ad is returned.
    googletag.setConfig({ collapseDiv: "ON_NO_FILL" });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    googletag.setConfig({ collapseDiv: "BEFORE_FETCH" });

    // Do not collapse the div for this slot.
    googletag.setConfig({ collapseDiv: "DISABLED" });

    // Clear the collapse setting.
    googletag.setConfig({ collapseDiv: null });
    ```

See also
:
    - [Collapse empty ad slots](https://developers.google.com/publisher-tag/samples/collapse-empty-ad-slots)
    - [Minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift)

*** ** * ** ***

#### `Optional` disableInitialLoad

`disableInitialLoad?: boolean`Setting to control when ads are requested.  

By default, the [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display) method both registers ad slots and requests ads for them. However, there are times when it may be preferable to separate these actions, in order to more precisely control when ad content is loaded.  

By enabling this setting, ads will not be requested for registered slots when the `display()` method is called. Instead, a separate call to [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh) must be made to initiate an ad request.  

This method *must* be called before calling [googletag.enableServices](https://developers.google.com/publisher-tag/reference#googletag.enableServices).

Example
:

    ### JavaScript

    ```javascript
    // Prevent requesting ads when `display()` is called.
    googletag.setConfig({ disableInitialLoad: true });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Prevent requesting ads when `display()` is called.
    googletag.setConfig({ disableInitialLoad: true });
    ```

    ### TypeScript

    ```typescript
    // Prevent requesting ads when `display()` is called.
    googletag.setConfig({ disableInitialLoad: true });
    ```

See also
:
    - [Control ad loading and refresh](https://developers.google.com/publisher-tag/guides/control-ad-loading)
    - [Control SRA batching](https://developers.google.com/publisher-tag/samples/control-sra-batching)

*** ** * ** ***

#### `Optional` lazyLoad

`lazyLoad?: https://developers.google.com/publisher-tag/reference#googletag.config.LazyLoadConfig`Settings to control the use of lazy loading in GPT.  

Lazy loading is a technique to delay the requesting and rendering of ads until they approach the user's viewport. For a more detailed example, see the [Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading) sample.  

**Note:** If [`singleRequest`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest) is enabled, lazy fetching only works when all slots are outside the fetch margin.  

Any lazy load settings which are not specified when calling `setConfig()` will use a default value set by Google. These defaults may be tuned over time. To disable a particular setting, set the value to `null`.

Example
:

    ### JavaScript

    ```javascript
    // Enable lazy loading.
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

    // Clear fetch margin only.
    googletag.setConfig({
      lazyLoad: { fetchMarginPercent: null },
    });

    // Clear all lazy loading settings.
    googletag.setConfig({ lazyLoad: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Enable lazy loading.
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

    // Clear fetch margin only.
    googletag.setConfig({
      lazyLoad: { fetchMarginPercent: null },
    });

    // Clear all lazy loading settings.
    googletag.setConfig({ lazyLoad: null });
    ```

    ### TypeScript

    ```typescript
    // Enable lazy loading.
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

    // Clear fetch margin only.
    googletag.setConfig({
      lazyLoad: { fetchMarginPercent: null },
    });

    // Clear all lazy loading settings.
    googletag.setConfig({ lazyLoad: null });
    ```

See also
:
    - [Ads best practices: Prioritize "important" ad slots](https://developers.google.com/publisher-tag/guides/ad-best-practices#prioritize_important_ad_slots)
    - [Lazy loading](https://developers.google.com/publisher-tag/samples/lazy-loading)

*** ** * ** ***

#### `Optional` location

`location?: string`Setting to geo-target line items to geographic locations.

Example
:

    ### JavaScript

    ```javascript
    // Geo-target line items to US postal code 10001.
    googletag.setConfig({ location: "10001,US" });

    // Clear the location setting.
    googletag.setConfig({ location: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Geo-target line items to US postal code 10001.
    googletag.setConfig({ location: "10001,US" });

    // Clear the location setting.
    googletag.setConfig({ location: null });
    ```

    ### TypeScript

    ```typescript
    // Geo-target line items to US postal code 10001.
    googletag.setConfig({ location: "10001,US" });

    // Clear the location setting.
    googletag.setConfig({ location: null });
    ```

See also
:
    - [Target geographic locations for delivery](https://support.google.com/admanager/answer/1260290)

*** ** * ** ***

#### `Optional` pps

`pps?: https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig`Settings to control publisher provided signals (PPS).

*** ** * ** ***

#### `Optional` privacyTreatments

`privacyTreatments?: https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatmentsConfig`Settings to control publisher privacy treatments.

*** ** * ** ***

#### `Optional` safeFrame

`safeFrame?: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig`Settings to control the use of [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT.  

Values configured via this setting will apply to all ad slots on the page. Individual ad slots may override these values via [SlotSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame).

Example
:

    ### JavaScript

    ```javascript
    // Force SafeFrame for all ads on the page.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion.
    googletag.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings.
    googletag.setConfig({ safeFrame: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Force SafeFrame for all ads on the page.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion.
    googletag.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings.
    googletag.setConfig({ safeFrame: null });
    ```

    ### TypeScript

    ```typescript
    // Force SafeFrame for all ads on the page.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion.
    googletag.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting.
    googletag.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings.
    googletag.setConfig({ safeFrame: null });
    ```

*** ** * ** ***

#### `Optional` singleRequest

`singleRequest?: boolean`Setting to enable or disable Single Request Architecture (SRA).  

When SRA is enabled, all ad slots defined prior to a [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display) or [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh) call will be batched into a single ad request. This provides performance benefits, but is also necessary to ensure roadblocks and competetive exclusions are honored.  

When SRA is disabled, each ad slot is requested individually. This is the default behavior of GPT.  

This method *must* be called prior to calling [googletag.enableServices](https://developers.google.com/publisher-tag/reference#googletag.enableServices).

Example
:

    ### JavaScript

    ```javascript
    // Enable Single Request Architecture.
    googletag.setConfig({ singleRequest: true });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Enable Single Request Architecture.
    googletag.setConfig({ singleRequest: true });
    ```

    ### TypeScript

    ```typescript
    // Enable Single Request Architecture.
    googletag.setConfig({ singleRequest: true });
    ```

See also
:
    - [About roadblocks](https://support.google.com/admanager/answer/177277)
    - [Ads best practices: Use Single Request Architecture correctly](https://developers.google.com/publisher-tag/guides/ad-best-practices#use_single_request_architecture_correctly)
    - [Control SRA batching](https://developers.google.com/publisher-tag/samples/control-sra-batching)

*** ** * ** ***

#### `Optional` targeting

`targeting?: Record<string, string | string[]>`Setting to control key-value targeting.  

Targeting configured via this setting will apply to all ad slots on the page. This setting may be called multiple times to define multiple targeting key-values, or overwrite existing values. Targeting keys are defined in your Google Ad Manager account.

Example
:

    ### JavaScript

    ```javascript
    // Setting a single targeting key-value.
    googletag.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key
    googletag.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    googletag.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    googletag.setConfig({ targeting: { interests: null } });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Setting a single targeting key-value.
    googletag.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key
    googletag.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    googletag.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    googletag.setConfig({ targeting: { interests: null } });
    ```

    ### TypeScript

    ```typescript
    // Setting a single targeting key-value.
    googletag.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key
    googletag.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    googletag.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    googletag.setConfig({ targeting: { interests: null } });
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

*** ** * ** ***

#### `Optional` threadYield

`threadYield?: "DISABLED" | "ENABLED_ALL_SLOTS"`Setting to control whether GPT should yield the JS thread when requesting and rendering creatives.  

GPT will yield only for browsers that support the Scheduler.postTask or Scheduler.yield API.  

Supported values:

- `null` (default): GPT will yield the JS thread for slots outside of the viewport.
- `ENABLED_ALL_SLOTS`: GPT will yield the JS thread for all slots regardless of whether the slot is within the viewport.
- `DISABLED`: GPT will not yield the JS thread.

Example
:

    ### JavaScript

    ```javascript
    // Disable yielding.
    googletag.setConfig({ threadYield: "DISABLED" });

    // Enable yielding for all slots.
    googletag.setConfig({ threadYield: "ENABLED_ALL_SLOTS" });

    // Enable yielding only for slots outside of the viewport (default).
    googletag.setConfig({ threadYield: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Disable yielding.
    googletag.setConfig({ threadYield: "DISABLED" });

    // Enable yielding for all slots.
    googletag.setConfig({ threadYield: "ENABLED_ALL_SLOTS" });

    // Enable yielding only for slots outside of the viewport (default).
    googletag.setConfig({ threadYield: null });
    ```

    ### TypeScript

    ```typescript
    // Disable yielding.
    googletag.setConfig({ threadYield: "DISABLED" });

    // Enable yielding for all slots.
    googletag.setConfig({ threadYield: "ENABLED_ALL_SLOTS" });

    // Enable yielding only for slots outside of the viewport (default).
    googletag.setConfig({ threadYield: null });
    ```

See also
:
    - [Scheduler](https://developer.mozilla.org/docs/Web/API/Scheduler)

*** ** * ** ***

#### `Optional` videoAds

`videoAds?: https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig`Settings to control video ads.

Example
:

    ### JavaScript

    ```javascript
    // Enable video ads and set video content and content source IDs.
    googletag.setConfig({
      videoAds: {
        enableVideoAds: true,
        videoContentId: "e1eGlRL7ju8",
        videoCmsId: "1234567",
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Enable video ads and set video content and content source IDs.
    googletag.setConfig({
      videoAds: {
        enableVideoAds: true,
        videoContentId: "e1eGlRL7ju8",
        videoCmsId: "1234567",
      },
    });
    ```

    ### TypeScript

    ```typescript
    // Enable video ads and set video content and content source IDs.
    googletag.setConfig({
      videoAds: {
        enableVideoAds: true,
        videoContentId: "e1eGlRL7ju8",
        videoCmsId: "1234567",
      },
    });
    ```

See also
:
    - [Video content ingestion](https://support.google.com/admanager/topic/9210762)

*** ** * ** ***

## googletag.config.PrivacyTreatmentsConfig

Settings to control publisher privacy treatments.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.PrivacyTreatmentsConfig.treatments` | An array of publisher privacy treatments to enable. |

### Properties

*** ** * ** ***

#### treatments

`treatments: "disablePersonalization"[]`An array of publisher privacy treatments to enable.

Example
:

    ### JavaScript

    ```javascript
    // Disable personalization across the entire page.
    googletag.setConfig({
      privacyTreatments: { treatments: ["disablePersonalization"] },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // Disable personalization across the entire page.
    googletag.setConfig({
      privacyTreatments: { treatments: ["disablePersonalization"] },
    });
    ```

    ### TypeScript

    ```typescript
    // Disable personalization across the entire page.
    googletag.setConfig({
      privacyTreatments: { treatments: ["disablePersonalization"] },
    });
    ```

*** ** * ** ***

## googletag.config.PublisherProvidedSignalsConfig

Publisher provided signals (PPS) configuration object.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.PublisherProvidedSignalsConfig.taxonomies` | An object containing [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy) mappings or null to clear the config. |

Example
:

    ### JavaScript

    ```javascript
    googletag.setConfig({
      pps: {
        taxonomies: {
          IAB_AUDIENCE_1_1: { values: ["6", "626"] },
          // '6' = 'Demographic | Age Range | 30-34'
          // '626' = 'Interest | Sports | Darts'
          IAB_CONTENT_2_2: { values: ["48", "127"] },
          // '48' = 'Books and Literature | Fiction'
          // '127' = 'Careers | Job Search'
        },
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    googletag.setConfig({
      pps: {
        taxonomies: {
          IAB_AUDIENCE_1_1: { values: ["6", "626"] },
          // '6' = 'Demographic | Age Range | 30-34'
          // '626' = 'Interest | Sports | Darts'
          IAB_CONTENT_2_2: { values: ["48", "127"] },
          // '48' = 'Books and Literature | Fiction'
          // '127' = 'Careers | Job Search'
        },
      },
    });
    ```

    ### TypeScript

    ```typescript
    googletag.setConfig({
      pps: {
        taxonomies: {
          IAB_AUDIENCE_1_1: { values: ["6", "626"] },
          // '6' = 'Demographic | Age Range | 30-34'
          // '626' = 'Interest | Sports | Darts'
          IAB_CONTENT_2_2: { values: ["48", "127"] },
          // '48' = 'Books and Literature | Fiction'
          // '127' = 'Careers | Job Search'
        },
      },
    });
    ```

See also
:
    - [About publisher provided signals (Beta)](https://support.google.com/admanager/answer/12451124)
    - [IAB Audience Taxonomy 1.1](https://iabtechlab.com/standards/audience-taxonomy/)
    - [IAB Content Taxonomy 2.2](https://iabtechlab.com/standards/content-taxonomy/)

### Properties

*** ** * ** ***

#### taxonomies

`taxonomies: Partial<Record<https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy, https://developers.google.com/publisher-tag/reference#googletag.config.TaxonomyData>>`An object containing [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy) mappings or null to clear the config.

*** ** * ** ***

## googletag.config.SafeFrameConfig

Settings to control [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.allowOverlayExpansion` | Whether SafeFrame should allow ad content to expand by overlaying page content. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.allowPushExpansion` | Whether SafeFrame should allow ad content to expand by pushing page content. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.forceSafeFrame` | Whether ad(s) should be forced to be rendered using a SafeFrame container. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.sandbox` | Whether SafeFrame should use the HTML5 sandbox attribute to prevent top level navigation without user interaction. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig.useUniqueDomain` | **Deprecated.**Whether SafeFrame should use randomized subdomains for Reservation creatives. |

See also
:
    - [PageSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame)
    - [SlotSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame)

### Properties

*** ** * ** ***

#### `Optional` allowOverlayExpansion

`allowOverlayExpansion?: boolean`Whether SafeFrame should allow ad content to expand by overlaying page content.

*** ** * ** ***

#### `Optional` allowPushExpansion

`allowPushExpansion?: boolean`Whether SafeFrame should allow ad content to expand by pushing page content.

*** ** * ** ***

#### `Optional` forceSafeFrame

`forceSafeFrame?: boolean`Whether ad(s) should be forced to be rendered using a SafeFrame container.

*** ** * ** ***

#### `Optional` sandbox

`sandbox?: boolean`Whether SafeFrame should use the HTML5 sandbox attribute to prevent top level navigation without user interaction. The only valid value is `true` (cannot be forced to `false`). Note that the sandbox attribute disables plugins (e.g. Flash).

*** ** * ** ***

#### `Optional` useUniqueDomain

`useUniqueDomain?: boolean`Whether SafeFrame should use randomized subdomains for Reservation creatives. Pass in `null` to clear the stored value.  

Note: this feature is enabled by default.

> [!WARNING]
> **Deprecated:** It is no longer possible to disable this feature. Setting `useUniqueDomain` has no effect.

See also
:
    - [Render creatives using SafeFrame](https://support.google.com/admanager/answer/9999596)

*** ** * ** ***

## googletag.config.SlotSettingsConfig

Main configuration interface for slot-level settings.  

Allows setting multiple features with a single API call for a single slot.  

All properties listed below are examples and do not reflect actual features that utilize setConfig. For the set of features, see fields within the SlotSettingsConfig type below.  

Examples:

- Only features specified in the [Slot.setConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.setConfig) call are modified.

  ```
    const slot = googletag.defineSlot("/1234567/example", [160, 600]);

    // Configure feature alpha.
    slot.setConfig({
        alpha: {...}
    });

    // Configure feature bravo. Feature alpha is unchanged.
    slot.setConfig({
       bravo: {...}
    });
  ```
- All settings for a given feature are updated with each call to [Slot.setConfig](https://developers.google.com/publisher-tag/reference#googletag.Slot.setConfig).

  ```
    // Configure feature charlie to echo = 1, foxtrot = true.
    slot.setConfig({
        charlie: {
            echo: 1,
            foxtrot: true,
        }
    });

    // Update feature charlie to echo = 2. Since foxtrot was not specified,
    // the value is cleared.
    slot.setConfig({
        charlie: {
            echo: 2
        }
    });
  ```
- All settings for a feature can be cleared by passing `null`.

  ```
    // Configure features delta, golf, and hotel.
    slot.setConfig({
        delta: {...},
        golf: {...},
        hotel: {...},
    });

    // Feature delta and hotel are cleared, but feature golf remains set.
    slot.setConfig({
        delta: null,
        hotel: null,
    });
  ```

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adExpansion` | Settings to configure ad expansion. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.adsenseAttributes` | Setting to configure AdSense attributes. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.categoryExclusion` | Setting to configure ad category exclusions. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.clickUrl` | Setting to configure the URL to which users will be redirected after clicking on the ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.collapseDiv` | Setting to configure the collapsing behavior of the ad slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.continueButton` | Settings to configure the continue button behavior for content pause ads. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.interstitial` | Settings that configure interstitial ad slot behavior. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.safeFrame` | Settings to configure the use of [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting` | Setting to configure key-value targeting. |

### Properties

*** ** * ** ***

#### `Optional` adExpansion

`adExpansion?: https://developers.google.com/publisher-tag/reference#googletag.config.AdExpansionConfig`Settings to configure ad expansion.

See also
:
    - [Ad expansion](https://support.google.com/admanager/answer/9117822)

*** ** * ** ***

#### `Optional` adsenseAttributes

`adsenseAttributes?: https://developers.google.com/publisher-tag/reference#googletag.config.AdSenseAttributesConfig`Setting to configure AdSense attributes.  

AdSense attributes configured via this setting will only apply to the ad slot. This setting may be called multiple times to define multiple attribute values, or overwrite existing values.  

AdSense attribute changes only apply to ads requested after this method has been called. For that reason, it is recommended to call this method before any calls to [googletag.display](https://developers.google.com/publisher-tag/reference#googletag.display) or [PubAdsService.refresh](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService.refresh).

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Set the AdSense ad format and channel IDs.
    slot.setConfig({
      adsenseAttributes: {
        adsense_ad_format: "120x240_as",
        adsense_channel_ids: "271828183+314159265",
      },
    });

    // Clear the AdSense channel IDs only.
    slot.setConfig({ adsenseAttributes: { adsense_channel_ids: null } });

    // Clear all AdSense attributes.
    slot.setConfig({ adsenseAttributes: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Set the AdSense ad format and channel IDs.
    slot.setConfig({
      adsenseAttributes: {
        adsense_ad_format: "120x240_as",
        adsense_channel_ids: "271828183+314159265",
      },
    });

    // Clear the AdSense channel IDs only.
    slot.setConfig({ adsenseAttributes: { adsense_channel_ids: null } });

    // Clear all AdSense attributes.
    slot.setConfig({ adsenseAttributes: null });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Set the AdSense ad format and channel IDs.
    slot.setConfig({
      adsenseAttributes: {
        adsense_ad_format: "120x240_as",
        adsense_channel_ids: "271828183+314159265",
      },
    });

    // Clear the AdSense channel IDs only.
    slot.setConfig({ adsenseAttributes: { adsense_channel_ids: null } });

    // Clear all AdSense attributes.
    slot.setConfig({ adsenseAttributes: null });
    ```

*** ** * ** ***

#### `Optional` categoryExclusion

`categoryExclusion?: string[]`Setting to configure ad category exclusions.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Label = AirlineAd
    slot.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Clearing category exclusion setting.
    slot.setConfig({ categoryExclusion: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Label = AirlineAd
    slot.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Clearing category exclusion setting.
    slot.setConfig({ categoryExclusion: null });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Label = AirlineAd
    slot.setConfig({
      categoryExclusion: ["AirlineAd"],
    });

    // Clearing category exclusion setting.
    slot.setConfig({ categoryExclusion: null });
    ```

See also
:
    - [Custom labels to block ads](https://support.google.com/admanager/answer/3238504)

*** ** * ** ***

#### `Optional` clickUrl

`clickUrl?: string`Setting to configure the URL to which users will be redirected after clicking on the ad.  

The Google Ad Manager servers still record a click even if the click URL is replaced. Any landing page URL associated with the creative that is served is appended to the provided value. Setting this value more than once will overwrite any previously configured value. Passing in `null` will clear the value.  

**Note:** This setting only applies to [non-SRA requests](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.singleRequest).

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Sets the click URL to 'http://www.example.com?original_click_url='.
    slot.setConfig({
      clickUrl: "http://www.example.com?original_click_url=",
    });

    // Clears the click URL.
    slot.setConfig({
      clickUrl: null,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Sets the click URL to 'http://www.example.com?original_click_url='.
    slot.setConfig({
      clickUrl: "http://www.example.com?original_click_url=",
    });

    // Clears the click URL.
    slot.setConfig({
      clickUrl: null,
    });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Sets the click URL to 'http://www.example.com?original_click_url='.
    slot.setConfig({
      clickUrl: "http://www.example.com?original_click_url=",
    });

    // Clears the click URL.
    slot.setConfig({
      clickUrl: null,
    });
    ```

*** ** * ** ***

#### `Optional` collapseDiv

`collapseDiv?: https://developers.google.com/publisher-tag/reference#googletag.config.CollapseDivBehavior`Setting to configure the collapsing behavior of the ad slot.  

A collapsed ad slot does not take up any space on the page.  

Supported values:

- `null` (default): The slot will not be collapsed.
- `DISABLED`: The slot will not collapse, whether or not an ad is returned.
- `BEFORE_FETCH`: The slot will start out collapsed, and expand when an ad is returned.
- `ON_NO_FILL`: The slot will start out expanded, and collapse if no ad is returned.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Collapse the div for this slot if no ad is returned.
    slot.setConfig({
      collapseDiv: "ON_NO_FILL",
    });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    slot.setConfig({
      collapseDiv: "BEFORE_FETCH",
    });

    // Do not collapse the div for this slot.
    slot.setConfig({
      collapseDiv: "DISABLED",
    });

    // Clear the collapse setting.
    slot.setConfig({
      collapseDiv: null,
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Collapse the div for this slot if no ad is returned.
    slot.setConfig({
      collapseDiv: "ON_NO_FILL",
    });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    slot.setConfig({
      collapseDiv: "BEFORE_FETCH",
    });

    // Do not collapse the div for this slot.
    slot.setConfig({
      collapseDiv: "DISABLED",
    });

    // Clear the collapse setting.
    slot.setConfig({
      collapseDiv: null,
    });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Collapse the div for this slot if no ad is returned.
    slot.setConfig({
      collapseDiv: "ON_NO_FILL",
    });

    // Collapse the div for this slot by default, and expand only
    // if an ad is returned.
    slot.setConfig({
      collapseDiv: "BEFORE_FETCH",
    });

    // Do not collapse the div for this slot.
    slot.setConfig({
      collapseDiv: "DISABLED",
    });

    // Clear the collapse setting.
    slot.setConfig({
      collapseDiv: null,
    });
    ```

See also
:
    - [Collapse empty ad slots](https://developers.google.com/publisher-tag/samples/collapse-empty-ad-slots)
    - [Minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift)

*** ** * ** ***

#### `Optional` continueButton

`continueButton?: https://developers.google.com/publisher-tag/reference#googletag.config.ContinueButtonConfig`Settings to configure the continue button behavior for content pause ads.  

These settings allow customizing the appearance and behavior of the exit and continue reading interactions associated with content pause formats.  

Any continue button settings which are not specified when calling `setConfig()` will use a default value set by Google.  

To disable or clear all continue button settings, pass `null`.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());
    // Configure continue button settings.
    slot.setConfig({
      continueButton: {
        font: "Arial",
        fontColor: "white",
        backgroundColor: "blue",
        targetId: "target-div-id",
        freqCapIntervalMinutes: 20,
      },
    });

    // Clear continue button settings.
    slot.setConfig({ continueButton: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());
    // Configure continue button settings.
    slot.setConfig({
      continueButton: {
        font: "Arial",
        fontColor: "white",
        backgroundColor: "blue",
        targetId: "target-div-id",
        freqCapIntervalMinutes: 20,
      },
    });

    // Clear continue button settings.
    slot.setConfig({ continueButton: null });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());
    // Configure continue button settings.
    slot.setConfig({
      continueButton: {
        font: "Arial",
        fontColor: "white",
        backgroundColor: "blue",
        targetId: "target-div-id",
        freqCapIntervalMinutes: 20,
      },
    });

    // Clear continue button settings.
    slot.setConfig({ continueButton: null });
    ```

*** ** * ** ***

#### `Optional` interstitial

`interstitial?: https://developers.google.com/publisher-tag/reference#googletag.config.InterstitialConfig`Settings that configure interstitial ad slot behavior.

See also
:
    - [Traffic web interstitials](https://support.google.com/admanager/answer/9840201)

*** ** * ** ***

#### `Optional` safeFrame

`safeFrame?: https://developers.google.com/publisher-tag/reference#googletag.config.SafeFrameConfig`Settings to configure the use of [SafeFrame](https://support.google.com/admanager/answer/6023110) in GPT.  

Values configured via this setting will only apply to the ad slot, and override values set via [PageSettingsConfig.safeFrame](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame).

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Force SafeFrame for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion for the slot.
    slot.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings for the slot.
    slot.setConfig({ safeFrame: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Force SafeFrame for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion for the slot.
    slot.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings for the slot.
    slot.setConfig({ safeFrame: null });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Force SafeFrame for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: true },
    });

    // Configure SafeFrame to allow overlay expansion for the slot.
    slot.setConfig({
      safeFrame: { allowOverlayExpansion: true },
    });

    // Clear forceSafeFrame setting for the slot.
    slot.setConfig({
      safeFrame: { forceSafeFrame: null },
    });

    // Clear all SafeFrame settings for the slot.
    slot.setConfig({ safeFrame: null });
    ```

*** ** * ** ***

#### `Optional` targeting

`targeting?: Record<string, string | string[]>`Setting to configure key-value targeting.  

Targeting configured via this setting will only apply to the ad slot. This setting may be called multiple times to define multiple targeting key-values, or overwrite existing values. Targeting keys are defined in your Google Ad Manager account.

Example
:

    ### JavaScript

    ```javascript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Setting a single targeting key-value.
    slot.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key.
    slot.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    slot.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    slot.setConfig({ targeting: { interests: null } });

    // Clear all targeting keys.
    slot.setConfig({ targeting: null });
    ```

    ### JavaScript (legacy)

    ```javascript
    var slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")
      .addService(googletag.pubads());

    // Setting a single targeting key-value.
    slot.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key.
    slot.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    slot.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    slot.setConfig({ targeting: { interests: null } });

    // Clear all targeting keys.
    slot.setConfig({ targeting: null });
    ```

    ### TypeScript

    ```typescript
    const slot = googletag
      .defineSlot("/1234567/sports", [160, 600], "div")!
      .addService(googletag.pubads());

    // Setting a single targeting key-value.
    slot.setConfig({ targeting: { interests: "sports" } });

    // Setting multiple values for a single targeting key.
    slot.setConfig({ targeting: { interests: ["sports", "music"] } });

    // Setting multiple targeting key-values at once.
    slot.setConfig({ targeting: { interests: ["sports", "music"], color: "red" } });

    // Clearing a single targeting key.
    slot.setConfig({ targeting: { interests: null } });

    // Clear all targeting keys.
    slot.setConfig({ targeting: null });
    ```

See also
:
    - [Key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting)

*** ** * ** ***

## googletag.config.TaxonomyData

An object containing the values for a single [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy).

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.TaxonomyData.values` | A list of [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy) values. |

### Properties

*** ** * ** ***

#### values

`values: readonly string[]`A list of [Taxonomy](https://developers.google.com/publisher-tag/reference#googletag.config.Taxonomy) values.

*** ** * ** ***

## googletag.config.VideoAdsConfig

Settings to configure video ad related settings.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.enableVideoAds` | Whether videos ads will be present on the page. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoCmsId` | The video content source ID. |
| `https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoContentId` | The video content ID. |

See also
:
    - [PageSettingsConfig.videoAds](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.videoAds)

### Properties

*** ** * ** ***

#### enableVideoAds

`enableVideoAds: boolean`Whether videos ads will be present on the page.  

When set to `true`, this enables content exclusion constraints on display and video ads.  

If the video content is known, set [videoContentId](https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoContentId) and [videoCmsId](https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoCmsId) to the values provided to the Google Ad Manager content ingestion service to utilize content exclusion for display ads.

*** ** * ** ***

#### `Optional` videoCmsId

`videoCmsId?: string`The video content source ID.  

This is a unique value assigned by the Google Ad Manager content ingestion service to identify the source of video content specified by [videoContentId](https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoContentId).

See also
:
    - [cmsid (Content Source ID)](https://support.google.com/admanager/answer/10678356#cmsid-vid&zippy=%2Ccmsid-content-source-id)

*** ** * ** ***

#### `Optional` videoContentId

`videoContentId?: string`The video content ID.  

This is a unique value that identifies a particular video from the content source specified by [videoCmsId](https://developers.google.com/publisher-tag/reference#googletag.config.VideoAdsConfig.videoCmsId). This value is assigned by the CMS that hosts your video content.

See also
:
    - [vid (Video ID)](https://support.google.com/admanager/answer/10678356#vid&zippy=%2Cvid-video-id)

*** ** * ** ***

## googletag.enums

This is the namespace that GPT uses for enum types.

| Enumerations ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.enums.OutOfPageFormat` | Out-of-page formats supported by GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.enums.TagForAgeTreatment` | Age treatment settings supported by GPT. |
| `https://developers.google.com/publisher-tag/reference#googletag.enums.TrafficSource` | [Traffic sources](https://support.google.com/admanager/answer/11233407) supported by GPT. |

### Enumerations

*** ** * ** ***

#### OutOfPageFormat

`OutOfPageFormat`Out-of-page formats supported by GPT.

See also
:
    - [defineOutOfPageSlot](https://developers.google.com/publisher-tag/reference#googletag.defineOutOfPageSlot)

| Enumeration Members ||
|---|---|
| `AD_INTENTS` | Ad Intents format. |
| `BOTTOM_ANCHOR` | Anchor format where slot sticks to the bottom of the viewport. |
| `GAME_MANUAL_INTERSTITIAL` | Game manual interstitial format. **Note:** Game manual interstitial is a [limited-access](https://support.google.com/admanager/answer/14640119) format. |
| `INTERSTITIAL` | Web interstitial creative format. |
| `LEFT_SIDE_RAIL` | Left side rail format. |
| `REWARDED` | Rewarded format. |
| `RIGHT_SIDE_RAIL` | Right side rail format. |
| `TOP_ANCHOR` | Anchor format where slot sticks to the top of the viewport. |

*** ** * ** ***

#### TagForAgeTreatment

`TagForAgeTreatment`Age treatment settings supported by GPT.

See also
:
    - [PrivacySettingsConfig.tagForAgeTreatment](https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.tagForAgeTreatment)

| Enumeration Members ||
|---|---|
| `CHILD` | Indicates that ad requests should receive CHILD age treatment. |
| `TEEN` | Indicates that ad requests should receive TEEN age treatment. |
| `UNSPECIFIED` | Default value. Indicates that no specific age restricted treatment signal applies to the ad request. |

*** ** * ** ***

#### TrafficSource

`TrafficSource`[Traffic sources](https://support.google.com/admanager/answer/11233407) supported by GPT.

See also
:
    - [PrivacySettingsConfig.trafficSource](https://developers.google.com/publisher-tag/reference#googletag.PrivacySettingsConfig.trafficSource)

| Enumeration Members ||
|---|---|
| `ORGANIC` | Direct URL entry, site search, or app download. |
| `PURCHASED` | Traffic redirected from properties other than owned (acquired or otherwise incentivized activity). |

*** ** * ** ***

## googletag.events

This is the namespace that GPT uses for Events. Your code can react to these events using Service.addEventListener.

| Interfaces ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event` | Base Interface for all GPT events. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap` | This is a pseudo-type that maps an event name to its corresponding event object type for [Service.addEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener) and [Service.removeEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent` | This event is fired when a game manual interstitial slot has been closed by the user. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent` | This event is fired when a game manual interstitial slot is ready to be shown to the user. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent` | This event is fired when an impression becomes viewable, according to the [Active View criteria](https://support.google.com/admanager/answer/4524488). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotClosedEvent` | This event is fired when a rewarded ad slot is closed by the user. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent` | This event is fired when a reward is granted for viewing a [rewarded ad](https://support.google.com/admanager/answer/9116812). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent` | This event is fired when a [rewarded ad](https://support.google.com/admanager/answer/9116812) is ready to be displayed. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotVideoCompletedEvent` | This event is fired when a rewarded video ad has finished playing. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent` | This event is fired when the creative's iframe fires its load event. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent` | This event is fired when the creative code is injected into a slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent` | This event is fired when an ad has been requested for a particular slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived` | This event is fired when an ad response has been received for a particular slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent` | This event is fired whenever the on-screen percentage of an ad slot's area changes. |

*** ** * ** ***

## googletag.events.Event

Base Interface for all GPT events. All GPT events below will have the following fields.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. |

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

### Properties

*** ** * ** ***

#### serviceName

`serviceName: string`Name of the service that triggered the event.

*** ** * ** ***

#### slot

`slot: https://developers.google.com/publisher-tag/reference#googletag.Slot`The slot that triggered the event.

*** ** * ** ***

## googletag.events.EventTypeMap

This is a pseudo-type that maps an event name to its corresponding event object type for [Service.addEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service.addEventListener) and [Service.removeEventListener](https://developers.google.com/publisher-tag/reference#googletag.Service.removeEventListener). It is documented for reference and type safety purposes only.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.gameManualInterstitialSlotClosed` | Alias for [events.GameManualInterstitialSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.gameManualInterstitialSlotReady` | Alias for [events.GameManualInterstitialSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.impressionViewable` | Alias for [events.ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.rewardedSlotClosed` | Alias for [events.RewardedSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotClosedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.rewardedSlotGranted` | Alias for [events.RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.rewardedSlotReady` | Alias for [events.RewardedSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.rewardedSlotVideoCompleted` | Alias for [events.RewardedSlotVideoCompletedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotVideoCompletedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.slotOnload` | Alias for [events.SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.slotRenderEnded` | Alias for [events.SlotRenderEndedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.slotRequested` | Alias for [events.SlotRequestedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.slotResponseReceived` | Alias for [events.SlotResponseReceived](https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived). |
| `https://developers.google.com/publisher-tag/reference#googletag.events.EventTypeMap.slotVisibilityChanged` | Alias for [events.SlotVisibilityChangedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent). |

### Properties

*** ** * ** ***

#### gameManualInterstitialSlotClosed

`gameManualInterstitialSlotClosed: https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent`Alias for [events.GameManualInterstitialSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotClosedEvent).

*** ** * ** ***

#### gameManualInterstitialSlotReady

`gameManualInterstitialSlotReady: https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent`Alias for [events.GameManualInterstitialSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent).

*** ** * ** ***

#### impressionViewable

`impressionViewable: https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent`Alias for [events.ImpressionViewableEvent](https://developers.google.com/publisher-tag/reference#googletag.events.ImpressionViewableEvent).

*** ** * ** ***

#### rewardedSlotClosed

`rewardedSlotClosed: https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotClosedEvent`Alias for [events.RewardedSlotClosedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotClosedEvent).

*** ** * ** ***

#### rewardedSlotGranted

`rewardedSlotGranted: https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent`Alias for [events.RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent).

*** ** * ** ***

#### rewardedSlotReady

`rewardedSlotReady: https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent`Alias for [events.RewardedSlotReadyEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent).

*** ** * ** ***

#### rewardedSlotVideoCompleted

`rewardedSlotVideoCompleted: https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotVideoCompletedEvent`Alias for [events.RewardedSlotVideoCompletedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotVideoCompletedEvent).

*** ** * ** ***

#### slotOnload

`slotOnload: https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent`Alias for [events.SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent).

*** ** * ** ***

#### slotRenderEnded

`slotRenderEnded: https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent`Alias for [events.SlotRenderEndedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent).

*** ** * ** ***

#### slotRequested

`slotRequested: https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent`Alias for [events.SlotRequestedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotRequestedEvent).

*** ** * ** ***

#### slotResponseReceived

`slotResponseReceived: https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived`Alias for [events.SlotResponseReceived](https://developers.google.com/publisher-tag/reference#googletag.events.SlotResponseReceived).

*** ** * ** ***

#### slotVisibilityChanged

`slotVisibilityChanged: https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent`Alias for [events.SlotVisibilityChangedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent).

*** ** * ** ***

## googletag.events.GameManualInterstitialSlotClosedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a game manual interstitial slot has been closed by the user.  

**Note:** Game manual interstitial is a [limited-access](https://support.google.com/admanager/answer/14640119) format.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when a game manual interstitial slot is closed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", (event) => {
        const slot = event.slot;
        console.log("Game manual interstital slot", slot.getSlotElementId(), "is closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when a game manual interstitial slot is closed.
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", function (event) {
        var slot = event.slot;
        console.log("Game manual interstital slot", slot.getSlotElementId(), "is closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    // This listener is called when a game manual interstitial slot is closed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotClosed", (event) => {
        const slot = event.slot;
        console.log("Game manual interstital slot", slot.getSlotElementId(), "is closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a game manual interstitial ad](https://support.google.com/admanager/answer/14640119)

*** ** * ** ***

## googletag.events.GameManualInterstitialSlotReadyEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a game manual interstitial slot is ready to be shown to the user.  

**Note:** Game manual interstitial is a [limited-access](https://support.google.com/admanager/answer/14640119) format.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.GameManualInterstitialSlotReadyEvent.makeGameManualInterstitialVisible` | Displays the game manual interstitial ad to the user. |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when a game manual interstitial slot is ready to
    // be displayed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotReady", (event) => {
        const slot = event.slot;
        console.log(
          "Game manual interstital slot",
          slot.getSlotElementId(),
          "is ready to be displayed.",
        );

        // Replace with custom logic.
        const displayGmiAd = true;
        if (displayGmiAd) {
          event.makeGameManualInterstitialVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when a game manual interstitial slot is ready to
    // be displayed.
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotReady", function (event) {
        var slot = event.slot;
        console.log(
          "Game manual interstital slot",
          slot.getSlotElementId(),
          "is ready to be displayed.",
        );

        // Replace with custom logic.
        var displayGmiAd = true;
        if (displayGmiAd) {
          event.makeGameManualInterstitialVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    // This listener is called when a game manual interstitial slot is ready to
    // be displayed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.GAME_MANUAL_INTERSTITIAL,
    );

    // Slot returns null if the page or device does not support game manual interstitial ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      googletag.pubads().addEventListener("gameManualInterstitialSlotReady", (event) => {
        const slot = event.slot;
        console.log(
          "Game manual interstital slot",
          slot.getSlotElementId(),
          "is ready to be displayed.",
        );

        // Replace with custom logic.
        const displayGmiAd = true;
        if (displayGmiAd) {
          event.makeGameManualInterstitialVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a game manual interstitial ad](https://support.google.com/admanager/answer/14640119)

### Methods

*** ** * ** ***

#### makeGameManualInterstitialVisible

`makeGameManualInterstitialVisible(): boolean`Displays the game manual interstitial ad to the user. Returns whether the ad was successfully displayed.

| Returns ||
|---|---|
| `boolean` |   |

*** ** * ** ***

## googletag.events.ImpressionViewableEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when an impression becomes viewable, according to the [Active View criteria](https://support.google.com/admanager/answer/4524488).

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when an impression becomes viewable.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("impressionViewable", (event) => {
      const slot = event.slot;
      console.log("Impression for slot", slot.getSlotElementId(), "became viewable.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when an impression becomes viewable.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("impressionViewable", function (event) {
      var slot = event.slot;
      console.log("Impression for slot", slot.getSlotElementId(), "became viewable.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called when an impression becomes viewable.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("impressionViewable", (event) => {
      const slot = event.slot;
      console.log("Impression for slot", slot.getSlotElementId(), "became viewable.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

*** ** * ** ***

## googletag.events.RewardedSlotClosedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a rewarded ad slot is closed by the user. It may fire either before or after a reward has been granted. To determine whether a reward has been granted, use [events.RewardedSlotGrantedEvent](https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent) instead.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the user closes a rewarded ad slot.
      googletag.pubads().addEventListener("rewardedSlotClosed", (event) => {
        const slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "has been closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the user closes a rewarded ad slot.
      googletag.pubads().addEventListener("rewardedSlotClosed", function (event) {
        var slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "has been closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the user closes a rewarded ad slot.
      googletag.pubads().addEventListener("rewardedSlotClosed", (event) => {
        const slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "has been closed.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)

*** ** * ** ***

## googletag.events.RewardedSlotGrantedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a reward is granted for viewing a [rewarded ad](https://support.google.com/admanager/answer/9116812). If the ad is closed before the criteria for granting a reward is met, this event will not fire.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotGrantedEvent.payload` | An object containing information about the reward that was granted. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotGranted", (event) => {
        const slot = event.slot;
        console.group("Reward granted for slot", slot.getSlotElementId(), ".");

        // Log details of the reward.
        console.log("Reward type:", event.payload?.type);
        console.log("Reward amount:", event.payload?.amount);
        console.groupEnd();

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotGranted", function (event) {
        var _a, _b;
        var slot = event.slot;
        console.group("Reward granted for slot", slot.getSlotElementId(), ".");

        // Log details of the reward.
        console.log("Reward type:", (_a = event.payload) === null || _a === void 0 ? void 0 : _a.type);
        console.log(
          "Reward amount:",
          (_b = event.payload) === null || _b === void 0 ? void 0 : _b.amount,
        );
        console.groupEnd();

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotGranted", (event) => {
        const slot = event.slot;
        console.group("Reward granted for slot", slot.getSlotElementId(), ".");

        // Log details of the reward.
        console.log("Reward type:", event.payload?.type);
        console.log("Reward amount:", event.payload?.amount);
        console.groupEnd();

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)

### Properties

*** ** * ** ***

#### payload

`payload: https://developers.google.com/publisher-tag/reference#googletag.RewardedPayload`An object containing information about the reward that was granted.

*** ** * ** ***

## googletag.events.RewardedSlotReadyEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a [rewarded ad](https://support.google.com/admanager/answer/9116812) is ready to be displayed. The publisher is responsible for presenting the user an option to view the ad before displaying it.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.RewardedSlotReadyEvent.makeRewardedVisible` | Displays the rewarded ad. |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when a rewarded ad slot becomes ready to be
    // displayed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotReady", (event) => {
        const slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "is ready to be displayed.");

        // Replace with custom logic.
        const userHasConsented = true;
        if (userHasConsented) {
          event.makeRewardedVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when a rewarded ad slot becomes ready to be
    // displayed.
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotReady", function (event) {
        var slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "is ready to be displayed.");

        // Replace with custom logic.
        var userHasConsented = true;
        if (userHasConsented) {
          event.makeRewardedVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    // This listener is called when a rewarded ad slot becomes ready to be
    // displayed.
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called whenever a reward is granted for a
      // rewarded ad.
      googletag.pubads().addEventListener("rewardedSlotReady", (event) => {
        const slot = event.slot;
        console.log("Rewarded ad slot", slot.getSlotElementId(), "is ready to be displayed.");

        // Replace with custom logic.
        const userHasConsented = true;
        if (userHasConsented) {
          event.makeRewardedVisible();
        }

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)

### Methods

*** ** * ** ***

#### makeRewardedVisible

`makeRewardedVisible(): boolean`Displays the rewarded ad. This method should not be called until the user has consented to view the ad.

| Returns ||
|---|---|
| `boolean` | Whether the rewarded ad was successfully displayed. |

*** ** * ** ***

## googletag.events.RewardedSlotVideoCompletedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when a rewarded video ad has finished playing.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the video in a rewarded ad slot has
      // finished playing.
      googletag.pubads().addEventListener("rewardedSlotVideoCompleted", (event) => {
        const slot = event.slot;
        console.log("Video in rewarded ad slot", slot.getSlotElementId(), "has finished playing.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### JavaScript (legacy)

    ```javascript
    var targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the video in a rewarded ad slot has
      // finished playing.
      googletag.pubads().addEventListener("rewardedSlotVideoCompleted", function (event) {
        var slot = event.slot;
        console.log("Video in rewarded ad slot", slot.getSlotElementId(), "has finished playing.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

    ### TypeScript

    ```typescript
    const targetSlot = googletag.defineOutOfPageSlot(
      "/1234567/example",
      googletag.enums.OutOfPageFormat.REWARDED,
    );

    // Slot returns null if the page or device does not support rewarded ads.
    if (targetSlot) {
      targetSlot.addService(googletag.pubads());

      // This listener is called when the video in a rewarded ad slot has
      // finished playing.
      googletag.pubads().addEventListener("rewardedSlotVideoCompleted", (event) => {
        const slot = event.slot;
        console.log("Video in rewarded ad slot", slot.getSlotElementId(), "has finished playing.");

        if (slot === targetSlot) {
          // Slot specific logic.
        }
      });
    }
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)
    - [Display a rewarded ad](https://developers.google.com/publisher-tag/samples/display-rewarded-ad)

*** ** * ** ***

## googletag.events.SlotOnloadEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when the creative's iframe fires its load event. When rendering rich media ads in sync rendering mode, no iframe is used so no `SlotOnloadEvent` will be fired.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when a creative iframe load event fires.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", (event) => {
      const slot = event.slot;
      console.log("Creative iframe for slot", slot.getSlotElementId(), "has loaded.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when a creative iframe load event fires.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", function (event) {
      var slot = event.slot;
      console.log("Creative iframe for slot", slot.getSlotElementId(), "has loaded.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called when a creative iframe load event fires.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotOnload", (event) => {
      const slot = event.slot;
      console.log("Creative iframe for slot", slot.getSlotElementId(), "has loaded.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

*** ** * ** ***

## googletag.events.SlotRenderEndedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when the creative code is injected into a slot. This event will occur before the creative's resources are fetched, so the creative may not be visible yet. If you need to know when all creative resources for a slot have finished loading, consider the [events.SlotOnloadEvent](https://developers.google.com/publisher-tag/reference#googletag.events.SlotOnloadEvent) instead.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.advertiserId` | Advertiser ID of the rendered ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.campaignId` | Campaign ID of the rendered ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.companyIds` | IDs of the companies that bid on the rendered backfill ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.creativeId` | Creative ID of the rendered reservation ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.creativeTemplateId` | Creative template ID of the rendered reservation ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.isBackfill` | Whether an ad was a backfill ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.isEmpty` | Whether an ad was returned for the slot. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.labelIds` | **Deprecated.** |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.lineItemId` | Line item ID of the rendered reservation ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.responseIdentifier` | The response identifier is a unique identifier for the ad response. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.size` | Indicates the pixel size of the rendered creative. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.slotContentChanged` | Whether the slot content was changed with the rendered ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.sourceAgnosticCreativeId` | Creative ID of the rendered reservation or backfill ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.sourceAgnosticLineItemId` | Line item ID of the rendered reservation or backfill ad. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotRenderEndedEvent.yieldGroupIds` | IDs of the yield groups for the rendered backfill ad. |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when a slot has finished rendering.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRenderEnded", (event) => {
      const slot = event.slot;
      console.group("Slot", slot.getSlotElementId(), "finished rendering.");

      // Log details of the rendered ad.
      console.log("Advertiser ID:", event.advertiserId);
      console.log("Campaign ID:", event.campaignId);
      console.log("Company IDs:", event.companyIds);
      console.log("Creative ID:", event.creativeId);
      console.log("Creative Template ID:", event.creativeTemplateId);
      console.log("Is backfill?:", event.isBackfill);
      console.log("Is empty?:", event.isEmpty);
      console.log("Line Item ID:", event.lineItemId);
      console.log("Size:", event.size);
      console.log("Slot content changed?", event.slotContentChanged);
      console.log("Source Agnostic Creative ID:", event.sourceAgnosticCreativeId);
      console.log("Source Agnostic Line Item ID:", event.sourceAgnosticLineItemId);
      console.log("Yield Group IDs:", event.yieldGroupIds);
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when a slot has finished rendering.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRenderEnded", function (event) {
      var slot = event.slot;
      console.group("Slot", slot.getSlotElementId(), "finished rendering.");

      // Log details of the rendered ad.
      console.log("Advertiser ID:", event.advertiserId);
      console.log("Campaign ID:", event.campaignId);
      console.log("Company IDs:", event.companyIds);
      console.log("Creative ID:", event.creativeId);
      console.log("Creative Template ID:", event.creativeTemplateId);
      console.log("Is backfill?:", event.isBackfill);
      console.log("Is empty?:", event.isEmpty);
      console.log("Line Item ID:", event.lineItemId);
      console.log("Size:", event.size);
      console.log("Slot content changed?", event.slotContentChanged);
      console.log("Source Agnostic Creative ID:", event.sourceAgnosticCreativeId);
      console.log("Source Agnostic Line Item ID:", event.sourceAgnosticLineItemId);
      console.log("Yield Group IDs:", event.yieldGroupIds);
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called when a slot has finished rendering.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRenderEnded", (event) => {
      const slot = event.slot;
      console.group("Slot", slot.getSlotElementId(), "finished rendering.");

      // Log details of the rendered ad.
      console.log("Advertiser ID:", event.advertiserId);
      console.log("Campaign ID:", event.campaignId);
      console.log("Company IDs:", event.companyIds);
      console.log("Creative ID:", event.creativeId);
      console.log("Creative Template ID:", event.creativeTemplateId);
      console.log("Is backfill?:", event.isBackfill);
      console.log("Is empty?:", event.isEmpty);
      console.log("Line Item ID:", event.lineItemId);
      console.log("Size:", event.size);
      console.log("Slot content changed?", event.slotContentChanged);
      console.log("Source Agnostic Creative ID:", event.sourceAgnosticCreativeId);
      console.log("Source Agnostic Line Item ID:", event.sourceAgnosticLineItemId);
      console.log("Yield Group IDs:", event.yieldGroupIds);
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

### Properties

*** ** * ** ***

#### advertiserId

`advertiserId: number`Advertiser ID of the rendered ad. Value is `null` for empty slots, backfill ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### campaignId

`campaignId: number`Campaign ID of the rendered ad. Value is `null` for empty slots, backfill ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### companyIds

`companyIds: number[]`IDs of the companies that bid on the rendered backfill ad. Value is `null` for empty slots, reservation ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### creativeId

`creativeId: number`Creative ID of the rendered reservation ad. Value is `null` for empty slots, backfill ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### creativeTemplateId

`creativeTemplateId: number`Creative template ID of the rendered reservation ad. Value is `null` for empty slots, backfill ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### isBackfill

`isBackfill: boolean`Whether an ad was a backfill ad. Value is `true` if the ad was a backfill ad, `false` otherwise.

*** ** * ** ***

#### isEmpty

`isEmpty: boolean`Whether an ad was returned for the slot. Value is `true` if no ad was returned, `false` otherwise.

*** ** * ** ***

#### labelIds

`labelIds: number[]`

> [!WARNING]
> **Deprecated:** This field is no longer populated.

*** ** * ** ***

#### lineItemId

`lineItemId: number`Line item ID of the rendered reservation ad. Value is `null` for empty slots, backfill ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### responseIdentifier

`responseIdentifier: string`The response identifier is a unique identifier for the ad response. This value can be used to identify and block the ad in the [Ad Review Center (ARC)](https://support.google.com/admanager/answer/146769).

*** ** * ** ***

#### size

`size: string | number[]`Indicates the pixel size of the rendered creative. Example: `[728, 90]`. Value is `null` for empty ad slots.

*** ** * ** ***

#### slotContentChanged

`slotContentChanged: boolean`Whether the slot content was changed with the rendered ad. Value is `true` if the content was changed, `false` otherwise.

*** ** * ** ***

#### sourceAgnosticCreativeId

`sourceAgnosticCreativeId: number`Creative ID of the rendered reservation or backfill ad. Value is `null` if the ad is not a reservation or line item backfill, or the creative is rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### sourceAgnosticLineItemId

`sourceAgnosticLineItemId: number`Line item ID of the rendered reservation or backfill ad. Value is `null` if the ad is not a reservation or line item backfill, or the creative is rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

#### yieldGroupIds

`yieldGroupIds: number[]`IDs of the yield groups for the rendered backfill ad. Value is `null` for empty slots, reservation ads, and creatives rendered by services other than [PubAdsService](https://developers.google.com/publisher-tag/reference#googletag.PubAdsService).

*** ** * ** ***

## googletag.events.SlotRequestedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when an ad has been requested for a particular slot.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when the specified service issues an ad
    // request for a slot. Each slot will fire this event, even though they
    // may be batched together in a single request if single request
    // architecture (SRA) is enabled.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRequested", (event) => {
      const slot = event.slot;
      console.log("Slot", slot.getSlotElementId(), "has been requested.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when the specified service issues an ad
    // request for a slot. Each slot will fire this event, even though they
    // may be batched together in a single request if single request
    // architecture (SRA) is enabled.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRequested", function (event) {
      var slot = event.slot;
      console.log("Slot", slot.getSlotElementId(), "has been requested.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called when the specified service issues an ad
    // request for a slot. Each slot will fire this event, even though they
    // may be batched together in a single request if single request
    // architecture (SRA) is enabled.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotRequested", (event) => {
      const slot = event.slot;
      console.log("Slot", slot.getSlotElementId(), "has been requested.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

*** ** * ** ***

## googletag.events.SlotResponseReceived

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired when an ad response has been received for a particular slot.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called when an ad response has been received
    // for a slot.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotResponseReceived", (event) => {
      const slot = event.slot;
      console.log("Ad response for slot", slot.getSlotElementId(), "received.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called when an ad response has been received
    // for a slot.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotResponseReceived", function (event) {
      var slot = event.slot;
      console.log("Ad response for slot", slot.getSlotElementId(), "received.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called when an ad response has been received
    // for a slot.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotResponseReceived", (event) => {
      const slot = event.slot;
      console.log("Ad response for slot", slot.getSlotElementId(), "received.");

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

*** ** * ** ***

## googletag.events.SlotVisibilityChangedEvent

Extends `https://developers.google.com/publisher-tag/reference#googletag.events.Event`This event is fired whenever the on-screen percentage of an ad slot's area changes. The event is throttled and will not fire more often than once every 200ms.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.events.SlotVisibilityChangedEvent.inViewPercentage` | The percentage of the ad's area that is visible. |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` | Name of the service that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.serviceName` property |
| `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` | The slot that triggered the event. ###### Inherited from the `https://developers.google.com/publisher-tag/reference#googletag.events.Event.slot` property |

Example
:

    ### JavaScript

    ```javascript
    // This listener is called whenever the on-screen percentage of an
    // ad slot's area changes.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotVisibilityChanged", (event) => {
      const slot = event.slot;
      console.group("Visibility of slot", slot.getSlotElementId(), "changed.");

      // Log details of the event.
      console.log("Visible area:", `${event.inViewPercentage}%`);
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // This listener is called whenever the on-screen percentage of an
    // ad slot's area changes.
    var targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotVisibilityChanged", function (event) {
      var slot = event.slot;
      console.group("Visibility of slot", slot.getSlotElementId(), "changed.");

      // Log details of the event.
      console.log("Visible area:", "".concat(event.inViewPercentage, "%"));
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

    ### TypeScript

    ```typescript
    // This listener is called whenever the on-screen percentage of an
    // ad slot's area changes.
    const targetSlot = googletag.defineSlot("/1234567/example", [160, 600]);
    googletag.pubads().addEventListener("slotVisibilityChanged", (event) => {
      const slot = event.slot;
      console.group("Visibility of slot", slot.getSlotElementId(), "changed.");

      // Log details of the event.
      console.log("Visible area:", `${event.inViewPercentage}%`);
      console.groupEnd();

      if (slot === targetSlot) {
        // Slot specific logic.
      }
    });
    ```

See also
:
    - [Ad event listeners](https://developers.google.com/publisher-tag/samples/ad-event-listeners)

### Properties

*** ** * ** ***

#### inViewPercentage

`inViewPercentage: number`The percentage of the ad's area that is visible. Value is a number between 0 and 100.

*** ** * ** ***

## googletag.secureSignals

This is the namespace that GPT uses for managing secure signals.

| Interfaces ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.BidderSignalProvider` | Returns a secure signal for a specific bidder. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.PublisherSignalProvider` | Returns a secure signal for a specific publisher. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvidersArray` | An interface for managing secure signals. |

| Type Aliases ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider` | Interface for returning a secure signal for a specific bidder or provider. |

### Type Aliases

*** ** * ** ***

#### SecureSignalProvider

`SecureSignalProvider: https://developers.google.com/publisher-tag/reference#googletag.secureSignals.BidderSignalProvider | https://developers.google.com/publisher-tag/reference#googletag.secureSignals.PublisherSignalProvider`Interface for returning a secure signal for a specific bidder or provider. One of `id` or `networkCode` must be provided, but not both.

*** ** * ** ***

## googletag.secureSignals.BidderSignalProvider

Returns a secure signal for a specific bidder.  

A bidder secure signal provider consists of 2 parts:  

1. A collector function, which returns a `Promise` that resolves to a secure signal.
2. An `id` which identifies the bidder associated with the signal.

To return a secure signal for a publisher, use [secureSignals.PublisherSignalProvider](https://developers.google.com/publisher-tag/reference#googletag.secureSignals.PublisherSignalProvider) instead.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.BidderSignalProvider.collectorFunction` | A function which returns a `Promise` that resolves to a secure signal. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.BidderSignalProvider.id` | A unique identifier for the collector associated with this secure signal, as registered in Google Ad Manager. |

Example
:

    ### JavaScript

    ```javascript
    // id is provided
    googletag.secureSignalProviders.push({
      id: "collector123",
      collectorFunction: () => {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // id is provided
    googletag.secureSignalProviders.push({
      id: "collector123",
      collectorFunction: function () {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

    ### TypeScript

    ```typescript
    // id is provided
    googletag.secureSignalProviders!.push({
      id: "collector123",
      collectorFunction: () => {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

See also
:
    - [Share secure signals with bidders](https://support.google.com/admanager/answer/10488752)

### Properties

*** ** * ** ***

#### collectorFunction

`collectorFunction: (() => Promise<string>)`A function which returns a `Promise` that resolves to a secure signal.

*** ** * ** ***

#### id

`id: string`A unique identifier for the collector associated with this secure signal, as registered in Google Ad Manager.

*** ** * ** ***

## googletag.secureSignals.PublisherSignalProvider

Returns a secure signal for a specific publisher.  

A publisher signal provider consists of 2 parts:  

1. A collector function, which returns a `Promise` that resolves to a secure signal.
2. A `networkCode` which identifies the publisher associated with the signal.

To return a secure signal for a bidder, use [secureSignals.BidderSignalProvider](https://developers.google.com/publisher-tag/reference#googletag.secureSignals.BidderSignalProvider) instead.

| Properties ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.PublisherSignalProvider.collectorFunction` | A function which returns a `Promise` that resolves to a secure signal. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.PublisherSignalProvider.networkCode` | The network code (as seen in the ad unit path) for the publisher associated with this secure signal. |

Example
:

    ### JavaScript

    ```javascript
    // networkCode is provided
    googletag.secureSignalProviders.push({
      networkCode: "123456",
      collectorFunction: () => {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

    ### JavaScript (legacy)

    ```javascript
    // networkCode is provided
    googletag.secureSignalProviders.push({
      networkCode: "123456",
      collectorFunction: function () {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

    ### TypeScript

    ```typescript
    // networkCode is provided
    googletag.secureSignalProviders!.push({
      networkCode: "123456",
      collectorFunction: () => {
        // ...custom signal generation logic...
        return Promise.resolve("signal");
      },
    });
    ```

See also
:
    - [Share secure signals with bidders](https://support.google.com/admanager/answer/10488752)

### Properties

*** ** * ** ***

#### collectorFunction

`collectorFunction: (() => Promise<string>)`A function which returns a `Promise` that resolves to a secure signal.

*** ** * ** ***

#### networkCode

`networkCode: string`The network code (as seen in the ad unit path) for the publisher associated with this secure signal.

*** ** * ** ***

## googletag.secureSignals.SecureSignalProvidersArray

An interface for managing secure signals.

| Methods ||
|---|---|
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvidersArray.clearAllCache` | Clears all signals for all collectors from cache. |
| `https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvidersArray.push` | Adds a new [secureSignals.SecureSignalProvider](https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider) to the signal provider array and begins the signal generation process. |

### Methods

*** ** * ** ***

#### clearAllCache

`clearAllCache(): void`Clears all signals for all collectors from cache.  

Calling this method may reduce the likelihood of signals being included in ad requests for the current and potentially later page views. Due to this, it should only be called when meaningful state changes occur, such as events that indicate a new user (log in, log out, sign up, etc.).

*** ** * ** ***

#### push

`push(provider: https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider): void`Adds a new [secureSignals.SecureSignalProvider](https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider) to the signal provider array and begins the signal generation process.

| Parameters ||
|---|---|
| `provider: https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider` | The [secureSignals.SecureSignalProvider](https://developers.google.com/publisher-tag/reference#googletag.secureSignals.SecureSignalProvider) object to be added to the array. |