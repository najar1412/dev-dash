from django.utils import timezone

from dashcore.models import Asset, Project
# Classes and methods for accessing Member info

class DashAsset:
    # TODO: Figure out why .new().asset[member_id] isnt being called from db
    def __init__(self, collection):
        collection = self.collection

    def new(member_id):

        asset = Asset.objects.create()
        asset.name = 'Not Set'
        asset.item = 'asset_.jpg'
        asset.item_thumb = 'asset_.jpg'
        asset.member_id.append(member_id)
        asset.save()

        return asset

    def new_collection(member_id):

        asset = Asset.objects.create(
            collection= 'True',
            name='Not Set',
            item='asset_collection.jpg',
            item_thumb='asset_collection.jpg'
            )
        asset.member_id.append(member_id)
        asset.save

        return asset

    def to_project(project_id, member_id):
        asset = Asset(
            collection='False',
            name='Not Set',
            project_id=project_id,
            item='asset_project.jpg',
            item_thumb='asset_project.jpg'
                )
        asset.member_id.append(member_id)
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
            'collect_asset': item.collect_asset,
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
                'collect_asset': asset[item].collect_asset,
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
            try:
                project = Project.objects.get(pk=asset.project_id)

                if asset_id in project.asset:
                    project.asset.remove(asset_id)
                    project.save()

            except:
                print('ERR: project_id in asset, cannot be located in DB')
                print('ERR: Deleting Asset Anyway')
                asset.delete()

            asset.delete()

        else:
            asset.delete()

        return True
