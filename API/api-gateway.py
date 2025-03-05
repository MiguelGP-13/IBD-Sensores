from flask import Flask, jsonify, request
import requests
import pika, os, time

app = Flask(__name__)



### Temperatura ###
@app.route('/temperatura', methods=['GET'])
def get_temperature():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/temperature')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/temperatura', methods=['POST'])
def post_temperature():
    try:
        temperatura_channel.basic_publish(exchange='',
                          routing_key='temperatura',
                          body=request.json)
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Temperature unavailable'}), 503
    # Enviar notificación
    # try:
    #     requests.post(
    #         'http://notification-service:5000/notify',
    #         json={'user_id': user_id, 'message': f'Book {book_id} borrowed successfully'}
    #     )
    # except requests.exceptions.RequestException:
    #     # Log error but don't fail the request
    #     print('Notification service unavailable')

    return jsonify({'message': 'Temperatura añadida correctamente'})

######

### Ocupacion ###
@app.route('/ocupacion', methods=['GET'])
def get_ocupacion():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/ocupacion')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/ocupacion', methods=['POST'])
def post_ocupacion():
    try:
        ocupacion_channel.basic_publish(exchange='',
                          routing_key='ocupacion',
                          body=request.json)
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Ocupacion unavailable'}), 503
    # Enviar notificación
    # try:
    #     requests.post(
    #         'http://notification-service:5000/notify',
    #         json={'user_id': user_id, 'message': f'Book {book_id} borrowed successfully'}
    #     )
    # except requests.exceptions.RequestException:
    #     # Log error but don't fail the request
    #     print('Notification service unavailable')

    return jsonify({'message': 'Ocupacion añadida correctamente'})

######

### Consumo ###
@app.route('/consumo', methods=['GET'])
def get_consumo():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/consumo')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/consumo', methods=['POST'])
def post_consumo():
    try:
        consumo_channel.basic_publish(exchange='',
                          routing_key='consumo',
                          body=request.json)
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Consumo unavailable'}), 503
    # Enviar notificación
    # try:
    #     requests.post(
    #         'http://notification-service:5000/notify',
    #         json={'user_id': user_id, 'message': f'Book {book_id} borrowed successfully'}
    #     )
    # except requests.exceptions.RequestException:
    #     # Log error but don't fail the request
    #     print('Notification service unavailable')

    return jsonify({'message': 'Consumo añadida correctamente'})

######

### Seguridad ###
@app.route('/seguridad', methods=['GET'])
def get_seguridad():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/seguridad')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/seguridad', methods=['POST'])
def post_seguridad():
    try:
        seguridad_channel.basic_publish(exchange='',
                          routing_key='seguridad',
                          body=request.json)
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Seguridad unavailable'}), 503
    # Enviar notificación
    # try:
    #     requests.post(
    #         'http://notification-service:5000/notify',
    #         json={'user_id': user_id, 'message': f'Book {book_id} borrowed successfully'}
    #     )
    # except requests.exceptions.RequestException:
    #     # Log error but don't fail the request
    #     print('Notification service unavailable')

    return jsonify({'message': 'Seguridad añadida correctamente'})

######

if __name__ == '__main__':
    time.sleep(10)  # Wait for RabbitMQ container to initialize
    app.run(host='0.0.0.0', port=8080)

    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
    temperatura_channel = connection.channel(channel_number=1)
    temperatura_channel.queue_declare(queue='temperatura')
    ocupacion_channel = connection.channel(channel_number=2)
    ocupacion_channel.queue_declare(queue='ocupacion')
    consumo_channel = connection.channel(channel_number=3)
    consumo_channel.queue_declare(queue='consumo')
    seguridad_channel = connection.channel(channel_number=4)
    seguridad_channel.queue_declare(queue='seguridad')


    connection.close()