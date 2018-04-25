# coding: utf-8
from LKList import *
from LKList_rear import *

class DLNode(LKNode):						#˫����ڵ���
	def __init__(self,elem,prev=None,next_=None):
		LNode.__init__(self,elem,next_)
		self.prev = prev
	
	
class DLList(LKList_rear):						#���ڴ�β���ĵ���������˫������
	def __init__(self):
		LKList_rear.__init__(self)
	
	def prepend(self,elem ):					#ǰ�����Ԫ��
		p = DLNode(elem,None,self._head)
		if self._head is None:
			self._rear = p
		else:
			p.next_.prev = p
		self._head = p
	
	def append(self,elem):						#�������Ԫ��
		p = DLNode(elem,self._rear,None)
		if self._head is None:
			self._head = p
		else:
			p.prev.next_ = p
		self._rear= p
		
	def pop(self):								#����Ԫ��
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._head.elem
		self._head = self._head.next_
		if self._head is not None:
			self._head.prev = None
		return e
		
	def pop_last(self):							#������ɾ��Ԫ��
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._rear.elem
		self._rear = self._rear.prev
		if self._rear is not None:
			self._head = None 				#����head��֤is empty��������
		else:
			self._rear.next_ = None 
		return e
	
	
	
	
	
	
	
	
	
	
	

