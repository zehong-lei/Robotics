Virtual environment(VS Code)
    python -m venv .venv
    .\.venv\Scripts\activate
    Ctrl + Shift + P    Python: Select Interpreter

PyBullet
    pip install pybullet
    # 首先，创建一个用于存放URDF文件的目录

URDF
    mkdir -p urdf
    # 进入该目录
    cd urdf

    # 从GitHub克隆包含URDF文件的仓库
    git clone https://github.com/ANYbotics/anymal_c_simple_description.git

    # 你现在可以在 urdf/anymal_c_simple_description/urdf/ 目录下找到 anymal.urdf 文件

旋转	Ctrl + 鼠标左键拖动
平移	Ctrl + 鼠标右键拖动 或 鼠标滚轮拖动
缩放	鼠标滚轮