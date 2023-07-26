from django.shortcuts import HttpResponse
class Brothermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("brother one time config & initialization")
    def __call__(self, request):
        print("brother before view")
        response = self.get_response(request)
        print("brother before view")
        return response

class Fathermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("father one time  config & initialization")
    def __call__(self, request):
        print("father before view")
        response = self.get_response(request)
        print("father before view")
        return response

class Mothermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("mother one time  config & initialization")
    def __call__(self, request):
        print("mother before view")
        response = HttpResponse(" i am mother middleware")
        print("mother before view")
        return response