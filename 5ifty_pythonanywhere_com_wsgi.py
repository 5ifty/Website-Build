

# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
import sys
path = '/home/5ifty/websitebuild'
if path not in sys.path:
    sys.path.append(path)



from flasky import app as application  
