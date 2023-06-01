""" 
figure모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈입니다. line class를 이용하여 선의 길이를 설정/참조를 수행하며 
area_square, are_circle, are_regular_triangle 함수로
각각 직사각형, 타원, 직각삼각형의 넓이를""" 
class line:
    """ 
     line class 는 선의 길이에 대해 저장하고 있는 클래스
     변수로는 외부에서 접근 불가능한 __width와 __height가 있으며,
     해당 변수를 수정하고 접근하기 위해
     set_length와, get_length 메소드를 제공      
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """ 
        생성자 초기 width와 height 값을 받는다
        Args:
        width (int or float) : 초기 선의 가로 길이 값입니다.
        height (int or float): 초기 선의 세로 길이 값입니다.
        """
        self.__width = width
        self.__height = height
    def set_length(self, width, height):
        """ 
         선의 길이를 수정
          Args:
          width (int or float) : 초기 선의 가로 길이 값입니다.
          height (int or float): 초기 선의 세로 길이 값입니다.
          """
        self.__width = width
        self.__height = height
    def get_length(self):
        """ 객체가 저장하고 있는 선의 길이를 변환합니다
         Returns:
          int or float :저장하고 있는 선의 길이 """
        return self.__width, self.__height
def area_rectangle(width, height):
    """
    길이를 입력받아 직사각형의 넓이를 구하는 함수
    Args:
        width (int or float) : 밑변의 길이
        height (int or float) : 높이의 길이
    Returns:
        int or float : 직사각형의 넓이를 반환
    """
def area_ellipse(width, height):
    """ 길이를 매개변수로 입력받아 타원의 넓이를 구하는 함수
         Args:
            width  (int or float) : 짧은 쪾 반지를 길이
            height (int or float) : 긴쪽 반지름 길이
        Returns:
         int or float: 원의 넓이를 반환 """
    if width <= 0 or height <= 0 : raise ValueError
    return height * width * math.pi
def area_right_triangle(width, height):
    """ 길이를 매개변수로 입력받아 직각삼각형의 넓이를 구하는 함수
        Args:
            width (int or float): 밑변의 길이
            height (int or float) : 높이의 길이
        Returns: 
            int or float: 직각삼각형의 넓이를 반환 """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2
def area_regular_triangle(length):
    """ length를 매개변수로 입력받아 정삼각형의 넓이를 구하는 함수
         Args:
          length (int of float):한변의 길이
        Returns:
         int or float : 정삼각형의 넓이를 반환
        """
    return length*length*math.sqrt(3)/4
 