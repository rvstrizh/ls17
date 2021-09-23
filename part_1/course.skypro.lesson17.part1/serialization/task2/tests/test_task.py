import json
import unittest
from typing import List

from task import get_json


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        glistjosn = get_json()
        glistlistdict: List[dict] = json.loads(glistjosn)
        print(glistlistdict)
        for g in glistlistdict:
            self.assertTrue("id" in g.keys(), msg="Не верный JSON. Поля id нет в результирующем JSON")
            self.assertTrue("surname" in g.keys(), msg="Не верный JSON. Поля surname нет в результирующем JSON")
            self.assertTrue("full_name" in g.keys(), msg="Не верный JSON. Поля full_name нет в результирующем JSON")
            self.assertTrue("tours_count" in g.keys(), msg="Не верный JSON. Поля tours_count нет в результирующем JSON")
            self.assertTrue("bio" in g.keys(), msg="Не верный JSON. Поля bio нет в результирующем JSON")
            self.assertTrue("is_pro" in g.keys(), msg="Не верный JSON. Поля is_pro нет в результирующем JSON")
            self.assertTrue("company" in g.keys(), msg="Не верный JSON. Поля company нет в результирующем JSON")
