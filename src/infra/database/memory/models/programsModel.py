import uuid
from domain.enum.enumQuery import EnumQuery

from infra.logger.logger import Logger

class Program:
    def __init__(self, _id=None, name=None, location=None, start_at=None, end_at=None):
        self._id = _id or uuid.uuid4()
        self.name = name
        self.location = location
        self.start_at = start_at
        self.end_at = end_at
        self.next_node = None
    def __str__(self):
        return f"Program(_id={self._id}, name={self.name}, location={self.location}, start_at={self.start_at}, end_at={self.end_at})"
class ProgramsModel:
    def __init__(self):
        self.head = None

    def set_program(self, program):
        if self.head is None:
            self.head = Program(**program)
            return self.head

        lastNode = self._findLastNode()
        lastNode.next_node = Program(**program)

    def findByLocation(self, query):
        node = self.head
        while node is not None:
            if node.location == query['location'] and self._is_between(node, query['hour']):
                return node
            node = node.next_node
        return None

    def _is_between(self, node, hour):
        return node.start_at <= hour <= node.end_at

    def _findLastNode(self):
        nextNode = self.head
        while nextNode.next_node is not None:
            nextNode = nextNode.next_node
        return nextNode

    def get_programs(self):
        node = self.head
        while node is not None:
            print(node.name, node.location, node.start_at, node.end_at, node._id)
            node = node.next_node
        return
