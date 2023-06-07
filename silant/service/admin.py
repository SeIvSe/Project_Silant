from django.contrib import admin
from .models import *

admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Complaint)

admin.site.register(ServiceCompany)
admin.site.register(MakeServiceCompany)
admin.site.register(TechniqueModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteeringBridgeModel)
admin.site.register(ServiceType)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
admin.site.register(EngineModel)
