"""
使用yaml改良你之前的小游戏代码，将两个角色信息通过yaml传递进去
游戏规则：
设定一个回合制2人对打游戏。
每个人物都有hp，power，skill
hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
"""
import yaml

class Game:
    def __init__(self):
        role = yaml.safe_load(open("./game_data.yaml"))  # 读取文件，存放到role变量中
        role_list = role['default']  # role_list列表存放获取到的人物
        # 第1个人物信息
        self.fist_hp = role[role_list[0]]['hp']  # 获取第1个人的hp
        self.fist_power = role[role_list[0]]['power']  # 获取第1个人的power
        self.fist_skill = role[role_list[0]]['skill']  # 获取第1个人的skill
        # 第2个人物信息
        self.second_hp = role[role_list[1]]['hp']  # 获取第2个人的hp
        self.second_power = role[role_list[1]]['power']  # 获取第2个人的power
        self.second_skill = role[role_list[1]]['skill']  # 获取第2个人的skill

    def fight(self):
        round = 0  # 初始化打斗的回合次数
        while True:
            round += 1  # 每打斗一次，回合次数就增加一次
            if round % 3 == 0:  # 每三个回合可以使用一次skill
                self.fist_hp = self.fist_hp - self.second_power * self.second_skill
                self.second_hp = self.second_hp - self.fist_power * self.fist_skill
            else:  # 否则不使用skill
                self.fist_hp = self.fist_hp - self.second_power
                self.second_hp = self.second_hp - self.fist_power
            # 打印每个回合各自的血量
            print("fist ", self.fist_hp)
            print("second ", self.second_hp)
            # 判断谁的hp最先<=0，就打印此人输了
            if self.fist_hp <= 0:
                print("fist is lose")
                break
            elif self.second_hp <= 0:
                print("second is lose")
                break

if __name__ == '__main__':
    game = Game()  # 实例化Game
    game.fight()  # 实例对象调用fight方法