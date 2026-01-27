# Deep Linking

## Deep linking

This guide will describe how to configure your app to handle deep links on various platforms. To handle incoming links, you need to handle 2 scenarios:

- If the app wasn't previously open, the deep link needs to set the initial state
- If the app was already open, the deep link needs to update the state to reflect the incoming link
React Native provides aLinkingto get notified of incoming links. React Navigation can integrate with theLinkingmodule to automatically handle deep links. On Web, React Navigation can integrate with browser'shistoryAPI to handle URLs on client side. Seeconfiguring linksto see more details on how to configure links in React Navigation.

While you don't need to use thelinkingprop from React Navigation, and can handle deep links yourself by using theLinkingAPI and navigating from there, it'll be significantly more complicated than using thelinkingprop which handles many edge cases for you. So we don't recommend implementing it by yourself.

Below, we'll go through required configurations so that the deep link integration works.

### Setting up deep links​

- Expo
- Community CLI

#### Configuring URL scheme​

First, you will want to specify a URL scheme for your app. This corresponds to the string before://in a URL, so if your scheme isexamplethen a link to your app would beexample://. You can register for a scheme in yourapp.jsonby adding a string under the scheme key:

```
{ "expo": { "scheme": "example" }}
```

Next, installexpo-linkingwhich we'd need to get the deep link prefix:

```
npx expo install expo-linking
```

Then you can useLinking.createURLto get the prefix for your app:

```
const linking = { prefixes: [Linking.createURL('/'),};
```

See more details below atConfiguring React Navigation.

It is necessary to useLinking.createURLsince the scheme differs between theExpo Dev Clientand standalone apps.

The scheme specified inapp.jsononly applies to standalone apps. In the Expo client app you can deep link usingexp://ADDRESS:PORT/--/whereADDRESSis often127.0.0.1andPORTis often19000- the URL is printed when you runexpo start. TheLinking.createURLfunction abstracts it out so that you don't need to specify them manually.

If you are using universal links, you need to add your domain to the prefixes as well:

```
const linking = { prefixes: [Linking.createURL('/'), 'https://app.example.com'],};
```

#### Universal Links on iOS​

To set up iOS universal Links in your Expo app, you need to configure yourapp configto include the associated domains and entitlements:

```
{ "expo": { "ios": { "associatedDomains": ["applinks:app.example.com"], "entitlements": { "com.apple.developer.associated-domains": ["applinks:app.example.com"] } } }}
```

You will also need to setupAssociated Domainson your server.

SeeExpo's documentation on iOS Universal Linksfor more details.

#### App Links on Android​

To set up Android App Links in your Expo app, you need to configure yourapp configto include theintentFilters:

```
{ "expo": { "android": { "intentFilters": [ { "action": "VIEW", "autoVerify": true, "data": [ { "scheme": "https", "host": "app.example.com" } ], "category": ["BROWSABLE", "DEFAULT"] } ] } }}
```

You will also need todeclare the associationbetween your website and your intent filters by hosting a Digital Asset Links JSON file.

SeeExpo's documentation on Android App Linksfor more details.

#### Setup on iOS​

Let's configure the native iOS app to open based on theexample://URI scheme.

You'll need to add theLinkingIOSfolder into your header search paths as describedhere. Then you'll need to add the following lines to your orAppDelegate.swiftorAppDelegate.mmfile:

- Swift
- Objective-C

```
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool { return RCTLinkingManager.application(app, open: url, options: options)}
```

```
#import <React/RCTLinkingManager.h>- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options{ return [RCTLinkingManager application:application openURL:url options:options];}
```

If your app is usingUniversal Links, you'll need to add the following code as well:

- Swift
- Objective-C

```
func application( _ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool { return RCTLinkingManager.application( application, continue: userActivity, restorationHandler: restorationHandler ) }
```

```
- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler{ return [RCTLinkingManager application:application continueUserActivity:userActivity restorationHandler:restorationHandler];}
```

Now you need to add the scheme to your project configuration.

The easiest way to do this is with theuri-schemepackage by running the following:

```
npx uri-scheme add example --ios
```

If you want to do it manually, open the project (e.g.SimpleApp/ios/SimpleApp.xcworkspace) in Xcode. Select the project in sidebar and navigate to the info tab. Scroll down to "URL Types" and add one. In the new URL type, set the identifier and the URL scheme to your desired URL scheme.

To make sure Universal Links work in your app, you also need to setupAssociated Domainson your server.

##### Hybrid React Native and native iOS Applications​

If you're using React Navigation within a hybrid app - an iOS app that has both Swift/ObjC and React Native parts - you may be missing theRCTLinkingIOSsubspec in yourPodfile, which is installed by default in new React Native projects. To add this, ensure yourPodfilelooks like the following:

```
 pod 'React', :path => '../node_modules/react-native', :subspecs => [ . . . // other subspecs 'RCTLinkingIOS', . . . ]
```

#### Setup on Android​

To configure the external linking in Android, you can create a new intent in the manifest.

The easiest way to do this is with theuri-schemepackage:npx uri-scheme add example --android.

If you want to add it manually, open upSimpleApp/android/app/src/main/AndroidManifest.xml, and make the following adjustments:

- SetlaunchModeofMainActivitytosingleTaskin order to receive intent on existingMainActivity(this is the default, so you may not need to actually change anything).
- Add the newintent-filterinside theMainActivityentry with aVIEWtype action:

```
<activity android:name=".MainActivity" android:launchMode="singleTask"> <intent-filter> <action android:name="android.intent.action.MAIN" /> <category android:name="android.intent.category.LAUNCHER" /> </intent-filter> <intent-filter> <action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> <data android:scheme="example" /> </intent-filter></activity>
```

Similar to Universal Links on iOS, you can also use a domain to associate the app with your website on Android byverifying Android App Links. First, you need to configure yourAndroidManifest.xml:

- Addandroid:autoVerify="true"to your<intent-filter>entry.
- Add your domain'sschemeandhostin a new<data>entry inside the<intent-filter>.
After adding them, it should look like this:

```
<activity android:name=".MainActivity" android:launchMode="singleTask"> <intent-filter> <action android:name="android.intent.action.MAIN" /> <category android:name="android.intent.category.LAUNCHER" /> </intent-filter> <intent-filter> <action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> <data android:scheme="example" /> </intent-filter> <intent-filter android:autoVerify="true"> <action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> <data android:scheme="http" /> <data android:scheme="https" /> <data android:host="app.example.com" /> </intent-filter></activity>
```

Then, you need todeclare the associationbetween your website and your intent filters by hosting a Digital Asset Links JSON file.

### Configuring React Navigation​

To handle deep links, you need to configure React Navigation to use theschemefor parsing incoming deep links:

- Static
- Dynamic

```
const linking = { prefixes: [ 'example://', // Or `Linking.createURL('/')` for Expo apps ],};function App() { return <Navigation linking={linking} />;}
```

```
const linking = { prefixes: [ 'example://', // Or `Linking.createURL('/')` for Expo apps ],};function App() { return ( <NavigationContainer linking={linking} fallback={<Text>Loading...</Text>}> {/* content */} </NavigationContainer> );}
```

If you are using universal links, you need to add your domain to the prefixes as well:

```
const linking = { prefixes: [ 'example://', // Or `Linking.createURL('/')` for Expo apps 'https://app.example.com', ],};
```

Seeconfiguring linksto see further details on how to configure links in React Navigation.

### Testing deep links​

Before testing deep links, make sure that you rebuild and install the app in your emulator/simulator/device.

If you're testing on iOS, run:

```
npx react-native run-ios
```

If you're testing on Android, run:

```
npx react-native run-android
```

If you're using Expo managed workflow and testing on Expo client, you don't need to rebuild the app. However, you will need to use the correct address and port that's printed when you runexpo start, e.g.exp://127.0.0.1:19000/--/.

If you want to test with your custom scheme in your Expo app, you will need rebuild your standalone app by runningexpo build:ios -t simulatororexpo build:androidand install the resulting binaries.

#### Testing withnpx uri-scheme​

Theuri-schemepackage is a command line tool that can be used to test deep links on both iOS & Android. It can be used as follows:

```
npx uri-scheme open [your deep link] --[ios|android]
```

For example:

```
npx uri-scheme open "example://chat/jane" --ios
```

Or if using Expo client:

```
npx uri-scheme open "exp://127.0.0.1:19000/--/chat/jane" --ios
```

#### Testing withxcrunon iOS​

Thexcruncommand can be used as follows to test deep links with the iOS simulator:

```
xcrun simctl openurl booted [your deep link]
```

For example:

```
xcrun simctl openurl booted "example://chat/jane"
```

#### Testing withadbon Android​

Theadbcommand can be used as follows to test deep links with the Android emulator or a connected device:

```
adb shell am start -W -a android.intent.action.VIEW -d [your deep link] [your android package name]
```

For example:

```
adb shell am start -W -a android.intent.action.VIEW -d "example://chat/jane" com.simpleapp
```

Or if using Expo client:

```
adb shell am start -W -a android.intent.action.VIEW -d "exp://127.0.0.1:19000/--/chat/jane" host.exp.exponent
```

### Integrating with other tools​

In addition to deep links and universal links with React Native'sLinkingAPI, you may also want to integrate other tools for handling incoming links, e.g. Push Notifications - so that tapping on a notification can open the app to a specific screen.

To achieve this, you'd need to override how React Navigation subscribes to incoming links. To do so, you can provide your owngetInitialURLandsubscribefunctions.

Here is an example integration withexpo-notifications:

- Static
- Dynamic

```
const linking = { prefixes: ['example://', 'https://app.example.com'], // Custom function to get the URL which was used to open the app async getInitialURL() { // First, handle deep links const url = await Linking.getInitialURL(); if (url != null) { return url; } // Handle URL from expo push notifications const response = await Notifications.getLastNotificationResponseAsync(); return response?.notification.request.content.data.url; }, // Custom function to subscribe to incoming links subscribe(listener) { // Listen to incoming links for deep links const linkingSubscription = Linking.addEventListener('url', ({ url }) => { listener(url); }); // Listen to expo push notifications when user interacts with them const pushNotificationSubscription = Notifications.addNotificationResponseReceivedListener((response) => { const url = response.notification.request.content.data.url; listener(url); }); return () => { // Clean up the event listeners linkingSubscription.remove(); pushNotificationSubscription.remove(); }; },};
```

```
const linking = { prefixes: ['example://', 'https://app.example.com'], // Custom function to get the URL which was used to open the app async getInitialURL() { // First, handle deep links const url = await Linking.getInitialURL(); if (url != null) { return url; } // Handle URL from expo push notifications const response = await Notifications.getLastNotificationResponseAsync(); return response?.notification.request.content.data.url; }, // Custom function to subscribe to incoming links subscribe(listener) { // Listen to incoming links for deep links const linkingSubscription = Linking.addEventListener('url', ({ url }) => { listener(url); }); // Listen to expo push notifications when user interacts with them const pushNotificationSubscription = Notifications.addNotificationResponseReceivedListener((response) => { const url = response.notification.request.content.data.url; listener(url); }); return () => { // Clean up the event listeners linkingSubscription.remove(); pushNotificationSubscription.remove(); }; }, config: { // Deep link configuration },};
```

Similar to the above example, you can integrate any API that provides a way to get the initial URL and to subscribe to new incoming URLs using thegetInitialURLandsubscribeoptions.

- Setting up deep linksConfiguring URL schemeUniversal Links on iOSApp Links on AndroidSetup on iOSSetup on Android
- Configuring URL scheme
- Universal Links on iOS
- App Links on Android
- Setup on iOS
- Setup on Android
- Configuring React Navigation
- Testing deep linksTesting withnpx uri-schemeTesting withxcrunon iOSTesting withadbon Android
- Testing withnpx uri-scheme
- Testing withxcrunon iOS
- Testing withadbon Android
- Integrating with other tools