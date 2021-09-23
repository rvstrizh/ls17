import json
import unittest

import sqlalchemy
from task import db, app
from data_db import tours_data, guides_data, users_data


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            from task import Guide, User, Tour
        except ImportError:
            assert False, "Не правильное имя класса Guide или User или Tour"
        except sqlalchemy.exc.ArgumentError:
            assert False, "Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще"

        db.drop_all()
        db.create_all()

        for d in guides_data:
            guide = Guide(
                id=d.get("id"),
                surname=d.get("surname"),
                full_name=d.get("full_name"),
                tours_count=d.get("tours_count"),
                bio=d.get("bio"),
                is_pro=d.get("is_pro"),
                company=d.get("company"),
            )
            with db.session.begin():
                db.session.add(guide)

        for d in tours_data:
            guide = Tour(
                id=d.get("id"),
                title=d.get("title"),
                description=d.get("description"),
                guide=d.get("guide"),
                guide_ru=d.get("guide_ru"),
                attractions=d.get("attractions"),
                city=d.get("city"),
                start_point=d.get("start_point"),
                end_point=d.get("end_point"),
                children_ok=d.get("children_ok"),
                group_size=d.get("group_size"),
                language=d.get("language"),
                duration_min=d.get("duration_min"),
                price_rur=d.get("price_rur"),
            )
            with db.session.begin():
                db.session.add(guide)

        for d in users_data:
            guide = User(
                id=d.get("id"),
                email=d.get("email"),
                password=d.get("password"),
                full_name=d.get("full_name"),
                city=d.get("city"),
                city_ru=d.get("city_ru"),
            )
            with db.session.begin():
                db.session.add(guide)

    def test_guide_by_id(self):
        with app.app_context():
            address = "/guides/2"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, dict), msg="Вернулся не JSON, может быть массив?")
        self.assertTrue(d.get("surname") == "Новикова", msg="Не правильно работает запрос к таблице")

    def test_all_guides(self):
        with app.app_context():
            address = "/guides"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d), len(guides_data), msg="Не правильно работает запрос к таблице")

    def test_user_by_id(self):
        with app.app_context():
            address = "/users/1"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, dict), msg="Вернулся не JSON, может быть массив?")
        self.assertTrue(d.get("full_name") == "Людмила Новикова", msg="Не правильно работает запрос к таблице")

    def test_all_users(self):
        with app.app_context():
            address = "/users"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d), len(users_data), msg="Не правильно работает запрос к таблице")

    def test_tour_by_id(self):
        with app.app_context():
            address = "/tours/1"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, dict), msg="Вернулся не JSON, может быть массив?")
        self.assertTrue(d.get("guide_ru") == "Андрей Васечкин", msg="Не правильно работает запрос к таблице")

    def test_all_tours(self):
        with app.app_context():
            address = "/tours"
            app.testing = True
            response = app.test_client().get(address)
        d = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(d, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d), len(tours_data), msg="Не правильно работает запрос к таблице")