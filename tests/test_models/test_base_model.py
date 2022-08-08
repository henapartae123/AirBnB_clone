#!/usr/bin/python3
""" Unittests for models/base_model.py """

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):

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
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_unique_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())