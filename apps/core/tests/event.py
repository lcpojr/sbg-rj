from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.event import Event

from faker import Faker

import pytz

factory = Faker("pt_BR")
tzinfo = pytz.utc


class EventCreateTestCase(TestCase):
    """
    Tests the event creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Event.objects.create(
                title=factory.text(max_nb_chars=50),
                resume=factory.text(max_nb_chars=150),
                description=factory.text(max_nb_chars=200),
                slug=factory.slug(),
                slideshow=factory.boolean(),
                image=factory.file_path(extension="jpg"),
                icon=factory.file_path(extension="png"),
                apresentation=factory.file_path(extension="pdf"),
                starts_at=factory.date_time_this_year(before_now=True, tzinfo=tzinfo),
                ends_at=factory.date_time_this_year(after_now=True, tzinfo=tzinfo),
            )
        )

    def test_fails_on_creation_if_params_are_invalid(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create()

    def test_fails_on_creation_if_already_exist(self):
        event = Event.objects.create(
            title=factory.text(max_nb_chars=50),
            resume=factory.text(max_nb_chars=150),
            description=factory.text(max_nb_chars=200),
            slug=factory.slug(),
            slideshow=factory.boolean(),
            image=factory.file_path(extension="jpg"),
            icon=factory.file_path(extension="png"),
            apresentation=factory.file_path(extension="pdf"),
            starts_at=factory.date_time_this_year(before_now=True, tzinfo=tzinfo),
            ends_at=factory.date_time_this_year(after_now=True, tzinfo=tzinfo),
        )

        with self.assertRaises(IntegrityError):
            Event.objects.create(
                title=event.title,
                resume=event.resume,
                description=event.description,
                slug=event.slug,
                slideshow=event.slideshow,
                image=event.image,
                icon=event.icon,
                apresentation=event.apresentation,
                starts_at=event.starts_at,
                ends_at=event.ends_at,
            )
