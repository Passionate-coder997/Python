Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import docx
>>> d = docx.Document()
>>> d.add_heading('THIS DOCUMENT IS CREATED USING PYTHON DOCX MODULE')
<docx.text.paragraph.Paragraph object at 0x00000000034090A0>
>>> d.add_paragraph('Hi this is word file').style = 'Title'
>>> d.add_picture('C:\\Users\\kushal\\Desktop\\python\\calcico.ico')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.add_picture('C:\\Users\\kushal\\Desktop\\python\\calcico.ico')
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\document.py", line 72, in add_picture
    return run.add_picture(image_path_or_stream, width, height)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\text\run.py", line 62, in add_picture
    inline = self.part.new_pic_inline(image_path_or_stream, width, height)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\parts\story.py", line 56, in new_pic_inline
    rId, image = self.get_or_add_image(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\parts\story.py", line 29, in get_or_add_image
    image_part = self._package.get_or_add_image_part(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\package.py", line 31, in get_or_add_image_part
    return self.image_parts.get_or_add_image_part(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\package.py", line 74, in get_or_add_image_part
    image = Image.from_file(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\image\image.py", line 46, in from_file
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\kushal\\Desktop\\python\\calcico.ico'
>>> d.add_picture('C:\\Users\\kushal\\Desktop\\python\\calico.ico')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d.add_picture('C:\\Users\\kushal\\Desktop\\python\\calico.ico')
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\document.py", line 72, in add_picture
    return run.add_picture(image_path_or_stream, width, height)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\text\run.py", line 62, in add_picture
    inline = self.part.new_pic_inline(image_path_or_stream, width, height)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\parts\story.py", line 56, in new_pic_inline
    rId, image = self.get_or_add_image(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\parts\story.py", line 29, in get_or_add_image
    image_part = self._package.get_or_add_image_part(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\package.py", line 31, in get_or_add_image_part
    return self.image_parts.get_or_add_image_part(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\package.py", line 74, in get_or_add_image_part
    image = Image.from_file(image_descriptor)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\image\image.py", line 55, in from_file
    return cls._from_stream(stream, blob, filename)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\image\image.py", line 176, in _from_stream
    image_header = _ImageHeaderFactory(stream)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\docx\image\image.py", line 199, in _ImageHeaderFactory
    raise UnrecognizedImageError
docx.image.exceptions.UnrecognizedImageError
>>> d.add_picture('C:\\Users\\kushal\\Desktop\\python\\one.png')
<docx.shape.InlineShape object at 0x000000000340EB80>
>>> d.add_picture('C:\\Users\\kushal\\Desktop\\python\\two.png')
<docx.shape.InlineShape object at 0x000000000340EEB0>
>>> d.add_picture('C:\\Users\\kushal\\Desktop\\python\\three.png')
<docx.shape.InlineShape object at 0x000000000340EFD0>
>>> d.add_table(rows=5, cols=5)
<docx.table.Table object at 0x00000000034090A0>
>>> d.save('C:\\Users\\kushal\\Desktop\\python\\createdwithpy.docx')
>>> 