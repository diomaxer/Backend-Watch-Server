from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from requests import Response
from rest_framework import viewsets, request
from users.models import CustomUser
from .models import Images, Product, Sex, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
from .forms import ProductForm, ImageForm
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .serializers import ProductSerializer, ProductSerializer2


# Create your views here.
def all_view(request, *args, **kwargs):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'all.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'watch/detail_view.html'
    context_object_name = 'prod'


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


@login_required
def post(request):
    try:
        ImageFormSet = modelformset_factory(Images,
                                            form=ImageForm, extra=2)

        if request.method == 'POST':

            postForm = ProductForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=Images.objects.none())

            if postForm.is_valid() and formset.is_valid():
                post_form = postForm.save(commit=False)
                post_form.user = request.user
                post_form.save()

                for form in formset.cleaned_data:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect("/")
            else:
                print(postForm.errors, formset.errors)
        else:
            postForm = ProductForm()
            formset = ImageFormSet(queryset=Images.objects.none())
            context = {'postForm': postForm, 'formset': formset}
        return render(request, 'create_product.html', context)
    except KeyError:
        return HttpResponseRedirect("/")
        # return render(request, 'sucsess.html', {})



class ProductSpecsView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def create(self, request, *args, **kwargs):
        product_data = request.data
        new_product = Product.objects.create(
            user=CustomUser.objects.get(id=product_data["user"]),
            name=product_data["name"],
            price=product_data["price"],
            sex=Sex.objects.get(id=product_data["sex"]),
            watch_type=WatchType.objects.get(id=product_data["watch_type"]),
            brand=Brand.objects.get(id=product_data["brand"]),
            equipment=Equipment.objects.get(id=product_data["equipment"]),
            condition=Condition.objects.get(id=product_data["condition"]),
            mex_type=MehType.objects.get(id=product_data["mex_type"]),
            corpus_material=Material.objects.get(id=product_data["corpus_material"]),
            bezel_material=Material.objects.get(id=product_data["bezel_material"]),
            glass=Glass.objects.get(id=product_data["glass"]),
            waterproof=Waterproof.objects.get(id=product_data["waterproof"]),
            dial=Colour.objects.get(id=product_data["dial"]),
            numbers=Numbers.objects.get(id=product_data["numbers"]),
            bracer=Material.objects.get(id=product_data["bracer"]),
            bracer_colour=Colour.objects.get(id=product_data["bracer_colour"]),
            zip_type=ZipType.objects.get(id=product_data["zip_type"]),
            zip_material=Material.objects.get(id=product_data["zip_material"]),

        )
        new_product.save()
        serializer = ProductSerializer(new_product, many=True)
        return Response(serializer.data)
