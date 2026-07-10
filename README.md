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



การเรียนใช้ภายหลัง
- source venv/bin/activate        # Windows: venv\Scripts\activate
- streamlit run app.py

สร้าง systemd Service
- sudo nano /etc/systemd/system/streamlit.service
ใส่
[Unit]
Description=Streamlit Dashboard
After=network.target

[Service]
Type=simple

User=ubuntu
Group=ubuntu

WorkingDirectory=/home/ubuntu/streamlit_app

Environment="PATH=/home/ubuntu/streamlit_app/venv/bin"

ExecStart=/home/ubuntu/streamlit_app/venv/bin/streamlit run app.py \
    --server.port=8501 \
    --server.address=0.0.0.0

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

หมายเหตุ: เปลี่ยน ubuntu เป็นชื่อผู้ใช้จริงของคุณ หากไม่ใช่ ubuntu (ตรวจสอบได้ด้วยคำสั่ง whoami)


Reload
sudo systemctl daemon-reload

Enable
sudo systemctl enable streamlit

เปิด Firewall
sudo ufw allow 8501/tcp

รีบูตทดสอบ
sudo reboot
