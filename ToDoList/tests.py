from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import todoListCreate, todoListUpdate, todoListDelete, todoListView
from django.contrib.auth.models import User
from ToDoList.models import todoList

class TestUrls(SimpleTestCase):

    def test_url_todoListCreate(self):
        createview_url = reverse('todolist.new')
        self.assertEqual(resolve(createview_url).func, todoListCreate, 'Todolist CreateView testing failed!')
        self.assertEqual(resolve(createview_url).route, 'todolist/new/', 'Todolist route testing failed!')

    def test_url_todoListView(self):
        listview_url = reverse('todolist.all')
        self.assertEqual(resolve(listview_url).func.view_class, todoListView, 'Todolist ListView testing failed!')
        self.assertEqual(resolve(listview_url).route, 'todolist/allitem/', 'Todolist route testing failed!')

    def test_url_todoListUpdate(self):
        pk = 1
        listview_url = reverse('todoList.update', args=[pk])
        self.assertEqual(resolve(listview_url).func.view_class, todoListUpdate, 'Todolist UpdateView testing failed!')
        self.assertEqual(resolve(listview_url).route, 'todolist/item/update/<int:pk>/', 'Todolist route testing failed!')

    def test_url_todoListDelete(self):
        pk = 1
        listview_url = reverse('todoList.delete', args=[pk])
        self.assertEqual(resolve(listview_url).func.view_class, todoListDelete, 'Todolist DeleteView testing failed!')
        self.assertEqual(resolve(listview_url).route, 'todolist/item/delete/<int:pk>/', 'Todolist route testing failed!')

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username="scarlett",password="password321") 
        self.listviewurl = reverse('todolist.all')
        self.createviewurl = reverse('todolist.new')

    def test_createview_post(self):
        self.client.login(username="scarlett", password="password321")
        data = {
            'title': 'Do something',
            'description': 'Do something to not get bore',
            'action': 'UN'
        }
        self.client.login(username="scarlett", password="password321")
        response = self.client.post(self.createviewurl, data)
        item = todoList.objects.get(id=1)
        self.assertEqual(response.status_code, 302)

    # def test_listview_get(self):
    #     self.client.login(username="scarlett", password="password321")
    #     response = self.client.get(reverse('todolist.all'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'userhomepage.html')
    #     self.assertEquals(response.content_data['items'].count(), 3)