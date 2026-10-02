OpenRouteService SDK
A Voxgig SDKGen project for generating an SDK from the OpenRouteService API definition.
Overview
This project was created as part of a Voxgig SDK task to generate an open-source SDK for an API that was not already represented in the Voxgig SDK catalogue.
The selected API is OpenRouteService, a routing and geospatial services API.
The project uses the OpenRouteService API definition as the source for Voxgig SDKGen and generates SDK implementations and supporting model files.
API
OpenRouteService
The API definition used for SDK generation is included in:
openrouteservice-sdk/.sdk/def/openrouteservice-openapi3.yml

The original API definition used during development is also included in the repository as:
openapi.json

Generated SDKs
Voxgig SDKGen generated SDK implementations for:
TypeScript — openrouteservice-sdk/ts/
Go — openrouteservice-sdk/go/
The Voxgig SDK model and generation configuration are contained in:
openrouteservice-sdk/.sdk/

Project Structure
.
├── openrouteservice-sdk/
│   ├── .sdk/          # Voxgig SDKGen model and generation configuration
│   ├── go/            # Generated Go SDK
│   └── ts/            # Generated TypeScript SDK
├── openapi.json       # OpenRouteService API definition used during development
├── REPORT.md          # SDKGen observations and development notes
├── LICENSE            # MIT License
└── README.md

SDKGen Process
The project was generated using the Voxgig SDKGen workflow:
Select an API that is not already represented in the Voxgig SDK catalogue.
Obtain the API definition.
Add the API definition to the SDKGen project.
Generate the Voxgig SDK model from the API definition.
Generate SDK implementations for the selected targets.
Review the generated project structure and output.
Document observations and issues encountered during the process.
Generated API Model
The OpenRouteService API definition was successfully processed by the Voxgig API definition generator.
The generation produced API entities, paths, methods and supporting model files that were then used to generate the TypeScript and Go SDKs.
Development Notes
During development, I encountered some tooling issues on Windows, including an npm process launch error and a later multisource_not_found error associated with the test scaffold.
The main OpenRouteService SDK generation completed successfully. The generated TypeScript and Go SDKs are included in this repository.
Further details and observations are documented in REPORT.md.
Original Route Explorer
Before the SDK generation work, this repository also contained a small Python-based OpenRouteService route exploration application.
The original files include:
app.py
requirements.txt
openapi.json
The Python application was used to manually explore the OpenRouteService API and verify routing behaviour before working with the SDKGen workflow.
License
This project is released under the MIT License.
Repository
GitHub:
https://github.com/anjalika4-debug/route_explorer_openrouter_service
