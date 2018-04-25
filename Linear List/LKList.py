# coding: utf-8


class LKNode:								#����ڵ���
	def __init__(self,elem,next_= None):
		self.elem = elem 
		self.next_ = next_


class LinkedListUnderflow(ValueError):		#�������Ӵ�����
	pass


class LKList:								#��������
	def __init__(self):						#��ʼ������
		self._head = None
	
	def is_empty(self): 
		return self._head is None
	
	def prepend(self,elem):					#�ڱ�ͷ��������
		self._head = LKNode(elem,self._head)
	
	def pop(self):							#ɾ����ͷ�ڵ㲢��������ڵ����Ԫ��
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem 
		self._head = self._head.next
		return e
	
	def append(self,elem ):					#�������˲���Ԫ��
		if self._head is None:
			self._head = LKNode(elem)
			return 
		p = self._head
		while p.next_ is not None:
			p = p.next_
		p.next_ = LKNode(elem)

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
		return e
		
	def find(self,pred):					#�ҵ����������ı�Ԫ��
		p = self._head
		while p is not None:
			if pred(p.elem ):
				return p.elem 
			p = p.next
	
	def printall(self):						#print all�鿴��Ԫ��
		p = self._head
		while p is not None:
			print(p.elem ,end = "")
			if p.next_ is not None:
				print(", ",end = "")
			p = p.next_
		print(" ")
	
	def elements(self):						#��������һ��������
		p = self._head
		while p is not None:
			yield p.elem 
			p = p.next_
	
	def fileter(self, pred):				#���ڸ�����ν��ɹѡ������pred��Ԫ��
		p = self._head
		while p is not None:
			if pred(p.elem ):
				yield p.elem
			p = p.next_
	
	def rev(self):							#����ת
		p = None
		while self._head is not None:
			q = self._head
			self._head = q.next_            #ժ��ԭ�����׽ڵ�
			q.next_ = p						
			p = q							#����ժ�µĽڵ����p���õĽڵ�����
		self._head = p						#���ñ�ͷ����
	
	def sort1(self):						#�ƶ�����Ԫ���������
		if self._head is None:
			return
		q = self._head.next_ 
		while q is not None:
			x = q.elem 
			p = self._head
			while p is not q and p.elem < x:	#����СԪ��
				p = p.next_ 
			while p is not q:					#������Ԫ�أ����Ԫ�ز���
				y = p.elem 
				p.elem = x
				x = y
				p = p.next_ 
			q.elem = x							#�������һ��Ԫ��
			q = q.next_
				 
	def sort2(self):						#�����ڵ�֮������ӹ�ϵ�������
		p = self._head
		if p is None and p.next_ is None:
			return
		rem = p.next_ 
		p.next_ = None
		while p is not None and p.elem <= rem.elem:
			q = p
			p = p.next_ 
		if q is None:
			self._head = rem
		else:
			q.next_ = rem
		q = rem
		rem = rem.next_ 
		q.next_ = p
				
