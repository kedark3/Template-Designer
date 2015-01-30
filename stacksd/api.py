# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import yaml
from openstack_dashboard.api import heat

from openstack_dashboard.dashboards.project.stacksd import mappings
from openstack_dashboard.dashboards.project.stacksd import sro
import tkMessageBox
import string
import random

class Stack(object):
    def __init__(self, id, name, status, status_reason):
        self.stack_id = id
        self.stack_name = name
        self.stack_status = status
        self.stack_status_reason = status_reason

class Resource(object):
    def __init__(self, name, status, status_reason, type):
        self.resource_type = type
        self.resource_name = name
        self.resource_status = status
        self.resource_status_reason = status_reason

a = {0:{}}

d3_data = {"nodes": [], "stack": {}}

resource_image_name = "asdkasd"

def d3_dataa(stack_id=''):
    
    #tkMessageBox.showinfo(title="Greetings", message="Hello World! from lb1\n" + str(len(d3_data['nodes'])))
    if stack_id == "e75ea590-dcc0-4989-8550-87d206b21970":
        while d3_data['nodes']:del d3_data['nodes'][:]

    return json.dumps(d3_data)

    '''try:
        stack = heat.stack_get(request, stack_id)
    except Exception:
        stack = Stack()
        stack.id = stack_id
        stack.stack_name = request.session.get('stack_name', '')
        stack.stack_status = 'DELETE_COMPLETE'
        stack.stack_status_reason = 'DELETE_COMPLETE'

    try:
        resources = heat.resources_list(request, stack.stack_name)
    except Exception:
        resources = []

    stack = Stack(stack_id,"stack1","Create Complete","Create Complete")
    tkMessageBox.showinfo(title="Greetings", message="Hello World!" + str(stack))
    d3_data = {"nodes": [], "stack": {}}
    
    if stack:
        stack_image = mappings.get_resource_image(stack.stack_status, 'stack')
        stack_image = '/static/dashboard/img/stack-green.svg'
        stack_node = {
            'stack_id': stack_id,
            'name': 'sujay',
            'status': 'SERVER_COMPLETE',
            'image': stack_image,
            'image_size': 60,
            'image_x': -30,
            'image_y': -30,
            'text_x': 40,
            'text_y': ".35em",
            'in_progress': False,
            'info_box': sro.stack_info(stack, stack_image)
        }
        d3_data['stack'] = stack_node
   
    if resource:
        for resource in resources:
            resource_image = mappings.get_resource_image(
                resource.resource_status,
                resource.resource_type)
            resource_status = mappings.get_resource_status(
                resource.resource_status)
            if resource_status in ('IN_PROGRESS', 'INIT'):
                in_progress = True
            else:
                in_progress = False
            resource_node = {
                'name': resource.resource_name,
                'status': resource.resource_status,
                'image': resource_image,
                'required_by': [],
                'image_size': 50,
                'image_x': -25,
                'image_y': -25,
                'text_x': 35,
                'text_y': ".35em",
                'in_progress': in_progress,
                'info_box': sro.resource_info(resource)
            }
            d3_data['nodes'].append(resource_node)
    return json.dumps(d3_data)     '''

def create_instance():
    
    #char = string.ascii_uppercase+string.digits
    #length1=random.randint(5,30)
    #a= 'instance' + str(len(d3_dataa[nodes]).join(map(lambda unused:random.choice(char),range(length1)))
    #tkMessageBox.showinfo(title="Greetings", message="Hello World!" + a)
    a = 'instance'   + str(len(d3_data['nodes']))
    

    resource = Resource(a, "Create Complete", "Create Complete", 'OS::Nova::Server')
    resource_image = mappings.get_resource_image(
                resource.resource_status,
                resource.resource_type)
    resource_status = mappings.get_resource_status(
                resource.resource_status)
    if resource_status in ('IN_PROGRESS', 'INIT'):
        in_progress = True
    else:
        in_progress = False
    resource_node = {
                'name': resource.resource_name,
                'status': resource_status,
                'image': resource_image,
                'required_by': [],
                'image_size': 50,
                'image_x': -25,
                'image_y': -25,
                'text_x': 35,
                'text_y': ".35em",
                'in_progress': in_progress,
                'info_box': sro.resource_info(resource)
            }
    d3_data['nodes'].append(resource_node)
    #return json.dumps(d3_data)

def create_lb():
    
    #char = string.ascii_uppercase+string.digits
    #length1=random.randint(5,30)
    #a= ''.join(map(lambda unused:random.choice(char),range(length1)))
    a = 'loadbalancer'   + str(len(d3_data['nodes']))
    resource = Resource(a, "Create Complete", "Create Complete", 'OS::Nova::LoadBalancer')
    resource_image = mappings.get_resource_image(
                resource.resource_status,
                resource.resource_type)
    resource_status = mappings.get_resource_status(
                resource.resource_status)
    if resource_status in ('IN_PROGRESS', 'INIT'):
        in_progress = True
    else:
        in_progress = False
    resource_node = {
                'name': resource.resource_name,
                'status': resource.resource_status,
                'image': resource_image,
                'required_by': [],
                'image_size': 50,
                'image_x': -25,
                'image_y': -25,
                'text_x': 35,
                'text_y': ".35em",
                'in_progress': in_progress,
                'info_box': sro.resource_info(resource)
            }
    d3_data['nodes'].append(resource_node)

def create_db():
    
    #char = string.ascii_uppercase+string.digits
    #length1=random.randint(5,30)
    #a= ''.join(map(lambda unused:random.choice(char),range(length1)))
    a = 'database'   + str(len(d3_data['nodes']))

    resource = Resource(a, "Create Complete", "Create Complete", 'OS::Nova::Database')
    resource_image = mappings.get_resource_image(
                resource.resource_status,
                resource.resource_type)
    resource_status = mappings.get_resource_status(
                resource.resource_status)
    if resource_status in ('IN_PROGRESS', 'INIT'):
        in_progress = True
    else:
        in_progress = False
    resource_node = {
                'name': resource.resource_name,
                'status': resource.resource_status,
                'image': resource_image,
                'required_by': [],
                'image_size': 50,
                'image_x': -25,
                'image_y': -25,
                'text_x': 35,
                'text_y': ".35em",
                'in_progress': in_progress,
                'info_box': sro.resource_info(resource)
            }
    d3_data['nodes'].append(resource_node)

def create_ins(dict):
    #env=kwargs.get('environment_so4')
    #kwargs.get('data')
    
    fo=open("template1","w")
    yaml.safe_dump(dict,fo,encoding='utf-8',allow_unicode=True,default_flow_style=False)
    fo.close()
    #temp = int(resource_image_name[-1])
    
    #a[temp]=dict

    #    return HttpResponse(kwargs)

def record_names(str):
    global resource_image_name 
    resource_image_name = str

    #tkMessageBox.showinfo(title="Greetings", message="Hello World! from lb1\n" + resource_image_name)
def del_node(s):
    #tkMessageBox.showinfo(title="Greetings", message="Hello World! from lb1\n" + s)
    pass

