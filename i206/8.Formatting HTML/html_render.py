#!/usr/bin/env python

"""
Python class example.
"""
import textwrap
###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Element(object):
        tag =''
        ind = ''

        def __init__(self,content=None,**kwargs):
                self.attributes = {}
                if content:
                        self.content = content
                else:
                        #self.content = ''
                        self.content = []
                if kwargs:                        
                        for key, value in kwargs.items():
                                #setattr(self, str(key), str(value))
                                self.attributes[key] = value
                
        def append(self,new_content):
                self.content.append(new_content)
                
        def render(self, file_out, ind = ''):
                file_out.write(textwrap.indent('<'+self.tag,ind))
                if len(self.attributes)>0:
                        for k,v in self.attributes.items():
                                file_out.write(' '+str(k)+'="'+str(v)+'"')
                file_out.write('>\n')
                
                if isinstance(self.content, str):
                        file_out.write(textwrap.indent(self.content, ind+'\t', predicate=None))
                else:
                        for e in self.content:
                                if isinstance(e, str):
                                        file_out.write(textwrap.indent(e, ind+'\t', predicate=None))
                                else:
                                        e.render(file_out,ind=ind+'\t')
                file_out.write('\n'+textwrap.indent('</'+self.tag+'>',ind)+'\n')

   

        
class Html(Element):
        tag = 'html'
        def render(self, file_out, ind = ''):
                file_out.write('<!DOCTYPE html>\n')
                super().render(file_out)



class Body(Element):
        tag = 'body'
        
class P(Element):
        tag = 'p'

class Head(Element):
        tag = 'head'
        
class OneLineTag(Element):
        def render(self, file_out, ind = ''):
                file_out.write(textwrap.indent('<'+self.tag+' ',ind))
                if len(self.attributes)>0:
                        for k,v in self.attributes.items():
                                file_out.write(str(k)+'="'+str(v)+'" ')
                file_out.write('>'+self.content+'</'+self.tag+'>\n')

        
class Title(OneLineTag):
        tag = 'title'

class SelfClosingTag(Element):
        def render(self, file_out, ind = ''):
                file_out.write(textwrap.indent('<'+self.tag,ind))
                if len(self.attributes)>0:
                        for k,v in self.attributes.items():
                                file_out.write(str(k)+'="'+str(v)+'" ')
                file_out.write('/>\n')

 

class Hr(SelfClosingTag):
        tag = 'hr'
        
class Br(SelfClosingTag):
        tag = 'br'               

class A(OneLineTag):
        tag = 'a' 
        def __init__(self,link,content):
            self.link =link
            super().__init__(content)

        def render(self, file_out, ind = ''):
                self.attributes['href'] = self.link
                super().render(file_out)
              

class Ul(Element):
        tag = 'ul'
        
class Li(Element):
        tag = 'li'

class H(OneLineTag):
        tag = 'h' 
        def __init__(self,no,content):
            super().__init__(content)
            self.no =no
        def render(self, file_out, ind = ''):
                file_out.write(textwrap.indent('<'+self.tag+str(self.no),ind))
                if len(self.attributes)>0:
                        for k,v in self.attributes.items():
                                file_out.write(str(k)+'="'+str(v)+'" ')
                file_out.write('>'+self.content+'</'+self.tag+'>'+'\n')
                


class Meta(SelfClosingTag):
        tag = 'meta'

 
