from celery import Celery
# from app.tasks import TestCeleryTask
from app.celeryconfig import Config
from importlib import import_module


celery_app = Celery(__file__)

celery_app.config_from_object(Config())

tasks = import_module('.tasks', package='app')

celery_app.tasks.register(
    tasks.TestCeleryTask,
)
