from dashcore.models import Member

# tools for rank module

class DashRank():

    def get(member_id):
        """
        accepts member id as string
        returns members rank
        """
        member = Member.objects.get(id=member_id)

        return member.rank


    def add(member_id, action='default'):
        """
        accepts member id as string, action via string defaults to 'default'
        returns
        """

        reward = {
            'default': 10,
            'new_collection': 140,
            'delete': 10,
            }


        if action not in reward:
            action = 'default'

            member = Member.objects.get(id=member_id)
            member.rank = int(member.rank) + reward[action]
            member.save()

        else:
            member = Member.objects.get(id=member_id)
            member.rank = int(member.rank) + reward[action]
            member.save()
