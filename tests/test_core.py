import unittest
from csv_formula_roundtrip.core import run
class DomainTests(unittest.TestCase):
 def test_quote_alone_not_enough(self):
  x=run({'rows':[['=1+1','a,b','normal']]});self.assertTrue(x['roundtrip_matches']);self.assertEqual(len(x['changed_cells']),1);self.assertIn("'=1+1",x['csv'])
 def test_whitespace(self):self.assertEqual(len(run({'rows':[['  +1','\t=1','\ufeff-2']]})['changed_cells']),3)
 def test_data_not_mutated(self):
  rows=[['=1']];run({'rows':rows});self.assertEqual(rows,[['=1']])
