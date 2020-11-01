from flask_shop.menu import menu,menu_api
from flask_shop import models,db
from flask import request
from flask_restful import Resource
from flask_shop.until.message import to_dict_msg

class Menu(Resource):
    def get(self):
        type_ = request.args.get('type')
        menu_list = []
        #获取数据并将数据填冲到menu——list中
        if type_ == 'list':
            #获取数据并将数据填冲到menu——list中
            mu = models.Menu.query.filter(models.Menu.level != 0).all()
            for m in mu:
                print(type(m))
                menu_list.append(m.to_dict())
        else:
            mu = models.Menu.query.filter(models.Menu.level == 1).all()
            for m in mu:
                #获取一级菜单转成json
                first_mu = m.to_dict()
                #给二级菜单创建保存容器
                first_mu['children'] = []
                for sm in m.children:
                    #获取2级菜单转成接送
                    secd_dict = sm.to_dict()
                    #给2级菜单创建保存容器，并把3级菜单数据加进来
                    secd_dict['children'] = sm.get_children_list()
                    #把二级菜单加到一级的children列表中
                    first_mu['children'].append(secd_dict)
                #把一级菜单加到根列表中
                menu_list.append(first_mu)
        return to_dict_msg(200,data=menu_list)

menu_api.add_resource(Menu,'/menu')