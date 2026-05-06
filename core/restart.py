import os, sys

def re():
    print("sys.executable =", sys.executable)
    print("sys.argv =", sys.argv)
    if getattr(sys, 'frozen', False):
        os.execl(sys.executable, sys.executable)
    else:
        script = os.path.abspath(sys.argv[0])
        os.execl(sys.executable, (sys.executable, script))