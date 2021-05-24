from typing import ClassVar
from django.db import models

# Create your models here.

class Destination:
    id: int
    name : str
    desc : str
    img : str
    price : int