# 가사 입력 받아 입력받은 배열 반환
# quit 들어올 때까지 계속 입력받음

## 문단 구분은 어떻게 할지

str = []
def get_lyrics():
    while(True):
        line = input()
        if(line == 'quit'):
            break
        str.append(line)
    return str

print(str)