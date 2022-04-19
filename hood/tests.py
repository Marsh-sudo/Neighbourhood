from django.test import TestCase
from .models import Post,Business,Neighbourhood

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.kasarani=Neighbourhood(name='kasarani',description='best neighborhood',health_number='07123453234')

    def test_instance(self):
        self.assertTrue(isinstance(self.kasarani,Neighbourhood))

    def test_create_method(self):
        self.kasarani.save()
        neighbors = Neighbourhood.objects.all()
        self.assertTrue(len(neighbors))
