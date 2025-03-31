"""全局配置项"""
import os
from collections import namedtuple

from .utils import net


_config = {
    "users": [
        "admin",
        "",
        "Admin",
        "manager",
        "hikvision",
        "user",
        "urgenon",
        "system",
        "Admin",
        "Morok",
        "User",
        "config",
        "TheJoker",
        "@MrRobotCorp3",
        "service",
        "router",
        "log",
    ],
    "passwords": [
        "admin",
        "admin12345",
        "asdf1234",
        "abc12345",
        "12345admin",
        "12345abc",
        "",
        "manager",
        "abcd1234",
        "admin123",
        "hd543211",
        "admin12345",
        "Admin123",
        "hik12345",
        "Admin@123",
        "hd5432123",
        "Admin12345",
        "admin1234",
        "Hik12345",
        "user12345",
        "admin@123",
        "abc12345",
        "12345",
        "hd5432111",
        "12345abc",
        "a1234567",
        "Admin1234",
        "Thejoker307",
        "Carl1tos",
        "hvi12345",
        "Password1",
        "@MrRobotCorp3",
    ],
    "user_agent": net.get_user_agent(),  # to save time, we only get user agent once.
    "ports": [
        80,
        81,
        82,
        83,
        84,
        85,
        88,
        8000,
        8001,
        8002,
        8003,
        8005,
        8008,
        8009,
        8080,
        8081,
        8085,
        8086,
        8088,
        8090,
        8100,
        8181,
        8300,
        8500,
        8686,
        8888,
        2051,
        9000,
        37777,
        49152,
        55555,
    ],
    # rules
    "product": {},
    "rules": set(),
    # file & dir
    "log": "log.txt",
    "not_vulnerable": "not_vulnerable.csv",
    "vulnerable": "results.csv",
    "snapshots": "snapshots",
    # wechat
    "wxuid": "",
    "wxtoken": "",
}


def get_config(args=None):
    # 指纹规则
    Rule = namedtuple('Rule', ['product', 'path', 'val'])
    with open(os.path.join(os.path.dirname(__file__), 'rules.csv'), 'r') as f:
        for line in [l.strip() for l in f if l.strip()]:
            product, path, val = line.split(',')
            _config['rules'].add(Rule(product, path, val))
            _config['product'][product] = product

    # 组装命令行获取的参数值
    if args:
        for arg in (args := vars(args)):
            # 此处不要直接 if args[arg]，因为这样会导致空字符串也为 False
            if args[arg] is not None:  
                _config[arg] = args[arg]

    Config = namedtuple('config', _config.keys())
    return Config(**_config)
