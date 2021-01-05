# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/12/16 22:29'

class algorithm():
    def insert_sort(self,lst):
        sort_lists=lst[:]
        for i in range(1,len(sort_lists)):
            key=sort_lists[i]
            j=i-1
            while j>=0:
                if sort_lists[j]>=key:
                    sort_lists[j+1]=sort_lists[j]
                    sort_lists[j]=key
                else:
                    break
                j-=1
        return sort_lists

    def shell_sort(self,lst):
        sort_lists=lst[:]
        k=int(n/2)

           for i in range(k,n)




if __name__=='__main__':
    a=[9,10,1,2,3]
    insert_lists=algorithm().insert_sort(a)

    print(insert_lists)