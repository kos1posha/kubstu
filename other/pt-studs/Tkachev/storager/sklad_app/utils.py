from django.contrib.auth.forms import AuthenticationForm

from sklad_app.forms import CreateProductForm, CreateStorageForm, ProductCountForm, EditStorageForm, RegisterForm, EditProductForm


def get_index_forms(request, csf=None, esf=None, cpf=None, epf=None, pcf=None, af=None, rf=None):
    if request.user.is_authenticated:
        return {
            'create_storage_form': csf or CreateStorageForm(),
            'edit_storage_form': esf or EditStorageForm(),
            'create_product_form': cpf or CreateProductForm(),
            'edit_product_form': epf or EditProductForm(),
            'product_count_form': pcf or ProductCountForm(),
            'init_storage_id': request.session.get('init_storage_id', -1),
        }
    else:
        return {
            'auth_form': af or AuthenticationForm(),
            'register_form': rf or RegisterForm(),
        }
