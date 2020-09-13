class Node():
    def __init__(self, state, parent, path):
        self.state = state
        self.parent = parent
        self.path = path


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.len = 0

    def add(self, node):
        self.frontier.append(node)
        self.len += 1

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            self.len -= 1
            return node
