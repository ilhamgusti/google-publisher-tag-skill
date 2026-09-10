# Cross-Origin Embedder Policy

`Cross-Origin-Embedder-Policy` ([COEP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy)) is a response header that lets a
page opt in to more restrictive handling. The Google Publisher Tag
(GPT) does not yet support pages served with this restriction;
thus, we recommend publishers affected by Chrome's
[`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) deprecation opt their site out by
[applying for the reverse Origin Trial](https://developer.chrome.com/blog/enabling-shared-array-buffer/#origin-trial) until Chrome
supports combining COEP with ads.

## How do I know if my site is affected?

Chrome has [documentation](https://web.dev/cross-origin-isolation-guide/#determine-where-in-your-website-sharedarraybuffer-is-used) describing how to use Chrome DevTools
to determine whether your site uses `SharedArrayBuffer`. If DevTools tells you
that the use of `SharedArrayBuffer` is in a third-party script, inquire from the
vendor whether `SharedArrayBuffer` is required for the script's operation.

## Why am I seeing a `SharedArrayBuffer` deprecation warning in desktop Chrome?

Because `SharedArrayBuffer` can be used to create a high resolution timer, it
can make [Spectre](https://security.googleblog.com/2021/03/a-spectre-proof-of-concept-for-spectre.html)-style attacks more efficient. Browsers are limiting
its use to pages that opt in to COEP. That limitation is already in place for
[Firefox](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer/Planned_changes) and [Android Chrome](https://developer.chrome.com/blog/enabling-shared-array-buffer/), and
[Desktop Chrome](https://developer.chrome.com/blog/enabling-shared-array-buffer/) will be applying it in version 92.

## Why doesn't GPT support COEP yet?

Displaying ads requires embedding cross-origin content, and COEP requires that
content to [explicitly opt in to](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy) cross-origin embedding. This requires
changes to every resource in every ad, both ones served by Google and ones
served by third parties. We are working with Chrome on [changes](https://www.chromestatus.com/feature/4918234241302528)
to allow COEP sites to include ads without requiring such extensive changes.

## What are my options?

If your site requires `SharedArrayBuffer`, Chrome is offering a per-site opt-out
through a [reverse Origin Trial](https://developer.chrome.com/blog/enabling-shared-array-buffer/#origin-trial), which allows use of
`SharedArrayBuffer` in Chrome 92 and later. Chrome plans to [continue
supporting this opt-out](https://groups.google.com/a/chromium.org/g/blink-dev/c/1NKvbIj3dq4/m/ToXFE-m7AgAJ) until support for embedding
unmodified third-party content is released. At that point we indend to ensure
GPT supports COEP pages.