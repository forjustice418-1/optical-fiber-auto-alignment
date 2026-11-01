<?xml version="1.0" ?>
<sdf version="1.7">

<model name="xyz_stage">

  <link name="base">

    <visual name="base_visual">
      <geometry>
        <box>
          <size>1 1 0.2</size>
        </box>
      </geometry>

      <material>
        <ambient>0 0 1 1</ambient>
      </material>

    </visual>

  </link>


  <link name="x_stage">

    <pose>0 0 0.25 0 0 0</pose>

    <visual name="x_visual">
      <geometry>
        <box>
          <size>0.6 0.6 0.1</size>
        </box>
      </geometry>

      <material>
        <ambient>0 1 0 1</ambient>
      </material>

    </visual>

  </link>


  <link name="fiber">

    <pose>0 0 0.45 0 0 0</pose>

    <visual name="fiber_visual">
      <geometry>
        <cylinder>
          <radius>0.03</radius>
          <length>0.3</length>
        </cylinder>
      </geometry>

      <material>
        <ambient>1 0 0 1</ambient>
      </material>

    </visual>

  </link>

</model>

</sdf>
