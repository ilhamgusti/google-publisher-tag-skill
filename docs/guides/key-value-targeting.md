Key-values can be used to target ads more granularly than ad units. Learn more
about [key-values](https://support.google.com/admanager/answer/188092).

> [!WARNING]
> **Warning:** Use key-value targeting with care. Under the terms of your contract, you must not pass any data that Google Ad Manager could [use or recognize as
> personally identifiable information](https://support.google.com/admanager/answer/7686480).

For each ad request, you may pass one or more keys, each with one or more
associated values. These key-values will be evaluated against targeting options
configured at the line item-level in Ad Manager. For example, if
you pass a custom key-value of `age=18-34`, line items targeted to the age range
18-34 will be eligible to serve, assuming all other criteria matches.

## Set targeting

You may specify key-values to configure targeting at both the slot- and
page-level based on your network's needs.

Slot-level

:   Allows you to set key-values for individual ad slots on your page.

    Slot-level targeting allows you to configure targeting on a per-slot basis.
    This is useful in cases where individual slots on the same page require
    different targeting, but can be inefficient in situations where the same
    key-values are applied to all slots. Use
    [`slot.setConfig({ targeting: ... })`](https://developers.google.com/publisher-tag/reference#googletag.config.SlotSettingsConfig.targeting) to utilize
    slot-level targeting, as in the following example.

Page-level

:   Allows you to set key-values across all ad slots on your page.

    Page-level targeting ensures that all ad slots have the same set of
    key-values. In some cases this may reduce the total amount of code needed to
    configure targeting. Use
    [`googletag.setConfig({ targeting: ... })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.targeting) to
    utilize page-level targeting, as in the following example.

```javascript
window.googletag = window.googletag || { cmd: [] };

// GPT slots
let adSlots = [];

googletag.cmd.push(() => {
  // Configure slot-level targeting.
  adSlots[0] = googletag
    .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad-1")
    .addService(googletag.pubads());
  adSlots[0].setConfig({
    targeting: {
      color: "red",
      position: "atf",
    },
  });

  adSlots[1] = googletag
    .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad-2")
    .addService(googletag.pubads());
  adSlots[1].setConfig({
    targeting: {
      position: "btf",
    },
  });

  // Configure page-level targeting and enable SRA.
  googletag.setConfig({
    targeting: {
      interests: "basketball",
    },
    singleRequest: true,
  });

  // Enable services.
  googletag.enableServices();
});
```

In this example, two ad slots are defined which specify ad unit
`/6355419/Travel/Asia` and ad size `728x90`. Then key-value targeting is
applied to further restrict and differentiate the ads which may serve in each
slot.

When both slot- and page-level targeting are used, the key-values are combined
and only ads satisfying all criteria will be eligible to serve to a given slot.
In this example, the effective tageting for each slot is:

| Ad slot | Effective targeting |
|---|---|
| 1 | `color=red AND position=atf AND interests=basketball` |
| 2 | `position=btf AND interests=basketball` |

> [!NOTE]
> **Note:** If the same targeting key is defined at both the page- and slot-level, the slot-level value will take precedence for that slot.

### Target multiple keys or values

In the preceding example, a combination of slot- and page-level targeting was
used to define multiple targeting keys for a single ad slot. Here are some
alternative approaches to achieve the same effective targeting:

### Slot-level targeting only

In this example, shared key-values are repeated for each ad slot.

    // Slot-level targeting with multiple keys.
    adSlots[0] = googletag
        .defineSlot('/6355419/Travel/Asia', [728, 90], 'banner-ad-1')
        .addService(googletag.pubads());
    adSlots[0].setConfig({
      targeting: {
        color: 'red',
        position: 'atf',
        interests: 'basketball'
      }
    });
    adSlots[1] = googletag
        .defineSlot('/6355419/Travel/Asia', [728, 90], 'banner-ad-2')
        .addService(googletag.pubads());
    adSlots[1].setConfig({
      targeting: {
        position: 'btf',
        interests: 'basketball'
      }
    });

### Page-level default targeting

In this example, default targeting is set at the page-level and overridden
at the slot-level as necessary.

> [!CAUTION]
> **Caution:** Key-values set at the page-level cannot be cleared at the slot-level, only modified.

    // Page-level default targeting.
    googletag.setConfig({
      targeting: {
        interests: 'basketball',
        position: 'btf'
      }
    });

    // Slot-level targeting overrides.
    adSlots[0] = googletag
        .defineSlot('/6355419/Travel/Asia', [728, 90], 'banner-ad-1')
        .addService(googletag.pubads());
    adSlots[0].setConfig({
      targeting: {
        color: 'red',
        position: 'atf'
      }
    });
    adSlots[1] = googletag
        .defineSlot('/6355419/Travel/Asia', [728, 90], 'banner-ad-2')
        .addService(googletag.pubads());

It's also possible to target multiple values for a single key by providing an
array of values when calling `setConfig()`:

    // Page-level targeting with multiple values for a single key.
    googletag.setConfig({ targeting: { interests: ['baseball', 'basketball'] } });

## Clear targeting

Once targeting has been set, the configured key-values will be sent with every
ad request for the life of the ad slot. In some circumstances, however, it may
be desirable for targeting to change over time. While `setConfig()` can be
used to add and overwrite key-values, it's not possible to remove them this way.
To accomplish that, you must clear the targeting by setting the value to `null`
in the `setConfig()` method.

```javascript
// Step 0, define slot- and page-level targeting.
adSlots[0] = googletag
  .defineSlot("/6355419/Travel/Asia", [728, 90], "banner-ad-1")
  .addService(googletag.pubads());
adSlots[0].setConfig({
  targeting: {
    color: "red",
    position: "atf",
  },
});

googletag.setConfig({
  targeting: {
    interests: "basketball",
  },
  singleRequest: true,
});

// Step 1, clear slot-level color targeting.
adSlots[0].setConfig({
  targeting: {
    color: null,
  },
});

// Step 2, clear all page-level targeting.
googletag.setConfig({
  targeting: null,
});
```

When `clearTargeting()` is called with a specific key (either at the
slot- or page- level), only that key is removed. When no key is specified, all
targeting at that level is removed.

In the preceding example, the effective targeting for the ad slot after each
step is:

| Step | Effective targeting |
|---|---|
| 0 | `color=red AND position=atf AND interests=basketball` |
| 1 | `position=atf AND interests=basketball` |
| 2 | `position=atf` |