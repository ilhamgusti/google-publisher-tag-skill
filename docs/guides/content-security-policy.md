# Integrate with a Content Security Policy

[Content Security Policy](https://csp.withgoogle.com/) (CSP) is a means of securing
your web page by limiting what resources and scripts are allowed to load and
execute. You can enable CSP by setting a `Content-Security-Policy` header in
HTTP responses from your web server.

There are two standard ways to configure CSP:

1. Specify an allowlist of domains that can inject their resources on the page.

2. Specify a random nonce, with which resources on the page must be marked in
   order to load. This approach is known as [strict CSP](https://csp.withgoogle.com/docs/strict-csp.html).

Because the domains that Google Publisher Tag (GPT) uses change over
time, we only support strict CSP (option 2). This approach removes the need to
maintain a rolling list of domains that might become outdated and break your
site.

## Setting up CSP with GPT

1. Enable CSP on your web server.

   Follow the steps outlined in [adopting strict CSP](https://csp.withgoogle.com/docs/adopting-csp.html) to
   set up the CSP header and apply the nonce to every script tag on your page,
   including `gpt.js`. GPT specifically supports the following
   CSP directives:

       Content-Security-Policy:
         object-src 'none';
         script-src 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' 'strict-dynamic' https: http:;
         base-uri 'none';
         report-uri https://your-report-collector.example.com/

   You can choose a more permissive policy if it fits your use case. More
   restrictive policies may break without notice.
2. Enable cross-domain rendering.

   Ad iframes can load external resources that might not be permitted by the
   CSP. Since same domain iframes inherit the top level window's CSP, and
   GPT cannot control the creative's contents, same-domain
   creatives will generally not work properly with CSP headers.

   To enable cross domain rendering for all creatives, execute
   [`googletag.setConfig({ safeFrame: { forceSafeFrame: true } })`](https://developers.google.com/publisher-tag/reference#googletag.config.PageSettingsConfig.safeFrame)
   before loading any ad slots.

   > [!NOTE]
   > **Note:** Certain reservation creatives may depend on being rendered in a same domain iframe and fail to load with safe frame enabled globally. Check your inventory to see if this is the case; one indicator is the creative content checking for the existence of `inDapIF` or `inGptIF` variables.

       <!doctype html>
       <html>
         <head>
           <meta charset="utf-8">
           <title>Hello GPT</title>
           <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" nonce="KC7tcz53FHqumKP1" async></script>
           <script nonce="KC7tcz53FHqumKP1">
             window.googletag = window.googletag || {cmd: []};
             googletag.cmd.push(function() {
               googletag.setConfig({ safeFrame: { forceSafeFrame: true } });
             });
           </script>
         </head>

## Testing

We recommend that you test your policies first by setting the
[`Content-Security-Policy-Report-Only`](https://developers.google.com/web/fundamentals/security/csp#reporting) header instead of
`Content-Security-Policy`. The header reports violations but still allows
them on the page.