#!/usr/bin/env python3

import connexion
from dynamic_orchestrator import encoder
from dynamic_orchestrator.core.concrete_orchestrator import ConcreteOrchestrator

def main():  
    options = {"swagger_ui": False}
    app = connexion.App(__name__, specification_dir='./', options = options)
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['UPLOAD_FOLDER'] = './'
    app.app.config['ORCHESTRATOR'] = ConcreteOrchestrator() 
    app.add_api('dynamic_orchestrator.yaml', arguments={'title': 'OpenApi 3.0 ReST interface for Accordion Orchestrator'}, pythonic_params=True)
    app.run(port=8080)
if __name__ == '__main__':
    main()