---
type: Reference
title: "Display ads in the shadow DOM"
description: "The [shadow DOM](https://developer.mozilla.org/docs/Web/API/Web_components/Using_shadow_DOM) lets you attach a DOM tree to an element, and have"
tags: [gpt, _staging]
timestamp: 2026-09-10T00:00:00Z
---

# Display ads in the shadow DOM

# Display ads in the shadow DOM

The [shadow DOM](https://developer.mozilla.org/docs/Web/API/Web_components/Using_shadow_DOM) lets you attach a DOM tree to an element, and have
the internals of that tree isolated from the rest of the page. By default, any
elements created inside of the shadow DOM are inaccessible to JS and CSS running
on the main page.

When the Google Publisher Tag (GPT) library is loaded on the main page, it's
capable of rendering ads into containers within the shadow DOM, if the following
requirements are met:

1. The shadow DOM is attached in [open mode](https://developer.mozilla.org/docs/Web/API/Web_components/Using_shadow_DOM#element.shadowroot_and_the_mode_option).
2. Calls to [`googletag.display()`](https://developers.google.com/publisher-tag/reference#googletag.display) provide a reference to an ad container element, instead of a DOM ID string.

