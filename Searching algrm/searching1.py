#coding:utf-8

def unorder_search(lists, key): 
	#���������㷨
    length = len(lists)
    for i in range(length):
        if lists[i] == key:
            return i
        else:
            return False



def binary_search(lists, key):
	#���ֲ����㷨
    low = 0
    high = len(lists) - 1
    time = 0
    while low <= high:
        time += 1
        mid = int((low + high) / 2)
        if key < lists[mid]:
            high = mid - 1
        elif key > lists[mid]:
            low = mid + 1
        else:
            # ��ӡ�۰�Ĵ���
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False
    
    
def binary_search2(lists, key):
	#��ֵ�����㷨
    low = 0
    high = len(lists) - 1
    time = 0
    while low <= high:
        time += 1
        # ����midֵ�ǲ�ֵ�㷨�ĺ��Ĵ���
        mid = low + int((high - low) * (key - lists[low])/(lists[high] - lists[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lists[mid]:
            high = mid - 1
        elif key > lists[mid]:
            low = mid + 1
        else:
            # ��ӡ���ҵĴ���
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False




def fibonacci_search(lists, key):
    # ��Ҫһ���ֳɵ�쳲������б������Ԫ�ص�ֵ���볬�����ұ���Ԫ�ظ�������ֵ��
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]
    low = 0
    high = len(lists) - 1    
    # Ϊ��ʹ�ò��ұ�����쳲��������ԣ��ڱ�������Ӽ���ͬ����ֵ
    # ���ֵ��ԭ���ұ������Ǹ�Ԫ�ص�ֵ
    # ��ӵĸ�����F[k]-1-high����
    k = 0
    while high > F[k]-1:
        k += 1
    print(k)
    i = high
    while F[k]-1 > i:
        lis.append(lists[high])
        i += 1
    print(lists)
    
    # �㷨���߼���time����չʾѭ���Ĵ�����
    time = 0
    while low <= high:
        time += 1
        # Ϊ�˷�ֹF�б��±����������if��else
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1]-1
        
        print("low=%s, mid=%s, high=%s" % (low, mid, high))
        if key < lists[mid]:
            high = mid - 1
            k -= 1
        elif key > lists[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                # ��ӡ���ҵĴ���
                print("times: %s" % time)
                return mid
            else:
                print("times: %s" % time)
                return high
    print("times: %s" % time)
    return False
