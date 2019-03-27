package com.example.applicationdemo1;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;

public class MainActivity extends Activity {
    Button b1;
    EditText ed1,ed2;
    TextView tx1;
    public String Username;
    static String MQTTHOST ="tcp://192.168.2.4:1883";
    MqttAndroidClient client;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String clientId = MqttClient.generateClientId();
        client = new MqttAndroidClient(this.getApplicationContext(), MQTTHOST, clientId);
        MqttConnectOptions options = new MqttConnectOptions();



        try {
            IMqttToken token = client.connect(options);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    Toast.makeText(MainActivity.this, "connected",Toast.LENGTH_LONG).show();
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    Toast.makeText(MainActivity.this, "connection failed",Toast.LENGTH_LONG).show();
                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }
        b1 = findViewById(R.id.button);
        ed1 = findViewById(R.id.editText);
        ed2 = findViewById(R.id.editText2);
        tx1 =findViewById(R.id.textView3);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((ed1.getText().toString().equals("Hunter") && ed2.getText().toString().equals("Hunter"))||(ed1.getText().toString().equals("Carter") && ed2.getText().toString().equals("Carter"))||(ed1.getText().toString().equals("Khazir") && ed2.getText().toString().equals("Khazir"))||(ed1.getText().toString().equals("Rick") && ed2.getText().toString().equals("Rick"))) {
                    Username= ed1.getText().toString();
                    tx1.setText("Welcome, "+Username);
                    pub("profiles",Username);
                    openHomepage();
                }else{
                    tx1.setText("Please Try Again");
                }
            }
        });


    }
    public void openHomepage() {
        Intent intent = new Intent(this, Push.class);
        startActivity(intent);
    }
    public void pub (String topic1,String msg) {
        String topic = topic1;
        String message = msg;
        try {
            client.publish(topic1, message.getBytes(),0,false);
        } catch ( MqttException e) {
            e.printStackTrace();
        }
    }
}
