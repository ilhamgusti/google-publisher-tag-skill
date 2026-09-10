---
type: Best Practice
title: "Monitor Performance"
description: "Techniques and APIs to measure and monitor ad loading performance."
resource: "https://developers.google.com/publisher-tag/guides/monitor-performance"
tags: [gpt, performance, metrics, monitoring]
timestamp: 2026-09-10T00:00:00Z
---

# Monitor performance

Making performance a priority isn't just good for users, it can also be
[good for business](https://wpostats.com/). While the best practices in this collection focus
primarily on optimizing your Google Publisher Tag (GPT) integration, many other
factors contribute to the overall performance of a given page. Whenever you
introduce changes, it's important to evaluate the impact of those changes on all
aspects of your site's performance.

## Measure page performance

In order to understand how a change impacts the performance of your site, you
first need to establish a baseline to compare against. The best way to do this
is to create a [performance budget](https://web.dev/performance-budgets-101/) that defines an ideal
baseline, which your site may or may not currently meet. If you're interested in
maintaining a fixed level of performance, however, you can use your site's
current performance metrics as a baseline.

To start measuring performance, a combination of the following approaches are
recommended:

-

  [Synthetic monitoring](https://en.wikipedia.org/wiki/Synthetic_monitoring)
  :   You can use tools like [Lighthouse](https://developers.google.com/web/tools/lighthouse) and
      [Publisher Ads Audits for Lighthouse](https://developers.google.com/publisher-ads-audits) to measure page
      performance in a lab setting. This type of measurement doesn't require
      end-user interaction, so it's well suited for use in automated tests and can
      be used to validate the performance of changes before releasing them to
      users.
-

  [Real user monitoring (RUM)](https://en.wikipedia.org/wiki/Real_user_monitoring)
  :   You can use tools like [Google Analytics](https://developers.google.com/analytics) and [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
      to gather real-world performance data directly from users. This type of
      measurement is based on end-user interactions, so it's useful for
      identifying last mile performance issues that synthetic tests can't easily
      uncover.

Be sure to take measurements and compare against your baseline regularly. This
will give you a good indication of whether your site's performance is trending
in the right direction over time.

### Choose what to measure

When it comes to performance, there's no single metric that can tell you
everything you need to know about how your site is doing. You'll need to look at
a variety of metrics covering various aspects of page performance to get a full
picture. Some key performance areas and suggested metrics are listed in the
following table:

| Performance area ||
|---|---|
| Perceived load speed | **Measures** How quickly a page is able to load and render all UI elements. *** ** * ** *** **Suggested metrics** [First contentful paint (FCP)](https://web.dev/fcp/) [Largest contentful paint (LCP)](https://web.dev/lcp/) [Time to render first ad](https://developers.google.com/publisher-ads-audits/reference/audits/first-ad-render) |
| Page load responsiveness | **Measures** How quickly a page becomes responsive after the initial load. *** ** * ** *** **Suggested metrics** [First input delay (FID)](https://web.dev/fid/) [Time to Interactive (TTI)](https://web.dev/tti/) [Total blocking time (TBT)](https://web.dev/tbt/) |
| Visual stability | **Measures** How much UI elements shift and whether these shifts interfere with user interaction. See [Minimize layout shift](https://developers.google.com/publisher-tag/guides/minimize-layout-shift) for more information. *** ** * ** *** **Suggested metrics** [Cumulative ad shift](https://developers.google.com/publisher-ads-audits/reference/audits/cumulative-ad-shift) [Cumulative layout shift (CLS)](https://web.dev/cls/) |

> [!NOTE]
> **Note:** This list isn't exhaustive, and doesn't cover every aspect of page performance. The list only includes metrics that you can measure universally on any site. You may need to define [custom metrics](https://web.dev/custom-metrics/) to properly measure performance on your unique site.

Aside from page performance, you may also want to measure ad-specific business
metrics. Information such as impressions, clicks, and viewability on a
slot-by-slot basis can be obtained from
[Google Ad Manager reporting](https://support.google.com/admanager/answer/2671992).

## Test changes

Once you've defined your performance metrics and started measuring them
regularly, you can begin using this data to evaluate the performance impact of
changes to your site as they're made. You do this by comparing metrics measured
after a change is made, to those measured before the change was made (and/or
the baseline you established earlier). This sort of testing will allow you to
detect and address performance issues before they become a major problem for
your business or users.

### Automated testing

You can measure metrics that don't depend on user interaction through synthetic
tests. These sorts of tests should be run as frequently as possible during the
development process to understand how unreleased changes will affect
performance. This sort of proactive testing can help uncover performance issues
before changes are ever released to users.

One way to accomplish this is by making synthetic tests part of a
[continuous integration (CI)](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/introduction-to-ci.md) workflow, where tests run
automatically whenever a change is made. You can use
[Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) to integrate synthetic performance testing into
many CI workflows:

- [Performance monitoring with Lighthouse CI](https://web.dev/lighthouse-ci/)
- [Publisher Ads Audits for Lighthouse CI usage](https://github.com/googleads/publisher-ads-lighthouse-plugin/tree/HEAD/lighthouse-ci)

### A/B testing

Metrics that depend on user interaction can't be fully tested until a change is
actually released to users. This can be risky if you're unsure of how the change
will behave. One technique for mitigating that risk is
[A/B testing](https://www.optimizely.com/optimization-glossary/ab-testing/).

During an A/B test, different variants of a page are served to users at random.
You can use this technique to serve a modified version of your page to a small
percentage of overall traffic, while most continue to be served the unmodified
page. Combined with RUM, you can then evaluate the relative performance of the
two groups to determine which performs better---without putting 100% of traffic at
risk.

Another benefit of A/B tests is that they allow you to more accurately measure
the effects of changes. For many sites, it can be difficult to determine whether
a small difference in performance is due to a recent change or a normal
variation in traffic. Since the experimental group of an A/B test represents a
fixed percentage of overall traffic, metrics should differ from the control
group by a constant factor. Therefore, differences observed between the 2 groups
can more confidently be attributed to the change being tested.

Tools like [AB Tasty](https://www.abtasty.com/), [Optimizely](https://www.optimizely.com/), and [VWO](https://vwo.com/) can
help with setting up and running A/B tests. Be aware, however, that tag based
A/B testing (the default configuration for these tools) may itself negatively
impact performance and provide misleading results. Therefore, server side
integration is strongly recommended:

- [AB Tasty: Server-Side Testing](https://www.abtasty.com/glossary/server-side-testing/)
- [Optimizely: Server-Side Testing](https://www.optimizely.com/optimization-glossary/server-side-testing/)
- [VWO: FullStack Testing](https://help.vwo.com/hc/sections/360005765713-FullStack-Testing)

#### A/B test results

To measure the impact of a change using an A/B test, you gather metrics from
both the control and experimental groups and compare them against one another.
To do this, you need a way to tell what traffic is part of which group.

For page performance metrics, include an identifier on each page indicating
whether the control or experimental version was served. This identifier can be
anything you'd like, as long as it's something you're able to parse and
correlate metrics to. If you're using a prebuilt testing framework, this will
usually be handled for you automatically.

For ad-specific business metrics, you can use GPT's
[key-value targeting](https://developers.google.com/publisher-tag/guides/key-value-targeting) feature to differentiate ad
requests from the control versus experimental group:

    // On control group (A) pages, set page-level targeting to:
    googletag.setConfig({ targeting: { 'your-test-id': 'a' } });

    // On experimental group (B) pages, set page-level targeting to:
    googletag.setConfig({ targeting: { 'your-test-id': 'b' } });

These key-values can then be referenced when running Google Ad Manager reports,
to [filter results](https://support.google.com/admanager/answer/3415374) by group.