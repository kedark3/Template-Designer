# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import logging
from operator import attrgetter

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect  # noqa
from django.utils.translation import ugettext_lazy as _
import django.views.generic

from horizon import exceptions
from horizon import forms
from horizon import tables
from horizon import tabs
from horizon.utils import memoized
from openstack_dashboard import api
from openstack_dashboard.dashboards.project.stacksd \
    import api as project_api
from openstack_dashboard.dashboards.project.stacksd \
    import forms as project_forms    
from openstack_dashboard.dashboards.project.stacksd \
    import tabs as project_tabs
import tkMessageBox


LOG = logging.getLogger(__name__)

#class IndexView(TemplateView):
 #   template_name = 'project/stacksd/index.html'
    #def get_context_data(self, **kwargs):
       #context = super(IndexView, self).get_context_data(**kwargs)
       #context['name'] = "Sujay"
       #return context

class IndexView(tabs.TabView):
    tab_group_class = project_tabs.StacksdTabs
    template_name = 'project/stacksd/index.html'
    
    '''
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def get_tabs(self, request, **kwargs):
        return self.tab_group_class(request, **kwargs)
        '''

class JSONView(django.views.generic.View):
    def get(self, request, stack_id=''):
        #stack_id = "e75ea590-dcc0-4989-8550-87d206b21979"
        return HttpResponse(project_api.d3_dataa(stack_id=stack_id),
                            content_type="application/json")

class ResourcesView(django.views.generic.View):
    def get(self, request, id , str = ''):
        stack_id = "e75ea590-dcc0-4989-8550-87d206b21979"
        stack_id1 = "e75ea590-dcc0-4989-8550-87d206b21970"
        
        if id == '0':
            return HttpResponse(project_api.d3_dataa(stack_id=stack_id1),
                            content_type="application/json")
        elif id == '1':
            project_api.create_instance()
            return HttpResponse(project_api.d3_dataa(stack_id=stack_id),
                            content_type="application/json")
            
        elif id == '2':
            project_api.create_lb()
            return HttpResponse(project_api.d3_dataa(stack_id=stack_id),
                            content_type="application/json")
        
        elif id == '3':
            project_api.create_template()
	    gen_template=project_api.ret_template()
            return HttpResponse(json.dumps(gen_template),content_type="application/json")       
        elif id == '6':
	    #v=project_api.gen_template
            #tkMessageBox.showinfo(title="Greetings", message="\nHERE")
            gen_template=project_api.ret_template()
	    #a=json.dumps(gen_template)
	    #validated=api.heat.template_validate(request,gen_template)
	    #tkMessageBox.showinfo(title="Greetings", message="\nHERE")
	    #tkMessageBox.showinfo(title="Greetings", message="\nHERE\n"+str(gen_template))
	    return HttpResponse(json.dumps(gen_template),content_type="application/json")
        '''
        elif id == '3':
            project_api.create_db()
            return HttpResponse(project_api.d3_dataa(stack_id=stack_id),
                            content_type="application/json")    
        
        elif id == '4':
            pass
            '''
        

class RemoveNode(django.views.generic.View):
    def get(self, request, str = 'sujay bothe' ):
        #tkMessageBox.showinfo(title="Greetings", message="Hello World! From Remove node view: \n" + s)
        project_api.del_node(str)
        return HttpResponseRedirect("/project/stacksd/")        
        
class InstanceFormView(forms.ModalFormView):
    form_class = project_forms.InstanceForm
    template_name = 'project/stacksd/formI.html'
    success_url = reverse_lazy('horizon:project:stacksd:index')
    
    def get_context_data(self, **kwargs):
        context = super(InstanceFormView, self).get_context_data(**kwargs)
        context['str'] = self.get_object()
        return context    

    @memoized.memoized_method
    def get_object(self):
        str = self.kwargs['str']
        #project_api.record_names(str)
        return str

    def get_initial(self):
        str = self.get_object()
        dict = project_api.get_data(str, "instance")
        return {'availability_zone': dict['availability_zone'],
                'instance_name': dict['instance_name'],
                'key_name': dict['key_name'],
                'flavor': dict['flavor'],
		'image': dict['image']
                }

class LoadBalancerFormView(forms.ModalFormView):
    form_class = project_forms.LoadBalancerForm
    template_name = 'project/stacksd/formLB.html'
    success_url = reverse_lazy('horizon:project:stacksd:index')
    
    def get_context_data(self, **kwargs):
        context = super(LoadBalancerFormView, self).get_context_data(**kwargs)
        context['str'] = self.get_object()
        return context

    @memoized.memoized_method
    def get_object(self):
        str = self.kwargs['str']
        return str

    def get_initial(self):
        str = self.get_object()
        dict = project_api.get_data(str, "loadbalancer")
        return {'lb_name': dict['lb_name'],
                'pool_id': dict['pool_id'],
                'protocol_port': dict['protocol_port'],
                'members': dict['members'],
                }    


class TemplateView(django.views.generic.View):
    def get(self, request,str = ''):
        #stack_id = "e75ea590-dcc0-4989-8550-87d206b21979"
        #stack_id1 = "e75ea590-dcc0-4989-8550-87d206b21970"
        project_api.create_template(str)
	gen_template=project_api.ret_template()
        #gen_template=project_api.ret_template()	
        #tkMessageBox.showinfo(title="Greetings", message="\nHERE")
	    #tkMessageBox.showinfo(title="Greetings", message="\nHERE\n"+str(v))
	    #return HttpResponse(project_api.d3_dataa(stack_id=stack_id),content_type="application/json")
        #return HttpResponseRedirect("/project/stacksd/")
	return HttpResponse(json.dumps(gen_template),content_type="application/json")

'''
class DatabaseFormView(forms.ModalFormView):
    form_class = project_forms.DatabaseForm
    template_name = 'project/stacksd/formD.html'
    success_url = reverse_lazy('horizon:project:stacksd:index')
    
    def get_context_data(self, **kwargs):
        context = super(DatabaseFormView, self).get_context_data(**kwargs)
        context['str'] = self.get_object()
        return context

    @memoized.memoized_method
    def get_object(self):
        str = self.kwargs['str']
        return str

    def get_initial(self):
        str = self.get_object()
        dict = project_api.get_data(str, "database")
        return {'database_name': dict['database_name'],
                'flavor': dict['flavor'],
                }    

   '''             
