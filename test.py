import unittest

from Compiler import Compiler
from Tree.AbstractSyntaxTree import AbstractSyntaxTree


class TestFirstLoop(unittest.TestCase):
    instance = AbstractSyntaxTree
    compiler = Compiler()
    compiler.image_output = True

    def setUp(self):
        self.instance.node_count = 0

    def test_array(self):
        self.compiler.analysis("./C_code/array.c")
        with open('./TreePlots/array_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/array_output.dot') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_assignments(self):
        self.compiler.analysis("./C_code/assignments.c")
        with open('./TreePlots/assignments_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/assignments_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_conditions(self):
        self.compiler.analysis("./C_code/conditions.c")
        with open('./TreePlots/conditions_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/conditions_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_function_calls(self):
        self.compiler.analysis("./C_code/function_calls.c")
        with open('./TreePlots/function_calls_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/function_calls_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_generic(self):
        self.compiler.analysis("./C_code/generic.c")
        with open('./TreePlots/generic_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/generic_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_operations(self):
        self.compiler.analysis("./C_code/operations.c")
        with open('./TreePlots/operations_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/operations_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_structs(self):
        self.compiler.analysis("./C_code/structs.c")
        with open('./TreePlots/structs_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/structs_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_switch(self):
        self.compiler.analysis("./C_code/switch.c")
        with open('./TreePlots/switch_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/switch_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)


class TestCleanerLoop(unittest.TestCase):
    instance = AbstractSyntaxTree
    compiler = Compiler()
    compiler.image_output = True

    def setUp(self):
        self.instance.node_count = 0

    def test_int_declaration(self):
        self.compiler.analysis("./C_code/declarations_int.c")
        with open('./TreePlots/declarations_int_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_int_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)
        with open('./TreePlots/declarations_int_cleaned_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_int_cleaned_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_float_declaration(self):
        self.compiler.analysis("./C_code/declarations_float.c")
        with open('./TreePlots/declarations_float_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_float_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)
        with open('./TreePlots/declarations_float_cleaned_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_float_cleaned_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_char_declaration(self):
        self.compiler.analysis("./C_code/declarations_char.c")
        with open('./TreePlots/declarations_char_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_char_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)
        with open('./TreePlots/declarations_char_cleaned_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_char_cleaned_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_array_declaration(self):
        self.compiler.analysis("./C_code/declarations_array.c")
        with open('./TreePlots/declarations_array_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_array_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)
        with open('./TreePlots/declarations_array_cleaned_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/declarations_array_cleaned_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)

    def test_int_assignment(self):
        self.compiler.analysis("./C_code/assignments_int.c")
        with open('./TreePlots/assignments_int_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/assignments_int_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)
        with open('./TreePlots/assignments_int_cleaned_output.dot', 'r') as myFile:
            actual_output = myFile.read()
        with open('ExpectedTestOutput/assignments_int_cleaned_output.dot', 'r') as myFile:
            expected_output = myFile.read()
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
