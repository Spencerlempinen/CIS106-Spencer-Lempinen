# Test Final Project.

import os
import re
import test
import urllib.request

# FILENAME = FILENAME
FILENAME = "plant_catalog.xml"

def setup_module(module):
    url = "https://www.w3schools.com/xml/" + FILENAME
    text = urllib.request.urlopen(url).read().decode()
    with open(FILENAME, "w") as file:
        file.write(text)


def teardown_module(module):
    files = [
        FILENAME,
        "cd_catalog.xml"
        "plant_catalog.xml",
        "simple.xml"
    ]

    for file in files:
        if os.path.exists(file):
            os.remove(file)


def test_final_project_folder_structure():
    test.check_assignment_folder_structure(
        "Final Project",
        r"final[ _]project\.(class|cs|java|js|lua|py|txt)|"
        "package-lock.json|test.csproj")


def test_final_project_required_program_plan_files():
    test.check_required_files("Final Project", "txt", 1)


def test_final_project_required_source_code_files():
    test.check_required_files("Final Project", "(cs|java|js|lua|py)", 1)


def test_final_project_source_code_comments():
    test.check_source_code_comments("Final Project", "Final Project", 1)


# def test_final_project_source_code_functions():
#     test.check_source_code_functions("Final Project", "Final Project", 0, 1, 1)


def test_final_project_source_code_formatting():
    test.check_source_code_formatting("Final Project", "Final Project")


def test_final_project_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Final Project", "Final Project")


def test_final_project_activity_1_source_code_references():
    test.check_source_code_references("Final Project", "Final Project")


def test_final_project_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Final Project", "Final Project")


def test_final_project_source_code_identifier_length():
    test.check_source_code_identifier_length("Final Project", "Final Project")


def test_final_project_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Final Project", "Final Project")


def test_final_project_output():
    url = "https://www.w3schools.com/xml/" + FILENAME
    text = urllib.request.urlopen(url).read().decode()
    with open(FILENAME, "w") as file:
        file.write(text)

    if FILENAME == "cd_catalog.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Empire Burlesque\s+-?\s+Bob Dylan\s+-?\s+USA\s+-?\s+\$?10.90\s+-?\s+1985",
            "Expected first line to match:\n"
                "Empire Burlesque - Bob Dylan - USA - 10.90 - 1985"
        )

        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Unchain my heart\s+-?\s+Joe Cocker\s+-?\s+USA\s+-?\s+\$?8.20\s+-?\s+1987",
            "Expected last line to match:\n"
                "Unchain my heart - Joe Cocker - USA - 8.20 - 1987"
        )

    elif FILENAME == "simple.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Belgian Waffles\s+-?\s+Two of our famous.+?maple syrup\s+-?\s+650\s+-?\s+\$?5\.95",
            "Expected first line to match:\n"
                "Belgian Waffles - Two of our famous ... maple syrup - 650 - 5.95"
        )

        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Homestyle Breakfast\s+-?\s+Two eggs,.+?hash browns\s+-?\s+950\s+-?\s+\$?6\.95",
            "Expected last line to match:\n"
                "Homestyle Breakfast - Two eggs, ... hash browns - 950 - 6.95"
        )

        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"5.+?800.+?6\.86",
            "Expected total line to contain:\n"
                "5 items - 800 average calories - $6.86 average price"
        )

    elif FILENAME == "plant_catalog.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Bloodroot\s+\(Sanguinaria canadensis\)\s+-?\s+4\s+-?\s+Mostly Shady\s+-?\s+\$?2.44",
            "Expected first line to match:\n"
                "Bloodroot (Sanguinaria canadensis) - 4 - Mostly Shady - $2.44"
        )

        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"Cardinal Flower\s+\(Lobelia cardinalis\)\s+-?\s+2\s+-?\s+Shade\s+-?\s+\$?3.02",
            "Expected last line to match:\n"
                "Cardinal Flower (Lobelia cardinalis) - 2 - Shade - $3.02"
        )

        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "",
            r"36.+?6\.37",
            "Expected total line to contain:\n"
                "36 items - $6.37 average price"
        )

    else:
        assert False, "Unexpected filename: " + FILENAME

    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_two_records():
    url = "https://www.w3schools.com/xml/" + FILENAME
    text = urllib.request.urlopen(url).read().decode()

    if FILENAME == "simple.xml":
        text = re.sub("<name>Belgian.+?<name>French", 
            "<name>French", text, flags=re.DOTALL)
    elif FILENAME == "plant_catalog.xml":
        text = re.sub("<COMMON>Bloodroot.+?<COMMON>Snakeroot",
            "<COMMON>Snakeroot", text, flags=re.DOTALL)
    elif FILENAME == "cd_catalog.xml":
        text = re.sub("<TITLE>Hide your heart.+?<TITLE>Unchain my heart",
            "<TITLE>Unchain my heart", text, flags=re.DOTALL)
    else:
        assert False, "Unexpected filename: " + FILENAME

    with open(FILENAME, "w") as file:
        file.write(text)


    if FILENAME == "simple.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "two records",
            r"2.+?775.+?(5\.72|5\.73)",
            "Expected total line to contain:\n"
                "2 items - 775 average calories - $5.73 average price"
        )

    elif FILENAME == "plant_catalog.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "two records",
            r"2.+?(4\.32|4\.33)",
            "Expected total line to contain:\n"
                "2 items - $4.33 average price"
        )

    elif FILENAME == "cd_catalog.xml":
        test.check_source_code_output(
            "Final Project",
            "Final Project",
            "",
            "two records",
            r"2.+?(9\.55)",
            "Expected total line to contain:\n"
                "2 items - $9.55 average price"
        )

    else:
        assert False, "Unexpected filename: " + FILENAME


    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_missing_file():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Missing file",
        r"error|missing|does not exist|doesn't exist",
        "Error message is missing or incorrect. "
            "Expected 'File is missing'.")


def test_final_project_empty_file():
    with open(FILENAME, "w") as file:
        file.write("")

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Empty file",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty'.")

    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_no_records():
    with open(FILENAME, "w") as file:
        file.write("<?xml version=""1.0"" encoding=""UTF-8""?>")

        if FILENAME == "cd_catalog.xml":
            file.write("<CATALOG>")
            file.write("</CATALOG>")
        elif FILENAME == "simple.xml":
            file.write("<breakfast_menu>")
            file.write("</breakfast_menu>")
        elif FILENAME == "plant_catalog.xml":
            file.write("<CATALOG>")
            file.write("</CATALOG>")
        else:
            assert False, "Unexpected filename: " + FILENAME


    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "No records",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty' or 'No data'.")

    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_missing_fields():
    url = "https://www.w3schools.com/xml/" + FILENAME
    text = urllib.request.urlopen(url).read().decode()

    if FILENAME == "simple.xml":
        text = re.sub(r" +<name>French Toast<\/name>\r?\n?", "", text)
    elif FILENAME == "plant_catalog.xml":
        text = re.sub(r" +<COMMON>Columbine<\/COMMON>\r?\n?", "", text)
    elif FILENAME == "cd_catalog.xml":
        text = re.sub(r" +<TITLE>Greatest Hits</TITLE>\r?\n?", "", text)
    else:
        assert False, "Unexpected filename: " + FILENAME

    with open(FILENAME, "w") as file:
        file.write(text)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Missing fields",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_bad_data():
    url = "https://www.w3schools.com/xml/" + FILENAME
    text = urllib.request.urlopen(url).read().decode()

    if FILENAME == "simple.xml":
        text = text.replace("<price>$4.50</price>", "<price>x</price>")
    elif FILENAME == "plant_catalog.xml":
        text = text.replace("<PRICE>$9.37</PRICE>", "<PRICE>x</PRICE>")
    elif FILENAME == "cd_catalog.xml":
        text = text.replace("<PRICE>8.10</PRICE>", "<PRICE>x</PRICE>")
    else:
        assert False, "Unexpected filename: " + FILENAME

    with open(FILENAME, "w") as file:
        file.write(text)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Bad data",
        r"missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def test_final_project_python_does_not_use_dictionaries():
    test.check_file_does_not_contain(
        "Final Project",
        "Final Project",
        r"py",
        r"\[\".+?\"\]",
        "must use parallel arrays rather than dictionaries.")

    test.check_file_does_not_contain(
        "Final Project",
        "Final Project",
        r"py",
        r"\[\'.+?\'\]",
        "must use parallel arrays rather than dictionaries.")


def test_final_project_source_code_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        r"(cs|java|js)",
        "try",
        "include try/catch error handling for file processing.")

    test.check_file_contains(
        "Final Project",
        "Final Project",
        r"(cs|java|js)",
        "catch",
        "include try/catch error handling for file processing.")


def test_final_project_lua_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        "lua",
        "pcall",
        "include pcall error handling for file processing.")


def test_final_project_python_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        "py",
        "try",
        "include try/except error handling for file processing.")

    test.check_file_contains(
        "Final Project",
        "Final Project",
        "py",
        "except",
        "include try/except error handling for file processing.")
