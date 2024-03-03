import random
while True:
    val_list = ['가위', '바위', '보']
    computer = random.choice(val_list)
    
    user = input('가위 바위 보 중에 하나를 입력하세요(종료: 0): ')
    print(f"user: {user}, computer: {computer}")
    if user == '0':
        print('게임을 종료합니다.')
        break
    elif user not in val_list:
        print('다시 입력해주세요.')
        continue

    if user == computer:
        print('비겼습니다.')
    elif (user == '가위' and computer == '보') or (user == '바위' and computer == '가위') or (user == '보' and computer == '바위'):
        print('유저가 이겼습니다.')
    else:
        print('컴퓨터가 이겼습니다.')