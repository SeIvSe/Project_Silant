from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import *
from .filters import *
from rest_framework import generics
from .serializers import *

class MaintenanceListView(LoginRequiredMixin, ListView):
    model = Maintenance
    template_name = 'Maintenance.html'

    def get_context_data(self, **kwargs):
        filter = MaintenanceFilter(self.request.GET, queryset=self.get_queryset())
        manager = self.request.user.groups.filter(name='Менеджер')
        if not manager.exists():
            this_manager = 'Не менеджер'
        else:
            this_manager = 'Менеджер'
        context = {'filter': filter, 'this_manager': this_manager}
        return context


class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    context_object_name = 'complaint'
    template_name = 'complaint.html'

    def get_context_data(self, **kwargs):
        filter = ComplaintFilter(self.request.GET, queryset=self.get_queryset())
        manager = self.request.user.groups.filter(name='Менеджер')
        if not manager.exists():
            this_manage = 'Не менеджер'
        else:
            this_manage = 'Менеджер'
        context = {'filter': filter, 'this_manager': this_manage}
        return context


class MaintenanceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = (
        'service.add_maintenance',
    )
    template_name = 'maintenance_create.html'
    form_class = MaintenanceForm


class ComplaintCreateView(PermissionRequiredMixin, CreateView):
    permission_required = (
        'service.add_complaint',
    )
    template_name = 'complaint_create.html'
    form_class = ComplaintForm

class MachineCreateView(PermissionRequiredMixin, CreateView):
    permission_required = (
        'service.add_machine',
    )
    template_name = 'machine_create.html'
    form_class = MachineForm


class MaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_maintenance',)
    template_name = 'maintenance_create.html'
    form_class = MaintenanceForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Maintenance.objects.get(pk=id)


class ComplaintUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_complaint',)
    template_name = 'complaint_create.html'
    form_class = ComplaintForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Complaint.objects.get(pk=id)

class MachineUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_machine',)
    template_name = 'machine_create.html'
    form_class = MachineForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Machine.objects.get(pk=id)


class MachineDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_machine',)
    template_name = 'delete_machine.html'
    queryset = Machine.objects.all()
    success_url = '/user/'

class MaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_maintenance',)
    template_name = 'delete_maintenance.html'
    queryset = Maintenance.objects.all()
    success_url = '/maintenance/'

class ComplaintDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_complaint',)
    template_name = 'delete_complaint.html'
    queryset = Complaint.objects.all()
    success_url = '/complaint/'


class SearchMachine(ListView):
    model = Machine
    template_name = 'search.html'
    context_object_name = 'machine'


    def get_queryset(self, **kwargs):
        search_query = self.request.GET.get('search', '')
        if search_query:
            machine = Machine.objects.filter(number_machine__icontains=search_query)
            if not machine.exists():
                machine = 'Не найдено'
        else:
            machine = 'Ваших данных нет в базе'
        context = machine
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['this_authorized'] = self.request.user.groups.exists()
        return context


def machine_user(request):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'


    filter = MachineFilter(request.GET)
    if this_authorized:
        if this_manager == 'Менеджер':
            machine = 0
        else:
            machine = Machine.objects.filter(client=request.user.first_name)
            if not machine.exists():
                service_list = ServiceCompany.objects.filter(name=request.user.first_name)
                if service_list.exists():
                    service = ServiceCompany.objects.get(name=request.user.first_name)
                    machine = Machine.objects.filter(service_company=service.id)
                else:
                    machine = 'Вашей техники нет в базе. Проверьте введенные сведения.'
        context = {'machine': machine,
                   'this_authorized': this_authorized,
                   'filter': filter,
                   'this_manager': this_manager,
                   }
    else:
        machine = 'Пройдите авторизацию'
        context = {'machine': machine}
    return render (request, 'user.html', context)


def maintenance_detail(request, maintenance_id):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'
    if this_authorized:
        maintenance = Maintenance.objects.get(pk=maintenance_id)
        machine = Machine.objects.get(number_machine=maintenance.machine_maintenance)
        service = ServiceType.objects.get(name=maintenance.service_type)
        service_company = ServiceCompany.objects.get(name=maintenance.service_company)
        context = {'maintenance': maintenance,
                   'machine': machine,
                   'this_authorized': this_authorized,
                   'service': service,
                   'service_company': service_company,
                   'this_manager': this_manager,
                   }
    else:
        maintenance = 'Пройдите авторизацию'
        context = {'maintenance': maintenance}
    return render(request, 'maintenance_detail.html', context)

def complaint_detail(request, complaint_id):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'
    if this_authorized:
        complaint = Complaint.objects.get(pk=complaint_id)
        machine = Machine.objects.get(number_machine=complaint.machine_complaint)
        node = FailureNode.objects.get(name=complaint.failure_node)
        recovery = RecoveryMethod.objects.get(name=complaint.recovery_method)
        service = ServiceCompany.objects.get(name=complaint.service_company_complaint)
        context = {'complaint': complaint,
                   'machine': machine,
                   'this_authorized': this_authorized,
                   'node': node,
                   'recovery': recovery,
                   'service': service,
                   'this_manager': this_manager,
                   }
    else:
        complaint = 'Пройдите авторизацию'
        context = {'complaint': complaint}
    return render(request, 'complaint_detail.html', context)

def complaint_list_machine(request, machine_id):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'
    if this_authorized:
        complaints = Complaint.objects.filter(machine_complaint=machine_id)
        machine = Machine.objects.get(pk=machine_id)
        context = {'complaints': complaints,
                   'machine': machine,
                   'this_authorized': this_authorized,
                   'this_manager': this_manager,
                   }
    else:
        complaints = 'Пройдите авторизацию'
        context = {'complaints': complaints}
    return render(request, 'complaints_machine.html', context)


def maintenance_list_machine(request, machine_id):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'
    if this_authorized:
        maintenances = Maintenance.objects.filter(machine_maintenance=machine_id)
        machine = Machine.objects.get(pk=machine_id)
        context = {'maintenances': maintenances,
                   'machine': machine,
                   'this_authorized': this_authorized,
                   'this_manager': this_manager,
                   }
    else:
        maintenances = 'Пройдите авторизацию'
        context = {'maintenances': maintenances}
    return render(request, 'maintenances_machine.html', context)


def machine_detail(request, machine_id):
    this_authorized = request.user.groups.exists()
    manager = request.user.groups.filter(name='Менеджер')
    if not manager.exists():
        this_manager = 'Не менеджер'
    else:
        this_manager = 'Менеджер'
    if this_authorized:
        machine = Machine.objects.get(pk=machine_id)
        technique = TechniqueModel.objects.get(name=machine.technique_model)
        engine = EngineModel.objects.get(name=machine.engine_model)
        trans = TransmissionModel.objects.get(name=machine.transmission_model)
        axle = DriveAxleModel.objects.get(name=machine.drive_axle_model)
        steering = SteeringBridgeModel.objects.get(name=machine.steering_bridge_model)
        service = ServiceCompany.objects.get(name=machine.service_company)
        context = {'machine': machine,
                   'technique': technique,
                   'this_authorized': this_authorized,
                   'engine': engine,
                   'trans': trans,
                   'axle': axle,
                   'steering': steering,
                   'service': service,
                   'this_manager': this_manager
                   }
    else:
        machine = 'Пройдите авторизацию'
        context = {'machine': machine}
    return render(request, 'machine_detail.html', context)


class ServiceCompanyListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_service_company')
    model = ServiceCompany
    context_object_name = 'service_company'
    template_name = 'lists/service_company_list.html'
    queryset = ServiceCompany.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceCompanyFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TechniqueModelListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_technique_model')
    model = TechniqueModel
    context_object_name = 'technique_model'
    template_name = 'lists/technique_model_list.html'
    queryset = TechniqueModel.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TechniqueModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EngineModelListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_engine_model')
    model = EngineModel
    context_object_name = 'engine_model'
    template_name = 'lists/engine_model_list.html'
    queryset = EngineModel.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EngineModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TransmissionModelListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_transmission_model')
    model = TransmissionModel
    context_object_name = 'transmission_model'
    template_name = 'lists/transmission_model_list.html'
    queryset = TransmissionModel.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransmissionModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DriveAxleModelListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_drive_axle_model')
    model = DriveAxleModel
    context_object_name = 'drive_axle_model'
    template_name = 'lists/drive_axle_model_list.html'
    queryset = DriveAxleModel.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DriveAxleModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SteeringBridgeModelListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_steering_bridge_model')
    model = SteeringBridgeModel
    context_object_name = 'steering_bridge_model'
    template_name = 'lists/steering_bridge_model_list.html'
    queryset = SteeringBridgeModel.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SteeringBridgeModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceTypeListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_service_type')
    model = ServiceType
    context_object_name = 'service_type'
    template_name = 'lists/service_type_list.html'
    queryset = ServiceType.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceTypeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class FailureNodeListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_failure_node')
    model = FailureNode
    context_object_name = 'failure_node'
    template_name = 'lists/failure_node_list.html'
    queryset = FailureNode.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FailureNodeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RecoveryMethodListView(PermissionRequiredMixin, ListView):
    permission_required = ('service.view_recovery_method')
    model = RecoveryMethod
    context_object_name = 'recovery_method'
    template_name = 'lists/recovery_method_list.html'
    queryset = RecoveryMethod.objects.all()
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecoveryMethodFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceCompanyCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_service_company')
    template_name = 'lists/create.html'
    form_class = ServiceCompanyForm
    login_url = '/'


class TechniqueModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_technique_model')
    template_name = 'lists/create.html'
    form_class = TechniqueModelForm
    login_url = '/'

class EngineModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_engine_model')
    template_name = 'lists/create.html'
    form_class = EngineModelForm
    login_url = '/'

class TransmissionModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_transmission_model')
    template_name = 'lists/create.html'
    form_class = TransmissionModelForm
    login_url = '/'

class DriveAxleModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_drive_axle_model')
    template_name = 'lists/create.html'
    form_class = DriveAxleModelForm
    login_url = '/'

class SteeringBridgeModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_steering_bridge_model')
    template_name = 'lists/create.html'
    form_class = SteeringBridgeModelForm
    login_url = '/'

class ServiceTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_service_type')
    template_name = 'lists/create.html'
    form_class = ServiceTypeForm
    login_url = '/'

class FailureNodeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_failure_node')
    template_name = 'lists/create.html'
    form_class = FailureNodeForm
    login_url = '/'


class RecoveryMethodCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('service.add_recovery_method')
    template_name = 'lists/create.html'
    form_class = RecoveryMethodForm
    login_url = '/'


class ServiceCompanyDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_service_company')
    template_name = 'lists/delete_service_company.html'
    queryset = ServiceCompany.objects.all()
    success_url = '/service_company/'
    login_url = '/'


class TechniqueModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_technique_model')
    template_name = 'lists/delete_technique_model.html'
    queryset = TechniqueModel.objects.all()
    success_url = '/technique_model/'
    login_url = '/'


class EngineModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_engine_model')
    template_name = 'lists/delete_engine_model.html'
    queryset = EngineModel.objects.all()
    success_url = '/engine_model/'
    login_url = '/'


class TransmissionModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_transmission_model')
    template_name = 'lists/delete_transmission_model.html'
    queryset = TransmissionModel.objects.all()
    success_url = '/transmission_model/'
    login_url = '/'


class DriveAxleModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_drive_axle_model')
    template_name = 'lists/delete_drive_axle_model.html'
    queryset = DriveAxleModel.objects.all()
    success_url = '/drive_axle_model/'
    login_url = '/'


class SteeringBridgeModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_steering_bridge_model')
    template_name = 'lists/delete_steering_bridge_model.html'
    queryset = SteeringBridgeModel.objects.all()
    success_url = '/steering_bridge_model/'
    login_url = '/'


class ServiceTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_service_type')
    template_name = 'lists/delete_service_type.html'
    queryset = ServiceType.objects.all()
    success_url = '/service_type/'
    login_url = '/'


class FailureNodeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_failure_node')
    template_name = 'lists/delete_failure_node.html'
    queryset = FailureNode.objects.all()
    success_url = '/failure_node/'
    login_url = '/'


class RecoveryMethodDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('service.delete_recovery_method')
    template_name = 'lists/delete_recovery_method.html'
    queryset = RecoveryMethod.objects.all()
    success_url = '/recovery_method/'
    login_url = '/'


class ServiceCompanyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_service_company')
    template_name = 'lists/create.html'
    form_class = ServiceCompanyForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ServiceCompany.objects.get(pk=id)


class TechniqueModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_technique_model')
    template_name = 'lists/create.html'
    form_class = TechniqueModelForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return TechniqueModel.objects.get(pk=id)


class EngineModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_engine_model')
    template_name = 'lists/create.html'
    form_class = EngineModelForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return EngineModel.objects.get(pk=id)


class TransmissionModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_transmission_model')
    template_name = 'lists/create.html'
    form_class = TransmissionModelForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return TransmissionModel.objects.get(pk=id)


class DriveAxleModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_drive_axle_model')
    template_name = 'lists/create.html'
    form_class = DriveAxleModelForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return DriveAxleModel.objects.get(pk=id)


class SteeringBridgeModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_steering_bridge_model')
    template_name = 'lists/create.html'
    form_class = SteeringBridgeModelForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return SteeringBridgeModel.objects.get(pk=id)


class ServiceTypeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_service_type')
    template_name = 'lists/create.html'
    form_class = ServiceTypeForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ServiceType.objects.get(pk=id)


class FailureNodeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_failure_node')
    template_name = 'lists/create.html'
    form_class = FailureNodeForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return FailureNode.objects.get(pk=id)


class RecoveryMethodUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('service.change_recovery_method')
    template_name = 'lists/create.html'
    form_class = RecoveryMethodForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return RecoveryMethod.objects.get(pk=id)



# Реализация API
class MachineAPIVew(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class TOAPIVew(generics.ListAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ComplaintAPIVew(generics.ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer