# coding: utf-8
from LKList import LKList

class LKList_rear(LKList):						#��������LKList����һ����β�ڵ������� ������
	def __init__(self):
		LKList.__init__(self)
		self._rear = None		
		
	def prepend(self,elem):					#�ڱ�ͷ��������
		if self._head is None:
			self._head = LNode(elem,self._head)
			self._rear = self._head
		else:
			self. _head = LNode(elem,self._head)
		
	def append(self,elem):					#�������˲���Ԫ��
		if self._head is None:
			self._head = LNode(elem,self._head)	
			self._rear = self._head
		else:
			self._rear.next_ = LNode(elem )
			self._rear = self._rear.next_
		
	def pop_last(self):						#ɾ����������Ԫ��
		if self._head is None:				#�ձ�
			raise LinkedListUnderflow("in pop_last")
		p = self._head
		if p.next is None:					#����ֻ��һ��Ԫ��
			e = p.elem
			self._head = None
			return e
		while p.next.next is not None:		#�ҵ�p.next.nextΪNone��p
			p = p.next
		e = p.next.elem 
		p.next = None
		self._rear = p 						#����ĩβָ��
		return e	
		
