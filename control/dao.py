#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230310
# Update   : 20230420
# Version  : 1.0
# Function : 根基營造 JNC Server get sensor value

###############
#
# JNC Server
#
###############
jnc_server = {'host':'59.125.238.217' , 'port':587 , 'cb-1':1 , 'cb-1_1':'0x0000' , 'cb-1_2':'0x0001' , 'cb-1_3':'0x0002'}

#################
#
# Tinfar_kedge
#
#################
kedge_connect = {'host':'61.220.205.143' , 'port':5306,'user':'backup' , 'pwd':'SLbackup#123' , 'db':'tinfar_kedge' , 'charset':'utf8'}

#############
#
# txt path
#
#############
txt_path = {'linux_txt_path':'/var/www/html/medicine/txt/' , 'linux_pdf_path':'/var/www/html/medicine/pdf/nas/backup_record.txt'}

