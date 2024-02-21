from __future__ import annotations

from typing import TypeVar, Generic, Optional, List
from enum import Enum

K = TypeVar("K")
V = TypeVar("V")


class NodeExistedError(RuntimeError): ...


class NodeNotExistedError(RuntimeError): ...


class TraversalType(Enum):
    PRE_ORDER = 'pre_order'
    IN_ORDER = 'in_order'
    POST_ORDER = 'post_order'


class Node(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key: K = key
        self.value: V = value
        self.children: List[Node] = []


class BinaryNode(Node[K, V]):
    def __init__(self, key: K, value: V):
        super().__init__(key, value)
        self.children: List[Optional[BinaryNode]] = [None, None]

    @property
    def left(self):
        return self.children[0]

    @left.setter
    def left(self, node: Optional[BinaryNode]):
        self.children[0] = node

    @property
    def right(self):
        return self.children[1]

    @right.setter
    def right(self, node: Optional[BinaryNode]):
        self.children[1] = node


N = TypeVar("N", bound=Node)
BN = TypeVar("BN", bound=BinaryNode)


class GenericTree(Generic[K, V, N]):
    def __init__(self, root: Optional[N] = None, node_cls: N = Node):
        self.root: Optional[N] = root
        self.node_cls = node_cls

    def insert(self, key: K, value: V):
        return self.insert_node(self.node_cls(key, value))

    def insert_node(self, node: N):
        raise NotImplementedError

    def update_node(self, node: N):
        raise NotImplementedError

    def search(self, key: K) -> Optional[N]:
        raise NotImplementedError

    def traversal(self, traversal_type: TraversalType = TraversalType.PRE_ORDER, reverse: bool = False):
        if traversal_type == TraversalType.PRE_ORDER:
            for node in self._pre_order_traversal(self.root, reverse):
                yield node
        elif traversal_type == TraversalType.IN_ORDER:
            for node in self._in_order_traversal(self.root, reverse):
                yield node
        elif traversal_type == TraversalType.POST_ORDER:
            for node in self._post_order_traversal(self.root, reverse):
                yield node

    def _pre_order_traversal(self, node: N, reverse: bool = False):
        pass

    def _in_order_traversal(self, node: N, reverse: bool = False):
        pass

    def _post_order_traversal(self, node: N, reverse: bool = False):
        pass


class BinaryTree(GenericTree[K, V, BN]):
    def __init__(self, root: Optional[BN] = None, node_cls: BN = BinaryNode):
        super().__init__()
        self.root: Optional[BN] = root
        self.node_cls = node_cls

    def _pre_order_traversal(self, root: BN, reverse: bool = False):
        yield root
        if not reverse:
            if root.left is not None:
                for node in self._pre_order_traversal(root.left, reverse):
                    yield node
            if root.right is not None:
                for node in self._pre_order_traversal(root.right, reverse):
                    yield node
        else:
            if root.right is not None:
                for node in self._pre_order_traversal(root.right, reverse):
                    yield node
            if root.left is not None:
                for node in self._pre_order_traversal(root.left, reverse):
                    yield node

    def _in_order_traversal(self, root: BN, reverse: bool = False):
        if not reverse:
            if root.left is not None:
                for node in self._in_order_traversal(root.left, reverse):
                    yield node
            yield root
            if root.right is not None:
                for node in self._in_order_traversal(root.right, reverse):
                    yield node
        else:
            if root.right is not None:
                for node in self._in_order_traversal(root.right, reverse):
                    yield node
            yield root
            if root.left is not None:
                for node in self._in_order_traversal(root.left, reverse):
                    yield node

    def _post_order_traversal(self, root: BN, reverse: bool = False):
        if not reverse:
            if root.left is not None:
                for node in self._post_order_traversal(root.left, reverse):
                    yield node
            if root.right is not None:
                for node in self._post_order_traversal(root.right, reverse):
                    yield node
        else:
            if root.right is not None:
                for node in self._post_order_traversal(root.right, reverse):
                    yield node
            if root.left is not None:
                for node in self._post_order_traversal(root.left, reverse):
                    yield node
        yield root

    def print(self):
        for node in self.traversal(traversal_type=TraversalType.PRE_ORDER):
            if node.left is not None:
                print(node.key, "--L-->", node.left.key)
            if node.right is not None:
                print(node.key, "--R-->", node.right.key)


class BinarySearchTree(BinaryTree[K, V, BN]):
    def __init__(self, node_cls: BN = BinaryNode):
        super().__init__()
        self.node_cls = node_cls

    def insert(self, key: K, value: V):
        self.root = self._insert_node(self.root, self.node_cls(key, value))

    def _insert_node(self, root: Optional[BN], node: BN) -> BN:
        if root is None:
            return node
        if node.key < root.key:
            root.left = self._insert_node(root.left, node)
            return root
        if node.key > root.key:
            root.right = self._insert_node(root.right, node)
            return root
        raise NodeExistedError

    def update(self, key: K, value: K, node_cls: BN = BinaryNode):
        self.update_node(self.node_cls(key, value))

    def update_node(self, node: BN):
        self.root = self._update_node(self.root, node)

    def _update_node(self, root: BN, node: BN) -> BN:
        if root is None:
            raise NodeNotExistedError
        if node.key < root.key:
            root.left = self._update_node(root.left, node)
            return root
        elif node.key > root.key:
            root.right = self._update_node(root.right, node)
            return root
        else:
            return node

    def search(self, key: K) -> Optional[BN]:
        return self._search(self.root, key)

    def _search(self, root: BN, key: K) -> Optional[BN]:
        if root is None:
            return
        if root.key == key:
            return root
        return self._search(root.left, key) or self._search(root.right, key)

    def remove(self, key: K) -> bool:
        pass

    def _remove(self, root: BN, key: K) -> bool:
        pass


BSTree = BinarySearchTree


class AVLNode(BinaryNode[K, V]):
    def __init__(self, key: K, value: V):
        super().__init__(key, value)
        self.height = 1
        self.left_height = 0
        self.right_height = 0

    @property
    def balance(self):
        return self.left_height - self.right_height

    @property
    def min_node(self):
        if self.left is None:
            return self
        return self.left.min_node

    @property
    def max_node(self):
        if self.right is None:
            return self
        return self.right.max_node


AVLBN = TypeVar("AVLBN", bound=AVLNode)


class AVLTree(BinarySearchTree[K, V, AVLBN]):
    def __init__(self, node_cls: AVLBN = AVLNode):
        super().__init__()
        self.node_cls = node_cls

    def insert(self, key: K, value: V):
        self.root = self._insert_node(self.root, self.node_cls(key, value))

    def delete(self, key: K):
        self.root = self._delete_node(self.root, self.node_cls(key, None))

    def _insert_node(self, root: BN, node: BN) -> BN:
        if root is None:
            return node
        elif node.key == root.key:
            raise NodeExistedError
        elif node.key < root.key:
            root.left = self._insert_node(root.left, node)
            root.left_height = 0 if root.left is None else root.left.height
        else:
            root.right = self._insert_node(root.right, node)
            root.right_height = 0 if root.right is None else root.right.height

        root.height = 1 + max(root.left_height, root.right_height)
        return self._balance(root, node)

    def _delete_node(self, root: BN, node: BN) -> BN:
        # Find the node to be deleted and remove it
        if root is None:
            return
        elif node.key < root.key:
            root.left = self._delete_node(root.left, node)
            root.left_height = 0 if root.left is None else root.left.height
        elif node.key > root.key:
            root.right = self._delete_node(root.right, node)
            root.right_height = 0 if root.right is None else root.right.height
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right.min_node
            root.key = temp.key
            root.value = temp.value
            root.right = self._delete_node(root.right, temp)
            root.right_height = 0 if root.right is None else root.right.height

        return self._balance(root, node)

    def _balance(self, root: BN, node: BN):
        if root is None:
            return

        balance_factor = root.balance

        if balance_factor > 1:
            if node.key < root.left.key:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balance_factor < -1:
            if node.key > root.right.key:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    # Function to perform left rotation
    def _left_rotate(self, z: BN) -> BN:
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2

        z.right_height = 0 if t2 is None else t2.height
        z.height = 1 + max(z.left_height, z.right_height)

        y.left_height = z.height
        y.height = 1 + max(y.left_height, y.right_height)

        return y

    # Function to perform right rotation
    def _right_rotate(self, z: BN) -> BN:
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3

        z.left_height = 0 if t3 is None else t3.height
        z.height = 1 + max(z.left_height, z.right_height)

        y.right_height = z.height
        y.height = 1 + max(y.left_height, y.right_height)

        return y

    def print(self):
        for node in self.traversal(traversal_type=TraversalType.PRE_ORDER):
            if node.left is not None:
                print(node.key, "--L-->", node.left.key)
            if node.right is not None:
                print(node.key, "--R-->", node.right.key)