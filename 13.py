def send(message):
    import smtplib 
    from email.mime.text import MIMEText 

    # 寄件者，收件者
    from_addr = 'mikeyang0618@gmail.com'
    to_addr = 'mikeyang0618@gmail.com'


    smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465) 
    smtpssl.login(from_addr, "xxxxxxxxx")

    msg ='復興站PM2.5='+message
    mime=MIMEText(msg, "plain", "utf-8") 
    mime["Subject"]="空氣檢測"
    # 顯示的名稱
    mime["From"]="PM2.5監視器"
    mime["To"]= to_addr

    smtpssl.sendmail(from_addr, to_addr, mime.as_string())
    smtpssl.quit()


    import requests, json
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
while True:
    # 若來源資料為 https 則加上 verify=False 參數
    response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)

    sites = response.json()
    for site in sites:
        if site['Site'] == '復興':
            send(site)
            break
    time.sleep(60*60)
