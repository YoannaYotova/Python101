class BowlingGame:
	def __init__(self, frames):
		self.frames = BowlingGame.validate(frames)

	@staticmethod
	def validate(frames):
		if len(frames) == 0 :
			raise ValueError('Invalid number of frames')

		else:
			count_frames = 0
			for i in frames:
				if i == 10:
					count_frames += 2
				else:
					count_frames += 1

			if count_frames != 20:
				if frames[len(frames) - 3] != 10 and frames[len(frames) - 3] + frames[len(frames) - 2] != 10: 
					raise ValueError('Invalid number of frames')
	
			return frames


	def result(self):
		res = 0
		tenth_frame_strike = False
		tenth_frame_spare = False

		for i in range(len(self.frames)):
			if self._is_strike(i):
				if i == len(self.frames) - 3:
					tenth_frame_strike = True
				res += (10 + self.frames[i + 1] + self.frames[i + 2])
				
			elif self._is_spare(i):
				if i == len(self.frames) - 2:
					tenth_frame_spare = True
				res += self.frames[i] + self.frames[i + 1]
			else:
				if tenth_frame_strike == False and tenth_frame_spare == False:
					res += self.frames[i]

			if res == 300:
				return res

		return res

	def _is_strike(self, index):
		return self.frames[index] == 10

	def _is_spare(self, index):
		if index % 2 == 1:
			return self.frames[index] + self.frames[index - 1] == 10
		else:
			return False



if __name__ == '__main__':
	main()