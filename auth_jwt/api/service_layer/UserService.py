
# Importando bibliotecas de terceiros
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserService:
    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_user(data):
        user = User(**data)
        user.save()
        return user

    @staticmethod
    def update_user(user_id, data):
        try:
            user = UserService.get_user_by_id(user_id)
            if user is not None:
                for attr, value in data.items():
                    setattr(user, attr, value)
                user.save()
                return user
            return None
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            if user is not None:
                user.delete()
                return True
            return False
        except ObjectDoesNotExist:
            return False
