# coding: utf-8
from LKList import LKList

class LCList(LKList):						#ѭ�����ӱ�
	def __init__(self):
		LKList.__init__(self)
		self._rear = None
		
	def is_empty(self): 
		return self._rear is None
	
	def prepend(self,elem):					#�ڱ�ͷ��������
		p = LNode(elem)
		if self._rear is None:
			p.next_ = p
			self._rear = p
		else:
			p.next_ = self._rear.next_
			self._rear.next_ = p
	
	def append(self,elem ):					#β�˲���
		self.prepend(elem)
		self._rear = self._rear.next_ 
	
	def pop(self):
		if self._rear is None:
			raise LinkedListUnderflow("in pop 0f LCList")
		p = self._rear.next_ 
		if self._rear is p:
			self._rear = None
		else:
			self._rear.next_ = p.next_ 
		return p.elem 
	
	def printall(self):
		if self.is_empty():
			return 
		p = self._rear.next_
		while True:
			print(p.elem )
			if p is self._rear:
				break
			p = p.next_
	
	
