from django.shortcuts import render

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from login.models import Personal, Project, Comment, Media

# Create your views here.
#views.py

@csrf_protect
def register(request):

    """ Add employee to personal collection """
    employee = Personal.objects.create(
        email="free@delete.com",
        first_name="From Register",
        last_name="delete"
    )
    employee.save()


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
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

def profile(request):
    return  render_to_response('profile.html')

def register_success(request):
    return render_to_response('home.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    return render_to_response('home.html', { 'user': request.user })

def project(request):

    """ Add project to project collection """
    project = Project.objects.create(
        email="free@delete.com",
        first_name="From Register",
        last_name="delete"
    )
    project.save()

    return render_to_response('project.html')

def comment(request):

    """ Add comment to comment collection """
    comment = Comment.objects.create(
        email="free@delete.com",
        first_name="From Register",
        last_name="delete"
    )
    comment.save()

    return render_to_response('comment.html')

def media(request):

    """ Add project to project collection """
    media = Media.objects.create(
        email="free@delete.com",
        first_name="From Register",
        last_name="delete"
    )
    media.save()

    return render_to_response('media.html')
