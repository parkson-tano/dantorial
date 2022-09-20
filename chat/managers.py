from django.db.models import Manager, Q, QuerySet


class PersonalRoomManager(Manager):
    def by_user(self, **kwargs):
        # Return the room by a particular user
        user = kwargs.get('user')
        query = Q(user_1=user) | Q(user_2=user)
        qs = self.get_queryset().filter(query).distinct()
        return qs
