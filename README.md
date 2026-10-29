# Mobile Health Unit Dispatch and Resource Allocation

## Project Overview

This project explores the development of a multi-model AI application for coordinating mobile health services in underserved communities.

The application aims to support mobile health coordinators in understanding incoming service requests, identifying community needs, navigating available resources, and allocating mobile health units when multiple communities compete for limited resources.

## Problem Statement

Coordinating mobile health services involves several interconnected tasks:

- Understanding incoming service requests.
- Identifying required health services and resources.
- Recognizing urgency indicators.
- Considering community locations and mobile health unit availability.
- Prioritizing competing requests when resources are limited.

This project explores how specialized AI models can divide these responsibilities and coordinate their outputs.

## Project Objectives

- Classify incoming service requests.
- Extract relevant information from requests.
- Route requests to appropriate processing components.
- Support resource navigation and dispatch planning.
- Explore multi-model collaboration for resource allocation.
- Maintain human oversight of important decisions.

## Current Development

### Chapter 1: Application Design and Single-Model Baseline

Implemented:
- Project-specific system prompt.
- Request preparation and validation.
- Structured response format.
- Local mock response for baseline testing.

The structured response includes:
- Request Summary
- Service Need
- Urgency Indicators
- Missing Information
- Recommended Next Step
- Human Review Required

The current baseline is a mock implementation and does not call an actual AI model.

### Chapter 2: Intent Classification and Routing

Implemented:
- Intent classification prompt.
- Local keyword-based mock classifier.
- Six request categories:
  - routine_service_request
  - resource_navigation
  - dispatch_coordination
  - potentially_urgent
  - general_question
  - unclear
- Routing based on intent and confidence.

| Request category | Processing route |
|---|---|
| Routine service request | Simple response |
| General question | Simple response |
| Resource navigation | Planning assistant |
| Dispatch coordination | Planning assistant |
| Potentially urgent | Emergency escalation |
| Unclear or low-confidence request | Human review |

The keyword classifier is for prototyping only. It is not a validated medical or emergency detection system.

## Proposed Multi-Model Architecture

The next phase will extend the prototype into a multi-model AI system.

1. **Intent Classification Model:** Identifies the type of request and selects the processing path.
2. **Request Understanding Model:** Extracts service requirements, community location, resource needs, and missing information.
3. **Resource and Dispatch Planning Model:** Evaluates available units, resource constraints, and competing requests to support allocation recommendations.
4. **Response Generation Model:** Produces structured explanations and recommendations for coordinators.

The final model selection and integration strategy will be established during implementation.

## Intended Workflow

```text
Incoming Community Request
            |
            v
    Intent Classification
            |
            v
       Request Router
            |
     +------+------+
     |      |      |
     v      v      v
 Routine  Resource Dispatch
 Request  Navigation Planning
     |      |      |
     +------+------+
            |
            v
     Response Generation
            |
            v
     Human Coordinator
            |
            v
        Final Action


Potentially urgent requests will follow a separate escalation path for appropriate emergency assistance and human review.

This is the proposed architecture, not a fully implemented multi-model system.
Repository Stru