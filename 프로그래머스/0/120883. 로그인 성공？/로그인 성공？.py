def solution(id_pw, db):
    for v in db:
        if id_pw == v:
            return "login"
        elif id_pw[0] == v[0] and id_pw[1] != v[1]:
            return 'wrong pw'
    return "fail"