from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Todo

class TodoTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', password='abc123')
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
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Todo title')
        self.assertEqual(body, 'Body content...')