import connexion
import six
from dynamic_orchestrator.converter.Parser import ReadFile
from dynamic_orchestrator.converter.MatchingModel import generate
from dynamic_orchestrator.converter.Converter import namespace,secret_generation, tosca_to_k8s  
from dynamic_orchestrator.models.inline_response500 import InlineResponse500  # noqa: E501
from dynamic_orchestrator.models.request_body import RequestBody  # noqa: E501
from dynamic_orchestrator import util
from  urllib.error import HTTPError
import base64
import json
from flask import current_app
import requests
from dynamic_orchestrator.core.concrete_orchestrator import ConcreteOrchestrator

def choose_application (name):   
    if name == 'accordion-plexus':
        token_name = 'gitlab+deploy-token-420906'
        token_pass = 'jwCSDnkoZDeZqwf2i9-m'
    if name == 'accordion-orbk':
        token_name = 'gitlab+deploy-token-420904'
        token_pass = 'gzP9s2bkJV-yeh1a6fn3'
    if name == 'accordion-ovr':
        token_name = 'gitlab+deploy-token-430087'
        token_pass = 'NDxnnzt9WvuR7zyAHchX'
    return token_name, token_pass

def supported_operation (operation):
    if operation == 'deploy':
        return deploy
    if operation == 'undeploy':
        return undeploy
    return None
    

def secret (name):  
    token_name, token_pass = choose_application(name)
    sample_string = token_name + ":" + token_pass
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    json_file = {
        "auths": {
            "https://registry.gitlab.com": {
                "auth": base64_string
            }
        }
    }
    json_string = json.dumps(json_file)
    json_base64_string = base64.b64encode(json_string.encode('utf-8')).decode("utf-8")
    return json_base64_string

def deploy(body):
    try:
        components = body.app_component_names
        if(components == None):
            error = 'Deploy operation not executed succesfully due to the following error: no application components to be deployed' 
            return {'reason': error}, 400
        
        if(len(components) == 0):
            error = 'Deploy operation not executed succesfully due to the following error: no application components to be deployed'
            return {'reason': error}, 400
        
        RID_response = requests.get('http://localhost:5000/miniclouds', timeout=5)
        RID_response.raise_for_status()
        RID_response = RID_response.json()
        print(RID_response)
        app_component_name = components[0].component_name
        app_component_name_parts = app_component_name.split('-')
        app_version = app_component_name_parts[2]+ '-' + app_component_name_parts[3] + '-'  + app_component_name_parts[4]
        app_name =   app_component_name_parts[0] + '-' + app_component_name_parts[1] + '-' + app_version
        app_instance = app_name + '-' + app_component_name_parts[5]
        
        nodelist, imagelist = ReadFile(body.app_model)
        matchmaking_model = generate(nodelist, app_instance)
        solver = ConcreteOrchestrator()
        
        solver.calculate_dep_plan(components, RID_response, matchmaking_model)

        namespace_yaml = namespace(app_instance)
        secret_yaml = secret_generation(secret(app_name), app_instance)        
        deployment_files, persistent_files, service_files, kustomization_file = tosca_to_k8s(nodelist, imagelist, app_instance)
      
        #print(namespace_yaml)
        #print(secret_yaml)
        #print(deployment_files)
        #print(matchmaking_model)
    except OSError as err:
        if not err:
            error = 'Deploy operation not executed successfully due to the following error: ' + err.strerror
        else:
            error = 'Deploy operation not executed successfully due to an unknown error! '
        return {'reason': error}, 500
    except:
        error = 'Deploy operation not executed successfully due to an unknown error!'
        return {'reason': error}, 500
    return 200

def undeploy(body):
    return 200

def orchestrator_LM_request(body):  # noqa: E501
    """orchestrator_lm_request

    Receive a request from the Lifecycle Manager ACCORDION component # noqa: E501

    :param body: The parameters of the request received from the LM
    :type body: dict | bytes

    :rtype: None
    """
   
    
    if connexion.request.is_json:
        body = RequestBody.from_dict(connexion.request.get_json())  # noqa: E501         
        operation = supported_operation(body.operation)
    if operation == None:
        error = 'Request not executed successfully due to the following error: operation not supported!' 
        return {'reason': error}, 400
    return operation(body)

        #kube_config_file = os.path.join( './config', current_app.config.get('KUBERNETES_CONFIG_FILE'))
        #config.load_kube_config(kube_config_file)
        #k8s_client = client.ApiClient()
        #kustomization_file_path = os.path.join(current_app.config.get('KUBERNETES_FOLDER') , name, 'kustomization.yaml')  
        #kustomization_file = open(kustomization_file_path, 'rb')
  
        #kustomization_file_content = yaml.safe_load(kustomization_file)
        #kustomization_file.close()
        
        #file_path = os.path.join(current_app.config.get('KUBERNETES_FOLDER') , name, '_namespace.yaml') 
        #result = utils.create_from_yaml(k8s_client, file_path, verbose=True, pretty=True)
        #if 'secret.yaml' in kustomization_file_content.get('resources'):
        #    file_path = os.path.join(current_app.config.get('KUBERNETES_FOLDER') , name, 'secret.yaml') 
        #    result = utils.create_from_yaml(k8s_client, file_path, verbose=True, pretty=True)

        #for file_name in kustomization_file_content.get('resources'):
        #    if file_name != 'secret.yaml' and file_name!='_namespace.yaml':
        #        file_path = os.path.join(current_app.config.get('KUBERNETES_FOLDER') , name, file_name) 
        #        result = utils.create_from_yaml(k8s_client, file_path, verbose=True, pretty=True)

    #except utils.FailToCreateError as KubeErr:
    #    error = 'Application ' + name + ' not deployed succesfully due to a Kubernetes error! '
    #    print(KubeErr)
    #    return {'message': error}, 500
    
