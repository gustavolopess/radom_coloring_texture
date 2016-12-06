# -*- coding: utf-8 -*-
import numpy as np

class Scene(object):
	"""docstring for Scene"""
	def __init__(self):
		super(Scene, self).__init__()
		self.points = []
		self.triangles = []
		self.random_factor = 0.0
		self.ka = 0.0
		self.kd = 0.0
		self.ks = 0.0
		self.n_factor = 0.0
		self.od = []
		self.ia = 0.0
		self.il = 0.0
		self.pl = 0.0

	def load_illumination_points_triangles_color(self):
	    with open("input/calice.txt") as calice_config:
	        lines = calice_config.readlines()

	    number_points = int(lines[0].split(" ")[0])
	    triangles = int(lines[0].split(" ")[1])

	    for x in range(1, number_points+1):
	        self.points.append( np.array(lines[x].splitlines()[0].split(" ")) )

	    for x in range(number_points+2, len(lines)):
	    	self.triangles.append( np.array(lines[x].splitlines()[0].split(" ")) )

		with open("input/aleatorizacao.txt", 'r') as random:
			self.random_factor = float(random.readline())

		with open("input/iluminacao.txt", 'r') as illumination:
			pass
