#함수를 꾸며주는 함수
#인자로 함수값을 받고 다시 함수를 내보내준다.

'''
def wrapper_function(func):
    def decorated_function():
        print("함수 이전에 실행")
        func()
        print("함수 이후에 실행")
        return decorated_function

new_function = wrapper_function(basic_funtion)
#위에 과정을 밑에서 @'함수이름'을 사용하여 축약 시킨다.

@wrapper_function
def basic_function():
    print("실행하고자 하는 함수")

'''

from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"