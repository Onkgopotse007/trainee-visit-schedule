from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_initial = FormsCollection (
    Crf(show_order=1, model='traineesubject.educationalquestionaire'),
    Crf(show_order=2, model='traineesubject.communityengagement'),
    name= 'initial',
)


crfs_followup = FormsCollection (
    Crf(show_order=1, model='traineesubject.educationalquestionaire'),
    Crf(show_order=2, model='traineesubject.communityengagement'),
    Crf(show_order=3, model='traineesubject.demographic'),
    name= 'followup',
)




crf.update(
    {'initial': crfs_initial,
     'followup': crfs_followup,
    }
)