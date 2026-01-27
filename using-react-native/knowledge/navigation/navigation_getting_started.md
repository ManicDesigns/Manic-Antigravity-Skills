# React Navigation Getting Started

## Getting started

TheFundamentalssection covers the most important aspects of React Navigation. It should be enough to build a typical mobile application and give you the background to dive deeper into the more advanced topics.

If you're already familiar with JavaScript, React and React Native, you'll be able to get moving with React Navigation quickly! If not, we recommend gaining some basic knowledge first, then coming back here when you're done.

- React Documentation
- React Native Documentation
- react-native>= 0.72.0
- expo>= 52 (if you useExpo Go)
- typescript>= 5.0.0 (if you use TypeScript)

### Starter template​

You can use theReact Navigation templateto quickly set up a new project:

```
npx create-expo-app@latest --template react-navigation/template
```

See the project'sREADME.mdfor more information on how to get started.

If you created a new project using the template, you can skip the installation steps below and move on to"Hello React Navigation".

Otherwise, you can follow the instructions below to install React Navigation into your existing project.

### Installation​

The@react-navigation/nativepackage contains the core functionality of React Navigation.

In your project directory, run:

- npm
- yarn
- pnpm
- bun

```
npm install @react-navigation/native
```

```
yarn add @react-navigation/native
```

```
pnpm add @react-navigation/native
```

```
bun add @react-navigation/native
```

#### Installing dependencies​

Next, install the dependencies used by most navigators:react-native-screensandreact-native-safe-area-context.

- Expo
- Community CLI
In your project directory, run:

```
npx expo install react-native-screens react-native-safe-area-context
```

This will install versions of these libraries that are compatible with your Expo SDK version.

In your project directory, run:

- npm
- yarn
- pnpm
- bun

```
npm install react-native-screens react-native-safe-area-context
```

```
yarn add react-native-screens react-native-safe-area-context
```

```
pnpm add react-native-screens react-native-safe-area-context
```

```
bun add react-native-screens react-native-safe-area-context
```

If you're on a Mac and developing for iOS, install the pods viaCocoapodsto complete the linking:

```
npx pod-install ios
```

##### Configuringreact-native-screenson Android​

react-native-screensrequires one additional configuration to properly work on Android.

EditMainActivity.ktorMainActivity.javaunderandroid/app/src/main/java/<your package name>/and add the highlighted code:

- Kotlin
- Java

```
import android.os.Bundleimport com.swmansion.rnscreens.fragment.restoration.RNScreensFragmentFactory// ...class MainActivity: ReactActivity() { // ... override fun onCreate(savedInstanceState: Bundle?) { supportFragmentManager.fragmentFactory = RNScreensFragmentFactory() super.onCreate(savedInstanceState) } // ...}
```

```
import android.os.Bundle;import com.swmansion.rnscreens.fragment.restoration.RNScreensFragmentFactory;// ...public class MainActivity extends ReactActivity { // ... @Override protected void onCreate(Bundle savedInstanceState) { getSupportFragmentManager().setFragmentFactory(new RNScreensFragmentFactory()); super.onCreate(savedInstanceState); } // ...}
```

This avoids crashes related to View state not being persisted across Activity restarts.

##### Opting-out of predictive back on Android​

React Navigation doesn't yet support Android's predictive back gesture, so you need to disable it for the system back gesture to work properly.

InAndroidManifest.xml, setandroid:enableOnBackInvokedCallbacktofalsein the<application>tag (or<activity>tag to opt-out at activity level):

```
<application android:enableOnBackInvokedCallback="false" > <!-- ... --></application>
```

### Setting up React Navigation​

When using React Navigation, you configurenavigatorsin your app. Navigators handle transitions between screens and provide UI such as headers, tab bars, etc.

When you use a navigator (such as stack navigator), you'll need to follow that navigator's installation instructions for any additional dependencies.

There are 2 ways to configure navigators:

#### Static configuration​

The static configuration API lets you write your navigation configuration in an object. This reduces boilerplate and simplifies TypeScript types and deep linking. Some aspects can still be changed dynamically.

This is therecommended wayto set up your app. If you need more flexibility later, you can mix and match with the dynamic configuration.

Continue to"Hello React Navigation"to start writing some code with the static API.

#### Dynamic configuration​

The dynamic configuration API lets you write your navigation configuration using React components that can change at runtime based on state or props. This offers more flexibility but requires significantly more boilerplate for TypeScript types, deep linking, etc.

Continue to"Hello React Navigation"to start writing some code with the dynamic API.

- Starter template
- InstallationInstalling dependencies
- Installing dependencies
- Setting up React NavigationStatic configurationDynamic configuration
- Static configuration
- Dynamic configuration