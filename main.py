import smtplib
from smtplib import SMTP
from email.utils import formataddr
from email.mime.text import MIMEText
import faker


def send(host, subject, from_addr, to_addr, msg):
    body = '\r\n'.join((  # 组合sendmail方法的邮件主体内容，各段以"\r\n"进行分离
        "From: %s" % "admin",
        "TO: %s" % to_addr,
        "subject: %s" % subject,
        "",
        msg
    ))
    server = SMTP()  # 创建一个smtp对象
    server.connect(host, 25)  # 链接smtp主机
    # server.login(from_, "123")  # 邮箱账号登陆
    server.sendmail(from_addr, to_addr, body)  # 发送邮件
    server.quit()  # 端口smtp链接


def send_mail():
    with open('textfile','rb') as fp:   # 读取文件内容
        msg=MIMEText(fp.read(),'plain','utf-8')   # 创建消息对象

    msg['Subject'] = "emailMessage"
    msg['From'] = formataddr("张三", "920664709@163.com")
    msg['To'] = formataddr("李四", "920664709@163.com")

    try:
        server = smtplib.SMTP() # 创建一个 SMTP() 对象
        server.connect("smtp.163.com","25") # 通过 connect 方法连接 smtp 主机
        # server.starttls() # 启动安全传输模式
        server.login("920664709@163.com","xxxxxx") # 邮箱账号登录校验
        server.sendmail("92066@163.com","92066@163.com", msg.as_string()) # 邮件发送
        server.quit() # 断开 smtp 连接
        print("邮件发送成功！")
    except Exception as e:
        print('失败：'+str(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fk = faker.Faker()
    mail_num = 200

    for i in range(mail_num):
        # host = fk.ipv4() # 定义smtp主机
        host = "127.0.0.1"  # 定义smtp主机
        subject = fk.paragraph()  # 定义邮件主题
        from_addr = fk.email()  # 定义邮件发件人
        to_addr = fk.email()  # 定义邮件收件人
        msg = ""
        msgs = fk.paragraphs(3)
        for m in msgs:
            msg = msg + m + '\n'
        # msg = "python is test smtp"  # 邮件内容,编码为ASCII范围内的字符或字节字符串，所以不能写中文
        send(host, subject, from_addr, to_addr, msg)
        if ((i + 1) % 5 == 0):
            print(str(i + 1)+" massages sent")    
