import json
import unittest

from app import db, models, repositories, app


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        email = "test@test.com"
        password = "password"
        user = repositories.UserRepository.save(
            email=email, password=password, password_confirmation=password
        )

        response = self.client.get("/api/users/" + str(user.id))
        json_response = json.loads(response.data.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["success"]["email"], email)
        self.assertEqual(json_response["success"]["password"], password)

    def test_create(self):
        email = "test@test.com"
        password = "password"
        response = self.client.post(
            "/api/users/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": email,
                    "password": password,
                    "password_confirmation": password,
                }
            ),
        )

        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.data.decode("utf-8"))

        self.assertEqual(json_response["success"]["email"], email)
        self.assertEqual(json_response["success"]["password"], password)
        self.assertEqual(models.User.query.count(), 1)

    def test_update_update_email(self):
        email = "test@test.com"
        password = "password"
        user = repositories.UserRepository.save(
            email=email, password=password, password_confirmation=password
        )

        new_email = "new_test@test.com"
        response = self.client.put(
            "/api/users/" + str(user.id),
            content_type="application/json",
            data=json.dumps({"email": new_email}),
        )

        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.data.decode("utf-8"))

        self.assertNotEqual(json_response["success"]["email"], email)
        self.assertEqual(json_response["success"]["email"], new_email)
