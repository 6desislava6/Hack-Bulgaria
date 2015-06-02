
closing = [']', '}', ')']
openning = ['[', '{', '(']


class BracketsEvaluator:

    MULT = 2

    def __init__(self, string):
        self.string = string

    def evaluate_brackets(self):
        if self.verify_brackets() is False:
            return 'NO'
        nested_numbers = self.get_nested_numbers_brackets()[0]
        return self.evaluate_nested_numbers(nested_numbers, first=True)

    @staticmethod
    def findlastlist(s):
        while s and isinstance(s[-1], list):
            s = s[-1]
        return s

    @staticmethod
    def find_before_lastlist(s):
        before_last = s
        while s and isinstance(s[-1], list):
            before_last = s
            s = s[-1]
        return before_last

    def verify_brackets(self):
        brackets_stack = []
        if self.string[0] not in openning:
            return False

        for symbol in self.string:
            if symbol in openning:
                if symbol == '(':
                    if len(brackets_stack) != 0 and brackets_stack[-1] != '[':
                        return False
                elif symbol == '[':
                    if len(brackets_stack) != 0 and brackets_stack[-1] != '{':
                        return False
                else:
                    if len(brackets_stack) != 0:
                        return False
                brackets_stack.append(symbol)
            if symbol in closing:
                if closing.index(symbol) != openning.index(brackets_stack[-1]):
                    return False
                else:
                    brackets_stack.pop()
        return len(brackets_stack) == 0

    # Other methods:
    # Regular expressions, matching:
    # smallest:
    # (\(\d*\))
    # middlest:
    # \[((\(\d*\))*\d*)*\]
    # biggest:
    # \{(\d*(\[((\(\d*\))*\d*)*\])*)*\}

    def get_nested_numbers_brackets(self):
        numbers_stack = []
        current_num_len = 0
        current_num_digits = []

        for symbol in self.string:
            if symbol in openning:
                # Making last number
                current_num = 0
                for i in range(current_num_len):
                    current_num += int(current_num_digits.pop()) * (10 ** i)
                current_num_len = 0

                # Adding number if not zero
                if current_num != 0:
                    self.findlastlist(numbers_stack).append(current_num)

                # Making the new 'nest' for nested brackets
                self.findlastlist(numbers_stack).append([])

            elif symbol in closing:
                # Making last number
                current_num = 0
                for i in range(current_num_len):
                    current_num += int(current_num_digits.pop()) * (10 ** i)
                current_num_len = 0

                # Appending lastly read number
                if current_num != 0:
                    self.findlastlist(numbers_stack).append(current_num)

                # Continuing writing in the before last nested bracket
                self.find_before_lastlist(numbers_stack).append(0)

            else:
                # Making numbers
                current_num_digits.append(symbol)
                current_num_len += 1

        return numbers_stack

    @classmethod
    def evaluate_nested_numbers(cls, numbers, first=False):
        # The first, initial brackets must not be multiplied by 2!
        # That is why I added keyword
        result = 0
        for element in numbers:
            if isinstance(element, list):
                result += cls.evaluate_nested_numbers(element)
            else:
                result += element
        if first:
            return result
        return cls.MULT * result


def main():
    input_string = input('Write expression here> ')
    evaluator = BracketsEvaluator(input_string)
    print(evaluator.evaluate_brackets())

if __name__ == '__main__':
    main()
