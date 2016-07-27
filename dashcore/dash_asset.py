from django.utils import timezone

from dashcore.models import Asset
# Classes and methods for accessing Member info

class DashAsset:
    def __init__(self, collection):
        collection = self.collection

    def new(collection, project_id='Not Set'):
        asset = Asset.objects.create(
            collection=collection,
            project_id=project_id,
            name='Not Set',
            item='Not Set',
            item_thumb='Not Set',
            tag='Not Set'
            )
        asset.save()

        return asset.id
