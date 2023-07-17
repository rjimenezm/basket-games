from django.db import models
from django.urls import reverse

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

# Create your models here.
class Competition(TimestampedModel):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    event_date = models.DateField(null=True)

    def __str__(self):
        return str(self.title)    

""" 	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})    
 """

class Player(TimestampedModel):
    name = models.CharField(max_length=250)
    number = models.IntegerField(null=True, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)  

class Team(TimestampedModel):
    name = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=3, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)
    player = models.ManyToManyField(Player)  

    def __str__(self):
        return f"{self.name}" if self.abbreviation == "" else f"{self.abbreviation}"
     
class Game(TimestampedModel):
    MODE_CHOICES = (
        ('1X1', '1X1'),
        ('2X2', '2X2'),
        ('3X3', '3X3')
    )
    event_date = models.DateField(null=True)
    mode = models.CharField(max_length=3, choices=MODE_CHOICES)
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_b')
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.team_a} vs {self.team_b}'    

class Stat(TimestampedModel):
    EVENT_CHOICE = (
        ('Free thrown', 'Free thrown'),
        ('1-point', 'One point shot'),
        ('2-point', 'Two points shot'),
        ('Personal foul', 'Personal foul'),
        ('Technical foul', 'Personal foul'),
        ('Shot foul', 'Shot foul'),
        ('Win', 'Win'),
        ('Tie', 'Tie')
    )
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    event = models.CharField(max_length=20, choices=EVENT_CHOICE)
    event_time = models.DateTimeField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
