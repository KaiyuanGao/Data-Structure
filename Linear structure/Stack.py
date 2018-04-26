# coding: utf-8



class StackUnderflow(ValueError):		#定义一个异常类，通过raise引发
	pass
	

class SStack():							#基于顺序表技术实现的栈类
	def __init__(self):
		self._elems = []				#所有栈操作都映射到list操作
		
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
		
		
class LStack():							#基于链接表技术实现的栈类
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


	
		
		
		

	
	
	
	
	
	
	
	
	
	
	
	
	
