from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="Heartbeat_Consumer",
)

topic = app.topic("video-heartbeat", value_deserializer="json")

sdf = app.dataframe(topic)

sdf.print()

if __name__ == "__main__":
    print("Starting Consumer Worker")
    app.run(sdf)
