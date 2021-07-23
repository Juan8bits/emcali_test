#!/usr/bin/python3
""" Unittest Module for BaseModel class
"""
from models.base_model import BaseModel
from models import storage, base_model
import pep8
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Class to add Unittest for a BaseModel class. """

    def __init__(self, *args, **kwargs):
        """ __init__ method."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)
        ob = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob.id, ob2.id)
        self.assertEqual(str, type(ob.id))

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at != new.updated_at)


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)
