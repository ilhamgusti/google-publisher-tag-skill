# Minimize layout shift

A layout shift occurs when a visible element on your page changes position or
size, affecting the position of content around it. Sometimes the shift is
intended, such as when a container expands as a result of a user action.
However, the dynamic nature of ads can lead to *unexpected layout shifts*, which
have a negative effect on the user experience and can cause serious usability
problems.

This guide explains how to measure and minimize layout shift when working with
Google Publisher Tags (GPT).

## How ads cause layout shift

Ads are usually requested asynchronously and dynamically add content to your
page during or after page load. While ads are being fetched, the rest of the
page continues to load and non-ad content may become visible to the user. If you
don't reserve sufficient space for the ads being loaded, they can end up
displacing visible non-ad content when they are eventually added to the page.

When working with Google Publisher Tags, there are a few points in the ad lifecycle
where layout shift can occur:

1. When `display()` is called. A slot may expand or collapse, depending on how it was configured.
2. When ad content is rendered. A slot may be resized if served a fluid ad or if insufficient space is otherwise available. A slot may also expand or collapse at this point, depending on how it was configured.
3. After ad content is rendered. Certain creative types are designed to expand after they appear on the page.

Keep in mind that the higher an ad slot is within the viewport, the more content
it has the potential to displace. Take special care with slots near the top of
the initial viewport (above the fold). These slots can cause a disproportionate
amount of layout shift because they are more likely to be visible when their ad
content is loaded.

## Measuring layout shift

[Cumulative Layout Shift (CLS)](https://web.dev/articles/cls/) is a [Core Web Vitals](https://web.dev/articles/vitals/) metric that
you can use to quantify the impact of layout shifts on your site, both in the
lab and in the field.

> [!IMPORTANT]
> **Important:** The [standards for Core Web Vitals](https://web.dev/articles/defining-core-web-vitals-thresholds) recommend that your site's 75th percentile CLS is less than 0.1 to be considered "good". This standard covers all layout shifts on your site, not only those caused by ads.

### In the lab

[Lab tools](https://web.dev/articles/cls/#lab-tools) measure CLS synthetically. This means that they don't
rely on real user interaction, making them well suited for use in continuous
integration and local development workflows. However, these tools usually only
measure performance during page load and are limited in the conditions they can
simulate, so reported values may be lower than what a real user would
experience.

[Publisher Ads Audits for Lighthouse](https://developers.google.com/publisher-ads-audits) is a tool that can be used to
measure CLS specifically attributable to GPT ads. For details,
see the [reduce ad-related layout shift](https://developers.google.com/publisher-ads-audits/reference/audits/cumulative-ad-shift) audit
documentation.

Chrome DevTools can also be configured to
[highlight layout shifts](https://developer.chrome.com/blog/new-in-devtools-77/#layoutshifts) as you navigate your site. This
can be used to manually identify layout shifts that occur near ad slots on your
page.

### In the field

[Field tools](https://web.dev/articles/cls/#field-tools) measure CLS experienced by real users as they
interact with your site. This process is commonly known as real user monitoring
(RUM). RUM allows you to observe how CLS is affected by real-world factors---such
as device capabilities, network conditions, user interaction, and page
personalization---which are often difficult or impossible to simulate with
synthetic tests.

> [!NOTE]
> **Note:** You can also use the [Layout Instability API](https://github.com/WICG/layout-instability) to [manually measure CLS](https://web.dev/articles/cls/#measure-cls-in-javascript) in the field.

## Minimizing layout shift

The only guaranteed way to avoid layout shift is to reserve a sufficient amount
of space for a given ad slot using CSS. Setting a fixed height and width
directly on the ad slot `div` is the most effective way to do this. However,
while this works well for static, fixed-size ad slots, more complicated
scenarios may require a more nuanced approach. Some common scenarios are
explained in the following sections.

### Multi-size ad slots

For ad slots that accept multiple sizes, we recommend one of the following
approaches:

- Reserve space for the largest size configured to serve.
- Reserve space for the smallest size configured to serve.
- Reserve space for the size most likely to serve, determined by examining historical fill data from Google Ad Manager reporting.

> [!CAUTION]
> **Caution:** Be aware of [ad slot expansion](https://support.google.com/admanager/answer/9117822) and [contraction settings](https://support.google.com/admanager/answer/9433610), which can affect the range of sizes eligible to serve to your ad slots.

#### Choosing the right approach

Reserving space for the largest size configured to serve is the most effective
way to eliminate layout shifts. However, this method can result in extra blank
space around the ad, in the event a creative smaller than the reserved size is
served. Shrinking the ad slot to match the size of the served creative would
incur an additional layout shift, so it's recommended to avoid doing this.
Instead, [vertical and horizontal centering](https://www.w3schools.com/css/css_align.asp) can be used to reduce
the visual impact of excess blank space.

On the other hand, reserving space for the smallest size configured to serve
avoids excess blank space around your ad. This can be a good option if your ad
slot is commonly filled with smaller creatives, or in cases where all of the
sizes the slot supports are similar. However, this method results in a layout
shift in the event a creative larger than the reserved size is served (although
such shifts are generally smaller when compared to not reserving space at all).

To strike a balance between blank space and layout shifts, you can reserve an
"average" amount of space for your ad slots. For example, reserving `100px`
vertically incurs a little blank space when a `320x50` creative is served, but
reduces the CLS score compared to reserving no space at all. You'll need to
experiment with different sizes to find the best balance for your own site.

When determining how much space to reserve for a given slot, examining
historical fill data from Google Ad Manager reporting can help you make a more
informed decision. This can be best illustrated by exploring some examples.

> [!NOTE]
> **Note:** The examples shown here only illustrate part of the process of determining how much space to reserve. After making changes, be sure to review field data and continue to make adjustments until your site's 75th percentile CLS meets the 0.1 benchmark.

##### Example #1

| Creative size (delivered) | Ad Server Impressions (%) |
|---|---|
| `300x250` | 70% |
| `320x50` | 30% |

In this case, reserving `250px` vertically can greatly reduce CLS since the
majority of served creatives are `300x250`.

##### Example #2

| Creative size (delivered) | Ad Server Impressions (%) |
|---|---|
| `970x90` | 60% |
| `728x90` | 10% |
| `320x50` | 20% |
| `728x250` | 5% |
| `300x250` | 5% |

In this case, a majority of ads are at most `90px` tall, so reserving `90px`
vertically should avoid a layout shift most of the time.

#### How to reserve space

We recommend tackling this issue by specifying the size of your ad slot via
[`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height) and [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width) CSS properties:

    <div id="ad-slot" style="min-width: 300px; min-height: 250px;"></div>

Using min-height and min-width attributes lets you reserve a minimum amount of
space for your ad slot, while still allowing the browser to increase the size of
the container as necessary. This ensures that no content gets cut-off in the
event that a larger creative is served.

You can combine this technique with [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/@media) to specify
different minimums for different screen sizes:

    @media screen and (max-width: 960px) {
      #ad-slot {
        min-height: 100px;
      }
    }

Reserving space with JavaScript should be avoided, since doing so can result in
a layout shift at the time the script loads. Reserving space with CSS avoids
this risk.

### Fluid ad slots

Fluid ad slots do not specify a fixed set of sizes that they support. Instead,
these slots [automatically resize](https://developers.google.com/publisher-tag/guides/ad-sizes#fluid_ads) to fit the creative content
served to them, allowing them to support creatives of indeterminate size. As a
result, it's not possible to reserve space for these slots prior to requesting
ad content, and fluid sized ads always cause layout shifts.

To mitigate the effects of layout shifts when working with fluid ad slots, we
recommend the following:

- Only use the `fluid` size for slots below the fold.
- Fetch fluid slots as early as possible to minimize the chance of a user scrolling them into view before the slot is resized.

### Collapsing and expanding ad slots

The [`collapseDiv` setting](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.collapseDiv) lets you collapse ad slot divs
so that they don't take up space on the page when there is no ad content to
display. However, this feature should be used with caution because it can
introduce unintended layout shifts. As noted in the [preceding section](https://developers.google.com/publisher-tag/guides/minimize-layout-shift#how),
collapsing and expanding ad slots can cause layout shifts at two different
points in the ad lifecycle.

If you need to make use of this feature, you can reduce the impact of layout
shifts by using historical fill data from Ad Manager reporting to
implement the following best practices:

- Slots which are likely to be filled should always start out **expanded**.
- Slots which are unlikely to fill should always start out **collapsed**.

For an example implementation, see the
[Collapse empty ad slots](https://developers.google.com/publisher-tag/samples/collapse-empty-ad-slots) sample.