from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

FAMILIAL_SITUATION_CHOICES = (
    ('Married',"married"),
    ('Divorced','divorced'),
    ('Separated','separated'),
    ('Single','single'),
    ('Widow(er)','widow(er)')
)
LODGING_CHOICES = (
    ('With Garden', 'with garden'),
    ('Without Garden', 'without garden'),

)

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user    =self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user    =self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    


class Account(AbstractBaseUser):
    email           =models.EmailField(verbose_name="email",max_length=60,unique=True)
    username        =models.CharField(max_length=30, unique=True)
    date_joined     =models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login      =models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)
    first_name      =models.CharField(verbose_name="first name",max_length=30,null=True, blank=True)
    last_name       =models.CharField(verbose_name="last name",max_length=30,null=True, blank=True)
    cin             =models.CharField(max_length=30,null=True, blank=True)
    salary          =models.IntegerField(null=True, blank=True)
    phone_number    =models.IntegerField(null=True, blank=True)
    lodging         =models.CharField(choices=LODGING_CHOICES,max_length=15,null=True, blank=True)
    fammilial_status=models.CharField(choices=FAMILIAL_SITUATION_CHOICES,max_length=10,null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username',]

    objects= MyAccountManager()
    def __str__(self):
        return self.email
    
    def has_perm(self,perm, obj=None):
        return self.is_admin
   
    def has_module_perms(self,app_label):
        return True

