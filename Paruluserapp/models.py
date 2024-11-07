from django.db import models

# Create your models here.
class pusermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)

class hdpmodel(models.Model):
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    trestbps = models.CharField(max_length=100)
    chol = models.CharField(max_length=100)
    fbs = models.CharField(max_length=100)
    restecg = models.CharField(max_length=100)
    thalach = models.CharField(max_length=100)
    exang = models.CharField(max_length=100)
    oldpeak = models.CharField(max_length=100)
    slope = models.CharField(max_length=100)
    ca = models.CharField(max_length=100)
    thal = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    custom_predictions = models.CharField(max_length=100)

class kdpmodel(models.Model):
    bp = models.CharField(max_length=100)
    sg = models.CharField(max_length=100)
    al = models.CharField(max_length=100)
    su = models.CharField(max_length=100)
    rbc = models.CharField(max_length=100)
    bu = models.CharField(max_length=100)
    sc = models.CharField(max_length=100)
    sod = models.CharField(max_length=100)
    pot = models.CharField(max_length=100)
    hemo = models.CharField(max_length=100)
    wbcc = models.CharField(max_length=100)
    rbcc = models.CharField(max_length=100)
    htn = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    custom_predictions = models.CharField(max_length=100)

class bdpmodel(models.Model):
    age = models.CharField(max_length=100)
    menopause  = models.CharField(max_length=100)
    Tumor = models.CharField(max_length=100)
    InvNodes = models.CharField(max_length=100)
    Breast = models.CharField(max_length=100)
    Metastasis = models.CharField(max_length=100)
    BreastQuadrant = models.CharField(max_length=100)
    History = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    custom_predictions = models.CharField(max_length=100)

class dpmodel(models.Model):
    pregnancies = models.CharField(max_length=100)
    glucose = models.CharField(max_length=100)
    bloodpressure = models.CharField(max_length=100)
    skinthickness = models.CharField(max_length=100)
    insulin = models.CharField(max_length=100)
    bmi = models.CharField(max_length=100)
    diabetespedigreefunction = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    custom_predictions = models.CharField(max_length=100)

class ldpmodel(models.Model):
    age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Total_Bilirubin = models.CharField(max_length=100)
    Direct_Bilirubin = models.CharField(max_length=100)
    Alkaline_Phosphotase = models.CharField(max_length=100)
    Alamine_Aminotransferase = models.CharField(max_length=100)
    Aspartate_Aminotransferase = models.CharField(max_length=100)
    Total_Protiens = models.CharField(max_length=100)
    Albumin = models.CharField(max_length=100)
    Albumin_and_Globulin_Ratio = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    custom_predictions = models.CharField(max_length=100)