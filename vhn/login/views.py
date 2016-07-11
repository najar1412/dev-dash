from django.shortcuts import render

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from login.models import Personal, Project, Comment, Media
from login.forms import NewProject, NameForm


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
    variables = RequestContext(request, {'form': form})

    return render_to_response('registration/register.html', variables)

def profile(request):
    return  render_to_response('profile.html')

def register_success(request):
    return render_to_response('home.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):

    form = NameForm()

    return render(request, 'home.html', {'user': request.user, 'form': form})


"""
def project(request):


    ''' Add project to project collection'''
    project = Project.objects.create(
        project_code="RO-001",
        project_inc="001",
        project_name="1 Garret Pl",
        project_start="The start date",
        project_end="The end date"
    )
    project.save()



    return render_to_response('project.html')

"""



def project(request):
    # if this is a POST request we need to process the form data
    form = NewProject()
    return render(request, 'project.html', {'form': form})






from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})





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
