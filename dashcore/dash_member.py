from django.utils import timezone

from dashcore.models import Member
# Classes and methods for accessing Member info

class DashMember:
    """
    Tools for accessing, appending Personal DB
    Arg:
        username - str()
        email - str()
    """
    def __init__(self, username, email):
        self.username = username,
        self.email = email


    def new(self):
        # Clean Username
        username = str(self.username)[2:-3]

        # Create DB entry
        member = Member.objects.create(
            username=username,
            email=self.email,
            user_image='user.jpg',
            first_name='Not Set',
            last_name='Not Set',
            start_date=str(timezone.now())[:10],
            cakeday='Not Set',
            role='Not Set',
            rank='1',
            holiday='25',
            med_provider='Not Set',
            med_plan='Net Set',
            dent_provider='Not Set',
            dent_plan='Not Set',
            curr_project='Not Set',
            pre_project='Not Set',
            sent_note='0',
            recv_note='0',
            assign_asset='Not Set'
                )
        member.save()


    def find(member_id):
        logged_member = {}
        # memberr = Member.objects.filter(username=member_id)
        member = Member.objects.get(username=member_id)
        logged_member[member.pk] = {
            'username': member.username,
            'email': member.email,
            'user_image': member.user_image,
            'first_name': member.first_name,
            'last_name': member.last_name,
            'start_date': member.start_date,
            'cakeday': member.cakeday,
            'role': member.role,
            'holiday': member.holiday,
            'med_provider': member.med_provider,
            'med_plan': member.med_plan,
            'dent_provider': member.dent_provider,
            'dent_plan': member.dent_plan,
            'curr_project': member.curr_project,
            'pre_project': member.pre_project,
            'assign_asset': member.assign_asset,
            'sent_note': member.sent_note,
            'recv_note': member.recv_note,
            'rank': member.rank
            }

        return logged_member


    def assign_asset():
        pass

    # Helper Methods
    def get_id(member):
        for member in Member.objects(username=member):
            return member.pk
