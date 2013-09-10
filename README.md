# unittest-tap-reporting

unittest-tap-reporting is a unittest test runner that can save test results
to TAP stream that can be consumed by a wide range of tools, such as build
systems, IDEs and continuous integration servers.

## Requirements

* Python 2.7

## Installation

The easiest way to install unittest-tap-reporting is via
[EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall). Follow
[these instructions](http://pypi.python.org/pypi/setuptools) to install
EasyInstall if you don't have it already.

Then, execute the following command line to install the latest stable version
of unittest-tap-reporting:

````bash
$ sudo easy_install unittest-tap-reporting
````

If you use Git and want to get the latest *development* version:

````bash
$ git clone git://github.com/vit1251/unittest-tap-reporting.git
$ cd unittest-tap-reporting
$ sudo python setup.py install
````

## Usage

The script below, adapted from the
[unittest](http://docs.python.org/library/unittest.html), shows how to use
`TAPTestRunner` in a very simple way. In fact, the only difference between
this script and the original one is the last line:

```python
import random
import unittest
import taprunner


class TestSequenceFunctions(unittest.TestCase):
  def setUp(self):
    self.seq = range(10)

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, range(10))

  def test_choice(self):
    element = random.choice(self.seq)
    self.assert_(element in self.seq)

  def test_sample(self):
    self.assertRaises(ValueError, random.sample, self.seq, 20)
    for element in random.sample(self.seq, 5):
      self.assert_(element in self.seq)


if __name__ == '__main__':
  unittest.main(testRunner=taprunner.TAPTestRunner()) # output='test-reports'
```
