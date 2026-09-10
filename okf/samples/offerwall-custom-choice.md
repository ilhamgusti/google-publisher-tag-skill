---
type: Sample
title: "Offerwall Custom Choice"
description: "Sample demonstrating publisher-customized choices inside Google Offerwall."
resource: "https://developers.google.com/publisher-tag/samples/offerwall-custom-choice"
tags: [gpt, sample, offerwall custom choice]
timestamp: 2026-09-10T00:00:00Z
---

# Offerwall with custom choice

# Display an Offerwall with Custom Choice

This example demonstrates how to display an Offerwall on your website and
present a custom choice to users. Learn more about Offerwall in the
[Google Ad Manager help center](https://support.google.com/admanager/answer/13860694).

Adding a custom choice lets you implement your own monetization solution
as an additional user selectable option within your Offerwall. For example, you
might let visitors purchase a subscription to access more content. For more
information about custom choice, see
[Set up a "custom choice" user choice](https://support.google.com/admanager/answer/13566866).

## Usage notes

- You must write and deploy your own implementation of the [Offerwall Custom Choice API](https://developers.google.com/funding-choices/offerwall-custom-choice-docs) to use the custom choice feature. Enabling custom choice without a correct implementation will result in Offerwall not displaying to end users.
- The location and text of your custom choice is previewable in the [message builder in Privacy \& messaging](https://support.google.com/admanager/answer/11897778). However, you can't preview the custom UI that displays after users select your custom choice from Google Ad Manager. Your custom code defines the look and behavior of the UI.
- You can only add one custom choice to an Offerwall.


## Sample implementation

**Live demo:** [https://googleads.github.io/google-publisher-tag-samples/offerwall-custom-choice/js/demo.html](https://googleads.github.io/google-publisher-tag-samples/offerwall-custom-choice/js/demo.html)

**Source:** [https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/offerwall-custom-choice](https://github.com/googleads/google-publisher-tag-samples/tree/main/dist/offerwall-custom-choice)

### JavaScript

```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Display an Offerwall with custom choice" />
    <title>Offerwall with custom choice</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      class MyCustomOfferwallChoice {
        constructor() {
          // Whether or not the user should be allowed to bypass the Offerwall.
          this.isUserEntitledToAccess = false;

          // Whether the custom Offerwall choice should be disabled.
          this.isCustomOfferwallChoiceDisabled = false;
        }

        /**
         * Custom choice initialization logic.
         */
        async initialize() {
          if (this.isCustomOfferwallChoiceDisabled) {
            // Indicate that the custom choice option should not be displayed.
            return Promise.resolve(
              window.googlefc.offerwall.customchoice.InitializeResponseEnum.CUSTOM_CHOICE_DISABLED,
            );
          }

          if (this.isUserEntitledToAccess) {
            // Indicate that the user should not be shown the Offerwall.
            return Promise.resolve(
              window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_GRANTED,
            );
          }

          // Indicate that the user may be shown the Offerwall.
          return Promise.resolve(
            window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_NOT_GRANTED,
          );
        }

        /**
         * Custom choice display logic.
         */
        async show() {
          // Locate the custom choice modal dialog.
          const modal = document.querySelector(".custom-choice-modal");

          // Show modal and return a Promise that will resolve when the modal is
          // closed.
          return new Promise((resolve) => {
            // Attach an event listener to resolve the Promise when the modal is
            // closed.
            modal?.addEventListener(
              "close",
              () => {
                // Return `true` if the subscribe button was clicked, otherwise `false`.
                resolve(modal?.returnValue === "subscribe");
              },
              { once: true },
            );

            // Show the custom choice modal.
            modal?.showModal();
          });
        }
      }

      // Instantiate the Offerwall custom choice registry and register your custom
      // choice implementation. Instantiating the registry lets you begin interacting
      // with it immediately, even if the Offerwall library hasn't finished loading.
      window.googlefc = window.googlefc || {};
      window.googlefc.offerwall = window.googlefc.offerwall || {};
      window.googlefc.offerwall.customchoice = window.googlefc.offerwall.customchoice || {};
      window.googlefc.offerwall.customchoice.registry = new MyCustomOfferwallChoice();
    </script>
    <style>
      .custom-choice-modal {
        max-width: 500px;
        border: 2px solid rgba(107, 110, 118, 0.4);
        border-radius: 8px;
        padding: 10px;
        background: white;
      }

      .custom-choice-modal:open::backdrop {
        background-color: black;
        opacity: 0.6;
      }

      .custom-choice-modal h1 {
        overflow-wrap: break-word;
        font:
          500 1.25em Poppins,
          sans-serif;
        color: #202124;
        text-align: center;
      }

      .custom-choice-list-container {
        border: 1px solid rgba(95, 99, 104, 0.4);
        border-radius: 8px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        z-index: 1;
        margin-top: 24px;
      }

      button.custom-choice-list-item-button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
        width: 100%;
        text-align: left;
      }

      button.custom-choice-list-item-button:hover {
        background-color: rgba(32, 33, 36, 0.04);
        transition: background-color 150ms ease-in;
      }

      .custom-choice-list-container > button:not(:last-child) {
        border-bottom: 1px solid rgba(95, 99, 104, 0.4);
      }
      .custom-choice-list-container > button:first-child {
        border-radius: 8px 8px 0 0;
      }
      .custom-choice-list-container > button:last-child {
        border-radius: 0 0 8px 8px;
      }
      .custom-choice-list-container > button:only-child {
        border-radius: 8px;
      }

      .custom-choice-list-item-text-container {
        display: flex;
        flex-direction: column;
        gap: 4px;
        max-width: 88%;
      }

      .custom-choice-list-item-text {
        overflow-wrap: break-word;
        font:
          500 14px "Poppins",
          sans-serif;
        color: #202124;
      }

      .custom-choice-list-item-subtext {
        overflow-wrap: break-word;
        font:
          400 14px "Roboto",
          sans-serif;
        color: #5f6368;
        margin: 0;
      }

      .custom-choice-choice-icon {
        align-items: center;
        display: flex;
        justify-content: center;
        margin-left: 12px;
      }

      .custom-choice-choice-icon svg {
        fill: #174ea6;
        height: 18px;
        width: 18px;
      }
    </style>
  </head>
  <body>
    <dialog class="custom-choice-modal">
      <form method="dialog">
        <h1>Subscribe for access.</h1>
        <div class="custom-choice-list-container">
          <!-- Item 1: Subscribe -->
          <button type="submit" class="custom-choice-list-item-button" value="subscribe">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Subscribe for just $4.00 per month</span>
              <p class="custom-choice-list-item-subtext">
                Includes exclusive tips and articles, special members-only promotions and the latest
                news and announcements first
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>

          <!-- Item 2: Go Back -->
          <button type="submit" class="custom-choice-list-item-button" value="back">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Go back</span>
              <p class="custom-choice-list-item-subtext">
                Check what other options we have available for you
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>
        </div>
      </form>
    </dialog>
  </body>
</html>
```

### JavaScript (legacy)

```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Display an Offerwall with custom choice" />
    <title>Offerwall with custom choice</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script>
      var __awaiter =
        (this && this.__awaiter) ||
        function (thisArg, _arguments, P, generator) {
          function adopt(value) {
            return value instanceof P
              ? value
              : new P(function (resolve) {
                  resolve(value);
                });
          }
          return new (P || (P = Promise))(function (resolve, reject) {
            function fulfilled(value) {
              try {
                step(generator.next(value));
              } catch (e) {
                reject(e);
              }
            }
            function rejected(value) {
              try {
                step(generator["throw"](value));
              } catch (e) {
                reject(e);
              }
            }
            function step(result) {
              result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected);
            }
            step((generator = generator.apply(thisArg, _arguments || [])).next());
          });
        };
      var __generator =
        (this && this.__generator) ||
        function (thisArg, body) {
          var _ = {
              label: 0,
              sent: function () {
                if (t[0] & 1) throw t[1];
                return t[1];
              },
              trys: [],
              ops: [],
            },
            f,
            y,
            t,
            g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
          return (
            (g.next = verb(0)),
            (g["throw"] = verb(1)),
            (g["return"] = verb(2)),
            typeof Symbol === "function" &&
              (g[Symbol.iterator] = function () {
                return this;
              }),
            g
          );
          function verb(n) {
            return function (v) {
              return step([n, v]);
            };
          }
          function step(op) {
            if (f) throw new TypeError("Generator is already executing.");
            while ((g && ((g = 0), op[0] && (_ = 0)), _))
              try {
                if (
                  ((f = 1),
                  y &&
                    (t =
                      op[0] & 2
                        ? y["return"]
                        : op[0]
                          ? y["throw"] || ((t = y["return"]) && t.call(y), 0)
                          : y.next) &&
                    !(t = t.call(y, op[1])).done)
                )
                  return t;
                if (((y = 0), t)) op = [op[0] & 2, t.value];
                switch (op[0]) {
                  case 0:
                  case 1:
                    t = op;
                    break;
                  case 4:
                    _.label++;
                    return { value: op[1], done: false };
                  case 5:
                    _.label++;
                    y = op[1];
                    op = [0];
                    continue;
                  case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                  default:
                    if (
                      !((t = _.trys), (t = t.length > 0 && t[t.length - 1])) &&
                      (op[0] === 6 || op[0] === 2)
                    ) {
                      _ = 0;
                      continue;
                    }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) {
                      _.label = op[1];
                      break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                      _.label = t[1];
                      t = op;
                      break;
                    }
                    if (t && _.label < t[2]) {
                      _.label = t[2];
                      _.ops.push(op);
                      break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
                }
                op = body.call(thisArg, _);
              } catch (e) {
                op = [6, e];
                y = 0;
              } finally {
                f = t = 0;
              }
            if (op[0] & 5) throw op[1];
            return { value: op[0] ? op[1] : void 0, done: true };
          }
        };
      var MyCustomOfferwallChoice = /** @class */ (function () {
        function MyCustomOfferwallChoice() {
          // Whether or not the user should be allowed to bypass the Offerwall.
          this.isUserEntitledToAccess = false;

          // Whether the custom Offerwall choice should be disabled.
          this.isCustomOfferwallChoiceDisabled = false;
        }

        /**
         * Custom choice initialization logic.
         */
        MyCustomOfferwallChoice.prototype.initialize = function () {
          return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
              if (this.isCustomOfferwallChoiceDisabled) {
                // Indicate that the custom choice option should not be displayed.
                return [
                  2 /*return*/,
                  Promise.resolve(
                    window.googlefc.offerwall.customchoice.InitializeResponseEnum
                      .CUSTOM_CHOICE_DISABLED,
                  ),
                ];
              }

              if (this.isUserEntitledToAccess) {
                // Indicate that the user should not be shown the Offerwall.
                return [
                  2 /*return*/,
                  Promise.resolve(
                    window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_GRANTED,
                  ),
                ];
              }

              // Indicate that the user may be shown the Offerwall.
              return [
                2 /*return*/,
                Promise.resolve(
                  window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_NOT_GRANTED,
                ),
              ];
            });
          });
        };

        /**
         * Custom choice display logic.
         */
        MyCustomOfferwallChoice.prototype.show = function () {
          return __awaiter(this, void 0, void 0, function () {
            var modal;
            return __generator(this, function (_a) {
              modal = document.querySelector(".custom-choice-modal");

              // Show modal and return a Promise that will resolve when the modal is
              // closed.
              return [
                2 /*return*/,
                new Promise(function (resolve) {
                  // Attach an event listener to resolve the Promise when the modal is
                  // closed.
                  modal === null || modal === void 0
                    ? void 0
                    : modal.addEventListener(
                        "close",
                        function () {
                          // Return `true` if the subscribe button was clicked, otherwise `false`.
                          resolve(
                            (modal === null || modal === void 0 ? void 0 : modal.returnValue) ===
                              "subscribe",
                          );
                        },
                        { once: true },
                      );

                  // Show the custom choice modal.
                  modal === null || modal === void 0 ? void 0 : modal.showModal();
                }),
              ];
            });
          });
        };
        return MyCustomOfferwallChoice;
      })();

      // Instantiate the Offerwall custom choice registry and register your custom
      // choice implementation. Instantiating the registry lets you begin interacting
      // with it immediately, even if the Offerwall library hasn't finished loading.
      window.googlefc = window.googlefc || {};
      window.googlefc.offerwall = window.googlefc.offerwall || {};
      window.googlefc.offerwall.customchoice = window.googlefc.offerwall.customchoice || {};
      window.googlefc.offerwall.customchoice.registry = new MyCustomOfferwallChoice();
    </script>
    <style>
      .custom-choice-modal {
        max-width: 500px;
        border: 2px solid rgba(107, 110, 118, 0.4);
        border-radius: 8px;
        padding: 10px;
        background: white;
      }

      .custom-choice-modal:open::backdrop {
        background-color: black;
        opacity: 0.6;
      }

      .custom-choice-modal h1 {
        overflow-wrap: break-word;
        font:
          500 1.25em Poppins,
          sans-serif;
        color: #202124;
        text-align: center;
      }

      .custom-choice-list-container {
        border: 1px solid rgba(95, 99, 104, 0.4);
        border-radius: 8px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        z-index: 1;
        margin-top: 24px;
      }

      button.custom-choice-list-item-button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
        width: 100%;
        text-align: left;
      }

      button.custom-choice-list-item-button:hover {
        background-color: rgba(32, 33, 36, 0.04);
        transition: background-color 150ms ease-in;
      }

      .custom-choice-list-container > button:not(:last-child) {
        border-bottom: 1px solid rgba(95, 99, 104, 0.4);
      }
      .custom-choice-list-container > button:first-child {
        border-radius: 8px 8px 0 0;
      }
      .custom-choice-list-container > button:last-child {
        border-radius: 0 0 8px 8px;
      }
      .custom-choice-list-container > button:only-child {
        border-radius: 8px;
      }

      .custom-choice-list-item-text-container {
        display: flex;
        flex-direction: column;
        gap: 4px;
        max-width: 88%;
      }

      .custom-choice-list-item-text {
        overflow-wrap: break-word;
        font:
          500 14px "Poppins",
          sans-serif;
        color: #202124;
      }

      .custom-choice-list-item-subtext {
        overflow-wrap: break-word;
        font:
          400 14px "Roboto",
          sans-serif;
        color: #5f6368;
        margin: 0;
      }

      .custom-choice-choice-icon {
        align-items: center;
        display: flex;
        justify-content: center;
        margin-left: 12px;
      }

      .custom-choice-choice-icon svg {
        fill: #174ea6;
        height: 18px;
        width: 18px;
      }
    </style>
  </head>
  <body>
    <dialog class="custom-choice-modal">
      <form method="dialog">
        <h1>Subscribe for access.</h1>
        <div class="custom-choice-list-container">
          <!-- Item 1: Subscribe -->
          <button type="submit" class="custom-choice-list-item-button" value="subscribe">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Subscribe for just $4.00 per month</span>
              <p class="custom-choice-list-item-subtext">
                Includes exclusive tips and articles, special members-only promotions and the latest
                news and announcements first
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>

          <!-- Item 2: Go Back -->
          <button type="submit" class="custom-choice-list-item-button" value="back">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Go back</span>
              <p class="custom-choice-list-item-subtext">
                Check what other options we have available for you
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>
        </div>
      </form>
    </dialog>
  </body>
</html>
```

### TypeScript

`ts/index.html`:


```html
<!DOCTYPE html>
<!--
 @license
 Copyright 2022 Google LLC. All Rights Reserved.
 SPDX-License-Identifier: Apache-2.0
-->
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Display an Offerwall with custom choice" />
    <title>Offerwall with custom choice</title>
    <script
      async
      src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"
      crossorigin="anonymous"
    ></script>
    <script type="module" src="/sample.ts"></script>
    <style>
      .custom-choice-modal {
        max-width: 500px;
        border: 2px solid rgba(107, 110, 118, 0.4);
        border-radius: 8px;
        padding: 10px;
        background: white;
      }

      .custom-choice-modal:open::backdrop {
        background-color: black;
        opacity: 0.6;
      }

      .custom-choice-modal h1 {
        overflow-wrap: break-word;
        font:
          500 1.25em Poppins,
          sans-serif;
        color: #202124;
        text-align: center;
      }

      .custom-choice-list-container {
        border: 1px solid rgba(95, 99, 104, 0.4);
        border-radius: 8px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        z-index: 1;
        margin-top: 24px;
      }

      button.custom-choice-list-item-button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
        width: 100%;
        text-align: left;
      }

      button.custom-choice-list-item-button:hover {
        background-color: rgba(32, 33, 36, 0.04);
        transition: background-color 150ms ease-in;
      }

      .custom-choice-list-container > button:not(:last-child) {
        border-bottom: 1px solid rgba(95, 99, 104, 0.4);
      }
      .custom-choice-list-container > button:first-child {
        border-radius: 8px 8px 0 0;
      }
      .custom-choice-list-container > button:last-child {
        border-radius: 0 0 8px 8px;
      }
      .custom-choice-list-container > button:only-child {
        border-radius: 8px;
      }

      .custom-choice-list-item-text-container {
        display: flex;
        flex-direction: column;
        gap: 4px;
        max-width: 88%;
      }

      .custom-choice-list-item-text {
        overflow-wrap: break-word;
        font:
          500 14px "Poppins",
          sans-serif;
        color: #202124;
      }

      .custom-choice-list-item-subtext {
        overflow-wrap: break-word;
        font:
          400 14px "Roboto",
          sans-serif;
        color: #5f6368;
        margin: 0;
      }

      .custom-choice-choice-icon {
        align-items: center;
        display: flex;
        justify-content: center;
        margin-left: 12px;
      }

      .custom-choice-choice-icon svg {
        fill: #174ea6;
        height: 18px;
        width: 18px;
      }
    </style>
  </head>
  <body>
    <dialog class="custom-choice-modal">
      <form method="dialog">
        <h1>Subscribe for access.</h1>
        <div class="custom-choice-list-container">
          <!-- Item 1: Subscribe -->
          <button type="submit" class="custom-choice-list-item-button" value="subscribe">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Subscribe for just $4.00 per month</span>
              <p class="custom-choice-list-item-subtext">
                Includes exclusive tips and articles, special members-only promotions and the latest
                news and announcements first
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>

          <!-- Item 2: Go Back -->
          <button type="submit" class="custom-choice-list-item-button" value="back">
            <div class="custom-choice-list-item-text-container">
              <span class="custom-choice-list-item-text">Go back</span>
              <p class="custom-choice-list-item-subtext">
                Check what other options we have available for you
              </p>
            </div>
            <svg
              class="custom-choice-choice-icon"
              aria-hidden="true"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              focusable="false"
            >
              <path d="M7.59 18.59L9 20l8-8-8-8-1.41 1.41L14.17 12"></path>
            </svg>
          </button>
        </div>
      </form>
    </dialog>
  </body>
</html>
```

`ts/sample.ts`:


```typescript
/**
 * @license
 * Copyright 2025 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

class MyCustomOfferwallChoice {
  // Whether or not the user should be allowed to bypass the Offerwall.
  private isUserEntitledToAccess = false;

  // Whether the custom Offerwall choice should be disabled.
  private isCustomOfferwallChoiceDisabled = false;

  /**
   * Custom choice initialization logic.
   */
  async initialize() {
    if (this.isCustomOfferwallChoiceDisabled) {
      // Indicate that the custom choice option should not be displayed.
      return Promise.resolve(
        window.googlefc.offerwall.customchoice.InitializeResponseEnum.CUSTOM_CHOICE_DISABLED,
      );
    }

    if (this.isUserEntitledToAccess) {
      // Indicate that the user should not be shown the Offerwall.
      return Promise.resolve(
        window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_GRANTED,
      );
    }

    // Indicate that the user may be shown the Offerwall.
    return Promise.resolve(
      window.googlefc.offerwall.customchoice.InitializeResponseEnum.ACCESS_NOT_GRANTED,
    );
  }

  /**
   * Custom choice display logic.
   */
  async show() {
    // Locate the custom choice modal dialog.
    const modal = document.querySelector(".custom-choice-modal") as HTMLDialogElement;

    // Show modal and return a Promise that will resolve when the modal is
    // closed.
    return new Promise<boolean>((resolve) => {
      // Attach an event listener to resolve the Promise when the modal is
      // closed.
      modal?.addEventListener(
        "close",
        () => {
          // Return `true` if the subscribe button was clicked, otherwise `false`.
          resolve(modal?.returnValue === "subscribe");
        },
        { once: true },
      );

      // Show the custom choice modal.
      modal?.showModal();
    });
  }
}

// Instantiate the Offerwall custom choice registry and register your custom
// choice implementation. Instantiating the registry lets you begin interacting
// with it immediately, even if the Offerwall library hasn't finished loading.
window.googlefc = window.googlefc || {};
window.googlefc.offerwall = window.googlefc.offerwall || {};
window.googlefc.offerwall.customchoice = window.googlefc.offerwall.customchoice || {};
window.googlefc.offerwall.customchoice.registry = new MyCustomOfferwallChoice();

/**
 * Offerwall custom choice type definitions.
 *
 * @see https://developers.google.com/funding-choices/offerwall-custom-choice-docs
 */
interface Window {
  googlefc: {
    offerwall: {
      customchoice: {
        InitializeResponseEnum: {
          CUSTOM_CHOICE_DISABLED: number;
          ACCESS_GRANTED: number;
          ACCESS_NOT_GRANTED: number;
        };
        registry: {
          initialize: () => Promise<number>;
          show: () => Promise<boolean>;
        };
      };
    };
  };
}
```
