# coding: utf-8


class LKNode:								#定义节点类
	def __init__(self,elem,next_= None):
		self.elem = elem 
		self.next_ = next_


class LinkedListUnderflow(ValueError):		#定义链接错误类
	pass


class LKList:								#单链表类
	def __init__(self):						#初始化链表
		self._head = None
	
	def is_empty(self): 
		return self._head is None
	
	def prepend(self,elem):					#在表头插入数据
		self._head = LKNode(elem,self._head)
	
	def pop(self):							#删除表头节点并返回这个节点里的元素
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem 
		self._head = self._head.next
		return e
	
	def append(self,elem ):					#在链表后端插入元素
		if self._head is None:
			self._head = LKNode(elem)
			return 
		p = self._head
		while p.next_ is not None:
			p = p.next_
		p.next_ = LKNode(elem)

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
		return e
		
	def find(self,pred):					#找到满足条件的表元素
		p = self._head
		while p is not None:
			if pred(p.elem ):
				return p.elem 
			p = p.next
	
	def printall(self):						#print all查看表元素
		p = self._head
		while p is not None:
			print(p.elem ,end = "")
			if p.next_ is not None:
				print(", ",end = "")
			p = p.next_
		print(" ")
	
	def elements(self):						#定义对象的一个迭代器
		p = self._head
		while p is not None:
			yield p.elem 
			p = p.next_
	
	def fileter(self, pred):				#基于给定的谓词晒选出满足pred的元素
		p = self._head
		while p is not None:
			if pred(p.elem ):
				yield p.elem
			p = p.next_
	
	def rev(self):							#链表反转
		p = None
		while self._head is not None:
			q = self._head
			self._head = q.next_            #摘下原来的首节点
			q.next_ = p						
			p = q							#将刚摘下的节点加入p引用的节点序列
		self._head = p						#重置表头链接
	
	def sort1(self):						#移动表中元素完成排序
		if self._head is None:
			return
		q = self._head.next_ 
		while q is not None:
			x = q.elem 
			p = self._head
			while p is not q and p.elem < x:	#跳过小元素
				p = p.next_ 
			while p is not q:					#倒换大元素，完成元素插入
				y = p.elem 
				p.elem = x
				x = y
				p = p.next_ 
			q.elem = x							#回填最后一个元素
			q = q.next_
				 
	def sort2(self):						#调整节点之间的连接关系完成排序
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
				
