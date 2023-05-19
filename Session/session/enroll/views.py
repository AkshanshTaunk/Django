from django.shortcuts import render

# Create your views here.
def setsession(request):
  request.session['name'] = 'Akshansh'
  return render (request,'enroll/setsession.html')

def getsession(request):
 name = request.session.get('name', default='Guest')
 return render (request,'enroll/getsession.html',{'name':name})

def delsession(request):
   # if 'name' in request.session:
   #   del request.session['name']# not completely deleted
   request.session.flush()#completely deleted from database(dbsqlite) too
   return render(request,'enroll/delsession.html')
