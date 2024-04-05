
from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule,Visit
from .requisitions import subject_requisition
from .crfs import crf

trainee_schedule = Schedule (
    name='trainee_schedule',
    verbose_name= 'Trainee +',
    onschedule_model='trainee_subject.onschedule',
    offschedule_model='trainee_subject.offschedule',
    consent_model='trainee_subject.subjectconsent',
    appointment_model='edc_appointment.appointment'

)

visit0T = Visit (
    code='1000T',
    title= 'Initial Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=subject_requisition,
    crfs=crf.get('initial'),
    facility_name='5-day clinic'

)

visit1T = Visit (
    code='2000T',
    title= 'follows up Visit',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic'

)
visit2T= Visit (
    code='3000T',
    title= 'Further Follow up Visit',
    timepoint=4,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic'

)

trainee_schedule.add_visit(visit=visit0T)
trainee_schedule.add_visit(visit=visit1T)
trainee_schedule.add_visit(visit=visit2T)
