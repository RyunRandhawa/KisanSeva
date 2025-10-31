# KisanSeva Android App

This is the Android application for the KisanSeva platform, converting your Flask website into a native mobile app.

## 📱 App Features

- **WebView Integration**: Loads your Flask backend seamlessly
- **Bottom Navigation**: Easy access to all main features
- **Camera & File Upload**: Full support for pest diagnosis image uploads
- **Offline Caching**: Better performance with WebView caching
- **Multi-language Support**: Integrated with your existing language system
- **Firebase Ready**: Pre-configured for Firebase Authentication & Database

## 🚀 Setup Instructions

### 1. Prerequisites

- Android Studio (Arctic Fox or newer)
- Java Development Kit (JDK) 11 or higher
- Your Flask backend running (locally or deployed)
- Firebase project (you mentioned Firebase is already installed)

### 2. Configure Backend URL

Open `MainActivity.java` and update the `BASE_URL`:

```java
// For local testing (use your computer's IP, not localhost)
private static final String BASE_URL = "http://192.168.1.100:5000/";

// For production (your deployed backend)
private static final String BASE_URL = "https://your-domain.com/";
```

**Finding your local IP address:**

- Windows: Open CMD and type `ipconfig`, look for IPv4 Address
- Mac/Linux: Open Terminal and type `ifconfig` or `ip addr`

### 3. Add Navigation Icons

Create the following icon files in `res/drawable/`:

You need to create these vector drawable XML files:

**ic_home.xml:**

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M10,20v-6h4v6h5v-8h3L12,3 2,12h3v8z"/>
</vector>
```

**ic_pest.xml:**

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M12,2C6.48,2 2,6.48 2,12s4.48,10 10,10 10,-4.48 10,-10S17.52,2 12,2zM13,17h-2v-2h2v2zM13,13h-2L11,7h2v6z"/>
</vector>
```

**ic_calendar.xml:**

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M19,3h-1L18,1h-2v2L8,3L8,1L6,1v2L5,3c-1.11,0 -1.99,0.9 -1.99,2L3,19c0,1.1 0.89,2 2,2h14c1.1,0 2,-0.9 2,-2L21,5c0,-1.1 -0.9,-2 -2,-2zM19,19L5,19L5,8h14v11zM7,10h5v5L7,15z"/>
</vector>
```

**ic_shop.xml:**

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M7,18c-1.1,0 -1.99,0.9 -1.99,2S5.9,22 7,22s2,-0.9 2,-2 -0.9,-2 -2,-2zM1,2v2h2l3.6,7.59 -1.35,2.45c-0.16,0.28 -0.25,0.61 -0.25,0.96 0,1.1 0.9,2 2,2h12v-2L7.42,15c-0.14,0 -0.25,-0.11 -0.25,-0.25l0.03,-0.12 0.9,-1.63h7.45c0.75,0 1.41,-0.41 1.75,-1.03l3.58,-6.49c0.08,-0.14 0.12,-0.31 0.12,-0.48 0,-0.55 -0.45,-1 -1,-1L5.21,4l-0.94,-2L1,2zM17,18c-1.1,0 -1.99,0.9 -1.99,2s0.89,2 1.99,2 2,-0.9 2,-2 -0.9,-2 -2,-2z"/>
</vector>
```

**ic_knowledge.xml:**

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M20,2L4,2c-1.1,0 -1.99,0.9 -1.99,2L2,22l4,-4h14c1.1,0 2,-0.9 2,-2L22,4c0,-1.1 -0.9,-2 -2,-2zM6,9h12v2L6,11L6,9zM14,14L6,14v-2h8v2zM18,8L6,8L6,6h12v2z"/>
</vector>
```

### 4. Firebase Configuration

1. Download `google-services.json` from your Firebase console
2. Place it in `AndroidApp/app/` directory
3. Make sure the package name matches: `com.kisanseva.app`

### 5. Build and Run

1. Open Android Studio
2. File → Open → Select `AndroidApp` folder
3. Wait for Gradle sync to complete
4. Connect your Android device or start an emulator
5. Click Run (Green play button) or press Shift+F10

## 📂 Project Structure

```
AndroidApp/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/kisanseva/app/
│   │   │   │   ├── MainActivity.java          # Main WebView activity
│   │   │   │   └── SplashActivity.java        # Splash screen
│   │   │   ├── res/
│   │   │   │   ├── layout/
│   │   │   │   │   ├── activity_main.xml      # Main layout
│   │   │   │   │   └── activity_splash.xml    # Splash layout
│   │   │   │   ├── menu/
│   │   │   │   │   └── bottom_navigation_menu.xml
│   │   │   │   ├── values/
│   │   │   │   │   ├── colors.xml             # App colors
│   │   │   │   │   ├── strings.xml            # App strings
│   │   │   │   │   └── themes.xml             # App themes
│   │   │   │   └── drawable/                   # Icons and drawables
│   │   │   └── AndroidManifest.xml
│   │   └── build.gradle                        # App dependencies
│   └── google-services.json                    # Firebase config
└── build.gradle                                 # Project config
```

## 🔧 Key Configuration Files

### MainActivity.java

- WebView configuration for your Flask backend
- Bottom navigation setup
- File upload handling
- Permission management

### AndroidManifest.xml

- All required permissions (Camera, Storage, Location, Internet)
- Activity declarations
- FileProvider for camera/file uploads

## 🎨 Customization

### Change App Colors

Edit `res/values/colors.xml` to match your brand:

```xml
<color name="primary_green">#2D5016</color>
<color name="accent_green">#4A7C2C</color>
```

### Update App Name

Edit `res/values/strings.xml`:

```xml
<string name="app_name">KisanSeva</string>
```

### Change App Icon

Replace files in `res/mipmap-*/ic_launcher.png` with your logo

## 📱 Testing

### Test Locally

1. Start your Flask backend: `python app.py`
2. Find your computer's IP address
3. Update `BASE_URL` in MainActivity.java
4. Run the app on your phone (connected to same WiFi)

### Test Production

1. Deploy your Flask app to a hosting service (Heroku, PythonAnywhere, etc.)
2. Update `BASE_URL` with your deployed URL
3. Build and test the app

## 🐛 Troubleshooting

### App shows blank screen

- Check if Flask backend is running
- Verify BASE_URL is correct
- Check network connectivity
- Look at Android Logcat for errors

### File uploads not working

- Ensure camera and storage permissions are granted
- Check FileProvider configuration in AndroidManifest.xml
- Verify file paths configuration

### Can't connect to localhost

- Use your computer's IP address, not `localhost` or `127.0.0.1`
- Ensure phone and computer are on same WiFi network
- Check if Flask is running with `host='0.0.0.0'`

## 📦 Building APK for Distribution

### Debug APK (for testing)

```bash
./gradlew assembleDebug
```

APK location: `app/build/outputs/apk/debug/app-debug.apk`

### Release APK (for production)

```bash
./gradlew assembleRelease
```

APK location: `app/build/outputs/apk/release/app-release.apk`

**Note:** For release builds, you need to:

1. Generate a keystore
2. Configure signing in `build.gradle`
3. Sign the APK

## 🚀 Deploying Your Backend

Since the app uses WebView to load your Flask backend, you need to deploy your Flask app online:

### Option 1: PythonAnywhere (Free)

1. Sign up at pythonanywhere.com
2. Upload your Flask files
3. Configure WSGI file
4. Get your URL (e.g., `yourname.pythonanywhere.com`)

### Option 2: Heroku

1. Create Heroku account
2. Install Heroku CLI
3. Deploy Flask app
4. Get your URL

### Option 3: Railway.app

1. Sign up at railway.app
2. Connect GitHub repo
3. Deploy automatically
4. Get your URL

## 📝 Important Notes

1. **CORS**: Your Flask backend should allow requests from mobile app:

```python
from flask_cors import CORS
CORS(app)
```

2. **HTTPS**: For production, use HTTPS for security

3. **API Keys**: Keep your API keys secure, don't hardcode them

4. **Testing**: Test on multiple devices and Android versions

5. **Permissions**: Request permissions at runtime for Android 6.0+

## 📞 Support

If you encounter issues:

1. Check Android Logcat for errors
2. Verify Flask backend is accessible
3. Test backend in mobile browser first
4. Check all file paths and URLs

## 🎉 Next Steps

1. ✅ Set up the project in Android Studio
2. ✅ Configure backend URL
3. ✅ Add navigation icons
4. ✅ Add Firebase configuration
5. ✅ Test on device/emulator
6. ✅ Deploy Flask backend online
7. ✅ Update BASE_URL to production
8. ✅ Build release APK
9. ✅ Publish to Google Play Store (optional)

Good luck with your KisanSeva Android app! 🌾📱
