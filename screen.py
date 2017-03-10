# -*- coding: utf-8 -*-

'@property练习'

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
    	if not isinstance(value, int):
        	raise ValueError('width must be an integer!')
    	self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
    	if not isinstance(value, int):
        	raise ValueError('height must be an integer!')
    	self._height = value

    @property
    def resolution(self):
        return self._width * self._height

#test
s = Screen()
s.width  = 1024
s.height = 768

print(s.resolution)