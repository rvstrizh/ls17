import json
import unittest

import sqlalchemy
from task import db, app, page_size, detect_offset
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

    def test_all_guides(self):
        with app.app_context():
            address = "/guides?page=1"
            app.testing = True
            response1 = app.test_client().get(address)
            address = "/guides?page=2"
            response2 = app.test_client().get(address)
        d1 = json.loads(response1.data.decode('utf-8'))
        d2 = json.loads(response2.data.decode('utf-8'))
        from task import Guide
        offset = detect_offset(1)
        first = Guide.query.limit(page_size).offset(offset).first()
        self.assertTrue(isinstance(d1, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d1), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertEqual(d1[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertTrue(isinstance(d2, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d2), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        offset = detect_offset(2)
        first = Guide.query.limit(page_size).offset(offset).first()
        self.assertEqual(d2[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")

    def test_all_users(self):
        with app.app_context():
            address = "/users?page=1"
            app.testing = True
            response1 = app.test_client().get(address)
            address = "/users?page=2"
            response2 = app.test_client().get(address)
        d1 = json.loads(response1.data.decode('utf-8'))
        d2 = json.loads(response2.data.decode('utf-8'))
        from task import User
        offset = detect_offset(1)
        first = User.query.limit(page_size).offset(offset).first()
        self.assertTrue(isinstance(d1, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d1), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertEqual(d1[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertTrue(isinstance(d2, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d2), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        offset = detect_offset(2)
        first = User.query.limit(page_size).offset(offset).first()
        self.assertEqual(d2[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")

    def test_all_tours(self):
        with app.app_context():
            address = "/tours?page=1"
            app.testing = True
            response1 = app.test_client().get(address)
            address = "/tours?page=2"
            response2 = app.test_client().get(address)
        d1 = json.loads(response1.data.decode('utf-8'))
        d2 = json.loads(response2.data.decode('utf-8'))
        from task import Tour
        offset = detect_offset(1)
        first = Tour.query.limit(page_size).offset(offset).first()
        self.assertTrue(isinstance(d1, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d1), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertEqual(d1[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")
        self.assertTrue(isinstance(d2, list), msg="Вернулся не JSON массив, может быть объект?")
        self.assertEqual(len(d2), page_size, msg="Не правильно работает пагинация, элементов больше чем 3")
        offset = detect_offset(2)
        first = Tour.query.limit(page_size).offset(offset).first()
        self.assertEqual(d2[0].get("id"), first.id, msg="Не правильно работает пагинация, элементов больше чем 3")
