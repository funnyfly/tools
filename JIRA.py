#!/user/bin/python
#-*-coding:utf-8-*-
from jira import JIRA
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

jira = JIRA("http://192.168.6.71:8888", basic_auth=('zhaofengyong','zhaofengyong'))

projects = jira.projects()
#查询可用的项目
# for project in projects:
#    print project,project.key

#查询任务类型：判断是否是子任务
#issue.fields.issuetype

# subtasks = issue.fields.subtasks
# print subtasks

#查询指定issue
issue = jira.issue('OPP-1712')
print issue.fields.timespent
#按冲刺查询任务
# issue = jira.search_issues("sprint='[COM]2018.7.2-2018.7.7'")
#print issue
# for i in issue:
    # print i.fields.status  #任务状态
    # print i.fields.assignee #经办人
    # print i.fields.summary #任务概要
    # print i.fields.subtasks #子任务
    # print i.fields.description  #任务内容
    # print i.fields.timeestimate #剩余时间
    # print issue.fields.timeoriginalestimate  #预估时间
    # print issue.fields.timespent  #实际工作时间