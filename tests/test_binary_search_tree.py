from simple_trees import BSTree, TraversalType


def build_bstree():
    tree = BSTree()

    tree.insert(4, 4)
    tree.insert(2, 2)
    tree.insert(6, 6)
    tree.insert(1, 1)
    tree.insert(7, 7)
    tree.insert(5, 5)
    tree.insert(3, 3)

    return tree


def test_traversal_and_not_reverse():
    tree = build_bstree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal()
        )
    )


def test_traversal_and_reverse():
    tree = build_bstree()

    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(reverse=True)
        )
    )


def test_pre_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [4, 2, 1, 3, 6, 5, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER)
        )
    )


def test_pre_order_traversal_and_reverse():
    tree = build_bstree()
    assert [4, 6, 7, 5, 2, 3, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.PRE_ORDER, reverse=True)
        )
    )


def test_in_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [1, 2, 3, 4, 5, 6, 7] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER)
        )
    )


def test_in_order_traversal_and_reverse():
    tree = build_bstree()

    assert [7, 6, 5, 4, 3, 2, 1] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.IN_ORDER, reverse=True)
        )
    )


def test_post_order_traversal_and_not_reverse():
    tree = build_bstree()

    assert [1, 3, 2, 5, 7, 6, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER)
        )
    )


def test_post_order_traversal_and_reverse():
    tree = build_bstree()

    assert [7, 5, 6, 3, 1, 2, 4] == list(
        map(
            lambda node: node.value,
            tree.traversal(traversal_type=TraversalType.POST_ORDER, reverse=True)
        )
    )

