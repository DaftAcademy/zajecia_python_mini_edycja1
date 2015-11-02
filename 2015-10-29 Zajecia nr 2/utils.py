# -*- coding: utf-8 -*- 

import os


SUPPORTED_EXTS = ('jpg', 'jpeg', 'png')


class BrightnessCategory(object):
	def __init__(self, name, bmin, bmax):
		if bmin > bmax:
			raise Exception('bmin({}) > bmax({})'.format(bmin, bmax))

		self.name = name
		self.bmin = bmin
		self.bmax = bmax
		self.images = set()

	def add_if_acceptable(self, ultra_image_obj):
		if self.bmin <= ultra_image_obj.brightness <= self.bmax:
			self.images.add(ultra_image_obj)
			return True
		return False


def find_images(folder_to_look_in):
	images_to_be_returned = list()
	for root_path, dirs, files in os.walk(folder_to_look_in):
		for fname in files:
			if fname.lower().rsplit('.', 1)[-1] in SUPPORTED_EXTS:
				images_to_be_returned.append(
					os.path.join(root_path, fname))
	return images_to_be_returned
