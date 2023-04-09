from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Mercedes-Benz",
            country="Germany"
        )
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="Test",
            password="12345Test",
            first_name="First",
            last_name="Last"
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Mercedes-Benz",
            country="Germany"
        )
        car = Car.objects.create(
            model="G 63",
            manufacturer=manufacturer
        )
        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license(self):
        username = "test"
        password = "12345Test"
        license_number = "XXX12345"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
