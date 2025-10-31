# 🚀 Quick Start Guide

## Step 1: Open in Android Studio

1. Open Android Studio
2. Click "Open an existing project"
3. Navigate to and select the `AndroidApp` folder
4. Wait for Gradle sync to complete (5-10 minutes)

## Step 2: Configure Your Backend URL

Edit `MainActivity.java` (line 36):

```java
private static final String BASE_URL = "http://YOUR_IP_HERE:5000/";
```

**Find your IP:**

- Windows: `ipconfig` in CMD → Look for IPv4 Address
- Mac/Linux: `ifconfig` or `ip addr`

## Step 3: Create Icon Files

Create these 5 files in `app/src/main/res/drawable/`:

1. `ic_home.xml` - Home icon
2. `ic_pest.xml` - Bug/diagnostic icon
3. `ic_calendar.xml` - Calendar icon
4. `ic_shop.xml` - Shopping cart icon
5. `ic_knowledge.xml` - Chat/forum icon

Copy the icon XML code from the main README.md file.

## Step 4: Add Firebase Config (Optional but Recommended)

1. Go to Firebase Console (console.firebase.google.com)
2. Create/Select your project
3. Download `google-services.json`
4. Place it in `app/` folder (same level as `build.gradle`)

## Step 5: Run Your Flask Backend

```bash
cd "Hackathon CGC"
python app.py
```

Make sure Flask runs on `0.0.0.0:5000` so mobile can access it:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Step 6: Run the App

1. Connect your Android phone via USB
2. Enable USB Debugging on your phone
3. Click the green "Run" button in Android Studio
4. Select your device
5. Wait for app to install and launch

## ✅ Checklist

- [ ] Android Studio installed
- [ ] Backend URL configured
- [ ] 5 icon files created
- [ ] Flask backend running
- [ ] Phone connected & USB debugging enabled
- [ ] App running on device

## 🐛 Common Issues

### App shows blank screen

- Check if Flask is running
- Verify IP address is correct
- Ensure phone and computer on same WiFi

### Icons not showing

- Make sure all 5 icon XML files are created
- Check file names match exactly

### Can't build/sync

- Check internet connection
- Try "File → Invalidate Caches / Restart"
- Update Android Studio to latest version

## 📱 For Production

Once testing works locally:

1. Deploy Flask to cloud (PythonAnywhere, Heroku, etc.)
2. Update `BASE_URL` to your deployed URL
3. Build release APK: `./gradlew assembleRelease`
4. Share or publish to Play Store

## Need Help?

- Check full README.md for detailed instructions
- View Android Logcat for error messages
- Test backend in mobile browser first
