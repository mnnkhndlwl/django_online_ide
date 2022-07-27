import uuid

def create_code_file(code,language):
    file_name = str(uuid.uuid4()) + "." + language
    with open( "code/ " + file_name, 'w') as f:
        f.write(code)
    return file_name
    
