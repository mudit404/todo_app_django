from django.test import TestCase
from todo_app.models import ToDoItem

class ToDoItemModelTest(TestCase):
    def test_create_todo_item(self):
        todo = ToDoItem.objects.create(
            title="Test Task",
            description="This is a test task",
        )
        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.description, "This is a test task")
