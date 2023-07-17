from django.contrib import admin
from .models import Competition, Player, Team, Game, Stat

class CompetitionPlayerInline(admin.TabularInline):
    model = Player
    extra = 0
    inline_classes = ('grp-collapse', 'grp-open')
    classes = ['collapse']    

class CompetitionTeamInline(admin.TabularInline):
    model = Team
    extra = 0
    classes = ['collapse']

class CompetitionGameInline(admin.TabularInline):
    model = Game
    extra = 0
    show_change_link = True
    classes = ['collapse']

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'event_date']
    list_filter = ['event_date']
    inlines = [CompetitionPlayerInline, CompetitionTeamInline, CompetitionGameInline]

class GameStatsInline(admin.TabularInline):
    model = Stat
    extra = 0

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'mode', 'event_date', 'team_a', 'team_b')
    list_filter = ['competition', 'mode']
    inlines = [GameStatsInline]

# Register your models here.
admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Game,GameAdmin)