# Avoiding Common Implementation Mistakes

The following scenarios represent some of the most common mistakes observed when
implementing GPT. While such implementations may appear to function well with the current
version of GPT, it is not guaranteed that they will continue to do so in the future. In the
most extreme cases these implementations may cause ad serving to break in unpredictable ways.
They are considered unsupported implementations.


Each scenario includes a suggested approach for fixing the issue shown.


Note that this list does not represent a fully exhaustive list of potential issues,
but is expected to serve as a helpful guide to identify the types of issues that may need to
be addressed.


Furthermore, depending on your implementation, you may need to look for all the places where
such changes may be necessary within your site.

## Common Mistakes

### Scenario 1: Using unofficial copies of GPT JavaScript libraries

|---|---|
| **High level use case description** | Hosting gpt.js, pubads_impl.js, or any libraries they load from your own servers, or loading these files from an unofficial source. |
| **Example Code snippet with error** | ``` // Incorrect: Accessing these files from an unofficial source <script async src="https://www.example.com/tag/js/gpt.js"></script> ``` |
| **Suggested ways to fix the error** | ``` // Correct: Access these files from a Google domain <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async></script> // Also correct, if using https://support.google.com/admanager/answer/9882911 <script src="https://pagead2.googlesyndication.com/tag/js/gpt.js" async></script> ``` |

### Scenario 2: Relying on gpt.js script tag listeners

|---|---|
| **High level use case description** | Assuming that the GPT API is ready to be called when the JavaScript file `gpt.js` is loaded is wrong, as some parts of the API are provided by the `pubads_impl.js` file. Relying in any way (including frameworks) on the API from within event listeners attached to the script tag is therefore incorrect. |
| **Example Code snippet with error** | ``` var tag = document.createElement('script'); tag.type = 'text/javascript'; tag.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js'; // Incorrect: Attaching a callback to the script's onload event. tag.onload = callback; var node = document.getElementsByTagName('script')[0]; node.parentNode.insertBefore(tag, node); ``` |
| **Suggested ways to fix the error** | ``` // Make sure that googletag.cmd exists. window.googletag = window.googletag || {}; googletag.cmd = googletag.cmd || []; // Correct: Queueing the callback on the command queue. googletag.cmd.push(callback); ``` |
| **Explanation / description of the fix** | `googletag.cmd` maintains a list of commands that will be run as soon as GPT is ready. This is the correct way to make sure your callback is run when GPT has loaded. |

### Scenario 3: Checking the googletag object to know whether GPT is ready

|---|---|
| **High level use case description** | Since the GPT API may not be ready when the JavaScript file `gpt.js` is loaded or when the `googletag` object is defined, checking that object to see whether the GPT API is available is not reliable. |
| **Example Code snippet with error** | ``` // Incorrect: Relying on the presence of the googletag object // as a check for the GPT API. if (typeof googletag != 'undefined') { functionProcessingGPT(); } ``` |
| **Suggested ways to fix the error** | ``` // Correct: Relying on googletag.apiReady as a check for the GPT API. if (window.googletag && googletag.apiReady) { functionProcessingGPT(); } ``` |
| **Explanation / description of the fix** | GPT will populate the boolean flag [googletag.apiReady](https://developers.google.com/publisher-tag/reference#googletag.apiReady) as soon as the API is ready to be called so that you can make reliable assertions. |

### Scenario 4: Relying on obfuscated code syntax

|---|---|
| **High level use case description** | If you're relying on precise syntax of the minified GPT library code, you will almost certainly experience breakages. Please limit your usage to the API documented in the [API Reference Guide](https://developers.google.com/publisher-tag/reference), as we are continually changing the inner workings of GPT for constant improvements. For example, a common requirement is to detect when PubAdsService is fully loaded in order to call `refresh()`. |
| **Example Code snippet with error** | ``` // Incorrect: Relying on an obfuscated property. if (googletag.pubads().a != null) { functionProcessingGPT(); } ``` |
| **Suggested ways to fix the error** | ``` // Correct: Relying on public GPT API methods // (i.e. googletag.pubadsReady in this case). if(window.googletag && googletag.pubadsReady) { functionProcessingGPT(); } ``` |
| **Explanation / description of the fix** | Only the public API can be relied on. In the case of detecting whether PubAdsService is fully loaded we have a boolean value [googletag.pubadsReady](https://developers.google.com/publisher-tag/reference#googletag.pubadsReady). |

### Scenario 5: Overwriting any function or variable of GPT

|---|---|
| **High level use case description** | Use cases based on overwriting any function or variable used by GPT may break at any time as this is not a supported use case. Timing changes in GPT internals may surface this kind of incorrect behavior by breakages. |
| **Example Code snippet with error** | ``` // Incorrect: Haphazardly overwriting a googletag.* property. googletag.cmd = []; ``` |
| **Suggested ways to fix the error** | ``` // Correct: Never overwrite googletag.* properties if they already exist. // Always check before assigning to them. googletag.cmd = googletag.cmd || []; ``` |

### Scenario 6: Mis-ordering calls to GPT

|---|---|
| **High level use case description** | Race conditions may create breakages as the internals of GPT evolve. An incorrectly ordered set of statements that were functional due to specific timings in the execution may not remain operational in the future. |
| **Example Code snippet with error** | ``` // Incorrect: Setting page-level key-value targeting after calling // googletag.enableServices(). googletag.enableServices(); googletag.defineSlot(...); googletag.pubads().setTargeting(e, a); ``` |
| **Suggested ways to fix the error** | ``` // Correct: Setting page-level key-value targeting before calling // googletag.enableServices(). googletag.pubads().setTargeting(e, a); googletag.defineSlot(...); googletag.enableServices(); ``` |
| **Explanation / description of the fix** | Avoid race conditions by making sure to respect the usual timing of GPT. Example valid partial orderings include: - **Define-Enable-Display** 1. Define page-level settings 2. Define slots 3. enableServices() 4. Display slots - **Enable-Define-Display** 1. Define page-level settings 2. enableServices() 3. Define slots 4. Display slots |

### Scenario 7: Misusing closures and JavaScript variable scoping

|---|---|
| **High level use case description** | Incorrect assumptions about JavaScript variable scoping, and the value of variables captured in the function passed to `googletag.cmd.push`. |
| **Example Code snippet with error** | ``` // Incorrect: Variable x is declared outside the anonymous function // but referenced within it. for (var x = 0; x < slotCount; x++) { window.googletag.cmd.push( function(){ // If GPT is not yet loaded, this code will be executed subsequently when // the command queue is processed. Every queued function will use the last value // assigned to x (most likely slotCount). // This is because the function closure captures the reference to x, // not the current value of x. window.googletag.display(slot[x]); }) } } ``` |
| **Suggested ways to fix the error** | ``` window.googletag.cmd.push( function(){ // Correct: We both declare and reference x inside the context of the function. for (var x = 0; x < slotCount; x++){ window.googletag.display(slot[x]); } } ) ``` |
| **Explanation / description of the fix** | In JavaScript, closures capture variables by reference rather than by value. This means that if a variable is re-assigned, then its new value will be used when the function closure that captured it is later executed. Thus the behaviour of the code in the closure may change depending on whether the callback is executed immediately or delayed. In the case of asynchronously loaded GPT, depending on how quickly GPT loads the callbacks on the command queue might execute immediately or not. In the previous example, this alters the behaviour of the queued commands. To avoid any issues, code should be written without the assumption that functions placed on the command queue will execute immediately, and care should be taken with regards to scoping rules of JavaScript. |

### Scenario 8: Moving slot containers within the DOM after calling display

|---|---|
| **High level use case description** | Moving or inserting slot containers in the DOM after calling display can lead to undesirable reflow and unpredictable behavior in GPT. |
| **Example Code snippet with error** | ``` // Incorrect: Moving slot containers after calling display googletag.defineSlot("/1234/travel/asia", [728, 90], "div-gpt-ad-123456789-0"); googletag.enableServices(); googletag.display("div-gpt-ad-123456789-0"); ... // Inserting another element before the slot container, pushing the slot container down the page. document.body.insertBefore(someOtherElement, document.getElementById("div-gpt-ad-123456789-0")); ``` |
| **Suggested ways to fix the error** | ``` // Correct: Make any DOM order changes before calling display document.body.insertBefore(someOtherElement, document.getElementById("div-gpt-ad-123456789-0")); ... googletag.defineSlot("/1234/travel/asia", [728, 90], "div-gpt-ad-123456789-0"); googletag.enableServices(); googletag.display("div-gpt-ad-123456789-0"); ``` |

### Scenario 9: Overwriting browser APIs

|---|---|
| **High level use case description** | Overwriting (a.k.a. monkey patching, polyfilling) browser APIs is not supported in GPT. This practice has the potential to break third party scripts like GPT in unexpected ways. |
| **Example Code snippet with error** | ``` // Incorrect: Overwriting window.fetch const { fetch: originalFetch } = window; window.fetch = (...args) => { console.log('Fetching!'); return originalFetch(resource, config); }; ``` |
| **Suggested ways to fix the error** | ``` // Correct: Avoid making changes to browser APIs. // If you need custom logic, consider leaving the browser API intact. const myFetch = (...args) => { console.log('Fetching!'); return window.fetch(...args); } ``` |