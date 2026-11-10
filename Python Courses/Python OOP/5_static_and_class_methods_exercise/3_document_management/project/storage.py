from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [category for category in self.categories if category.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [document for document in self.documents if document.id == document_id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = next((category for category in self.categories if category.id == category_id), None)

        if category is not None:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = next((topic for topic in self.topics if topic.id == topic_id), None)

        if topic is not None:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = next((document for document in self.documents if document.id == document_id), None)

        if document is not None:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = next((document for document in self.documents if document.id == document_id), None)
        return document

    def __repr__(self):
        return "\n".join(str(document) for document in self.documents)
