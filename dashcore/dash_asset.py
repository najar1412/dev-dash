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
        project.asset.append(str(asset.id))
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
        """delete('')
        Removes Asset from library.
        If Asset is assigned to a project, that reference is removed also.
        Aug:
            '', str - Asset Primary Key
        Note:
            Would using a foreign key, database relationship remove the step of
            having to remove the entry from the project?
        """
        asset = Asset.objects.get(pk=asset_id)

        if asset.project_id:
            project = Project.objects.get(pk=asset.project_id)
            print(project.asset)

            if asset_id in project.asset:
                print('----')
                print(asset_id)
                project.asset.remove(asset_id)
                project.save()
                print(project.asset)

            asset.delete()

        else:
            asset.delete()

        return True
