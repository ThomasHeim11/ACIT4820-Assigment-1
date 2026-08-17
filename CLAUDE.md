# ACIT4820 — Project Instructions

## ROS 2 only — never ROS 1

This project targets **ROS 2 Jazzy** on Ubuntu 24.04. ROS 1 is end-of-life (Noetic
EOL May 2025) and must never be used, suggested, or mixed in.

Web searches and older tutorials are full of ROS 1 material that looks superficially
correct. Verify before copying: if a snippet uses any of the left-hand column below,
it is ROS 1 and must be rewritten.

| Never use (ROS 1)                     | Always use (ROS 2)                          |
| ------------------------------------- | ------------------------------------------- |
| `catkin_make`, `catkin build`         | `colcon build --symlink-install`            |
| `catkin_ws/`, `devel/`                | `ros2_ws/`, `install/`                      |
| `rospy`, `roscpp`                     | `rclpy`, `rclcpp`                           |
| `rosrun`, `roslaunch`                 | `ros2 run`, `ros2 launch`                   |
| `rostopic`, `rosnode`, `rosbag`       | `ros2 topic`, `ros2 node`, `ros2 bag`       |
| `roscore` / ROS master                | no master — DDS discovery                   |
| `catkin_pkg`, `package.xml` format 1  | `ament_python` / `ament_cmake`, format 3    |
| `.launch` files (ROS 1 XML schema)    | `.launch.xml` (ROS 2 XML schema)            |
| `rospy.init_node()`, `rospy.Rate`     | `rclpy.init()`, `Node`, `create_timer()`    |
| `rospy.loginfo()`                     | `self.get_logger().info()`                  |
| `$(find pkg)` in launch               | `$(find-pkg-share pkg)`                     |

### Launch files

ROS 1 and ROS 2 XML launch files share the `.launch.xml`-ish look but are **not**
compatible. ROS 2 requires `<node pkg=" " exec=" ">` (not `type=`), and package
paths resolve with `$(find-pkg-share ...)`. Prefer XML launch files over Python ones
in this project.

### Documentation

When citing or consulting docs, use the **Jazzy** version of docs.ros.org. Treat
`wiki.ros.org` as ROS 1 unless a page is explicitly marked otherwise.

## Environment

- ROS 2 Jazzy at `/opt/ros/jazzy`, auto-sourced from `~/.bashrc`
- Workspace overlay must be sourced per shell: `source install/setup.bash`
- Build from the workspace root, never from inside `src/`
- Wayland session with XWayland; RViz and Qt GUIs run fine
