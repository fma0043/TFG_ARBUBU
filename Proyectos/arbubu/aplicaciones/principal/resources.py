 from import_export import resources
 from .models import Individuos

 class IndividuoResource(resources.ModelResource):
   class Meta:
     model = Individuos
