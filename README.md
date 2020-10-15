# ZoomSDKJWTGenerator
This Can be used to generate [Zoom](https://zoom.us) JWT tokens for use with any Zoom SDK variants for these platforms
1. [Zoom Android SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/android "Zoom Android SDK")
2. [Zoom iOS SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/iOS "Zoom iOS SDK")
3. [Zoom Mac SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/macos "Zoom Mac SDK")
4. [Zoom Windows SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/windows "Zoom Windows SDK")
5. [Zoom Windows SDK (C# Wrapper)](https://marketplace.zoom.us/docs/sdk/native-sdks/windows/c-sharp-wrapper "Zoom Windows SDK (C# Wrapper)")
6. [Zoom Electron SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/electron "Zoom Electron SDK")
7. [Zoom SDK Ionic](https://marketplace.zoom.us/docs/sdk/native-sdks/ionic/overview "Zoom SDK Ionic")
8. [Zoom SDK Cordova Plugin](https://marketplace.zoom.us/docs/sdk/native-sdks/ionic/overview "Zoom SDK Cordova Plugin")

This python class will generate [Zoom](https://zoom.us) JWT tokens for use with v2 of the [Zoom API](https://zoom.github.io/api/#authentication) and takes care of regenerating expired tokens dynamically.

## Requirements:
The pyjwt python library is required. `pip install pyjwt` or `pip3 install pyjwt` depending on your version
