from django.contrib import admin
from .models import Produit

admin.autodiscover()
admin.site.enable_nav_sidebar = False



class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','ordre' ,'designation', 'reference', 'category')
    prepopulated_fields = {"slug": ("designation",)}
    list_display_links = ('id','designation',)
    list_per_page = 40
    list_editable = ('ordre',)
    list_filter = ('category',)
    search_fields = ('id', 'designation','reference')


admin.site.register(Produit, ProduitAdmin)

# admin.site.register(Slide, CategoryAdmin)
# admin.site.register(Categorie_produit, CategoryAdmin)
# admin.site.register(Categories_Solution, SolutionCategoryAdmin)
# admin.site.register(SliderAPropos, SliderAProposAdmin)
# admin.site.register(Catalogue, CatalogueAdmin)
# admin.site.register(ContactForm, ContactFormAdmin)
# admin.site.register(Partenaire, PartenairesAdmin)
# admin.site.register(ProduitDetail, ProduitDetailAdmin)
# admin.site.register(Post, PostAdmin)