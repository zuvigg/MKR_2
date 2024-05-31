from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewTests(TestCase):

    def setUp(self):
        Category.objects.create(name='Dessert')
        Recipe.objects.create(title='Chocolate Cake', category_id=1)
        Recipe.objects.create(title='Apple Pie', category_id=1)
        Recipe.objects.create(title='Pancakes', category_id=1)
        Recipe.objects.create(title='Brownies', category_id=1)
        Recipe.objects.create(title='Cookies', category_id=1)
        Recipe.objects.create(title='Ice Cream', category_id=1)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Cake')
        self.assertContains(response, 'Apple Pie')
        self.assertContains(response, 'Pancakes')
        self.assertContains(response, 'Brownies')
        self.assertContains(response, 'Cookies')
        self.assertNotContains(response, 'Ice Cream')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dessert (6)')
