import html_render as hr

body = hr.Body()
x=hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text", style=u"text-align: center; font-style: oblique;")
print(x.__dict__)
body.append(x)


'''
def __init__(self,first,last,pay,prog_lang):
    super().__init__(first,last,pay)
    Employee.__init__(self,first,last,pay)
    self.prog_lang= prog_lang
'''
