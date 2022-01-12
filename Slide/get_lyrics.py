# 가사 입력 받아 입력받은 배열 반환
# quit 들어올 때까지 계속 입력받음

# 문단 구분은 어떻게 할지


def get_lyrics():           # 아무 값도 안 들어올시 처리..
    with open('lyrics.txt','r', encoding='UTF8') as f:
        lyric_str = f.readlines()

    # while(True):
    #     line = input()
    #     if(line == 'quit'):
    #         break
    #     str.append(line)
    return lyric_str

