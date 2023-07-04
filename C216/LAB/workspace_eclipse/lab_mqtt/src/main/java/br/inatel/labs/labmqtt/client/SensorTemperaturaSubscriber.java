package br.inatel.labs.labmqtt.client;

import java.util.UUID;

import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.MqttClient;

public class SensorTemperaturaSubscriber {

	public static void main(String[] args) throws MqttException {

		//1.Criando o subscriber
		String subscriberId = UUID.randomUUID().toString();
		IMqttClient subscriber = new MqttClient( MyConstants.URI_BROKER, subscriberId);

		//2.Conexão
		MqttConnectOptions options = new MqttConnectOptions();
		options.setAutomaticReconnect(true);
		options.setCleanSession(true);
		options.setConnectionTimeout(10);
		subscriber.connect(options);
	
		//3.Recebe a mensagem do Broker
		subscriber.subscribe(MyConstants.TOPIC_1, (topic, msg) -> {
			byte[] payload = msg.getPayload();
			System.out.println( "Payload recebido: " + payload);
			System.out.println( "Topic recebido: " + topic);
		});
		
	}
}