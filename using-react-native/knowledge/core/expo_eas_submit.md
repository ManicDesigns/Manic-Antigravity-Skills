# EAS Submit to App Stores

## EAS Submit

Edit page

Copy page

EAS Submit is a hosted service for submitting Android and iOS app binaries to the Google Play Store and Apple App Store from the command line.

Edit page

Copy page

EAS Submitis a hosted service from EAS (Expo Application Services) for submitting Android and iOS binaries directly to the Google Play Store and Apple App Store without opening theGoogle Play Console, or downloading theTransporter app.

EAS Submit automates the final step of mobile app distribution by sending your built binaries to Google and Apple for store review. It removes the need for manual uploads and reduces errors that happen during store submission. It also allows developers using Windows and Linux to upload iOS builds, since this is only supported on macOS machines.

EAS Submit works with apps built withEAS Buildor locally and supports multiple submission profiles. You can trigger a submission from a CLI command, after a build is finished, or from a CI/CD service. This gives teams a faster, more consistent release workflow across both platforms.

### Quick start

Submit an Android build:

Copy

Submit an iOS build:

Copy

Build and submit in one step:

Copy

### How EAS Submit works

EAS Submitdelivers your app to the app stores' distribution pipelines (a chosen track on Google Play Store orTestFlightfor iOS), following thedefault submission behavior for app stores. It queues up your app for distribution on the Google Play Console and App Store Connect, and then you can log into those sites to send your apps off to review, so then they can be distributed to your users.

#### Android (Google Play Store)

- Where it goes: EAS Submit uploads the build to Google Play Console.
- What happens then: The build is placed in the track you specify (internal, alpha, beta, or production).
- First-time submissions: Google requires you to upload your app manually at least once before API-based submissions work.
- Does this mean production?If you use internal, alpha, or beta, the app is only available to testers in that track.If you explicitly choose production, then yes â once Google approves the release, it will be available to all users.
- If you use internal, alpha, or beta, the app is only available to testers in that track.
- If you explicitly choose production, then yes â once Google approves the release, it will be available to all users.

#### iOS (App Store Connect/TestFlight)

- Where it goes: EAS Submit uploads the build to App Store Connect.
- What happens then: The build becomes available in TestFlight.
- Does this mean production? No â a TestFlight build is not automatically released to the Apple App Store.
- How production happens: You must log into App Store Connect, fill in all the metadata, security questionnaire and upload app screenshots, then choose the build, and submit it for App Review before it can be released to production.

### When to use EAS Submit

### Frequently asked questions (FAQ)

Yes. EAS Submit accepts any valid.aab(Android App Bundle) or.ipa(iOS App Archive) file.

For builds created with EAS Build, runeas submitand select a build from the list or let it use the latest build automatically.

For local builds, use the--pathflag to specify the binary:

The binary must be correctly signed. For Android, this means a release keystore. For iOS, this means a distribution certificate and provisioning profile.

Yes. All iOS submissions through EAS Submit are uploaded to App Store Connect and appear in TestFlight after processing. Processing typically takes 10-15 minutes but can vary.

Once processed, you can distribute the build to internal testers immediately or add external testers after a brief Beta App Review. To release to the App Store, you must manually submit the build for App Review through App Store Connect.

Yes. EAS Submit works in CI environments and integrates withEAS Workflows. You can add a submit job to your workflow configuration. For example:

```
jobs:
 submit_ios_to_store:
 type: submit
 params:
 platform: ios
 after:
 - build_ios

```

For more information, seeEAS Workflows pre-packaged jobs.

For CI pipelines, you can also use the--non-interactiveflag to skip prompts and--latestto automatically select the most recent build:

Copy

EAS Submit uploads your binary but does not manage store listing metadata, screenshots, or release notes.

For Google Play Store, configure your store listing directly inGoogle Play Consolebefore submitting.

For Apple App Store, you can useEAS Metadatato automate app information and localized descriptions.

For Android, you need aGoogle Service Account Keywith access to your app in Google Play Console. Your app must be uploaded manually at least once before API submissions work.

For iOS, you need an Apple Developer account. EAS Submit requires yourascAppId(App Store Connect app ID) and will prompt for your Apple ID credentials or use an App Store Connect API Key if configured.

For more information, seeGoogle's Play Store's prerequisitesandApple's App Store prerequisites.

To understand why your EAS Submit submission failed, open the submission details page in theEAS dashboard:

- Use the logs provided on the submission details page to understand the error.
- Look for"Build Annotations" bubbleif there is one. These highlight common failure reasons and suggested fixes directly in the logs.

### Get started

Learn how to submit an Android app to the Google Play Store.

Learn how to submit an iOS/iPadOS app to the Apple App Store.

See how to configure your submissions with eas.json.