The Google Publisher Tag (GPT) library lets you generate ad tags
with *passback* functionality. These tags can be used in any situation where an
ad request to a third party should ultimately be filled by an ad trafficked in
your own Google Ad Manager network.

## Use cases

### Traffic remnant or fallback line items

Passback tags can be used when a third-party server doesn't have an ad to
serve or when an ad doesn't meet the minimum CPM/floor price agreed upon with
the third party. In these cases, the third-party server instead serves a
GPT passback tag, which returns a [house ad](https://support.google.com/admanager/answer/79305) or
other [remnant ad](https://support.google.com/admanager/table/7636513#remnantad) from your own Ad Manager
network.

#### Example workflow


If third-party ad network A wants to return an ad to
Ad Manager publisher B, but does not have an eligible ad, ad
network A delivers a passback tag. This passback tag will then return an ad
from the Ad Manager ad server to publisher B which matches the
targeting criteria.

1. The webpage makes a call to the Ad Manager ad server using the Ad Manager ad tag.
2. The Ad Manager ad server returns an ad containing a third-party ad tag.
3. The third-party ad tag calls the third-party ad server for an ad.
4. The third-party ad server does not have an eligible ad, so returns a passback ad tag.
5. The passback ad tag makes a call to Ad Manager to serve an ad matching the specified targeting criteria.
6. The Ad Manager ad server returns an ad that matches the passback ad tag targeting criteria.

### Serve ads on another publisher's website

Passback tags can be used to serve ads from your Ad Manager
network on another publisher's website. In these cases, the GPT
passback tag would be trafficked by the other publisher and would return an ad
from your own Ad Manager network.

#### Example workflow


If Ad Manager network A wants to deliver ads to publisher B,
Ad Manager network A sends a passback tag to publisher B.
Publisher B serves the passback tag, which ultimately returns an ad from
Ad Manager network A.

1. The passback ad tag makes a call to Ad Manager to serve an ad matching the specified targeting criteria.
2. The Ad Manager server returns an ad that matches the passback ad tag targeting criteria.

### Serve video ads

To create video passbacks, use a standard video tag to pass back from a third
party to Ad Manager.

You can build this tag [manually](https://support.google.com/admanager/answer/1068325) or using the
[Ad Manager video tag generator](https://support.google.com/admanager/answer/1181016).

## Construct passback tags

Passback tags can be constructed using the same API used to construct normal
GPT ad tags. However, passback tags must be rendered inside an
`iframe` to prevent them from inheriting page-level settings from any other
GPT instance active on the publisher's website.

> [!WARNING]
> **Warning:** Passback tags must be constructed as shown in the following example. The legacy `definePassback()` and `defineOutOfPagePassback()` GPT library methods are deprecated and will be removed in a future update.

A basic example passback tag is shown in the following section. Remember that
this fragment is intended to be rendered inside an `iframe`. To see this in
practice, you can [try a live demo](https://stackblitz.com/edit/gpt-passback-example?file=index.html) of this example on
StackBlitz.

    <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
    <div id="gpt-passback">
      <script>
        window.googletag = window.googletag || {cmd: []};
        googletag.cmd.push(function() {
            googletag.defineSlot('/6355419/Travel/Europe', [728, 90], 'gpt-passback')
              .addService(googletag.pubads());
            googletag.enableServices();
            googletag.display('gpt-passback');
        });
      </script>
    </div>

## Configure passback tags

Passback tags support the normal range of features available to
GPT tags, such as those covered in the
[key-value targeting guide](https://developers.google.com/publisher-tag/guides/key-value-targeting) and [code samples](https://developers.google.com/publisher-tag/samples).
Features which are unique to passback tags or which require special
configuration when used in a passback context are explained in the following
sections.

### Enable click tracking

To add click tracking to a passback tag, a clickthrough URL macro can be
appended to the tag as in the following example. The clickthrough URL will be
dynamically prepended to the clickthrough URL stored on the
Ad Manager ad server.

    <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
    <div id="gpt-passback">
      <script>
        window.googletag = window.googletag || {cmd: []};
        googletag.cmd.push(function() {
            const slot = googletag.defineSlot('/6355419/Travel/Europe', [728, 90], 'gpt-passback')
              .addService(googletag.pubads());
            slot.setConfig({ clickUrl: '%%CLICK_URL_UNESC%%' });
            googletag.enableServices();
            googletag.display('gpt-passback');
        });
      </script>
    </div>

### Inherit privacy settings

Since passback tags are rendered in an iframe, they do not automatically inherit
privacy settings configured at the page-level. When passbacks are being used to
serve an ad from one Ad Manager publisher to another, the
[TFAT macro](https://support.google.com/admanager/answer/2376981#tag-for-age-treatment) can be used to include the current page-level
age treatment setting in the passback ad request.

> [!NOTE]
> **Note:** the TFAT macro can only be used when both publishers use Ad Manager for ad serving.

    <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
    <div id="gpt-passback">
      <script>
        window.googletag = window.googletag || {cmd: []};
        googletag.cmd.push(function() {
            googletag.defineSlot('/6355419/Travel/Europe', [728, 90], 'gpt-passback')
              .addService(googletag.pubads());
            googletag.pubads()
    .setPrivacySettings({ tagForAgeTreatment: Number('%%TFAT%%') });
            googletag.enableServices();
            googletag.display('gpt-passback');
        });
      </script>
    </div>

### Manage child publisher's inventory

Multiple Customer Management (MCM) is an Ad Manager feature that
grants access to ad requests that other publishers have delegated to your
account. For more information, see
[About Multiple Customer Management](https://support.google.com/admanager/answer/11130475).

To utilize MCM, the passback tags of the parent publisher must be updated to
include the Ad Manager network code of the child publisher. This
allows Ad Manager to recognize the child publisher network and
helps verify creatives are served correctly.

    <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
    <div id="gpt-passback">
      <script>
        window.googletag = window.googletag || {cmd: []};
        googletag.cmd.push(function() {
            googletag.defineSlot('/6355419,1234/Travel/Europe', [728, 90], 'gpt-passback')
              .addService(googletag.pubads())
            googletag.enableServices();
            googletag.display('gpt-passback');
        });
      </script>
    </div>

In the preceding example, `6355419` is the Ad Manager network code
for the parent publisher and `1234` is the network code for the child publisher.

### Specify page URL

Since passback tags are rendered in an iframe, GPT may not be
able to determine the URL of the page on which the tag is being served. If you
are using Ad Exchange or AdSense to fill passback impressions, these systems
can't send contextual information about the page to buyers without a page URL.
This can lead to lower fill rates, lower CPMs, or in some cases, rejected ad
requests.

To avoid this, the [PATTERN macro](https://support.google.com/admanager/answer/2376981#pattern) can be used to provide
page URL information to a third-party network or ad server. This information can
then be added to the passback tag as a `page_url` attribute.

#### Example workflow

1. A user visits example.com/mypage.html. The page requests ads.
2. Ad Manager serves a third-party network tag and inserts a <var translate="no">URL</var> using the `%%PATTERN:url%%` macro.
3. The third-party network receives the ad request, but can't fill it.
4. The third party serves a Ad Manager passback into its own iframe, setting the `page_url` AdSense attribute to the URL value provided in the ad request.
5. Ad Manager receives an ad request with the page URL. Ad Exchange and AdSense can send buyers contextual information.

    <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script>
    <div id="gpt-passback">
      <script>
        window.googletag = window.googletag || {cmd: []};
        googletag.cmd.push(function() {
            googletag.defineSlot('/6355419/Travel/Europe', [728, 90], 'gpt-passback')
              .addService(googletag.pubads());
            googletag.setConfig({
    adsenseAttributes: { page_url: 'URL' },
    });
            googletag.enableServices();
            googletag.display('gpt-passback');
        });
      </script>
    </div>