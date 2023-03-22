class Plants:
	def need_oxygen(self):
    	print('Need oxygen.')
class Flowers(Plants):
	def need_water(self):
    	print('Need water everyday.')
    def need_sunlight(self):
    	print('Meed sunglight.')
    def living (self):
    	self.need_water()
        self.need_sunlight()

olivia = Flowers()
olivia.living()
