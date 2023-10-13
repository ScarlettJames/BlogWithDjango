from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ToDoList.models import todoList

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username="scarlett",password="password321")
        self.client.login(username="scarlett", password="password321")
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
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, self.listviewurl)
        self.assertEquals(item.title, data['title'])
        response = self.client.get(response.url)
        self.assertTemplateUsed(response, 'userhomepage.html')
        self.assertEquals(response.content_data['items'].count(), 1)

    # def test_listview_get(self):
    #     self.client.login(username="scarlett", password="password321")
    #     response = self.client.get(reverse('todolist.all'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'userhomepage.html')
    #     self.assertEquals(response.content_data['items'].count(), 3)