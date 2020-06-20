from flask import Flask, render_template, url_for
from healthchecks.services.users import UserService
from healthchecks.services.sms_notifications import SmsService
from healthchecks.services.manage_pages import ManagePageService
from healthchecks.services.email_notifications import EmailService
from healthchecks.services.company_settings import CompanySettingsService
from healthchecks.services.auth import AuthService
import threading

def healthChecktimer():
    # threading.Timer(600.0, healthChecktimer).start()
    
    # Managing Users Microservices Health Check
    Userhandler = UserService()
    Userhandler.create_service_url()
    # Userhandlernum = Userhandler.number_of_services_in_each_microservices
    UserhandlerHealthCheck = Userhandler.process_services(Userhandler.services)

    # SMS Notifications Microservices Health Check
    SmsNotificationHandler = SmsService()
    SmsNotificationHandler.create_service_url()
    # smsnum = SmsNotificationHandler.number_of_services_in_each_microservices
    SmsNotificationHandlerHealthCheck = SmsNotificationHandler.process_services(SmsNotificationHandler.services)

    # Managing Static and External Pages Microservices Health Check
    ManagePageHandler = ManagePageService()
    ManagePageHandler.create_service_url()
    # managenum = ManagePageHandler.number_of_services_in_each_microservices
    ManagePageHandlerHealthCheck = ManagePageHandler.process_services(ManagePageHandler.services)

    # Email Notifications Microservices Health Check
    EmailHandler = EmailService()
    EmailHandler.create_service_url()
    # emailnum = EmailHandler.number_of_services_in_each_microservices
    EmailHandlerHealthCheck = EmailHandler.process_services(EmailHandler.services)

    # Managing Company Settings Microservices Health Check
    CompanyHandler = CompanySettingsService()
    CompanyHandler.create_service_url()
    # companynum = CompanyHandler.number_of_services_in_each_microservices
    CompanyHandlerHealthCheck = CompanyHandler.process_services(CompanyHandler.services)

    # Authentication Microservices Health Check
    AuthHandler = AuthService()
    AuthHandler.create_service_url()
    # authnum = AuthHandler.number_of_services_in_each_microservices
    AuthHandlerHealthCheck = AuthHandler.process_services(AuthHandler.services)

    return {'Users':UserhandlerHealthCheck, 'Sms Notifications':SmsNotificationHandlerHealthCheck, 'Manage Pages':ManagePageHandlerHealthCheck, 'Email Services':EmailHandlerHealthCheck, 'Company Services':CompanyHandlerHealthCheck, 'Auth Services':AuthHandlerHealthCheck}


app = Flask(__name__)

@app.route('/')
def index():
    data = healthChecktimer()
    UsersData = data['Users']
    smsData = data['Sms Notifications']
    emailData = data['Email Services']
    managePagesData = data['Manage Pages']
    companyData = data['Company Services']
    authData = data['Auth Services']

    return render_template('dashboard.html', UsersData=UsersData, smsData=smsData, emailData=emailData, managePagesData=managePagesData, companyData=companyData, authData=authData)

if __name__ == "__main__":
    app.run(debug=True)