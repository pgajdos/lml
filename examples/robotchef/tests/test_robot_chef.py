import sys

from mock import patch
from nose.tools import eq_

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO
else:
    from io import StringIO


@patch("sys.stdout", new_callable=StringIO)
def test_peking_duck(stdout):
    arguments = ["robotchef", "Peking Duck"]
    from robotchef.main import main

    with patch.object(sys, "argv", arguments):
        main()
        eq_(stdout.getvalue(), "I can roast Peking Duck\n")
