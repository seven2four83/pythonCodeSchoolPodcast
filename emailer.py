import requests
import smtplib
def get_emails():
    emails = {}
    try:
        email_file = open('emails.txt','r')
        for emailId in email_file:
            (email,name) = emailId.split(',')
            emails[email] = name.strip()
        return emails
    except FileNotFoundError as err:
        print(err)   

def send_emails(emails,schedule,weather_forecasts):
    server = smtplib.SMTP('smtp.gmail.com','587')
    server.starttls()
    password = input('Enter gmail password')
    from_email = 'flying.through.python@gmail.com'
    to_email = 'vikibornin1991@gmail.com'
    server.login(from_email, password)
    server.sendmail(from_email, to_email,'Yours,\nPython Noob')
    server.quit()
    return

def get_schedule():
    try:
        schedule_file = open('schedule.txt','r')
        schedules = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedules

def get_weather_forecasts():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=f641b59e03463c808393605f493b1f93'
    request = requests.get(url)
    weather_json = request.json()
    desc = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']    
    #print (desc, temp_min, temp_max)

    return 'The circus weather forecast is ', desc, ' with a min of ',int(temp_min),' and a max of ',int(temp_max)
    
def main():
    emails = get_emails()
    schedule = get_schedule()
    weather_forecasts = get_weather_forecasts()
    send_emails(emails, schedule, weather_forecasts)

main()
