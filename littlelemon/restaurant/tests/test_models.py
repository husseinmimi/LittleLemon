from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        menu = Menu.objects.create(title="Ice Cream", price=80, inventory=80)
        self.assertEqual(menu.__str__(), "Ice Cream : 80")
