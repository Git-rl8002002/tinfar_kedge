/*
* Author   : JasonHung
* Date     : 20220211
* Update   : 20230419
* Function : JNC CB and sensor value
*/

/*
 * database  tinfar_kedge
 */ 
create database tinfar_kedge DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use tinfar_kedge;


/* 
 * alarm_sign
 */
create table alarm_sign(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(10) null,
r_month varchar(10) null,
r_day varchar(10) null,
account varchar(50) null,
k_position varchar(50) null,
k_tag_name varchar(50) null,
k_tag_val varchar(50) null,
g_tag_name varchar(50) null,
g_tag_val varchar(50) null,
sign_status varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * login_out_record
 */
create table login_out_record(
no int not null primary key AUTO_INCREMENT,
login_time datetime null,
logout_time datetime null,
a_user varchar(200) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* 
 * account
 */
create table account(
no int not null primary key AUTO_INCREMENT,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
r_time time null,
a_user varchar(200) null,
a_pwd varchar(200) null,
a_lv varchar(10) null,
a_position varchar(10) null,
a_status varchar(50) null,
a_comment text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into account (a_user , a_pwd , a_lv , a_status , a_position) VALUES('admin','1qaz#123','1','run' , 'all');
insert into account (a_user , a_pwd , a_lv , a_status , a_position) VALUES('kedge','kedge#123','2','run' , 'all');