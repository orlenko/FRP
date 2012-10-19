from django.views.generic import DetailView, ListView
from django.http import HttpResponse
import os
import time

from memdir import models
from appy.pod.renderer import Renderer
from subprocess import call
import logging


log = logging.getLogger(__name__)


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


# Download reports
def report_pdf(request, report_type, member_id, extra_data={}):
    try:
        log.debug('Looking for report %s for member %s' % (report_type, member_id))
        # Make sure the headless soffice is running.
        #call(['soffice',
        #      '--headless',
        #      '"-accept=socket,host=localhost,port=2002;urp;"'])

        # Populate the context
        if int(member_id):
            member = models.Member.objects.get(pk=int(member_id))
        #members = models.Member.objects.all()
        timestr = time.ctime()

        # Generate the file
        dirname = os.path.abspath(os.path.dirname(__file__))
        template_dir = os.path.join(dirname, 'report-templates')
        template = os.path.join(template_dir, '%s.odt' % report_type)
        timestamp = time.time()
        output = template.replace('.odt', '%s.pdf' % timestamp)
        log.debug('Will generate from %s to %s' % (template, output))
        data = {}
        data.update(locals())
        data.update(extra_data)
        log.debug('Creating renderer')
        renderer = Renderer(template, data, output)
        log.debug('Running renderer')
        renderer.run()
        log.debug('Rendering complete')

        # Generate response
        retval = HttpResponse(mimetype='application/pdf')
        retval['Content-Disposition'] = (
            'attachment; filename=%s' % os.path.basename(output)
        )
        reader = open(output, 'rb')
        retval.write(reader.read())

        # Clean up
        reader.close()
        os.unlink(output)
        return retval
    except:
        log.debug('Failed to generate report', exc_info=True)
        raise


def report_region_pdf(request, region):
    regions_dict = dict(models.Member.REGION_CHOICES)
    region_name = regions_dict.get(region, region)
    rowcouples = []
    couple = []
    for member in models.Member.objects.filter(region=region):
        couple.append(member)
        if len(couple) == 2:
            rowcouples.append(couple)
            couple = []
    if couple:
        couple.append(None)
        rowcouples.append(couple)
    return report_pdf(request, 'provincial-listing', 0, locals())
