
# create temporary dir and copy all the files there
# do git init in that dir
# scan via trufflehog
# get scanned data and return it.

import tempfile
import subprocess
import os
import shutil

class SecretsChecker:

    def scan(self, files):
        _temp_dir = tempfile.TemporaryDirectory()
        p = subprocess.Popen(["git","init"], cwd=_temp_dir.name)
        p.wait()
        for file in files:
            _temp_path = os.path.join(_temp_dir.name, os.path.basename(file))
            print("FileName: "+_temp_path)
            shutil.copy2(file, _temp_path)
        p = subprocess.Popen(["ls","-a"], cwd=_temp_dir.name)
        p.wait()
        p = subprocess.Popen(["git","config", "user.name", "foo"], cwd=_temp_dir.name)
        p.wait()
        p = subprocess.Popen(["git","config", "user.email", "bar"], cwd=_temp_dir.name)
        p.wait()
        p = subprocess.Popen(["ls","-all"], cwd=_temp_dir.name)
        out,err = p.communicate()
        print(out)
        p = subprocess.Popen(["git","add", "."], cwd=_temp_dir.name)
        out,err = p.communicate()
        print(out)
        p = subprocess.Popen(["git","commit", "-m", "dummy_commit"], cwd=_temp_dir.name)
        out,err = p.communicate()
        print(out)
        p = subprocess.Popen(["git","log"], cwd=_temp_dir.name)
        out,err = p.communicate()
        print(out)
        p = subprocess.Popen(["trufflehog", _temp_dir.name], cwd=_temp_dir.name)
        out,err = p.communicate()
        print(out)
