# Firebase Cloud Messaging

## Cloud Messaging

Installation and getting started with Cloud Messaging.

### Installation

This module requires that the@react-native-firebase/appmodule is already setup and installed. To install the "app" module, view theGetting Starteddocumentation.

```
# Install & setup the app module
yarn add @react-native-firebase/app

# Install the messaging module
yarn add @react-native-firebase/messaging

# If you're developing your app using iOS, run this command
cd ios/ && pod install

```

iOS requires further configuration before you can start receiving and sending
messages through Firebase. Read the documentation on how tosetup iOS with Firebase Cloud Messaging.

Use of thesendMessage()API and it's associated listeners requires a customXMPPserver. Read the documentation on how toMessaging with XMPP.

If you're using an older version of React Native without auto-linking support, or wish to integrate into an existing project,
you can follow the manual installation steps foriOSandAndroid.

### Expo

#### iOS - Notifications entitlement

Since Expo SDK51, Notifications entitlement is no longer always added to iOS projects during prebuild. If your project uses push notifications, you may need to add the aps-environment entitlement to your app config:

```
{
 "expo": {
 "ios": {
 "entitlements": {
 "aps-environment": “production”
 }
 }
 }
}

```

#### iOS - Remote notification

If you requireremote notificationon Expo, you can also add this to your Expoapp.jsonorapp.config.js

```
{
 "expo": {
 "ios": {
 "infoPlist": {
 "UIBackgroundModes": ["remote-notification"]
 }
 }
 }
}

```

#### Android - Google Play Notification Delegation

If you use the REST v1 APIs (used by the Firebase admin SDKs) and your app is running on Android Q+ with current Google Play services, Google implemented "Notification Delegation" for messages. Notification delegation is not currently compatible with react-native-firebase. Specifically, if your notifications are delegated via proxy to Play Services, then your messaging listeners will not be called.

To work around this incompatibility, react-native-firebase disables notification delegation by default currently, using theAndroidManifest.xmlmethod listed as one of the options described here:https://firebase.google.com/docs/cloud-messaging/android/message-priority#proxy.

You may re-enable notification delegation if your use case requires it and you can accept the messaging listener methods not executing for delegated messages by altering the firebase.json settingmessaging_android_notification_delegation_enabledtotrue.

You may also use the new messaging APIs to get and set the notification delegation state for the app, as desired.

### What does it do

React Native Firebase provides native integration of Firebase Cloud Messaging (FCM) for both Android & iOS. FCM is a cost
free service, allowing for server-device and device-device communication. The React Native Firebase Messaging module provides
a simple JavaScript API to interact with FCM.

The module also provides basic support for displaying local notifications, to learn more view theNotificationsdocumentation.

### Usage

#### iOS - Requesting permissions

iOS prevents messages containing notification (or 'alert') payloads from being displayed unless you have received explicit permission from the user.

To learn more about local notifications, view theNotificationsdocumentation.

This module provides arequestPermissionmethod which triggers a native permission dialog requesting the user's permission:

```
import messaging from '@react-native-firebase/messaging';

async function requestUserPermission() {
 const authStatus = await messaging().requestPermission();
 const enabled =
 authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
 authStatus === messaging.AuthorizationStatus.PROVISIONAL;

 if (enabled) {
 console.log('Authorization status:', authStatus);
 }
}

```

The permissions API for iOS provides much more fine-grain control over permissions and how they're handled within your
application. To learn more, view the advancediOS Permissionsdocumentation.

#### Android - Requesting permissions

On Android API level 32 and below, you do not need to request user permission. This method can still be called on Android devices; however, and will always resolve successfully. For API level 33+ you will need to request the permission manually using either the built-in react-nativePermissionsAndroidAPIs or a related module such asreact-native-permissions

```
 import {PermissionsAndroid} from 'react-native';
 PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.POST_NOTIFICATIONS);

```

#### Receiving messages

FCM messages can be sent torealAndroid/iOS devices and Android emulators (iOS simulators however donothandle cloud messages) via a number of methods (see below).
A message is simply a payload of data which can be used however you see fit within your application.

Common use-cases for handling messages could be:

- Displaying a notification (seeNotifications).
- Syncing message data silently on the device (e.g. viaAsyncStorage).
- Updating the application's UI.
To learn about how to send messages to devices from your own server setup, view theServer Integrationdocumentation.

Depending on the devices state, incoming messages are handled differently by the device and module. To understand these
scenarios, it is first important to establish the various states a device can be in:

The user must have opened the app before messages can be received. If the user force quits the app from the device settings, it must be re-opened again before receiving messages.

Depending on the contents of the message, it's important to understand both how the device will handle the message (e.g. display a notification, or even ignore it) and also how the library sends events to your own listeners.

##### Message handlers

The device state and message contents determines which handler will be called:

- In cases where the message is data-only and the device is in the background or quit, both Android & iOS treat the message
as low priority and will ignore it (i.e. no event will be sent). You can however increase the priority by setting theprioritytohigh(Android) andcontent-availabletotrue(iOS) properties on the payload.
In cases where the message is data-only and the device is in the background or quit, both Android & iOS treat the message
as low priority and will ignore it (i.e. no event will be sent). You can however increase the priority by setting theprioritytohigh(Android) andcontent-availabletotrue(iOS) properties on the payload.

- On iOS in cases where the message is data-only and the device is in the background or quit, the message will be delayed
until the background message handler is registered via setBackgroundMessageHandler, signaling the application's javascript
is loaded and ready to run.
On iOS in cases where the message is data-only and the device is in the background or quit, the message will be delayed
until the background message handler is registered via setBackgroundMessageHandler, signaling the application's javascript
is loaded and ready to run.

To learn more about how to send these options in your message payload, view the Firebase documentation for yourFCM API implementation.

##### Notifications

The device state and message contents can also determine whether aNotificationwill be displayed:

##### Foreground state messages

To listen to messages in the foreground, call theonMessagemethod inside of your application code. Code
executed via this handler has access to React context and is able to interact with your application (e.g. updating the state or UI).

For example, the React NativeAlertAPI could be used to display a new Alert
each time a message is delivered'

```
import React, { useEffect } from 'react';
import { Alert } from 'react-native';
import messaging from '@react-native-firebase/messaging';

function App() {
 useEffect(() => {
 const unsubscribe = messaging().onMessage(async remoteMessage => {
 Alert.alert('A new FCM message arrived!', JSON.stringify(remoteMessage));
 });

 return unsubscribe;
 }, []);
}

```

TheremoteMessageproperty contains all of the information about the message sent to the device from FCM, including
any custom data (via thedataproperty) and notification data. To learn more, view theRemoteMessageAPI reference.

If theRemoteMessagepayload contains anotificationproperty when sent to theonMessagehandler, the device
will not show any notification to the user. Instead, you could trigger alocal notificationor update the in-app UI to signal a new notification.

##### Background & Quit state messages

Note: If you use @notifee/react-native, since v7.0.0,onNotificationOpenedAppandgetInitialNotificationwill no longer trigger as notifee will handle the event.

When the application is in a background or quit state, theonMessagehandler will not be called when receiving messages.
Instead, you need to setup a background callback handler via thesetBackgroundMessageHandlermethod.

To setup a background handler, call thesetBackgroundMessageHandleroutside of your application logic as early as possible:

```
// index.js
import { AppRegistry } from 'react-native';
import messaging from '@react-native-firebase/messaging';
import App from './App';

// Register background handler
messaging().setBackgroundMessageHandler(async remoteMessage => {
 console.log('Message handled in the background!', remoteMessage);
});

AppRegistry.registerComponent('app', () => App);

```

The handler must return a promise once your logic has completed to free up device resources. It must not attempt to update
any UI (e.g. via state) - you can however perform network requests, update local storage etc.

TheremoteMessageproperty contains all of the information about the message sent to the device from FCM, including
any custom data via thedataproperty. To learn more, view theRemoteMessageAPI reference.

If theRemoteMessagepayload contains anotificationproperty when sent to thesetBackgroundMessageHandlerhandler, the device
will have displayed anotificationto the user.

When an incoming message is "data-only" (contains nonotificationoption), both Android & iOS regard it as low priority
and will prevent the application from waking (ignoring the message). To allow data-only messages to trigger the background
handler, you must set the "priority" to "high" on Android, and enable thecontent-availableflag on iOS. For example,
if using the Node.jsfirebase-adminpackage to send a message:

```
admin.messaging().sendToDevice(
 [], // device fcm tokens...
 {
 data: {
 owner: JSON.stringify(owner),
 user: JSON.stringify(user),
 picture: JSON.stringify(picture),
 },
 },
 {
 // Required for background/quit data-only messages on iOS
 contentAvailable: true,
 // Required for background/quit data-only messages on Android
 priority: 'high',
 },
);

```

For iOS specific "data-only" messages, the message must include the appropriate APNs headers as well as thecontent-availableflag in order to trigger the background handler. For example, if using the Node.jsfirebase-adminpackage to send a "data-only" message to an iOS device:

```
admin.messaging().send({
 data: {
 //some data
 },
 apns: {
 payload: {
 aps: {
 contentAvailable: true,
 },
 },
 headers: {
 'apns-push-type': 'background',
 'apns-priority': '5',
 'apns-topic': '', // your app bundle identifier
 },
 },
 //must include token, topic, or condition
 //token: //device token
 //topic: //notification topic
 //condition: //notification condition
});

```

View theSending Notification Requests to APNsdocumentation to learn more about APNs headers.

These options can be applied to all FCM messages. View theServer Integrationdocumentation
to learn more about other available SDKs.

Although the library supports handling messages in background/quit states, the underlying implementation on how this works is different on Android & iOS.

On Android, aHeadless JStask (an Android only feature) is created that runs separately to your main React component; allowing your background handler code to run without mounting your root component.

On iOS however, when a message is received the device silently starts your application in a background state. At this point, your background handler (viasetBackgroundMessageHandler) is triggered, but your root React component also gets mounted. This can be problematic for some users since any side-effects will be called inside of your app (e.g.useEffects, analytics events/triggers etc). To get around this problem,
you can configure yourAppDelegate.mfile (see instructions below) to inject aisHeadlessprop into your root component. Use this property to conditionally rendernull("nothing") if your app is launched in the background:

```
// index.js
import { AppRegistry } from 'react-native';
import messaging from '@react-native-firebase/messaging';

// Handle background messages using setBackgroundMessageHandler
messaging().setBackgroundMessageHandler(async remoteMessage => {
 console.log('Message handled in the background!', remoteMessage);
});

// Check if app was launched in the background and conditionally render null if so
function HeadlessCheck({ isHeadless }) {
 if (isHeadless) {
 // App has been launched in the background by iOS, ignore
 return null;
 }

 // Render the app component on foreground launch
 return <App />;
}

// Your main application component defined here
function App() {
 // Your application
}

AppRegistry.registerComponent('app', () => HeadlessCheck);

```

To inject aisHeadlessprop into your app, please update yourAppDelegate.mfile as instructed below:

```
// add this import statement at the top of your `AppDelegate.m` file
#import "RNFBMessagingModule.h"

// in "(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions" method
// Use `addCustomPropsToUserProps` to pass in props for initialization of your app
// Or pass in `nil` if you have none as per below example
// For `withLaunchOptions` please pass in `launchOptions` object
// and use it to set `self.initialProps` (available with react-native >= 0.71.1, older versions need a more difficult style, upgrading is recommended)

self.initialProps = [RNFBMessagingModule addCustomPropsToUserProps:nil withLaunchOptions:launchOptions];

```

- For projects that use react-native-navigation (or if you just don't want to mess with your launchProperties) you can use thegetIsHeadlessmethod (iOS only) from messaging like so:

```
messaging()
 .getIsHeadless()
 .then(isHeadless => {
 // do sth with isHeadless
 });

```

On Android, theisHeadlessprop will not exist.

On iOS devices, the user is able to toggle Background App Refresh in device's Settings. Furthermore, the Background App Refresh setting will automatically be off if the device is in low power mode.

If the iOS Background App Refresh mode is off, your handler configured insetBackgroundMessageHandlerwill not be triggered.

##### Topics

Topics are a mechanism which allow a device to subscribe and unsubscribe from named PubSub channels, all managed via FCM.
Rather than sending a message to a specific device by FCM token, you can instead send a message to a topic and any
devices subscribed to that topic will receive the message.

Topics allow you to simplify FCMserver integrationas you do not need to keep a store of
device tokens. There are however some things to keep in mind about topics:

- Messages sent to topics should not contain sensitive or private information. Do not create a topic for a specific user
to subscribe to.
- Topic messaging supports unlimited subscriptions for each topic.
- One app instance can be subscribed to no more than 2000 topics.
- The frequency of new subscriptions is rate-limited per project. If you send too many subscription requests in a short
period of time, FCM servers will respond with a 429 RESOURCE_EXHAUSTED ("quota exceeded") response. Retry with exponential backoff.
- A server integration can send a single message to multiple topics at once. This however is limited to 5 topics.
To learn more about how to send messages to devices subscribed to topics, view theSend messages to topicsdocumentation.

To subscribe a device, call thesubscribeToTopicmethod with the topic name (must not include "/"):

```
messaging()
 .subscribeToTopic('weather')
 .then(() => console.log('Subscribed to topic!'));

```

To unsubscribe from a topic, call theunsubscribeFromTopicmethod with the topic name:

```
messaging()
 .unsubscribeFromTopic('weather')
 .then(() => console.log('Unsubscribed fom the topic!'));

```

### firebase.json

Messaging can be further configured to provide more control over how FCM is handled internally within your application.

#### Auto Registration (iOS)

React Native Firebase Messaging automatically registers the device with APNs to receive remote messages. If you need
to manually control registration you can disable this via thefirebase.jsonfile:

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "messaging_ios_auto_register_for_remote_messages": false
 }
}

```

Once auto-registration is disabled you must manually callregisterDeviceForRemoteMessagesin your JavaScript code as
early as possible in your application startup;

```
import messaging from '@react-native-firebase/messaging';

async function registerAppWithFCM() {
 await messaging().registerDeviceForRemoteMessages();
}

```

#### Foreground Presentation Options (iOS)

React Native Firebase Messaging configures how to present a notification in a foreground app.
Refer toUNNotificationPresentationOptionsfor the details.

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "messaging_ios_foreground_presentation_options": ["badge", "sound", "list", "banner"]
 }
}

```

#### Auto initialization

Firebase generates an Instance ID, which FCM uses to generate a registration token and which Analytics uses for data collection.
When an Instance ID is generated, the library will upload the identifier and configuration data to Firebase. In most cases,
you do not need to change this behavior.

If you prefer to prevent Instance ID auto-generation, disable auto initialization for FCM and Analytics:

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "analytics_auto_collection_enabled": false,
 "messaging_auto_init_enabled": false
 }
}

```

To re-enable initialization (e.g. once requested permission) call themessaging().setAutoInitEnabled(true)method.

#### Background handler timeout (Android)

On Android, a background event sent tosetBackgroundMessageHandlerhas 60 seconds to resolve before it is automatically
canceled to free up device resources. If you wish to override this value, set the number of milliseconds in your config:

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "messaging_android_headless_task_timeout": 30000
 }
}

```

#### Notification Channel ID

On Android, any message which displays aNotificationuse a default Notification Channel
(created by FCM called "Miscellaneous"). This channel contains basic notification settings which may not be appropriate for
your application. You can change what Channel is used by updating themessaging_android_notification_channel_idproperty:

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "messaging_android_notification_channel_id": "high-priority"
 }
}

```

Creating and managing Channels is outside of the scope of the React Native Firebase library, however external libraries
such asNotifeecan provide such functionality.

#### Notification Color

On Android, any messages which display aNotificationdo not use a color to tint the content
(such as the small icon, title etc). To provide a custom tint color, update themessaging_android_notification_colorproperty
with a Android color resource name.

The library provides a set ofpredefined colorscorresponding to theHTML colorsfor convenience, for example:

```
// <projectRoot>/firebase.json
{
 "react-native": {
 "messaging_android_notification_color": "@color/hotpink"
 }
}

```

Note that only predefined colors can be used infirebase.json. If you want to use a custom color defined in your application resources, then you should set it in theAndroidManifest.xmlinstead.

```
<!-- <projectRoot>/android/app/src/main/res/values/colors.xml -->
<resources>
 <color name="my_custom_color">#123456</color>
</resources>

<!-- <projectRoot>/android/app/src/main/AndroidManifest.xml -->

<!-- add "tools" to manifest tag -->
<manifest xmlns:tools="http://schemas.android.com/tools">
 <application>
 <!-- ... -->

 <meta-data
 android:name="com.google.firebase.messaging.default_notification_color"
 android:resource="@color/my_custom_color"
 tools:replace="android:resource" />
 </application>
</manifest>

```