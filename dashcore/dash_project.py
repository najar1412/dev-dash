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
            asset='Not Set',
            location='Not Set',
            signedoff = False,
            flagdelete = False
            )

        project.save()

    def find_one():
        project_detail = {}

        return 'mock project'

    def find_all():
        project_all = {}

        for attri in Project.objects:
            project_all[attri.pk] = {
                'code':attri.code,
                'inc':attri.inc,
                'name':attri.name,
                'start':attri.start,
                'end':attri.end,
                'creator_id' :attri.creator_id,
                'assigned_user_id' :attri.assigned_user_id,
                'asset':attri.asset,
                'location' :attri.location,
                'signedoff' :attri.signedoff,
                'flagdelete' :attri.flagdelete
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
