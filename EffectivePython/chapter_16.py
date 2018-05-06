'''
@author：KongWeiKun
@file: chapter_16.py
@time: 17-10-19 下午2:02
@contact: 836242657@qq.com
'''
def index_words(text):
    result=[]
    if text:
        # result.append(0)
        yield 0
    for index,letter in enumerate(text):
        if letter== ' ':
            # result.append(index+1)
            yield index+1
    return result

address='Four score and seven years ago...'
result=list(index_words(address))
print(result[:3])
