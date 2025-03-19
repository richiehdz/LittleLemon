from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Taco Pastor", price=2.00, inventory=100)
        self.item2 = Menu.objects.create(title="Taco Asada", price=2.5, inventory=150)
        self.item3 = Menu.objects.create(title="Quesadilla Mixta", price=5, inventory=50)
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 3)