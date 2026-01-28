# Sign in with Apple

> **Source**: https://developer.apple.com/sign-in-with-apple/

## Overview

Sign in with Apple provides fast, private authentication. **Required** for apps that offer third-party social login (Google, Facebook).

---

## Requirements

Apps **must** offer Sign in with Apple if they:
- Have Sign in with Google
- Have Sign in with Facebook
- Have any other third-party social login

**Exceptions**:
- Educational/enterprise apps with existing accounts
- Apps using your company's own account system only
- Government or civic apps

---

## User Experience

### What Users Get
- One-tap sign in with Face ID/Touch ID
- Hide My Email (relay email address)
- No tracking across apps
- Works on all Apple devices

### Button Placement
- Place at top or prominent position among login options
- Use Apple's official button styles
- Same visual weight as other sign-in options

---

## Implementation

### Setup in React Native

```bash
npm install @invertase/react-native-apple-authentication
cd ios && pod install
```

### Enable Capability
1. Xcode → Project → Signing & Capabilities
2. Add "Sign in with Apple" capability

### Basic Usage

```typescript
import { appleAuth } from '@invertase/react-native-apple-authentication';

async function onAppleButtonPress() {
  // Request credentials
  const response = await appleAuth.performRequest({
    requestedOperation: appleAuth.Operation.LOGIN,
    requestedScopes: [
      appleAuth.Scope.EMAIL,
      appleAuth.Scope.FULL_NAME
    ],
  });

  // Verify credential state
  const credentialState = await appleAuth.getCredentialStateForUser(response.user);
  
  if (credentialState === appleAuth.State.AUTHORIZED) {
    // User authenticated
    const { identityToken, nonce, email, fullName, user } = response;
    
    // Send to your backend or Firebase
    console.log('Apple User ID:', user);
    console.log('Email:', email); // May be null after first sign-in
  }
}
```

### Firebase Integration

```typescript
import auth from '@react-native-firebase/auth';
import { appleAuth } from '@invertase/react-native-apple-authentication';

async function signInWithApple() {
  const response = await appleAuth.performRequest({
    requestedOperation: appleAuth.Operation.LOGIN,
    requestedScopes: [appleAuth.Scope.EMAIL, appleAuth.Scope.FULL_NAME],
  });

  // Create Firebase credential
  const credential = auth.AppleAuthProvider.credential(
    response.identityToken,
    response.nonce
  );

  // Sign in to Firebase
  const userCredential = await auth().signInWithCredential(credential);
  return userCredential.user;
}
```

---

## Important Notes

### Email Handling
- Email is only provided on **first** sign-in
- If user chooses "Hide My Email", you get a relay address
- Store the email immediately - you won't get it again

```typescript
// First sign-in
const email = response.email; // "user@icloud.com" or "abc123@privaterelay.appleid.com"

// Subsequent sign-ins
const email = response.email; // null - use stored value
```

### Name Handling
- Full name only provided on first sign-in
- Structure: `{ givenName, familyName, middleName, nickname }`

```typescript
const fullName = response.fullName;
const displayName = `${fullName?.givenName} ${fullName?.familyName}`;
```

### User ID
- `response.user` is stable Apple user identifier
- Use this to link accounts across sign-ins
- Different per developer account

---

## Button Styles

Apple requires specific button styling:

```typescript
import { AppleButton } from '@invertase/react-native-apple-authentication';

<AppleButton
  buttonStyle={AppleButton.Style.BLACK}  // BLACK, WHITE, WHITE_OUTLINE
  buttonType={AppleButton.Type.SIGN_IN}   // SIGN_IN, CONTINUE
  style={{ width: '100%', height: 45 }}
  onPress={onAppleButtonPress}
/>
```

### Style Requirements
- Minimum button height: 30 points (44 recommended)
- Button must say "Sign in with Apple" or "Continue with Apple"
- Use SF Symbols Apple logo
- Match visual weight of other sign-in buttons

---

## Account Deletion

**Required**: If your app allows sign-in with Apple, you must support account deletion.

When deleting account:
1. Delete user data from your systems
2. Revoke Apple token

```typescript
import { appleAuth } from '@invertase/react-native-apple-authentication';

async function deleteAccount() {
  // Get current credentials
  const response = await appleAuth.performRequest({
    requestedOperation: appleAuth.Operation.REFRESH
  });
  
  // Revoke with Apple
  await appleAuth.revokeTokens({
    authorizationCode: response.authorizationCode
  });
  
  // Delete from your backend
  await yourApi.deleteUserAccount();
}
```

---

## Credential State Changes

Listen for account revocation:

```typescript
import { appleAuth } from '@invertase/react-native-apple-authentication';

useEffect(() => {
  const unsubscribe = appleAuth.onCredentialRevoked(() => {
    // User revoked access - sign them out
    signOut();
  });
  return unsubscribe;
}, []);
```

---

## Resources
- Sign in with Apple: https://developer.apple.com/sign-in-with-apple/
- HIG - Sign in with Apple: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
- react-native-apple-authentication: https://github.com/invertase/react-native-apple-authentication
