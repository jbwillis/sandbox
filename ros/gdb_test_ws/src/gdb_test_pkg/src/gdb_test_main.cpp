/* Simple node for getting familar with GDB and ros
 * To build: 
 * 		catkin_make -DCMAKE_BUILD_TYPE=Debug
 * To run with GDB: 
 * 		rosrun --prefix 'gdb' gdb_test_pkg gdb_test_main
 */

#include <ros/ros.h>

#include <iostream>

void callback(const ros::TimerEvent &event)
{

	ROS_INFO("Callback called");
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "gdb_test_node");

	ros::NodeHandle nh;


	ros::Timer cb = nh.createTimer(ros::Duration(.1), &callback);

	while(ros::ok())
	{

		ros::spinOnce();
	}

	return 0;
}
