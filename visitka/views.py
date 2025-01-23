from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import QuestForm
from .models import Service, Questoins

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        question = request.POST.get("question")

        quest_form = QuestForm(request.POST)

        if quest_form.is_valid():
            data = {"correct": True, "name": name, "email": email, "question": question}
            Quest = Questoins(name=name, email=email, question=question)
            Quest.save()
        else:
            data = {"correct": False, "value": "Данные некорректны!"}

        return TemplateResponse(request, "post_question.html", data)
    else:
        quest_form = QuestForm()
        return render(request, "contact.html", {"form": quest_form})

def sertificates(request):
    return render(request, "sertificates.html")

def service(request):
    services = Service.objects.all()
    serv_list = []
    for cur_serv in services:
        cur_data = {"name": cur_serv.name, "price": cur_serv.price, "description": cur_serv.description}
        serv_list.append(cur_data)
    data = {"serv_list": serv_list}
    return render(request, "service.html", context=data)

def post_question(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    question = request.POST.get("question")

    data = {"name": name, "email": email, "question": question}

    return TemplateResponse(request, "post_question.html", data)

