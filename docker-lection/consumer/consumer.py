import pika
import json
from config import Config

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # Process the message here

def receive_message():
    print("Receiving messages from " + Config.RABBIT_MQ_HOST)
    # Establish a connection with RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = Config.RABBIT_MQ_HOST, 
                                                                   virtual_host = "/",
                                                                   credentials = pika.credentials.PlainCredentials(Config.RABBITMQ_USER, Config.RABBITMQ_PASS)))
    channel = connection.channel()

    # Declare the same queue as the sender to make sure it exists
    channel.queue_declare(queue=Config.QUEUE_NAME)

    # Start consuming messages
    channel.basic_consume(queue=Config.QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    
if __name__ == '__main__':
    receive_message()