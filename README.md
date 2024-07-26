## AutoResolutionAdjust-自动修改游戏内分辨率

### 引入话题

在游玩各类游戏时,我们常常遇见关于游戏优化的问题,通常来讲,我们会选择降低游戏的某一部分的渲染精度,比如将阴影,模型精度等降低,通过牺牲整个画面某一部分的精度来维持整体的相对高精度.

但有一个方法却常常被人遗忘,那就是修改游戏的分辨率,可惜的是,仅仅修改游戏分辨率有可能使得游戏变成了一个小窗口,这对于电脑屏幕较小的用户简直是个灾难.但实际上,在修改游戏分辨率的同时,将电脑的系统分辨率也更改至对应的分辨率便能解决问题.

经过实验,修改分辨率是相当有效的提升帧率的方法.相较于修改游戏内的各个选项,这种方法可以做到在保证渲染的东西完整的情况下提高帧率(有的游戏将某一选项改为低就几乎变成了没有,比如角色阴影消失)

总而言之,这种方法适用于以下几种人:

- 懒得去琢磨怎么调整各个画质选项之间关系的人
- 想要用较低的配置挑战高配置的游戏的人(往往这时仅调整画质选项全低仍然低帧数)
- 希望用整体的画质下降换取各个画质选项的较高的人(人话就是不想那些阴影、体积雾等消失的人)

### 软件介绍

然而，如果在每次游戏开始，游戏结束时都去设置里调整一次分辨率未免太过于麻烦,而在平时,又没必要保持一个较低的分辨率.所以基于此,我将修改分辨率的行为做成了自动化程序.

在启动程序后,设置好游戏的路径以及游戏内外分辨率,然后便可以开始监听同时启动游戏,这时程序将会自动最小化,然后调整系统分辨率,并监听(即关注游戏的关闭与否,可能有用词不当,请见谅),等到游戏结束运行时,便将分辨率调整回正常状态,之后程序退出.

但是,有几个注意事项:

- 在运行程序前,建议关闭系统的勿扰模式,否则可能无法收到程序的提示消息

- 程序仅限于windows系统,11可用,10的话未经测试,但应该可以,本系列下其他版本应该也可行.但其他系统大概率不行

- 软件需要管理员权限,这是因为在某些路径下启动应用需要使用管理员权限.当然,如果每次都要右键启动程序也不方便,你可以参照下文中方法来设置每次都以管理员模式运行[跳转到方法](#func-1)
- 所设置的分辨率必须是可以在系统中调整的分辨率,换而言之,你需要先进入系统设置,找到分辨率设置,查看你能设置哪些分辨率,然后再填入本程序,否则将无法成功调整分辨率
- 本程序有一个配套的resize.exe文件,是用于调整分辨率的,不能调整位置,改名
- 在开始监听前,仅点击可行性测试按钮,测试本程序的功能是否正常
- 不要把程序放置于中文目录下,这可能会导致意料之外的错误
- 当你发现程序无故停止运行,那就是遇见了bug,因为在设计之初并未考虑过多,所以错误捕获没有怎么设计,可以参照以下方法来查看bug原因[跳转](#func-2)

### <a name="func-1"></a>通过快捷方式实现每一次运行都为管理员权限

1. 在程序的.exe文件上右键,选择创建快捷方式![图片1-1](https://raw.githubusercontent.com/WFengYueWuQing/AutoResolutionAdjust/main/func-1-1.png)
2. 然后右键创建的快捷方式,选择属性![图片1-2](https://raw.githubusercontent.com/WFengYueWuQing/AutoResolutionAdjust/main/func-1-2.png)
3. 在打开的页面中,选择高级,勾选用管理员身份运行,按确定关闭两个窗口![图片1-3](https://raw.githubusercontent.com/WFengYueWuQing/AutoResolutionAdjust/main/func-1-3.png)
4. 然后你就完成了,以后都可以用该快捷方式启动,无论接下来给快捷方式改名或是移动位置,都不会影响本程序,但要注意,此时就不能更改本程序的位置了,不然快捷方式将会失效

### <a name="func-2"></a>寻找程序闪退原因/bug自查/找出错误信息

1.打开程序的目录,在路径输入的位置输入cmd

2.在打开的窗口中,输入文件名称(注意后缀名要加),然后回车

3.此时程序将会自动运行,不要关闭此窗口,当程序闪退时,它将提示错误信息,请依据该信息自查问题或复制后发送给我来修复

4.此时你可以试试复刻导致闪退的操作然后修复

图示:![图示2-1](https://raw.githubusercontent.com/WFengYueWuQing/AutoResolutionAdjust/main/func-2-1.png)

### 补充

在配置菜单中的轮询间隔意思为每隔几秒检查一次游戏是否关闭,数字越小则游戏关闭后调整分辨率的反应越快,同时要注意配置菜单中的每一项都不建议填小数,可能导致意外情况

软件的可执行程序在program_executable文件夹下,请下载该文件夹

resize.exe为c++程序,其源码处于resize文件夹下

程序的主函数处于interface.py文件下

软件打算找时间再B站上发布视频,有可能要一段时间,我的账户为w_风月无情.
