from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.news import News

from faker import Faker

import pytz

factory = Faker("pt_BR")
tzinfo = pytz.utc


class NewsCreateTestCase(TestCase):
    """
    Tests the news creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            News.objects.create(
                title=factory.text(max_nb_chars=50),
                resume=factory.text(max_nb_chars=200),
                description=factory.text(max_nb_chars=200),
                publish_date=factory.date_time_this_year(
                    before_now=True, tzinfo=tzinfo
                ),
                slug=factory.slug(),
                image=factory.file_path(extension="jpg"),
                icon=factory.file_path(extension="png"),
            )
        )

    def test_fails_on_creation_if_params_are_invalid(self):
        with self.assertRaises(IntegrityError):
            News.objects.create()

    def test_fails_on_creation_if_already_exist(self):
        news = News.objects.create(
            title=factory.text(max_nb_chars=50),
            resume=factory.text(max_nb_chars=200),
            description=factory.text(max_nb_chars=200),
            publish_date=factory.date_time_this_year(before_now=True, tzinfo=tzinfo),
            slug=factory.slug(),
            image=factory.file_path(extension="jpg"),
            icon=factory.file_path(extension="png"),
        )

        with self.assertRaises(IntegrityError):
            News.objects.create(
                title=news.title,
                resume=news.resume,
                description=news.description,
                publish_date=news.publish_date,
                slug=news.slug,
                image=news.image,
                icon=news.icon,
            )
