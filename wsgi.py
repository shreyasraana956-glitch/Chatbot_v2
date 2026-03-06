import os
import sys

# This file allows gunicorn to run the app from the root directory
# while the actual code lives in the 'ai_teacher' subfolder.

# Add the project directory to the python path
path = os.path.join(os.path.dirname(__file__), "ai_teacher")
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_teacher.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
