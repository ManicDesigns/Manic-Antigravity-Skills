# Google Sign-In for Android

> **Source**: https://developers.google.com/identity/sign-in/android

## Overview

Google Sign-In enables one-tap authentication using users' Google accounts. Uses the modern Credential Manager API.

---

## Implementation Options

| Method | Use Case |
|--------|----------|
| **Firebase Auth** | Full auth stack with backend |
| **Credential Manager** | Native Google-only auth |
| **Expo Auth Session** | Expo managed workflow |

---

## Firebase Authentication (Recommended)

### Installation

```bash
npm install @react-native-google-signin/google-signin
npm install @react-native-firebase/auth
cd ios && pod install
```

### Configure

1. **Firebase Console**: Enable Google Sign-In provider
2. **Download config files**:
   - `google-services.json` → `android/app/`
   - `GoogleService-Info.plist` → `ios/`

3. **Get Web Client ID** from Firebase Console → Authentication → Sign-in method → Google

### Code

```typescript
import { GoogleSignin, statusCodes } from '@react-native-google-signin/google-signin';
import auth from '@react-native-firebase/auth';

// Configure on app start
GoogleSignin.configure({
  webClientId: 'YOUR_WEB_CLIENT_ID.apps.googleusercontent.com',
  offlineAccess: true,
});

async function signInWithGoogle() {
  try {
    // Check Play Services
    await GoogleSignin.hasPlayServices({ showPlayServicesUpdateDialog: true });
    
    // Sign in
    const { idToken } = await GoogleSignin.signIn();
    
    // Create Firebase credential
    const credential = auth.GoogleAuthProvider.credential(idToken);
    
    // Sign in to Firebase
    const userCredential = await auth().signInWithCredential(credential);
    
    return userCredential.user;
  } catch (error) {
    if (error.code === statusCodes.SIGN_IN_CANCELLED) {
      console.log('User cancelled');
    } else if (error.code === statusCodes.IN_PROGRESS) {
      console.log('Sign in already in progress');
    } else if (error.code === statusCodes.PLAY_SERVICES_NOT_AVAILABLE) {
      console.log('Play Services not available');
    } else {
      console.error('Sign in error:', error);
    }
    throw error;
  }
}
```

---

## Sign Out

```typescript
async function signOut() {
  try {
    // Sign out from Google
    await GoogleSignin.signOut();
    
    // Sign out from Firebase
    await auth().signOut();
  } catch (error) {
    console.error('Sign out error:', error);
  }
}
```

---

## Get User Info

```typescript
async function getCurrentUser() {
  const currentUser = await GoogleSignin.getCurrentUser();
  
  if (currentUser) {
    return {
      id: currentUser.user.id,
      email: currentUser.user.email,
      name: currentUser.user.name,
      photo: currentUser.user.photo,
    };
  }
  
  return null;
}
```

---

## Android Configuration

### android/app/build.gradle
```gradle
apply plugin: 'com.google.gms.google-services'

dependencies {
    implementation platform('com.google.firebase:firebase-bom:32.0.0')
    implementation 'com.google.android.gms:play-services-auth:20.5.0'
}
```

### android/build.gradle
```gradle
buildscript {
    dependencies {
        classpath 'com.google.gms:google-services:4.3.15'
    }
}
```

### SHA-1 Fingerprint
Required for Google Sign-In:

```bash
# Debug
keytool -list -v -alias androiddebugkey -keystore ~/.android/debug.keystore -storepass android

# Release
keytool -list -v -alias your-key-alias -keystore /path/to/your.keystore
```

Add SHA-1 to Firebase Console → Project Settings → Your Apps → Android

---

## One Tap Sign-In

Streamlined sign-in for returning users:

```typescript
import { GoogleOneTapSignIn } from '@react-native-google-signin/google-signin';

async function oneTapSignIn() {
  try {
    const { idToken, user } = await GoogleOneTapSignIn.signIn({
      webClientId: 'YOUR_WEB_CLIENT_ID.apps.googleusercontent.com',
      nonce: generateNonce(), // Optional: for added security
    });
    
    // Use with Firebase
    const credential = auth.GoogleAuthProvider.credential(idToken);
    await auth().signInWithCredential(credential);
  } catch (error) {
    // Fall back to regular sign in
    await signInWithGoogle();
  }
}
```

---

## Expo Implementation

### Installation
```bash
npx expo install expo-auth-session expo-crypto
```

### Code
```typescript
import * as Google from 'expo-auth-session/providers/google';
import * as WebBrowser from 'expo-web-browser';

WebBrowser.maybeCompleteAuthSession();

function useGoogleAuth() {
  const [request, response, promptAsync] = Google.useAuthRequest({
    androidClientId: 'YOUR_ANDROID_CLIENT_ID',
    iosClientId: 'YOUR_IOS_CLIENT_ID',
    webClientId: 'YOUR_WEB_CLIENT_ID',
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { authentication } = response;
      // Use authentication.accessToken
    }
  }, [response]);

  return {
    signIn: () => promptAsync(),
    isLoading: !request,
  };
}
```

---

## Button Styling

Use Google's branding guidelines:

```tsx
import { GoogleSigninButton } from '@react-native-google-signin/google-signin';

<GoogleSigninButton
  style={{ width: 312, height: 48 }}
  size={GoogleSigninButton.Size.Wide}
  color={GoogleSigninButton.Color.Dark}
  onPress={signInWithGoogle}
/>
```

Or custom button following brand guidelines:
- Use official Google "G" logo
- Text: "Sign in with Google"
- Minimum height: 40dp
- White or dark backgrounds only

---

## Silent Sign-In

Check if user is already signed in:

```typescript
async function checkSilentSignIn() {
  try {
    const isSignedIn = await GoogleSignin.isSignedIn();
    
    if (isSignedIn) {
      // Get tokens silently
      const tokens = await GoogleSignin.getTokens();
      
      // Re-authenticate with Firebase
      const credential = auth.GoogleAuthProvider.credential(tokens.idToken);
      await auth().signInWithCredential(credential);
      
      return true;
    }
  } catch (error) {
    console.log('Silent sign-in failed');
  }
  return false;
}
```

---

## Resources
- Google Sign-In: https://developers.google.com/identity/sign-in/android
- react-native-google-signin: https://github.com/react-native-google-signin/google-signin
- Firebase Auth: https://firebase.google.com/docs/auth/android/google-signin
