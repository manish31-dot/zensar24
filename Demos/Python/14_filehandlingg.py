try:

    file = open(
        "company_report.txt",
        "r"
    )

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print(
        "Report file not found."
    )

 