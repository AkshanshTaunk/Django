from django.shortcuts import render

# Create your views here.
def setcookie(request):
   response = render(request,'enroll/setcookie.html')
#    response.set_cookie('name','yash',max_age=60)
#    response.set_cookie('lname','taunk',max_age=60)
   response.set_signed_cookie('name','yash',salt='nm',max_age=60)
   return response

def getcookie(request):
#    name = request.COOKIES['name']
   name = request.get_signed_cookie('name',salt='nm')
#    lname = request.COOKIES.get('lname',"guest")
   return render(request,'enroll/getcookie.html',{'nm':name})

def delcookie(request):
   response = render(request,'enroll/delcookie.html')
   response.set_cookie('name')
   return response