# Reanimated Getting Started

## Getting started

The goal of theFundamentalssection is to help you gain a strong foundation on the core concepts of Reanimated and give you the confidence to explore more advanced use cases on your own. This section is packed with interactive examples, code snippets and explanations. Are you ready? Let's dive in!

### What is React Native Reanimated?​

React Native Reanimated is a powerful animation library built bySoftware Mansion.

With Reanimated, you can easily create smooth animations and interactions that run on theUI thread.

### Prerequisites​

Reanimated 4.x works only withthe React Native New Architecture (Fabric).
If your app still uses the old architecture, you can use Reanimated in version 3 which is still actively maintained.

Alternatively, you can dive intoour exampleson GitHub.

### Installation​

It takes two steps to add Reanimated 4 to an Expo project:

#### Step 1: Install the package​

Installreact-native-reanimatedandreact-native-workletspackages from npm:

- NPM
- YARN

```
npm install react-native-reanimated
```

```
yarn add react-native-reanimated
```

##### Dependencies​

This library requires an installation of thereact-native-workletsdependency. It was separated fromreact-native-reanimatedfor better modularity and must be installed separately.
You can read more about Worklets in theWorklets documentation.

- NPM
- YARN

```
npm install react-native-worklets
```

```
yarn add react-native-worklets
```

#### Step 2: Rebuild native dependencies​

Run prebuild to update the native code in theiosandandroiddirectories.

- NPM
- YARN

```
npx expo prebuild
```

```
yarn expo prebuild
```

And that's it! Reanimated 4 is now configured in your Expo project.

#### React Native Community CLI​

When usingReact Native Community CLI, you also need to manually add thereact-native-worklets/pluginplugin to yourbabel.config.js.

```
 /** @type {import('react-native-worklets/plugin').PluginOptions} */ const workletsPluginOptions = { // Your custom options. } module.exports = { presets: [ ... // don't add it here :) ], plugins: [ ... ['react-native-worklets/plugin', workletsPluginOptions], ], };
```

react-native-worklets/pluginhas to be listed last.

Why do I need this?

In short, the Worklets Babel plugin automatically converts special JavaScript functions (calledworklets) to allow them to be passed and run on the UI thread.

SinceExpo SDK 50, the Expo starter template includes the Worklets Babel plugin by default.

To learn more about the plugin head onto toWorklets Babel plugin docs page.

##### Clear Metro bundler cache (recommended)​

- NPM
- YARN

```
npm start -- --reset-cache
```

```
yarn start --reset-cache
```

##### Android​

No additional steps are necessary.

##### iOS​

While developing for iOS, make sure to installpodsfirst before running the app:

```
cd ios && pod install && cd ..
```

##### Web​

For building apps that target web usingreact-native-webwe highly recommend to useExpo.

To use Reanimated on the web all you need to do is to install and add@babel/plugin-proposal-export-namespace-fromBabel plugin to yourbabel.config.js.

- NPM
- YARN

```
npm install @babel/plugin-proposal-export-namespace-from
```

```
yarn add @babel/plugin-proposal-export-namespace-from
```

```
 /** @type {import('react-native-worklets/plugin').PluginOptions} */ const workletsPluginOptions = { // Your custom options. } module.exports = { presets: [ ... // don't add it here :) ], plugins: [ ... '@babel/plugin-proposal-export-namespace-from', ['react-native-worklets/plugin', workletsPluginOptions], ], };
```

Make sure to listreact-native-worklets/pluginlast.

More advanced use cases such as running Reanimated withwebpackor withNext.jsare explained in a separateWeb Supportguide.

- What is React Native Reanimated?
- Prerequisites
- InstallationStep 1: Install the packageStep 2: Rebuild native dependenciesReact Native Community CLI
- Step 1: Install the package
- Step 2: Rebuild native dependencies
- React Native Community CLI