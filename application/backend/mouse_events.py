class BasicMouseEvent():

    def __init__(self, aoi=None, x=-1, y=-1, is_press=False, timestamp=-1):
		self.aoi = aoi
        self.x  = x
        self.y = y
        self.is_press = is_press
        self.time_stamp = timestamp

class DragDropMouseEvent():

    def __init__(self, time_stamp, duration, displacement, drag_start, aoi=None):
        self.drag_start = drag_start
		self.aoi = aoi
        self.duration = duration
        self.time_stamp = timestamp
        self.displacement = displacement
