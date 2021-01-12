from django.db import models
from uok.users.models import User


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "Faculties"

    name = models.CharField(max_length=255, unique=True)
    caption = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.caption}'


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    caption = models.CharField(max_length=255, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Plan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)

    def get_modules(self):
        return Module.objects.filter(plan=self.id)

    def __str__(self):
        return f'{self.name}-{self.department}'


class Module(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, blank=True, on_delete=models.DO_NOTHING)
    credit = models.SmallIntegerField(default=0)
    elective = models.BooleanField(default=False)
    lecture_hours = models.SmallIntegerField(default=1)
    lab_hours = models.SmallIntegerField(default=1)
    description = models.TextField(blank=True)

    def get_pre_modules(self):
        return Dependency.objects.filter(post_module=self.id)

    def get_post_modules(self):
        return Dependency.objects.filter(pre_module=self.id)

    def __str__(self):
        return f'{self.name} ({self.code})'


class Dependency(models.Model):
    class Meta:
        verbose_name_plural = "Dependencies"
        unique_together = ('pre_module', 'post_module',)

    pre_module = models.ForeignKey(Module,
                                   related_name="pre_module",
                                   on_delete=models.CASCADE)
    post_module = models.ForeignKey(Module,
                                    related_name="post_module",
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f'''{self.pre_module}     =>     {self.post_module}'''


class Student3(models.Model):
    user = models.OneToOneField(User,
                                default="",
                                on_delete=models.CASCADE,
                                primary_key=True)

    reg_id = models.IntegerField(unique=True, null=False)

    plan = models.ForeignKey(Plan,
                             blank=True,
                             on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE)

    remarks = models.TextField(blank=True)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return f'{self.reg_id}: {self.name()}: {self.department.name} '

    # def get_absolute_url(self):
    #     """Get url for user's detail view.
    #
    #     Returns:
    #         str: URL for user detail.
    #
    #     """
    #     return reverse("students:detail", kwargs={"reg_id": self.reg_id})
