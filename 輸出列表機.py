import tempfile
#from functions.收據編號產生器 import new_ser_No
import win32api
import win32print 


def printing(newwb):
    #filename = tempfile.mktemp (".txt")
    #open (filename, "w").write ("This is a test")
    n = "收據範本1210.xlsx"
    win32api.ShellExecute (
    0,
    "print",
    n,
    #
    # If this is None, the default printer will
    # be used anyway.
    #
    '/d:"%s"' % win32print.GetDefaultPrinter (),
    ".",
    0
    )
