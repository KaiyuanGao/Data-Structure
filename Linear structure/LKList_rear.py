# coding: utf-8
from LKList import LKList

class LKList_rear(LKList):						#给单链表LKList增加一个表尾节点引用域 派生类
	def __init__(self):
		LKList.__init__(self)
		self._rear = None		
		
	def prepend(self,elem):					#在表头插入数据
		if self._head is None:
			self._head = LNode(elem,self._head)
			self._rear = self._head
		else:
			self. _head = LNode(elem,self._head)
		
	def append(self,elem):					#在链表后端插入元素
		if self._head is None:
			self._head = LNode(elem,self._head)	
			self._rear = self._head
		else:
			self._rear.next_ = LNode(elem )
			self._rear = self._rear.next_
		
	def pop_last(self):						#删除表中最后的元素
		if self._head is None:				#空表
			raise LinkedListUnderflow("in pop_last")
		p = self._head
		if p.next is None:					#表中只有一个元素
			e = p.elem
			self._head = None
			return e
		while p.next.next is not None:		#找到p.next.next为None的p
			p = p.next
		e = p.next.elem 
		p.next = None
		self._rear = p 						#更新末尾指针
		return e	
		
