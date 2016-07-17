import calendar
import datetime
from collections import namedtuple

from django.shortcuts import render

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

from login.models import Personal, Project, Comment, Media
from login.forms import NewProjectForm, NewCommentForm, DelNote, UpdateRegistrationForm


# Create your views here.
#views.py

@csrf_protect
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            """ Figure out where django saves User.object """
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            """ Add employee to personal collection """
            employee = Personal.objects.create(
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                first_name = "",
                last_name = "",
                dob = "",
                start_date = str(timezone.now())[:10],
                hols = "",
                med_provider = "",
                med_plan = "",
                dent_provider = "",
                dent_plan = "",
                curr_project = "",
                pre_project = "",
                role = "",
                user_image = "user_.jpg"
            )
            employee.save()

            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def stat(request):

    loggedin_user_info = {}
    for user in Personal.objects:
        if str(request.user) == user.username:
            loggedin_user_info = [
                user.id,
                user.first_name,
                user.last_name,
                user.role,
                user.dob,
                user.start_date,
                user.hols,
                user.med_provider,
                user.med_plan,
                user.dent_provider,
                user.dent_plan,
                user.curr_project,
                user.email,
                user.user_image,
                ]

    return  render(request, 'stat.html', {
        'loggedin_user_info': loggedin_user_info,
        'user': request.user
        })


@login_required
def setting(request):

    loggedin_user_info = {}
    for user in Personal.objects:
        if str(request.user) == user.username:
            loggedin_user_info = [
                user.id,
                user.first_name,
                user.last_name,
                user.role,
                user.dob,
                user.start_date,
                user.hols,
                user.med_provider,
                user.med_plan,
                user.dent_provider,
                user.dent_plan,
                user.curr_project,
                user.email,
                user.user_image,
                ]

    return  render(request, 'setting.html', {
        'loggedin_user_info': loggedin_user_info,
        'user': request.user
        })


def register_success(request):
    return render(request, 'registration/success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):


    projects_list = []
    project_datatable = "['row_label', 'bar_label', 's_date', 'e_date']"

    # Get current projects
    get_projects = [x.to_mongo() for x in Project.objects]

    for projects in get_projects:
        projects_list.append(projects.to_dict())

    # build datatable from database
    for project in projects_list:

        start_date_format = []
        end_date_format = []

        # Clean start date
        _date_start = project['project_start'].split('/')

        start_date_format.append(_date_start[2])
        start_date_format.append(_date_start[0])
        start_date_format.append(_date_start[1])

        # Clean end date
        _date_end = project['project_end'].split('/')

        end_date_format.append(_date_end[2])
        end_date_format.append(_date_end[0])
        end_date_format.append(_date_end[1])

        # append data table for current project chart
        project_datatable += ", [ '{}', '{}', new Date({}), new Date({}) ]".format(
            project['project_name'],
            project['project_name'],
            start_date_format,
            end_date_format
            )

    # user information
    loggedin_user_info = {}
    for user in Personal.objects:
        if str(request.user) == user.username:
            loggedin_user_info = [
                user.id,
                user.first_name,
                user.last_name,
                user.role,
                user.dob,
                user.start_date,
                user.hols,
                user.med_provider,
                user.med_plan,
                user.dent_provider,
                user.dent_plan,
                user.curr_project,
                user.email,
                user.user_image,
                ]

    # Get user messages
    user_message = {}
    user_message_count = 0
    for note in Comment.objects:
        if str(note.item_id) == str(request.user):
            user_message[user_message_count] = [
                    note.pk,
                    note.op_id,
                    note.item_id,
                    note.subject,
                    note.content,
                    note.parent_id,
                    ]


            user_message_count += 1

    form = NewProjectForm()
    comment_form = NewCommentForm()

    project_count = len(projects_list)

    return render(request, 'home.html', {
        'user': request.user,
        'form': form,
        'comment_form': comment_form,
        'project_datatable' :project_datatable,
        'loggedin_user_info': loggedin_user_info,
        'user_message': user_message,
        'project_count': project_count,
        }
        )


def project(request):
    return render(request, 'project.html')


def new_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get data from form
            project_code = form.cleaned_data['project_code']
            project_inc = form.cleaned_data['project_inc']
            project_name = form.cleaned_data['project_name']
            project_start = form.cleaned_data['project_start']
            project_end = form.cleaned_data['project_end']
            creator_id = form.cleaned_data['creator_id']

            # append data to database
            new_project = Project(
                project_code=project_code,
                project_inc=project_inc,
                project_name=project_name,
                project_start=project_start,
                project_end=project_end,
                creator_id=creator_id,
                    )

            new_project.save()

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewProjectForm()

    return render(request, 'name.html', {'form': form})


def update_user(request):

    if request.method == 'POST':
        form = UpdateRegistrationForm(request.POST)
        if form.is_valid():
            field_update = []


            for item in form.cleaned_data:
                if form.cleaned_data[item] != '':
                    field_update.append(str(item))
                    Personal.objects(username=str(request.user)).update(
                        **{item: form.cleaned_data[item]
                        })


    # user information
    loggedin_user_info = {}
    for user in Personal.objects:
        if str(request.user) == user.username:
            loggedin_user_info = [
                user.id,
                user.first_name,
                user.last_name,
                user.role,
                user.dob,
                user.start_date,
                user.hols,
                user.med_provider,
                user.med_plan,
                user.dent_provider,
                user.dent_plan,
                user.curr_project,
                user.email,
                user.user_image,
                ]

    return HttpResponseRedirect('/thank/')

def note(request):

    loggedin_sent_note = {}
    for note in Comment.objects(op_id=str(request.user)):

        loggedin_sent_note[note.pk] = {
        'note_id': note.pk,
        'op_id': note['op_id'],
        'item_id': note['item_id'],
        'subject': note['subject'],
        'content': note['content'],
        'rate': note['rate']
        }


    loggedin_recv_note = {}
    for note in Comment.objects(item_id=str(request.user)):

        loggedin_recv_note[note.pk] = {
        'note_id': note.pk,
        'op_id': note['op_id'],
        'item_id': note['item_id'],
        'subject': note['subject'],
        'content': note['content'],
        'rate': note['rate']
        }


    # user information
    loggedin_user_info = {}
    for user in Personal.objects:
        if str(request.user) == user.username:
            loggedin_user_info = [
                user.id,
                user.first_name,
                user.last_name,
                user.role,
                user.dob,
                user.start_date,
                user.hols,
                user.med_provider,
                user.med_plan,
                user.dent_provider,
                user.dent_plan,
                user.curr_project,
                user.email,
                user.user_image,
                ]


    return render(request, 'note.html', {
        'loggedin_user_info': loggedin_user_info,
        'loggedin_sent_note': loggedin_sent_note,
        'loggedin_recv_note': loggedin_recv_note
        })




def send_note(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            op_id = form.cleaned_data['op_id']
            item_id = form.cleaned_data['item_id']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            rate = form.cleaned_data['rate']

            # append data to database
            new_comment = Comment(
                op_id=op_id,
                item_id=item_id,
                subject=subject,
                content=content,
                rate=rate,
                    )

            new_comment.save()

            return HttpResponseRedirect('/note/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewCommentForm()

    return render(request, 'name.html', {'form': form})


def del_note(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = DelNote(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('whaaa')
            id_to_del = form.cleaned_data['id_to_del']
            print('----')
            print(id_to_del)

            doc_to_del = Comment(pk=id_to_del)
            doc_to_del.delete()



    return HttpResponseRedirect('/note/')

def media(request):

    """ Add project to project collection """
    media = Media.objects.create(
        email="free@delete.com",
        first_name="From Register",
        last_name="delete"
    )
    media.save()

    return render(request, 'media.html')
