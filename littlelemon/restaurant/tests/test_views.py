from django.test import TestCase
from restaurant.models import Menu

from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=80, inventory=80)
        Menu.objects.create(title="Ice Coffe", price=30, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data, serializer.data)
        self.assertIs

