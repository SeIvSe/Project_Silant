from django.urls import path
from .views import *
from rest_framework.schemas import get_schema_view

urlpatterns = [

path('', SearchMachine.as_view(), name='search'),
path('user/', machine_user, name='user'),


path('complaint/', ComplaintListView.as_view(), name='complaint'),
path('complaint_add/', ComplaintCreateView.as_view(), name='complaint_create'),
path('complaint_edit/<int:pk>/', ComplaintUpdateView.as_view(), name='complaint_update'),
path('complaint/<int:complaint_id>/', complaint_detail, name='complaint_detail'),
path('complaint_delete/<int:pk>/', ComplaintDeleteView.as_view(), name='complaint_delete'),
path('complaint_list/<int:machine_id>/', complaint_list_machine, name='complaint_list'),


path('machine_add/', MachineCreateView.as_view(), name='machine_create'),
path('machine/<int:machine_id>/', machine_detail, name='machine_detail'),
path('machine_edit/<int:pk>/', MachineUpdateView.as_view(), name='machine_update'),
path('machine_delete/<int:pk>/', MachineDeleteView.as_view(), name='machine_delete'),


path('maintenance/', MaintenanceListView.as_view(), name='maintenance'),
path('maintenance_add/', MaintenanceCreateView.as_view(), name='maintenance_create'),
path('maintenance/<int:maintenance_id>/', maintenance_detail, name='maintenance_detail'),
path('maintenance_edit/<int:pk>/', MaintenanceUpdateView.as_view(), name='maintenance_update'),
path('maintenance_delete/<int:pk>/', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
path('maintenance_list/<int:machine_id>/', maintenance_list_machine, name='maintenance_list'),


path('technique_model/', TechniqueModelListView.as_view(), name='technique_model'),
path('technique_model_create/', TechniqueModelCreateView.as_view(), name='technique_model_create'),
path('technique_model_edit/<int:pk>/', TechniqueModelUpdateView.as_view(), name='technique_model_edit'),
path('technique_model_delete/<int:pk>/', TechniqueModelDeleteView.as_view(), name='technique_model_delete'),


path('engine_model/', EngineModelListView.as_view(), name='engine_model'),
path('engine_model_create/', EngineModelCreateView.as_view(), name='engine_model_create'),
path('engine_model_edit/<int:pk>/', EngineModelUpdateView.as_view(), name='engine_model_edit'),
path('engine_model_delete/<int:pk>/', EngineModelDeleteView.as_view(), name='engine_model_delete'),


path('transmission_model/', TransmissionModelListView.as_view(), name='transmission_model'),
path('transmission_model_create/', TransmissionModelCreateView.as_view(), name='transmission_model_create'),
path('transmission_model_edit/<int:pk>/', TransmissionModelUpdateView.as_view(), name='transmission_model_edit'),
path('transmission_model_delete/<int:pk>/', TransmissionModelDeleteView.as_view(), name='transmission_model_delete'),


path('drive_axle_model/', DriveAxleModelListView.as_view(), name='drive_axle_model'),
path('drive_axle_model_create/', DriveAxleModelCreateView.as_view(), name='drive_axle_model_create'),
path('drive_axle_model_edit/<int:pk>/', DriveAxleModelUpdateView.as_view(), name='drive_axle_model_edit'),
path('drive_axle_model_delete/<int:pk>/', DriveAxleModelDeleteView.as_view(), name='drive_axle_model_delete'),


path('steering_bridge_model/', SteeringBridgeModelListView.as_view(), name='steering_bridge_model'),
path('steering_bridge_model_create/', SteeringBridgeModelCreateView.as_view(), name='steering_bridge_model_create'),
path('steering_bridge_model_edit/<int:pk>/', SteeringBridgeModelUpdateView.as_view(), name='steering_bridge_model_edit'),
path('steering_bridge_model_delete/<int:pk>/', SteeringBridgeModelDeleteView.as_view(), name='steering_bridge_model_delete'),


path('service_type/', ServiceTypeListView.as_view(), name='service_type'),
path('service_type_create/', ServiceTypeCreateView.as_view(), name='service_type_create'),
path('service_type_edit/<int:pk>/', ServiceTypeUpdateView.as_view(), name='service_type_edit'),
path('service_type_delete/<int:pk>/', ServiceTypeDeleteView.as_view(), name='service_type_delete'),


path('failure_node/', FailureNodeListView.as_view(), name='failure_node'),
path('failure_node_create/', FailureNodeCreateView.as_view(), name='failure_node_create'),
path('failure_node_edit/<int:pk>/', FailureNodeUpdateView.as_view(), name='failure_node_edit'),
path('failure_node_delete/<int:pk>/', FailureNodeDeleteView.as_view(), name='failure_node_delete'),


path('recovery_method/', RecoveryMethodListView.as_view(), name='recovery_method'),
path('recovery_method_create/', RecoveryMethodCreateView.as_view(), name='recovery_method_create'),
path('recovery_method_edit/<int:pk>/', RecoveryMethodUpdateView.as_view(), name='recovery_method_edit'),
path('recovery_method_delete/<int:pk>/', RecoveryMethodDeleteView.as_view(), name='recovery_method_delete'),


path('service_company/', ServiceCompanyListView.as_view(), name='service_company'),
path('service_company_create/', ServiceCompanyCreateView.as_view(), name='service_company_create'),
path('service_company_edit/<int:pk>/', ServiceCompanyUpdateView.as_view(), name='service_company_edit'),
path('service_company_delete/<int:pk>/', ServiceCompanyDeleteView.as_view(), name='service_company_delete'),


path('api/machine/', MachineAPIVew.as_view()),
    path('api/maintenance/', TOAPIVew.as_view()),
    path('api/complaint/', ComplaintAPIVew.as_view()),
    path('openapi/', get_schema_view(
        title="My_Silant",
        description="API for My_Silant",
        version="v 1.0.0"
    ), name='openapi-schema'),

]