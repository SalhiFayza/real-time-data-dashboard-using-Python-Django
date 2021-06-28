
from .models import Foo
def my_scheduled_job():
    foo_instance = Foo.objects.create(ph='test',humdit='test',waterTemp='test',temp='test')
