import paho.mqtt.client as mqtt

class Subscriber:
    URL = "broker.hivemq.com"
    PORT = 1883
    TOPIC = "sensor"
    USER_NAME = "aaa"
    USER_PASS = "bb"
    LIVE_TIME = 3000
    def __init__(self, url=URL, port=PORT, topic=TOPIC, user_name=USER_NAME, user_pass=USER_PASS, live_time=LIVE_TIME):
        self.url = url
        self.port = port
        self.topic = topic
        self.user_name = user_name
        self.user_pass = user_pass
        self.live_time = live_time
        self.client = None
        self.connected = False

    def __call__(self):
        self.start()

    def start(self):
        if not self.connected:
            self.connect()
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected")
        self.connected = True
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        # upload to mongo
        print(msg.topic + " " + msg.payload.decode('utf-8'))

    def on_disconnect(self, client, userdata, rc):
        print("mqtt diconnected",rc)
        self.connected = False
        self.start()
    
    def connect(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(self.user_name, self.user_pass)
        self.client.connect(self.url, self.port,self.live_time)