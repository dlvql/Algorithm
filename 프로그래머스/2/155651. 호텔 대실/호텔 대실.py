def solution(book_time):
    book_time = [list(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]) , i)) for i in book_time]
    book_time = list(map(lambda x: [x[0], x[1] + 10], book_time))
    book_time.sort()
    room = []
    for i in book_time:
        for idx, j in enumerate(room):
            if j[1] <= i[0]:
                room.pop(idx)
                break
        room.append(i)
    return len(room)