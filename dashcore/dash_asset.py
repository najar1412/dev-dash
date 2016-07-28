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
        asset = Asset.objects.create(
            collection='False',
            project_id=project_id,
            name='Not Set',
            item='user.jpg',
            item_thumb='user.jpg',
            tag='Not Set',
            member_id='Not Sec'
            )

        asset.save()

        Project.objects(pk=project_id).update(
            **{'asset': str(asset.id)
            })

        return project_id


    def find(asset_id):
        asset = {}

        asset_items = Asset.objects(id=asset_id)
        for item in asset_items:
            asset[item['id']] = {
                'collection': item['collection'],
                'project_id': item['project_id'],
                'name': item['name'],
                'item': item['item'],
                'item_thumb': item['item_thumb'],
                'tag': item['tag'],
                'member_id':item['member_id']
                }

        return asset
