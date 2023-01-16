# Test Assignment 8.

import test


def test_assignment_8_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 8",
        r"(nested )?activity[ _]?#?\d\.(class|cs|java|js|lua|py|txt)|"
        "package-lock.json|test.csproj")


def test_assignment_8_required_program_plan_files():
    test.check_required_files("Assignment 8", "txt", 1)


def test_assignment_8_required_source_code_files():
    test.check_required_files("Assignment 8", "(cs|java|js|lua|py)", 1)


def test_assignment_8_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 1", 1)


def test_assignment_8_activity_1_source_code_contains():
    test.check_file_contains(
        "Assignment 8",
        "Activity 1",
        "(cs|java|js|lua|py)",
        r"\s+for",
        "Program must use a For loop.")


def test_assignment_8_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 1", 1, 1, 1)


def test_assignment_8_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_references():
    test.check_source_code_references("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "1\n3\n",
        "(value|number).*?\n?.*?(expression|times)",
        "Input label(s) missing or incorrect. "
            "Expecting value and expressions.")


def test_assignment_8_activity_1_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "1\n3\n",
        r"1 \* 1 = 1\n1 \* 2 = 2\n1 \* 3 = 3",
        "output is incorrect. Expected:\n"
            "1 * 1 = 1\n1 * 2 = 2\n1 * 3 = 3")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "3\n5\n",
        r"3 \* 1 = 3\n3 \* 2 = 6\n3 \* 3 = 9\n3 \* 4 = 12\n3 \* 5 = 15",
        "output is incorrect. Expected:\n"
            "3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15")


def test_assignment_8_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 2", 1)


def test_assignment_8_activity_2_source_code_contains():
    test.check_file_contains(
        "Assignment 8",
        "Activity 2",
        "(cs|java|js|lua|py)",
        r"\s+for",
        "Program must use a For loop.")


def test_assignment_8_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 2", 1, 1, 1)


def test_assignment_8_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_references():
    test.check_source_code_references("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "3\n1\n2\n3\n",
        "(grades|scores).*?\n?.*?(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting scores and score.")


def test_assignment_8_activity_2_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "3\n1\n2\n3\n",
        r"2",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "2\n1\n2\n",
        r"1\.5",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "2\n1\n2\n",
        r"1\.5.+?average|average.+?1\.5",
        "average output label is missing or incorrect."
            "Expected average. "
            "Include output label on same line as result.")


def test_assignment_8_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 3", 1)


def test_assignment_8_activity_3_source_code_contains():
    test.check_file_contains(
        "Assignment 8",
        "Activity 3",
        "(cs|java|js|lua|py)",
        r"\s+for",
        "Program must use a For loop.")


def test_assignment_8_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 3", 1, 1, 1)


def test_assignment_8_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_references():
    test.check_source_code_references("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "1\n",
        "number|times|iterations",
        "Input label(s) missing or incorrect. "
            "Expecting number.")


def test_assignment_8_activity_3_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "1\n",
        r"3",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "2\n",
        r"3\.16",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "3\n",
        r"3\.13",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "4\n",
        r"3\.14",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "4\n",
        r"3\.14.+?pi|pi.+?3\.14",
        "(Pi output label is missing or incorrect. "
            "Expected pi. "
            "Include output label on same line as result.")


def test_assignment_8_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 4", 1)


def test_assignment_8_activity_4_source_code_contains():
    test.check_file_contains(
        "Assignment 8",
        "Activity 4",
        "(cs|java|js|lua|py)",
        r"\s+for",
        "Program must use a For loop.")


def test_assignment_8_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 4", 1, 1, 1)


def test_assignment_8_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_references():
    test.check_source_code_references("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 4")


def test_assignment_8_activity_4_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "1\n",
        "number|times|iterations",
        "Input label(s) missing or incorrect. "
            "Expecting number.")


def test_assignment_8_activity_4_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "1\n",
        r"0",
        "output calculation is incorrect."
            "Expecting 0.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "2\n",
        r"0\s+1",
        "output calculation is incorrect."
            "Expecting 0 1")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "3\n",
        r"0\s+1\s+1",
        "output calculation is incorrect."
            "Expecting 0 1 1")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "10\n",
        r"0\s+1\s+1\s+2\s+3\s+5\s+8\s+13\s+21\s+34",
        "output calculation is incorrect."
            "Expecting 0 1 1 2 3 5 8 13 21 34")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 4",
        "",
        "1\n",
        r"Fibonacci sequence",
        "(Output label is missing or incorrect. "
            "Expecting Fibonacci sequence")
