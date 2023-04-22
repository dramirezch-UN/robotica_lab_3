sub = rossubscriber('/turtle1/pose', 'turtlesim/Pose');
latest = sub.LatestMessage;