# Test Assignment 2.

import test


def test_assignment_2_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 2",
        r"activity[ _]?#?1\.(class|fprg|txt|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_2_required_program_plan_files():
    test.check_required_files("Assignment 2", "txt", 1)


def test_assignment_2_required_flowgorithm_files():
    test.check_required_files("Assignment 2", "fprg", 1)


def test_assignment_2_required_source_code_files():
    test.check_required_files("Assignment 2", "(cs|java|js|lua|py)", 1)


def test_assignment_2_activity_1_program_plan_introduction():
    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r".+?\nInput",
        "Program plan introduction missing or incorrect.")


def test_assignment_2_activity_1_program_plan_input():
    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\nInput.*?\n\s+None.*?\n",
        "Program plan Input section missing or incorrect.")

    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\n\nInput.*?\n\s+None.*?\n",
        "Program plan Input section spacing is incorrect.")


def test_assignment_2_activity_1_program_plan_process():
    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\nProcess.*?\n\s+None.*?\n",
        "Program plan Process section missing or incorrect.")

    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\n\nProcess.*?\n\s+None.*?\n",
        "Program plan Process section spacing is incorrect.")


def test_assignment_2_activity_1_program_plan_output():
    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\nOutput.*?\n\s+Hello .*?",
        "Program plan Output section missing or incorrect.")

    test.check_file_contains(
        "Assignment 2",
        "Activity 1",
        "txt",
        r"\n\nOutput.*?\n\s+Hello .*?",
        "Program plan Output section spacing is incorrect.")


def test_assignment_2_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 2", "Activity 1", 1, "fprg")


def test_assignment_2_activity_1_flowgorithm_output():
    test.check_flowgorithm_output("Assignment 2", "Activity 1", 1)


def test_assignment_2_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 2", "Activity 1")


def test_assignment_2_activity_1_flowgorithm_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 2",
        "Activity 1",
        "fprg",
        "world",
        "Requirements are to change \"world\" to your name.")


def test_assignment_2_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 2", "Activity 1", 1)


def test_assignment_2_activity_1_source_code_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 2",
        "Activity 1",
        "(cs|java|js|lua|py)",
        "world",
        "Requirements are to change \"world\" to your name.")


def test_assignment_2_activity_1_source_code_output():
    test.check_source_code_output(
        "Assignment 2",
        "Activity 1",
        "",
        "\n",
        "hello.+?$",
        "Output does not match requirements.")


def test_assignment_2_git_log():
    test.check_git_log(
        "Assignment 2",
        "hello.+?world",
        "Git log is missing required \"Hello world!\" text. "
            "You must commit Activity 1 changes before working on "
            "Activity 2.")
