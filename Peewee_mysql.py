#!/usr/bin/python3
##peewee ORM

from peewee import *

import pymysql

db = MySQLDatabase('test', user ='root', password= '123456',host='localhost')

class BaseModel(Model):
	"""docstring for BaseModel"""
	class Meta:
		database = db


class Course(BaseModel):
	id = PrimaryKeyField()
	title = CharField(null = False)
	period = IntegerField()

	class Meta: ###定义数据库的表名
		order_by = ('title', )
		db_table = 'course'

class Teacher(BaseModel):
	id = PrimaryKeyField()
	name = CharField(null = False)
	gender = BooleanField()
	address = CharField()
	course_id = ForeignKeyField(Course, to_field = "id", related_name="course")



	class Meta:
		order_by = ('name',)
		db_table = 'teacher'

Course.create_table()###创建表

Teacher.create_table()

##新增行
# Course.create(id = 1, title = '大学英语', period = 64)
# Course.create(id = 2, title = '高等数学', period = 128)
# Course.create(id = 3, title = '数据结构', period = 64)

# Teacher.create(name = '张三', gender = True, address='...', course_id=1)

# Teacher.create(name = '曹强', gender = True, address='北京市海淀区北京邮电大学', course_id=2)



###查询一行

# record = Course.get(Course.title =='大学英语')
# print("课程%s, 学时%d" % (record.title, record.period))


# ####更新
# record.period=200
# record.save()


# # ###删除
# record.delete_instance()

# ###查询所有的记录

courses = Course.select()
for p in courses:
	print(p.id, p.title, p.period)

# ###带条件查询,并将结果按period字段倒序排序

# courses = Course.select().where(Course.id <10).order_by(Course.period.desc())
# for p in courses:
# 	print(p.id, p.title, p.period)
# ####统计所有课程的平均课时

# total = Course.select(fn.Avg(Course.period).alias('avg_period'))
# for t in total:
# 	print(t.avg_period)
# ###更新多个记录

# Course.update(period = 400).where(Course.id > 2).execute()
# ###多表连接操作。
Record = Course.select().join(Teacher).where(Teacher.gender==True)
for t in Record:
	print(t)




