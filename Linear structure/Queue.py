#coding: utf-8


class QueueUnderflow(ValueError):						#定义一个异常类
	pass
	
	
class SQueue():
	def __init__(self, inin_len=8):
		self._len = _len								#存储区长度
		self._elem = [0]*inii_len						#元素存储 list类型
		self_head = 0									#表头元素下表
		self._num = 0									#元素个数
		
	def is_empty(self):									
		return self._num == 0							
		
	def peek(self):										#查看队列里最早的元素
		if self._num == 0:
			raise QueueUnderflow
		return self._elem[self._head]
		
	def dequeue(self):									#出队操作
		if self._num == 0:
			raise QueueUnderflow
		e = self._elem[self._head]
		self._head = (self._head+1)% self._len			#取得队列首元素后更新head的值
		self._num -=1                                   #出兑一个元素使得队列元素总数减一
		return e
		
	def enqueue(self, e):								#入队操作，比较复杂
		if self._num == self._len:						#判断队列是否已满，若是则用extend
			self._extend()
		k = (self._head +self._num) % self._len			#更新元素下标值
		self._elem[k] = e
		self._num += 1
		
	def _extend(self):									#extend将存储区长度加倍，吧原有元素迁移到新表中
		old_len = self._len
		self._len *= 2
		new_elem = [0] * self._len
		for i in range(old_len):
			new_elem[i] = self._elem[(self._head+i) % old_len]
		self._elem, self._head = new_elem, 0
		
	
