def solution(s):
    st = list()
    for i in s:
        if st and st[-1] == i:
            st.pop()
        else:
            st.append(i)
    return 1 if not st else 0