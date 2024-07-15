from django.db import models

# Create your models here.
class lignin(models.Model):
    bacteria = models.CharField(max_length=50)
    pathway = models.CharField(max_length=200)
    ph = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    
class ncbidb(models.Model):
    org = models.CharField(max_length=200)
    gene = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    sequence = models.TextField()
    pathways = models.CharField(max_length=200)

class pagetab(models.Model):
    org = models.CharField(max_length=200)
    pathways = models.TextField()
    gene = models.TextField()
    taxonomy = models.CharField(max_length=200)
class taxonomytb(models.Model):
    org = models.CharField(max_length=200)
    comptax = models.CharField(max_length=200)
    taxonomy1 = models.CharField(max_length=200)
    taxonomy2 = models.CharField(max_length=200)
    taxonomy3 = models.CharField(max_length=200)
    taxonomy4 = models.CharField(max_length=200)
    taxonomy5 = models.CharField(max_length=200)
    taxonomy6 = models.CharField(max_length=200)
    taxonomy7 = models.CharField(max_length=200)
    taxonomy8 = models.CharField(max_length=200)
class GeneData(models.Model):
    gene = models.TextField()
    organism = models.TextField()
    gene_id = models.TextField()
    protein_id = models.TextField()
    product = models.TextField()
    GO_function = models.TextField()
    GO_process = models.TextField()
    EC_number = models.TextField()
    GO_component = models.TextField()
    function = models.TextField()
    translation = models.TextField()
    pathways = models.TextField()