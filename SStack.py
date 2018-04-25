# coding: utf-8

class StackUnderflow(ValueError):
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
		
#ջ�ļ�Ӧ�ã�����ƥ������

def check_parent(text):
	parent = "()[]{}"
	open_parent = "([{"
	opposite = {")":"(", "]":"[", "} ":"{"}
	
	def parentheses(text):
		i = 0
		size = len(text)
		while True:
			while i < size and text[i] not in parent:
				i += 1
			if i >= size:
				return 
			yield text[i], i
			i += 1
			
	st = SStack()
	for pr, i in parentheses(text):
		if pr in open_parent:
			st.push(pr)
		elif st.pop() != opposite[pr]:
			print("Unmatching is found at", i, "for", pr)
			return False
	print("all parentheses are correctly matched.")
	return True
	
	
	
check_parent("fdf}fd{dfs[}fd)(fdsf{")	
	
	
	
	
	
	
	
	
	
	
	
	
	
