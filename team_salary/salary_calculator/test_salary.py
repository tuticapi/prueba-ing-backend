from rest_framework import status
from rest_framework.test import APITestCase


class LocalTestCase(APITestCase):

    def setUp(self):
        self.url = '/api/v1/team-salary/'

    def test_json_empty(self):
        response = self.client.post(
            self.url,
            None,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_information(self):
        response = self.client.post(
            self.url,
            {},
            format='json'
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data.get('error'), "missing information")

    def test_missing_fields(self):
        response = self.client.post(
            self.url,
            {'jugadores': [{
            }]
            },
            format='json'
        )
        data = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["nombre"][0], "This field is required.")

    def test_invalid_data_type(self):
        response = self.client.post(
            self.url,
            {'jugadores': [{
                "nombre": "Sebastian",
                "nivel": "A",
                "goles": "M",
                "sueldo": "M",
                "bono": "M",
                "sueldo_completo": "M",
                "equipo": "azul"
            }]
            },
            format='json'
        )

        data = response.data[0]
        self.assertEqual(data["goles"][0], "A valid integer is required.")
        self.assertEqual(data["sueldo"][0], "A valid number is required.")
        self.assertEqual(data["bono"][0], "A valid number is required.")
        self.assertEqual(data["sueldo_completo"][0],
                         "A valid number is required.")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ivalid_level(self):
        response = self.client.post(
            self.url,
            {'jugadores': [{
                "nombre": "Diego",
                "nivel": "Z",
                "goles": 1,
                "sueldo": 100,
                "bono": 200,
                "sueldo_completo": None,
                "equipo": "azul"
            }]
            },
            format='json'
        )
        data = response.data[0]
        self.assertIn(data["nivel"][0], "\"Z\" is not a valid choice.")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
