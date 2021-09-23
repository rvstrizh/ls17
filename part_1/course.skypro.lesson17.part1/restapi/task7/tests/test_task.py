import json
import unittest

from task import app


class TestCase(unittest.TestCase):
    def test_get_tours(self):
        with app.app_context():
            address = "/tours"
            app.testing = True
            response = app.test_client().get(address)
            self.assertEqual(response.status_code, 200, msg="Получение списке туров не отдает правильный код ответа")
            self.assertEqual(len(json.loads(response.data.decode('utf-8'))), 4, msg="Получение списке туров не отдает список туров")

    def test_get_tour(self):
        with app.app_context():
            address = "/tours/1"
            app.testing = True
            response = app.test_client().get(address)
            self.assertEqual(response.status_code, 200, msg="Получение тура по ID не отдает правильный код ответа")
            self.assertEqual(len(json.loads(response.data.decode('utf-8'))), 1, msg="Получение тура по ID отдает больше чем 1 тур")
            self.assertEqual(json.loads(response.data.decode('utf-8'))["id"], 1, msg="Получение тура по ID не запрашиваемый нужный тур")

    def test_create_tour(self):
        with app.app_context():
            address = "/tours"
            app.testing = True
            data = {
                "f1": "test"
            }
            response = app.test_client().post(address, data=data)
            self.assertEqual(response.status_code, 201, msg="Создание тура по ID не отдает правильный код ответа")


    def test_update_tour(self):
        with app.app_context():
            address = "/tours/1"
            app.testing = True
            data = {
                "f1": "test"
            }
            response = app.test_client().put(address, data=json.dumps(data))
            self.assertEqual(response.status_code, 204, msg="Обновление тура по ID не отдает правильный код ответа")

    def test_delete_tour(self):
        with app.app_context():
            address = "/tours/1"
            app.testing = True
            response = app.test_client().delete(address)
            self.assertEqual(response.status_code, 204, msg="Удаление тура по ID не отдает правильный код ответа")

