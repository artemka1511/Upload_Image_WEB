from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from upload.models import UploadImage
from upload.forms import FileFieldForm


class FileFieldView(LoginRequiredMixin, FormView):
    form_class = FileFieldForm
    template_name = 'upload/index.html'
    success_url = '/upload/'
    model = UploadImage

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                UploadImage.objects.create(image=f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
