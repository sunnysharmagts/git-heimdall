
# create temporary dir and copy all the files there
# do git init in that dir
# scan via trufflehog
# get scanned data and return it.

import os
import shutil
import subprocess
import tempfile


class SecretsChecker:

    def scan(self, files):
        _temp_dir = tempfile.TemporaryDirectory()
        _current_dir = _temp_dir.name

        p = subprocess.run(["git", "init"], cwd=_current_dir,
                           capture_output=False, shell=False)

        p = subprocess.run(["mv", ".git/hooks/temp-pre-commit",
                           ".git/hooks/pre-commit"],
                           cwd=_current_dir,
                           capture_output=False,
                           shell=False)

        p = subprocess.run(["chmod", "a+x", ".git/hooks/pre-commit"],
                           cwd=_current_dir, capture_output=False, shell=False)

        for file in files:
            _temp_path = os.path.join(_current_dir, os.path.basename(file))
            shutil.copy2(file, _temp_path)

        p = subprocess.run(["git", "config", "user.name", "foo"],
                           cwd=_current_dir, capture_output=False,
                           shell=False)

        p = subprocess.run(["git", "config", "user.email", "bar"],
                           cwd=_current_dir, capture_output=False, shell=False)

        p = subprocess.run(["git", "add", "."], cwd=_current_dir,
                           capture_output=False, shell=False)

        p = subprocess.run(["git", "commit", "-m", "dummy_commit"],
                           cwd=_current_dir, capture_output=False, shell=False)

        p = subprocess.run(["trufflehog", _current_dir], cwd=_current_dir,
                           capture_output=True)
        shutil.rmtree(_current_dir)
        _val = p.stdout
        _vuln = _val.decode()
        _vuln = _vuln.replace('92m', '91m')
        _final_vuln = ''
        for line in _vuln.splitlines():
            if line.startswith('\x1b[91mDate:') or \
               line.startswith('\x1b[91mBranch:') or \
               line.startswith('\x1b[91mCommit:') or \
               line.startswith('\x1b[91mHash:'):
                continue
            _final_vuln = _final_vuln + '\n' + line
        print(_final_vuln)
