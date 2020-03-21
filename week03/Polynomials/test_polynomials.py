import unittest
from polynomials import Term, Polynomial

class TestTerm(unittest.TestCase):

	def test_representing_the_term_as_string(self):
		t = Term(2,3)

		self.assertEqual(str(t), '2*x^3')

	def test_derivative_of_term_with_coeficient_and_power_return_after_derivation(self):
		t = Term(2,4)

		res = t.derivative()

		self.assertEqual(res, '8*x^3')

	def test_derivative_of_term_with_coeficient_and_power_return_term_with_pow_equal_to_one(self):
		t = Term(2,2)

		res = t.derivative()

		self.assertEqual(res, '4*x')

	def test_derivative_of_term_with_coeficient_and_power_equal_to_one(self):
		t = Term(3,1)

		res = t.derivative()

		self.assertEqual(res, '3')

	def test_derivative_of_term_with_coeficientequal_to_one(self):
		t = Term(1,3)

		res = t.derivative()

		self.assertEqual(res, '3*x^2')

	def test_derivative_of_term_with_coeficient_and_power_return_term_with_coeficient_equal_to_one(self):
			t = Term(1,1)

			res = t.derivative()

			self.assertEqual(res, '1')

	def test_derivative_of_term_with_coeficient_and_power_equal_to_zero(self):
			t = Term(5,0)

			res = t.derivative()

			self.assertEqual(res, '0')

	def test_convert_string_into_term_with_only_one_constant(self):
		s = '3'

		res = Term.convert_into_term(s)

		self.assertEqual(res, ('3','0'))

	def test_convert_string_into_term_with_constant_and_variable_with_power_equal_to_one(self):
		s = '3*x'

		res = Term.convert_into_term(s)

		self.assertEqual(res, ('3','1'))

	def test_convert_string_into_term_with_constant_and_variable_with_power(self):
		s = '3*x^4'

		res = Term.convert_into_term(s)

		self.assertEqual(res, ('3','4'))

class TestPolynomial(unittest.TestCase):

	def test_adding_terms_in_polynomial_return_derivative(self):
		term1 = Term(2,3)
		term2 = Term(3,1)
		term3 = Term(1,0)


		term_1 = Term(1,4)
		term_2 = Term(10,3)

		poly1 = Polynomial([term1, term2, term3])
		poly2 = Polynomial([term_1, term_2])

		res1 = poly1.derivative()
		res2 = poly2.derivative()

		self.assertEqual(res1, '6*x^2+3')
		self.assertEqual(res2, '4*x^3+30*x^2')

	def test_adding_terms_reversed_in_polynomial_return_derivative(self):
		term1 = Term(2,0)
		term2 = Term(3,1)
		term3 = Term(4,2)

		poly = Polynomial([term1, term2, term3])

		res = poly.derivative()
		self.assertEqual(res, '3+8*x')

	def test_adding_one_term_which_is_constant_in_polynomial_return_derivative_zero(self):
		term1 = Term(2,0)

		poly = Polynomial([term1])

		res = poly.derivative()
		self.assertEqual(res, '0')

	def test_adding_one_term_which_is_coefficient_and_variable_in_polynomial_return_derivative_constant(self):
		term1 = Term(2,1)

		poly = Polynomial([term1])

		res = poly.derivative()
		self.assertEqual(res, '2')


if __name__ == '__main__':
	unittest.main()