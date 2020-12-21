from django.contrib import admin
from .models import Produit, Marque, Post, Tag

admin.autodiscover()
admin.site.enable_nav_sidebar = False



class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','ordre','is_active','marque' ,'designation', 'reference', 'category')
    prepopulated_fields = {"slug": ("designation",)}
    list_display_links = ('id','designation',)
    list_per_page = 50
    list_editable = ('ordre','is_active')
    list_filter = ('category',)
    search_fields = ('id', 'designation','reference')


admin.site.register(Produit, ProduitAdmin)

@admin.register(Marque)
class MarqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre','tag', 'created_date')
    list_display_links = ('id', 'titre', )
    prepopulated_fields = {"slug": ("titre",)}

@admin.register(Tag)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'tag')




# admin.site.register(Slide, CategoryAdmin)
# admin.site.register(Categorie_produit, CategoryAdmin)
# admin.site.register(Categories_Solution, SolutionCategoryAdmin)
# admin.site.register(SliderAPropos, SliderAProposAdmin)
# admin.site.register(Catalogue, CatalogueAdmin)
# admin.site.register(ContactForm, ContactFormAdmin)
# admin.site.register(Partenaire, PartenairesAdmin)
# admin.site.register(ProduitDetail, ProduitDetailAdmin)
# admin.site.register(Post, PostAdmin)