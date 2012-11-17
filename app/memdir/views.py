from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponse
import os
import time
import datetime

from memdir import models
from appy.pod.renderer import Renderer
import logging


log = logging.getLogger(__name__)


class MemberDirectoryView(ListView):
    # Abstract Model View
    queryset = models.Member.objects.filter(is_frp_member=True)
    model = models.Member

class LocationDirectoryArchiveView(ListView):
    queryset = models.Location.objects.all()
    model = models.Member
    template_name = "memdir/region_list.html"

    def get_context_data(self, **kwargs):
        object_list = kwargs['object_list']
        context = super(LocationDirectoryArchiveView, self).get_context_data(**kwargs)
        log.info('Object list: %s' % object_list)
        regions = sorted(list(set([location.region for location in object_list])))
        log.info('Regions: %s' % regions)
        context['regions'] = regions
        return context


member_directory_view = LocationDirectoryArchiveView.as_view()


class LocationDetailView(DetailView):
    queryset = models.Location.objects.all()
    model = models.Member
    extra_context = "location"
location_detail_view = LocationDetailView.as_view()


class RegionView(TemplateView):
    template_name = 'memdir/region.html'

    def get_context_data(self, **kwargs):
        region = self.args[0]
        log.info('Looking for region %s' % region)
        context = super(RegionView, self).get_context_data(**kwargs)
        all_locations = models.Location.objects.all()
        regions = sorted(list(set([location.region for location in all_locations])))
        locations = list(models.Location.objects.filter(region=region).order_by('frp_program_name'))
        communities = sorted(list(set([location.community for location in locations])))
        context['region'] = region
        context['regions'] = regions
        context['region_name'] = dict(models.REGION_CHOICES)[region]
        context['communities'] = communities
        context['locations'] = locations
        return context


class CommunityView(ListView):
    template_name = 'memdir/community.html'

    def get_queryset(self):
        community = self.args[0]
        return list(models.Location.objects.filter(community=community).order_by('frp_program_name'))

    def get_context_data(self, **kwargs):
        object_list = kwargs['object_list']
        community = self.args[0]
        context = super(CommunityView, self).get_context_data(**kwargs)
        locations = object_list
        context['community'] = community
        context['locations'] = locations
        if locations:
            region = locations[0].region
            context['region'] = region
            context['region_name'] = dict(models.REGION_CHOICES)[region]
            region_locations = list(models.Location.objects.filter(region=region).order_by('frp_program_name'))
            communities = sorted(list(set([location.community for location in region_locations])))
            context['communities'] = communities
        return context


# Download reports
def report_pdf(request, report_type, member_id, extra_data={}):
    try:
        log.debug('Looking for report %s for member %s' % (report_type, member_id))

        # Populate the context
        if int(member_id):
            member = models.Member.objects.get(pk=int(member_id))
        #members = models.Member.objects.all()
        timestr = time.ctime()
        year = datetime.datetime.now().year

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
    regions_dict = dict(models.REGION_CHOICES)
    region_name = regions_dict.get(region, region)
    rowcouples = []
    couple = []
    for member in models.Member.objects.filter(region=region, is_frp_member=True):
        for location in member.locations.all():
            couple.append(location)
            if len(couple) == 2:
                rowcouples.append(couple)
                couple = []
    if couple:
        couple.append(None)
        rowcouples.append(couple)
    return report_pdf(request, 'provincial-listing', 0, locals())

