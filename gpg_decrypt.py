import os
import fs
from fs import open_fs
import gnupg
import datetime

#密钥仓库所在路径，一般安装gnupg后默认路径如下，根据情况修改
gpg = gnupg.GPG(gnupghome="/root/.gnupg")
home_fs = open_fs(".")

files_dir = []
files_dir_clean = []

#我在python文件所在路径下新建了解密文件夹，用于存放解密后的数据文件
if os.path.exists("decrypted/"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir(u"decrypted/")
    print("Created decrypted directory")

#待解密数据文件所在路径
files_dir.append("./encrypted/Desktop.gpg")

files_dir_clean.append("Desktop")

for x in files_dir:
    with open(x, "rb") as f:
        print(datetime.datetime.now())
        status = gpg.decrypt_file(f, passphrase="你的私钥保护密码",output=files_dir_clean[files_dir.index(x)])
        print(datetime.datetime.now())
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)
        os.rename(files_dir_clean[files_dir.index(x)], "decrypted/" + files_dir_clean[files_dir.index(x)])
