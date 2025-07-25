from django.test import Client, TestCase
from .models import User
# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        u1 = User.objects.create_user("foo", "foo@g.com", "")
        u2 = User.objects.create_user("bar", "bar@g.com", "")
        u3 = User.objects.create_user("baz", "baz@g.com", "")
        
    def test_email(self):
        u = User.objects.get(username="foo")
        self.assertEqual(u.email, "foo@g.com")
    
    def test_login(self):
        c = Client()
        response = c.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        c = Client()
        response = c.post("/register", {"username": "poo", "email": "poo@g.com", "password": "", "confirmation":""})
        self.assertEqual(response.status_code, 302)