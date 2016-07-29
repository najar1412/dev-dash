from django.utils import timezone

from dashcore.models import Project
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
            flagdelete = False
            )

        project.save()

        return project.id

    def find(project_id):
        project = {}

        asset_list = Project.objects.get(id=project_id).asset[1:-1].split(',')

        item = Project.objects.get(id=project_id)
        project[item.id] = {
            'code': item.code,
            'inc': item.inc,
            'name': item.name,
            'start': item.start,
            'end': item.end,
            'creator_id': item.creator_id,
            'assigned_user_id': item.assigned_user_id,
            'asset': asset_list,
            'location': item.location,
            'signedoff': item.signedoff,
            'flagdelete': item.flagdelete,
            }

        return project

    def find_all():
        project_all = {}

        project = Project.objects.all()
        for item in range(len(project)):
            project_all[project[item].pk] = {
                'code': project[item].code,
                'inc': project[item].inc,
                'name': project[item].name,
                'start': project[item].start,
                'end': project[item].end,
                'creator_id': project[item].creator_id,
                'assigned_user_id': project[item].assigned_user_id,
                'asset': project[item].asset,
                'location': project[item].location,
                'signedoff': project[item].signedoff,
                'flagdelete': project[item].flagdelete
                }

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
