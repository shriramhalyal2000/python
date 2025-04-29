if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #setting the arra
    l=set(arr)
    #listing array by list funtion
    lst=list(l)
    #sortiing in acesnding order
    lst.sort()
    #printing second last number
    print(lst[-2])