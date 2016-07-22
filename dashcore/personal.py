from django.utils import timezone

from dashcore.models import Personal
# Classes and methods for accessing Personal info

class DB_Personal:
    """
    Tools for accessing, appending Personal DB
    Arg:
        username - str()
        email - str()
    """
    def __init__(self, username, email):
        self.username = username,
        self.email = email

    def make_person(self):
        # Clean Username
        username = str(self.username)[2:-3]

        # Create DB entry
        person = Personal.objects.create(
            username=username,
            email=self.email,
            user_image='user.jpg',
            first_name='Not Set',
            last_name='Not Set',
            start_date=str(timezone.now())[:10],
            cakeday='Not Set',
            role='Not Set',
            rate='Not Set',
            holiday='25',
            med_provider='Not Set',
            med_plan='Net Set',
            dent_provider='Not Set',
            dent_plan='Not Set',
            curr_project='Not Set',
            pre_project='Not Set',
            sent_note='0',
            recv_note='0'
                )
        person.save()

    def find_person(user):
        person_detail = {}

        for person in Personal.objects:
            person_detail[str(user)] = {
                'username': person.username,
                'email': person.email,
                'user_image':person.user_image,
                'first_name':person.first_name,
                'last_name':person.last_name,
                'start_date':person.start_date,
                'cakeday':person.cakeday,
                'role':person.role,
                'rate':person.rate,
                'holiday':person.holiday,
                'med_provider':person.med_provider,
                'med_plan': person.med_plan,
                'dent_provider': person.dent_provider,
                'dent_plan': person.dent_plan,
                'curr_project': person.curr_project,
                'pre_project': person.pre_project,
                'sent_note': person.sent_note,
                'recv_note': person.recv_note
                }

        return person_detail
