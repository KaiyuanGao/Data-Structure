#!/usr/bin/python
#coding=utf-8



class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 删除
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print ("fail")
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p


    # 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print (node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    # 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print (node.data)
            self.inOrderTraverse(node.rchild)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print (node.data)


