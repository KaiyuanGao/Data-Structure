#coding:utf-8


class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)]  # ʹ��list���ݽṹ��Ϊ��ϣ��Ԫ�ر��淽��
        self.count = size  # ����

    def hash(self, key):
        return key % self.count  # ɢ�к������ó���������

    def insert_hash(self, key):
        #"""����ؼ��ֵ���ϣ����"""
        address = self.hash(key)  # ��ɢ�е�ַ
        while self.elem[address]:  # ��ǰλ���Ѿ��������ˣ�������ͻ��
            address = (address+1) % self.count  # ����̽����һ��ַ�Ƿ����
        self.elem[address] = key  # û�г�ͻ��ֱ�ӱ��档

    def search_hash(self, key):
        #"""���ҹؼ��֣����ز���ֵ"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:  # ˵��û�ҵ�����ѭ�����˿�ʼ��λ��
                return False
        return True


if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(12)
    for i in list_a:
        hash_table.insert_hash(i)

    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")

    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))
