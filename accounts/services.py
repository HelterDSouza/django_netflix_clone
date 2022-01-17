from typing import Dict

from accounts.models import CustomUser


class UserService(object):
    @staticmethod
    def create(
        *,
        email: str,
        password: str = None,
        **extra_fields,
    ) -> CustomUser:

        user = CustomUser.objects.create_user(
            email=email, password=password, **extra_fields
        )
        print(user.password)
        return user
