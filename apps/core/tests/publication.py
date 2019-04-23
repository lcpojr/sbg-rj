from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.publication import Publication

from faker import Faker

factory = Faker("pt_BR")


class PublicationCreateTestCase(TestCase):
    """
    Tests the publication creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Publication.objects.create(
                name=factory.text(max_nb_chars=50),
                category=factory.text(max_nb_chars=25),
                document=factory.file_path(extension="pdf"),
            )
        )

    def test_fails_on_creation_if_already_exist(self):
        publication = Publication.objects.create(
            name=factory.text(max_nb_chars=50),
            category=factory.text(max_nb_chars=25),
            document=factory.file_path(extension="pdf"),
        )

        with self.assertRaises(IntegrityError):
            Publication.objects.create(
                name=publication.name,
                category=publication.category,
                document=publication.document,
            )
