from pptx import Presentation  # 라이브러리
from pptx.util import Pt
from get_lyrics import get_lyrics
from math import ceil # slide 갯수구하기 by 올림
from comtypes.client import Constants, CreateObject
import os
from pptx_tools import utils




def get_slide_num(lyric_str):
    slide_num = ceil(len(lyric_str) / 2)
    return slide_num


# slide_str 만들기 / index : 슬라이드마다 들어가는 가사 두줄
def get_slide_str(lyric_str) :
    slide_str = []
    slide_num = get_slide_num(lyric_str)
    '''
    for idx in range(lyric_str):
        slide_str[idx // 2] = slide_str[idx // 2] + value
    '''
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
        p = title.text_frame.paragraphs[0]
        run = p.add_run()

        title.text_frame.paragraphs[0].font.name = font_style
        print(content.text)
        print("----------------------------")
        #title.text_frame.paragraphs[1].font.name = font_style #paragraph : 단락/행/엔터기준 구분
        title.text_frame.paragraphs[0].font.size = Pt(font_size)
        #title.text_frame.paragraphs[1].font.size = Pt(font_size)

    prs.save('add all slides1.pptx')




''' image 저장
def save_pptx_as_png(png_foldername, pptx_filename, overwrite_folder: bool = False):
    if os.path.isdir(png_foldername) and not overwrite_folder:
        print(f"Folder {png_foldername} already exists. "
              f"Set overwrite_folder=True, if you want to overwrite folder content.")
        return

    powerpoint = CreateObject("Powerpoint.Application")
    pp_constants = Constants(powerpoint)

    pres = powerpoint.Presentations.Open(pptx_filename)
    pres.SaveAs(png_foldername, pp_constants.ppSaveAsPNG)
    pres.close()
    if powerpoint.Presentations.Count == 0:  # only close, when no other Presentations are open!
        powerpoint.quit()

'''

if __name__ == '__main__':
    # 폰트 크기, 스타일 입력
    while True:
        try: # 잘못입력했을 시
            size = input("원하는 폰트 사이즈를 입력해주세요 : ")
            style = input("원하는 폰트 스타일을 입력해주세요 : ")

            if size == '': # 디폴트 값
                 font_size = 30
            else: # 주어진 값 있을 시
                font_size = int(size)
            if style == '': # 디폴트 값
                font_style = '함초름돋음'
            else: ## 이상한 폰트 입력해도 입력이 된다는 문제점 ##
                font_style = style
            break # 오류 없으면 while문 넘어가기
        except ValueError: # 숫자가 아닌 값 입력 시
            print("잘못된 값을 입력했습니다.")
            print("처음부터 다시 입력하세요.")



    lyric_str = get_lyrics()
    make_slide(lyric_str, font_size, font_style)
    #save_pptx_as_png('all_slides_to_png','C:/Users/김대희/PycharmProjects/pythonProject2/Slide/add all slides1.pptx')
    png_folder = 'C:/Users/김대희/PycharmProjects/pythonProject2/Slide'
    pptx_file ='C:/Users/김대희/PycharmProjects/pythonProject2/Slide/add all slides1.pptx'
    utils.save_pptx_as_png(png_folder, pptx_file)