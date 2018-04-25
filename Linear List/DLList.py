# coding: utf-8
from LKList import *
from LKList_rear import *

class DLNode(LKNode):						#双链表节点类
	def __init__(self,elem,prev=None,next_=None):
		LNode.__init__(self,elem,next_)
		self.prev = prev
	
	
class DLList(LKList_rear):						#基于带尾结点的单链表派生双链表类
	def __init__(self):
		LKList_rear.__init__(self)
	
	def prepend(self,elem ):					#前向加入元素
		p = DLNode(elem,None,self._head)
		if self._head is None:
			self._rear = p
		else:
			p.next_.prev = p
		self._head = p
	
	def append(self,elem):						#后向加入元素
		p = DLNode(elem,self._rear,None)
		if self._head is None:
			self._head = p
		else:
			p.prev.next_ = p
		self._rear= p
		
	def pop(self):								#弹出元素
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._head.elem
		self._head = self._head.next_
		if self._head is not None:
			self._head.prev = None
		return e
		
	def pop_last(self):							#弹出后删除元素
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._rear.elem
		self._rear = self._rear.prev
		if self._rear is not None:
			self._head = None 				#设置head保证is empty正常工作
		else:
			self._rear.next_ = None 
		return e
	
	
	
	
	
	
	
	
	
	
	

