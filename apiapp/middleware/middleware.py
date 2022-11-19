import time
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

# Custom middlewares

class TimetakenMiddleware(MiddlewareMixin):
    '''
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        return self.get_response(request)
    '''
    #request
    def process_request(self, request) -> None:
        request.start_time = timezone.now()
        
    '''
    def process_view(self):
        return 
    
    #response
    
    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        print(exception.message)
        return 
    
    def process_template_response(self):
        return 
    '''
    
    def process_response(self, request, response) -> None:
        total_time = timezone.now() - request.start_time
        print("Time taken: {}".format(total_time))
        print("Response recieved: "+str(time.ctime(time.time())))
        return response