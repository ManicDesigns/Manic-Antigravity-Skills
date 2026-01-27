# Stack Navigator

## Native Stack Navigator

Native Stack Navigator provides a way for your app to transition between screens where each new screen is placed on top of a stack.

This navigator uses the native APIsUINavigationControlleron iOS andFragmenton Android so that navigation built withcreateNativeStackNavigatorwill behave exactly the same and have the same performance characteristics as apps built natively on top of those APIs. It also offers basic Web support usingreact-native-web.

One thing to keep in mind is that while@react-navigation/native-stackoffers native performance and exposes native features such as large title on iOS etc., it may not be as customizable as@react-navigation/stackdepending on your needs. So if you need more customization than what's possible in this navigator, consider using@react-navigation/stackinstead - which is a more customizable JavaScript based implementation.

### Installation​

To use this navigator, ensure that you have@react-navigation/nativeand its dependencies (follow this guide), then install@react-navigation/native-stack:

- npm
- yarn
- pnpm
- bun

```
npm install @react-navigation/native-stack
```

```
yarn add @react-navigation/native-stack
```

```
pnpm add @react-navigation/native-stack
```

```
bun add @react-navigation/native-stack
```

### Usage​

To use this navigator, import it from@react-navigation/native-stack:

- Static
- Dynamic

```
import { createNativeStackNavigator } from '@react-navigation/native-stack';const MyStack = createNativeStackNavigator({ screens: { Home: HomeScreen, Profile: ProfileScreen, },});
```

```
import { createNativeStackNavigator } from '@react-navigation/native-stack';const Stack = createNativeStackNavigator();function MyStack() { return ( <Stack.Navigator> <Stack.Screen name="Home" component={HomeScreen} /> <Stack.Screen name="Profile" component={ProfileScreen} /> </Stack.Navigator> );}
```

If you encounter any bugs while usingcreateNativeStackNavigator, please open issues onreact-native-screensrather than thereact-navigationrepository!

### API Definition​

#### Props​

The native stack navigator accepts thecommon propsshared by all navigators.

#### Options​

The followingoptionscan be used to configure the screens in the navigator:

##### title​

String that can be used as a fallback forheaderTitle.

##### statusBarAnimation​

Sets the status bar animation (similar to theStatusBarcomponent). Defaults tofadeon iOS andnoneon Android.

Supported values:

- "fade"
- "none"
- "slide"
On Android, setting eitherfadeorslidewill set the transition of status bar color. On iOS, this option applies to the appereance animation of the status bar.

Requires settingView controller-based status bar appearance -> YES(or removing the config) in yourInfo.plistfile.

Only supported on Android and iOS.

##### statusBarHidden​

Whether the status bar should be hidden on this screen.

Requires settingView controller-based status bar appearance -> YES(or removing the config) in yourInfo.plistfile.

Only supported on Android and iOS.

##### statusBarStyle​

Sets the status bar color (similar to theStatusBarcomponent).

Supported values:

- "auto"(iOS only)
- "inverted"(iOS only)
- "dark"
- "light"
Defaults toautoon iOS andlighton Android.

Requires settingView controller-based status bar appearance -> YES(or removing the config) in yourInfo.plistfile.

Only supported on Android and iOS.

##### statusBarBackgroundColor​

This option is deprecated and will be removed in a future release (for apps targeting Android SDK 35 or above edge-to-edge mode is enabled by default
and it is expected that the edge-to-edge will be enforced in future SDKs, seeherefor more information).

Sets the background color of the status bar (similar to theStatusBarcomponent).

Only supported on Android.

##### statusBarTranslucent​

This option is deprecated and will be removed in a future release (for apps targeting Android SDK 35 or above edge-to-edge mode is enabled by default
and it is expected that the edge-to-edge will be enforced in future SDKs, seeherefor more information).

Sets the translucency of the status bar (similar to theStatusBarcomponent). Defaults tofalse.

Only supported on Android.

##### contentStyle​

Style object for the scene content.

##### animationMatchesGesture​

Whether the gesture to dismiss should use animation provided toanimationprop. Defaults tofalse.

Doesn't affect the behavior of screens presented modally.

Only supported on iOS.

##### fullScreenGestureEnabled​

Whether the gesture to dismiss should work on the whole screen. Using gesture to dismiss with this option results in the same transition animation assimple_push. This behavior can be changed by settingcustomAnimationOnGestureprop. Achieving the default iOS animation isn't possible due to platform limitations. Defaults tofalse.

Doesn't affect the behavior of screens presented modally.

Only supported on iOS.

##### fullScreenGestureShadowEnabled​

Whether the full screen dismiss gesture has shadow under view during transition. Defaults totrue.

This does not affect the behavior of transitions that don't use gestures enabled byfullScreenGestureEnabledprop.

##### gestureEnabled​

Whether you can use gestures to dismiss this screen. Defaults totrue. Only supported on iOS.

##### animationTypeForReplace​

The type of animation to use when this screen replaces another screen. Defaults topush.

Supported values:

- push: the new screen will perform push animation.
push: the new screen will perform push animation.

- pop: the new screen will perform pop animation.
pop: the new screen will perform pop animation.

##### animation​

How the screen should animate when pushed or popped.

Only supported on Android and iOS.

Supported values:

- default: use the platform default animation
default: use the platform default animation

- fade: fade screen in or out
fade: fade screen in or out

- fade_from_bottom: fade the new screen from bottom
fade_from_bottom: fade the new screen from bottom

- flip: flip the screen, requirespresentation: "modal"(iOS only)
flip: flip the screen, requirespresentation: "modal"(iOS only)

- simple_push: default animation, but without shadow and native header transition (iOS only, uses default animation on Android)
simple_push: default animation, but without shadow and native header transition (iOS only, uses default animation on Android)

- slide_from_bottom: slide in the new screen from bottom
slide_from_bottom: slide in the new screen from bottom

- slide_from_right: slide in the new screen from right (Android only, uses default animation on iOS)
slide_from_right: slide in the new screen from right (Android only, uses default animation on iOS)

- slide_from_left: slide in the new screen from left (Android only, uses default animation on iOS)
slide_from_left: slide in the new screen from left (Android only, uses default animation on iOS)

- none: don't animate the screen
none: don't animate the screen

##### presentation​

How should the screen be presented.

Only supported on Android and iOS.

Supported values:

- card: the new screen will be pushed onto a stack, which means the default animation will be slide from the side on iOS, the animation on Android will vary depending on the OS version and theme.
card: the new screen will be pushed onto a stack, which means the default animation will be slide from the side on iOS, the animation on Android will vary depending on the OS version and theme.

- modal: the new screen will be presented modally. this also allows for a nested stack to be rendered inside the screen.
modal: the new screen will be presented modally. this also allows for a nested stack to be rendered inside the screen.

- transparentModal: the new screen will be presented modally, but in addition, the previous screen will stay so that the content below can still be seen if the screen has translucent background.
transparentModal: the new screen will be presented modally, but in addition, the previous screen will stay so that the content below can still be seen if the screen has translucent background.

- containedModal: will use "UIModalPresentationCurrentContext" modal style on iOS and will fallback to "modal" on Android.
containedModal: will use "UIModalPresentationCurrentContext" modal style on iOS and will fallback to "modal" on Android.

- containedTransparentModal: will use "UIModalPresentationOverCurrentContext" modal style on iOS and will fallback to "transparentModal" on Android.
containedTransparentModal: will use "UIModalPresentationOverCurrentContext" modal style on iOS and will fallback to "transparentModal" on Android.

- fullScreenModal: will use "UIModalPresentationFullScreen" modal style on iOS and will fallback to "modal" on Android. A screen using this presentation style can't be dismissed by gesture.
fullScreenModal: will use "UIModalPresentationFullScreen" modal style on iOS and will fallback to "modal" on Android. A screen using this presentation style can't be dismissed by gesture.

- formSheet: will use "BottomSheetBehavior" on Android and "UIModalPresentationFormSheet" modal style on iOS.
formSheet: will use "BottomSheetBehavior" on Android and "UIModalPresentationFormSheet" modal style on iOS.

To use Form Sheet for your screen, addpresentation: 'formSheet'to theoptions.

- Static
- Dynamic

```
import { createNativeStackNavigator } from '@react-navigation/native-stack';const MyStack = createNativeStackNavigator({ screens: { Home: { screen: HomeScreen, }, Profile: { screen: ProfileScreen, options: { presentation: 'formSheet', headerShown: false, sheetAllowedDetents: 'fitToContents', }, }, },});
```

```
import { createNativeStackNavigator } from '@react-navigation/native-stack';const Stack = createNativeStackNavigator();function MyStack() { return ( <Stack.Navigator> <Stack.Screen name="Home" component={HomeScreen} /> <Stack.Screen name="Profile" component={ProfileScreen} options={{ presentation: 'formSheet', headerShown: false, sheetAllowedDetents: 'fitToContents', }} /> </Stack.Navigator> );}
```

Due to technical issues in platform component integration withreact-native,presentation: 'formSheet'has limited support forflex: 1.

On Android, usingflex: 1on a top-level content container passed to aformSheetwithshowAllowedDetents: 'fitToContents'causes the sheet to not display at all, leaving only the dimmed background visible. This is because it is the sheet, not the parent who is source of the size. Setting fixed values forsheetAllowedDetents, e.g.[0.4, 0.9], works correctly (content is aligned for the highest detent).

On iOS,flex: 1withshowAllowedDetents: 'fitToContents'works properly but setting a fixed value forshowAllowedDetentscauses the screen to not respect theflex: 1style - the height of the container does not fill theformSheetfully, but rather inherits intrinsic size of its contents. This tradeoff iscurrentlynecessary to prevent"sheet flickering" problem on iOS.

If you don't useflex: 1but the content's height is less than max screen height, the rest of the sheet might become translucent or use the default theme background color (you can see this happening on the screenshots in the descrption ofthis PR). To match the sheet to the background of your content, setbackgroundColorin thecontentStyleprop of the given screen.

On Android, there are also some problems with getting nested ScrollViews to work properly. The solution is to setnestedScrollEnabledon theScrollView, but this does not work if the content's height is less than theScrollView's height. Please seethis PRfor details and suggestedworkaround.

On Android, nested stack andheaderShownprop are not currently supported for screens withpresentation: 'formSheet'.

##### sheetAllowedDetents​

Works only whenpresentationis set toformSheet.

Describes heights where a sheet can rest.

Supported values:

- fitToContents- intents to set the sheet height to the height of its contents.
- Array of fractions, e.g.[0.25, 0.5, 0.75]:Heights should be described as fraction (a number from[0, 1]interval) of screen height / maximum detent height.The arraymustbe sorted in ascending order. This invariant is verified only in developement mode, where violation results in error.iOS accepts any number of detents, whileAndroid is limited to three- any surplus values, beside first three are ignored.
- Heights should be described as fraction (a number from[0, 1]interval) of screen height / maximum detent height.
- The arraymustbe sorted in ascending order. This invariant is verified only in developement mode, where violation results in error.
- iOS accepts any number of detents, whileAndroid is limited to three- any surplus values, beside first three are ignored.
Defaults to[1.0].

Only supported on Android and iOS.

##### sheetElevation​

Works only whenpresentationis set toformSheet.

Integer value describing elevation of the sheet, impacting shadow on the top edge of the sheet.

Not dynamic - changing it after the component is rendered won't have an effect.

Defaults to24.

Only supported on Android.

##### sheetExpandsWhenScrolledToEdge​

Works only whenpresentationis set toformSheet.

Whether the sheet should expand to larger detent when scrolling.

Defaults totrue.

Only supported on iOS.

Please note that for this interaction to work, the ScrollView must be "first-subview-chain" descendant of the Screen component. This restriction is due to platform requirements.

##### sheetCornerRadius​

Works only whenpresentationis set toformSheet.

The corner radius that the sheet will try to render with.

If set to non-negative value it will try to render sheet with provided radius, else it will apply system default.

If left unset, system default is used.

Only supported on Android and iOS.

##### sheetInitialDetentIndex​

Works only whenpresentationis set toformSheet.

Indexof the detent the sheet should expand to after being opened.

If the specified index is out of bounds ofsheetAllowedDetentsarray, in dev environment more errors will be thrown, in production the value will be reset to default value.

Additionaly there islastvalue available, when set the sheet will expand initially to last (largest) detent.

Defaults to0- which represents first detent in the detents array.

Only supported on Android and iOS.

##### sheetGrabberVisible​

Works only whenpresentationis set toformSheet.

Boolean indicating whether the sheet shows a grabber at the top.

Defaults tofalse.

Only supported on iOS.

##### sheetLargestUndimmedDetentIndex​

Works only whenpresentationis set toformSheet.

The largest sheet detent for which a view underneath won't be dimmed.

This prop can be set to an number, which indicates index of detent insheetAllowedDetentsarray for which there won't be a dimming view beneath the sheet.

Additionaly there are following options available:

- none- there will be dimming view for all detents levels,
- last- there won't be a dimming view for any detent level.
Defaults tonone, indicating that the dimming view should be always present.

Only supported on Android and iOS.

##### orientation​

The display orientation to use for the screen.

Supported values:

- default- resolves to "all" without "portrait_down" on iOS. On Android, this lets the system decide the best orientation.
- all: all orientations are permitted.
- portrait: portrait orientations are permitted.
- portrait_up: right-side portrait orientation is permitted.
- portrait_down: upside-down portrait orientation is permitted.
- landscape: landscape orientations are permitted.
- landscape_left: landscape-left orientation is permitted.
- landscape_right: landscape-right orientation is permitted.
Only supported on Android and iOS.

##### autoHideHomeIndicator​

Boolean indicating whether the home indicator should prefer to stay hidden. Defaults tofalse.

Only supported on iOS.

##### gestureDirection​

Sets the direction in which you should swipe to dismiss the screen.

Supported values:

- vertical– dismiss screen vertically
- horizontal– dismiss screen horizontally (default)
When usingverticaloption, optionsfullScreenGestureEnabled: true,customAnimationOnGesture: trueandanimation: 'slide_from_bottom'are set by default.

Only supported on iOS.

##### animationDuration​

Changes the duration (in milliseconds) ofslide_from_bottom,fade_from_bottom,fadeandsimple_pushtransitions on iOS. Defaults to350.

For screens withdefaultandfliptransitions, and, as of now, for screens withpresentationset tomodal,formSheet,pageSheet(regardless of transition), the duration isn't customizable.

Only supported on iOS.

##### navigationBarColor​

This option is deprecated and will be removed in a future release (for apps targeting Android SDK 35 or above edge-to-edge mode is enabled by default
and it is expected that the edge-to-edge will be enforced in future SDKs, seeherefor more information).

Sets the navigation bar color. Defaults to initial status bar color.

Only supported on Android.

##### navigationBarHidden​

Boolean indicating whether the navigation bar should be hidden. Defaults tofalse.

Only supported on Android.

##### freezeOnBlur​

Boolean indicating whether to prevent inactive screens from re-rendering. Defaults tofalse.
Defaults totruewhenenableFreeze()fromreact-native-screenspackage is run at the top of the application.

Only supported on iOS and Android.

##### scrollEdgeEffects​

Configures the scroll edge effect for thecontent ScrollView(the ScrollView that is present in first descendants chain of the Screen).
Depending on values set, it will blur the scrolling content below certain UI elements (e.g. header items, search bar) for the specified edge of the ScrollView.
When set in nested containers, i.e. Native Stack inside Native Bottom Tabs, or the other way around, the ScrollView will use only the innermost one's config.

Edge effects can be configured for each edge separately. The following values are currently supported:

- automatic- the automatic scroll edge effect style,
- hard- a scroll edge effect with a hard cutoff and dividing line,
- soft- a soft-edged scroll edge effect,
- hidden- no scroll edge effect.
Defaults toautomaticfor each edge.

Using bothblurEffectandscrollEdgeEffects(>= iOS 26) simultaneously may cause overlapping effects.

Only supported on iOS, starting from iOS 26.

#### Header related options​

The navigator supports following options to configure the header:

##### headerBackButtonMenuEnabled​

Boolean indicating whether to show the menu on longPress of iOS >= 14 back button. Defaults totrue.

Only supported on iOS.

##### headerBackVisible​

Whether the back button is visible in the header. You can use it to show a back button alongsideheaderLeftif you have specified it.

This will have no effect on the first screen in the stack.

##### headerBackTitle​

Title string used by the back button on iOS. Defaults to the previous scene's title, "Back" or arrow icon depending on the available space. SeeheaderBackButtonDisplayModeto read about limitations and customize the behavior.

UseheaderBackButtonDisplayMode: "minimal"to hide it.

Only supported on iOS.

##### headerBackButtonDisplayMode​

How the back button displays icon and title.

Supported values:

- "default" - Displays one of the following depending on the available space: previous screen's title, generic title (e.g. 'Back') or no title (only icon).
- "generic" – Displays one of the following depending on the available space: generic title (e.g. 'Back') or no title (only icon).
- "minimal" – Always displays only the icon without a title.
The space-aware behavior is disabled when:

- The iOS version is 13 or lower
- Custom font family or size is set (e.g. withheaderBackTitleStyle)
- Back button menu is disabled (e.g. withheaderBackButtonMenuEnabled)
In such cases, a static title and icon are always displayed.

Only supported on iOS.

##### headerBackTitleStyle​

Style object for header back title. Supported properties:

- fontFamily
- fontSize
Only supported on iOS.

Example:

```
headerBackTitleStyle: { fontSize: 14, fontFamily: 'Georgia',},
```

##### headerBackIcon​

Icon to display in the header as the icon in the back button. Defaults to back icon image for the platform:

- A chevron on iOS
- An arrow on Android
Currently only supports image sources.

Example:

```
headerBackIcon: { type: 'image', source: require('./path/to/icon.png'),}
```

##### headerLargeStyle​

Style of the header when a large title is shown. The large title is shown ifheaderLargeTitleEnabledistrueand the edge of any scrollable content reaches the matching edge of the header.

Supported properties:

- backgroundColor
Only supported on iOS.

##### headerLargeTitleEnabled​

Whether to enable header with large title which collapses to regular header on scroll.
Defaults tofalse.

For large title to collapse on scroll, the content of the screen should be wrapped in a scrollable view such asScrollVieworFlatList. If the scrollable area doesn't fill the screen, the large title won't collapse on scroll. You also need to specifycontentInsetAdjustmentBehavior="automatic"in yourScrollView,FlatListetc.

Only supported on iOS.

##### headerLargeTitleShadowVisible​

Whether drop shadow of header is visible when a large title is shown.

##### headerLargeTitleStyle​

Style object for large title in header. Supported properties:

- fontFamily
- fontSize
- fontWeight
- color
Only supported on iOS.

Example:

```
 headerLargeTitleStyle: { fontFamily: 'Georgia', fontSize: 22, fontWeight: '500', color: 'blue', },
```

##### headerStyle​

Style object for header. Supported properties:

- backgroundColor

##### headerShadowVisible​

Whether to hide the elevation shadow (Android) or the bottom border (iOS) on the header.

Android:

iOS:

##### headerTransparent​

Boolean indicating whether the navigation bar is translucent.

Defaults tofalse. Setting this totruemakes the header absolutely positioned - so that the header floats over the screen so that it overlaps the content underneath, and changes the background color totransparentunless specified inheaderStyle.

This is useful if you want to render a semi-transparent header or a blurred background.

Note that if you don't want your content to appear under the header, you need to manually add a top margin to your content. React Navigation won't do it automatically.

To get the height of the header, you can useHeaderHeightContextwithReact's Context APIoruseHeaderHeight.

##### headerBlurEffect​

Blur effect for the translucent header. TheheaderTransparentoption needs to be set totruefor this to work.

Supported values:

- extraLight
extraLight

- light
light

- dark
dark

- regular
regular

- prominent
prominent

- systemUltraThinMaterial
systemUltraThinMaterial

- systemThinMaterial
systemThinMaterial

- systemMaterial
systemMaterial

- systemThickMaterial
systemThickMaterial

- systemChromeMaterial
systemChromeMaterial

- systemUltraThinMaterialLight
systemUltraThinMaterialLight

- systemThinMaterialLight
systemThinMaterialLight

- systemMaterialLight
systemMaterialLight

- systemThickMaterialLight
systemThickMaterialLight

- systemChromeMaterialLight
systemChromeMaterialLight

- systemUltraThinMaterialDark
systemUltraThinMaterialDark

- systemThinMaterialDark
systemThinMaterialDark

- systemMaterialDark
systemMaterialDark

- systemThickMaterialDark
systemThickMaterialDark

- systemChromeMaterialDark
systemChromeMaterialDark

Using bothblurEffectandscrollEdgeEffects(>= iOS 26) simultaneously may cause overlapping effects.

Only supported on iOS.

##### headerBackground​

Function which returns a React Element to render as the background of the header. This is useful for using backgrounds such as an image or a gradient.

Example:

```
 headerBackground: () => ( <LinearGradient colors={['#c17388', '#90306f']} style={{ flex: 1 }} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }} /> ),
```

##### headerTintColor​

Tint color for the header. Changes the color of back button and title.

##### headerLeft​

Function which returns a React Element to display on the left side of the header. This replaces the back button. SeeheaderBackVisibleto show the back button along side left element. It receives the following properties in the arguments:

- tintColor- The tint color to apply. Defaults to thetheme's primary color.
- canGoBack- Boolean indicating whether there is a screen to go back to.
- label- Label text for the button. Usually the title of the previous screen.
- href- Thehrefto use for the anchor tag on web
Example:

```
 headerLeft: () => ( <MaterialCommunityIcons name="map" color="gray" size={36} /> ), headerBackVisible: true, headerBackTitle: 'Back',
```

##### unstable_headerLeftItems​

This option is experimental and may change in a minor release.

Function which returns an array of items to display as on the left side of the header. This will overrideheaderLeftif both are specified. It receives the following properties in the arguments:

- tintColor- The tint color to apply. Defaults to thetheme's primary color.
- canGoBack- Boolean indicating whether there is a screen to go back to.
Example:

```
unstable_headerLeftItems: () => [ { type: 'button', title: 'Edit', onPress: () => { // Do something }, },],
```

SeeHeader itemsfor more information.

Only supported on iOS.

##### headerRight​

Function which returns a React Element to display on the right side of the header. It receives the following properties in the arguments:

- tintColor- The tint color to apply. Defaults to thetheme's primary color.
tintColor- The tint color to apply. Defaults to thetheme's primary color.

- canGoBack- Boolean indicating whether there is a screen to go back to.
canGoBack- Boolean indicating whether there is a screen to go back to.

Example:

```
headerRight: () => <MaterialCommunityIcons name="map" color="blue" size={36} />;
```

##### unstable_headerRightItems​

This option is experimental and may change in a minor release.

Function which returns an array of items to display as on the right side of the header. This will overrideheaderRightif both are specified. It receives the following properties in the arguments:

- tintColor- The tint color to apply. Defaults to thetheme's primary color.
- canGoBack- Boolean indicating whether there is a screen to go back to.
Example:

```
unstable_headerRightItems: () => [ { type: 'button', title: 'Edit', onPress: () => { // Do something }, },],
```

SeeHeader itemsfor more information.

Only supported on iOS.

##### headerTitle​

String or a function that returns a React Element to be used by the header. Defaults totitleor name of the screen.

When a function is passed, it receivestintColorandchildrenin the options object as an argument. The title string is passed inchildren.

Note that if you render a custom element by passing a function, animations for the title won't work.

##### headerTitleAlign​

How to align the header title. Possible values:

- left
left

- center
center

Defaults tolefton platforms other than iOS.

Not supported on iOS. It's alwayscenteron iOS and cannot be changed.

##### headerTitleStyle​

Style object for header title. Supported properties:

- fontFamily
fontFamily

- fontSize
fontSize

- fontWeight
fontWeight

- color
color

Example:

```
 headerTitleStyle: { color: 'blue', fontSize: 22, fontFamily: 'Georgia', fontWeight: 300, },
```

##### headerSearchBarOptions​

Options to render a native search bar. Search bars are rarely static so normally it is controlled by passing an object toheaderSearchBarOptionsnavigation option in the component's body.

On iOS, you also need to specifycontentInsetAdjustmentBehavior="automatic"in yourScrollView,FlatListetc. If you don't have aScrollView, specifyheaderTransparent: false.

Example:

```
React.useLayoutEffect(() => { navigation.setOptions({ headerSearchBarOptions: { // search bar options }, });}, [navigation]);
```

Supported properties are:

Ref to manipulate the search input imperatively. It contains the following methods:

- focus- focuses the search bar
- blur- removes focus from the search bar
- setText- sets the search bar's content to given value
- clearText- removes any text present in the search bar input field
- cancelSearch- cancel the search and close the search bar
- toggleCancelButton- depending on passed boolean value, hides or shows cancel button (only supported on iOS)
Controls whether the text is automatically auto-capitalized as it is entered by the user.
Possible values:

- systemDefault
- none
- words
- sentences
- characters
Defaults tosystemDefaultwhich is the same assentenceson iOS andnoneon Android.

Whether to automatically focus search bar when it's shown. Defaults tofalse.

Only supported on Android.

The search field background color. By default bar tint color is translucent.

Only supported on iOS.

The color for the cursor caret and cancel button text.

Only supported on iOS.

The text to be used instead of defaultCancelbutton text.

Only supported on iOS.Deprecatedstarting from iOS 26.

Whether the back button should close search bar's text input or not. Defaults tofalse.

Only supported on Android.

Boolean indicating whether to hide the navigation bar during searching.

If left unset, system default is used.

Only supported on iOS.

Boolean indicating whether to hide the search bar when scrolling. Defaults totrue.

Only supported on iOS.

The type of the input. Defaults to"text".

Supported values:

- "text"
- "phone"
- "number"
- "email"
Only supported on Android.

Boolean indicating whether to obscure the underlying content with semi-transparent overlay.

If left unset, system default is used.

Only supported on iOS.

Controls preferred placement of the search bar. Defaults toautomatic.

Supported values:

- automatic
- stacked
- inline(deprecatedstarting from iOS 26, it is mapped tointegrated)
- integrated(available starting from iOS 26, on prior versions it is mapped toinline)
- integratedButton(available starting from iOS 26, on prior versions it is mapped toinline)
- integratedCentered(available starting from iOS 26, on prior versions it is mapped toinline)
Only supported on iOS.

Boolean indicating whether the system can place the search bar among other toolbar items on iPhone.

Set this prop tofalseto prevent the search bar from appearing in the toolbar whenplacementisautomatic,integrated,integratedButtonorintegratedCentered.

Defaults totrue. Ifplacementis set tostacked, the value of this prop will be overridden withfalse.

Only supported on iOS, starting from iOS 26.

Text displayed when search field is empty.

The color of the text in the search field.

The color of the hint text in the search field.

Only supported on Android.

The color of the search and close icons shown in the header

Only supported on Android.

Whether to show the search hint icon when search bar is focused. Defaults totrue.

Only supported on Android.

A callback that gets called when search bar has lost focus.

A callback that gets called when the cancel button is pressed.

A callback that gets called when the search button is pressed.

```
const [search, setSearch] = React.useState('');React.useLayoutEffect(() => { navigation.setOptions({ headerSearchBarOptions: { onSearchButtonPress: (event) => setSearch(event?.nativeEvent?.text), }, });}, [navigation]);
```

A callback that gets called when the text changes. It receives the current text value of the search bar.

Example:

```
const [search, setSearch] = React.useState('');React.useLayoutEffect(() => { navigation.setOptions({ headerSearchBarOptions: { onChangeText: (event) => setSearch(event.nativeEvent.text), }, });}, [navigation]);
```

##### headerShown​

Whether to show the header. The header is shown by default. Setting this tofalsehides the header.

##### header​

Custom header to use instead of the default header.

This accepts a function that returns a React Element to display as a header. The function receives an object containing the following properties as the argument:

- navigation- The navigation object for the current screen.
- route- The route object for the current screen.
- options- The options for the current screen
- back- Options for the back button, contains an object with atitleproperty to use for back button label.
Example:

```
import { getHeaderTitle } from '@react-navigation/elements';// ..header: ({ navigation, route, options, back }) => { const title = getHeaderTitle(options, route.name); return ( <MyHeader title={title} leftButton={ back ? <MyBackButton onPress={navigation.goBack} /> : undefined } style={options.headerStyle} /> );};
```

To set a custom header for all the screens in the navigator, you can specify this option in thescreenOptionsprop of the navigator.

Note that if you specify a custom header, the native functionality such as large title, search bar etc. won't work.

#### Events​

The navigator canemit eventson certain actions. Supported events are:

##### transitionStart​

This event is fired when the transition animation starts for the current screen.

Event data:

- e.data.closing- Boolean indicating whether the screen is being opened or closed.
Example:

```
React.useEffect(() => { const unsubscribe = navigation.addListener('transitionStart', (e) => { // Do something }); return unsubscribe;}, [navigation]);
```

##### transitionEnd​

This event is fired when the transition animation ends for the current screen.

Event data:

- e.data.closing- Boolean indicating whether the screen was opened or closed.
Example:

```
React.useEffect(() => { const unsubscribe = navigation.addListener('transitionEnd', (e) => { // Do something }); return unsubscribe;}, [navigation]);
```

##### gestureCancel​

This event is fired when the swipe back gesture is canceled. Only supported on iOS.

Example:

```
React.useEffect(() => { const unsubscribe = navigation.addListener('gestureCancel', (e) => { // Do something }); return unsubscribe;}, [navigation]);
```

##### sheetDetentChange​

This event is fired when the screen haspresentationset toformSheetand the sheet detent changes.

Event data:

- e.data.index- Index of the current detent in thesheetAllowedDetentsarray.
- e.data.stable- Boolean indicating whether the sheet is being dragged or settling. Only supported on Android. On iOS, this is alwaystrue.
Example:

```
React.useEffect(() => { const unsubscribe = navigation.addListener('sheetDetentChange', (e) => { // Do something }); return unsubscribe;}, [navigation]);
```

#### Helpers​

The native stack navigator adds the following methods to the navigation object:

##### replace​

Replaces the current screen with a new screen in the stack. The method accepts the following arguments:

- name-string- Name of the route to push onto the stack.
- params-object- Screen params to pass to the destination route.

```
navigation.replace('Profile', { owner: 'Michaś' });
```

##### push​

Pushes a new screen to the top of the stack and navigate to it. The method accepts the following arguments:

- name-string- Name of the route to push onto the stack.
- params-object- Screen params to pass to the destination route.

```
navigation.push('Profile', { owner: 'Michaś' });
```

##### pop​

Pops the current screen from the stack and navigates back to the previous screen. It takes one optional argument (count), which allows you to specify how many screens to pop back by.

```
navigation.pop();
```

##### popTo​

Navigates back to a previous screen in the stack by popping screens after it. The method accepts the following arguments:

- name-string- Name of the route to navigate to.
- params-object- Screen params to pass to the destination route.
- options- Options object containing the following properties:merge-boolean- Whether params should be merged with the existing route params, or replace them (when navigating to an existing screen). Defaults tofalse.
- merge-boolean- Whether params should be merged with the existing route params, or replace them (when navigating to an existing screen). Defaults tofalse.
If a matching screen is not found in the stack, this will pop the current screen and add a new screen with the specified name and params.

```
navigation.popTo('Profile', { owner: 'Michaś' });
```

##### popToTop​

Pops all of the screens in the stack except the first one and navigates to it.

```
navigation.popToTop();
```

#### Hooks​

The native stack navigator exports the following hooks:

##### useAnimatedHeaderHeight​

The hook returns an animated value representing the height of the header. This is similar touseHeaderHeightbut returns an animated value that changed as the header height changes, e.g. when expanding or collapsing large title or search bar on iOS.

It can be used to animated content along with header height changes.

```
import { Animated } from 'react-native';import { useAnimatedHeaderHeight } from '@react-navigation/native-stack';const MyView = () => { const headerHeight = useAnimatedHeaderHeight(); return ( <Animated.View style={{ height: 100, aspectRatio: 1, backgroundColor: 'tomato', transform: [{ translateY: headerHeight }], }} /> );};
```

### Header items​

Theunstable_headerLeftItemsandunstable_headerRightItemsoptions allow you to add header items to the left and right side of the header respectively. This items can show native buttons, menus or custom React elements.

On iOS 26+, the header right items can also be collapsed into an overflow menu by the system when there is not enough space to show all items. Note that custom elements (withtype: 'custom') won't be collapsed into the overflow menu.

There are 3 categories of items that can be displayed in the header:

#### Action​

A regular button that performs an action when pressed, or shows a menu.

Common properties:

- type: Must bebuttonormenu.
type: Must bebuttonormenu.

- label: Label of the item. The label is not shown ificonis specified. However, it is used by screen readers, or if the header items get collapsed due to lack of space.
label: Label of the item. The label is not shown ificonis specified. However, it is used by screen readers, or if the header items get collapsed due to lack of space.

- labelStyle: Style object for the label. Supported properties:fontFamilyfontSizefontWeightcolor(of typeColorValue)
labelStyle: Style object for the label. Supported properties:

- fontFamily
- fontSize
- fontWeight
- color(of typeColorValue)
- icon: Optional icon to show instead of the label.The icon can be an image:{type:'image',source:require('./path/to/image.png'),tinted:true,// Whether to apply tint color to the icon. Defaults to true.}Or aSF Symbolsname:{type:'sfSymbol',name:'heart',}
icon: Optional icon to show instead of the label.

The icon can be an image:

```
{ type: 'image', source: require('./path/to/image.png'), tinted: true, // Whether to apply tint color to the icon. Defaults to true.}
```

Or aSF Symbolsname:

```
{ type: 'sfSymbol', name: 'heart',}
```

- variant: Visual variant of the button. Supported values:plain(default)doneprominent(iOS 26+)
variant: Visual variant of the button. Supported values:

- plain(default)
- done
- prominent(iOS 26+)
- tintColor: Tint color to apply to the item.
tintColor: Tint color to apply to the item.

- disabled: Whether the item is disabled.
disabled: Whether the item is disabled.

- width: Width of the item.
width: Width of the item.

- hidesSharedBackground(iOS 26+): Whether the background this item may share with other items in the bar should be hidden. Setting this totruehides the liquid glass background.
hidesSharedBackground(iOS 26+): Whether the background this item may share with other items in the bar should be hidden. Setting this totruehides the liquid glass background.

- sharesBackground(iOS 26+): Whether this item can share a background with other items. Defaults totrue.
sharesBackground(iOS 26+): Whether this item can share a background with other items. Defaults totrue.

- identifier(iOS 26+) - An identifier used to match items across transitions.
identifier(iOS 26+) - An identifier used to match items across transitions.

- badge(iOS 26+): An optional badge to display alongside the item. Supported properties:value: The value to display in the badge. It can be a string or a number.style: Style object for the badge. Supported properties:fontFamilyfontSizefontWeightcolorbackgroundColor
badge(iOS 26+): An optional badge to display alongside the item. Supported properties:

- value: The value to display in the badge. It can be a string or a number.
- style: Style object for the badge. Supported properties:fontFamilyfontSizefontWeightcolorbackgroundColor
- fontFamily
- fontSize
- fontWeight
- color
- backgroundColor
- accessibilityLabel: Accessibility label for the item.
accessibilityLabel: Accessibility label for the item.

- accessibilityHint: Accessibility hint for the item.
accessibilityHint: Accessibility hint for the item.

Supported properties whentypeisbutton:

- onPress: Function to call when the button is pressed.
- selected: Whether the button is in a selected state.
Example:

```
unstable_headerRightItems: () => [ { type: 'button', label: 'Edit', icon: { type: 'sfSymbol', name: 'pencil', }, onPress: () => { // Do something }, },],
```

Supported properties whentypeismenu:

- changesSelectionAsPrimaryAction: Whether the menu is a selection menu. Tapping an item in a selection menu will add a checkmark to the selected item. Defaults tofalse.
- menu: An object containing the menu items. It contains the following properties:title: Optional title to show on top of the menu.multiselectable: Whether multiple items in the menu can be selected (i.e. in "on" state). Defaults tofalse.layout: How the menu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.items: An array of menu items. A menu item can be either anactionor asubmenu.action: An object with the following properties:type: Must beaction.label: Label of the menu item.description: The secondary text displayed alongside the label of the menu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'trash',}onPress: Function to call when the menu item is pressed.state: Optional state of the menu item. Supported values:onoffmixeddisabled: Whether the menu item is disabled.destructive: Whether the menu item is styled as destructive.hidden: Whether the menu item is hidden.keepsMenuPresented: Whether to keep the menu open after selecting this item. Defaults tofalse.discoverabilityLabel: An elaborated title that explains the purpose of the action. On iOS, the system displays this title in the discoverability heads-up display (HUD). If this is not set, the HUD displays the label property.submenu: An object with the following properties:type: Must besubmenu.label: Label of the submenu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'pencil',}inline: Whether the menu is displayed inline with the parent menu. By default, submenus are displayed after expanding the parent menu item. Inline menus are displayed as part of the parent menu as a section. Defaults tofalse.layout: How the submenu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.destructive: Whether the submenu is styled as destructive.multiselectable: Whether multiple items in the submenu can be selected (i.e. in "on" state). Defaults tofalse.items: An array of menu items (can be eitheractionorsubmenu).
- title: Optional title to show on top of the menu.
- multiselectable: Whether multiple items in the menu can be selected (i.e. in "on" state). Defaults tofalse.
- layout: How the menu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.
- default(default): menu items are displayed normally.
- palette: menu items are displayed in a horizontal row.
- items: An array of menu items. A menu item can be either anactionor asubmenu.action: An object with the following properties:type: Must beaction.label: Label of the menu item.description: The secondary text displayed alongside the label of the menu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'trash',}onPress: Function to call when the menu item is pressed.state: Optional state of the menu item. Supported values:onoffmixeddisabled: Whether the menu item is disabled.destructive: Whether the menu item is styled as destructive.hidden: Whether the menu item is hidden.keepsMenuPresented: Whether to keep the menu open after selecting this item. Defaults tofalse.discoverabilityLabel: An elaborated title that explains the purpose of the action. On iOS, the system displays this title in the discoverability heads-up display (HUD). If this is not set, the HUD displays the label property.submenu: An object with the following properties:type: Must besubmenu.label: Label of the submenu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'pencil',}inline: Whether the menu is displayed inline with the parent menu. By default, submenus are displayed after expanding the parent menu item. Inline menus are displayed as part of the parent menu as a section. Defaults tofalse.layout: How the submenu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.destructive: Whether the submenu is styled as destructive.multiselectable: Whether multiple items in the submenu can be selected (i.e. in "on" state). Defaults tofalse.items: An array of menu items (can be eitheractionorsubmenu).
- action: An object with the following properties:type: Must beaction.label: Label of the menu item.description: The secondary text displayed alongside the label of the menu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'trash',}onPress: Function to call when the menu item is pressed.state: Optional state of the menu item. Supported values:onoffmixeddisabled: Whether the menu item is disabled.destructive: Whether the menu item is styled as destructive.hidden: Whether the menu item is hidden.keepsMenuPresented: Whether to keep the menu open after selecting this item. Defaults tofalse.discoverabilityLabel: An elaborated title that explains the purpose of the action. On iOS, the system displays this title in the discoverability heads-up display (HUD). If this is not set, the HUD displays the label property.
action: An object with the following properties:

- type: Must beaction.
type: Must beaction.

- label: Label of the menu item.
label: Label of the menu item.

- description: The secondary text displayed alongside the label of the menu item.
description: The secondary text displayed alongside the label of the menu item.

- icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'trash',}
icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:

```
{ type: 'sfSymbol', name: 'trash',}
```

- onPress: Function to call when the menu item is pressed.
onPress: Function to call when the menu item is pressed.

- state: Optional state of the menu item. Supported values:onoffmixed
state: Optional state of the menu item. Supported values:

- on
- off
- mixed
- disabled: Whether the menu item is disabled.
disabled: Whether the menu item is disabled.

- destructive: Whether the menu item is styled as destructive.
destructive: Whether the menu item is styled as destructive.

- hidden: Whether the menu item is hidden.
hidden: Whether the menu item is hidden.

- keepsMenuPresented: Whether to keep the menu open after selecting this item. Defaults tofalse.
keepsMenuPresented: Whether to keep the menu open after selecting this item. Defaults tofalse.

- discoverabilityLabel: An elaborated title that explains the purpose of the action. On iOS, the system displays this title in the discoverability heads-up display (HUD). If this is not set, the HUD displays the label property.
discoverabilityLabel: An elaborated title that explains the purpose of the action. On iOS, the system displays this title in the discoverability heads-up display (HUD). If this is not set, the HUD displays the label property.

- submenu: An object with the following properties:type: Must besubmenu.label: Label of the submenu item.icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'pencil',}inline: Whether the menu is displayed inline with the parent menu. By default, submenus are displayed after expanding the parent menu item. Inline menus are displayed as part of the parent menu as a section. Defaults tofalse.layout: How the submenu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.destructive: Whether the submenu is styled as destructive.multiselectable: Whether multiple items in the submenu can be selected (i.e. in "on" state). Defaults tofalse.items: An array of menu items (can be eitheractionorsubmenu).
submenu: An object with the following properties:

- type: Must besubmenu.
type: Must besubmenu.

- label: Label of the submenu item.
label: Label of the submenu item.

- icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:{type:'sfSymbol',name:'pencil',}
icon: Optional icon to show alongside the label. The icon can be aSF Symbolsname:

```
{ type: 'sfSymbol', name: 'pencil',}
```

- inline: Whether the menu is displayed inline with the parent menu. By default, submenus are displayed after expanding the parent menu item. Inline menus are displayed as part of the parent menu as a section. Defaults tofalse.
inline: Whether the menu is displayed inline with the parent menu. By default, submenus are displayed after expanding the parent menu item. Inline menus are displayed as part of the parent menu as a section. Defaults tofalse.

- layout: How the submenu items are displayed. Supported values:default(default): menu items are displayed normally.palette: menu items are displayed in a horizontal row.
layout: How the submenu items are displayed. Supported values:

- default(default): menu items are displayed normally.
- palette: menu items are displayed in a horizontal row.
- destructive: Whether the submenu is styled as destructive.
destructive: Whether the submenu is styled as destructive.

- multiselectable: Whether multiple items in the submenu can be selected (i.e. in "on" state). Defaults tofalse.
multiselectable: Whether multiple items in the submenu can be selected (i.e. in "on" state). Defaults tofalse.

- items: An array of menu items (can be eitheractionorsubmenu).
items: An array of menu items (can be eitheractionorsubmenu).

Example:

```
unstable_headerRightItems: () => [ { type: 'menu', label: 'Options', icon: { type: 'sfSymbol', name: 'ellipsis', }, menu: { title: 'Options', items: [ { type: 'action', label: 'Edit', icon: { type: 'sfSymbol', name: 'pencil', }, onPress: () => { // Do something }, }, { type: 'submenu', label: 'More', items: [ { type: 'action', label: 'Delete', destructive: true, onPress: () => { // Do something }, }, ], }, ], }, },],
```

#### Spacing​

An item to add spacing between other items in the header.

Supported properties:

- type: Must bespacing.
- spacing: Amount of spacing to add.

```
unstable_headerRightItems: () => [ { type: 'button', label: 'Edit', onPress: () => { // Do something }, }, { type: 'spacing', spacing: 10, }, { type: 'button', label: 'Delete', onPress: () => { // Do something }, },],
```

#### Custom​

A custom item to display any React Element in the header.

Supported properties:

- type: Must becustom.
- element: A React Element to display as the item.
- hidesSharedBackground: Whether the background this item may share with other items in the bar should be hidden. Setting this totruehides the liquid glass background on iOS 26+.
Example:

```
unstable_headerRightItems: () => [ { type: 'custom', element: <MaterialCommunityIcons name="map" color="gray" size={36} />, },],
```

The advantage of using this overheaderLeftorheaderRightoptions is that it supports features like shared background on iOS 26+.

- Installation
- Usage
- API DefinitionPropsOptionsHeader related optionsEventsHelpersHooks
- Props
- Options
- Header related options
- Events
- Helpers
- Hooks
- Header itemsActionSpacingCustom
- Action
- Spacing
- Custom