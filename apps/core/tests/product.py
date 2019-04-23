from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models.product import Product

from faker import Faker

factory = Faker("pt_BR")


class ProductCreateTestCase(TestCase):
    """
    Tests the product creation units
    """

    def setUp(self):
        pass

    def test_succeeds_on_creation_if_params_are_correct(self):
        self.assertIsNotNone(
            Product.objects.create(
                name=factory.text(max_nb_chars=50),
                description=factory.text(max_nb_chars=200),
                slug=factory.slug(),
                image=factory.file_path(extension="jpg"),
                icon=factory.file_path(extension="png"),
                price_associated=10.5,
                price_non_associated=10.5,
            )
        )

    def test_fails_on_creation_if_params_are_invalid(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create()

    def test_fails_on_creation_if_already_exist(self):
        product = Product.objects.create(
            name=factory.text(max_nb_chars=50),
            description=factory.text(max_nb_chars=200),
            slug=factory.slug(),
            image=factory.file_path(extension="jpg"),
            icon=factory.file_path(extension="png"),
            price_associated=10.5,
            price_non_associated=10.5,
        )

        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name=product.name,
                description=product.description,
                slug=product.slug,
                image=product.image,
                icon=product.icon,
                price_associated=product.price_associated,
                price_non_associated=product.price_non_associated,
            )
