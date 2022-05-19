from django.db import models


class Block(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image_1 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Scenario(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image_1 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='image/', blank=True, null=True)
    block_relation = models.ManyToManyField(Block)
    relation = models.ForeignKey('Projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    desc = models.TextField()
    relation = models.ManyToManyField('self')
    block_relation = models.ForeignKey(Block, on_delete=models.CASCADE)
    scenario_relation = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, default=None)
    image_1 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Projects(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image_1 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='image/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
