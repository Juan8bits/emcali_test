#!/usr/bin/python3
"""Defines unittests for models/engine/db_storage.py."""
import unittest
import MySQLdb
import models
from os import getenv
from models.base_model import Base
from models.user import User
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
import pep8


class TestDBStorage(unittest.TestCase):
    """ Unittests for testing the DBStorage class. """
    @classmethod
    def setUpClass(cls):
        """DBStorage testing setup.
        Instantiate new DBStorage.
        Fill DBStorage test session with instances of all classes.
        """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.user = User(email="jm@gmail.com", password="pass123",
                            first_name="juan", last_name="ramierz",
                            phone="3226571761")
            cls.storage._DBStorage__session.add(cls.user)
            cls.storage._DBStorage__session.commit()


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """

    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)
