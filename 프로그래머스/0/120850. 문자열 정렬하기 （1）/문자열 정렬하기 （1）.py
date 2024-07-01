def solution(my_string):
    ans = []
    for i in my_string:
        if(ord(i) <= 57):
            ans.append(int(i))
    ans.sort()
    return ans