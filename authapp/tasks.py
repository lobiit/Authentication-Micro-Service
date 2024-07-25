from celery import shared_task


@shared_task
def handle_user_profile(data):
    print(f"Received data: {data}")
