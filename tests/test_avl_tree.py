from py_simple_trees import AVLTree, AVLNode, TraversalType


def build_avl_tree():
    tree = AVLTree()
    tree.insert(AVLNode(1, 1))
    tree.insert(AVLNode(2, 2))
    tree.insert(AVLNode(3, 3))
    tree.insert(AVLNode(4, 4))
    tree.insert(AVLNode(5, 5))
    tree.insert(AVLNode(6, 6))
    tree.insert(AVLNode(7, 7))
    return tree


def test_traversal_and_not_reverse():
    tree = build_avl_tree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(map(lambda node: node.value, tree.traversal()))


def test_traversal_and_reverse():
    tree = build_avl_tree()
    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(lambda node: node.value, tree.traversal(reverse=True))
    )


def test_pre_order_traversal_and_not_reverse():
    tree = build_avl_tree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER),
        )
    )


def test_pre_order_traversal_and_reverse():
    tree = build_avl_tree()
    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER, reverse=True),
        )
    )


def test_in_order_traversal_and_not_reverse():
    tree = build_avl_tree()
    assert [1, 2, 3, 4, 5, 6, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER),
        )
    )


def test_in_order_traversal_and_reverse():
    tree = build_avl_tree()
    assert [7, 6, 5, 4, 3, 2, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER, reverse=True),
        )
    )


def test_post_order_traversal_and_not_reverse():
    tree = build_avl_tree()
    assert [1, 3, 2, 5, 7, 6, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER),
        )
    )


def test_post_order_traversal_and_reverse():
    tree = build_avl_tree()
    assert [7, 5, 6, 3, 1, 2, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER, reverse=True),
        )
    )
