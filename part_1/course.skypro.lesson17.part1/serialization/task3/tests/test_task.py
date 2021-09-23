import json
import unittest

from task import app


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        with app.app_context():
            address = "/guides_json"
            app.testing = True
            response1 = app.test_client().get(address)
            address = "/guides_dict"
            app.testing = True
            response2 = app.test_client().get(address)
        self.assertEqual(response1.status_code, 200, msg="Новая вьюшка должна иметь URL /guides_json, видимо случайно удалили")
        self.assertEqual(response2.status_code, 200, msg="Старая вьюшка с URL /guides_dict куда-то пропала. Верните пожалуйста ее на место")
        self.assertEqual(json.loads(response1.data), json.loads(response2.data), msg="Не верно сделано преобразование")