from crontab import CronTab
import constants

tab = CronTab(user=True)
cron_job = tab.new(constants.commandline_crontab)
# cron_job.minute().every(5)
cron_job.minute.every(5)
# writes content to crontab
tab.write()
print tab.render()