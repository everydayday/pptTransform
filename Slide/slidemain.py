# from get_lyrics import get_lyrics
from math import ceil  # slide 갯수구하기 by 올림

import win32com.client
from pptx import Presentation  # 라이브러리
from pptx.util import Pt, Cm
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import ColorFormat, RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

# from pptx_tools import utils


def get_slide_num(lyric_str):
    slide_num = ceil(len(lyric_str) / 2)
    print(lyric_str.count('\n'))
    return slide_num


# slide_str 만들기 / index : 슬라이드마다 들어가는 가사 두줄
def get_slide_str(lyric_str):
    my_list = lyric_str.split('\n')
    slide_list = []
    idx_count = 0

    for idx, value in enumerate(my_list):
        if idx % 2 == 0 and value == '':
            my_list[idx] = '\n'
            my_list.insert(idx + 1, '\n')

    for idx, value in enumerate(my_list):

        if idx % 2 == 0:
            if value == '':
                slide_list.append('\n')
                slide_list.append('\n')
                idx_count += 1
            else:
                slide_list.append(value)
        else:
            if value == '\n':
                slide_list[idx_count] = slide_list[idx_count] + value
                idx_count += 1
            else:
                slide_list[idx_count] = slide_list[idx_count] + "\n" + value
                idx_count += 1

    return slide_list
    slide_str = []
    slide_num = get_slide_num(lyric_str)
    '''
    for idx in range(lyric_str):
        slide_str[idx // 2] = slide_str[idx // 2] + value
    '''
    for i in range(slide_num):
        try:
            slide_str.append(lyric_str[i * 2] + lyric_str[i * 2 + 1].replace("\n", ""))
        except IndexError:  # 가사줄의 갯수가 홀수여서 마지막에 str[i*2]까지만 해당할 시
            slide_str.append(lyric_str[i * 2])

    return slide_str


# slide 생성
# 가사만 주면 ok
def make_slide(lyric_str, font_size=30, font_style='함초름돋음',font_col_rgb=(0,0,0), background_col_rgb = (0,0,0)):  # slide_str 아무 값도 없을 시, 오류 메시지 출력
    # 파워포인트 객체 선언                                                       # font_col_rgb : tuple 로 넘겨줌
    print("start in make_slide")
    prs = Presentation()
    prs.slide_width = Inches(16)
    prs.slide_height = Inches(9)
    # slide 마다 가사 리스트
    slide_str = get_slide_str(lyric_str)
    # slide 갯수 구하기 (올림)
    global slide_num
    slide_num = len(slide_str)
    # slide_num = ceil(len(lyric_str) / 2)
    # slide 만들기
    for i in range(0, slide_num):
        blank_slide_layout = prs.slide_layouts[6]  # 슬라이드 종류 선택
        slide = prs.slides.add_slide(blank_slide_layout)  # 슬라이드 추가

        # 위치, 가로/세로 길이 - 텍스트 상자
        left = Cm(0)
        top = Cm(0)
        width = Cm(25.4)
        height = Cm(19)


        # https://vincinotes.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%8C%EC%9B%8C%ED%8F%AC%EC%9D%B8%ED%8A%B8-%EC%9E%90%EB%8F%99%ED%99%94-python-pptx-%EB%A7%8C%EB%93%A4%EA%B8%B0/
        # 도형 삽입 for background
        shapes = slide.shapes
        left = top = Inches(1)
        width = Inches(8)
        height = Inches(5.5)
        shape = shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height) # ppt 크기 만큼 설정

        # 도형 색 채우기
        fill = shape.fill
        fill.solid()
        # fill.patterned()
        fill.fore_color.rgb = RGBColor(background_col_rgb[0], background_col_rgb[1], background_col_rgb[2])

        # 텍스트 상자 넣기
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.text = slide_str[i]
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE  # TOP 부분만 나와서 MIDDLE 찍었는데 이게 되네...
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        tf.paragraphs[0].font.name = font_style
        tf.paragraphs[0].font.size = Pt(font_size)
        #tf.paragraphs[0].font.color.rgb = RGBColor(255, 0, 0)
        print("font_col_rgb in make_slide :",font_col_rgb)
        tf.paragraphs[0].font.color.rgb = RGBColor(font_col_rgb[0],font_col_rgb[1],font_col_rgb[2])
        # title = prs.slides[i].shapes.title
        # content = slide.placeholders[0]
        # content.text = slide_str[i]
        # p = title.text_frame.paragraphs[0]
        # run = p.add_run()


        # title.text_frame.paragraphs[0].font.name = font_style
    print(tf.text)
    print("----------------------------")
    '''
    print("before prs.save in make_slide")
    #prs.save('add all slides.pptx')
    #prs.save('doit.pptx')
    prs.save('add all slides1.pptx')
    print("after prs.save in make_slide")
    '''

    prs.save('add all slides1.pptx')

# image 저장
def save_pptx_as_png():

    print("start in save_pptx_as_png")
    Application = win32com.client.Dispatch("PowerPoint.Application")
    print("before Presentation in save_pptx_as_png")

    Presentation = Application.Presentations.Open(r"C:\Users\김대희\PycharmProjects\pythonProject2 - 복사본\UI\add all slides1.pptx", WithWindow=False) #withwindow : background 실행
    print("after Presentation in save_pptx_as_png")
    # 상대 경로로 설정하니 오류가 나네...?

    for i in range(slide_num):
        Presentation.Slides[i].Export(r"C:\Users\김대희\PycharmProjects\pythonProject2 - 복사본\slideImagefolder\pptimage{}.png".format(i), "PNG") # jpg 하니깐 표시가 안 돼.


    Application.Quit()
    esentation = None
    Application = None


def slide_main(lyric_str, font_style = '함초름돋움', font_size = 30, font_col_rgb=(255,255,255),background_col_rgb = (0,0,0)):
    print("start in slide_main")
    make_slide(lyric_str, font_size, font_style, font_col_rgb,background_col_rgb)
    print("before save_pptx_as_png")
    save_pptx_as_png()
    # png_folder = 'C:/Users/김대희/PycharmProjects/pythonProject2/Slide'
    # pptx_file = 'C:/Users/김대희/PycharmProjects/pythonProject2/Slide/add all slides1.pptx'
    # utils.save_pptx_as_png(png_folder, pptx_file)


if __name__ == '__main__':
    slide_main()