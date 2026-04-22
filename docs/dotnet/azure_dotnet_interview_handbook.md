# Azure + .NET Interview Handbook (Canonical Docs Entry)

## Overview
This page brings the existing `.NET/Azure` interview handbook into the main `docs` navigation structure.

Primary source content:
- `02-dotnet/azure-dotnet-interview-handbook.md`

## Quality Review Status
The source handbook is good and interview-useful for:
- Azure Functions, App Service, Service Bus/Event Grid/Event Hub
- ASP.NET Core fundamentals and performance
- C# async/runtime concepts
- SQL optimization basics
- architecture modernization talking points

## Corrections Already Applied
The following technical corrections are already updated in source file:
- Function timeout guidance is treated as **plan-dependent**.
- Service Bus queue semantics are clarified as **point-to-point with competing consumers**.
- Event Grid wording is clarified for **event notification/retry behavior**.

## Gaps Still Remaining (if you want full normalization)
To fully match your strict repository answer standard, the source file still needs:
- per-question `Question summary` for all sections
- `Trusted reference links` for each question
- deeper paragraph-style explanation per question in the same consistent template
- normalized 50-question bank style (currently mixed: deep sections + grouped question list)

## Recommended Use
- Use `02-dotnet/azure-dotnet-interview-handbook.md` now for active prep.
- If you want strict normalization, convert each topic/question into your mandatory 6-part format in follow-up passes.

## Related Topics
- [Compute Architecture Decisions](../compute/compute_architecture.md)
- [Integration: APIM, Messaging, Eventing](../integration/apim_messaging_eventing.md)
- [Security, IAM, Networking](../security/security_iam_networking.md)
- [System Design HLD/LLD](../system-design/system_design_hld_lld.md)
