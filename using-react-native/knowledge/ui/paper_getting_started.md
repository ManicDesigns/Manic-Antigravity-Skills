# React Native Paper Getting Started

## Getting Started

### Installation​

- Open a Terminal in your project's folder and run:
- npm
- Yarn
- pnpm

```
npm install react-native-paper
```

```
yarn add react-native-paper
```

```
pnpm add react-native-paper
```

- Fromv5there is a need to installreact-native-safe-area-contextfor handling safe area.
- npm
- Yarn
- pnpm

```
npm install react-native-safe-area-context
```

```
yarn add react-native-safe-area-context
```

```
pnpm add react-native-safe-area-context
```

Additionaly foriOSplatform there is a requirement to link the native parts of the library:

```
npx pod-install
```

- If you're on a vanilla React Native project, you also need to install and link@react-native-vector-icons/material-design-icons.
SpecificallyMaterialDesignIconsicon pack needs to be included in the project, because some components use those internally (e.g.AppBar.BackActionon Android).

- npm
- Yarn
- pnpm

```
npm install @react-native-vector-icons/material-design-icons
```

```
yarn add @react-native-vector-icons/material-design-icons
```

```
pnpm add @react-native-vector-icons/material-design-icons
```

Thereact-native-vector-iconslibrary requires some additional setup steps for each platform. To ensure proper use of icon fonts, please follow theirinstallation guide.

If you use Expo, you don't need to install vector icons - those are the part of the expo package. However, if you have ababel.config.jsor.babelrcfile, make sure that it includesbabel-preset-expo.

If you don't want to install vector icons, you can usebabel-plugin-optional-requireto opt-out.

#### Bundle size optimization​

To get smaller bundle size by excluding modules you don't use, you can use our optional babel plugin. The plugin automatically rewrites the import statements so that only the modules you use are imported instead of the whole library. Addreact-native-paper/babelto thepluginssection in yourbabel.config.jsfor production environment. It should look like this:

```
module.exports = { presets: ['module:metro-react-native-babel-preset'], env: { production: { plugins: ['react-native-paper/babel'], }, },};
```

If you created your project using Expo, it'll look something like this:

```
module.exports = function (api) { api.cache(true); return { presets: ['babel-preset-expo'], env: { production: { plugins: ['react-native-paper/babel'], }, }, };};
```

The plugin only works if you are importing the library using ES2015 import statements and not withrequire.

The above examples are for the latestreact-nativeusing Babel 7. If you havereact-native <= 0.55, you'll have a.babelrcfile instead of ababel.config.jsfile and the content of the file will be different.

If you're using Flow for typechecking your code, you need to add the following under the[options]section in your.flowconfig:

```
module.file_ext=.jsmodule.file_ext=.native.jsmodule.file_ext=.android.jsmodule.file_ext=.ios.js
```

### Usage​

Wrap your root component inPaperProviderfromreact-native-paper(if you are using versions prior to 5.8.0 you need to useProvider). If you have a vanilla React Native project, it's a good idea to add it in the component which is passed toAppRegistry.registerComponent. This will usually be in theindex.jsfile. If you have an Expo project, you can do this inside the exported component in theApp.jsfile.

Example:

```
import * as React from 'react';import { AppRegistry } from 'react-native';import { PaperProvider } from 'react-native-paper';import { name as appName } from './app.json';import App from './src/App';export default function Main() { return ( <PaperProvider> <App /> </PaperProvider> );}AppRegistry.registerComponent(appName, () => Main);
```

ThePaperProvidercomponent provides the theme to all the components in the framework. It also acts as a portal to components which need to be rendered at the top level.

If you have another provider (such asRedux), wrap it outsidePaperProviderso that the context is available to components rendered inside aModalfrom the library:

```
import * as React from 'react';import { PaperProvider } from 'react-native-paper';import { Provider as StoreProvider } from 'react-redux';import App from './src/App';import store from './store';export default function Main() { return ( <StoreProvider store={store}> <PaperProvider> <App /> </PaperProvider> </StoreProvider> );}
```

### Customization​

You can provide a custom theme to customize the colors, typescales etc. with theProvidercomponent. Check theMaterial Design 3 default themeto see what customization options are supported.

Example:

```
import * as React from 'react';import { MD3LightTheme as DefaultTheme, PaperProvider,} from 'react-native-paper';import App from './src/App';const theme = { ...DefaultTheme, colors: { ...DefaultTheme.colors, primary: 'tomato', secondary: 'yellow', },};export default function Main() { return ( <PaperProvider theme={theme}> <App /> </PaperProvider> );}
```

For MD2 check the followingMaterial Design 2 default theme.

- InstallationBundle size optimization
- Bundle size optimization
- Usage
- Customization