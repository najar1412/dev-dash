from collections import defaultdict
from django.utils import timezone

from dashcore.models import Project, Asset
# Classes and methods for accessing Project info

class DashProject:
    def __init__(self, code, inc):
        self.code = code,
        self.inc = inc

    def new(code, inc):
        project = Project.objects.create(
            code=code,
            inc=inc,
            name='Not Set',
            start='Not Set',
            end='Not Set',
            creator_id='Not Set',
            assigned_user_id='Not Set',
            asset=[],
            location='Not Set',
            signedoff = False,
            flagdelete = False,
            project_image = 'user.jpg'
            )

        project.save()

        return project.id

    def find(project_id):
        project = {}

        item = Project.objects.get(id=project_id)
        project[item.id] = {
            'code': item.code,
            'inc': item.inc,
            'name': item.name,
            'start': item.start,
            'end': item.end,
            'creator_id': item.creator_id,
            'assigned_user_id': item.assigned_user_id,
            'asset': item.asset,
            'location': item.location,
            'signedoff': item.signedoff,
            'flagdelete': item.flagdelete
            }

        return project

    def find_all():
        project_all = {}
        asset_all = {}

        projects = Project.objects.all()
        for project in projects:

            project_all[project.pk] = {
                'code': project.code,
                'inc': project.inc,
                'name': project.name,
                'start': project.start,
                'end': project.end,
                'creator_id': project.creator_id,
                'assigned_user_id': project.assigned_user_id,
                'asset': {},
                'location': project.location,
                'signedoff': project.signedoff,
                'flagdelete': project.flagdelete
                }

            for asset_id in project.asset:
                asset = Asset.objects.get(id=asset_id)
                project_all[project.pk]['asset']['{}'.format(asset_id)] = asset.item_thumb


        print(project_all)




        return project_all


    def update():
        pass


    def delete(_request):
        del_id = []
        for key in _request.POST:
            del_id.append(_request.POST['delete'])

        del_id = list(set(del_id))[0]
        project_del = Project(pk=del_id)
        project_del.delete()

        return True

    def sign_off():
        pass

    def archive():
        pass
