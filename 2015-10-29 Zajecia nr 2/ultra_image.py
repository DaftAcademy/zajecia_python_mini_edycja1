# -*- coding: utf-8 -*- 

from PIL import (
	Image,
	ImageStat,
)


class UltraImage(object):
	
	def __init__(self, image_path):
		self.image_path = image_path
		img = Image.open(self.image_path)
		self.pil_image = img.convert('RGB')
		self._brightness = None

	@property
	def size(self):
		return self.pil_image.size

	@property
	def brightness(self):
		if not self._brightness:
			istat = ImageStat.Stat(self.pil_image)
			x = istat.mean
			bval = (
				(0.2126 * x[0]) 
				+ (0.7152 * x[1]) 
				+ (0.0722 * x[2])
			)
			self._brightness = bval

		return self._brightness
