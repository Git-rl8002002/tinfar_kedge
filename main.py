#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230419
# Function : 根基營造

import sys , time , pymysql , minimalmodbus , re , logging , requests , json
from pyModbusTCP.client import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from fpdf import *

from control.dao import * 
from gui.ui_login import *
from gui.ui_main import *


##################################################################################################################
#
# main_content
#
##################################################################################################################
class main_content(QMainWindow):
    
    ############
    # logging
    ############
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format,level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S")
    #logging.disable(logging.INFO)
    
    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.main(g_user , g_lv)
    
    #########
    # main
    #########
    def main(self , g_user , g_lv):
        
        ############
        # welcome
        ############
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)

        ###########
        # logout
        ###########
        self.ui.action_logout.triggered.connect(self.action_logout)
        
        ####################
        # account manager
        ####################
        self.ui.action_account.triggered.connect(lambda:self.account_manager(g_lv))

        if int(g_lv) == 1 or int(g_lv) == 2:

            self.ui.btn_account_cancel.clicked.connect(self.account_cancel)
            self.ui.btn_account_alter.clicked.connect(self.account_alter)
            self.ui.btn_account_add.clicked.connect(self.account_add)
            self.ui.btn_account_del.clicked.connect(self.account_del)

            self.add_account_date()
            self.add_account_lv()
            self.add_account_position()
        
        elif int(g_lv) == 3:

            ### disabled account manager 
            self.ui.groupBox.setDisabled(True)

            ### disabled account list
            self.ui.groupBox_4.setDisabled(True)
            self.ui.account_list.setColumnCount(5)
            self.ui.account_list.setHeaderLabels(['帳號','密碼','等級','位置','備註'])
            self.ui.account_list.setColumnWidth(0,120)
            self.ui.account_list.setColumnWidth(1,120)
            self.ui.account_list.setColumnWidth(2,60)
            self.ui.account_list.setColumnWidth(3,150)
            self.ui.account_list.setColumnWidth(4,300)
        
        ####################
        # sensor position
        ####################
        self.ui.action_sensor.triggered.connect(self.sensor_position)
        
    ####################
    # sensor_position
    ####################
    def sensor_position(self):

        self.ui.statusbar.showMessage("載入感測器監控")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sensor)
        
        self.a_sensor_position(g_user , g_lv)

    ######################
    # a_sensor_position
    ######################
    def a_sensor_position(self , g_user, g_lv):
        
        conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
        curr = conn.cursor()

        try:
            sql = "select a_position from account where a_user='{0}' and a_lv='{1}'".format(g_user , g_lv)
            curr.execute(sql)
            res = curr.fetchone()

            #####################################
            # all position for manager account
            #####################################
            if res[0] == 'all':
                self.kedge_jnc_cb_realtime('all')

            elif res[0] == '二重埔':
                self.kedge_jnc_cb_realtime('二重埔')


            

        except Exception as e:
            logging.info("< Error > a_sensor_position : " + str(e))
        
        finally:
            conn.commit()
            conn.close()        

    ##########################
    # kedge_jnc_cb_realtime
    ##########################
    def kedge_jnc_cb_realtime(self , position):

        if position == 'all':
            #######################
            # Device 1 : 南門市場
            #######################
            d_url_1      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_1     = requests.get(d_url_1)
            d_r_data_1   = d_data_1.text
            d_data_val_1 = json.loads(d_r_data_1)

            url_1      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_1     = requests.get(url_1)
            r_data_1   = data_1.text
            data_val_1 = json.loads(r_data_1)

            ### clear
            self.ui.kedge_cb_list_1.clear()
            
            self.ui.kedge_cb_list_1.setColumnCount(4)
            self.ui.kedge_cb_list_1.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_1.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_1.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_1.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_1.setColumnWidth(3 , 200)

            
            for val in data_val_1["Device"]:
                #logging.info(str(d_data_val_1['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_1['Connect']))
            
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_1)
                root.setText(0,str(d_data_val_1['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_1['Connect']))

            print('\n')
            
            #######################
            # Device 2 : 桃園會展
            #######################
            d_url_2      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_2     = requests.get(d_url_2)
            d_r_data_2   = d_data_2.text
            d_data_val_2 = json.loads(d_r_data_2)

            url_2      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_2     = requests.get(url_2)
            r_data_2   = data_2.text
            data_val_2 = json.loads(r_data_2)

            ### clear
            self.ui.kedge_cb_list_2.clear()
            
            self.ui.kedge_cb_list_2.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_2.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_2.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_2.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_2.setColumnWidth(3 , 200)

            for val in data_val_2["Device"]:
                #logging.info(str(d_data_val_2['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_2['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_2)
                root.setText(0,str(d_data_val_2['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_2['Connect']))
                

            print('\n')
            
            #######################
            # Device 3 : 泰山社宅
            #######################
            d_url_3      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_3     = requests.get(d_url_3)
            d_r_data_3   = d_data_3.text
            d_data_val_3 = json.loads(d_r_data_3)

            url_3      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_3     = requests.get(url_3)
            r_data_3   = data_3.text
            data_val_3 = json.loads(r_data_3)

            ### clear
            self.ui.kedge_cb_list_3.clear()
            
            self.ui.kedge_cb_list_3.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_3.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_3.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_3.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_3.setColumnWidth(3 , 200)

            for val in data_val_3["Device"]:
                #logging.info(str(d_data_val_3['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_3['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_3)
                root.setText(0,str(d_data_val_3['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_3['Connect']))

            print('\n')
            
            #####################
            # Device 4 : 二重埔
            #####################
            d_url_4      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_4     = requests.get(d_url_4)
            d_r_data_4   = d_data_4.text
            d_data_val_4 = json.loads(d_r_data_4)

            url_4      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_4     = requests.get(url_4)
            r_data_4   = data_4.text
            data_val_4 = json.loads(r_data_4)
            
            ### clear
            self.ui.kedge_cb_list_4.clear()
            
            self.ui.kedge_cb_list_4.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_4.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_4.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_4.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_4.setColumnWidth(3 , 200)

            for val in data_val_4["Device"]:
                #logging.info(str(d_data_val_4['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_4['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_4)
                root.setText(0,str(d_data_val_4['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_4['Connect']))

            print('\n')
            
            ########################
            # Device 5 : 民權東路案
            ########################
            d_url_5      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_5     = requests.get(d_url_5)
            d_r_data_5   = d_data_5.text
            d_data_val_5 = json.loads(d_r_data_5)

            url_5      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_5     = requests.get(url_5)
            r_data_5   = data_5.text
            data_val_5 = json.loads(r_data_5)

            ### clear
            self.ui.kedge_cb_list_5.clear()
            
            self.ui.kedge_cb_list_5.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_5.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_5.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_5.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_5.setColumnWidth(3 , 200)

            for val in data_val_5["Device"]:
                #logging.info(str(d_data_val_5['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_5['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_5)
                root.setText(0,str(d_data_val_5['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_5['Connect']))

            print('\n')
            
            #######################
            # Device 6 : 秀朗橋案
            #######################
            d_url_6      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_6     = requests.get(d_url_6)
            d_r_data_6   = d_data_6.text
            d_data_val_6 = json.loads(d_r_data_6)

            url_6      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_6     = requests.get(url_6)
            r_data_6   = data_6.text
            data_val_6 = json.loads(r_data_6)

            ### clear
            self.ui.kedge_cb_list_6.clear()
            
            self.ui.kedge_cb_list_6.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_6.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_6.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_6.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_6.setColumnWidth(3 , 200)

            for val in data_val_6["Device"]:
                #logging.info(str(d_data_val_6['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_6['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_6)
                root.setText(0,str(d_data_val_6['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_6['Connect']))

            print('\n')

            #####################
            # Device 7 : 裕毛屋
            #####################
            d_url_7      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_7     = requests.get(d_url_7)
            d_r_data_7   = d_data_7.text
            d_data_val_7 = json.loads(d_r_data_7)

            url_7      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_7     = requests.get(url_7)
            r_data_7   = data_7.text
            data_val_7 = json.loads(r_data_7)

            ### clear
            self.ui.kedge_cb_list_7.clear()
            
            self.ui.kedge_cb_list_7.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_7.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_7.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_7.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_7.setColumnWidth(3 , 200)

            for val in data_val_7["Device"]:
                #logging.info(str(d_data_val_7['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_7['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_7)
                root.setText(0,str(d_data_val_7['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_7['Connect']))

            print('\n')

            #######################
            # Device 8 : 後龍大橋
            #######################
            d_url_8      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_8     = requests.get(d_url_8)
            d_r_data_8   = d_data_8.text
            d_data_val_8 = json.loads(d_r_data_8)

            url_8      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_8     = requests.get(url_8)
            r_data_8   = data_8.text
            data_val_8 = json.loads(r_data_8)

            ### clear
            self.ui.kedge_cb_list_8.clear()
            
            self.ui.kedge_cb_list_8.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_8.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_8.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_8.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_8.setColumnWidth(3 , 200)

            for val in data_val_8["Device"]:
                #logging.info(str(d_data_val_8['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_8['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_8)
                root.setText(0,str(d_data_val_8['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_8['Connect']))

            print('\n')
            
            ################################
            # Device 9 : 嘉義車站C611世賢南
            ################################
            d_url_9      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_9     = requests.get(d_url_9)
            d_r_data_9   = d_data_9.text
            d_data_val_9 = json.loads(d_r_data_9)

            url_9      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_9     = requests.get(url_9)
            r_data_9   = data_9.text
            data_val_9 = json.loads(r_data_9)

            ### clear
            self.ui.kedge_cb_list_9.clear()
            
            self.ui.kedge_cb_list_9.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_9.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_9.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_9.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_9.setColumnWidth(3 , 200)

            for val in data_val_9["Device"]:
                #logging.info(str(d_data_val_9['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_9['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_9)
                root.setText(0,str(d_data_val_9['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_9['Connect']))

            print('\n')

            ##################################
            # Device 10 : 嘉義車站C611宏仁女中
            ##################################
            d_url_10      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_10     = requests.get(d_url_10)
            d_r_data_10   = d_data_10.text
            d_data_val_10 = json.loads(d_r_data_10)

            url_10      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_10     = requests.get(url_10)
            r_data_10   = data_10.text
            data_val_10 = json.loads(r_data_10)

            ### clear
            self.ui.kedge_cb_list_10.clear()
            
            self.ui.kedge_cb_list_10.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_10.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_10.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_10.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_10.setColumnWidth(3 , 200)

            for val in data_val_10["Device"]:
                #logging.info(str(d_data_val_10['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_10['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_10)
                root.setText(0,str(d_data_val_10['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_10['Connect']))

            print('\n')

            ##################################
            # Device 11 : 嘉義車站C612嘉北車站
            ##################################
            d_url_11      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_11     = requests.get(d_url_11)
            d_r_data_11   = d_data_11.text
            d_data_val_11 = json.loads(d_r_data_11)

            url_11      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_11     = requests.get(url_11)
            r_data_11   = data_11.text
            data_val_11 = json.loads(r_data_11)

            ### clear
            self.ui.kedge_cb_list_11.clear()
            
            self.ui.kedge_cb_list_11.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_11.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_11.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_11.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_11.setColumnWidth(3 , 200)

            for val in data_val_11["Device"]:
                #logging.info(str(d_data_val_11['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_11['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_11)
                root.setText(0,str(d_data_val_11['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_11['Connect']))

            print('\n')
            
            ###############################
            # Device 12 : 嘉義車站C612北興
            ###############################
            d_url_12      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_12     = requests.get(d_url_12)
            d_r_data_12   = d_data_12.text
            d_data_val_12 = json.loads(d_r_data_12)

            url_12      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_12     = requests.get(url_12)
            r_data_12   = data_12.text
            data_val_12 = json.loads(r_data_12)

            ### clear
            self.ui.kedge_cb_list_12.clear()
            
            self.ui.kedge_cb_list_12.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_12.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_12.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_12.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_12.setColumnWidth(3 , 200)

            for val in data_val_12["Device"]:
                #logging.info(str(d_data_val_12['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_12['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_12)
                root.setText(0,str(d_data_val_12['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_12['Connect']))

            print('\n')
            
            #############################
            # Device 13 : 台南車站一號口
            #############################
            d_url_13      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_13     = requests.get(d_url_13)
            d_r_data_13   = d_data_13.text
            d_data_val_13 = json.loads(d_r_data_13)

            url_13      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_13     = requests.get(url_13)
            r_data_13   = data_13.text
            data_val_13 = json.loads(r_data_13)

            ### clear
            self.ui.kedge_cb_list_13.clear()
            
            self.ui.kedge_cb_list_13.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_13.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_13.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_13.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_13.setColumnWidth(3 , 200)

            for val in data_val_13["Device"]:
                #logging.info(str(d_data_val_13['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_13['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_13)
                root.setText(0,str(d_data_val_13['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_13['Connect']))

            print('\n')

            #############################
            # Device 14 : 台南車站四號口
            #############################
            d_url_14      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_14     = requests.get(d_url_14)
            d_r_data_14   = d_data_14.text
            d_data_val_14 = json.loads(d_r_data_14)

            url_14      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_14     = requests.get(url_14)
            r_data_14   = data_14.text
            data_val_14 = json.loads(r_data_14)

            ### clear
            self.ui.kedge_cb_list_14.clear()
            
            self.ui.kedge_cb_list_14.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_14.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_14.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_14.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_14.setColumnWidth(3 , 200)

            for val in data_val_14["Device"]:
                #logging.info(str(d_data_val_14['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_14['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_14)
                root.setText(0,str(d_data_val_14['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_14['Connect']))
        
        elif position == '二重埔':
            
            #####################
            # Device 4 : 二重埔
            #####################
            d_url_4      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
            d_data_4     = requests.get(d_url_4)
            d_r_data_4   = d_data_4.text
            d_data_val_4 = json.loads(d_r_data_4)

            url_4      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
            data_4     = requests.get(url_4)
            r_data_4   = data_4.text
            data_val_4 = json.loads(r_data_4)
            
            ### clear
            self.ui.kedge_cb_list_4.clear()
            
            self.ui.kedge_cb_list_4.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:off,1:on)'])
            self.ui.kedge_cb_list_4.setColumnWidth(0 , 180)
            self.ui.kedge_cb_list_4.setColumnWidth(1 , 180)
            self.ui.kedge_cb_list_4.setColumnWidth(2 , 100)
            self.ui.kedge_cb_list_4.setColumnWidth(3 , 200)

            for val in data_val_4["Device"]:
                #logging.info(str(d_data_val_4['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_4['Connect']))
                
                root  = QTreeWidgetItem(self.ui.kedge_cb_list_4)
                root.setText(0,str(d_data_val_4['DeviceName']))
                root.setText(1,str(val['TagName']))
                root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
                root.setText(3,str(d_data_val_4['Connect']))

            print('\n')

    ##################
    # action_logout
    ##################
    def action_logout(self):
        
        self.ui.statusbar.showMessage("登出")

        #####################
        # close main form
        #####################
        self.close()

        self.login = main_login()
        self.login.show()

    ################
    # account_del
    ################
    def account_del(self):

        ### variables
        a_user = self.ui.account_user.text()
        a_pwd  = self.ui.account_pwd.text()
        a_lv   = self.ui.account_lv.text()
        a_position = self.ui.account_position.text()
        a_comment  = self.ui.account_comment.toPlainText()
        
        conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
        curr = conn.cursor()

        try:
            sql = "update account set a_status='stop' where a_user='{0}'".format(a_user)
            res = curr.execute(sql)

            if res:
                QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 刪除成功.'))
                
                ##########
                # clear
                ##########
                self.account_cancel()

            else:
                QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 刪除失敗.'))

        except Exception as e:
            logging.info("< Error > account del : " + str(e))
        
        finally:
            conn.commit()
            conn.close()

        ########################
        # reload account list
        ########################
        self.account_list(g_lv)    
        

    ################
    # account_add
    ################
    def account_add(self):
        
        ### variables
        a_user = self.ui.account_user.text()
        a_pwd  = self.ui.account_pwd.text()
        a_lv   = self.ui.account_lv.text()
        a_position = self.ui.account_position.text()
        a_comment  = self.ui.account_comment.toPlainText()

        if len(a_user) == 0:
            QMessageBox.information(self , '訊息' , str('帳號不能空白 !'))
        elif len(a_pwd) == 0:
            QMessageBox.information(self , '訊息' , str('密碼不能空白 !'))
        elif len(a_lv) == 0:   
            QMessageBox.information(self , '訊息' , str('等級不能空白 !')) 
        elif len(a_position) == 0:
            QMessageBox.information(self , '訊息' , str('位置不能空白 !'))    
        else:
            ### record time
            r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_year  = time.strftime("%Y" , time.localtime())
            r_month = time.strftime("%m" , time.localtime())
            r_day   = time.strftime("%d" , time.localtime()) 
            
            conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
            curr = conn.cursor()

            try:
                sql = "insert into account (r_time , r_year , r_month , r_day , a_user , a_pwd , a_lv , a_position , a_comment , a_status) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(r_time , r_year , r_month , r_day , a_user , a_pwd , a_lv , a_position , a_comment , 'run')
                res = curr.execute(sql)

                if res:
                    QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 新增成功.'))
                    
                    ##########
                    # clear
                    ##########
                    self.account_cancel()

                else:
                    QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 新增失敗.'))

            except Exception as e:
                logging.info("< Error > account add : " + str(e))
            
            finally:
                conn.commit()
                conn.close()

            ########################
            # reload account list
            ########################
            self.account_list(g_lv)

    #########################
    # add_account_position
    #########################
    def add_account_position(self):

        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y_%m" , time.localtime())
        r_day   = time.strftime("%d" , time.localtime()) 

        conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
        curr = conn.cursor()

        try:
            sql = "select distinct s_content from {0}".format(r_month)
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.account_position2.addItem("")
            self.ui.account_position2.addItem("all")

            for val in res:
                self.ui.account_position2.addItem(val[0])
            
            self.ui.account_position2.currentIndexChanged.connect(self.change_account_position)

        except Exception as e:
            logging.info("< Error > add_account_position : " + str(e))
        
        finally:
            conn.commit()
            conn.close()
    
    ############################
    # change_account_position
    ############################
    def change_account_position(self):
        val = self.ui.account_position2.currentText()
        self.ui.account_position.setText(val)
    
    ###################
    # add_account_lv
    ###################
    def add_account_lv(self):
        
        conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
        curr = conn.cursor()

        try:
            sql = "select distinct a_lv from account where a_lv != 1 order by a_lv desc"
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.account_lv2.addItem("")

            for val in res:
                self.ui.account_lv2.addItem(val[0])
            
            self.ui.account_lv2.currentIndexChanged.connect(self.change_account_lv)

        except Exception as e:
            logging.info("< Error > add_account_lv : " + str(e))
        
        finally:
            conn.commit()
            conn.close()

    ######################
    # change_account_lv
    ######################
    def change_account_lv(self):
        val = self.ui.account_lv2.currentText()
        self.ui.account_lv.setText(val)

    #####################
    # add_account_date
    #####################
    def add_account_date(self):
        
        self.ui.b_account_date2.setDisplayFormat("yyyy-MM-dd")
        self.ui.b_account_date2.setDate(QDate.currentDate())
        self.ui.b_account_date2.dateChanged.connect(self.sell_account_date_val)

        r_day = time.strftime("%Y-%m-%d" , time.localtime())
        self.ui.b_account_date.setText(r_day)
    
    ##########################
    # sell_account_date_val
    ##########################
    def sell_account_date_val(self):
        date_val = self.ui.b_account_date2.text()
        self.ui.b_account_date.setText(date_val)

    ##################
    # account_alter
    ##################
    def account_alter(self):
        
        ### variables
        a_user = self.ui.account_user.text()
        a_pwd  = self.ui.account_pwd.text()
        a_lv   = self.ui.account_lv.text()
        a_position = self.ui.account_position.text()
        a_comment  = self.ui.account_comment.toPlainText()
        
        conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
        curr = conn.cursor()

        try:
            sql = "update account set a_pwd='{0}' , a_lv='{1}' , a_position='{2}' , a_comment='{3}' where a_user='{4}'".format(a_pwd , a_lv , a_position , a_comment , a_user)
            res = curr.execute(sql)

            if res:
                QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 修改成功.'))
                
                ##########
                # clear
                ##########
                self.account_cancel()

            else:
                QMessageBox.information(self , '訊息' , str('帳號 ' + a_user + ' , 修改失敗.'))

        except Exception as e:
            logging.info("< Error > account alter : " + str(e))
        
        finally:
            conn.commit()
            conn.close()

        ########################
        # reload account list
        ########################
        self.account_list(g_lv)
        

    ###################
    # account_cancel
    ###################
    def account_cancel(self):
        
        ### clear
        self.ui.account_user.clear()
        self.ui.account_pwd.clear()
        self.ui.account_lv.clear()
        self.ui.account_position.clear()
        self.ui.account_comment.clear()

    ####################
    # account_manager
    ####################
    def account_manager(self , g_lv):
        
        self.ui.statusbar.showMessage("載入帳號管理")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_account)
        self.account_list(g_lv)
        
    #################
    # account_list
    #################
    def account_list(self , g_lv):
        
        if int(g_lv) == 1 or int(g_lv) == 2:
            
            ### clear
            self.ui.account_list.clear()
            self.ui.account_list2.clear()

            #############
            # a_lv = 2
            #############    
            conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
            curr = conn.cursor()

            try:
                sql = "select a_user , a_pwd , a_lv , a_position , a_comment from account where a_lv != 1 and a_lv = 2 and a_status='run' order by a_lv desc"
                curr.execute(sql)
                res = curr.fetchall()

                self.ui.account_list.setColumnCount(5)
                self.ui.account_list.setHeaderLabels(['帳號','密碼','等級','位置','備註'])
                self.ui.account_list.setColumnWidth(0,120)
                self.ui.account_list.setColumnWidth(1,120)
                self.ui.account_list.setColumnWidth(2,60)
                self.ui.account_list.setColumnWidth(3,150)
                self.ui.account_list.setColumnWidth(4,300)
                
                for val in res:
                    root = QTreeWidgetItem(self.ui.account_list)    
                    root.setText(0,str(val[0]))
                    root.setText(1,str(val[1]))
                    root.setText(2,str(val[2]))
                    root.setText(3,str(val[3]))
                    root.setText(4,str(val[4]))

                ### double click account list loading data
                self.ui.account_list.doubleClicked.connect(self.doubleclick_account_list)

            except Exception as s:
                logging.info("< Error > account list : " + str(e))

            finally:
                conn.commit()
                conn.close()
            
            #############
            # a_lv = 3
            #############
            conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
            curr = conn.cursor()
            try:
                sql = "select a_user , a_pwd , a_lv , a_position , a_comment from account where a_lv = 3  and a_status='run' order by a_lv desc"
                curr.execute(sql)
                res = curr.fetchall()

                self.ui.account_list2.setColumnCount(5)
                self.ui.account_list2.setHeaderLabels(['帳號','密碼','等級','位置','備註'])
                self.ui.account_list2.setColumnWidth(0,120)
                self.ui.account_list2.setColumnWidth(1,120)
                self.ui.account_list2.setColumnWidth(2,60)
                self.ui.account_list2.setColumnWidth(3,150)
                self.ui.account_list2.setColumnWidth(4,300)
                
                for val in res:
                    root = QTreeWidgetItem(self.ui.account_list2)    
                    root.setText(0,str(val[0]))
                    root.setText(1,str(val[1]))
                    root.setText(2,str(val[2]))
                    root.setText(3,str(val[3]))
                    root.setText(4,str(val[4]))

                ### double click account list loading data
                self.ui.account_list2.doubleClicked.connect(self.doubleclick_account_list2)

            except Exception as s:
                logging.info("< Error > account list : " + str(e))

            finally:
                conn.commit()
                conn.close()
        
        elif int(g_lv) == 3:
            self.ui.account_list.setDisabled(True)
            self.ui.account_list.setColumnCount(5)
            self.ui.account_list.setHeaderLabels(['帳號','密碼','等級','位置','備註'])
            self.ui.account_list2.setColumnCount(5)
            self.ui.account_list2.setHeaderLabels(['帳號','密碼','等級','位置','備註'])

    #############################
    # doubleclick_account_list2
    #############################
    def doubleclick_account_list2(self):
        item  = self.ui.account_list2.currentItem()
        a_user = item.text(0)
        a_pwd  = item.text(1)
        a_lv   = item.text(2)
        a_position = item.text(3)
        a_comment  = item.text(4)
        
        ### double click loading account data
        self.ui.account_user.setText(a_user)
        self.ui.account_pwd.setText(a_pwd)
        self.ui.account_lv.setText(a_lv)
        self.ui.account_position.setText(a_position)
        self.ui.account_comment.setText(a_comment)

    #############################
    # doubleclick_account_list
    #############################
    def doubleclick_account_list(self):
        item  = self.ui.account_list.currentItem()
        a_user = item.text(0)
        a_pwd  = item.text(1)
        a_lv   = item.text(2)
        a_position = item.text(3)
        a_comment  = item.text(4)
        
        ### double click loading account data
        self.ui.account_user.setText(a_user)
        self.ui.account_pwd.setText(a_pwd)
        self.ui.account_lv.setText(a_lv)
        self.ui.account_position.setText(a_position)
        self.ui.account_comment.setText(a_comment)


##################################################################################################################
#
# login
#
##################################################################################################################
class main_login(QFrame):
    
    ############
    # logging
    ############
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format,level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S")
    #logging.disable(logging.INFO)

    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.login_init()

    ###############
    # init_login
    ###############
    def login_init(self):

        #####################
        # btn login submit
        #####################
        self.ui.btn_submit.clicked.connect(self.login_submit)

        ######################
        # btn cancel submit
        ######################
        self.ui.btn_cancel.clicked.connect(self.cancel_submit)
        
    ##################
    # cancel submit
    ##################
    def cancel_submit(self , event):
        QApplication.closeAllWindows()

    #################
    # login_submit
    #################
    def login_submit(self):
        
        ### user and pwd
        self.user = self.ui.login_user.text()
        self.pwd  = self.ui.login_pwd.text()

        if len(self.user) == 0 or len(self.pwd) == 0:
            self.ui.login_msg.clear()
            self.ui.login_msg.setStyleSheet('color:red;')
            self.ui.login_msg.setText('登入 帳號 or 密碼不能空白 !')

        else:
            
            conn = pymysql.connect(host=kedge_connect['host'],port=kedge_connect['port'],user=kedge_connect['user'],passwd=kedge_connect['pwd'],database=kedge_connect['db'],charset=kedge_connect['charset'])    
            curr = conn.cursor()
            
            try:
                sql = "select a_user , a_lv from account where a_user='{0}' and a_pwd='{1}' and a_status='run'".format(self.user , self.pwd)
                curr.execute(sql)
                res = curr.fetchone()
                
                if len(res[0]) > 0:
                    
                    try:
                        ### login record
                        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                        sql2   = "insert into login_out_record(login_time , a_user) value('{0}','{1}')".format(r_time , res[0])
                        curr.execute(sql2)

                        ### global variable
                        global g_user , g_lv
                        g_user = res[0]
                        g_lv = res[1]
                        
                        ### login successful    
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setStyleSheet('color:blue;')
                        self.ui.login_msg.setText('登入成功 , 馬上進入主頁')

                        #####################
                        # close login form
                        #####################
                        self.close()
                        
                        #####################
                        # new main content
                        #####################
                        self.main = main_content()
                        self.main.show()
                        
                    except Exception as e:
                        self.ui.login_msg.setText('< Error > ' + str(e))
                        logging.info('< Error > '+ str(e))

                    finally:
                        pass

            except Exception as e:
                self.ui.login_msg.clear()
                self.ui.login_msg.setStyleSheet('color:red;')
                self.ui.login_msg.setText('帳號  : ' + self.user + ' 沒有註冊過，無此帳號 !')

            finally:
                conn.commit()
                conn.close()

##################################################################################################################
#
# start
#
##################################################################################################################
if __name__ == '__main__':
    app   = QApplication(sys.argv)
    login = main_login()
    login.show()
    sys.exit(app.exec())
    

