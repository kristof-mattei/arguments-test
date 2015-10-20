import subprocess
import os

result = subprocess.check_output([
	r"..\src\App\bin\Debug\App.exe",
	"test",
	"-testwithequals=test",
	"-testwithcolon:test",
	"-testwithspace test"
	], cwd=".", universal_newlines=True)
	
print(result)