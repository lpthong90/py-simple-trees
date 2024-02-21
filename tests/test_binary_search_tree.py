from py_simple_trees import BSTree, BinaryNode, TraversalType


def build_bstree():
    tree = BSTree()

    tree.insert(BinaryNode(4, 4))
    tree.insert(BinaryNode(2, 2))
    tree.insert(BinaryNode(6, 6))
    tree.insert(BinaryNode(1, 1))
    tree.insert(BinaryNode(7, 7))
    tree.insert(BinaryNode(5, 5))
    tree.insert(BinaryNode(3, 3))

    return tree


def test_traversal_and_not_reverse():
    tree = build_bstree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(map(lambda node: node.value, tree.traversal()))


def test_traversal_and_reverse():
    tree = build_bstree()

    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(lambda node: node.value, tree.traversal(reverse=True))
    )


def test_pre_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER),
        )
    )


def test_pre_order_traversal_and_reverse():
    tree = build_bstree()
    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER, reverse=True),
        )
    )


def test_in_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [1, 2, 3, 4, 5, 6, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER),
        )
    )


def test_in_order_traversal_and_reverse():
    tree = build_bstree()

    assert [7, 6, 5, 4, 3, 2, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER, reverse=True),
        )
    )


def test_post_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [1, 3, 2, 5, 7, 6, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER),
        )
    )


def test_post_order_traversal_and_reverse():
    tree = build_bstree()

    assert [7, 5, 6, 3, 1, 2, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER, reverse=True),
        )
    )


def test_update():
    tree = build_bstree()

    tree.update(BinaryNode(key=4, value=-4))
    assert tree.root.key == 4
    assert tree.root.value == -4


def test_search():
    tree = build_bstree()

    node = tree.search(BinaryNode(key=4))

    assert node is not None
    assert node.key == 4
    assert node.value == 4


def test_remove():
    tree = build_bstree()

    tmp_node = BinaryNode(key=4)
    tree.remove(tmp_node)
    node = tree.search(tmp_node)

    assert node is None
