วิธีติดตั้ง

# 1. สร้าง virtual environment (แนะนำ)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. ติดตั้งไลบรารีที่จำเป็น
pip install -r requirements.txt
requirements.txt มี:

streamlit — ตัวสร้างเว็บแอป
psutil — อ่านค่า CPU/RAM
streamlit-autorefresh — ทำให้หน้าเว็บรีเฟรชอัตโนมัติทุกวินาที (จำเป็นสำหรับนาฬิกาแบบเรียลไทม์)

#วิธีใช้งาน
bashstreamlit run app.py

จากนั้นเบราว์เซอร์จะเปิดขึ้นอัตโนมัติที่ http://localhost:8501 (ถ้าไม่เปิดเอง ให้เปิดลิงก์นี้เอง)
หมายเหตุ

แอปนี้ต้องรันบนเครื่อง/เซิร์ฟเวอร์จริง (ไม่ใช่ผ่านหน้าแชทนี้) เพราะต้องอ่านค่า CPU/RAM ของเครื่องที่รันจริง
