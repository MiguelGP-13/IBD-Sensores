import pika, os, time
import json

with open('seguridad.csv', 'a') as f:
    # Create csv with header
    f.write('timestamp,status,alerts,alert_level\n')

time.sleep(10)  # Wait for RabbitMQ container to initialize

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
channel = connection.channel(channel_number=4)

channel.queue_declare(queue='seguridad')

def callback(ch, method, properties, body):
    data = json.load(body)
    linea = f"{data['timestamp']},{data['status']},{data['alerts']},{data['alert_level']}"
    with open('data/seguridad.csv', 'a') as f:
        f.write(linea + '\n')

channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

channel.start_consuming()