from django.views.generic import DetailView, ListView, FormView, CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forms import UserMemberAdminForm, RegisterMemberForm
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

class MemberCreateView(CreateView):
    queryset = models.Member.objects.all()
    model = models.Member
    form = RegisterMemberForm()
    extra_context = "member"

member_create_view = MemberCreateView.as_view()

@login_required
def member_change_view(request, *args, **kwargs):
    """
    A custom form view for updating
    """
    data = request.POST or None
    form = UserMemberAdminForm(data=data)
    try:
        member = models.Member.objects.get(slug=kwargs['slug'])
        if data is None:
            form = UserMemberAdminForm(data,instance=member)
    except models.Member.DoesNotExist:
        return HttpResponse(status=404)
    if request.user.is_superuser:
        if form.is_valid():
            mem = form.save()
            return redirect(mem.get_absolute_url())
        ret = dict(member=member,form=form)
        return render(request, 'memdir/member_form_change.html', ret)
    else:
        try:
            muser = models.MemberUser.objects.get(user=request.user)
        except models.MemberUser.DoesNotExist:
            return HttpResponse(status=404)
        if muser in member.users.all():
            if form.is_valid():
                mem = form.save()
                return redirect(mem.get_absolute_url())
            ret = dict(member=member,form=form)
            return render(request, 'memdir/member_form_change.html', ret)
        else:
            return HttpResponse(status=403)

