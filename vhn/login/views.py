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
def upload_media(request):
    media_return = {}

    if request.method == 'POST':
        form = UploadMedia(request.POST)

        if form.is_valid():
            media = Media.objects.create(
                op_id=request.user,
                media_type=form.cleaned_data['media_type'],
                media_name=form.cleaned_data['media_name'],
                media_pname=form.cleaned_data['media_pname'],
                media_pname_thumb=form.cleaned_data['media_pname_thumb'],
            )
            media.save()


            for attri in Media.objects(id=media.pk):
                media_return[attri.pk] = {
                    'op_id': attri.op_id,
                    'media_type': attri.media_type,
                    'media_pname': attri.media_pname,
                    'media_pname_thumb': attri.media_pname_thumb,
                    'note_id': attri.note_id
                }


    return render(request, 'media.html', {
        'media': media_return
    })

def media(request):

    # TODO: remove hardcore
    media_return = {}
    for attri in Media.objects(id='5790d868c1d6231cc0afc34f'):
        media_return[attri.pk] = {
            'op_id': attri.op_id,
            'media_type': attri.media_type,
            'media_pname': attri.media_pname,
            'media_pname_thumb': attri.media_pname_thumb,
            'note_id': attri.note_id
        }

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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]

            user_message_count += 1

    # TODO: remove hardcore
    note_return = {}
    for note in Comment.objects(item_id='5790d868c1d6231cc0afc34f'):
        note_return[note.pk] = {
            'op_id': note.op_id,
            'item_id': note.item_id,
            'subject': note.subject,
            'content': note.content,
            'rate': note.rate,
            'parent_id': note.parent_id
        }


    return render(request, 'media.html', {
    'media': media_return,
    'loggedin_user_info': loggedin_user_info,
    'user_message': user_message,
    'note': note_return
        })


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
                hols = "21",
                med_provider = "",
                med_plan = "",
                dent_provider = "",
                dent_plan = "",
                curr_project = "",
                pre_project = "",
                role = "",
                user_image = "user_.jpg",
                rate = "100"
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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]


    return  render(request, 'stat.html', {
        'loggedin_user_info': loggedin_user_info,
        'user': request.user,
        'user_message': user_message
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
                user.rate
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
                user.rate,
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
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


    project_collect = {}
    for project in Project.objects:

        project_collect[project.pk] = {
            'p_code': project['project_code'],
            'p_inc': project['project_inc'],
            'p_name': project['project_name'],
            'p_start': project['project_start'],
            'p_end': project['project_end'],
            'creator_id': project['creator_id'],
            'assigned_user_id': project['assigned_user_id'],
            'location': project['location'],
            'signedoff': project['signedoff'],
            'flagdelete': project['flagdelete'],
            'p_id': project.pk,

        }

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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]


    return render(request, 'project.html', {
        'loggedin_user_info': loggedin_user_info,
        'project_collect': project_collect,
        'user_message': user_message
        })



def del_project(request):


    id_to_del = []
    for key in request.POST:

        id_to_del.append(request.POST['delete'])

    id_to_del = list(set(id_to_del))[0]
    print(id_to_del)

    doc_to_del = Project(pk=id_to_del)
    doc_to_del.delete()


    return HttpResponseRedirect('/project/')


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

            return HttpResponseRedirect('/project/')

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
                user.rate
                ]

    return HttpResponseRedirect('/thank/')

def almanac(request):

    personal_collect = {}
    for x in Personal.objects:

        personal_collect[x.pk] = {
            'first_name': x['first_name'],
            'last_name': x['last_name'],
            'user_image': x['user_image'],
            'username': x['username'],
            'email': x['email'],
            'rate': x['rate']

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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]

            user_message_count += 1


    return render(request, 'almanac.html', {
        'loggedin_user_info': loggedin_user_info,
        'user_message': user_message,
        'personal_collect': personal_collect
        })

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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]

            user_message_count += 1



    return render(request, 'note.html', {
        'loggedin_user_info': loggedin_user_info,
        'loggedin_sent_note': loggedin_sent_note,
        'loggedin_recv_note': loggedin_recv_note,
        'user_message': user_message
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



def post_note(request):
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

            append_media = Media.objects(id=item_id)

            append_media.update(add_to_set__note_id=[new_comment.pk])

    note_return = {}
    for note in Comment.objects(item_id=item_id):
        note_return[note.pk] = {
            'op_id': note.op_id,
            'item_id': note.item_id,
            'subject': note.subject,
            'content': note.content,
            'rate': note.rate,
            'parent_id': note.parent_id
        }

    # TODO: remove hardcore
    media_return = {}
    for attri in Media.objects(id='5790d868c1d6231cc0afc34f'):
        media_return[attri.pk] = {
            'op_id': attri.op_id,
            'media_type': attri.media_type,
            'media_pname': attri.media_pname,
            'media_pname_thumb': attri.media_pname_thumb,
            'note_id': attri.note_id
        }


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
                user.rate
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
                    len(Comment.objects(item_id=str(request.user))), # one of these will be filterd with 'if read:'
                    len(Comment.objects(item_id=str(request.user)))
                    ]

            user_message_count += 1



    return render(request, 'media.html', {
    'media': media_return,
    'note': note_return,
    'loggedin_user_info': loggedin_user_info,
    'user_message': user_message
        })



def del_note(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = DelNote(request.POST)
        # check whether it's valid:
        if form.is_valid():

            id_to_del = form.cleaned_data['id_to_del']
            doc_to_del = Comment(pk=id_to_del)
            doc_to_del.delete()


    return HttpResponseRedirect('/media/')
