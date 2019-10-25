from sparse_merkle import SparseMerkle
from unittest.mock import MagicMock

import unittest

class TestSparseMerkle(unittest.TestCase):
    def setUp(self):
        self.x = SparseMerkle()

        def side_effect(value):
            return value
        
        self.x.get_hash = MagicMock(side_effect = side_effect)
        
    def test_get_height(self):
        self.assertEqual(self.x.get_height(2), 2)
        self.assertEqual(self.x.get_height(3), 2)
        self.assertEqual(self.x.get_height(9), 4)
    
    def test_find_common_ancestor(self):
        self.assertEqual(self.x.find_common_ancestor(2, 3), 1)
        self.assertEqual(self.x.find_common_ancestor(4, 6), 1)
        self.assertEqual(self.x.find_common_ancestor(5, 6), 1)
        self.assertEqual(self.x.find_common_ancestor(4, 5), 2)
        self.assertEqual(self.x.find_common_ancestor(4, 11), 2)
        self.assertEqual(self.x.find_common_ancestor(4, 14), 1)
        self.assertEqual(self.x.find_common_ancestor(4, 4), 4)
        self.assertRaises(ValueError, lambda: self.x.find_common_ancestor(0, 1))

    def test_get_concat(self):
        self.assertEqual(self.x.get_concat('1', '2'), '1-2')

    def test_get_null_proofs(self):
        expected = {}
        expected[0] = '0'
        expected[1] = '-'.join(['0' for i in range(2)])
        expected[2] = '-'.join(['0' for i in range(4)])
        expected[3] = '-'.join(['0' for i in range(8)])
        expected[4] = '-'.join(['0' for i in range(16)])
        expected[5] = '-'.join(['0' for i in range(32)])
        self.assertEqual(self.x.get_null_proofs(5), expected)


if __name__ == '__main__':
    unittest.main()
