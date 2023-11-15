def apiStringInput():
    return(['select * from shootings'])


rule getData:
    output:
        "data/raw/shootingsTable.xlsx",
        "data/raw/crimesTable.xlsx",
        "data/raw/arrestsTable.xlsx"
    script:
        "src/getCartoData.py"


