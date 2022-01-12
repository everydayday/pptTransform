from pptx import Presentation  # 라이브러리
from pptx.util import Pt
from get_lyrics import get_lyrics
from math import ceil # slide 갯수구하기 by 올림




def get_slide_num(lyric_str):
    slide_num = ceil(len(lyric_str) / 2)
    return slide_num


# slide_str 만들기 / index : 슬라이드마다 들어가는 가사 두줄
def get_slide_str(lyric_str) :
    slide_str = []
    slide_num = get_slide_num(lyric_str)
    for i in range(slide_num):
        try:
            slide_str.append(lyric_str[i*2]  + lyric_str[i*2+1])
        except IndexError: # 가사줄의 갯수가 홀수여서 마지막에 str[i*2]까지만 해당할 시
            slide_str.append(lyric_str[i*2]  )
    return slide_str



# 창이 열리고
# 가사 입력



# slide 생성
# 가사만 주면 ok
def make_slide(lyric_str ,font_size = 30, font_style = '함초름돋음'):    # slide_str 아무 값도 없을 시, 오류 메시지 출력
    # 파워포인트 객체 선언
    prs = Presentation()
    # slide 마다 가사 리스트
    slide_str = get_slide_str(lyric_str)
    # slide 갯수 구하기 (올림)
    slide_num = ceil(len(lyric_str) / 2)
    # slide 만들기
    for i in range(0, slide_num):
        title_slide_layout = prs.slide_layouts[0]  # 슬라이드 종류 선택
        slide = prs.slides.add_slide(title_slide_layout)  # 슬라이드 추가
        content = slide.placeholders[0]
        content.text = slide_str[i]
        title = prs.slides[i].shapes.title
        title.text_frame.paragraphs[0].font.name = font_style
        #title.text_frame.paragraphs[1].font.name = font_style #paragraph : 단락/행/엔터기준 구분
        title.text_frame.paragraphs[0].font.size = Pt(font_size)
        #title.text_frame.paragraphs[1].font.size = Pt(font_size)

    prs.save('add all slides1.pptx')





if __name__ == '__main__':
    # 전체 가사 입력
    lyric_str = get_lyrics()
    make_slide(lyric_str, 10)
