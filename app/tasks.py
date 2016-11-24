from app import celery_app


class TestCeleryTask(
    celery_app.Task,
):
    name = 'app.tasks.TestCeleryTask'

    def run(self, company='hello world'):
        from time import sleep
        sleep(5)
        print(company)