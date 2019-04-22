from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.user import User

from faker import Faker

import pytz

factory = Faker("pt_BR")


class UserCreateTestCase(TestCase):
    """
    Tests the user creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            User.objects.create(
                first_name=factory.first_name(),
                last_name=factory.last_name(),
                email=factory.free_email(),
                password=factory.password(),
                is_active=factory.boolean(),
                is_staff=factory.boolean(),
                is_superuser=factory.boolean(),
            )
        )

    def test_fails_on_creation_if_already_exist(self):
        user = User.objects.create(
            first_name=factory.first_name(),
            last_name=factory.last_name(),
            email=factory.free_email(),
            password=factory.password(),
            is_active=factory.boolean(),
            is_staff=factory.boolean(),
            is_superuser=factory.boolean(),
        )

        with self.assertRaises(IntegrityError):
            User.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                password=user.password,
                is_active=user.is_active,
                is_staff=user.is_staff,
                is_superuser=user.is_superuser,
            )
