#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from utils import (
	BrightnessCategory,
	find_images,
)
from ultra_image import UltraImage
from html_gallery import generate_gal_html


# Podmienic na cos co istnieje
PICTURE_FOLDER = '/home/user/example_images'

categories = [
	BrightnessCategory('bright', 130, 255),
	BrightnessCategory('medium', 90, 129),
	BrightnessCategory('dark', 0, 89),
]


if __name__ == '__main__':
	for image_path in find_images(PICTURE_FOLDER):
		uim = UltraImage(image_path)
		for cat in categories:
			cat.add_if_acceptable(uim)

print generate_gal_html(categories)
