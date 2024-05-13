import os


class Config:
    RABBIT_MQ_HOST = os.environ.get('RABBIT_MQ_HOST') or 'localhost'
    RABBITMQ_USER = os.environ.get('RABBITMQ_USER') or 'guest'
    RABBITMQ_PASS = os.environ.get('RABBITMQ_PASS') or 'guest'
    QUEUE_NAME = os.environ.get('QUEUE_NAME') or 'my_queue'
    