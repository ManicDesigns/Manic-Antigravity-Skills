# Android Developer & Play Store Guide

## Overview
Google Play Developer account ($25 one-time) is required to:
- Publish apps on Google Play Store
- Access Play Console analytics
- Use internal/closed/open testing tracks
- Access Android beta features

## Enrollment Steps

### 1. Google Account
- Use business Google account
- Recommended: G Suite/Workspace for organizations

### 2. Developer Registration
- Visit https://play.google.com/console/signup
- Pay $25 one-time fee
- Complete identity verification (if required)

### 3. Organization Verification
- May require D-U-N-S Number
- Business documentation
- 2-5 business days

## Google Play Console

### Creating an App
1. Log in at https://play.google.com/console
2. All apps → Create app
3. Fill in:
   - App name
   - Default language
   - App or Game
   - Free or Paid

### Required Assets
- **App Icon**: 512x512px PNG
- **Feature Graphic**: 1024x500px
- **Screenshots**:
  - Phone: 16:9 or 9:16 (min 320px, max 3840px)
  - 7" Tablet: min 1024x500
  - 10" Tablet: min 1024x500
- **Preview Video**: YouTube link (optional)

### Store Listing
- Short description: 80 characters
- Full description: 4000 characters
- What's new: 500 characters

### Release Tracks

| Track | Purpose | Audience |
|-------|---------|----------|
| Internal | Quick testing | 100 testers |
| Closed | Beta with invite | Unlimited |
| Open | Public beta | Anyone can join |
| Production | Live release | All users |

### Content Rating
Required questionnaire covering:
- Violence
- Sexual content
- Profanity
- Gambling
- User-generated content

### Data Safety
Declare:
- Data collected
- Data shared
- Security practices
- Data deletion capability

## Android App Bundle

### Build with EAS
```bash
# Create AAB (Android App Bundle)
eas build --platform android

# Submit to Play Store
eas submit --platform android
```

### Signing
- EAS manages signing keys
- Or provide your own keystore

### app.json Configuration
```json
{
  "expo": {
    "android": {
      "package": "com.company.appname",
      "versionCode": 1,
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#ffffff"
      }
    }
  }
}
```

## Core Android Concepts

### Permissions
```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
```

### Deep Links
```json
{
  "expo": {
    "android": {
      "intentFilters": [
        {
          "action": "VIEW",
          "data": [{ "scheme": "myapp" }],
          "category": ["BROWSABLE", "DEFAULT"]
        }
      ]
    }
  }
}
```

## Resources
- Play Console: https://play.google.com/console
- Android Developers: https://developer.android.com
- Material Design: https://m3.material.io
- Play Store Policies: https://play.google.com/about/developer-content-policy/
