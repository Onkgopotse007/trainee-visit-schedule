from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedule import trainee_schedule


trainee_visit_schedule = VisitSchedule(
    name='trainee_visit_schedule',
    verbose_name='trainee',
    offstudy_model='trainee_prn.subjectoffstudy',
    locator_model='trainee_subject.subjectlocator',
    death_report_model= 'trainee_prn.deathreport',
    previous_visit_schedule=None
)

trainee_visit_schedule.add_schedule(trainee_schedule)

site_visit_schedules.register(trainee_visit_schedule)