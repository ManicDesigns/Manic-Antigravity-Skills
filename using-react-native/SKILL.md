---
name: using-react-native
description: React Native mobile app development with Expo. Use when building iOS/Android apps, mobile UI, or when user mentions "mobile app", "React Native", "Expo", or cross-platform development.
---

# React Native Mobile Development

Build cross-platform iOS and Android apps with React Native and Expo.

## When to Use This Skill
- User wants to build a mobile app
- User mentions "React Native", "Expo", or "mobile"
- User needs iOS or Android specific guidance
- User asks about app store deployment

## Quick Start

### Create New Project
```bash
npx create-expo-app@latest MyApp
cd MyApp
npx expo start
```

### Run on Device
- Press `i` for iOS Simulator
- Press `a` for Android Emulator
- Scan QR code with Expo Go app for physical device

---

## Project Structure
```
MyApp/
├── app/                 # Expo Router screens (file-based routing)
│   ├── _layout.tsx      # Root layout
│   ├── index.tsx        # Home screen (/)
│   └── (tabs)/          # Tab navigation group
├── components/          # Reusable components
├── constants/           # Colors, config
├── hooks/               # Custom hooks
├── assets/              # Images, fonts
├── app.json             # Expo config
└── package.json
```

---

## Core Dependencies

### Essential
```bash
# Navigation
npx expo install @react-navigation/native @react-navigation/native-stack
npx expo install react-native-screens react-native-safe-area-context

# Firebase
npx expo install @react-native-firebase/app @react-native-firebase/auth
npx expo install @react-native-firebase/firestore @react-native-firebase/messaging

# UI Library (choose one)
npx expo install react-native-paper         # Material Design
npx expo install @gluestack-ui/themed       # Tailwind-style
npx expo install tamagui                    # Cross-platform optimized

# Animations
npx expo install react-native-reanimated
npx expo install lottie-react-native
```

---

## Firebase Setup

### 1. Install Firebase
```bash
npx expo install @react-native-firebase/app
```

### 2. Configure app.json
```json
{
  "expo": {
    "plugins": [
      "@react-native-firebase/app"
    ],
    "android": {
      "googleServicesFile": "./google-services.json"
    },
    "ios": {
      "googleServicesFile": "./GoogleService-Info.plist"
    }
  }
}
```

### 3. Authentication
```typescript
import auth from '@react-native-firebase/auth';

// Sign in
await auth().signInWithEmailAndPassword(email, password);

// Google Sign-In
import { GoogleSignin } from '@react-native-google-signin/google-signin';
const { idToken } = await GoogleSignin.signIn();
const credential = auth.GoogleAuthProvider.credential(idToken);
await auth().signInWithCredential(credential);

// Auth state listener
auth().onAuthStateChanged(user => {
  if (user) console.log('User signed in:', user.uid);
});
```

### 4. Firestore
```typescript
import firestore from '@react-native-firebase/firestore';

// Read
const doc = await firestore().collection('users').doc(userId).get();

// Write
await firestore().collection('users').doc(userId).set({ name: 'John' });

// Real-time listener
firestore().collection('orders').onSnapshot(snapshot => {
  snapshot.docs.forEach(doc => console.log(doc.data()));
});
```

### 5. Push Notifications
```typescript
import messaging from '@react-native-firebase/messaging';

// Request permission
await messaging().requestPermission();

// Get FCM token
const token = await messaging().getToken();

// Handle foreground messages
messaging().onMessage(async remoteMessage => {
  console.log('Notification:', remoteMessage);
});

// Handle background messages
messaging().setBackgroundMessageHandler(async remoteMessage => {
  console.log('Background message:', remoteMessage);
});
```

---

## Navigation Patterns

### Stack Navigation
```typescript
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Details" component={DetailsScreen} />
    </Stack.Navigator>
  );
}
```

### Tab Navigation
```typescript
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

function App() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
}
```

### Expo Router (File-based)
```
app/
├── _layout.tsx          # Root layout
├── index.tsx            # / route
├── profile.tsx          # /profile route
└── (tabs)/
    ├── _layout.tsx      # Tab layout
    ├── home.tsx         # /home tab
    └── settings.tsx     # /settings tab
```

---

## UI Components

### React Native Paper (Material)
```typescript
import { Button, Card, TextInput } from 'react-native-paper';

<Card>
  <Card.Title title="Card Title" />
  <Card.Content>
    <TextInput label="Email" mode="outlined" />
  </Card.Content>
  <Card.Actions>
    <Button mode="contained" onPress={handleSubmit}>Submit</Button>
  </Card.Actions>
</Card>
```

### Gluestack UI
```typescript
import { Box, Button, Text, Input } from '@gluestack-ui/themed';

<Box p="$4" bg="$backgroundLight">
  <Input placeholder="Enter email" />
  <Button action="primary" onPress={handleSubmit}>
    <Text>Submit</Text>
  </Button>
</Box>
```

---

## Platform-Specific Code

### Conditional Rendering
```typescript
import { Platform } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 50 : 30,
    ...Platform.select({
      ios: { shadowColor: 'black' },
      android: { elevation: 4 },
    }),
  },
});
```

### Platform Files
```
Button.ios.tsx      # iOS-specific
Button.android.tsx  # Android-specific
Button.tsx          # Fallback
```

---

## App Store Deployment

### Build with EAS
```bash
# Install EAS CLI
npm install -g eas-cli

# Login
eas login

# Configure
eas build:configure

# Build for stores
eas build --platform ios
eas build --platform android

# Submit to stores
eas submit --platform ios
eas submit --platform android
```

### app.json for Production
```json
{
  "expo": {
    "name": "MyApp",
    "slug": "myapp",
    "version": "1.0.0",
    "ios": {
      "bundleIdentifier": "com.company.myapp",
      "buildNumber": "1"
    },
    "android": {
      "package": "com.company.myapp",
      "versionCode": 1
    }
  }
}
```

---

## Knowledge Files

Detailed documentation in [knowledge/](knowledge/):
- `core/` - Expo and React Native fundamentals
- `firebase/` - Auth, Firestore, FCM integration
- `navigation/` - Navigation patterns
- `ui/` - UI library references
- `patterns/` - Best practices and patterns
