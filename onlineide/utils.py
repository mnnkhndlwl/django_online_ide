import uuid
import subprocess
import django
django.setup()
from .models import Submissions


def create_code_file(code, language):
    file_name = str(uuid.uuid4()) + "." + language
    with open("code/" + file_name, "w") as f:
        f.write(code)
    return file_name


def execute_file(file_name, language, submission_id):
    submission = Submissions.objects.get(pk=submission_id)
    if language == "cpp":
        # g++ xyz.cpp
        result = subprocess.run(["g++", "code/" + file_name], stdout=subprocess.PIPE)
        if result.returncode != 0:
            # Compile time error
            submission.status = 'E'
            submission.save()
            return
        result = subprocess.run(["a.exe"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            # Runtime error
            submission.status = 'E'
            submission.save()
            return
        output = result.stdout.decode("utf-8")
        submission.output = output
        submission.status = 'S'
        submission.save()
