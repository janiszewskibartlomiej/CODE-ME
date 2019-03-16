import unittest
import sys
from contextlib import contextmanager
from io import StringIO

from zaddom04_e1 import timer, przykladowa_funkcja


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Etap1(unittest.TestCase):
    def test_poprawne_dzialanie(self):
        with captured_output() as (out, err):
            timer(przykladowa_funkcja)

            output = out.getvalue().strip()
        timer_output = output.split('\n')[1]

        self.assertEqual(timer_output[:22], 'Czas wykonania: 0:00:0')

        seconds = float(timer_output[22:])
        self.assertGreater(seconds, 0)
        self.assertLessEqual(seconds, 10)


if __name__ == '__main__':
    unittest.main()
