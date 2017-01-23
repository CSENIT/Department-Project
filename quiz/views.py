from django.shortcuts import render
from .models import quiz_data
# Create your views here.

def quiz(request):
	quiz_list=quiz_data.objects.all()
	html=''
	for quiz in quiz_list:
		html+='<div class="col s12 m3">'
		html+='<div class="card"><div class="card-image waves-effect waves-block waves-light">'
		html+='<img class="activator" src="'+request.scheme+'://'+request.get_host()+'/media/'+str(quiz.image)+'">'
		html+='</div>'
		html+='<div class="card-content">'
		html+='<span class="card-title activator grey-text text-darken-4">'+quiz.name+'</span>'
		html+='</div>'
		html+='<div class="card-reveal">'
		html+='<span class="card-title grey-text text-darken-4">'+quiz.name+'</span>'
		html+='<p>'+quiz.description+'</p>'
		html+='</div></div>'
		html+='</div>'
	json={}
	json['response']=html
	return render(request,"quiz/quiz.html",json)