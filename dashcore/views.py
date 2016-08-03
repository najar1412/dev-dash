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


# TODO: Refactor register to Member DB
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
    #Get members current assets
    current_asset = {}
    member_id = DashMember.get_id(request.user)
    cur_asset = Asset.objects.all()
    for x in cur_asset:
        if str(member_id) in x.member_id:
            current_asset[x.pk] = x.item_thumb
    # Member information
    logged_member = DashMember.find(request.user)

    return render_to_response('dash.html', {
        'logged_member': logged_member,
        'current_asset': current_asset
            })


def setting(request):
    member_id = DashMember.get_id(str(request.user))
    logged_member = DashMember.find(member_id)

    return render(request, 'setting.html', {
        'logged_member': logged_member
        })


def project_dash(request):

    # Current project information
    project_all = DashProject.find_all()

    # Member information
    logged_member = DashMember.find(request.user)

    return render_to_response('project_dash.html', {
        'logged_member': logged_member,
        'project': project_all
        })


def project(request):
    # Asset information
    project = DashProject.find(request.GET.get('query_name'))
    # Member information
    logged_member = DashMember.find(request.user)

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

            return HttpResponseRedirect('/project?query_name={}'.format(str(project)))

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

        return HttpResponseRedirect('/project_dash/')


def project_asset(request):
    """
    asset = DashAsset.to_project(request.POST['project_id'])
    # Member information
    logged_member = DashMember.find(request.user)
    """
    return HttpResponseRedirect('/project?query_name={}'.format(request.POST['project_id']))


def rank(request):
    # Member information
    logged_member = DashMember.find(request.user)

    return render_to_response('rank.html', {
        'logged_member': logged_member
        })


def asset_dash(request):
    # Asset Information
    asset_collect = DashAsset.find_all()
    # Member information
    logged_member = DashMember.find(request.user)

    return render(request, 'asset_dash.html', {
        'logged_member': logged_member,
        'asset_collect': asset_collect
        })


def asset(request):
    # Get asset details using id
    asset_detail = DashAsset.find(request.GET.get('query_name'))

    for detail in asset_detail.keys():
        if asset_detail[detail]['collection'] == 'False':

            # Member information
            logged_member = DashMember.find(request.user)

            return render(request, 'asset.html', {
                'logged_member': logged_member,
                'asset_detail': asset_detail
                })

        else:

            # Member information
            logged_member = DashMember.find(request.user)

            return render(request, 'collection.html', {
                'logged_member': logged_member,
                'asset_detail': asset_detail
                })


def asset_new(request):
    if 'project_id' in request.POST:
        asset = DashAsset.to_project(request.POST['project_id'], request.POST['member_id'])

    elif 'member_id_collection' in request.POST:
        asset = DashAsset.new_collection(request.POST['member_id_collection'])

        # Get asset details using asset id
        asset_detail = DashAsset.find(asset.pk)
        # Member information
        logged_member = DashMember.find(request.user)

        return render(request, 'collection.html', {
            'logged_member': logged_member,
            'asset_detail': asset_detail
            })

    else:
        asset = DashAsset.new(request.POST['member_id'])

    # Get asset details using asset id
    asset_detail = DashAsset.find(asset.pk)
    # Member information
    logged_member = DashMember.find(request.user)

    return render(request, 'asset.html', {
        'logged_member': logged_member,
        'asset_detail': asset_detail
        })


def asset_del(request):
    #TODO: Need to remove asset id from project/datbase. if asset has project_id
    # Asset to delete
    if 'delete' in request.POST:
        DashAsset.delete(request.POST['delete'])
    elif 'contri' in request.POST:
        asset = Asset.objects.get(pk=request.POST['asset_id'])
        asset.member_id.append(request.POST['contri'])
        asset.save()
        # Asset Information
        asset_detail = DashAsset.find(request.POST['asset_id'])
        # Member information
        logged_member = DashMember.find(request.user)
        return render(request, 'asset.html', {
            'logged_member': logged_member,
            'asset_detail': asset_detail
            })

    # Asset Information
    asset_collect = DashAsset.find_all()
    # Member information
    logged_member = DashMember.find(request.user)

    return render(request, 'asset_dash.html', {
        'logged_member': logged_member,
        'asset_collect': asset_collect
        })
