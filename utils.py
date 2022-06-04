def get_lines(diff, startChar1, startChar2):
    lines = diff.split('\n')
    return_lines = []
    for line in lines:
        if line.startswith(startChar1) or line.startswith(startChar2):
            return_lines.append(line[0:])
    return return_lines

def get_bug_id(data):
    bug_Id = data["project"]
    bug_Id += " "
    bug_Id += str(data["bugId"])
    return bug_Id

def get_exception_type(data):
    exception_type = data["failingTests"][0]["error"]
    return exception_type

def get_pattern_data(data):
    pattern_data = data['repairPatterns']
    pattern_data = '\n'.join(pattern_data)
    return pattern_data

def get_buggy_lines(data):
    diff_data = data['diff']
    buggy_lines = get_lines(diff_data, '- ', '- ')
    buggy_lines = '\n'.join(buggy_lines)
    return buggy_lines

def get_fixed_lines(data):
    diff_data = data['diff']
    fixed_lines = get_lines(diff_data, '+ ', '+ ')
    fixed_lines = '\n'.join(fixed_lines)
    return fixed_lines

def get_combined_lines(data):
    diff_data = data['diff']
    combined_lines = get_lines(diff_data, '- ', '+ ')
    combined_lines = '\n'.join(combined_lines)
    return combined_lines

def get_all(data):
    bug_Id = get_bug_id(data)
    exception_type = get_exception_type(data)
    pattern_data = get_pattern_data(data)
    buggy_lines = get_buggy_lines(data)
    fixed_lines = get_fixed_lines(data)
    combined_lines = get_combined_lines(data)
    return [bug_Id, exception_type, pattern_data, buggy_lines, fixed_lines, combined_lines]