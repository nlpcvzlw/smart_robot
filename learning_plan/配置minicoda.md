# 设置Conda环境

## conda管理环境的优缺点
- Conda 是一个开源的包管理系统和环境管理系统，主要用于安装多种语言（包括 Python、R 等）的包和管理环境。


- Conda 环境是包含特定集合的包的目录，可以用来隔离不同项目的包，防止包之间的冲突。每个 Conda 环境都有自己的安装目录，且不会与其他环境共享库。


- 跨平台和语言： Conda 可以在 Windows、macOS 和 Linux 上运行，且可以用来安装 Python、R、Ruby、Lua、Scala、Java、JavaScript、C/C++、FORTRAN 等多种语言的包。


- 环境管理： Conda 可以创建多个独立的环境，每个环境可以有自己的包和版本，这对于需要使用不同版本包的不同项目非常有用。


- 包管理： Conda 可以安装非 Python 包，而 pip 只能安装 Python 包。此外，Conda 还可以从 Anaconda.org 和其他第三方源安装包。


- 易于使用： Conda 的命令行界面设计得非常易于使用，且有大量的文档和社区支持。


- 集成度高： Conda 可以与 Anaconda Navigator 和 Jupyter Notebook 等工具无缝集成，提供图形化的包和环境管理界面。


## Windows 安装Conda
Windows 建议先安装Linux环境，在Linux环境中配合命令行使用最佳

### Windows环境中使用Linux系统

- 如果是win10，Windows 10 提供了一个名为 "Windows Subsystem for Linux"（WSL）的功能，可以在 Windows 上运行 Linux 环境。在 WSL 中，你可以像在 Linux 中一样使用 Linux 命令行来安装和控制 Conda。以下是安装和使用的步骤：


- 安装 WSL：在 "控制面板" -> "程序" -> "启用或关闭 Windows 功能" 中勾选 "适用于 Linux 的 Windows 子系统"，然后重启电脑。


- 安装 Linux 发行版：在 Microsoft Store 中搜索 "Linux"，然后选择一个 Linux 发行版进行安装，例如 "Ubuntu"。


- 安装完成后，打开 "Ubuntu"，然后设置你的用户名和密码。


- 更新你的包列表：在命令行中输入 sudo apt update。

### 安装miniconda
- 安装 Miniconda：首先在 Miniconda 的官方网站下载 Linux 版本的 Miniconda，然后在命令行中运行下载的 .sh 文件进行安装。
[官方源](https://docs.conda.io/projects/miniconda/en/latest/)、[清华源](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)
- 下载Miniconda3-latest-Linux-x86_64.sh并安装；

- 在wsl中执行 bash Miniconda3-latest-Linux-x86_64.sh  ——>  source ~/.bashrc 


- 安装完成后，你可以在命令行中输入 conda --version 来检查是否安装成功。如果显示出 conda 的版本号，说明已经安装成功。


- 注意：在 WSL 中，你的 Windows 系统盘通常会被挂载在 /mnt/c/ 目录下，你可以通过这个目录来访问你的 Windows 文件系统。

## conda 环境应用

### 查看虚拟环境列表
- conda env list
- conda info -e

### 创建虚拟环境
- conda create -n <env_name> python_version
- conda create -n pyenv python=3.6

###  复制虚拟环境
- conda create --name <new_env_name> --clone <old_env_name>

###  删除虚拟环境
- conda remove -n <env_name> --all

###  激活虚拟环境
- conda activate <env_name> 

###  退出虚拟环境(进入环境状态下才可使用)
- conda deactivate 

——————————————————————————————————————————————————————————————

###  查看所有包
- conda list -n <env_name>  # 若不指定-n，默认在当前的环境

###  搜索某个包信息
- conda search <package_name>  # 查询包的版本

### 安装
- conda install -n <env_name> -c 镜像地址 <package_name>  # 若不指定-n，默认在当前的虚拟环境
- conda install <package_name>
- conda install <package_name>=1.5.0  # 指定版本

###  更新
###  更新当前环境所有包
- conda update --all

###  更新指定包
- conda update -n <env_name> <package_name>  # 若不指定-n，默认在当前的虚拟环境
- conda update <package_name>

###  删除
- conda remove -n <env_name> <package_name>  # 若不指定-n，默认在当前的虚拟环境
- conda remove <package_name>

### 查看已经添加的channels
- conda config --get channels

### 添加清华镜像(安装一次，镜像也只配置一次)
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
- conda config --set show_channel_urls yes
### 执行完上述命令后，会生成 ~/.condarc

### 删除镜像
- conda config --remove channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free'

### 恢复原源
- conda config --get channels


