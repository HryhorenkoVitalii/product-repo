import time

from celery import shared_task
from PIL import Image

from .models import Product


@shared_task
def upload_logo(product_uuid):
    product = Product.objects.get(pk=product_uuid)
    start_time = time.time()
    if img_path := product.logo:
        with Image.open(img_path) as im:
            im.rotate(180).save(str(img_path), "JPEG")
    product.rotate_duration = time.time() - start_time
    product.save()
