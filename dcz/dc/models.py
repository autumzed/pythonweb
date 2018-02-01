#-*-coding:utf-8-*- 
from django.db import models

# Create your models here.
from django.db import models
def decode(info):
    return info.decode('utf-8')
# class product(models.Model):
#     product = models.CharField(max_length=300, verbose_name="书目/课", null=False, blank=False)
#
#     # 预留字段
#     devf1 = models.CharField(max_length=300, null=True, blank=True)
#
#     # 预留字段
#     devf2 = models.CharField(max_length=300, null=True, blank=True)
#
#     # 预留字段
#     devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)


class hrmresource(models.Model):
    zyear = models.CharField(max_length=300, verbose_name="报考年份", null=False, blank=False)

    zdate = models.CharField(max_length=300, verbose_name="报名时间", null=False, blank=False)

    schoolname = models.CharField(max_length=300, verbose_name="校名称", null=False, blank=False)

    zcity = models.CharField(max_length=300, verbose_name="市", null=False, blank=False)

    uname = models.CharField(max_length=300, verbose_name="学员姓名", null=False, blank=False)

    tel = models.CharField(max_length=300, verbose_name="学员手机", null=True, blank=True)

    uaddress = models.CharField(max_length=300, verbose_name="学员地址", null=True, blank=True)

    zpostcode = models.CharField(max_length=300, verbose_name="邮编", null=True, blank=True)

    ubank = models.CharField(max_length=300, verbose_name="银行", null=True, blank=True)

    uid = models.CharField(max_length=300, verbose_name="身份证号", null=False, blank=False)

    uqq = models.CharField(max_length=300, verbose_name="QQ邮箱", null=True, blank=True)

    uaccount = models.CharField(max_length=300, verbose_name="账号", null=True, blank=True)

    upws = models.CharField(max_length=300, verbose_name="密码", null=True, blank=True)

    uwechat = models.CharField(max_length=300, verbose_name="微信号", null=True, blank=True)

    denum = models.CharField(max_length=300, verbose_name="行政代码", null=True, blank=True)

    idcopy = models.CharField(max_length=300, verbose_name="身份证复印件（有、无）", null=True, blank=True)

    ptype = models.CharField(max_length=300, verbose_name="手机型号", null=True, blank=True)

    birth = models.CharField(max_length=300, verbose_name="生日", null=True, blank=True)

    devf1 = models.CharField(max_length=300, null=True, blank=True)

    devf2 = models.CharField(max_length=300, null=True, blank=True)

    devf3 = models.CharField(max_length=300, null=True, blank=True)

    devf4 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    devf5 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    devf6 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)


class sales(models.Model):
    uid = models.CharField(max_length=300, verbose_name="学员id", null=False, blank=False)

    uname = models.CharField(max_length=300, verbose_name="学员姓名", null=False, blank=False)

    product = models.CharField(max_length=300, verbose_name="书目/课", null=False, blank=False)

    ztype = models.CharField(max_length=300, verbose_name="类别", null=False, blank=False)

    ucount = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="数量", null=False, blank=False)

    uamt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="总额", null=False, blank=False)

    zbsamt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="总校打款", null=True, blank=True)

    splace = models.CharField(max_length=300, verbose_name="营销", null=True, blank=True)

    snote = models.CharField(max_length=300, verbose_name="备注", null=True, blank=True)

    fprestored = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="分校预存", null=True, blank=True)

    channel = models.CharField(max_length=900, verbose_name="报名途径", null=True, blank=True)

    # 预留字段
    devf1 = models.CharField(max_length=300, null=True, blank=True)

    # 预留字段
    devf2 = models.CharField(max_length=300, null=True, blank=True)

    # 预留字段
    devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # 预留字段
    devf4 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # 预留字段
    devf5 = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)


# class ztype(models.Model):
#     ztype = models.CharField(max_length=300, verbose_name="类别", null=False, blank=False)
#
#     # 预留字段
#     devf1 = models.CharField(max_length=300, null=True, blank=True)
#
#     # 预留字段
#     devf2 = models.CharField(max_length=300, null=True, blank=True)
#
#     # 预留字段
#     devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)


class uexam(models.Model):
    uid = models.CharField(max_length=300, verbose_name="学员id", null=False, blank=False)

    uname = models.CharField(max_length=300, verbose_name="学员姓名", null=False, blank=False)

    jexam = models.CharField(max_length=50, verbose_name="技能成绩", null=False, blank=False)

    bexam = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="笔试成绩", null=True, blank=True)

    # 预留字段
    devf1 = models.CharField(max_length=300, null=True, blank=True)

    # 预留字段
    devf2 = models.CharField(max_length=300, null=True, blank=True)

    # 预留字段
    devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # class express(models.Model):
    #     uid = models.CharField(max_length=300, verbose_name="学员id", null=False, blank=False)
    #
    #     name = models.CharField(max_length=300, verbose_name="学员姓名", null=False, blank=False)
    #
    #     product = models.CharField(max_length=300, verbose_name="书目/课", null=False, blank=False)
    #
    #     ztype = models.CharField(max_length=300, verbose_name="类别", null=False, blank=False)
    #
    #     bookname = models.CharField(max_length=300, verbose_name="书名", null=True, blank=True)
    #
    #     expressnum = models.CharField(max_length=300, verbose_name="单号", null=True, blank=True)
    #
    #     exdate = models.CharField(max_length=300, verbose_name="发书/开课时间", null=False, blank=False)
    #
    #     # 预留字段
    #     devf1 = models.CharField(max_length=300, null=True, blank=True)
    #
    #     # 预留字段
    #     devf2 = models.CharField(max_length=300, null=True, blank=True)
    #
    #     # 预留字段
    #     devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    #
    #     webdate = models.CharField(max_length=300, verbose_name="开课时间", null=False, blank=False)
    #
    #     # 预留字段
    #     devf1 = models.CharField(max_length=300, null=True, blank=True)
    #
    #     # 预留字段
    #     devf2 = models.CharField(max_length=300, null=True, blank=True)
    #
    #     # 预留字段
    #     devf3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

class qa(models.Model):
    question = models.TextField(verbose_name="问题", null=True, blank=True)
    opr_1 = models.TextField(verbose_name="选项1", null=True, blank=True)
    opr_2 = models.TextField(verbose_name="选项2", null=True, blank=True)
    opr_3 = models.TextField(verbose_name="选项3", null=True, blank=True)
    opr_4 = models.TextField(verbose_name="选项4", null=True, blank=True)
    opr_5 = models.TextField(verbose_name="选项5", null=True, blank=True)
    opr_6 = models.TextField(verbose_name="选项6", null=True, blank=True)
    opr_7 = models.TextField(verbose_name="选项7", null=True, blank=True)
    answer = models.TextField(verbose_name="答案", null=True, blank=True)
    analysis = models.TextField(verbose_name="解析", null=True, blank=True)
    beizhu = models.TextField(verbose_name="备注", null=True, blank=True)
    weighted = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="权重(默认为1)", null=False, blank=False, default=1)
    devf1 = models.TextField(verbose_name="自定义项1", null=True, blank=True)
    devf2 = models.TextField(verbose_name="自定义项2", null=True, blank=True)
    devf3 = models.TextField(verbose_name="自定义项3", null=True, blank=True)
    type = models.TextField(verbose_name="题型", null=True, blank=True, default='1')

"""
    存储学生的答题细节
"""
class qa_record(models.Model):
    uid = models.CharField(max_length=300, verbose_name="学员id", null=False, blank=False)
    questionIDs =  models.TextField(verbose_name="题的id,用逗号隔开", null=True, blank=True)
    select = models.TextField(verbose_name="选项记录,用逗号隔开", null=True, blank=True)
    test_score = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="成绩", null=False, blank=False, default=0)

    type = models.TextField(verbose_name="题型", null=True, blank=True, default='1')

    devf1 = models.TextField(verbose_name="自定义项1", null=True, blank=True)
    devf2 = models.TextField(verbose_name="自定义项2", null=True, blank=True)
    devf3 = models.TextField(verbose_name="自定义项3", null=True, blank=True)


class ns(models.Model):
    opr_1 = models.CharField(max_length=300, null=True, blank=True)
    imp_1 = models.ImageField(upload_to="media/upto", null=False, blank=False)
    ty_1 = models.CharField(max_length=300, null=True, blank=True)
    beizhu = models.TextField(verbose_name="备注", null=True, blank=True)

    devf1 = models.CharField(max_length=300, null=True, blank=True)
    devf2 = models.CharField(max_length=300, null=True, blank=True)
    devf3 = models.TextField(verbose_name="自定义项3", null=True, blank=True)
