# coding: utf-8


class LNode:								#�ڵ���
	def __init__(self,elem,next_= None):
		self.elem = elem 
		self.next_ = next_


class LinkedListUnderflow(ValueError):		#���Ӵ�����
	pass


class Llist:								#��������
	def __init__(self):
		self._head = None
	
	def is_empty(self): 
		return self._head is None
	
	def prepend(self,elem):					#�ڱ�ͷ��������
		self._head = LNode(elem,self._head)
	
	def pop(self):							#ɾ����ͷ�ڵ㲢��������ڵ����Ԫ��
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem 
		self._head = self._head.next
		return e
	
	def append(self,elem ):					#�������˲���Ԫ��
		if self._head is None:
			self._head = LNode(elem)
			return 
		p = self._head
		while p.next_ is not None:
			p = p.next_
		p.next_ = LNode(elem)

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
		
		
class Llist1(Llist):						#������Llist����һ����β�ڵ������� ������
	def __init__(self):
		Llist.__init__(self)
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
		
		
class LCList(Llist):						#ѭ�����ӱ�
	def __init__(self):
		Llist.__init__(self)
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
	
	
class DLNode(LNode):						#˫����ڵ���
	def __init__(self,elem,prev=None,next_=None):
		LNode.__init__(self,elem,next_)
		self.prev = prev
	
	
class DLlist(Llist):						#˫������
	def __init__(self):
		Llist.__init__(self)
	
	def prepend(self,elem ):
		p = DLNode(elem,None,self._head)
		if self._head is None:
			self._rear = p
		else:
			p.next_.prev = p
		self._head = p
	
	def append(self,elem):
		p = DLNode(elem,self._rear,None)
		if self._head is None:
			self._head = p
		else:
			p.prev.next_ = p
		self._rear= p
		
	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._head.elem
		self._head = self._head.next_
		if self._head is not None:
			self._head.prev = None
		return e
		
	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop 0f DLlist")
		e = self._rear.elem
		self._rear = self._rear.prev
		if self._rear is not None:
			self._head = None 				#����head��֤is empty��������
		else:
			self._rear.next_ = None 
		return e
	
	
	
	
	
	
	
	
	
	
	
#�򵥵�ʹ�������� 
llist1 = LNode(1)
p = llist1
for i in range(2,11):
	p.next_ = LNode(i)
	p = p.next_
	
p = llist1
while p is not None:
	print(p.elem)
	p = p.next_

mlist1 = Llist()
for i in range(10):
	mlist1.prepend(i)
	
for i in range(11,20):
	mlist1.append(i)

mlist1.printall()
