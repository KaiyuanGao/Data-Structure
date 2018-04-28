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
			

class MinHeap:
    def __init__(self, item=[]):
        # ��ʼ����itemΪ����
        self.items = item
        self.heapsize = len(self.items)

    def LEFT(self, i):
        return 2 * i + 1

    def RIGHT(self, i):
        return 2 * i + 2

    def PARENT(self, i):
        return (i - 1) / 2

    def MIN_HEAPIFY(self, i):
        # ��С�ѻ���ʹ��iΪ����������Ϊ��С��
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heapsize and self.items[l] < self.items[i]:
            smallest = l
        else:
            smallest = i

        if r < self.heapsize and self.items[r] < self.items[smallest]:
            smallest = r

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.MIN_HEAPIFY(smallest)

    def INSERT(self, val):
        # ����һ��ֵval�����ҵ���ʹ����ѽṹ
        self.items.append(val)
        idx = len(self.items) - 1
        parIdx = self.PARENT(idx)
        while parIdx >= 0:
            if self.items[parIdx] > self.items[idx]:
                self.items[parIdx], self.items[idx] = self.items[idx], self.items[parIdx]
                idx = parIdx
                parIdx = self.PARENT(parIdx)
            else:
                break
        self.heapsize += 1

    def DELETE(self):
        last = len(self.items) - 1
        if last < 0:
            # ��Ϊ��
            return None
        # else:
        self.items[0], self.items[last] = self.items[last], self.items[0]
        val = self.items.pop()
        self.heapsize -= 1
        self.MIN_HEAPIFY(0)
        return val


    def BUILD_MIN_HEAP(self):
        # ������С��, O(nlog(n))
        i = self.PARENT(len(self.items) - 1)
        while i >= 0:
            self.MIN_HEAPIFY(i)
            i -= 1

    def SHOW(self):
        print(self.items)


class MinPriorityQ(MinHeap):
    def __init__(self, item=[]):
        MinHeap.__init__(self, item)

    def enQ(self, val):
        MinHeap.INSERT(self, val)

    def deQ(self):
        val = MinHeap.DELETE(self)
        return val
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
