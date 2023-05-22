from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
  request.session['name'] = 'Akshansh'
  return render (request,'enroll/setsession.html')

def getsession(request):
 if 'name' in request.session:
  name = request.session.get('name')
  request.session.modified == True
  return render (request,'enroll/getsession.html',{'name':name})
 else:
   return HttpResponse("your session has been expired")
 
def delsession(request):
   # if 'name' in request.session:
   #   del request.session['name']# not completely deleted
   request.session.flush()#completely deleted from database(dbsqlite) too
   return render(request,'enroll/delsession.html')
