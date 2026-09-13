import platform
import shutil


class Config:
    system = platform.system()
    firefox_path = shutil.which("firefox")
    if firefox_path == None:
        firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.EXE'