from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from . import models

class MemberDirectoryView(ListView):
    # Abstract Model View
    queryset = models.Member.objects.all()
    model = models.Member

class MemberDirectoryArchiveView(ListView):
    queryset = models.Member.objects.all()
    model = models.Member
    template_name = "memdir/region_list.html"
member_directory_view = MemberDirectoryArchiveView.as_view()

class RegionContextView(MemberDirectoryView):
    """
        Branched from: https://raw.github.com/gregplaysguitar/django-baseclasses/master/baseclasses/views.py
    """
    ##context_object_name = "region"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(RegionContextView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

# Region Directories
class NorthernDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='northern')
northern_directory = NorthernDirectory.as_view(extra_context=dict(
        region="Northern",
    ))

class OtherDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='other')
other_directory = OtherDirectory.as_view(extra_context=dict(
        region="Other",
    ))

class FraserDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='fraservalley')
fraser_directory = FraserDirectory.as_view(extra_context=dict(
        region="Fraser Valley",
    ))

class InteriorDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='interior')
interior_directory = InteriorDirectory.as_view(extra_context=dict(
        region="Interior BC",
    ))

class VancoastDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='vancoast')
vancoast_directory = VancoastDirectory.as_view(extra_context=dict(
        region="Vancouver Coast",
    ))

class VanisleDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='vanisle')
vanisle_directory = VanisleDirectory.as_view(extra_context=dict(
        region="Vancouver Island",
    ))

class UnknownDirectory(RegionContextView):
    queryset = models.Member.objects.filter(region='unknown')
unknown_directory = UnknownDirectory.as_view(extra_context=dict(
        region="Unknown",
    ))

# Detail view

class MemberDetailView(DetailView):
    queryset = models.Member.objects.all()
    model = models.Member
    extra_context = "member"
member_detail_view = MemberDetailView.as_view()

