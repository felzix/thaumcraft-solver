from logging import getLogger
from networkx import Graph


logger = getLogger()


class Aspect(object):
    def __init__(self, name, components=None):
        self.name = name
        self.components = components or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Aspect {}'.format(self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

    def __ne__(self, other):
        return not (self == other)


class AspectGraph(object):
    def __init__(self, aspects):
        self.graph = Graph()
        self.graph.add_nodes_from(aspects)
        for aspect in aspects:
            self.graph.add_edges_from([
                (aspect, component) for component in aspect.components
            ])

    def get_aspect(self, aspect_name):
        for aspect in self.graph.nodes():
            if aspect.name == aspect_name:
                return aspect

    def neighbors(self, aspect):
        return self.graph.neighbors(aspect)

    def all_paths(self, source, destination, depth):
        def helper(paths, current_depth=0):
            current_depth += 1
            if current_depth == depth:
                return paths
            more_paths = []
            for path in paths:
                neighbors = self.neighbors(path[-1])
                logger.debug('path: {}'.format(path))
                logger.debug('neighbors: {}'.format(neighbors))
                more_paths += [list(path)+[neighbor] for neighbor in neighbors]
                logger.debug('more_paths: {}'.format(more_paths))
            return helper(more_paths, current_depth)
        all_paths = helper([neighbor] for neighbor in self.neighbors(source))
        logger.debug('all_paths: {}'.format(all_paths))
        good_paths = [path for path in all_paths if path[-1] == destination]
        logger.debug('good_paths: {}'.format(good_paths))
        return good_paths
