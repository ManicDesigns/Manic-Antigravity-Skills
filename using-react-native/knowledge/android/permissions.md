# Android Permissions

> **Source**: https://developer.android.com/guide/topics/permissions/overview

## Overview

Android permissions protect user privacy by restricting access to sensitive data and system functionality. React Native apps must declare permissions and properly request runtime permissions.

---

## Permission Types

| Type | Description | User Action | Example |
|------|-------------|-------------|---------|
| **Install-time** | Auto-granted at install | None | Internet, Bluetooth |
| **Runtime** | Requested while app running | User prompt | Camera, Location |
| **Special** | Requires system settings | Manual toggle | System alert window |

---

## Declaring Permissions

### AndroidManifest.xml
Located at `android/app/src/main/AndroidManifest.xml`:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- Install-time permissions -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    
    <!-- Runtime permissions -->
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    
    <!-- Notification permission (Android 13+) -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    
    <application>
        ...
    </application>
</manifest>
```

---

## Common Permissions

### Install-time (Granted Automatically)
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
```

### Runtime (Requires User Approval)
```xml
<!-- Camera -->
<uses-permission android:name="android.permission.CAMERA" />

<!-- Location -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />

<!-- Storage (Android 12 and below) -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

<!-- Photos/Media (Android 13+) -->
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
<uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />

<!-- Contacts -->
<uses-permission android:name="android.permission.READ_CONTACTS" />

<!-- Microphone -->
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

---

## React Native Permission Handling

### Installation

```bash
npm install react-native-permissions
```

### iOS (Podfile)
```ruby
# ios/Podfile - Add permissions you need
pod 'Permission-Camera', :path => '../node_modules/react-native-permissions/ios/Camera'
pod 'Permission-PhotoLibrary', :path => '../node_modules/react-native-permissions/ios/PhotoLibrary'
```

### Usage

```typescript
import { check, request, PERMISSIONS, RESULTS } from 'react-native-permissions';
import { Platform } from 'react-native';

// Check permission status
const checkCameraPermission = async () => {
  const permission = Platform.select({
    android: PERMISSIONS.ANDROID.CAMERA,
    ios: PERMISSIONS.IOS.CAMERA,
  });
  
  const result = await check(permission);
  return result;
};

// Request permission
const requestCameraPermission = async () => {
  const permission = Platform.select({
    android: PERMISSIONS.ANDROID.CAMERA,
    ios: PERMISSIONS.IOS.CAMERA,
  });
  
  const result = await request(permission);
  
  switch (result) {
    case RESULTS.GRANTED:
      console.log('Permission granted');
      return true;
    case RESULTS.DENIED:
      console.log('Permission denied');
      return false;
    case RESULTS.BLOCKED:
      console.log('Permission blocked - open settings');
      return false;
  }
};
```

### Permission Results
| Result | Meaning |
|--------|---------|
| `GRANTED` | Permission allowed |
| `DENIED` | Permission denied (can ask again) |
| `BLOCKED` | Permission denied permanently |
| `UNAVAILABLE` | Feature not available on device |
| `LIMITED` | iOS only - limited access |

---

## Location Permissions

### Types
- **Coarse**: Approximate location (city level)
- **Fine**: Precise GPS location
- **Background**: Location while app is in background

### Request Flow
```typescript
import { request, PERMISSIONS } from 'react-native-permissions';

async function requestLocation() {
  // First request foreground location
  const foreground = await request(PERMISSIONS.ANDROID.ACCESS_FINE_LOCATION);
  
  if (foreground === 'granted') {
    // Then request background (if needed)
    const background = await request(
      PERMISSIONS.ANDROID.ACCESS_BACKGROUND_LOCATION
    );
  }
}
```

---

## Notifications (Android 13+)

Android 13+ requires explicit notification permission:

```typescript
import messaging from '@react-native-firebase/messaging';
import { request, PERMISSIONS } from 'react-native-permissions';

async function requestNotificationPermission() {
  // Request permission (Android 13+)
  if (Platform.OS === 'android' && Platform.Version >= 33) {
    await request(PERMISSIONS.ANDROID.POST_NOTIFICATIONS);
  }
  
  // Request FCM permission
  const authStatus = await messaging().requestPermission();
  return authStatus === messaging.AuthorizationStatus.AUTHORIZED;
}
```

---

## Best Practices

### 1. Request Contextually
Request permission when the feature is about to be used, not at app startup.

```typescript
// BAD: Request all permissions on launch
useEffect(() => {
  requestAllPermissions(); // ❌
}, []);

// GOOD: Request when user taps camera button
const onCameraPress = async () => {
  const granted = await requestCameraPermission();
  if (granted) {
    openCamera();
  }
};
```

### 2. Explain Before Requesting
Show rationale before the system dialog:

```typescript
import { Alert } from 'react-native';

const requestWithRationale = async () => {
  Alert.alert(
    'Camera Permission',
    'We need camera access to scan barcodes for product lookup.',
    [
      { text: 'Cancel', style: 'cancel' },
      { 
        text: 'Allow', 
        onPress: () => requestCameraPermission() 
      },
    ]
  );
};
```

### 3. Handle Denial Gracefully
```typescript
import { Linking } from 'react-native';

const openSettings = () => {
  Linking.openSettings();
};

// Show button to open settings if blocked
{permissionBlocked && (
  <Button title="Open Settings" onPress={openSettings} />
)}
```

### 4. Minimize Permissions
Only request what you need. Play Store may reject apps with unnecessary permissions.

---

## Resources
- Android Permissions: https://developer.android.com/guide/topics/permissions
- react-native-permissions: https://github.com/zoontek/react-native-permissions
- Best Practices: https://developer.android.com/training/permissions/usage-notes
