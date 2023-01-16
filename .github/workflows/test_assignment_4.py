# Test Assignment 4.

import test


def test_assignment_4_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 4",
        r"activity[ _]?#?\d\.(class|txt|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_4_duplicate_activities():
    test.check_duplicate_activities("Assignment 3", "Assignment 4")


def test_assignment_4_required_program_plan_files():
    test.check_required_files("Assignment 4", "txt", 1)


def test_assignment_4_activity_1_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_1_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r"pay.+?Input",
        "Program plan introduction missing or incorrect. Expected pay.")


def test_assignment_4_activity_1_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r"Input.*?hours.*?(rate|wage).*?Process",
        "Program plan Input section missing or incorrect. Expected hours and rate")


def test_assignment_4_activity_1_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r"Process.*?weekly.+?(yearly|annual|monthly).+?(monthly|yearly|annual).+?Output",
        "Program plan Process section missing or incorrect. "
            "Expected weekly, monthly, and yearly.")


def test_assignment_4_activity_1_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 1",
        "txt",
        r"Output.*?weekly.+?monthly.+?(yearly|annual)",
        "Program plan Output section missing or incorrect. "
            "Expected weekly, monthly, and yearly.")


def test_assignment_4_activity_2_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_2_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r"age.+?Input",
        "Program plan introduction missing or incorrect. Expected age.")


def test_assignment_4_activity_2_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r"Input.*?years.*?Process",
        "Program plan Input section missing or incorrect. Expected years")


def test_assignment_4_activity_2_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r"Process.*?months.+?days.+?hours.+?seconds.+?Output",
        "Program plan Process section missing or incorrect. "
            "Expected months, days, hours, and seconds.")


def test_assignment_4_activity_2_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 2",
        "txt",
        r"Output.*?months.+?days.+?hours.+?seconds",
        "Program plan Output section missing or incorrect. "
            "Expected months, days, hours, and seconds.")


def test_assignment_4_activity_3_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_3_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r"distance.+?Input",
        "Program plan introduction missing or incorrect. Expected distance.")


def test_assignment_4_activity_3_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r"Input.*?miles.*?Process",
        "Program plan Input section missing or incorrect. Expected miles")


def test_assignment_4_activity_3_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r"Process.*?(yards|kilometers).+?(feet|meters).+?(inches|centimeters).+?Output",
        "Program plan Process section missing or incorrect. "
            "Expected yards, feet, and inches or kilimeters, meters, and centimeters.")


def test_assignment_4_activity_3_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        "txt",
        r"Output.*?(yards|kilometers).+?(feet|meters).+?(inches|centimeters)",
        "Program plan Output section missing or incorrect. "
            "Expected yards, feet, and inches or kilimeters, meters, and centimeters.")


def test_assignment_4_activity_4_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_4_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r"area.+?Input",
        "Program plan introduction missing or incorrect. Expected area.")


def test_assignment_4_activity_4_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r"Input.*?(length|base|radius).*?Process",
        "Program plan Input section missing or incorrect. "
            "Expected length, base, or radius")


def test_assignment_4_activity_4_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r"Process.*?area.+?Output",
        "Program plan Process section missing or incorrect. Expected area.")


def test_assignment_4_activity_4_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r"Output.*?area",
        "Program plan Output section missing or incorrect. Expected area.")


def test_assignment_4_activity_5_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 5",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 5",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_5_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        "txt",
        r"area.+?Input",
        "Program plan introduction missing or incorrect. Expected area.")


def test_assignment_4_activity_5_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 5",
        "txt",
        r"Input.*?length.*?width.+?Process",
        "Program plan Input section missing or incorrect. "
            "Expected length and width")


def test_assignment_4_activity_5_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 5",
        "txt",
        r"Process.*?area.+?Output",
        "Program plan Process section missing or incorrect. Expected area.")


def test_assignment_4_activity_5_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 5",
        "txt",
        r"Output.*?area",
        "Program plan Output section missing or incorrect. Expected area.")


def test_assignment_4_activity_6_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_6_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r"paint.+?Input",
        "Program plan introduction missing or incorrect. Expected paint.")


def test_assignment_4_activity_6_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r"Input.*?length.*?width.+?height.+?(price|cost).+?feet.+?Process",
        "Program plan Input section missing or incorrect. "
            "Expected length, width, height, price, and feet.")


def test_assignment_4_activity_6_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r"Process.*?gallons.+?cost.+?Output",
        "Program plan Process section missing or incorrect. "
            "Expected gallons and cost.")


def test_assignment_4_activity_6_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 6",
        "txt",
        r"Output.*?gallons.+?cost",
        "Program plan Output section missing or incorrect. "
            "Expected gallons and cost.")


def test_assignment_4_activity_7_program_plan_structure():
    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r".+?\nInput.+?Process.+?Output",
        "Program plan structure doesn't match rquirements. "
            "Check for introduction, Input, Process, and Output.")

    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r".+?\n\s*\nInput.*?\n\s+.+?\n\s*\nProcess.*?\n\s+.+?\n\s*\nOutput.*?\n\s+.+",
        "Program plan formatting doesn't match example. "
            "Check blank lines, spacing, and indenting.")


def test_assignment_4_activity_7_program_plan_introduction():
    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r"(dog|age).+?(age|dog).+?Input",
        "Program plan introduction missing or incorrect. Expected dog age.")


def test_assignment_4_activity_7_program_plan_input():
    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r"Input.*?name.*?age.+?Process",
        "Program plan Input section missing or incorrect. "
            "Expected name and age.")


def test_assignment_4_activity_7_program_plan_process():
    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r"Process.*?age.+?Output",
        "Program plan Process section missing or incorrect. "
            "Expected age.")


def test_assignment_4_activity_7_program_plan_output():
    test.check_file_contains(
        "Assignment 4",
        "Activity 7",
        "txt",
        r"Output.*?name.+?age",
        "Program plan Output section missing or incorrect. "
            "Expected name and age.")


def test_assignment_4_required_source_code_files():
    test.check_required_files("Assignment 4", "(cs|java|js|lua|py)", 1)


def test_assignment_4_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 1", 1)


def test_assignment_4_activity_1_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 1", 2)


def test_assignment_4_activity_1_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 1", 5)


def test_assignment_4_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "hours.*?\n?.*?(rate|per hour|hourly|wage)",
        "Input label(s) missing or incorrect. "
            "Expecting hours and rate.")


def test_assignment_4_activity_1_weekly_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "150",
        "weekly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "162.75",
        "weekly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"week.+?150|150.+?week",
        "weekly output label is missing or incorrect.")


def test_assignment_4_activity_1_monthly_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "600|650",
        "monthly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "651|705.25",
        "monthly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"month.+?6|6.+?month",
        "monthly output label is missing or incorrect.")


def test_assignment_4_activity_1_yearly_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "7800",
        "yearly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "8463",
        "yearly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"year.+?7800|7800.+?year|annual.+?7800|7800.+?annual",
        "yearly output label is missing or incorrect.")


def test_assignment_4_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 2", 1)


def test_assignment_4_activity_2_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 2", 1)


def test_assignment_4_activity_2_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 2", 5)


def test_assignment_4_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "age|years",
        "Input label(s) missing or incorrect. Expecting years.")


def test_assignment_4_activity_2_months_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "12",
        "months calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "month.+?12|12.+?month",
        "months output label is missing or incorrect.")


def test_assignment_4_activity_2_days_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "365",
        "days calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "day.+?365|365.+?day",
        "days output label is missing or incorrect.")


def test_assignment_4_activity_2_hours_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "8760",
        "hours calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "hour.+?8760|8760.+?hour",
        "hours output label is missing or incorrect.")


def test_assignment_4_activity_2_seconds_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "31536000|3.1536E7",
        "seconds calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "seconds.+?31536000|31536000.+?seconds|"
            "seconds.+?3.1536E7|3.1536E7.+?seconds",
        "seconds output label is missing or incorrect.")


def test_assignment_4_activity_2_minutes_output():
    test.check_file_does_not_contain(
        "Assignment 4",
        "Activity 2",
        r"(cs|java|js|lua|py)",
        "minute",
        "processing error. Processing should not include minutes.")


def test_assignment_4_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 3", 1)


def test_assignment_4_activity_3_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 3", 1)


def test_assignment_4_activity_3_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 3", 4)


def test_assignment_4_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_file_contains():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        r"(cs|java|js|lua|py)",
        "feet|meter",
        "must include output labels with either feet or meters.")


def test_assignment_4_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "",
        "1\n",
        "mile",
        "input label(s) missing or incorrect. Expecting miles.")


def test_assignment_4_activity_3_yards_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        "1760",
        "yards calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"yard.+?1760|1760.+?yard",
        "yards output label is missing or incorrect.")


def test_assignment_4_activity_3_feet_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        "5280",
        "feet calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"feet.+?5280|5280.+?feet",
        "feet output label is missing or incorrect.")


def test_assignment_4_activity_3_inches_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"63360",
        "inches calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"inches.+?63360|63360.+?inches",
        "inches output label is missing or incorrect.")


def test_assignment_4_activity_3_kilometers_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        "1.6",
        "kilometers calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"kilometer.+?1\.6|1\.6.+?kilometer",
        "kilometers output label is missing or incorrect.")


def test_assignment_4_activity_3_meters_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{2}",
        "meters calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"meter.+?16\d{2}|16\d{2}.+?meter",
        "mneters output label is missing or incorrect.")


def test_assignment_4_activity_3_centimeters_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{4}",
        "centimeters calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"centimeter.+?16\d{4}|16\d{4}.+?centimeter",
        "centimeters output label is missing or incorrect.")


def test_assignment_4_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 4", 1)


def test_assignment_4_activity_4_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 4", 2)


def test_assignment_4_activity_4_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 4", 4)


def test_assignment_4_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_file_contains():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        r"(cs|java|js|lua|py)",
        "triangle|rectangle|trapezoid|ellipse|"
            "square|parallelogram|circle|sector",
        "must indicate shape type.")


def test_assignment_4_activity_4_triangle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_4_activity_4_triangle_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "triangle area calculation output is incorrect. "
            "Expected 0.5")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "triangle.+?area.+?0.5|area.+?triangle.+?0.5|"
            "0.5.+?triangle.+?0.5.+?area|area.+?triangle",
        "triangle output label is missing or incorrect.")


def test_assignment_4_activity_4_rectangle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"width.*?\n?.*?height|length.*?\n?.*?width",
        "input label(s) missing or incorrect. "
            "Expecting width and height.")


def test_assignment_4_activity_4_rectangle_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "rectangle area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "rectangle.+?area.+?1|area.+?rectangle.+?1|"
            "1.+?rectangle.+?1.+?area|area.+?rectangle",
        "rectangle output label is missing or incorrect.")


def test_assignment_4_activity_4_trapezoid_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "trapezoid area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "trapezoid.+?area.+?1|area.+?trapezoid.+?1|"
            "1.+?trapezoid.+?1.+?area|area.+?trapezoid",
        "trapezoid output label is missing or incorrect.")


def test_assignment_4_activity_4_ellipse_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "ellipse area calculation output is incorrect. "
            "Expected 3.14")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "ellipse.+?area.+?3.14|area.+?ellipse.+?3.14|"
            "3.14.+?ellipse.+?3.14.+?area|area.+?ellipse",
        "ellipse output label is missing or incorrect.")


def test_assignment_4_activity_4_square_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "side|base|height|length|width",
        "input label(s) missing or incorrect. "
            "Expecting side.")


def test_assignment_4_activity_4_square_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "square area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "square.+?area.+?1|area.+?square.+?1|"
            "1.+?square.+?1.+?area|area.+?square",
        "square output label is missing or incorrect.")


def test_assignment_4_activity_4_parallelogram_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_4_activity_4_parallelogram_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "parallelogram area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "parallelogram.+?area.+?1|area.+?parallelogram.+?1|"
            "1.+?parallelogram.+?1.+?area|area.+?parallelogram",
        "parallelogram output label is missing or incorrect.")


def test_assignment_4_activity_4_circle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_4_activity_4_circle_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "circle area calculation output is incorrect. "
            "Expected 3.14")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "circle.+?area.+?3.14|area.+?circle.+?3.14|"
            "3.14.+?circle.+?3.14.+?area|area.+?circle",
        "circle output label is missing or incorrect.")


def test_assignment_4_activity_4_sector_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_4_activity_4_sector_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "sector area calculation output is incorrect. "
            "Expected 0.5")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "sector.+?area.+?0.5|area.+?sector.+?0.5|"
            "0.5.+?sector.+?0.5.+?area|area.+?sector",
        "sector output label is missing or incorrect.")


def test_assignment_4_activity_5_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 5", 1)


def test_assignment_4_activity_5_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 5", 2)


def test_assignment_4_activity_5_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 5", 3)


def test_assignment_4_activity_5_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10\n10\n",
        "length.*?\n?.*?width|long.*?\n?.*?wide",
        "input label(s) missing or incorrect. "
            "Expecting length and width.")


def test_assignment_4_activity_5_area_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "12\n10\n",
        r"13\.33",
        "area calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "12.5\n10.5\n",
        "14.58",
        "area calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10\n10\n",
        r"(area|yards).+?11\.11|11\.11.+?(yards|area)",
        "area output label is missing or incorrect. "
            "Expecting yards. "
            "Include output label on same line as result.")


def test_assignment_4_activity_6_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 6", 1)


def test_assignment_4_activity_6_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 6", 5)


def test_assignment_4_activity_6_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 6", 8)


def test_assignment_4_activity_6_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_gallons_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "2",
        "gallons calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "gallon.+?2|2.+?gallon",
        "gallons output label is missing or incorrect.")


def test_assignment_4_activity_6_cost_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "60",
        "cost calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        r"(cost|price).+?60|60.+?(price|cost)",
        "cost output label is missing or incorrect.")


def test_assignment_4_activity_7_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 7", 1)


def test_assignment_4_activity_7_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 7", 2)


def test_assignment_4_activity_7_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 7", 3)


def test_assignment_4_activity_7_source_code_formatting():
    test.check_source_code_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_references():
    test.check_source_code_references("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "name.*?\n?.*?(age|years|old)",
        "input label(s) missing or incorrect. "
            "Expecting name and age.")


def test_assignment_4_activity_7_age_output():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "14",
        "age calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "Rover.+?14|14.+?Rover",
        "name label output is missing or incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "year.+?14|14.+?year",
        "age output label is missing or incorrect. "
            "Expected years.")
