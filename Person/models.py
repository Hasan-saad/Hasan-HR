from django.db import models

# Create your models here.

Religion = (
	('مسلم' , 'مسلم'),
	('مسيحي' , 'مسيحي'),
	)
Sex = (
	('ذكر','ذكر'),
	('انسة','انسة'),
	)
Social_Status = (
	('اعزب','اعزب'),
	('متزوج','متزوج'),
	('ارمل','ارمل'),
	('مطلق','مطلق'),
	)
Management = (
	('الحسابات','الحسابات'),
	('المبيعات','المبيعات'),
	('موارد بشرية','موارد بشرية'),
	('مخازن','مخازن'),
	('مصنع','مصنع'),
	('مشاريع','مشاريع'),
	('الهندسية','الهندسية'),
	('نظم المعلومات','نظم المعلومات'),
	)
HealthInsurance = (
	('A','A'),
	('B','B'),
	('C','C'),
	)
FileStatus = (
	('مكتمل','مكتمل'),
	('غير مكتمل','غير مكتمل'),
	)

# this is split images for folders for evry person folder with person name 
def image_upload(instance, fileName):
	imageName , extension = fileName.split(".")
	return "%s/%s.%s"%(instance.nameEnglish,imageName,extension)	

# This is Main class, add all emploeyees
class Personal(models.Model):
	codeEmploey = models.DecimalField(max_digits=4, decimal_places=0)
	nameArabic = models.CharField(max_length = 30)
	nameEnglish = models.CharField(max_length = 30)
	address = models.CharField(max_length = 100)
	nationalCode = models.DecimalField(max_digits=14, decimal_places=0)
	mobileNum = models.CharField(max_length = 20)
	email = models.EmailField()
	dragaJops = models.CharField(max_length = 100)
	jop =  models.CharField(max_length = 100)
	numInsurance = models.CharField(max_length = 100)
	vacations = models.IntegerField(default= 0) # count the Vacations
	birthDate = models.DateField(auto_now=False, auto_now_add=False, default = '1111-11-11')
	dateOfHiring = models.DateField(auto_now=False, auto_now_add=False, default = '2021-01-01')
	management = models.ForeignKey('Management', on_delete = models.CASCADE)
	religion = models.CharField(max_length = 10, choices = Religion)
	sex = models.CharField(max_length = 10, choices = Sex)
	socialStatus = models.CharField(max_length = 10, choices = Social_Status)
	healthInsurance = models.CharField(max_length = 50, choices = HealthInsurance)
	fileStatus = models.CharField(max_length = 50, choices = FileStatus)
	صورة_شخصية = models.ImageField(upload_to = image_upload)
	صورة_شهادة_ميلاد = models.ImageField(upload_to = image_upload)
	صورة_التجنيد = models.ImageField(upload_to = image_upload)
	شهادة_التخرج = models.ImageField(upload_to = image_upload)
	صورة_مباشرة_عمل = models.ImageField(upload_to = image_upload)
	صورة_فيش_جنائي = models.ImageField(upload_to = image_upload)
	صورة_اقرار_استلام_عمل = models.ImageField(upload_to = image_upload)
	صورة_البطاقة = models.ImageField(upload_to = image_upload)
	صورة_كعب_عمل = models.ImageField(upload_to = image_upload)
	صورة_نموذج_111 = models.ImageField(upload_to = image_upload)
	
	def __str__(self):
		return self.nameEnglish


class Management(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


TypeOfVacation = (
	('A','عارضة'),
	('B','مرضي'),
	('C','اعتيادي'),
	('D','بدون مرتب'),
)
class Vacation(models.Model):
	name = models.ForeignKey(Personal, related_name='Vacation', on_delete=models.CASCADE)
	dateFr = models.DateField()
	dateLs = models.DateField()
	vacation_num = models.IntegerField(default=0)
	vacation = models.CharField(max_length= 15, choices= TypeOfVacation)
	
	def __str__(self):
		return ' {} ==> {} ==> {}'.format( str(self.name), self.vacation_num, self.vacation)


# class ClassName(object):
#     	def __init__(self, *args):
# 		super(ClassName, self).__init__(*args))
		


