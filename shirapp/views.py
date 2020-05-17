from django.shortcuts import render
from .forms import ContactForm, FormSnippet


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)
    else:
        form = ContactForm()
    context = {
        'form':form
    }
    return render(request, "form.html", context)
    

def senippet_detail(request):
    if request.method == "POST":
        form = FormSnippet(request.POST)
        if form.is_valid():
            form.save()
    form = FormSnippet()
    context = {
        'form':form
    }
    return render(request, "form.html", context)