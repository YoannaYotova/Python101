import unittest
from reduce_file_path import removing_double_slash, removing_last_slash, removing_double_dots, removing_directory_point

class TestReduceDoubleSlash(unittest.TestCase):
	def test_raises_error_if_the_path_is_empty(self):
		path = ""
		exc = None

		try:
			removing_double_slash(path)
		except Exception as err:
			exc = err


		self.assertIsNotNone(str(exc))
		self.assertEqual(str(exc), 'Invalid path')

	def test_with_one_slash(self):
		path = "/"

		res = removing_double_slash (path)
		self.assertEqual(res, "/")

	def  test_with_more_slashes(self):
		path = "//python101/week02///"

		res = removing_double_slash(path)

		self.assertEqual(res,"/python101/week02/")

class TestRemovingLastSlash(unittest.TestCase):
	def test_with_no_slash_at_the_end(self):
		path = "python101/week02"

		res = removing_last_slash(path)

		self.assertEqual(res, path)

	def test_with_slash_at_the_end(self):
		path = "pyhton101/week02/"

		res = removing_last_slash(path)

		self.assertEqual(res, "pyhton101/week02")

class TestRemovingDoubleDots(unittest.TestCase):
	def test_with_one_double_dots_at_the_begining(self):
		path = "/../"

		res = removing_double_dots(path)

		self.assertEqual(res, "/")
	def test_with_more_double_dots(self):
		path ="/python/../week02/etc/../passwd/"

		res = removing_double_dots(path)

		self.assertEqual(res, "/week02/passwd")

class TestRemovingDirectoryPath(unittest.TestCase):
	def test_with_more_directory_points(self):
		path = "/srv/./././././"
		res = removing_directory_point(path)

		self.assertEqual(res, "/srv")


if __name__ == '__main__':
	unittest.main()