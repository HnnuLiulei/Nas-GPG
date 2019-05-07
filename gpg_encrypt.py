import os
import fs
from fs import open_fs
import gnupg
import datetime

#密钥仓库所在路径，一般安装gnupg后默认路径如下，根据情况修改
gpg = gnupg.GPG(gnupghome="/root/.gnupg")
home_fs = open_fs(".")

#我在python文件所在路径下新建了加密文件夹，用于存放待加密的数据文件
if os.path.exists("encrypted/"):
    print("Encrypt directory exists")
else:
    home_fs.makedir(u"encrypted")
    print("Created encrypted directory")

files_dir = []

#待加密数据文件所在路径
files_dir.append("./Desktop")

for x in files_dir:
    with open(x, "rb") as f:
        print(datetime.datetime.now())
        status = gpg.encrypt_file(f,recipients=["liulei@hnnu.edu.cn（以此形式替换成你的公钥）"],output= files_dir[files_dir.index(x)]+".gpg")
        print(datetime.datetime.now())
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)
        os.rename(files_dir[files_dir.index(x)] + ".gpg", "encrypted/" +files_dir[files_dir.index(x)] + ".gpg")
