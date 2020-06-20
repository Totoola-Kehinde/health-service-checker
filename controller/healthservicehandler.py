import os
import requests, urllib.request, json
import datetime

class HandleService:
    """Class To Handle Request passed"""

    all_services = []
    uptime = None # Uptime For Microservice Availability 
    downtime = None # Downtime For Microservice Not Available
    number_of_services_in_each_microservices = None

    # Result Gotten from each service health check
    # This would be appended to the result list

    def process_services(self, services):
        # Get the Number Of Total Service List That is passed to this method
        count = 0
        total_service_list = len(services)
        self.number_of_services_in_each_microservices = total_service_list
        while count < total_service_list:
            count = count
            self.check_service(services[count])
            count += 1
        return self.all_services

    
    # Checks the Service and append the result
    def check_service(self, service):
        if service is None:
            self.message = 'Please Provide Service!'
            
        elif self.check_service_status(service):
            self.output = {
                'service': None,
                'message': None,
                'status': None,
                'uptime': self.uptime,
                'downtime': self.downtime
                }
            self.output['service'] = service
            self.output['status'] = 'Online'
            self.output['uptime'] = datetime.datetime.utcnow()
            self.output['message'] = "This Service is Available and Working Fine"     
            self.all_services.append(self.output)
            return self.all_services
            
        elif self.check_service_status(service) == False:
            self.output = {
                'service': None,
                'message': None,
                'status': None,
                'uptime': self.uptime,
                'downtime': self.downtime
                }
            self.output['service'] = service
            self.output['status'] = 'Fail'
            self.output['uptime'] = datetime.datetime.utcnow()
            self.output['message'] = "This Service is Not Found! - Does Not Exist!"
            self.all_services.append(self.output)
            return self.all_services

    # Check the service status and availabilty
    def check_service_status(self, service):
        return_bool = None
        res = requests.get(service) # get the respond code
        res_code = res.status_code # respond code from service check
        if res_code == 200:
            # Request Response is OK
            return_bool = True
        elif res_code == 404:
            return_bool = False
        return return_bool

    def calculate_uptime(self):
        pass

    def calculate_downtime(self):
        pass
