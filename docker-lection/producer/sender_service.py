import pika
import json
from config import Config

def send_message(message):
    print("Sending message to " + Config.RABBIT_MQ_HOST)
    # Establish a connection with RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = Config.RABBIT_MQ_HOST, 
                                                                   virtual_host = "/",
                                                                   credentials = pika.credentials.PlainCredentials(Config.RABBITMQ_USER, Config.RABBITMQ_PASS)))
    channel = connection.channel()

    # Create a queue where the message will be delivered
    print(channel.queue_declare(queue=Config.QUEUE_NAME))

    # Send the message
    channel.basic_publish(exchange='', routing_key=Config.QUEUE_NAME, body=json.dumps(message))

    print(" [x] Sent %r" % json.dumps(message))
    connection.close()