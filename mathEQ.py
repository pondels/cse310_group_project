

class Math():

    def slope(self, x1, y1, x2, y2):
        try:
            slope = (y1 - y2) / (x1 - x2)
            return slope
        except:return 1