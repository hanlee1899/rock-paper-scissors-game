import random

def up_down_game():
    print('\n--------------------------------------------------------------------------------------\n')
    print('~~업다운 게임~~\n')
    print('<<게임 설명>>')
    print('1) 당신은 3번의 기회 안에 컴퓨터가 선택한 숫자를 맞춰야 합니다.')
    print('2) 숫자의 범위는 1이상 10이하이고, 자연수입니다.')
    print('3) 당신이 제시한 숫자가 컴퓨터가 선택한 숫자보다 클시 <다운> 을 출력합니다.')
    print('4) 당신이 제시한 숫자가 컴퓨터가 선택한 숫자보다 작을시 <업> 을 출력합니다.')
    print('5) 3번안에 숫자를 맞추지 못할시 당신은 10코인을 얻습니다.')
    print('6) 1번안에 맞출시 200코인, 2번안에 맞출시 150코인, 3번안에 맞출시 100코인을 얻습니다.')
    print('\n--------------------------------------------------------------------------------------\n')

    my_coin = 0
    chance = 3
    computer_number = random.randrange(1, 11)
    while chance > 0:
        print('숫자를 제시하세요.')
        try:
            my_number = int(input('>> '))
            print()

            if my_number <= 0 or my_number > 10:
                print('<1이상 10이하의 자연수만 입력할 수 있습니다>\n\n다시 입력하세요.')
                continue
        except:
            print('\n<자연수가 아닌 값은 입력할 수 없습니다>\n\n다시 입력하세요.')
            continue
        
        if my_number > computer_number:
            print('컴퓨터: <다운>\n')
        elif my_number < computer_number:
            print('컴퓨터: <업>\n')
        else:
            print(f'정답입니다!! {4 - chance}번 안에 맞추셨으므로 {200 - 50 * (3 - chance)}코인을 드립니다.\n')
            my_coin = 200 - 50 * (3 - chance)
            break
        
        chance -= 1
    if my_coin == 0:
        print(f'컴퓨터가 선택한 숫자는 {computer_number}이였습니다.\n3번 안에 맞추지 못하셨으므로 10코인을 드립니다.\n')
        my_coin = 10
    
    return my_coin
        
def game_manager():
    print('<가위바위보 게임에 필요한 코인을 얻기 위해 <<업다운 게임>>을 진행해야 합니다>')
    while True:
        print('1: 업다운 게임 진행\n2: 게임 종료')
        try:
            my_answer = int(input('>> '))
            print()

            if my_answer != 1 and my_answer != 2:
                print('<선택지 1번과 2번 중에서만 선택이 가능합니다>\n\n다시 입력하세요.')
                continue

            if my_answer == 1:
                my_coin = up_down_game()
                break
            else:
                print('게임을 종료합니다.')
                return
        except:
            print('\n<1또는 2만 입력가능합니다>\n\n다시 입력하세요.')
            continue

    cnt_win, cnt_lose = 0, 0

    while True:
        print('1: 가위바위보 게임 진행\n2: 현재 코인 잔액 확인\n3: 현재 승률 확인\n4: 게임 종료')
        try:
            my_answer = int(input('>> '))
            print()

            if my_answer != 1 and my_answer != 2 and my_answer != 3 and my_answer != 4:
                print('<선택지 1번 ~ 4번 중에서만 선택이 가능합니다>\n\n다시 입력하세요.')
                continue

            if my_answer == 1:
                if my_coin == 0:
                    print('<보유 중이신 코인이 없습니다>\n')
                    game_manager()
                    break
                my_coin, cnt_win, cnt_lose = rock_paper_scissors_game(my_coin, cnt_win, cnt_lose)
            elif my_answer == 2:
                print(f'현재 나의 코인: {my_coin}\n')
                continue
            elif my_answer == 3:
                if cnt_win + cnt_lose == 0:
                    print('<현재까지 이기거나 진 게임이 없어 승률을 계산할 수 없습니다>\n')
                    continue
                odds_of_winning = round(cnt_win / (cnt_win + cnt_lose) * 100, 2)
                print(f'현재 승률은 {odds_of_winning}% 입니다.\n')
            elif my_answer == 4:
                print('게임을 종료합니다.')
                break
        except:
            print('\n<선택지 1번 ~ 4번 중에서만 선택이 가능합니다>\n\n다시 입력하세요.')
            continue

def rock_paper_scissors_game(my_coin, cnt_win, cnt_lose):
    print('\n--------------------------------------------------------------------------------------\n')
    print('~~가위바위보 게임~~\n')
    print('<<게임 설명>>')
    print('1) 당신은 [가위, 바위, 보] 중 하나의 선택만 할 수 있습니다')
    print('2) 가위바위보를 이길 시 투자한 코인의 랜덤 배수만큼을 얻습니다.')
    print('3) 가위바위보를 패배할 시 투자한 코인을 모두 잃습니다.')
    print('4) 가위바위보를 비길 시 투자한 코인을 돌려받습니다.')
    print('\n--------------------------------------------------------------------------------------\n')

    while True:
        try:
            print('투자할 코인을 입력하세요.')
            invest_coin = int(input('>> '))
            print()

            if invest_coin <= 0:
                print('<0보다 작거나 같은 코인을 투자할 수 없습니다>\n\n다시 입력하세요.')
                continue
            if invest_coin > my_coin:
                print('<현재 가지고 있는 코인보다 높게 투자할 수 없습니다>\n\n다시 입력하세요.')
                continue
            break
        except:
            print('\n<숫자만 입력가능합니다>\n\n다시 입력하세요.')
            continue

    my_coin -= invest_coin
    print('게임을 시작합니다!!\n')
    com_choice = random.choice(['가위', '바위', '보'])

    while True:
        print('가위, 바위, 보 중 하나를 입력하세요.')
        my_choice = input('>> ')
        print()

        if my_choice != '가위' and my_choice != '바위' and my_choice != '보':
            print('<가위, 바위, 보 만 입력할 수 있습니다>\n\n다시 입력하세요.')
            continue
        break

    print(f'컴퓨터: {com_choice}')
    print(f'나: {my_choice}\n')
    game_result = game_referee(com_choice, my_choice)

    if game_result == 0:
        print(f'비기셨습니다!!\n{invest_coin}코인을 돌려받습니다.\n')
        my_coin += invest_coin
    elif game_result == 1:
        print(f'패배하셨습니다!!\n{invest_coin}코인을 잃습니다.\n')
        cnt_lose += 1
    else:
        print('이기셨습니다!!')
        randomNum = random.randrange(2, 6)
        print(f'축하합니다!! 투자한 코인의 {randomNum}배인 {invest_coin * randomNum}코인을 돌려받습니다.\n')
        my_coin += invest_coin * randomNum 
        cnt_win += 1
    
    return my_coin, cnt_win, cnt_lose

def game_referee(com_choice, my_choice):
    if com_choice == '가위':
        if my_choice == '가위':
            return 0
        elif my_choice == '바위':
            return 2
        else:
            return 1
    elif com_choice == '바위':
        if my_choice == '가위':
            return 1
        elif my_choice == '바위':
            return 0
        else:
            return 2
    else:
        if my_choice == '가위':
            return 2
        elif my_choice == '바위':
            return 1
        else:
            return 0

game_manager()