from django.db import models


class Room(models.Model):
	name = models.CharField(max_length=200, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	old_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0.00)
	home_adress = models.CharField(max_length=200, unique=True)
	House_number = models.IntegerField()
	entrance_number = models.IntegerField()
	apartment_number = models.IntegerField()
	total_floors = models.IntegerField()
	floor = models.IntegerField()
	flat_area = models.IntegerField()
	kitchen_area = models.IntegerField()
	living_space = models.TextField()
	# slug               =models.SlugField(max_length=200,unique=True)
	author = models.CharField(max_length=200)
	publisher = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True)

	quantity = models.IntegerField()
	image = models.ImageField(upload_to='product/', blank=True)
# meta_keywards = models.CharField("meta_keyward",max_length=255,help_text='Comma-delimited of SEO keywards for meta tag')
# meta_description = models.CharField("meta_description",max_length=255,help_text='content for meta tag')

# categories          =models.OneToManyField(category_name)
