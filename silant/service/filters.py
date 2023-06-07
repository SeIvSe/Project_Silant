from django_filters import FilterSet
from .models import *


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = (
           'technique_model',
           'engine_model',
           'transmission_model',
           'steering_bridge_model',
           'drive_axle_model',
        )


class MaintenanceFilter(FilterSet):

    class Meta:
        model = Maintenance
        fields = (
            'service_type',
            'machine',
            'company_make_service',
        )


class ComplaintFilter(FilterSet):

    class Meta:
        model = Complaint
        fields =(
            'failure_node',
            'recovery_method',
            'service_company_complaint',
        )


class ServiceCompanyFilter(FilterSet):

    class Meta:
        model = ServiceCompany
        fields = (
            'name',
            'description',
        )

class TechniqueModelFilter(FilterSet):

    class Meta:
        model = TechniqueModel
        fields = (
            'name',
            'description',
        )

class EngineModelFilter(FilterSet):

    class Meta:
        model = EngineModel
        fields = (
            'name',
            'description',
        )

class TransmissionModelFilter(FilterSet):

    class Meta:
        model = TransmissionModel
        fields = (
            'name',
            'description',
        )

class DriveAxleModelFilter(FilterSet):

    class Meta:
        model = DriveAxleModel
        fields = (
            'name',
            'description',
        )

class SteeringBridgeModelFilter(FilterSet):

    class Meta:
        model = SteeringBridgeModel
        fields = (
            'name',
            'description',
        )

class ServiceTypeFilter(FilterSet):

    class Meta:
        model = ServiceType
        fields = (
            'name',
            'description',
        )

class FailureNodeFilter(FilterSet):

    class Meta:
        model = FailureNode
        fields = (
            'name',
            'description',
        )

class RecoveryMethodFilter(FilterSet):

    class Meta:
        model = RecoveryMethod
        fields = (
            'name',
            'description',
        )