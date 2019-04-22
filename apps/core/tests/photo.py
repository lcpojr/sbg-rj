from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.gallery import Gallery
from apps.core.models.photo import Photo

from faker import Faker

factory = Faker("pt_BR")


class PhotoCreateTestCase(TestCase):
    """
    Tests the photo creation units
    """

    def setUp(self):
        Gallery.objects.create(
            title="my test gallery",
            description=factory.text(max_nb_chars=200),
            category=factory.text(max_nb_chars=25),
            slug=factory.slug(),
            image=factory.file_path(extension="jpg"),
        )

    def test_succeeds_on_creation_if_params_are_correct(self):
        gallery = Gallery.objects.get(title="my test gallery")

        self.assertIsNotNone(
            Photo.objects.create(
                image=factory.file_path(extension="jpg"), gallery=gallery
            )
        )
