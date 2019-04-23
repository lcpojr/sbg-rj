from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.slideshow import Slideshow

from faker import Faker

factory = Faker("pt_BR")


class SlideshowCreateTestCase(TestCase):
    """
    Tests the slideshow creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Slideshow.objects.create(
                title=factory.text(max_nb_chars=50),
                resume=factory.text(max_nb_chars=100),
                image=factory.file_path(extension="jpg"),
            )
        )

    def test_fails_on_creation_if_already_exist(self):
        slideshow = Slideshow.objects.create(
            title=factory.text(max_nb_chars=50),
            resume=factory.text(max_nb_chars=100),
            image=factory.file_path(extension="jpg"),
        )

        with self.assertRaises(IntegrityError):
            Slideshow.objects.create(
                title=slideshow.title, resume=slideshow.resume, image=slideshow.image
            )
