from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class ShopItem(models.Model):
    name = models.CharField(max_length=100)  # Required field for the item's name
    description = models.TextField()  # Required field for a detailed description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Required field for price with up to 10 digits

    def __str__(self):
        return self.name


class ShopItemImage(models.Model):
    shop_item = models.ForeignKey(ShopItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='shop_images/')
    image_name = models.CharField(max_length=255, blank=True)  # Store the name of the image (optional)

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the instance already exists
            old_instance = ShopItemImage.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                old_instance.image.delete(save=False)  # Delete old image
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.shop_item.name}"

@receiver(post_delete, sender=ShopItemImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)  # Delete the file from the file system