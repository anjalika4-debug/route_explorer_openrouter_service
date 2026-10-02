# Voxgig SDKGen – OpenRouteService Observations

## API I Selected

I selected **OpenRouteService** because I could not find an existing OpenRouteService SDK in the Voxgig SDK catalogue.

I used the OpenRouteService API definition as the source for generating the SDK.

## My Experience

I worked with the Voxgig SDKGen tooling to generate an SDK from the OpenRouteService API definition.

The process helped me understand how an API definition is converted into a structured SDK model and then into generated SDK code.

The generated project includes TypeScript and Go SDK output, along with the Voxgig `.sdk` model and supporting project files.

## Issues I Faced

The main issue I encountered on Windows was:

`Failed to start npm: spawn npm ENOENT`

Although npm was installed and available from PowerShell, the SDK creation process initially had difficulty starting npm from the generator.

I also encountered a `multisource_not_found` error related to the generated test scaffold. After investigating it, I found that the actual OpenRouteService SDK generation had completed successfully; the remaining error was related to the test scaffold rather than the generated SDK output.

## How I Worked Around It

I investigated the generated `.sdk` structure and ran the relevant SDK generation steps separately instead of relying only on the complete generation command.

I also checked the generated model and output directories to verify that the OpenRouteService API had been converted into SDK components.

This allowed me to successfully generate the TypeScript and Go SDKs.

## My Observations

1. The SDKGen process can generate a substantial amount of project structure automatically from an API definition.
2. The generated `.sdk` model is useful for understanding how Voxgig represents API entities, features, targets and generated components.
3. The Windows error messages were not always immediately clear about the underlying cause, so identifying which stage of the generation process had failed was important.
4. The generated project contains many files, which can initially make it difficult to understand which files are source/model files and which are generated output.
5. Separating the main SDK generation from the test scaffold made it easier to identify that the OpenRouteService SDK itself had been generated successfully.
6. Clearer Windows-specific troubleshooting information and a short explanation of the generated project structure would make the initial experience easier for a new SDKGen user.

## 30-Minute Time Box

The initial setup and troubleshooting took longer than the suggested 30-minute time box because of the Windows/npm issue and the generated test-scaffold issue.

However, working through these problems gave me a better understanding of the SDKGen workflow and the relationship between the API definition, `.sdk` model and generated SDK output.

## Repository

GitHub repository:

https://github.com/anjalika4-debug/route_explorer_openrouter_service

The repository contains the generated OpenRouteService SDK and the Voxgig SDKGen project structure.
