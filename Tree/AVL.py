#!/usr/bin/python
#coding=utf-8



class ALVTreeNode():  
    def __init__(self, data, height, freq, left, right):  
        self.data = data;  
        self.height = height;  
        self.freq = freq;  
        self.left = left;  
        self.right = right;  
  
#С��<����  
def less(x1, x2):  
    return x1 < x2;  
      
class ALVTree():  
    def __init__(self):  
        self.root = None;  
        self.left = None;  
        self.right = None;  
  
    def setValue(self, root, left, right):  
        self.root = root;  
        self.left = left;  
        self.right = right;  
  
    def getValue(self):  
        return [self.root, self.left, self.right];  
  
          
    def info(self, node):  
        if (node == None):  
            info = 'None';  
        else:  
            if (node.left == None):  
                sL = 'None';  
            else:  
                sL = node.left.data;  
  
            if (node.right == None):  
                sR = 'None';  
            else:  
                sR = node.right.data;  
  
            info = [node.data, node.height, node.freq, sL, sR];  
        print(info);  
  
    def genNode(self, data, height, freq, left, right):  
        return ALVTreeNode(data, height, freq, left, right);  
  
          
    def height(self, node):  
        if (node == None):  
            return 0;  
        else:  
            lh = self.height(node.left);  
            rh = self.height(node.right);  
  
            node.height = max(lh, rh)+1;  
              
            return node.height;  
  
    #��������µ���ת  
    #������Ǹ߶���ߵĽڵ㣬Ҳ���Ǵ������root  
    def rotateLL(self, k2):  
        k1 = k2.left;  
        k2.left = k1.right;  
        k1.right = k2;  
  
        k2.height = max(self.height(k2.left), self.height(k2.right))+1;  
        k1.height = max(self.height(k1.left), k2.height)+1;  
  
        return k1;  
  
    #��������µ���ת  
    #������Ǹ߶���ߵĽڵ㣬Ҳ���Ǵ������root  
    def rotateRR(self, k2):  
        k1 = k2.right;  
        k2.right = k1.left;  
        k1.left = k2;  
  
        k2.height = max(self.height(k2.left), self.height(k2.right))+1;  
        k1.height = max(self.height(k1.right), k2.height)+1;  
  
        return k1;  
  
    #�����������ת  
    #������Ǹ߶���ߵĽڵ㣬Ҳ���Ǵ������root  
    def rotateLR(self, k3):  
        k1 = self.rotateRR(k3.left);  
        k3.left = k1;  
        k2 = self.rotateLL(k3);  
  
        return k2;  
  
    #�����������ת  
    #������Ǹ߶���ߵĽڵ㣬Ҳ���Ǵ������root  
    def rotateRL(self, k3):  
        k1 = self.rotateLL(k3.right);  
        k3.right = k1;  
        k2 = self.rotateRR(k3);  
  
        return k2;  
  
    #ƽ��ֵ  
    def balanceFlag(self, node):  
        return self.height(node.left)-self.height(node.right);  
  
    #��ƽ��  
    def LBalance(self, root):  
        p = root;  
        c = p.left;  
        rc = c.right;  
  
        cbf = self.balanceFlag(c);  
  
        if (cbf == 1):  
            root = self.rotateLL(root);  
        elif (cbf == -1):  
            root = self.rotateLR(root);  
  
        return root;  
  
    #��ƽ��  
    def RBalance(self, root):  
        p = root;  
        c = p.right;  
        lc = c.left;  
  
        cbf = self.balanceFlag(c);  
  
        if (cbf == -1):  
            root = self.rotateRR(root);  
        elif (cbf == 1):  
            root = self.rotateRL(root);  
  
        return root;  
