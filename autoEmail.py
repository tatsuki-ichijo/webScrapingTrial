import getpass
import smtplib
from email import message

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'ranchivt@gmail.com'  # 送信元のアドレス
to_email = input("送り先は？：")  # 送りたい先のアドレス
username = 'ranchivt@gmail.com'  # Gmailのアドレス
password = getpass.getpass(prompt="パスワードを入力してください：")  # Gmailのパスワード

def Mailsend():
    # メールの内容を作成
    msg = message.EmailMessage()

    # メールの本文
    msg.set_content(bH)

    # 件名
    msg['Subject'] = '今日のBlogosヘッドライン'

    # メール送信元
    msg['From'] = from_email

    # メール送信先
    msg['To'] = to_email

    # メールサーバーへアクセス
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
