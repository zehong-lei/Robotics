import pybullet as p
import pybullet_data
import time
import os

def main():
    """
    在PyBullet中加载ANYmal C模型和一个平坦的地面。
    """ 
    # 1. 连接到PyBullet物理引擎
    # 使用p.GUI连接到一个带图形用户界面的实例
    # 使用p.DIRECT将连接到一个没有GUI的实例
    physicsClient = p.connect(p.GUI)

    # 2. 设置一个平坦的地面
    # PyBullet自带了一些常用的模型，包括地面
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")

    # 3. 设置重力
    p.setGravity(0, 0, -9.81)

    # 4. 加载ANYmal的URDF文件
    # 假设你的脚本在 'scripts/' 目录下，URDF文件相对于脚本的位置
    # 根据你的目录结构调整路径
    urdf_path = os.path.join(os.path.dirname(__file__), "..", "urdf", "anymal_c_simple_description", "urdf", "anymal.urdf")
    
    # 检查URDF文件是否存在
    if not os.path.exists(urdf_path):
        print(f"错误：找不到URDF文件，请检查路径：{urdf_path}")
        p.disconnect()
        return

    # 定义机器人的初始位置和姿态
    start_pos = [0, 0, 0.7]  # x, y, z 坐标
    start_orientation = p.getQuaternionFromEuler([0, 0, 0])  # 欧拉角 -> 四元数

    # 使用loadURDF加载机器人模型
    print(f"正在从以下路径加载URDF: {urdf_path}")
    anymal_id = p.loadURDF(urdf_path, start_pos, start_orientation)

    # 5. 运行仿真
    print("ANYmal模型已加载。仿真正在运行...")
    try:
        while True:
            p.stepSimulation()
            time.sleep(1./240.) # 仿真步长
    except p.error as e:
        print(f"PyBullet 错误: {e}")
    finally:
        p.disconnect()

if __name__ == "__main__":
    main()