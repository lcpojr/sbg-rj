from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.gallery import Gallery

from faker import Faker

import pytz

factory = Faker("pt_BR")
tzinfo = pytz.utc


class GalleryCreateTestCase(TestCase):
    """
    Tests the gallery creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Gallery.objects.create(
                title=factory.text(max_nb_chars=50),
                description=factory.text(max_nb_chars=200),
                category=factory.text(max_nb_chars=25),
                slug=factory.slug(),
                image=factory.file_path(extension="jpg"),
            )
        )

    def test_fails_on_creation_if_already_exist(self):
        gallery = Gallery.objects.create(
            title=factory.text(max_nb_chars=50),
            description=factory.text(max_nb_chars=200),
            category=factory.text(max_nb_chars=25),
            slug=factory.slug(),
            image=factory.file_path(extension="jpg"),
        )

        with self.assertRaises(IntegrityError):
            Gallery.objects.create(
                title=gallery.title,
                description=gallery.description,
                category=gallery.category,
                slug=gallery.slug,
                image=gallery.image,
            )
