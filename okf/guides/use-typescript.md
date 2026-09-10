---
type: Guide
title: "Use Google Publisher Tag with TypeScript"
description: "How to set up and use official GPT TypeScript type definitions."
resource: "https://developers.google.com/publisher-tag/guides/use-typescript"
tags: [gpt, typescript, types, tooling]
timestamp: 2026-09-10T00:00:00Z
---

# TypeScript and Google Publisher Tags

[TypeScript](https://www.typescriptlang.org/) is a strongly typed, object-oriented programming language that
compiles to JavaScript. TypeScript is a superset of JavaScript, and
supports all of JavaScript's features plus optional
[static typing](https://en.wikipedia.org/wiki/Type_system#STATIC).

Since TypeScript is a superset of JavaScript, all working JavaScript code is
also TypeScript code. However, [TypeScript tooling](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#types-for-tooling) can help detect
and prevent bugs that you might not notice in plain JavaScript.

## Get started

[DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) is an open source project that maintains a repository of
type [declaration files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html) for many packages, including the
Google Publisher Tag (GPT) library. You can install
the GPT types with [npm](https://docs.npmjs.com/about-npm) from the
[@types/google-publisher-tag](https://www.npmjs.com/package/@types/google-publisher-tag) package.

    npm install --save-dev @types/google-publisher-tag

Once installed, you have access to all of the types exposed by the
[`googletag`](https://developers.google.com/publisher-tag/reference#googletag) object in your own code. You can also take
advantage of code completion and content assist for GPT methods
and properties in source code editors that have those features,
for example, [Visual Studio Code](https://code.visualstudio.com/docs/languages/typescript).

## Demonstration

The following demo re-implements our [Get started](https://developers.google.com/publisher-tag/guides/get-started) example in
TypeScript, using the [@types/google-publisher-tag](https://www.npmjs.com/package/@types/google-publisher-tag) package and
[Vite](https://vitejs.dev/).
<iframe src="https://stackblitz.com/edit/gpt-getting-started?embed=1&amp;file=index.html,sample.ts&amp;hideNavigation=1&amp;terminal=dev" style="height: 600px; width: 100%"></iframe>