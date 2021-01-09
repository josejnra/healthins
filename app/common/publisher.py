from abc import ABC, abstractmethod

from google.cloud import pubsub_v1
from google.cloud.pubsub_v1.publisher import Client


class AbstractPublisher(ABC):

    @abstractmethod
    def publish_message(self, topic: str, message: str):
        raise NotImplementedError


class GCPPubSub(AbstractPublisher):

    def __init__(self, project_id: str, key_json_path: str):
        self.project_id = project_id
        self.publisher = self.create_publisher(key_json_path)

    @staticmethod
    def create_publisher(key_json) -> Client:
        return pubsub_v1.PublisherClient.from_service_account_json(key_json)

    def publish_message(self, topic: str, message: str):
        topic_name = f'projects/{self.project_id}/topics/{topic}'
        return self.publisher.publish(topic_name, data=message.encode('utf-8'))


class PublisherMessage:

    def __init__(self, publisher: AbstractPublisher):
        self.publisher = publisher

    def publish(self, topic: str, message: str):
        return self.publisher.publish_message(topic, message)
