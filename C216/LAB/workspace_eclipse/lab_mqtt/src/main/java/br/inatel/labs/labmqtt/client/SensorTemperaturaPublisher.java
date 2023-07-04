package br.inatel.labs.labmqtt.client;

import java.util.Random;
import java.util.UUID;

import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.MqttClient;

public class SensorTemperaturaPublisher {
	
	public static void main(String[] args) throws MqttException {
		
		//1.Criando o publisher
		String publisherId = UUID.randomUUID().toString();
		MqttClient publisher = new MqttClient( MyConstants.URI_BROKER, publisherId);

		//2.Criando uma mensagem
		MqttMessage msg = getTemperatureMessage();
		msg.setQos(0);
		msg.setRetained(true);
		
		//3.Conexão
		MqttConnectOptions options = new MqttConnectOptions();
		options.setAutomaticReconnect(true);
		options.setCleanSession(true);
		options.setConnectionTimeout(10);
		publisher.connect(options);

		//4.PUBLICA A MENSAGEM NO BROKER
		publisher.publish(MyConstants.TOPIC_1, msg);

		//5.DESCONECTA
		publisher.disconnect();
	}

	private static MqttMessage getTemperatureMessage() {
		Random r = new Random();
		double temperatura = 80 + r.nextDouble() * 20.0;
		byte[] payload = String.format("T:%04.2f", temperatura).getBytes();
		return new MqttMessage(payload);
	}
}