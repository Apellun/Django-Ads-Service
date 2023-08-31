from rest_framework import status
from django.core import mail
from django.test import TestCase


class PasswordResetTest(TestCase):
    register_url = "http://localhost/api/users/"
    activate_url = "http://localhost/api/users/activation/"
    login_url = "http://localhost/token/login/"
    send_reset_password_email_url = "http://localhost/api/users/reset_password/"
    confirm_reset_password_url = "http://localhost/api/users/reset_password_confirm/"
    
    user_data = {
        "email": "test@example.com", 
        "first_name": "test_user",
        "last_name": "test_user", 
        "password": "verysecret",
        "phone": "+79998887766"
    }
    login_data = {
        "phone": "+79998887766",
        "email": "test@example.com", 
        "password": "verysecret"
    }

    def test_reset_password(self):
        # register the new user
        response = self.client.post(self.register_url, self.user_data, format="json")
        # expected response 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # expected one email to be send
        self.assertEqual(len(mail.outbox), 1)
        
        # parse email to get uid and token
        email_lines = mail.outbox[0].body.splitlines()
        activation_link = [l for l in email_lines if "/activation/" in l][0]
        uid, token = activation_link.split("/")[-3:-1]
        
        # verify email
        data = {"uid": uid, "token": token}
        response = self.client.post(self.activate_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # reset password
        data = {"email": self.user_data["email"]}
        response = self.client.post(self.send_reset_password_email_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # parse reset-password email to get uid and token
        # it is a second email!
        email_lines = mail.outbox[1].body.splitlines()
        reset_link = [l for l in email_lines if "/reset_password_confirm/" in l][0]
        uid, token = reset_link.split("/")[-3:-1]

        # confirm reset password
        data = {"uid": uid, "token": token, "new_password": "new_verysecret", "re_new_password": "new_verysecret"}
        response = self.client.post(self.confirm_reset_password_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # login to get the authentication token with old password
        response = self.client.post(self.login_url, self.login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # login to get the authentication token with new password
        login_data = dict(self.login_data)
        login_data["password"] = "new_verysecret"
        response = self.client.post(self.login_url, login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)