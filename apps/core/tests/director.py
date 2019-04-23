from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.director import Director

from faker import Faker

import pytz

factory = Faker("pt_BR")
tzinfo = pytz.utc


class DirectorCreateTestCase(TestCase):
    """
    Tests the director creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Director.objects.create(
                first_name=factory.first_name(),
                last_name=factory.last_name(),
                role=factory.job(),
                email=factory.free_email(),
                started_at=factory.date_time_this_year(before_now=True, tzinfo=tzinfo),
                ends_at=factory.date_time_this_year(after_now=True, tzinfo=tzinfo),
            )
        )

    def test_fails_on_creation_if_params_are_invalid(self):
        with self.assertRaises(IntegrityError):
            Director.objects.create()

    def test_fails_on_creation_if_already_exist(self):
        director = Director.objects.create(
            first_name=factory.first_name(),
            last_name=factory.last_name(),
            role=factory.job(),
            email=factory.free_email(),
            started_at=factory.date_time_this_year(before_now=True, tzinfo=tzinfo),
            ends_at=factory.date_time_this_year(after_now=True, tzinfo=tzinfo),
        )

        with self.assertRaises(IntegrityError):
            Director.objects.create(
                first_name=director.first_name,
                last_name=director.last_name,
                role=director.role,
                email=director.email,
                started_at=director.started_at,
                ends_at=director.ends_at,
            )
