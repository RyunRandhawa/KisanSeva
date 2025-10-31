import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",  # or use "localhost"
        user="RyunRandhawa",
        password="R005911"
    )
    print("✅ Connected successfully using pymysql!")
except Exception as e:
    print("❌ Error:", e)
