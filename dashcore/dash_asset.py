from django.utils import timezone

from dashcore.models import Asset, Project
# Classes and methods for accessing Member info

class DashAsset:
    # TODO: Figure out why .new().asset[member_id] isnt being called from db
    def __init__(self, collection):
        collection = self.collection

    def new(collection, project_id='Not Set', member_id='Not Sec'):
        asset = Asset.objects.create(
            collection=collection,
            project_id=project_id,
            name='Not Set',
            item='Not Set',
            item_thumb='user.jpg',
            tag='Not Set',
            member_id=member_id
            )
        asset.save()

        return asset.id

    def to_project(project_id):
        listy = []
        asset = Asset(
            collection='False',
            project_id=project_id,
            name='Not Set',
            item='user.jpg',
            item_thumb='user.jpg',
            tag='Not Set',
            member_id='Not Sec'
                )
        asset.save()


        project = Project.objects.get(pk=project_id)

        if project.asset != '{}':
            string_clean = str(project.asset)[1:-1].split(',')
            string_clean.append(asset.id)
            project.asset = string_clean
        else:
            project.asset = [asset.id]

        project.save()

        return asset


    def find(asset_id):
        asset = {}

        item = Asset.objects.get(id=asset_id)
        asset[item.id] = {
            'collection': item.collection,
            'project_id': item.project_id,
            'name': item.name,
            'item': item.item,
            'item_thumb': item.item_thumb,
            'tag': item.tag,
            'member_id':item.member_id
            }

        return asset

    def find_all():
        asset_collect = {}

        asset = Asset.objects.all()
        for item in range(len(asset)):
            asset_collect[asset[item].pk] = {
                'collection': asset[item].collection,
                'project_id': asset[item].project_id,
                'name': asset[item].name,
                'item': asset[item].item,
                'item_thumb': asset[item].item_thumb,
                'tag': asset[item].tag,
                'member_id': asset[item].member_id
                }
        return asset_collect


    def delete(asset_id):
        project_id = Asset.objects.get(id=asset_id).project_id

        try:
            asset_list = Project.objects.get(id=project_id).asset[1:-1].split(',')
            if asset_id in asset_list:
                asset_list.remove(asset_id)
        except:
            pass

        asset = Asset.objects.get(id=asset_id)

        if asset.project_id:
            try:
                project = Project.objects.get(id=asset.project_id)
                project.asset = asset_list
                project.save()
            except:
                pass

            asset.delete()

        else:
            asset.delete()

        return True
