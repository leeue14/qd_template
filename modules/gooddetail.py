#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DataProvider(object):
    #数据模块类名必须是DataProvider

    """服务配置"""
    settings = dict()
    def __init__(self, settings):
        """settings为进程配置，进程启动时，选择的config目录ini文件转换后的选项 """
        self.settings = settings

    def execute(self, data, handler=None, **param):
        #每个provider只提供唯一的一个execute方法,
        # data: 参数是前面provider的执行结果（provider可以需要前面provider的执行数据），
        # paras: url请求的参数
        # handler: 请求的handler

        d = {}
        d['w'] = handler.get_argument('w', '商品数据来了')
        d['data'] = [{"second_name": "君度的口感很独特，香醇而且丰富。既浓烈也温和，既清凉又温暖，有点儿苦涩的味道，苦中有有丝丝的甘甜。 君度的口感很独特，香醇而且丰富。如果你不嫌麻烦，还可以加点儿汤力水或者柠檬汽水、果汁调成鸡尾酒那样喝， 也很不错的呢。 君度力是娇酒很不错的酒！而且适合女士喝，很浪漫的酒",
            "product_dt": "生产日期: 2014年08月01日 至 2014年09月01日",
            "id": 3036,
            "name": "法国原装进口 Cointreau君度橙味力娇酒配制酒700ml 鸡尾酒调酒",
            "status": "0000",
            "skus": [
                {
                    "postfee": 0,
                    "id": 3026,
                    "stock": 2,
                    "status": "0000",
                    "spuid": 3036,
                    "select": {},
                    "style": "",
                    "tbid": -43745416788,
                    "realPrice": 7900,
                    "mallPrice": 7900
                }
            ],
            "style_imgs": {},
            "style_name": "",
            "category_list": [
                "饮料",
                "饮用水"
            ],
            "desc_imgs": [
                "https://img.alicdn.com/imgextra/i4/832423496/TB2TjPDcRLN8KJjSZFPXXXoLXXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i1/832423496/TB2E393a7.HL1JjSZFlXXaiRFXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i4/832423496/TB2T7Xkk4XkpuFjy0FiXXbUfFXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i4/832423496/TB2YTFfcRfM8KJjSZFrXXXSdXXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i2/832423496/TB23CR3cSJjpuFjy0FdXXXmoFXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i2/832423496/TB28DlTcR0kpuFjSsppXXcGTXXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i4/832423496/TB22StIcNXlpuFjSsphXXbJOXXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i2/832423496/TB209lTcH8kpuFjy0FcXXaUhpXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i1/832423496/TB2kJ0McSxjpuFjSszeXXaeMVXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i3/832423496/TB2H9xIcNXlpuFjSsphXXbJOXXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i3/832423496/TB2mTNzcSBjpuFjy1XdXXaooVXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i3/832423496/TB27YtIcR0kpuFjSsziXXa.oVXa_!!832423496.jpg",
                "https://img.alicdn.com/imgextra/i3/832423496/TB2LQeevd0opuFjSZFxXXaDNVXa_!!832423496.jpg"
            ],
            "country": "法国",
            "coverimgs": [
                "//gd2.alicdn.com/imgextra/i4/832423496/TB2dSjwfqmgSKJjSspiXXXyJFXa_!!832423496.jpg_50x50.jpg",
                "//gd2.alicdn.com/imgextra/i2/TB1ORfzHFXXXXXAaXXXXXXXXXXX_!!0-item_pic.jpg_50x50.jpg",
                "//gd3.alicdn.com/imgextra/i3/TB1GkDyHFXXXXXDaXXXXXXXXXXX_!!0-item_pic.jpg_50x50.jpg",
                "//gd1.alicdn.com/imgextra/i1/832423496/TB2lj8qcFXXXXciXpXXXXXXXXXX_!!832423496.jpg_50x50.jpg",
                "//gd2.alicdn.com/imgextra/i2/832423496/TB2xxRzcFXXXXbBXXXXXXXXXXXX_!!832423496.png_50x50.jpg"
            ],
            "brand_info": {
                "logo2": "",
                "create_dt": 1513493616,
                "update_dt": 1513493616,
                "id": 3,
                "logo1": "",
                "name": "启德酒水",
                "status": "0"
            },
            "attr": [
                {
                    "key": "厂名",
                    "value": [
                        "君度"
                    ]
                },
                {
                    "key": "厂址",
                    "value": [
                        "法国"
                    ]
                },
                {
                    "key": "厂家联系方式",
                    "value": [
                        "021-54881409"
                    ]
                },
                {
                    "key": "配料表",
                    "value": [
                        "水，食用酒精，白砂糖，桔皮"
                    ]
                },
                {
                    "key": "储藏方法",
                    "value": [
                        "常温避光"
                    ]
                },
                {
                    "key": "保质期",
                    "value": [
                        "3650"
                    ]
                },
                {
                    "key": "食品添加剂",
                    "value": [
                        "无"
                    ]
                },
                {
                    "key": "产品名称",
                    "value": [
                        "Cointreau/君度",
                        "力娇酒",
                        "700mL",
                        "40%Vol."
                    ]
                },
                {
                    "key": "体积(ml)",
                    "value": [
                        "700"
                    ]
                },
                {
                    "key": "品牌",
                    "value": [
                        "Cointreau/君度"
                    ]
                },
                {
                    "key": "品名",
                    "value": [
                        "力娇酒"
                    ]
                },
                {
                    "key": "酒精度数",
                    "value": [
                        "中度酒（38%≤A≤50%）"
                    ]
                },
                {
                    "key": "适用场景",
                    "value": [
                        "团圆小酌区"
                    ]
                },
                {
                    "key": "产地",
                    "value": [
                        "法国"
                    ]
                },
                {
                    "key": "包装方式",
                    "value": [
                        "包装"
                    ]
                },
                {
                    "key": "包装种类",
                    "value": [
                        "礼盒装"
                    ]
                },
                {
                    "key": "净含量",
                    "value": [
                        "700mL"
                    ]
                },
                {
                    "key": "度数",
                    "value": [
                        "40%Vol."
                    ]
                },
                {
                    "key": "年份",
                    "value": [
                        "3年"
                    ]
                },
                {
                    "key": "口味",
                    "value": [
                        "橙味"
                    ]
                }
            ]
        }
    ]
        return d
