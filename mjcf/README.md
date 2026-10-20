# TIAGo++ MuJoCo model (MJCF)

A MuJoCo model of the TIAGo++ with its omnidirectional base, taken from
[MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/pal_tiago_dual)
and changed as listed below. Requires MuJoCo 2.2.2 or later.

- `tiago_dual.xml` is the robot.
- `tiago_dual_position.xml` adds a position actuator to every joint of the robot.

The meshes are read from this package's `meshes` folder. The four Menagerie meshes the
package held no copy of are in `meshes/mujoco`: the omnidirectional base, its wheels,
the dual-arm torso's fixed part and the gripper body.

The model is used by `semantic_digital_twin` in
https://github.com/cram2/cognitive_robot_abstract_machine.

## Changes from MuJoCo Menagerie

The free joint on `base_link` was removed. A robot is attached to the world by the drive
its mobile base declares, and a description that carries its own free root joint would
float beside that drive instead of being moved by it.

A grasping frame was added to each wrist, named as the URDF description names it. Every
Cartesian goal, speed limit and tolerance is stated at a gripper's tool frame, and with
the wrist standing in for one they all act 24 cm from where the hand holds something,
which multiplies every error by that lever.

Each finger was split into a mount and a flat box pad, named `*_finger_pad`, which the
gripper closes with. The convex hull of the shipped finger mesh is a wedge, which reads
as a 4 cm opening between the fingers instead of the real 8.6 cm.

Every joint was given an armature of 0.1 kg m², the inertia of the rotor behind it, which
the shipped model does not state. Without it, a wrist held by its position servo
oscillates apart within a second of simulated time.

## License

The model and the meshes in `meshes/mujoco` are released under the
[Apache-2.0 License](LICENSE).
