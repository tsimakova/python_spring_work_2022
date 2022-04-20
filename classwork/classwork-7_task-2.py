
#todo: задан словарь

#{ "sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12, "overscan_top":10 }

# Нужно создать  файл config.txt с содержимым вида:
'''
sdtv_mode=2
hdmi_drive=2
hdmi_group=2
hdmi_mode=16
overscan_left=20
overscan_right=12
overscan_top=10
© 2022 GitHub, Inc.
'''

param_dict = {"sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12, "overscan_top":10}

fd = open("D:\PYTHON_course\config.txt", "r+")  # open file for reading and writing

for k, v in param_dict.items():  # select keys and values from dictionary
    fd.write(str(k) + "=" + str(v) + '\n')  # write formatted string to the opened file

fd.close

