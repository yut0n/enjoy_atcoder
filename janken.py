Gu = 'g'
Choki = 'c'
Par = 'p'

host_hand = 'g'
other_hand = 'c'

def Janken_type(host_hand,other_hand){
    if host_win:
        return 1
    elif draw:
        return 0
    else:
        return 2
}

def host_win(host_hand,other_hand){
    if host_hand == Gu and other_hand == Choki:
        return True
    elif host_hand == Choki and other_hand == Par:
        return True
    elif host_hand == Par and other_hand == Gu:
        return True
    else:
        return False
}
def draw(host_hand,other_hand){
    if host_hand == other_hand:
        return True
    else:
        return False
}