from django.shortcuts import render, HttpResponse

from dashcore.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

from dashcore.personal import DB_Personal
from dashcore.models import Personal
from dashcore.forms import RegistrationForm


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
                )


            person = DB_Personal(form.cleaned_data['username'], form.cleaned_data['email'])
            person.make_person()

            """
            person = Personal.objects.create(
                username='someone',
                email='email@someone.come'
                    )
            """

            return HttpResponseRedirect('/register/success/')

    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
        })

    return render_to_response(
        'registration/register.html',
        variables,
        )


def register_success(request):

    return render_to_response(
        'registration/success.html',
        )


def logout_page(request):
    logout(request)

    return HttpResponseRedirect('/')


@login_required
def dash(request):
    user = '57926f28c1d6231e303861ca'
    loggedin_user = DB_Personal.find_person(user)

    return render_to_response(
        'dash.html', {
            'user': request.user,
            'loggedin_user': loggedin_user
            }
        )

def setting(request):
    user = '57926f28c1d6231e303861ca'
    loggedin_user = DB_Personal.find_person(user)


    return render(request, 'setting.html', {
        'loggedin_user': loggedin_user
        })
