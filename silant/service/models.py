from django.db import models

class ServiceCompany(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/service_company'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисная компания'


class TechniqueModel(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/technique_model'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модель техники'


class EngineModel(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/engine_model'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модель двигателя'


class TransmissionModel(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/transmission_model'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модель трансмиссии'


class DriveAxleModel(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/drive_axle_model'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модель ведущего моста'


class SteeringBridgeModel(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/steering_bridge_model'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модель управляемого моста'


class Machine(models.Model):
    number_machine = models.TextField(unique=True, verbose_name='Зав. № машины')
    technique_model = models.ForeignKey(TechniqueModel, verbose_name='Модель техники', on_delete=models.CASCADE)
    engine_model = models.ForeignKey(EngineModel, verbose_name='Модель двигателя', on_delete=models.CASCADE)
    engine_number = models.TextField(verbose_name='Зав. № двигателя')
    transmission_model = models.ForeignKey(TransmissionModel, verbose_name='Модель трансмиссии', on_delete=models.CASCADE)
    transmission_number = models.TextField(verbose_name='Зав. № трансмиссии')
    drive_axle_model = models.ForeignKey(DriveAxleModel, verbose_name='Модель ведущего моста', on_delete=models.CASCADE)
    drive_axle_number = models.TextField(verbose_name='Зав. № ведущего моста')
    steering_bridge_model = models.ForeignKey(SteeringBridgeModel, verbose_name='Модель управляемого моста', on_delete=models.CASCADE)
    steering_bridge_number = models.TextField(verbose_name='Зав. № управляемого моста')
    supply_contract = models.TextField(verbose_name='Договор поставки №, дата')
    shipping_date = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.TextField(verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(verbose_name='Комплектация (доп. опции)')
    client = models.TextField(verbose_name='Клиент')
    service_company = models.ForeignKey(ServiceCompany, verbose_name='Сервисная компания', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/user'

    def __str__(self):
        return self.number_machine

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машина'
        ordering = ['-shipping_date']


class MakeServiceCompany(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/make_service_company'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация, проводившая ТО'
        verbose_name_plural = 'Организация, проводившая ТО'


class ServiceType(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/service_type'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'


class Maintenance(models.Model):
    service_type = models.ForeignKey(ServiceType, verbose_name='Вид ТО', on_delete=models.CASCADE)
    service_date = models.DateField(verbose_name='Дата проведения ТО')
    operating_time = models.FloatField(verbose_name='Наработка, м/час')
    work_order_number = models.TextField(verbose_name='№ заказ-наряда')
    work_order_date = models.DateField(verbose_name='дата заказ-наряда')
    company_make_service = models.ForeignKey(MakeServiceCompany, verbose_name='Организация, проводившая ТО', on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, verbose_name='Машина', on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, verbose_name='Сервисная компания', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/maintenance'

    def __str__(self):
        return self.work_order_number

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Техническое обслуживание'
        ordering = ['-service_date']


class FailureNode(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/failure_node'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Описание отказа'
        verbose_name_plural = 'Описание отказа'


class RecoveryMethod(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def get_absolute_url(self):
        return f'/recovery_method'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способ восстановления'


class Complaint(models.Model):
    date_rejection = models.DateField(verbose_name='Дата отказа')
    operating_time = models.FloatField(verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey(FailureNode, verbose_name='Узел отказа', on_delete=models.CASCADE)
    failure_description = models.TextField(verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(RecoveryMethod, verbose_name='Способ восстановления', on_delete=models.CASCADE)
    spare_parts = models.TextField(verbose_name='Используемые запасные части', null=True, blank=True)
    recovery_date = models.DateField(verbose_name='Дата восстановления')
    equipment_downtime = models.IntegerField(verbose_name='Время простоя техники')
    machine_complaint = models.ForeignKey(Machine, verbose_name='Машина', on_delete=models.CASCADE)
    service_company_complaint = models.ForeignKey(ServiceCompany, verbose_name='Сервисная компания', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return f'/complaint'

    def downtime(self):
        return (self.recovery_date - self.date_rejection).days

    def __str__(self):
        return self.failure_description

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ['-date_rejection']