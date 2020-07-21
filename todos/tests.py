from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Todo, CustomUser, Category

class TodoTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', password='abc123', email='test@example.com')
        testuser1.save()
        
        # Create a todo
        test_todo = Todo.objects.create(
            author=testuser1, title='Todo title', body='Body content...')
        test_todo.save()
    
    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        author = f'{todo.author}'
        title = f'{todo.title}'
        body = f'{todo.body}'
        self.assertEqual(author, 'test@example.com')
        self.assertEqual(title, 'Todo title')
        self.assertEqual(body, 'Body content...')


    def test_todo_counts(self):
        counter = Todo.objects.all().count()
        self.assertEqual(counter, int('1'))       


    def test_todo_creation(self):
        t = Todo.objects.get(id=1)
        self.assertTrue(isinstance(t, Todo))
        self.assertEqual(t.__str__(), t.title)


    def test_todo_delete(self):
        todo = Todo.objects.get(id=1)
        todo.delete()
        counter = Todo.objects.all().count()
        self.assertEqual(counter, int('0'))
        no_response = self.client.get('todos/1/')
        self.assertEqual(no_response.status_code, 404)



class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testCat = Category.objects.create(
            subject = 'Important',
        )
        testCat.save()

    def test_cat_creation(self):
        c = Category.objects.get(id=1)
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.subject)