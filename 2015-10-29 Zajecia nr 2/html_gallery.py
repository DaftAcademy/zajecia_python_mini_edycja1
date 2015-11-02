# -*- coding: utf-8 -*- 

ROOT_DOC_HTML = u'''<html>
	<head>
		<title>Brightness Gallery</title>
	</head>
	<body>
		<h1>My Brightness Gallery</h1>
		<div id="sections">
			{0}
		</div>
	</body>
</html>
'''

CAT_HTML = u'''<div class="section">
	<h2>{0}</h2>
	<div>
		{1}
	</div>
</div>
'''

IMG_HTML = u'<img src="{}" alt="{}" width="150" />'

def generate_gal_html(categories):
	doc_str = ROOT_DOC_HTML
	cat_html_l = list()
	for cat in categories:
		images_l = list()
		for img in cat.images:
			images_l.append(IMG_HTML.format(
				img.image_path, img.brightness))
		cat_html_l.append(
			CAT_HTML.format(cat.name, u'\n'.join(images_l)))

	return doc_str.format(u''.join(cat_html_l))

