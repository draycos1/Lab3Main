package com.example.applicationdemo1;

import android.content.Intent;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.io.UnsupportedEncodingException;

public class DefaultSettings extends AppCompatActivity {
    Button b1,b2,b3;
    Switch m,r,d,w;
    String defaultsettingsstring;

   int mstat=0;
   int  dstat=0;
    int rstat=0;
    int wstat=0;
    TextView tx1;
    static String MQTTHOST ="tcp://192.168.2.4:1883";

    String topicStr= "Doorp";
    MqttAndroidClient client;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_default_settings);
        String clientId = MqttClient.generateClientId();
        client = new MqttAndroidClient(this.getApplicationContext(), MQTTHOST, clientId);
        MqttConnectOptions options = new MqttConnectOptions();



        try {
            IMqttToken token = client.connect(options);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    Toast.makeText(DefaultSettings.this, "connected",Toast.LENGTH_LONG).show();
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    Toast.makeText(DefaultSettings.this, "connection failed",Toast.LENGTH_LONG).show();
                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }
        b1 = findViewById(R.id.button2);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openHomePage();
            }
        });
        b2 = findViewById(R.id.button);
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                LogOut();
            }
        });
        b3 = findViewById(R.id.publishbut);
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                defaultsettingsstring=(Integer.toString(dstat)+Integer.toString(wstat)+Integer.toString(mstat)+Integer.toString(rstat));
                pub("Settings",defaultsettingsstring);
            }
        });
        d = findViewById(R.id.switchd);
        d.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                   dstat=1;
                }
                else {
                    dstat=0;
                }
            }
        });

        w = findViewById(R.id.switchw);
        m = findViewById(R.id.switchm);
        r = findViewById(R.id.switchr);
        w.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    wstat=1;
                }
                else {
                    wstat =0;
                }
            }
        });
        m.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                   mstat=1;
                }
                else {
                    mstat=0;
                }
            }
        });
        r.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                   rstat=1;
                }
                else {
                    rstat=0;
                }
            }
        });





    }




    public void openHomePage() {
        Intent intent = new Intent(this, Push.class);
        startActivity(intent);
    }
    public void LogOut() {
        Intent intent = new Intent(this, MainActivity.class);
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
