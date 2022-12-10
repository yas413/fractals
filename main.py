from PIL import Image, ImageDraw
import tqdm
import matplotlib.pyplot as plt
import random
from drawnow import drawnow

print("""                                                                  
                                                                  
  ______   ______   ______   ______   ______   ______   ______    
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/    
                                                                  
                                                                  
 ._. ___________                     __         .__           ._. 
 | | \\_   _____/___________    _____/  |______  |  |   ______ | | 
 |_|  |    __) \\_  __ \\__  \\ _/ ___\\   __\\__  \\ |  |  /  ___/ |_| 
 |-|  |     \\   |  | \\// __ \\  \\___|  |  / __ \\|  |__\\___ \\  |-| 
 | |  \\___  /   |__|  (____  /\\___  >__| (____  /____/____  > | | 
 |_|      \\/               \\/     \\/          \\/          \\/  |_| 
                                                                  
                                                                  
  ______   ______   ______   ______   ______   ______   ______    
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/    
                                                                  
                                                                  """)


def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (int(s * pt1[0] + t * pt2[0] + u * pt3[0]),
            int(s * pt1[1] + t * pt2[1] + u * pt3[1]))

def midpoint(x,y,a,b):
	return (x+a)//2,(y+b)//2

def xandy(x,y):
	return [(px,py) for px,py in zip(x,y)]

def fractals_plt():
	x = [100,500,900]
	y = [100,900,100]
	px, py = point_on_triangle(*xandy(x,y))
	x.append(px)
	y.append(py)
	N = int(input("Total Number of points:"))
	for i in range(N):
		r = random.randint(0,2)
		px, py = midpoint(px, py, x[r], y[r])
		y.append(py)
		x.append(px)
	plt.scatter(x,y)
	plt.show()

class Fractal:
	def __init__(self):
		self.x = [100,500,900]
		self.y = [100,900,100]
		plt.ion()
		self.figure = plt.figure()
		self.px, self.py = point_on_triangle(*xandy(self.x,self.y))
		self.x.append(self.px)
		self.y.append(self.py)
		self.N = int(input("Total Number of points:"))
		drawnow(self.make_fig)
		self.fractals_fps()

	def make_fig(self):
		plt.scatter(self.x, self.y)

	def fractals_fps(self):
		for i in range(self.N):
			r = random.randint(0,2)
			self.px, self.py = midpoint(self.px, self.py, self.x[r], self.y[r])
			self.x.append(self.px)
			self.y.append(self.py)
			drawnow(self.make_fig)

def fractals_img():
	size = int(input("Width:"))
	x = [(int(size*0.1)),size//2,int(size*0.9)]
	y = [int(size*0.1),int(size*0.9),int(size*0.1)]
	im = Image.new("RGB",(size, size),(0,0,0))
	dr = ImageDraw.Draw(im)
	px, py = point_on_triangle(*xandy(x,y))
	x.append(px)
	y.append(py)
	N = int(input("Total Number of points:"))
	for i in tqdm.tqdm(range(N)):
		r = random.randint(0,2)
		px, py = midpoint(px, py, x[r], y[r])
		y.append(py)
		x.append(px)
	dr.point(xandy(x,y),fill="white")
	im.rotate(180).show()


if __name__ == "__main__":
	fractals_img()
