from django.shortcuts import render, redirect, get_object_or_404
from .models import Desk, Contact, Places, Answer, RASPUNSURI
from .forms import UserForm, ContactForm, DeskForm, AnswerForm
from django.views import generic
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import datetime

############PAGINA_PRINCIPALA###############
class HomeView(generic.View):
    def get(self, request):
        date_posted = datetime.datetime.now().year
        new_model = Desk.objects.all()
        if request.method == "POST":
            locatie = request.POST.get('locatie')
            lookup = (Q(tara__icontains = locatie))
            model = Desk.objects.filter(lookup)
            return render(request, "my_app/home.html", {'date_posted':date_posted, 'model':model})
        else:
            return render(request, "my_app/home.html", {'date_posted':date_posted, 'new_model':new_model})

def contact(request):
    date_posted = datetime.datetime.now().year
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ContactForm()
    context = {
        'date_posted':date_posted,
        'form':form,
    }
    return render(request, "my_app/contact.html", context)

def all_desk(request):
    date_posted = datetime.datetime.now().year
    model = Desk.objects.all()
    context = {
        'date_posted':date_posted,
        'model':model
    }
    return render(request, "my_app/all_desk.html", context)

@login_required
def cautare_birouri(request):
    new_model = Desk.objects.all()
    if request.method == "POST":
        date_posted = datetime.datetime.now().year
        locatie = request.POST.get("locatie")
        lookup = (Q(tara__icontains = locatie))
        model = Desk.objects.filter(lookup)
        return render(request, "my_app/cautare_birouri.html", {'date_posted':date_posted, 'model':model, 'new_model':new_model})
    else:
        return render(request, "my_app/cautare_birouri.html", {'date_posted':date_posted, 'model':model, 'new_model':new_model})

##############################################
#############INREGISTRARE#####################
##############################################

def inregistrare(request):
    date_posted = datetime.datetime.now().year
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:intra_in_cont')
        else:
            messages.info(request, "Parola ta este prea scurta! Te rugam sa folosesti minim 8 caractere, cifre si semne de punctuatie!")
    context = {
        'date_posted':date_posted,
        'form':form,
    }
    return render(request, "my_app/inregistrare.html", context)

def user_login(request):
    date_posted = datetime.datetime.now().year
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Numele sau parola sunt incorecte!")
    context = {
        'date_posted':date_posted,
    }
    return render(request, "my_app/intra_in_cont.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

###############################################
#################CONTUL_MEU####################
###############################################

@login_required
def contul_meu(request, pk):
    date_posted = datetime.datetime.now().year
    anunt = User.objects.get(id=pk)
    user = request.user
    model = user.favorit.all()
    context = {
        'date_posted':date_posted,
        'model':model,
        'anunt':anunt,
    }
    return render(request, "my_app/contul_meu.html", context)

@login_required
def intrebari(request):
    date_posted = datetime.datetime.now().year
    form = AnswerForm()
    optiune1 = RASPUNSURI[0][0]
    optiune2 = RASPUNSURI[1][0]
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AnswerForm()
    context = {
        'form':form,
        'date_posted':date_posted,
        'optiune1':optiune1,
        'optiune2':optiune2,
    }
    return render(request, "my_app/intrebari.html", context)

@login_required
def pag_desk(request, pk):
    date_posted = datetime.datetime.now().year
    model = Desk.objects.get(id=pk)
    new_model = Places.objects.all()
    context = {
        'date_posted':date_posted,
        'model':model,
        'new_model':new_model,
    }
    return render(request, "my_app/pag_desk.html", context)

@login_required
def editeaza_profil(request, pk):
    date_posted = datetime.datetime.now()
    model = User.objects.get(id=pk)
    form = UserForm(instance=model)
    if request.method == "POST":
        form = UserForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
        else:
            form = UserForm()
    context = {
        'date_posted':date_posted,
        'form':form,
    }
    return render(request, "my_app/editeaza_profil.html", context)

@login_required
def search_places(request, pk):
    date_posted = datetime.datetime.now().year
    new_model = Desk.objects.get(id=pk)
    if request.method == "POST":
        start_calendar = request.POST.get("start_calendar")
        end_calendar = request.POST.get("end_calendar")
        lookup = (Q(start_date__icontains = start_calendar) and Q(end_date__icontains = end_calendar))
        model = Places.objects.filter(lookup)
        return render(request, "my_app/search_places.html", {'date_posted':date_posted, 'model':model, 'new_model':new_model})
    else:
        return render(request, "my_app/search_places.html", {'date_posted':date_posted, 'new_model':new_model})

@login_required
def pag_places(request, pk):
    date_posted = datetime.datetime.now().year
    model = Places.objects.filter(id=pk)
    favorit_id = False
    anunt = Places.objects.get(id=pk)
    if anunt.favorit.filter(id=request.user.id).exists():
        favorit_id = True
    context = {
        'date_posted':date_posted,
        'model':model,
        'favorit_id':favorit_id,
        'anunt':anunt,
    }
    return render(request, "my_app/pag_places.html", context)

def desk_availability(request, pk):
    anunt = get_object_or_404(Places, id=request.POST.get('favorit'))
    favorit_id = False
    if anunt.favorit.filter(id=request.user.id).exists():
        anunt.favorit.remove(request.user)
        favorit_id = True
    else:
        anunt.favorit.add(request.user)
        favorit_id = False
    return HttpResponseRedirect(reverse("my_app:pag_places", args=[str(pk)]))

# Create your views here.
