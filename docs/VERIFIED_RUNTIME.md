# Общие сведения о runtime

Target: Steam1.09/build12996889, UE4.27, Windows x64. External UE4SS v3.0.1-1181-g83330635 and UEHelpers. Runtime mutations only on the game thread, validate object class/lifetime, fail safely. No automatic game launch, termination or hot reload without a verified cleanup mechanism.

Feature-specific identifiers and accepted observations remain owned by <ModName>/docs/VERIFIED_RUNTIME.md. This file records existing accepted evidence and module entry points; the canonical cross-mod knowledge index is now [NikichMods/Asterigos-Research/docs/RESEARCH_INDEX.md](https://github.com/NikichMods/Asterigos-Research/blob/main/docs/RESEARCH_INDEX.md). Consult both where relevant and promote newly accepted reusable findings to Research; preserve originating evidence and avoid competing copies.

DX11 removed stationary black flicker on rough rocks in user tests; DX12 root cause was not proved. Smooth Motion still120FPS. Local paths, raw evidence and proprietary game files stay under ignored root .local and the historical archive. Other host builds remain unverified.
