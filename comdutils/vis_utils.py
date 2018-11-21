import cv2
import numpy as np 
import random


def give_frame(image, company_name, project_name):
	h, w, _ = image.shape
	space = int(0.1 * h/2)
	cv2.rectangle(image, (0, 0), (int(0.5 * w), int(0.1 * h)), (255, 255, 255), -1)
	## put project name
	cv2.putText(image, project_name, (5, int( 5 + space/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2, cv2.LINE_AA)
	## put company name
	cv2.putText(image, company_name, (5, int( 5 + space + space/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2, cv2.LINE_AA)
	return image


def draw_rectangles(rects, image, COLORS):
	## draw rectangle
	for i in rects:
		idx = random.randint(0,len(COLORS)-1)
		cv2.rectangle(image, (i[0], i[1]), (i[2], i[3]), COLORS[idx], 2)
	return image


def put_topoverlays(rects, image, alpha=0.3):
	h, w, _ = image.shape
	im = np.ones(shape=image.shape).astype(np.uint8)
	overlay_bboxs = []
	for i in rects:
		x1 = int(i[0])
		x2 = int(min(i[0] + 1.7 * (i[2] - i[0]), w))
		y1 = int(i[1])
		y2 = int(max(i[1] - 0.2 * (i[3] - i[1]), 0))
		overlay_bboxs.append([x1, y1, x2, y2])
		cv2.rectangle(im, (x1, y1), (x2, y2), (100, 100, 0), -1)
		cv2.rectangle(im, (x1, y1), (x2, y2), (0, 100, 255), 2)
	image = cv2.addWeighted(im, alpha, image, 1 - alpha, 0, image)
	return image, overlay_bboxs


def put_vertical_textsoverrect(rects, image, text_list):
	for idx, i in enumerate(rects):
		h = i[3] - i[1]
		space = int(h/len(text_list[0]))

		for idx2, j in enumerate(text_list[idx]):
			cv2.putText(image, j, ((i[0] + 5), int(i[1] + space * idx2 + space/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
	return image