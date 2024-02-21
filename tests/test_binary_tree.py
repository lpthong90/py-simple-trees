from simple_trees import BinaryTree, BinaryNode, TraversalType


def build_tree():
    root = BinaryNode(1, 1)

    root.left = BinaryNode(2, 2)
    root.right = BinaryNode(3, 3)

    root.left.left = BinaryNode(4, 4)
    root.left.right = BinaryNode(5, 5)
    root.right.left = BinaryNode(6, 6)
    root.right.right = BinaryNode(7, 7)

    tree = BinaryTree[int, int, BinaryNode](root=root)
    return tree


def test_traversal_and_not_reverse():
    tree = build_tree()

    assert [1, 2, 4, 5, 3, 6, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal()
        )
    )


def test_traversal_and_reverse():
    tree = build_tree()

    assert [1, 3, 7, 6, 2, 5, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(reverse=True)
        )
    )


def test_pre_order_traversal_and_not_reverse():
    tree = build_tree()

    assert [1, 2, 4, 5, 3, 6, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER)
        )
    )


def test_pre_order_traversal_and_reverse():
    tree = build_tree()

    assert [1, 3, 7, 6, 2, 5, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER, reverse=True)
        )
    )


def test_in_order_traversal_and_not_reverse():
    tree = build_tree()

    assert [4, 2, 5, 1, 6, 3, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER)
        )
    )


def test_in_order_traversal_and_reverse():
    tree = build_tree()

    assert [7, 3, 6, 1, 5, 2, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER, reverse=True)
        )
    )


def test_post_order_traversal_and_not_reverse():
    tree = build_tree()

    assert [4, 5, 2, 6, 7, 3, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER)
        )
    )


def test_post_order_traversal_and_reverse():
    tree = build_tree()

    assert [7, 6, 3, 5, 4, 2, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER, reverse=True)
        )
    )
