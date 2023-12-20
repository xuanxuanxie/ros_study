# 创建自己的工作空间,需要创建catkin_ws和src文件夹
sudo mkdir xxx/catkin_ws/src 
cd catkin_ws
执行 catkin_make => 生成build和devel文件夹 

# 遇到Permission denied的时候，可以采用↓来使得每个人都有对该路径有读和写以及执行的权利，（文件夹上锁）
sudo chmod 777 -R xxx（文件路径）

# 执行 source /devel/setup.bash => 让一些Ros*开头的命令可以使用，每开个terminal都需要source一下

# echo $ROS_PACKAGE_PATH 可以查看 ROS_PACKAGE_PATH 的工作空间目录

# 创建catkin软件包
cd catkin_ws/src
catkin_create_pkg xxx(软件包名) xxx(软件包依赖的包)

# 创建完软件包后（可以多个），回到catkin_ws路径下，
catkin_make 
# 会产生新的build和devel文件（覆盖之前的）

# 在运行所有ROS程序之前，都要运行
roscore

# 查看当前正在活动的ROS节点
rosnode list

# 查看ROS节点的更多信息
rosnode info /节点名字      *** rosnode info /rosout

# 运行软件包内的节点
rosrun 包名 节点名     ***  rosrun turtlesim turtlesim_node 
***   rosrun turtlesim turtlesim_node __name:=my_turtle    重映射参数，改变了节点的名字




#----------------- bug while run the carla-ros-bridge---------------------------
# 报错：RuntimeError: rpc::rpc_error during call in get_sensor_token 
检查egg文件有没有加入到环境变量中去，如果按照readme文件export不行的话，
将 export PYTHONPATH= " ${CARLA_ROOT} /PythonAPI/carla/ " : " ${ SCENARIO_RUNNER_ROOT} " : " ${LEADERBOARD_ROOT} "
改成 export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":"${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg":${PYTHONPATH}

