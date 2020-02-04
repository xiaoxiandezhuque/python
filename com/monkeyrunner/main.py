from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# 连接手机设备
device = MonkeyRunner.waitForConnection(6, '127.0.0.1:62026')

# 卸载
device.removePackage('com.kotlin.mvp')

# 安装
device.installPackage('E:/JAVA/monkeyrunner/Test1/ThinkDrive_new.apk')

# 截图
result = device.takeSnapshot()
# 将截图保存到文件
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test1\\Test1_001.png', 'png')

# 暂停5秒
MonkeyRunner.sleep(5)

# 启动任意的Activity
# device.startActivity(component="包名/启动Activity")
# 以下两种都OK
device.startActivity(component="cn.richinfo.thinkdrive/cn.richinfo.thinkdrive.ui.activities.NavigateActivity")
device.startActivity(component="cn.richinfo.thinkdrive/.ui.activities.NavigateActivity")

# 字符串发送到键盘
# device.type('字符串')
device.type('Findyou')

# 唤醒设备屏幕
# 锁屏后,屏幕关闭，可以用下命令唤醒
device.wake()

# 重起手机
device.reboot()

# 模拟滑动
# device.drag(X,Y,D,S)
# X 开始坐标
# Y 结束坐标
# D 拖动持续时间(以秒为单位)，默认1.0秒
# S 插值点时要采取的步骤。默认值是10
device.drag((100, 1053), (520, 1053), 0.1, 10)

# 在指定位置发送触摸事件
# device.touch(x,y,触摸事件类型)
# x,y的单位为像素
# 触摸事件类型，请见下文中Findyou对device.press描述
device.touch(520, 520, 'DOWN_AND_UP')

# 发送指定类型指定键码的事件
# device.press(参数1:键码,参数2:触摸事件类型)
# 参数1：见android.view.KeyEvent
# 参数2，如有TouchPressType()返回的类型－触摸事件类型，有三种。
# 1、DOWN 发送一个DOWN事件。指定DOWN事件类型发送到设备，对应的按一个键或触摸屏幕上。
# 2、UP 发送一个UP事件。指定UP事件类型发送到设备，对应释放一个键或从屏幕上抬起。
# 3、DOWN_AND_UP 发送一个DOWN事件，然后一个UP事件。对应于输入键或点击屏幕。
# 以上三种事件做为press()参数或touch()参数

# 按下HOME键
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
# 按下BACK键
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
# 按下下导航键
device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
# 按下上导航键
device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
# 按下OK键
device.press('KEYCODE_DPAD_CENTER', MonkeyDevice.DOWN_AND_UP)

# KeyCode:
#
# home键 KEYCODE_HOME
# back键 KEYCODE_BACK
# send键 KEYCODE_CALL
# end键 KEYCODE_ENDCALL
# 上导航键 KEYCODE_DPAD_UP
# 下导航键 KEYCODE_DPAD_DOWN
# 左导航 KEYCODE_DPAD_LEFT
# 右导航键 KEYCODE_DPAD_RIGHT
# ok键 KEYCODE_DPAD_CENTER
# 上音量键 KEYCODE_VOLUME_UP
# 下音量键 KEYCODE_VOLUME_DOWN
# power键 KEYCODE_POWER
# camera键 KEYCODE_CAMERA
# menu键 KEYCODE_MENU

# 点击事件触发，界面开始变化，截屏比较
imagetobecompared = MonkeyRunner.loadImageFromFile('image file path');
screenshot = device.takeSnapshot();
if screenshot.sameAs(imagetobecompared, 0.9):
    print("2张图片相同")
else:
    print("2张图片不相同")
