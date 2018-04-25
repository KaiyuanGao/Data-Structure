# coding: utf-8

class prioqueError(ValueError):
	pass
	

class prioque1:									#���ȶ��е�list��ʵ��
	def __init__(self, elist=[]):
		self._elems = list(elist)
		self._elems.sort(reverse = True)
		
	def enqueue(self, e):
		i = len(self._elems) - 1
		while i >= 0 :
			if self._elems[i] <= e:
				i -= 1
			else:
				break
		self._elems.insert(i+1, e)
		
	def is_empty(self):
		return not self._elems
		
	def peek(self):
		if self.is_empty():
			raise prioqueError("in top")
		return self._elems[-1]
		
	def dequeue(self):
		if self.is_empty():
			raise prioqueError("in top")
		return self._elems.pop()



class prioque2:									#���ȶ��еĶ�ʵ��
	def __init__(self, elist=[]):
		self._elems = list(elist)
		if elist:
			self.buildhead()
			
	def is_empty(self):
		return not self._elems
		
	def peek(self):
		if self.is_empty():
			raise prioqueError("in peek")
		return self._elems[0]
		
	def enqueue(self, e):						#������Ԫ��
		self._elems.append(None)
		self.siftup(e, len(self._elems)-1)
		
	def siftup(self, e, last):					#����ɹѡ�ĸ�������
		elems, i, j = self._elems, last, (last-1)//2
		while i > 0 and e < elems[j]:
			elems[i] = elems[j]
			i. j = j, (j-1)//2
		elem[i] = e
	    
	def dequeue(self):							#����Ԫ��
		if self.is_empty():
			raise prioqueError("in dequeue")
		elems = self._elems
		e0 = elems[0]
		e = elems.pop()
		if len(elems) > 0:
			self.siftdown(e, 0, len(elems))
	
	def siftdown(self, e, begin, end):			#����ɾѡ�ĸ�������
		elems, i, j = self._elems, begin, begin*2+1
		while j < end:
			if j+1 < end and elems[j+1] < elems[j]:
				j += 1
			if e < elems[j]:
				break
			elems[i] = elems[j]
			i = j
			j = 2*j+1
		elems[i] = e
		
	def buildhead(self):						#����һ�����е�list������ʼ�ѣ�������O(n)
		end = len(self._elems)
		for i in range(end//2, -1, -1):
			self.siftdown(self._elems[i], i, end)
			

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
