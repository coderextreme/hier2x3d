import bpy

skeleton = bpy.data.objects.new("Armature", bpy.data.armatures.new("Armature"))
bpy.context.collection.objects.link(skeleton)
bpy.context.view_layer.objects.active = skeleton
skeleton.select_set(True)
bpy.ops.object.mode_set(mode='EDIT')

# Create joints
joints = [
("humanoid_root", (0.0000, 0.0277, 0.8240), (0, 0, 0)),
                ("l_metatarsophalangeal_1", (0.0619, -0.0083, 0.0059), (0.0644, -0.0577, 0.0147)),
              ("l_tarsometatarsal_1", (0.0644, -0.0577, 0.0147), (0.0672, -0.0835, 0.0235)),
            ("l_cuneonavicular_1", (0.0672, -0.0835, 0.0235), (0.0781, -0.0970, 0.0283)),
                    ("l_tarsal_distal_interphalangeal_2", (0.0841, 0.0216, 0.0013), (0.0841, 0.0121, 0.0041)),
                  ("l_tarsal_proximal_interphalangeal_2", (0.0841, 0.0121, 0.0041), (0.0824, -0.0040, 0.0064)),
                ("l_metatarsophalangeal_2", (0.0824, -0.0040, 0.0064), (0.0800, -0.0608, 0.0175)),
              ("l_tarsometatarsal_2", (0.0800, -0.0608, 0.0175), (0.0812, -0.0805, 0.0250)),
            ("l_cuneonavicular_2", (0.0812, -0.0805, 0.0250), (0.0781, -0.0970, 0.0283)),
                    ("l_tarsal_distal_interphalangeal_3", (0.1002, 0.0178, 0.0013), (0.0987, 0.0086, 0.0034)),
                  ("l_tarsal_proximal_interphalangeal_3", (0.0987, 0.0086, 0.0034), (0.0963, -0.0065, 0.0065)),
                ("l_metatarsophalangeal_3", (0.0963, -0.0065, 0.0065), (0.0944, -0.0625, 0.0175)),
              ("l_tarsometatarsal_3", (0.0944, -0.0625, 0.0175), (0.0928, -0.0821, 0.0248)),
            ("l_cuneonavicular_3", (0.0928, -0.0821, 0.0248), (0.0781, -0.0970, 0.0283)),
          ("l_talocalcaneonavicular", (0.0781, -0.0970, 0.0283), (0.1101, -0.0736, 0.0656)),
                    ("l_tarsal_distal_interphalangeal_4", (0.1155, 0.0118, 0.0008), (0.1140, 0.0044, 0.0037)),
                  ("l_tarsal_proximal_interphalangeal_4", (0.1140, 0.0044, 0.0037), (0.1097, -0.0107, 0.0058)),
                ("l_metatarsophalangeal_4", (0.1097, -0.0107, 0.0058), (0.1063, -0.0634, 0.0160)),
              ("l_tarsometatarsal_4", (0.1063, -0.0634, 0.0160), (0.1105, -0.0998, 0.0267)),
                    ("l_tarsal_distal_interphalangeal_5", (0.1271, 0.0000, 0.0000), (0.1262, -0.0077, 0.0023)),
                  ("l_tarsal_proximal_interphalangeal_5", (0.1262, -0.0077, 0.0023), (0.1239, -0.0153, 0.0051)),
                ("l_metatarsophalangeal_5", (0.1239, -0.0153, 0.0051), (0.1206, -0.0671, 0.0124)),
              ("l_tarsometatarsal_5", (0.1206, -0.0671, 0.0124), (0.1105, -0.0998, 0.0267)),
            ("l_transversetarsal", (0.1105, -0.0998, 0.0267), (0.0889, -0.1278, 0.0494)),
          ("l_calcaneocuboid", (0.0889, -0.1278, 0.0494), (0.1101, -0.0736, 0.0656)),
        ("l_talocrural", (0.1101, -0.0736, 0.0656), (0.1040, 0.0308, 0.4867)),
      ("l_knee", (0.1040, 0.0308, 0.4867), (0.0961, -0.0001, 0.9124)),
    ("l_hip", (0.0961, -0.0001, 0.9124), (0.0000, 0.0016, 0.9149)),
                ("r_metatarsophalangeal_1", (-0.0619, -0.0083, 0.0059), (-0.0644, -0.0577, 0.0147)),
              ("r_tarsometatarsal_1", (-0.0644, -0.0577, 0.0147), (-0.0672, -0.0835, 0.0235)),
            ("r_cuneonavicular_1", (-0.0672, -0.0835, 0.0235), (-0.0781, -0.0970, 0.0283)),
                    ("r_tarsal_distal_interphalangeal_2", (-0.0841, 0.0216, 0.0013), (-0.0841, 0.0121, 0.0041)),
                  ("r_tarsal_proximal_interphalangeal_2", (-0.0841, 0.0121, 0.0041), (-0.0823, -0.0040, 0.0064)),
                ("r_metatarsophalangeal_2", (-0.0823, -0.0040, 0.0064), (-0.0800, -0.0608, 0.0175)),
              ("r_tarsometatarsal_2", (-0.0800, -0.0608, 0.0175), (-0.0812, -0.0805, 0.0250)),
            ("r_cuneonavicular_2", (-0.0812, -0.0805, 0.0250), (-0.0781, -0.0970, 0.0283)),
                    ("r_tarsal_distal_interphalangeal_3", (-0.1002, 0.0178, 0.0013), (-0.0987, 0.0086, 0.0034)),
                  ("r_tarsal_proximal_interphalangeal_3", (-0.0987, 0.0086, 0.0034), (-0.0963, -0.0065, 0.0065)),
                ("r_metatarsophalangeal_3", (-0.0963, -0.0065, 0.0065), (-0.0944, -0.0625, 0.0175)),
              ("r_tarsometatarsal_3", (-0.0944, -0.0625, 0.0175), (-0.0928, -0.0821, 0.0248)),
            ("r_cuneonavicular_3", (-0.0928, -0.0821, 0.0248), (-0.0781, -0.0970, 0.0283)),
          ("r_talocalcaneonavicular", (-0.0781, -0.0970, 0.0283), (-0.0801, -0.0766, 0.0712)),
                    ("r_tarsal_distal_interphalangeal_4", (-0.1155, 0.0118, 0.0008), (-0.1140, 0.0044, 0.0037)),
                  ("r_tarsal_proximal_interphalangeal_4", (-0.1140, 0.0044, 0.0037), (-0.1097, -0.0107, 0.0058)),
                ("r_metatarsophalangeal_4", (-0.1097, -0.0107, 0.0058), (-0.1063, -0.0634, 0.0160)),
              ("r_tarsometatarsal_4", (-0.1063, -0.0634, 0.0160), (-0.1105, -0.0998, 0.0267)),
                    ("r_tarsal_distal_interphalangeal_5", (-0.1271, 0.0000, 0.0000), (-0.1262, -0.0077, 0.0023)),
                  ("r_tarsal_proximal_interphalangeal_5", (-0.1262, -0.0077, 0.0023), (-0.1239, -0.0153, 0.0051)),
                ("r_metatarsophalangeal_5", (-0.1239, -0.0153, 0.0051), (-0.1206, -0.0671, 0.0124)),
              ("r_tarsometatarsal_5", (-0.1206, -0.0671, 0.0124), (-0.1105, -0.0998, 0.0267)),
            ("r_transversetarsal", (-0.1105, -0.0998, 0.0267), (-0.0889, -0.1278, 0.0494)),
          ("r_calcaneocuboid", (-0.0889, -0.1278, 0.0494), (-0.0801, -0.0766, 0.0712)),
        ("r_talocrural", (-0.0801, -0.0766, 0.0712), (-0.0867, 0.0318, 0.4913)),
      ("r_knee", (-0.0867, 0.0318, 0.4913), (-0.0950, 0.0029, 0.9171)),
    ("r_hip", (-0.0950, 0.0029, 0.9171), (0.0000, 0.0016, 0.9149)),
  ("sacroiliac", (0.0000, 0.0016, 0.9149), (0.0000, 0.0277, 0.8240)),
                                                    ("l_eyelid_joint", (0.0503, -0.0689, 1.4157), (0.0044, 0.0236, 1.6209)),
                                                    ("r_eyelid_joint", (-0.0507, -0.0689, 1.4157), (0.0044, 0.0236, 1.6209)),
                                                    ("l_eyeball_joint", (0.0479, -0.0188, 1.3963), (0.0044, 0.0236, 1.6209)),
                                                    ("r_eyeball_joint", (-0.0483, -0.0188, 1.3963), (0.0044, 0.0236, 1.6209)),
                                                    ("l_eyebrow_joint", (0.0216, 0.0051, 1.4053), (0.0044, 0.0236, 1.6209)),
                                                    ("r_eyebrow_joint", (-0.0219, 0.0051, 1.4053), (0.0044, 0.0236, 1.6209)),
                                                    ("temporomandibular", (-0.0002, -0.0865, 1.3043), (0.0044, 0.0236, 1.6209)),
                                                  ("skullbase", (0.0044, 0.0236, 1.6209), (0.0066, -0.0034, 1.6144)),
                                                ("vc1", (0.0066, -0.0034, 1.6144), (0.0066, -0.0103, 1.5928)),
                                              ("vc2", (0.0066, -0.0103, 1.5928), (0.0066, -0.0103, 1.5800)),
                                            ("vc3", (0.0066, -0.0103, 1.5800), (0.0066, -0.0084, 1.5662)),
                                          ("vc4", (0.0066, -0.0084, 1.5662), (0.0066, -0.0082, 1.5520)),
                                        ("vc5", (0.0066, -0.0082, 1.5520), (0.0066, -0.0143, 1.5357)),
                                      ("vc6", (0.0066, -0.0143, 1.5357), (0.0066, -0.0301, 1.5132)),
                                    ("vc7", (0.0066, -0.0301, 1.5132), (0.0065, -0.0387, 1.4951)),
                                                    ("l_carpal_interphalangeal_1", (0.1955, 0.0464, 0.8159), (0.1951, 0.0246, 0.8226)),
                                                  ("l_metacarpophalangeal_1", (0.1951, 0.0246, 0.8226), (0.1924, -0.0534, 0.8472)),
                                                ("l_carpometacarpal_1", (0.1924, -0.0534, 0.8472), (0.1811, -0.0826, 0.6975)),
                                              ("l_midcarpal_1", (0.1811, -0.0826, 0.6975), (0.1984, -0.0583, 0.8663)),
                                                      ("l_carpal_distal_interphalangeal_2", (0.2028, -0.0236, 0.7139), (0.2017, -0.0248, 0.7363)),
                                                    ("l_carpal_proximal_interphalangeal_2", (0.2017, -0.0248, 0.7363), (0.1983, -0.0280, 0.7815)),
                                                  ("l_metacarpophalangeal_2", (0.1983, -0.0280, 0.7815), (0.1983, -0.0280, 0.8024)),
                                                ("l_carpometacarpal_2", (0.1983, -0.0280, 0.8024), (0.1811, -0.0935, 0.6984)),
                                              ("l_midcarpal_2", (0.1811, -0.0935, 0.6984), (0.1984, -0.0583, 0.8663)),
                                                      ("l_carpal_distal_interphalangeal_3", (0.2026, -0.0494, 0.7011), (0.2013, -0.0503, 0.7273)),
                                                    ("l_carpal_proximal_interphalangeal_3", (0.2013, -0.0503, 0.7273), (0.1987, -0.0530, 0.7818)),
                                                  ("l_metacarpophalangeal_3", (0.1987, -0.0530, 0.7818), (0.1987, -0.0530, 0.8029)),
                                                ("l_carpometacarpal_3", (0.1987, -0.0530, 0.8029), (0.1809, -0.1067, 0.7000)),
                                              ("l_midcarpal_3", (0.1809, -0.1067, 0.7000), (0.1984, -0.0583, 0.8663)),
                                                      ("l_carpal_distal_interphalangeal_4", (0.1983, -0.0767, 0.7045), (0.1973, -0.0777, 0.7287)),
                                                    ("l_carpal_proximal_interphalangeal_4", (0.1973, -0.0777, 0.7287), (0.1956, -0.0794, 0.7815)),
                                                  ("l_metacarpophalangeal_4", (0.1956, -0.0794, 0.7815), (0.1956, -0.0794, 0.8019)),
                                                ("l_carpometacarpal_4", (0.1956, -0.0794, 0.8019), (0.1809, -0.1276, 0.6973)),
                                                      ("l_carpal_distal_interphalangeal_5", (0.1948, -0.1017, 0.7277), (0.1938, -0.1024, 0.7452)),
                                                    ("l_carpal_proximal_interphalangeal_5", (0.1938, -0.1024, 0.7452), (0.1925, -0.1036, 0.7866)),
                                                  ("l_metacarpophalangeal_5", (0.1925, -0.1036, 0.7866), (0.1925, -0.1036, 0.8066)),
                                                ("l_carpometacarpal_5", (0.1925, -0.1036, 0.8066), (0.1809, -0.1276, 0.6973)),
                                              ("l_midcarpal_4_5", (0.1809, -0.1276, 0.6973), (0.1984, -0.0583, 0.8663)),
                                            ("l_radiocarpal", (0.1984, -0.0583, 0.8663), (0.2014, -0.0682, 1.1357)),
                                          ("l_elbow", (0.2014, -0.0682, 1.1357), (0.2029, -0.0387, 1.4376)),
                                        ("l_shoulder", (0.2029, -0.0387, 1.4376), (0.0962, -0.0424, 1.4269)),
                                      ("l_acromioclavicular", (0.0962, -0.0424, 1.4269), (0.0820, -0.0353, 1.4488)),
                                    ("l_sternoclavicular", (0.0820, -0.0353, 1.4488), (0.0065, -0.0387, 1.4951)),
                                                    ("r_carpal_interphalangeal_1", (-0.1864, 0.0506, 0.8190), (-0.1874, 0.0306, 0.8256)),
                                                  ("r_metacarpophalangeal_1", (-0.1874, 0.0306, 0.8256), (-0.1899, -0.0473, 0.8502)),
                                                ("r_carpometacarpal_1", (-0.1899, -0.0473, 0.8502), (-0.1811, -0.0826, 0.6975)),
                                              ("r_midcarpal_1", (-0.1811, -0.0826, 0.6975), (-0.1959, -0.0521, 0.8694)),
                                                      ("r_carpal_distal_interphalangeal_2", (-0.1945, -0.0173, 0.7169), (-0.1954, -0.0185, 0.7393)),
                                                    ("r_carpal_proximal_interphalangeal_2", (-0.1954, -0.0185, 0.7393), (-0.1961, -0.0218, 0.7846)),
                                                  ("r_metacarpophalangeal_2", (-0.1961, -0.0218, 0.7846), (-0.1961, -0.0218, 0.8055)),
                                                ("r_carpometacarpal_2", (-0.1961, -0.0218, 0.8055), (-0.1811, -0.0935, 0.6984)),
                                              ("r_midcarpal_2", (-0.1811, -0.0935, 0.6984), (-0.1959, -0.0521, 0.8694)),
                                                      ("r_carpal_distal_interphalangeal_3", (-0.1939, -0.0432, 0.7042), (-0.1950, -0.0441, 0.7304)),
                                                    ("r_carpal_proximal_interphalangeal_3", (-0.1950, -0.0441, 0.7304), (-0.1972, -0.0468, 0.7849)),
                                                  ("r_metacarpophalangeal_3", (-0.1972, -0.0468, 0.7849), (-0.1972, -0.0468, 0.8060)),
                                                ("r_carpometacarpal_3", (-0.1972, -0.0468, 0.8060), (-0.1809, -0.1067, 0.7000)),
                                              ("r_midcarpal_3", (-0.1809, -0.1067, 0.7000), (-0.1959, -0.0521, 0.8694)),
                                                      ("r_carpal_distal_interphalangeal_4", (-0.1908, -0.0706, 0.7077), (-0.1920, -0.0716, 0.7318)),
                                                    ("r_carpal_proximal_interphalangeal_4", (-0.1920, -0.0716, 0.7318), (-0.1951, -0.0732, 0.7845)),
                                                  ("r_metacarpophalangeal_4", (-0.1951, -0.0732, 0.7845), (-0.1951, -0.0732, 0.8049)),
                                                ("r_carpometacarpal_4", (-0.1951, -0.0732, 0.8049), (-0.1809, -0.1276, 0.6973)),
                                                      ("r_carpal_distal_interphalangeal_5", (-0.1908, -0.0960, 0.7540), (-0.1902, -0.0963, 0.7483)),
                                                    ("r_carpal_proximal_interphalangeal_5", (-0.1902, -0.0963, 0.7483), (-0.1926, -0.0975, 0.7896)),
                                                  ("r_metacarpophalangeal_5", (-0.1926, -0.0975, 0.7896), (-0.1926, -0.0975, 0.8096)),
                                                ("r_carpometacarpal_5", (-0.1926, -0.0975, 0.8096), (-0.1809, -0.1276, 0.6973)),
                                              ("r_midcarpal_4_5", (-0.1809, -0.1276, 0.6973), (-0.1959, -0.0521, 0.8694)),
                                            ("r_radiocarpal", (-0.1959, -0.0521, 0.8694), (-0.1949, -0.0620, 1.1388)),
                                          ("r_elbow", (-0.1949, -0.0620, 1.1388), (-0.1907, -0.0325, 1.4407)),
                                        ("r_shoulder", (-0.1907, -0.0325, 1.4407), (-0.0836, -0.0401, 1.4281)),
                                      ("r_acromioclavicular", (-0.0836, -0.0401, 1.4281), (-0.0694, -0.0330, 1.4600)),
                                    ("r_sternoclavicular", (-0.0694, -0.0330, 1.4600), (0.0065, -0.0387, 1.4951)),
                                  ("vt1", (0.0065, -0.0387, 1.4951), (0.0063, -0.0484, 1.4761)),
                                ("vt2", (0.0063, -0.0484, 1.4761), (0.0062, -0.0570, 1.4583)),
                              ("vt3", (0.0062, -0.0570, 1.4583), (0.0061, -0.0675, 1.4320)),
                            ("vt4", (0.0061, -0.0675, 1.4320), (0.0060, -0.0745, 1.4102)),
                          ("vt5", (0.0060, -0.0745, 1.4102), (0.0059, -0.0800, 1.3866)),
                        ("vt6", (0.0059, -0.0800, 1.3866), (0.0058, -0.0833, 1.3625)),
                      ("vt7", (0.0058, -0.0833, 1.3625), (0.0057, -0.0845, 1.3382)),
                    ("vt8", (0.0057, -0.0845, 1.3382), (0.0057, -0.0838, 1.3126)),
                  ("vt9", (0.0057, -0.0838, 1.3126), (0.0056, -0.0822, 1.2848)),
                ("vt10", (0.0056, -0.0822, 1.2848), (0.0053, -0.0810, 1.2679)),
              ("vt11", (0.0053, -0.0810, 1.2679), (0.0051, -0.0808, 1.2278)),
            ("vt12", (0.0051, -0.0808, 1.2278), (0.0048, -0.0805, 1.1912)),
          ("vl1", (0.0048, -0.0805, 1.1912), (0.0045, -0.0800, 1.1546)),
        ("vl2", (0.0045, -0.0800, 1.1546), (0.0041, -0.0796, 1.1276)),
      ("vl3", (0.0041, -0.0796, 1.1276), (0.0035, -0.0787, 1.0925)),
    ("vl4", (0.0035, -0.0787, 1.0925), (0.0028, -0.0776, 1.0568)),
  ("vl5", (0.0028, -0.0776, 1.0568), (0.0000, 0.0277, 0.8240)),
]

for joint in joints:
    joint_name, joint_start, joint_end = joint
    bpy.ops.armature.bone_primitive_add(name=joint_name)
    new_segment = skeleton.data.edit_bones[joint_name]
    new_segment.head = joint_start
    new_segment.tail = joint_end

# Connect joints
segments = [
                ("l_tarsometatarsal_1", "l_metatarsophalangeal_1"),
              ("l_cuneonavicular_1", "l_tarsometatarsal_1"),
            ("l_talocalcaneonavicular", "l_cuneonavicular_1"),
                    ("l_tarsal_proximal_interphalangeal_2", "l_tarsal_distal_interphalangeal_2"),
                  ("l_metatarsophalangeal_2", "l_tarsal_proximal_interphalangeal_2"),
                ("l_tarsometatarsal_2", "l_metatarsophalangeal_2"),
              ("l_cuneonavicular_2", "l_tarsometatarsal_2"),
            ("l_talocalcaneonavicular", "l_cuneonavicular_2"),
                    ("l_tarsal_proximal_interphalangeal_3", "l_tarsal_distal_interphalangeal_3"),
                  ("l_metatarsophalangeal_3", "l_tarsal_proximal_interphalangeal_3"),
                ("l_tarsometatarsal_3", "l_metatarsophalangeal_3"),
              ("l_cuneonavicular_3", "l_tarsometatarsal_3"),
            ("l_talocalcaneonavicular", "l_cuneonavicular_3"),
          ("l_talocrural", "l_talocalcaneonavicular"),
                    ("l_tarsal_proximal_interphalangeal_4", "l_tarsal_distal_interphalangeal_4"),
                  ("l_metatarsophalangeal_4", "l_tarsal_proximal_interphalangeal_4"),
                ("l_tarsometatarsal_4", "l_metatarsophalangeal_4"),
              ("l_transversetarsal", "l_tarsometatarsal_4"),
                    ("l_tarsal_proximal_interphalangeal_5", "l_tarsal_distal_interphalangeal_5"),
                  ("l_metatarsophalangeal_5", "l_tarsal_proximal_interphalangeal_5"),
                ("l_tarsometatarsal_5", "l_metatarsophalangeal_5"),
              ("l_transversetarsal", "l_tarsometatarsal_5"),
            ("l_calcaneocuboid", "l_transversetarsal"),
          ("l_talocrural", "l_calcaneocuboid"),
        ("l_knee", "l_talocrural"),
      ("l_hip", "l_knee"),
    ("sacroiliac", "l_hip"),
                ("r_tarsometatarsal_1", "r_metatarsophalangeal_1"),
              ("r_cuneonavicular_1", "r_tarsometatarsal_1"),
            ("r_talocalcaneonavicular", "r_cuneonavicular_1"),
                    ("r_tarsal_proximal_interphalangeal_2", "r_tarsal_distal_interphalangeal_2"),
                  ("r_metatarsophalangeal_2", "r_tarsal_proximal_interphalangeal_2"),
                ("r_tarsometatarsal_2", "r_metatarsophalangeal_2"),
              ("r_cuneonavicular_2", "r_tarsometatarsal_2"),
            ("r_talocalcaneonavicular", "r_cuneonavicular_2"),
                    ("r_tarsal_proximal_interphalangeal_3", "r_tarsal_distal_interphalangeal_3"),
                  ("r_metatarsophalangeal_3", "r_tarsal_proximal_interphalangeal_3"),
                ("r_tarsometatarsal_3", "r_metatarsophalangeal_3"),
              ("r_cuneonavicular_3", "r_tarsometatarsal_3"),
            ("r_talocalcaneonavicular", "r_cuneonavicular_3"),
          ("r_talocrural", "r_talocalcaneonavicular"),
                    ("r_tarsal_proximal_interphalangeal_4", "r_tarsal_distal_interphalangeal_4"),
                  ("r_metatarsophalangeal_4", "r_tarsal_proximal_interphalangeal_4"),
                ("r_tarsometatarsal_4", "r_metatarsophalangeal_4"),
              ("r_transversetarsal", "r_tarsometatarsal_4"),
                    ("r_tarsal_proximal_interphalangeal_5", "r_tarsal_distal_interphalangeal_5"),
                  ("r_metatarsophalangeal_5", "r_tarsal_proximal_interphalangeal_5"),
                ("r_tarsometatarsal_5", "r_metatarsophalangeal_5"),
              ("r_transversetarsal", "r_tarsometatarsal_5"),
            ("r_calcaneocuboid", "r_transversetarsal"),
          ("r_talocrural", "r_calcaneocuboid"),
        ("r_knee", "r_talocrural"),
      ("r_hip", "r_knee"),
    ("sacroiliac", "r_hip"),
  ("humanoid_root", "sacroiliac"),
                                                    ("skullbase", "l_eyelid_joint"),
                                                    ("skullbase", "r_eyelid_joint"),
                                                    ("skullbase", "l_eyeball_joint"),
                                                    ("skullbase", "r_eyeball_joint"),
                                                    ("skullbase", "l_eyebrow_joint"),
                                                    ("skullbase", "r_eyebrow_joint"),
                                                    ("skullbase", "temporomandibular"),
                                                  ("vc1", "skullbase"),
                                                ("vc2", "vc1"),
                                              ("vc3", "vc2"),
                                            ("vc4", "vc3"),
                                          ("vc5", "vc4"),
                                        ("vc6", "vc5"),
                                      ("vc7", "vc6"),
                                    ("vt1", "vc7"),
                                                    ("l_metacarpophalangeal_1", "l_carpal_interphalangeal_1"),
                                                  ("l_carpometacarpal_1", "l_metacarpophalangeal_1"),
                                                ("l_midcarpal_1", "l_carpometacarpal_1"),
                                              ("l_radiocarpal", "l_midcarpal_1"),
                                                      ("l_carpal_proximal_interphalangeal_2", "l_carpal_distal_interphalangeal_2"),
                                                    ("l_metacarpophalangeal_2", "l_carpal_proximal_interphalangeal_2"),
                                                  ("l_carpometacarpal_2", "l_metacarpophalangeal_2"),
                                                ("l_midcarpal_2", "l_carpometacarpal_2"),
                                              ("l_radiocarpal", "l_midcarpal_2"),
                                                      ("l_carpal_proximal_interphalangeal_3", "l_carpal_distal_interphalangeal_3"),
                                                    ("l_metacarpophalangeal_3", "l_carpal_proximal_interphalangeal_3"),
                                                  ("l_carpometacarpal_3", "l_metacarpophalangeal_3"),
                                                ("l_midcarpal_3", "l_carpometacarpal_3"),
                                              ("l_radiocarpal", "l_midcarpal_3"),
                                                      ("l_carpal_proximal_interphalangeal_4", "l_carpal_distal_interphalangeal_4"),
                                                    ("l_metacarpophalangeal_4", "l_carpal_proximal_interphalangeal_4"),
                                                  ("l_carpometacarpal_4", "l_metacarpophalangeal_4"),
                                                ("l_midcarpal_4_5", "l_carpometacarpal_4"),
                                                      ("l_carpal_proximal_interphalangeal_5", "l_carpal_distal_interphalangeal_5"),
                                                    ("l_metacarpophalangeal_5", "l_carpal_proximal_interphalangeal_5"),
                                                  ("l_carpometacarpal_5", "l_metacarpophalangeal_5"),
                                                ("l_midcarpal_4_5", "l_carpometacarpal_5"),
                                              ("l_radiocarpal", "l_midcarpal_4_5"),
                                            ("l_elbow", "l_radiocarpal"),
                                          ("l_shoulder", "l_elbow"),
                                        ("l_acromioclavicular", "l_shoulder"),
                                      ("l_sternoclavicular", "l_acromioclavicular"),
                                    ("vt1", "l_sternoclavicular"),
                                                    ("r_metacarpophalangeal_1", "r_carpal_interphalangeal_1"),
                                                  ("r_carpometacarpal_1", "r_metacarpophalangeal_1"),
                                                ("r_midcarpal_1", "r_carpometacarpal_1"),
                                              ("r_radiocarpal", "r_midcarpal_1"),
                                                      ("r_carpal_proximal_interphalangeal_2", "r_carpal_distal_interphalangeal_2"),
                                                    ("r_metacarpophalangeal_2", "r_carpal_proximal_interphalangeal_2"),
                                                  ("r_carpometacarpal_2", "r_metacarpophalangeal_2"),
                                                ("r_midcarpal_2", "r_carpometacarpal_2"),
                                              ("r_radiocarpal", "r_midcarpal_2"),
                                                      ("r_carpal_proximal_interphalangeal_3", "r_carpal_distal_interphalangeal_3"),
                                                    ("r_metacarpophalangeal_3", "r_carpal_proximal_interphalangeal_3"),
                                                  ("r_carpometacarpal_3", "r_metacarpophalangeal_3"),
                                                ("r_midcarpal_3", "r_carpometacarpal_3"),
                                              ("r_radiocarpal", "r_midcarpal_3"),
                                                      ("r_carpal_proximal_interphalangeal_4", "r_carpal_distal_interphalangeal_4"),
                                                    ("r_metacarpophalangeal_4", "r_carpal_proximal_interphalangeal_4"),
                                                  ("r_carpometacarpal_4", "r_metacarpophalangeal_4"),
                                                ("r_midcarpal_4_5", "r_carpometacarpal_4"),
                                                      ("r_carpal_proximal_interphalangeal_5", "r_carpal_distal_interphalangeal_5"),
                                                    ("r_metacarpophalangeal_5", "r_carpal_proximal_interphalangeal_5"),
                                                  ("r_carpometacarpal_5", "r_metacarpophalangeal_5"),
                                                ("r_midcarpal_4_5", "r_carpometacarpal_5"),
                                              ("r_radiocarpal", "r_midcarpal_4_5"),
                                            ("r_elbow", "r_radiocarpal"),
                                          ("r_shoulder", "r_elbow"),
                                        ("r_acromioclavicular", "r_shoulder"),
                                      ("r_sternoclavicular", "r_acromioclavicular"),
                                    ("vt1", "r_sternoclavicular"),
                                  ("vt2", "vt1"),
                                ("vt3", "vt2"),
                              ("vt4", "vt3"),
                            ("vt5", "vt4"),
                          ("vt6", "vt5"),
                        ("vt7", "vt6"),
                      ("vt8", "vt7"),
                    ("vt9", "vt8"),
                  ("vt10", "vt9"),
                ("vt11", "vt10"),
              ("vt12", "vt11"),
            ("vl1", "vt12"),
          ("vl2", "vl1"),
        ("vl3", "vl2"),
      ("vl4", "vl3"),
    ("vl5", "vl4"),
  ("humanoid_root", "vl5"),
]

for segment in segments:
    parent_joint, child_joint = segment
    parent = skeleton.data.edit_bones[parent_joint]
    child = skeleton.data.edit_bones[child_joint]
    child.parent = parent

# Exit edit mode
bpy.ops.object.mode_set(mode='OBJECT')