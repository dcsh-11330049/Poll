from django.db import models

# Create your models here.

class Poll(models.Model): 
    """
        Poll element, refers to a poll
        (user-defined)
    """
    topic = models.CharField("投票主題", max_length = 64, help_text = "將投票主題填在這！")
    description = models.TextField("說明文字", blank = True, help_text = "將此投票的說明文字填在這！")
    creation_date = models.DateField("創建日期", auto_now_add = True)
    def __str__(self) -> str:
        return self.topic

class Option(models.Model):
    """
        Option element (sub-element of the Poll element), refers to an option in the Poll
        (user-defined)
    """
    title = models.CharField("選項文字", max_length = 64, help_text = "將選項的文字填在這裡！")
    votes = models.IntegerField("票數", default = 0)
    poll_id = models.IntegerField("投票主題編號", help_text = "將投票主題的編號輸入這裡！")
    def __str__(self) -> str:
        return "{} - {}　（票數：{}）".format(self.poll_id, self.title, self.votes)
        return f"{self.poll_id} - {self.title}: {self.votes}"