#coding: utf-8


class QueueUnderflow(ValueError):
	pass
	
	
	
class SQueue():
	def __init__(self, inin_len=8):
		self._len = _len
		self._elem = [0]*inii_len
		self_head = 0
		self._num = 0
		
	def is_empty(self):
		return self._num = 0
		
	def peek(self):
		if self._num = 0:
			raise QueueUnderflow
		return self._elem[self._head]
		
	def dequue(self):
		if self._num = 0:
			raise QueueUnderflow
		e = self._elem[self._head]
		self._head = (self._head+1)% self._len
		self._num -=1
		return e
		
	def enqueue(self, e):
		if self._num = self._len:
			self._extend()
		k = (self._head +self._num) % self._len
		self._elem[k] = e
		self._num += 1
		
	def _extend(self):
		old_len = self._len
		self._len *= 2
		new_elem = [0] * self._len
		for i in range(old_len):
			new_elem[i] = self._elem[(self._head+i) % old_len]
		self._elem, self._head = new_elem, 0
		
	
