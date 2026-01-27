# React Native Firebase Overview

## React Native Firebase

Welcome to React Native Firebase! To get started, you must first setup a Firebase project and install the "app" module.

React Native Firebase has begun to deprecate the namespaced API (i.e firebase-js-sdk< v9chaining API). React Native Firebase will be moving to the modular API (i.e. firebase-js-sdk>= v9) in the next major release. Seemigration guidefor more information.

React Native Firebase is the officially recommended collection of packages that brings React Native support for all Firebase services on both Android and iOS apps.

React Native Firebase fully supports React Native apps built usingReact Native CLIor usingExpo.

#### Prerequisites

Before getting started, the documentation assumes you are able to create a project with React Native and that you have an active Firebase project.
If you do not meet these prerequisites, follow the links below:

- React Native - Setting up the development environment
- Create a new Firebase project
Additionally, current versions of firebase-ios-sdk have a minimum Xcode requirement of 16.2, which implies a minimum macOS version of 14.5 (macOS Sequoia).

#### Installation for Expo projects

Integration with Expo is possible when using adevelopment build. You can configure the project viaconfig pluginsor manually configure the native projects yourself (the "bare workflow").

NOTE:React Native Firebase cannot be used in the pre-compiledExpo Go appbecause React Native Firebase uses native code that is not compiled into Expo Go.

Warning:If you are usingexpo-dev-client, native crashes (such as those triggered bycrashlytics().crash()) willnotbe reported to Firebase Crashlytics during development. This is becauseexpo-dev-clientprovides a custom error overlay that catches and displays errors before they are sent to Firebase. To test native crash reporting, you must removeexpo-dev-clientand run your app in a standard release or debug build without the custom error overlay.

To create a new Expo project, see theGet startedguide in Expo documentation.

##### Install React Native Firebase modules

To install React Native Firebase's baseappmodule, use the commandnpx expo install @react-native-firebase/app.

Similarly you can install other React Native Firebase modules such as for Authentication and Crashlytics:npx expo install @react-native-firebase/auth @react-native-firebase/crashlytics.

##### Configure React Native Firebase modules

The recommended approach to configure React Native Firebase is to useExpo Config Plugins. You will add React Native Firebase modules to thepluginsarray of yourapp.jsonorapp.config.js. See the note below to determine which modules require Config Plugin configurations.

If you are instead manually adjusting your Android and iOS projects (this is not recommended), follow the same instructions as[React Native CLI projects](#Installation for React Native CLI (non-Expo) projects).

To enable Firebase on the native Android and iOS platforms, create and download Service Account files for each platform from your Firebase project. Then provide paths to the downloadedgoogle-services.jsonandGoogleService-Info.plistfiles in the followingapp.jsonfields:expo.android.googleServicesFileandexpo.ios.googleServicesFile. See the example configuration below.

For iOS only, sincefirebase-ios-sdkrequiresuse_frameworksthen you want to configureexpo-build-propertiesapp.jsonby adding"useFrameworks": "static". See the example configuration below.

The following is an exampleapp.jsonto enable the React Native Firebase modules App, Auth and Crashlytics, that specifies the Service Account files for both mobile platforms, and that sets the application ID to the example value ofcom.mycorp.myapp(change to match your own):

```
{
 "expo": {
 "android": {
 "googleServicesFile": "./google-services.json",
 "package": "com.mycorp.myapp"
 },
 "ios": {
 "googleServicesFile": "./GoogleService-Info.plist",
 "bundleIdentifier": "com.mycorp.myapp"
 },
 "plugins": [
 "@react-native-firebase/app",
 "@react-native-firebase/auth",
 "@react-native-firebase/crashlytics",
 [
 "expo-build-properties",
 {
 "ios": {
 "useFrameworks": "static"
 }
 }
 ]
 ]
 }
}

```

Listing a module in the Config Plugins (the"plugins"array in the JSON above) is only required for React Native Firebase modules that involvenative installation steps- e.g. modifying the Xcode project,Podfile,build.gradle,AndroidManifest.xmletc. React Native Firebase modules without native steps will work out of the box; no"plugins"entry is required. Not all modules have Expo Config Plugins provided yet. A React Native Firebase module has Config Plugin support if it contains anapp.plugin.jsfile in its package directory (e.g.node_modules/@react-native-firebase/app/app.plugin.js).

##### Local app compilation

If you are compiling your app locally, runnpx expo prebuild --cleanto generate the native project directories. Then, follow the local app compilation steps described inLocal app developmentguide in Expo docs. If you prefer using a build service, refer toEAS Build.

Note: if you have already installed an Expo development build (using something likenpx expo runafter doing the--prebuildlocal development steps...) before installing react-native-firebase, then you must uninstall it first as it will not contain the react-native-firebase native modules and you will get errors withRNFBAppModule not foundetc. If so, uninstall the previous development build, do a clean build usingnpx expo prebuild --clean, and then attemptnpx expo run:<platform>again.

##### Expo Tools for VSCode

If you are using theExpo ToolsVSCode extension, the IntelliSense will display a list of available plugins when editing thepluginssection ofapp.json.

#### Installation for React Native CLI (non-Expo) projects

Installing React Native Firebase to a RN CLI project requires a few steps; installing the NPM module, adding the Firebase config files &
rebuilding your application.

##### 1. Install via NPM

Install the React Native Firebase "app" module to the root of your React Native project with NPM or Yarn:

```
# Using npm
npm install --save @react-native-firebase/app

# Using Yarn
yarn add @react-native-firebase/app

```

The@react-native-firebase/appmodule must be installed before using any other Firebase service.

##### 2. React Native CLI - Android Setup

To allow the Android app to securely connect to your Firebase project, a configuration file must be downloaded and added
to your project.

On the Firebase console, add a new Android application and enter your projects details. The "Android package name" must match your
local projects package name which can be found inside of thenamespacefield in/android/app/build.gradle, or in themanifesttag within the/android/app/src/main/AndroidManifest.xmlfile within your project for projects using android gradle plugin v7 and below

The debug signing certificate is optional to use Firebase with your app, but is required for Invites and Phone Authentication.
To generate a certificate runcd android && ./gradlew signingReport. This generates two variant keys.
You have to copyboth'SHA1' and 'SHA-256' keys that belong to the 'debugAndroidTest' variant key option.
Then, you can add those keys to the 'SHA certificate fingerprints' on your app in Firebase console.

Download thegoogle-services.jsonfile and place it inside of your project at the following location:/android/app/google-services.json.

To allow Firebase on Android to use the credentials, thegoogle-servicesplugin must be enabled on the project. This requires modification to two
files in the Android directory.

First, add thegoogle-servicesplugin as a dependency inside of your/android/build.gradlefile:

```
buildscript {
 dependencies {
 // ... other dependencies
 classpath 'com.google.gms:google-services:4.4.4'
 // Add me --- /\
 }
}

```

Lastly, execute the plugin by adding the following to your/android/app/build.gradlefile:

```
apply plugin: 'com.android.application'
apply plugin: 'com.google.gms.google-services' // <- Add this line

```

##### 3. React Native CLI - iOS Setup

To allow the iOS app to securely connect to your Firebase project, a configuration file must be downloaded and added to your project, and you must enable frameworks in CocoaPods

On the Firebase console, add a new iOS application and enter your projects details. The "iOS bundle ID" must match your
local project bundle ID. The bundle ID can be found within the "General" tab when opening the project with Xcode.

Download theGoogleService-Info.plistfile.

Using Xcode, open the projects/ios/{projectName}.xcodeprojfile (or/ios/{projectName}.xcworkspaceif using Pods).

Right click on the project name and "Add files" to the project, as demonstrated below:

Add files via Xcode

Select the downloadedGoogleService-Info.plistfile from your computer, and ensure the "Copy items if needed" checkbox is enabled.

Select 'Copy Items if needed'

To allow Firebase on iOS to use the credentials, the Firebase iOS SDK must be configured during the bootstrap phase of your application.

To do this, open your/ios/{projectName}/AppDelegate.swiftfile and add the following:

At the top of the file, import the Firebase SDK right after'import ReactAppDependencyProvider':

```
import Firebase

```

Within your existingapplicationmethod, add the following to the top of the method:

```
 override func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
 // Add me --- \/
 FirebaseApp.configure()
 // Add me --- /\
 // ...
}

```

To allow Firebase on iOS to use the credentials, the Firebase iOS SDK must be configured during the bootstrap phase of your application.

To do this, open your/ios/{projectName}/AppDelegate.mmfile (orAppDelegate.mif on older react-native), and add the following:

At the top of the file, import the Firebase SDK right after'#import "AppDelegate.h"':

```
#import <Firebase.h>

```

Within your existingdidFinishLaunchingWithOptionsmethod, add the following to the top of the method:

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 // Add me --- \/
 [FIRApp configure];
 // Add me --- /\
 // ...
}

```

Beginning with firebase-ios-sdk v9+ (react-native-firebase v15+) you must tell CocoaPods to use frameworks.

Open the file./ios/Podfileand add this line inside your targets (right before theuse_react_nativeline in current react-native releases that calls the react native Podfile function to get the native modules config):

```
use_frameworks! :linkage => :static

```

To use Static Frameworks on iOS, you also need to manually enable this for the project with the following global to your/ios/Podfilefile:

```
# right after `use_frameworks! :linkage => :static`
$RNFirebaseAsStaticFramework = true

```

Notes: React-Native-Firebase usesuse_frameworks, which has compatibility issues with Flipper & Fabric.

Flipper:use_frameworksisnotcompatible with Flipper. You must disable Flipper by commenting out the:flipper_configurationline in your Podfile. Flipper is deprecated in the react-native community and this will not be fixed - Flipper and react-native-firebase will never work together on iOS.

New Architecture:Fabric is partially compatible withuse_frameworks!. If you enable the bridged / compatibility mode, react-native-firebase will compile correctly and be usable.

##### 4. Autolinking & rebuilding

Once the above steps have been completed, the React Native Firebase library must be linked to your project and your application needs to be rebuilt.

Users on React Native 0.60+ automatically have access to "autolinking",
requiring no further manual installation steps. To automatically link the package, rebuild your project:

```
# Android apps
npx react-native run-android

# iOS apps
cd ios/
pod install --repo-update
cd ..
npx react-native run-ios

```

Once successfully linked and rebuilt, your application will be connected to Firebase using the@react-native-firebase/appmodule. This module does not provide much functionality, therefore to use other Firebase services, each of the modules for the individual Firebase services need installing separately.

#### Other / Web

If you are using the firebase-js-sdk fallback support forweb or "other" platformsthen you must initialize Firebase dynamically by callinginitializeApp.

However, you only want to do this for the web platform. For non-web / native apps the "default" firebase app instance will already be configured by the native google-services.json / GoogleServices-Info.plist files as mentioned above.

At some point during your application's bootstrap processes, initialize firebase like this:

```
import { getApp, initializeApp } from '@react-native-firebase/app';

// web requires dynamic initialization on web prior to using firebase
if (Platform.OS === 'web') {
 const firebaseConfig = {
 // ... config items pasted from firebase console for your web app here
 };

 initializeApp(firebaseConfig);
}

// ...now throughout your app, use firebase APIs normally, for example:
const firebaseApp = getApp();

```

#### Miscellaneous

##### Overriding Native SDK Versions

React Native Firebase internally sets the versions of the native SDKs which each module uses. Each release of the library
is tested against a fixed set of SDK versions (e.g. Firebase SDKs), allowing us to be confident that every feature the
library supports is working as expected.

Sometimes it's required to change these versions to play nicely with other React Native libraries or to work around temporary build failures; therefore we allow
manually overriding these native SDK versions.

Using your own SDK versions is not recommended and not supported as it can lead to unexpected build failures when new react-native-firebase versions are released that expect to use new SDK versions. Proceed with caution and remove these overrides as soon as possible when no longer needed.

Within your projects /android/build.gradle file, provide your own versions by specifying any of the following options shown below:

```
project.ext {
 set('react-native', [
 versions: [
 // Overriding Build/Android SDK Versions if desired
 android : [
 minSdk : 23,
 targetSdk : 33,
 compileSdk: 34,
 ],

 // Overriding Library SDK Versions if desired
 firebase: [
 // Override Firebase SDK Version
 bom : "34.7.0"
 ],
 ],
 ])
}

```

Once changed, rebuild your application withnpx react-native run-android.

Open your projects/ios/Podfileand add any of the globals shown below to the top of the file:

```
# Override Firebase SDK Version if desired
$FirebaseSDKVersion = '12.8.0'

```

Once changed, reinstall your projects pods via pod install and rebuild your project withnpx react-native run-ios.

Alternatively, if you cannot edit the Podfile easily (as when using Expo), you may add the environment variableFIREBASE_SDK_VERSION=12.8.0(or whatever version you need) to the command line that installs pods. For exampleFIREBASE_SDK_VERSION=12.8.0 yarn expo prebuild --clean

##### Android Performance

On Android, React Native Firebase usesthread pool executorto provide improved performance and managed resources.
To increase throughput, you can tune the thread pool executor viafirebase.jsonfile within the root of your project:

```
// <project-root>/firebase.json
{
 "react-native": {
 "android_task_executor_maximum_pool_size": 10,
 "android_task_executor_keep_alive_seconds": 3
 }
}

```