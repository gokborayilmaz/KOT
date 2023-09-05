import contextlib
import time
import unittest
import os
import sys
import shutil
import copy
from unittest.mock import patch
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from kot import KOT, HASHES, KOT_Serial, KOT_Cloud
import kot


class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestCloud(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.remote = KOT_Cloud("cloud-workflow")

    def test_remote_api_set_get_deletestring(self):

        

        the = time.time()
        value = f"Value{the}"

        self.remote.set("key", value)
        time.sleep(1)

        self.assertEqual(self.remote.get("key",), value)

        self.remote.delete("key")
        time.sleep(1)


        self.assertNotEqual(self.remote.get("key"), value)

    def test_remote_api_active(self):
        self.remote.active(my_function)
        time.sleep(1)
        self.assertEqual(self.remote.get("my_function")(), 123)
        self.remote.delete("my_function")

backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
