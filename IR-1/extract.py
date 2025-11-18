#!/usr/bin/python3
import base64
import json
import os

file_lists = []
with open("global.json", "r") as f:
    file_lists = json.load(f)

with open("IR-1.sql", "w") as f:
    f.write(
        "USE compiler;\n"
    )

phase_id = 1
cnt = 0

for case in file_lists:
    cnt += 1
    case_name = case.get("name", "")

    # Extract case name from path
    source = case.get("source", "")[0]
    input = case.get("input", "")[0]
    output = case.get("output", "")[0]

    # Read the test case file
    content = None
    try:
        with open(source, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {case}: {e}")
        continue
    
    # Encode code as base64
    base64_code = base64.b64encode(content.encode()).decode()
    base64_input = base64.b64encode(input.encode()).decode()
    base64_output = base64.b64encode(output.encode()).decode()
    
    # Generate SQL INSERT statement
    try: 
        with open("IR-1.sql", "a") as f:
            f.write(
                f'INSERT INTO TestCases (test_case_id, test_case_disp_name, problem_phase, source_code_base64, input_base64, answer_base64) '
                f'VALUES ({cnt}, "{case_name}", {phase_id}, "{base64_code}", "{base64_input}", "{base64_output}");\n'
            )
    except Exception as e:
        print(f"Error writing SQL for {case}: {e}")
