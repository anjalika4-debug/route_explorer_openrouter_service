&#x20;Voxgig SDK Developer Experience Report



\## Project



\*\*OpenRouteService SDK\*\*



\## API Selection



I selected the OpenRouteService API because it did not have an SDK listed in the Voxgig open-source SDK catalogue at the time of this project.



The OpenRouteService API provides routing and geospatial services, and an OpenAPI/Swagger definition was available for use with the Voxgig SDK generator.



\## Generator Experience



I used the Voxgig SDK generator to create the SDK project from the OpenRouteService OpenAPI definition.



The generator created a structured SDK project containing the Voxgig SDK generation configuration, model files, tests, documentation-related files, and project configuration.



The generated project was then committed to GitHub under an MIT License.



\## Issue Encountered



The main issue occurred during automatic dependency installation on Windows.



The Voxgig generator reported:



`Failed to start npm: spawn npm ENOENT`



The system had Node.js and npm installed and npm could be executed normally from PowerShell. The problem occurred specifically when the generator attempted to start npm as a child process.



\## Workaround



I entered the generated `.sdk` directory and ran:



`npm install`



manually.



The installation completed successfully and generated the required dependencies and post-install files.



\## Developer Experience Observations



The generator was able to create a substantial SDK project from the OpenAPI definition, including the internal Voxgig model structure and supporting project files.



The main friction point was the automatic npm installation step on Windows. Having a clear fallback instruction for manually running `npm install` could make the experience easier when the generator cannot start npm automatically.



The generated project also contains a relatively large number of files, so it can initially be difficult for a new developer to understand which files are generated configuration, model files, tests, and SDK-related source files.



\## Time-boxing



The task instructions specified a maximum of 30 minutes of human work. I treated the 30-minute limit as a time-box for the implementation and did not count automated generation, dependency installation, or environment-related troubleshooting as additional SDK development work.



The Windows npm process-spawning issue was documented rather than treated as a reason to modify the generated SDK manually.



\## Repository



The completed project is available in my GitHub repository:



`https://github.com/anjalika4-debug/route\_explorer\_openrouter\_service`



\## Conclusion



Overall, the Voxgig SDK generator successfully produced the OpenRouteService SDK project from the API definition. The main issue I encountered was the Windows `spawn npm ENOENT` error during automatic installation, which I worked around by installing the dependencies manually inside the generated `.sdk` directory.



I have documented this issue because it was the most significant part of my developer experience with the generator.



