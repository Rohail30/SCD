from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
	# return HttpResponse("""<h1 style=""color:red"">Hello this is django"</h1>""")
	student = [
		{'name':'abdullah', 'age':22, 'program':'BSCS', 'batch':'2023'},
		{'name':'abdullah', 'age':22, 'program':'BSCS', 'batch':'2023'},
		{'name':'abdullah', 'age':22, 'program':'BSCS', 'batch':'2023'},
		{'name':'abdullah', 'age':22, 'program':'BSCS', 'batch':'2023'},
		{'name':'abdullah', 'age':22, 'program':'BSCS', 'batch':'2023'},
	]
	return render(request, 'home/index.html', context={'student': student})