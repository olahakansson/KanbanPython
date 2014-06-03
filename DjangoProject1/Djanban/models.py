from django.db import models



class WorkItem(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date published')
    description = models.CharField(max_length=200)

  
#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

#    def __unicode__(self):
#        return self.choice_text