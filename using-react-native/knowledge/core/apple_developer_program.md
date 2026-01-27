# Apple Developer Program Guide

## Overview
The Apple Developer Program ($99/year) is required to:
- Distribute apps on the App Store
- Access beta OS releases
- Use TestFlight for testing
- Access App Store Connect analytics

## Enrollment Steps

### 1. Apple ID
- Create/use Apple ID at https://appleid.apple.com
- Enable two-factor authentication

### 2. Enroll
- Visit https://developer.apple.com/programs/enroll/
- Choose Individual or Organization
- Pay $99/year fee

### 3. Organization Requirements
For businesses:
- D-U-N-S Number (free from Dun & Bradstreet)
- Legal entity name must match
- Legal signing authority required

## App Store Connect

### Creating an App
1. Log in at https://appstoreconnect.apple.com
2. My Apps → New App
3. Fill in:
   - Platform: iOS
   - App Name (30 characters max)
   - Bundle ID (from Xcode)
   - SKU (unique identifier)

### Required Assets
- **App Icon**: 1024x1024px PNG
- **Screenshots**: 
  - 6.5" (1284x2778) - iPhone
  - 5.5" (1242x2208) - iPhone
  - 12.9" (2048x2732) - iPad
- **Preview Videos**: Optional, 15-30 seconds

### App Review Guidelines
Key areas to comply with:
- Safety (no objectionable content)
- Performance (complete, bug-free)
- Business (clear pricing, no scams)
- Design (follows HIG)
- Legal (privacy policy required)

### Submission Checklist
- [ ] App binary uploaded via Xcode/EAS
- [ ] App description and keywords
- [ ] Support URL
- [ ] Privacy policy URL
- [ ] Age rating questionnaire
- [ ] App review notes (demo account if needed)

## TestFlight

### Internal Testing
- Up to 100 internal testers
- No review required
- Immediate access

### External Testing
- Up to 10,000 testers
- Requires beta review (24-48 hours)
- Public link available

```bash
# Upload with EAS
eas build --platform ios
eas submit --platform ios
```

## Resources
- Developer Portal: https://developer.apple.com
- App Store Connect: https://appstoreconnect.apple.com
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- App Store Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
