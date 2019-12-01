from psutil import cpu_percent as cpu
from threading import Timer
import logging
import smtplib
import datetime

host = 'smtp.gmail.com'
port = 587
username = 'aliilteriskeskin@gmail.com'
password = 'Your Password'
from_email = username
to_list = ['ali@heybooster.ai']

logging.basicConfig(filename='cpu_server_alert_system.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

CRITICAL = 10


def cpu_percent_controller():
    a = cpu()
    if a > CRITICAL:
        now = datetime.datetime.now()
        date = datetime.datetime.strftime(now, '%c')
        logging.warning(f'{date} - Alert CPU Usage Percent: {a}')
        message = f'''\
            Subject: Server Alert!!
            {date} -- CPU Usage Percent: {a}'''
        
        email_conn = smtplib.SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username, password)
        email_conn.sendmail(from_email, to_list, message)
        email_conn.quit()
    Timer(5.0, cpu_percent_controller).start()

if __name__ == '__main__':
    cpu_percent_controller()
