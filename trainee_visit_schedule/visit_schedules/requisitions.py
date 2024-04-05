from edc_visit_schedule import FormsCollection,Requisition
from trainee_labs import viral_load_panel

subject_requisition= FormsCollection(
    Requisition(
    required=True,
        show_order=10,
        panel=viral_load_panel,additional=False)
        ,name='subject_requisition')