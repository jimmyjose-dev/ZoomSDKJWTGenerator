# ZoomSDKJWTGenerator
It can generate [Zoom](https://zoom.us) JWT that can be used with any Zoom SDK variants for these platforms:
1. [Zoom Android SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/android "Zoom Android SDK")
2. [Zoom iOS SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/iOS "Zoom iOS SDK")
3. [Zoom Mac SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/macos "Zoom Mac SDK")
4. [Zoom Windows SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/windows "Zoom Windows SDK")
5. [Zoom Windows SDK (C# Wrapper)](https://marketplace.zoom.us/docs/sdk/native-sdks/windows/c-sharp-wrapper "Zoom Windows SDK (C# Wrapper)")
6. [Zoom Electron SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/electron "Zoom Electron SDK")
7. [Zoom SDK Ionic](https://marketplace.zoom.us/docs/sdk/native-sdks/ionic/overview "Zoom SDK Ionic")
8. [Zoom SDK Cordova Plugin](https://marketplace.zoom.us/docs/sdk/native-sdks/ionic/overview "Zoom SDK Cordova Plugin")


## Requirements:

#### 1) Zoom
https://marketplace.zoom.us/develop/create

Create an app with type SDK , option will look like this:

[![Zoom App SDK type](https://dl.dropboxusercontent.com/s/e49i9ni9zje4o6d/zoomsdkappcreate.png "Zoom App SDK type")](https://dl.dropboxusercontent.com/s/e49i9ni9zje4o6d/zoomsdkappcreate.png "Zoom App SDK type")

a. Note the SDK key

b. Note the SDK secret 


#### 2) Python
The pyjwt python library is required. `pip install pyjwt` or `pip3 install pyjwt` depending on your version

------------

## Usage
```
zoom_sdk = ZoomSDKJWT("SDK KEY","SDK Secret")
zoom_sdk.generate_token()
```
or if you want to import in another module
```
from ZoomSDKJWT import ZoomSDKJWT
zoom_sdk = ZoomSDKJWT("SDK KEY","SDK Secret")
zoom_sdk.generate_token()
```

### Note
You can run the code as it is by providing SDK Key and SDK Secret and it will generate a valid JWT, but if you want to modify the validity/expiry of JWT, keep these points in mind:
1. The **exp** value should **not exceed** 2 days, by default its set to 1 day 
2. The **tokenExp**  value should be **more than** 30 mins and **less than** exp value, by default its set for 1 hour.
