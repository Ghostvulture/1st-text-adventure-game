prince_name=input('欢迎来到游戏。你的名字是：')
princess_name=input('你希望公主的名字是：')

def start_game():
    print(f"你是一名王子，名叫{prince_name}。你生活在一个中世纪的王国。一天你约心爱的公主{princess_name}一起吃牛心管，却迟迟不见她的身影。原来她和她的电瓶车一起被恶龙劫持了，被困在恶龙的巢穴里。你的任务是救出公主")
    print("恶龙经营着一个世界500强的绑架集团。他在巢穴外围设置了两道防线。你需要在突破防线的同时增长属性点数，才能成功救出公主。")
    print("让我们开始吧。")


def one_tool():
    print("你驾驶电瓶车到了第一道关卡前。这里的集市有三家店铺。要到哪里逛逛吗？")
    print("1.打铁铺")
    print("2.药剂铺")
    print("3.占卜店")

def one_roll():
    global choice0
    print(f"你继续来到了关卡。只见三个巨大的长西瓜漂浮在空中，带着咄咄逼人的眼睛和嘴。朱唇轻启，3D立体环绕音立马在你脑内纵横鼓荡：“家人们谁懂啊，今天遇到一个……")
    print(f"1.跳一段“鸡你太美”，用纯正的普信震慑对手")
    print(f"2.一动不动，假装自己是压缩毛巾")
    print(f"3.{choice0}")#记得引入一个变量

def two_roll():
    print("你马不停蹄地来到了第二道防线。在由无数0和1组成的拱廊中间，漂浮着数学之神的使者：Robin Gang。与编者激烈讨论后，他放弃了给你出微积分题的想法，给你出了一道较简单的数学题。请听题：")
    print("1=5")
    print("2=25")
    print("3=625")
    print("4=3125")
    print("5=?")
    print("1.答案是1")
    print("2.和他说：你这考的啥，都不是数学")
    print(f"3.{choice0}")
def two_tool():
    print("越过第二道防线，你来到了文字小铺。你需要些什么呢？")
    print("1.紫色内裤")
    print("2.血橙")
    print("3.字序转换器")

def three_roll():
    print("你成功来到了恶龙的堡垒。打开门，恶龙向你扑来。你会怎么做？")
    print("1.觉得恶龙不可能向你扑来，无动于衷")
    print("2.被恶龙的庞大吓得手足无措，直接开摆")
    print(f"3.{choice0}")
    
def good_ending():
    print("一时间，似天崩地裂，世界混沌。迷雾散去，你发现公主驾驶着温顺的恶龙向你走来。原来，公主是一名骑士，被拐后很快驯服了恶龙。刚才的恶龙是公主用3D投影仪1：1仿真的（参见蜘蛛侠2反派）。这一切，是公主对王子的试炼。")
    print("恭喜你，你是合格的王子。让本骑士带你驾驶恶龙游荡四方吧！")
    print("he：公主和王子驾驶恶龙遨游宇宙，游历四方。")

def bad_ending():
    print("一时间，似天崩地裂，世界混沌。迷雾散去，你发现公主驾驶着温顺的恶龙向你走来。原来，公主是一名骑士，被拐后很快驯服了恶龙。刚才的恶龙是公主用3D投影仪1：1仿真的（参见蜘蛛侠2反派）。这一切，是公主对王子的试炼。")
    print("想要和本公主一起去冒险？恐怕你的资历还不够。")
    
def end_game():
    print("游戏结束。")
    return
    
    #主线剧情


def choice1_1():
    print("打铁铺里，南无加特林菩萨刚刚物理超度了企图把他放进火炉里融化成黄金的打铁师傅。")
    print("南无加特林菩萨看你长的比较亲切，决定把随身携带的加特林赠送给你。")
def choice1_2():
    print("走进药剂铺，你发现你被骗了。")
    print("这里是欧洲魔法大陆的韦斯莱玩笑商店，但是偏偏什么都缺货，只有迷情剂。你只好购买了迷情剂。")
def choice1_3():
    print("占卜师用周易给你算了一卦（她说周易更适合中国宝宝体质），说你最近能量不足。")
    print("她逼迫你学社会摇来积攒三界能量。")


def choice2_1():
    print("西瓜觉得这是烂梗，还没它新，但是抵不住经典永流传的力量自爆了。你通过了。")
def choice2_2():
    print("西瓜们舍不得牺牲同伴获取汁水让你变答辩膏，无奈离开了。你通过了，但是你变成了压缩毛巾。")
def choice2_31():
    print("西瓜们裂开来，你通过了。你开始吃西瓜。")
def choice2_32():
    print("你的喷头对准了自己而你没注意，喷错方向了。")
    print("结局：你疯狂爱上了手中的迷情剂，展开了一段禁忌之恋。")
def choice2_33():
    print("西瓜们觉得很难顶，离开了。果然，够抽象的人运气不会太差。")


def choice3_1():
    print("恭喜你答对了！没办法，他们只好把你放了。")
def choice3_2():
    print("虽然这是脑筋急转弯，但你不尊重他。他恼羞成怒。你没有通过关卡。")
def choice3_31():
    print("他的身体被你轰出一个大洞。正当你自鸣得意之时，无数0和1飞出，填补上了他的伤口。数学之神无限于凡人之身。")
    print("结局：你惹怒了数学之神，它强迫你重新做一遍一轮和二轮用书。你被困在了去年8月。")
def choice3_32():
    print("你成功喷到了Robin Gan。但是你忘了他的成名作吗？")
    print("他开始在trap beat 中吟诵：I won’t even take a glance, I would rather do my math……”真正热爱数学者怎能被异性所动！")
    print("结局：你受他的影响，深耕数学原野，把公主忘记了。")
def choice3_33():
    print("Robin Gan在你规律的抽搐中感悟到斐波那契数列之美，觉得你的数学直觉远超这题，恭敬地把你放了。")
    print("但是什么都用社会摇解决，代价又是什么呢？")


def choice4_1():
    print("你穿上了紫色内裤。触发BUFF“紫腚能行”")
def choice4_2():
    print("触发俗语“菌叫橙死，橙不能不死”。你变成了云南菌子。")
def choice4_3():
    print("你获得了字序转换器。你把公主转换成了主公。你变成了关羽。完蛋了。")
    print("结局：中世纪的世界崩坏了，你和主公飞升到那遥远的东方古国，完成他们的故事。")



#option1='用加特林扫射'
#option2='将迷情剂向他们抛去'
#option3='跳一段社会摇'
#定义

def show_scene(description, options):
    print(description)
    print_options(options)

# 替换原来的每个关卡展示部分

def make_choice(options):
    choice = input("你的选择是：")
    while choice not in options:
        print("选择无效，请重新选择。")
        choice = input("你的选择是：")
    return choice

# 替换原来的每个关卡选择部分


def print_options(options):
    for i, option in enumerate(options):
        print(f"{i+1}.{option}")

# 替换原来的打印选项列表部分

print_options(["打铁铺", "药剂铺", "占卜店"])





start_game()

show_scene("你驾驶电瓶车到了第一道关卡前。这里的集市有三家店铺。要到哪里逛逛吗？", ["打铁铺", "药剂铺", "占卜店"])
choice1 = make_choice(["1", "2", "3"])
print_options(["打铁铺", "药剂铺", "占卜店"])





one_roll()
choice2=input('你的选择是：')
if choice2=="1":
    choice2_1()
elif choice2 =="2":
    choice2_2()
elif choice2=="3":
    if choice1=="1":
        choice2_31()
    elif choice1=="2":
        choice2_32()
        end_game()
    elif choice1=="3":
        choice2_33()

else:
    print("选择无效，请重新选择。")
    one_roll()


two_roll()
choice3=input('你的选择是：')
if choice3=="1":
    choice3_1()
elif choice3 =="2":
    choice3_2()
elif choice3=="3":
    if choice1=="1":
        choice3_31()
        end_game()
    elif choice2=="2":
        choice3_32()
        end_game()
    elif choice3=="3":
        choice3_33()
else:
    print("选择无效，请重新选择。")
    two_roll()


two_tool()
choice4=input('你的选择是：')
if choice4=="1":
    choice4_1()
elif choice4 =="2":
    choice4_2()
elif choice4=="3":
    choice4_3()
    end_game()
    
else:
    print("选择无效，请重新选择。")


three_roll()
choice5=input('你的选择是：')
if choice5=="2":
    bad_ending()
    end_game()
elif choice5 =="1":
    good_ending()
elif choice5=="3":
    good_ending()
    end_game()

else:
    print("选择无效，请重新选择。")
    three_roll()
    


