import unittest
import requests


class TestMethods(unittest.TestCase):

    URL = 'http://localhost:8000/bookmark/'
    auth_1 = ('user_1', 'keepersolutions')
    auth_2 = ('user_2', 'keepersolutions')
    auth_invalid = ('invalid_user', 'invalid_user')
    data = {
        "title": "Google",
        "url": "https://www.google.com/",
        "private": True
    }

    # POST: /bookmark/ (Try to create a new bookmark without authentication)
    def test_post_anonymous(self):
        response = requests.post(self.URL, data=self.data)
        self.assertEqual(response.status_code, 500)

    # POST: /bookmark/ (Create a new bookmark)
    def test_post(self):
        response = requests.post(self.URL, data=self.data, auth=self.auth_1)
        self.assertEqual(response.status_code, 201)

    # GET: /bookmark/ (Get the list of public bookmarks)
    def test_get_anonymous(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), list)

    # GET: /bookmark/ (Get the list of owner bookmarks and public bookmarks)
    def test_get(self):
        response = requests.get(self.URL, auth=self.auth_1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), list)

    # GET: /bookmark/ (Try to get a single bookmark without authentication)
    def test_get_instance_anonymous(self):
        response = requests.get(self.URL+'2/')
        self.assertEqual(response.status_code, 403)

    # GET/PUT/DELETE: /bookmark/<bookmark_id> (Try to operate a single bookmark with an invalid user)
    def test_get_instance_invalid_user(self):
        response = requests.get(self.URL+'2/', auth=self.auth_invalid)
        self.assertEqual(response.status_code, 403)
    def test_put_instance_invalid_user(self):
        response = requests.put(self.URL+'2/', data=self.data, auth=self.auth_invalid)
        self.assertEqual(response.status_code, 403)
    def test_delete_instance_invalid_user(self):
        response = requests.delete(self.URL+'2/', auth=self.auth_invalid)
        self.assertEqual(response.status_code, 403)

    # GET/PUT/DELETE: /bookmark/<bookmark_id> (Try to operate a single bookmark with a user who is not the creator)
    def test_get_instance_user_not_creator(self):
        response = requests.get(self.URL+'2/', auth=self.auth_2)
        self.assertEqual(response.status_code, 404)
    def test_put_instance_user_not_creator(self):
        response = requests.put(self.URL+'2/', data=self.data, auth=self.auth_2)
        self.assertEqual(response.status_code, 404)
    def test_delete_instance_user_not_creator(self):
        response = requests.delete(self.URL+'2/', auth=self.auth_2)
        self.assertEqual(response.status_code, 404)

    # PUT: /bookmark/<bookmark_id> (Update a single bookmark)
    def test_put_instance(self):
        self.data.update({"private": False})
        response = requests.put(self.URL+'2/', data=self.data, auth=self.auth_1)
        self.assertEqual(response.status_code, 200)

    # DELETE: /bookmark/<bookmark_id> (Delete a single bookmark)
    # def test_delete_instance(self):
    #     response = requests.delete(self.URL+'2/', auth=self.auth_1)
    #     self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()