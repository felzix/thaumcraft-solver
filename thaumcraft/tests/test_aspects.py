from nose.tools import assert_list_equal, assert_set_equal, eq_, nottest

from thaumcraft.aspects import Aspect, AspectGraph


def test_aspect_no_components():
    name = 'nom'
    aspect = Aspect(name)
    eq_(aspect.name, name)
    assert_list_equal(aspect.components, [])


def test_aspect_components():
    name = 'nom'
    component_aspect = Aspect('anything')
    aspect = Aspect(name, [component_aspect])
    eq_(aspect.name, name)
    assert_list_equal(aspect.components, [component_aspect])


def test_graph_no_aspects():
    graph = AspectGraph([])
    assert_list_equal(graph.graph.nodes(), [])
    assert_list_equal(graph.graph.edges(), [])


def test_graph_one_aspect():
    aspect = Aspect('nom')
    graph = AspectGraph([aspect])
    assert_list_equal(graph.graph.nodes(), [aspect])
    assert_list_equal(graph.graph.edges(), [])


def test_graph_two_aspects():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    graph = AspectGraph([aspect1, aspect2])
    assert_set_equal(set(graph.graph.nodes()), {aspect1, aspect2})
    assert_edges_equal(graph, {
        (aspect1, aspect2),
    })


def test_no_neighbors():
    aspect = Aspect('nom')
    graph = AspectGraph([aspect])
    assert_list_equal(graph.neighbors(aspect), [])


def test_one_neighbor():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    graph = AspectGraph([aspect1, aspect2])
    assert_list_equal(graph.neighbors(aspect1), [aspect2])


def test_1_path_1():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    graph = AspectGraph([aspect1, aspect2])
    paths = graph.all_paths(aspect1, aspect2, 1)
    eq_(len(paths), 1)
    assert_list_equal(paths, [[aspect2]])


def test_1_path_2():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    aspect3 = Aspect('O2', components=[aspect2])
    graph = AspectGraph([aspect1, aspect2, aspect3])
    paths = graph.all_paths(aspect1, aspect3, 2)
    eq_(len(paths), 1)


def test_1_path_3():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    aspect3 = Aspect('O2', components=[aspect2])
    aspect4 = Aspect('bravo', components=[aspect3])
    graph = AspectGraph([aspect1, aspect2, aspect3, aspect4])
    paths = graph.all_paths(aspect1, aspect4, 3)
    eq_(len(paths), 1)


def test_2_path_2():
    aspect1 = Aspect('nom')
    aspect2 = Aspect('am', components=[aspect1])
    aspect3 = Aspect('O2', components=[aspect1])
    graph = AspectGraph([aspect1, aspect2, aspect3])
    paths = graph.all_paths(aspect1, aspect1, 2)
    eq_(len(paths), 2)


@nottest
def assert_edges_equal(graph, expected_edges):
    """
    :param graph: AspectGraph instance
    :param expected_edges: collection of tuples of aspect_1 and aspect_2
    :return: nothing
    :raises: AssertionError
    """
    edges = {frozenset(tuple_) for tuple_ in graph.graph.edges()}
    expected_edges = {frozenset(tuple_) for tuple_ in expected_edges}
    assert_set_equal(edges, expected_edges)