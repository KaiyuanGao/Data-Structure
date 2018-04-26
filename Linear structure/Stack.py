# coding: utf-8



class StackUnderflow(ValueError):		#����һ���쳣�࣬ͨ��raise����
	pass
	

class SStack():							#����˳�����ʵ�ֵ�ջ��
	def __init__(self):
		self._elems = []				#����ջ������ӳ�䵽list����
		
	def is_empty(self):
		return self._elems == []
		
	def top(self):						
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]
	
	def push(self, elem):
		self._elems.append(elem)
		
	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems.pop()
		
		
class LStack():							#�������ӱ���ʵ�ֵ�ջ��
	def __init__(self):
		self._top = None
	
	def is_empty(self):
		return self._top is None
	
	def top(self):
		if self._top is None:
			raise StackUnderflow("in LStack.top()")
		return self._top.elem
		
	def push(self,elem):
		self._top = LKNOde(elem,self._top)
		
	def pop(self):
		if self._top is None:
			raise StackUnderflow("in LStack.pop()")
		p = self._top
		self._top = p.next
		return p.elem


	
		
		
		

	
	
	
	
	
	
	
	
	
	
	
	
	
