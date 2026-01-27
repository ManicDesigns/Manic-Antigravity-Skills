# Firebase Analytics

## Analytics

Installation and getting started with Analytics.

### Installation

This module requires that the@react-native-firebase/appmodule is already setup and installed. To install the "app" module, view theGetting Starteddocumentation.

```
# Install & setup the app module
yarn add @react-native-firebase/app

# Install the analytics module
yarn add @react-native-firebase/analytics

# If you're developing your app using iOS, run this command
cd ios/ && pod install

```

If you're using an older version of React Native without autolinking support, or wish to integrate into an existing project,
you can follow the manual installation steps foriOSandAndroid.

### What does it do

Analytics collects usage and behavior data for your app. Its two primary concerns are:

- Events: What is happening in your app, such as user actions, system events, or errors.
- User properties: Attributes you define to describe segments of your user base, such as language preference or geographic location.
Analytics automatically logs someeventsanduser properties; you don't need to add any code to enable them. However, Analytics also allows you to logcustomorpredefinedevents within your app. How you can do this will be explained below.

### Usage

Analytics offers a wealth ofPredefined Eventsto track user behavior. Analytics also offers folks the ability to logCustom Events. If you're already familiar with Google Analytics, this method is equivalent to using the event command ingtag.js.

#### Event Parameters

Please pay very special attention to what parameters you send in foranyevents - custom, predefined or otherwise.

WARNINGParameters arenotvalidated and incorrect parameters willsilentlybe accepted but thenfail to log an eventin the Analytics console.

It is the developer's responsibility to verify that their parameters are correct and are being logged correctly.

Different event types require different parameters (some require no parameters, some require an array of strings, most require just a string, etc). The developer must examine the reference for each type of event and send the correct parameters. You may watch device logs and the Analytics console to make sure the events are correctly sent to Google Analytics.

#### Custom Events

Below is an example showing how a custom event can be logged. Please be aware that primitive data types or arrays of primitive data types are logged in your Firebase Analytics console.

```
import react, { useEffect } from 'react';
import { View, Button } from 'react-native';
import analytics from '@react-native-firebase/analytics';

function App() {
 return (
 <View>
 <Button
 title="Add To Basket"
 onPress={async () =>
 await analytics().logEvent('basket', {
 id: 3745092,
 item: 'mens grey t-shirt',
 description: ['round neck', 'long sleeved'],
 size: 'L',
 })
 }
 />
 </View>
 );
}

```

#### Predefined Events

To help you get started, Analytics provides a number ofevent methodsthat are common among
different types of apps, including retail and e-commerce, travel, and gaming apps. To learn more about these events and
when to use them, browse theEvents and propertiesarticles in the Firebase Help Center.

Below is a sample of how to use one of the predefined methods the Analytics module provides for you:

```
import react, { useEffect } from 'react';
import { View, Button } from 'react-native';
import analytics from '@react-native-firebase/analytics';

function App() {
 return (
 <View>
 <Button
 title="Press me"
 // Logs in the firebase analytics console as "select_content" event
 // only accepts the two object properties which accept strings.
 onPress={async () =>
 await analytics().logSelectContent({
 content_type: 'clothing',
 item_id: 'abcd',
 })
 }
 />
 </View>
 );
}

```

For a full reference to predefined events and expected parameters, please check out thereference API.

#### Reserved Events

The Analytics package works out of the box, however a number of events are automatically reported to Firebase.
These event names are called as 'Reserved Events'. Attempting to send any custom event using thelogEventmethod
with any of the following event names will throw an error.

#### App instance id

Below is an example showing how to retrieve the app instance id of the application. This will return null on android
if FirebaseAnalytics.ConsentType.ANALYTICS_STORAGE has been set to FirebaseAnalytics.ConsentStatus.DENIED and null on
iOS if ConsentType.analyticsStorage has been set to ConsentStatus.denied.

```
import analytics from '@react-native-firebase/analytics';
// ...
const appInstanceId = await analytics().getAppInstanceId();

```

##### Web / Other platform instance id

Ensure you have installed an Async Storage provider for Firebase to preserve the instance id. Failure to do so means the instance id will be reset every time the application terminates.

The main documentation for "other platform" support containsan example.

### Disable Ad Id usage on iOS

Apple has a strict ban on the usage of Ad Ids ("IDFA") in Kids Category apps. They will not accept any app
in the Kids category if the app accesses the IDFA iOS symbols.

Additionally, apps must implement Apples "App Tracking Transparency" (or "ATT") requirements if they access IDFA symbols.
However, if an app does not use IDFA and otherwise handles data in an ATT-compatible way, it eliminates this ATT requirement.

If you need to avoid IDFA usage while still using analytics, then you needfirebase-ios-sdkv7.11.0 or greater and to define the following variable in your Podfile:

```
$RNFirebaseAnalyticsWithoutAdIdSupport = true

```

Duringpod install, using that variable installs theFirebaseAnalytics/CorePod but not theFirebaseAnalytics/IdentitySupportPod, so you may use Firebase Analytics in Kids Category apps,
or Firebase Analytics without needing the App Tracking Transparency handling (assuming no other parts
of your app handle data in a way that requires ATT)

Note that for obvious reasons, configuring Firebase Analytics for use without IDFA is incompatible with AdMob

### Device Identification

If you would like to enable Firebase Analytics to generate automatic audience metrics for iOS (as it does by default in Android), you must link additional iOS libraries,as documented by the Google Firebase team. Specifically you need to link inAdSupport.framework.

The way to do this using CocoaPods is to add this variable to yourPodfileso@react-native-firebase/analyticswill link it in for you:

```
$RNFirebaseAnalyticsEnableAdSupport = true

```

Note: this setting will have no effect if you disabled Ad IDs as described above, since this setting is specifically linking in theAdSupportframework which requires the Ad IDs.

### firebase.json

#### Disable Auto-Initialization

Analytics can be further configured to disable auto collection of Analytics data. This is useful for opt-in-first
data flows, for example when dealing with GDPR compliance. This is possible by setting the below noted property
on thefirebase.jsonfile at the root of your project directory.

```
// <project-root>/firebase.json
{
 "react-native": {
 "analytics_auto_collection_enabled": false
 }
}

```

To re-enable analytics (e.g. once you have the users consent), call thesetAnalyticsCollectionEnabledmethod:

```
import { firebase } from '@react-native-firebase/analytics';
// ...
await firebase.analytics().setAnalyticsCollectionEnabled(true);

```

To update user's consent (e.g. once you have the users consent), call thesetConsentmethod:

```
import { firebase } from '@react-native-firebase/analytics';
// ...
await firebase.analytics().setConsent({
 analytics_storage: true,
 ad_storage: true,
 ad_user_data: true,
 ad_personalization: true,
});

```

#### Disable screenview tracking

Analytics automatically tracks some information about screens in your application, such as the class name of the UIViewController or Activity that is currently in focus.
Automatic screenview reporting can be turned off/on throughgoogle_analytics_automatic_screen_reporting_enabledproperty offirebase.jsonfile.

```
// <project-root>/firebase.json
{
 "react-native": {
 "google_analytics_automatic_screen_reporting_enabled": false
 }
}

```

### Seeing Events in Firebase Console Realtime View or Analytics DebugView

Events show in the Firebase Console Realtime View within a few seconds of your app sending the events. This is an easy way to verify your events implementation as you develop your application.

However, the Realtime View on Firebase Console offers no way to filter to a specific stream of events so after your app launches your development events will be mixed with all events from your app.

To examine just your development events you will need to use the Analytics DebugView available on the main Google Analytics site for your app as documented in the "Monitor the events in DebugView" section of theGoogle Analytics documentation

Analytics events only show up in DebugView if marked correctly. Follow the instructions below for each platform to mark your events as Debug events.

#### iOS

When running on iOS in debug, events won't be logged by default. If you want to see events in DebugView in the Firebase Console when running debug builds, you'll need tofirst set a flagwhen launching in debug. This flag used to be variously called-FIRAnalyticsDebugEnabledand-FIRDebugEnabled, but please check the previous link.

To always set the flag when running debug builds of your app, you canedit your scheme in Xcodeto always include the flag.

#### Android

When running on Android in debug, events won't be logged by default. If you want to see events in DebugView in the Firebase Console when running debug builds, you'll need to run the following command on the terminaladb shell setprop debug.firebase.analytics.app <package-name>- where<package-name>should be replaced with your app's package name.

#### Other / Web

To mark your events as "Debug" events for platforms using react-native-firebase "other" platform support, you need to set the global debug flagglobalThis.RNFBDebugtotruethen reload the app.

This toggle must be set to the value you want before accessing the analytics instance for the first time, so you should do it as early in your app's bootstrap sequence as possible.

For example, you might modify your index.js file like so:

```
/**
 * @format
 */

import { AppRegistry } from 'react-native';
import App from './App';
import { name as appName } from './app.json';

// \/ Add these lines below
// Enable debug mode for react-native-firebase:
if (__DEV__) globalThis.RNFBDebug = true;
// /\ Add these lines above

AppRegistry.registerComponent(appName, () => App);

```