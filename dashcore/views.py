from django.shortcuts import render, HttpResponse

from dashcore.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

from dashcore.forms import RegistrationForm, UpdateRegistrationForm, AssetForm
from dashcore.dash_member import DashMember
from dashcore.dash_project import DashProject
from dashcore.dash_asset import DashAsset
from dashcore.models import Member, Project, Asset


# TODO: Refactor register to Member db
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

            member = DashMember(form.cleaned_data['username'], form.cleaned_data['email'])
            member.new()

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


def update_member(request):
    if request.method == 'POST':
        form = UpdateRegistrationForm(request.POST)
        if form.is_valid():
            field_update = []

            for item in form.cleaned_data:
                if form.cleaned_data[str(item)] != '':
                    field_update.append(str(item))
                    Member.objects(username=str(request.user)).update(
                        **{item: form.cleaned_data[item]
                        })


            member_id = DashMember.get_id(str(request.user))
            logged_member = DashMember.find(member_id)

            return render(request, 'setting.html', {
                'logged_member': logged_member
                })

@login_required
def dash(request):
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    return render_to_response(
        'dash.html', {
            'logged_member': logged_member
            }
        )

def setting(request):
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)


    return render(request, 'setting.html', {
        'logged_member': logged_member
        })

def project(request):

    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    project = DashProject.find_all()

    return render(request, 'project.html', {
        'logged_member': logged_member,
        'project': project
        })

def project_new(request):

    if request.method == 'POST':
        form = ProjectNewForm(request.POST)

        if form.is_valid():
            project = DashProject.new(
            code=form.cleaned_data['code'],
            inc=form.cleaned_data['inc']
                )

        # Get member details
        member_id = DashMember.get_id(str(request.user))
        logged_member = DashMember.find(member_id)

        project = DashProject.find_all()

        return render(request, 'project.html', {
            'logged_member': logged_member,
            'project': project
            })
    else:
        # TODO: Error Catching

        # Get member details
        member_id = DashMember.get_id(str(request.user))
        logged_member = DashMember.find(member_id)

        return render(request, 'project.html', {
            'logged_member': logged_member
            })

def project_del(request):
    if request.method == 'POST':
        DashProject.delete(request)

        return HttpResponseRedirect('/project/')

def project_asset(request):
    # TODO: Refactor to DashAsset
    if request.method == 'POST':
        form = AssetForm(request.POST)

        if form.is_valid():
            asset = DashAsset.new(
            collection=form.cleaned_data['collection'],
            project_id=str(form.cleaned_data['project_id']),
            member_id='Not Set'
                )


            Project.objects(pk=form.cleaned_data['project_id']).update(
                                    **{'asset': str(asset)
                                    })






    return HttpResponseRedirect('/project/')

def rank(request):

    # Get member details
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    return render(request, 'rank.html', {
        'logged_member': logged_member
        })

def asset_dash(request):
    asset_collect = {}

    for asset in Asset.objects():
        asset_collect[asset['id']] = {
            'name': asset['name'],
            'collection': asset['collection'],
            'project_id': asset['project_id'],
            'item_thumb': asset['item_thumb']
            }
    print(asset_collect)

    # Get member details using request.user
    # TODO: remove request.user call, and member id from somewhere
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    return render(request, 'asset_dash.html', {
        'logged_member': logged_member,
        'asset_collect': asset_collect
        })





@csrf_exempt
def asset(request):

    # Get asset details using id
    asset_detail = DashAsset.find(request.GET.get('query_name'))

    # Get member details using request.user
    # TODO: remove request.user call, and member id from somewhere
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    return render(request, 'asset.html', {
        'logged_member': logged_member,
        'asset_detail': asset_detail
        })

@csrf_exempt
def asset_new(request):

    if request.method == 'POST':
        form = AssetForm(request.POST)

        if form.is_valid():
            asset = DashAsset.new(
                collection=form.cleaned_data['collection']
            )


        # Get member details
        member_id = DashMember.get_id(str(request.user))
        logged_member = DashMember.find(member_id)

        return render(request, 'asset.html', {
            'logged_member': logged_member
            })
