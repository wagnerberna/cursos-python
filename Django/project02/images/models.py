from django.db import models
from history.models import History

# método para ser add no upload_to
def images_history(instance, file_name):
    return "/".join(["history", str(instance.id_history.id_history)])


#  upload_to
class ImagesHistory(models.Model):
    id_image_history = models.AutoField(primary_key=True)
    image = models.ImageField(blank=False, null=False, upload_to=images_history)
    id_history = models.ForeignKey(
        History,
        related_name="images",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
