import sys

class Term:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def __str__(self):
        return f'{self.coefficient}*x^{self.power}'

    def __repr__(self):
        return f'{self.coefficient}*x^{self.power}'

    def __eq__(self, other):
        return str(self) == str(other)

    def derivative(self):
        if self.power == 0:
            return "0"
        else:
            new_coef = self.coefficient * self.power
            new_power = self.power - 1

            if new_power == 0:
                return str(new_coef)

            elif new_power == 1:
                return f'{new_coef}*x'

            elif new_coef == 1:
                return f'x^{new_power}'

            else:
                return f'{new_coef}*x^{new_power}'

    @staticmethod
    def convert_into_term(term_as_string):
        if term_as_string.find('x') == -1:
            return (term_as_string, '0')

        else:
            if term_as_string[0] == 'x':
                if len(term_as_string) == 1:
                    return ('1','1')
                else:
                    term_as_string = term_as_string.split("x^")
                    return ('1', term_as_string[1])
            else:
                if term_as_string.find('^') == -1:
                    return (term_as_string[0], '1')
                else:
                    term_as_string = term_as_string.split("*x^")
                    return (term_as_string[0], term_as_string[1])

class Polynomial:
    def __init__(self, terms):
        self.terms = terms

    def derivative(self):
        each_derivative = ""
        list_with_derivatives = []
        count_zero_derivatives = 0

        #list with every derivative
        for i in range(len(self.terms)):
    
            if self.terms[i].derivative() != '0':
                each_derivative = "".join(self.terms[i].derivative())
                list_with_derivatives.append(each_derivative)
            else:
                count_zero_derivatives += 1

        #case all derivatives are zero
        if count_zero_derivatives == len(self.terms):
            return "0"

        #string with all derivatives
        res = ""
        for i in range(len(list_with_derivatives) - 1):
            res += list_with_derivatives[i] + '+'

        if len(list_with_derivatives) > 1:
            return res + list_with_derivatives[len(list_with_derivatives) - 1]
        else:
            return each_derivative

    @classmethod
    def print_derivative(cls):
        polynomial = sys.argv[1].split('+')
        lst = []
        for term in polynomial:
            t = Term.convert_into_term(term)

            lst.append(Term(int(t[0]),int(t[1])))

        poly = cls(lst)
        res = poly.derivative()

        return res

if __name__ == '__main__':
    main()