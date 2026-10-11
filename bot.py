import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_health_check_email():
    sender_email = os.environ.get("SENDER_EMAIL")
    app_password = os.environ.get("APP_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL", sender_email)

    if not sender_email or not app_password:
        print("Lỗi: Chưa cấu hình SENDER_EMAIL hoặc APP_PASSWORD trong GitHub Secrets!")
        return

    subject = "🤖 [Bot Health Check] Điểm danh ngầm từ GitHub Actions!"
    body = (
        "Xin chào Phát!\n\n"
        "Đây là email điểm danh tự động từ con bot chạy trên GitHub Actions.\n"
        "Nếu Phát nhận được email này, nghĩa là con bot vẫn đang hoạt động ngon lành, khỏe mạnh!\n\n"
        "Chúc Phát một ngày làm việc hiệu quả!"
    )

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Tự động gửi email điểm danh thành công!")
    except Exception as e:
        print(f"❌ Gửi email thất bại. Lỗi: {e}")

if __name__ == "__main__":
    send_health_check_email()
