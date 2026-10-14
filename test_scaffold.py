import tempfile, unittest
from pathlib import Path
from T_C0D3 import scaffold, create_project, validate_name
class Tests(unittest.TestCase):
 def test_names(self):
  for n in ['site','My-site_2','a'*40]: self.assertEqual(validate_name(n),n)
 def test_bad(self):
  for n in ['', '../x','/tmp/x','a/b','a\\b','.','..','con','LPT9','COM1','a'*41,'🙂','1site','a b','<img>']:
   with self.assertRaises(ValueError): validate_name(n)
 def test_files(self): self.assertEqual(list(scaffold('demo')),['index.html','css/style.css','js/main.js'])
 def test_dry(self):
  with tempfile.TemporaryDirectory() as d:
   self.assertFalse(create_project(d,'demo')['created']);self.assertFalse((Path(d)/'demo').exists())
 def test_apply(self):
  with tempfile.TemporaryDirectory() as d:
   self.assertTrue(create_project(d,'demo',True)['created'])
   for f,c in scaffold('demo').items(): self.assertEqual((Path(d)/'demo'/f).read_text(),c)
 def test_no_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'demo';p.mkdir();(p/'keep').write_text('keep')
   with self.assertRaises(FileExistsError): create_project(d,'demo',True)
   self.assertEqual((p/'keep').read_text(),'keep')
 def test_symlink(self):
  with tempfile.TemporaryDirectory() as d:
   (Path(d)/'demo').symlink_to(Path(d)/'missing')
   with self.assertRaises(FileExistsError): create_project(d,'demo',True)
 def test_missing_parent(self):
  with self.assertRaises(FileNotFoundError): create_project('/nonexistent-tc-parent','demo',True)
