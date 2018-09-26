from PIL import Image
import pytesseract

# https://www.jianshu.com/p/5c8c6b170f6f     参考这篇文章

# 上面都是导包，只需要下面这一行就能实现图片文字识别
text = pytesseract.image_to_string(Image.open(r'E:\work\python\com\wenzishibie\2.png'), lang='test200')
print(text)
print(type(text))
# if text.__contains__("召 唤"):
#     print("true")