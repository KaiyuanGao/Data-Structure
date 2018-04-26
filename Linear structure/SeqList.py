class SqList(object):
  
    def __init__(self, size):  
        self.data = list(None for _ in range(size))  
        self.length = 0  
        self.max_size = size 
         
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
			
    def add_item(self, item):  
        """ 
        ��ӵ���item 
        :param item: 
        :return: 
        """  
        if self.length < self.max_size:  
            self.data[self.length] = item  
            self.length += 1  
        else:  
            raise IndexError("List is full !")  
  
    def create_list(self, tar_list):  
        """ 
        ���һ��list�����б��� 
        :param tar_list: 
        :return: 
        """  
        for i, item in enumerate(tar_list):  
            if self.length >= self.max_size:  
                raise IndexError("List is full!")  
            else:  
                self.add_item(tar_list[i])  
  
    def delete(self, i):  
        """ 
        ɾ��λ��Ϊi�Ľڵ��ֵ 
        :param i: 
        :return: 
        """  
        if i > self.length or i <= 0:  
            raise IndexError("Index is out of range")  
        else:  
            j = i  
            while j < self.length:  
                self.data[j-1] = self.data[j]  
                j += 1  
            self.data[self.length - 1] = None  
            self.length -= 1  
  
    def get_elem(self, i):  
        """ 
        ����λ��Ϊi�Ľڵ��ֵ 
        :param i: 
        :return: 
        """  
        if i > self.length or i <= 0:  
            raise IndexError("Index is out of range")  
        else:  
            return self.data[i-1]  
  
    def get_location(self, elem):  
        """ 
        ���ص�һ���ڵ�ֵΪelem��λ�� 
        :param elem: 
        :return: 
        """  
        for i, item in enumerate(self.data):  
            if item == elem:  
                return i+1  
        return -1  
  
    def show_list(self):  
        """ 
        ������б������е�Ԫ�� 
        :return: 
        """  
        for i, item in enumerate(self.data):  
            if item is not None:  
                print(self.data[i]) 
            else:  
                print ('') 
                break  
  
  
if __name__ == '__main__':  
    sql = SqList(10)  
    ll = [1, 2, 3, 4, 5]  
    sql.create_list(ll)  
    sql.show_list()  
    sql.delete(1)  
    sql.show_list()  
    sql.get_elem(4)  
    b = sql.get_location(3)  
    print (b )
