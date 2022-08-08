#!/usr/bin/python3
""" Unittests for models/base_model.py """
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_str_repr(self):
        datetime = datetime.today()
        datetime_repr = repr(datetime)
        basemodel = BaseModel()
        basemodel.id = "123"
        basemodel.created_at = basemodel.updated_at = datetime
        basemodelstr = basemodel.__str__()
        self.assertIn("[BaseModel] (123)", basemodelstr)
        self.assertIn("'id': '123'", basemodelstr)
        self.assertIn("'created_at': " + datetime_repr, basemodelstr)
        self.assertIn("'updated_at': " + datetime_repr, basemodelstr)

    def test_id_is_public(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_unique_ids(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_two_unique_created_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, basemodel2.created_at)

    def test_two_unique_updated_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, basemodel2.updated_at)

    def test_args_unused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_with_kwargs(self):
        datetime = datetime.today()
        datetime_iso = datetime.isoformat()
        basemodel = BaseModel(id="12345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(basemodel.id, "12345")
        self.assertEqual(basemodel.created_at, datetime)
        self.assertEqual(basemodel.updated_at, datetime)

    def test_when_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        datetime = datetime.today()
        datetime_iso = datetime.isoformat()
        basemodel = BaseModel("12", id="345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, datetime)
        self.assertEqual(basemodel.updated_at, datetime)
    
class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_once(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, basemodel.updated_at)

    def test_saves_twice(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        second_updated_at = basemodel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        basemodel.save()
        self.assertLess(second_updated_at, basemodel.updated_at)

    def test_save_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_save_updates_file(self):
        basemodel = BaseModel()
        basemodel.save()
        basemodelid = "BaseModel." + basemodel.id
        with open("file.json", "r") as f:
            self.assertIn(basemodelid, f.read())