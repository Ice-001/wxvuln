#!/usr/bin/env python3
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from run import send_dingtalk_notification, notify_daily_report

def test_notification():
    appkey = os.environ.get('DINGDING_ACCESS_TOKEN')
    appsecret = os.environ.get('DINGDING_SECRET')

    if not appkey or not appsecret:
        print('DINGDING_ACCESS_TOKEN or DINGDING_SECRET not set')
        sys.exit(1)

    title = '钉钉通知测试'
    content = '### 钉钉通知测试成功\n\n这是一条来自 GitHub Actions 的测试消息。\n\n时间: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    result = send_dingtalk_notification(title, content)
    if result:
        print('Test notification sent successfully')
    else:
        print('Test notification failed')
        sys.exit(1)

def test_report_notification(test_date):
    if test_date:
        notify_daily_report(test_date)
        print('Notification for ' + test_date + ' sent')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test_report_notification(sys.argv[1])
    else:
        test_notification()
