# Ad sizes

Every ad slot you define must specify the ad size(s) eligible to serve in that
slot. The way ad sizes are specified varies depending on the type of ads to be
displayed, as well as the size and flexibility of the ad slots themselves.

In some cases, ad size might be overridden at the line item level within
Google Ad Manager. Visit the [help center](https://support.google.com/admanager/answer/3187916) to learn
more.

Full code for the examples included in this guide can be found on the [ad
sizes](https://developers.google.com/publisher-tag/samples/ad-sizes) sample page.

## Fixed-size ads

You can define an ad slot with a single fixed size.

    googletag
      .defineSlot("/6355419/Travel/Europe/France/Paris", [300, 250], "fixed-size-ad")
      .addService(googletag.pubads());

In this example, only creatives with size `300x250` will be served.

Key point: When working with fixed-size ads, we strongly recommend that you
define the size of the `<div>` element where the creative will render. Since
creatives are often rendered asynchronously, they might cause other elements on
the page to shift if insufficient space is reserved for them.

## Multi-size ads

If an ad supports multiple sizes, provide a list of supported sizes when
defining the ad slot.

    googletag
      .defineSlot(
        "/6355419/Travel/Europe",
        [[300, 250], [728, 90], [750, 200], "fluid"],
        "multi-size-ad",
      )
      .addService(googletag.pubads());

In this example, creatives with sizes `300x250`, `728x90`, and `750x200` can be
served. Ad Manager only considers creatives matching these sizes
during the [ad selection process](https://support.google.com/admanager/answer/1143651).

If dimensions are not specified for the ad slot `<div>` in CSS,
GPT automatically sets the dimensions equal to the shortest
declared height and widest declared width over 1px when `display()` is called.
In this case, that would be `750x90`. However, this sizing might occur after
other content on the page has loaded, causing that content to shift. To avoid
layout shifts, reserve space using CSS as shown in the
[minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift) guide.

When working with multi-size ads, ensure that your layout is flexible enough to
support an ad with the largest size specified. This will avoid creatives being
inadvertently cropped.

## Fluid ads

Fluid ads have no fixed size, but rather adapt to fit the creative content they
display. [Native ads](https://support.google.com/admanager/answer/6366845) are currently the only fluid ad
type supported by Ad Manager.

When working with fluid ads, a custom `fluid` size might be specified.

    googletag
      .defineSlot("/6355419/Travel", ["fluid"], "native-ad")
      .addService(googletag.pubads());

In this example, the ad slot will have the width of its parent container and
resize its height to fit the creative content. The steps GPT
takes to resize the ad slot are as follows:

1. Ad response is received.
2. Creative content is written into an iframe, with initial height set to `0px` and width set to `100%`.
3. Once all resources in the iframe have finished loading, the creative is made visible by setting the height of the iframe equal to the height of the iframe's `<body>` element.

> [!CAUTION]
> Due to the flexible nature of fluid ads, there are a number of caveats to be aware of, including:
>
> - Fluid ads will generally take longer to become visible than ads with a fixed size.
> - Fluid ads might trigger a reflow of page content when they are resized, which can [negatively affect
>   performance](https://developers.google.com/speed/docs/insights/browser-reflow).
> - Fluid ads might render incorrectly if an ancestor element of the creative iframe has a fixed height less than that of the fluid creative content.

## Responsive ads

Responsive ads extend multi-size ads and allow you to specify the size of the
creatives to serve based on the size of the viewport of the browser making the
request. This functionality can be used to control the size of creatives served
to different types of devices (desktop, tablet, mobile, etc.).

This is accomplished by defining a mapping between viewport size and ad size,
then associating that mapping with an ad slot.

```javascript
const responsiveAdSlot = googletag
  .defineSlot(
    "/6355419/Travel/Europe",
    [
      [300, 250],
      [728, 90],
      [750, 200],
    ],
    "responsive-ad",
  )
  .addService(googletag.pubads());

const mapping = googletag
  .sizeMapping()
  .addSize(
    [1024, 768],
    [
      [750, 200],
      [728, 90],
    ],
  )
  .addSize([640, 480], [300, 250])
  .addSize([0, 0], [])
  .build();

responsiveAdSlot.defineSizeMapping(mapping);
```

In this example, the mapping specifies:

- When viewport \>= `1024x768`, ads sized `750x200` or `728x90` can serve.
- When `1024x768` \> viewport \>= `640x480`, ads sized `300x250` can serve.
- When viewport \< `640x480`, no ads can serve.

GPT will detect the size of the viewport of the browser making
the request and use the largest mapping that fits. To determine the largest
mapping GPT first considers width, then height (i.e., `[100,
10]` \> `[10, 100]`). In the event of an error in the mapping or if the viewport
size can't be determined, the sizes specified in `defineSlot()` will be used.

The mapping is then associated with an ad slot by calling the
[Slot.defineSizeMapping()](https://developers.google.com/publisher-tag/reference#googletag.Slot_defineSizeMapping) method. This method
accepts an array of mappings in the following format:

```javascript
[
  [
    [viewport-width-1, viewport-height-1],
    [[ad-width-1, ad-height-1], [ad-width-2, ad-height-2], ...]
  ],
  [
    [viewport-width-2, viewport-height-2],
    [[ad-width-3, ad-height-3], [ad-width-4, ad-height-4], ...]
  ],
  ...
]
```

The order of viewport sizes within this array defines their priority. The
[`SizeMappingBuilder`](https://developers.google.com/publisher-tag/reference#googletagsizemappingbuilder) used in the
[example above](https://developers.google.com/publisher-tag/guides/ad-sizes#responsive-example) is a convenient way to generate an array of
this format, with sizes automatically ordered from largest to smallest. In that
example, the output of
[`SizeMappingBuilder.build()`](https://developers.google.com/publisher-tag/reference#googletag.SizeMappingBuilder_build) is:

    [
      [[1024, 768], [[750, 200], [728, 90]]],
      [[640, 480], [[300, 250]]],
      [[0, 0], []]
    ]