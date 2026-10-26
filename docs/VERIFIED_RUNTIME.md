# Общие сведения о runtime

Target: Steam1.09/build12996889, UE4.27, Windows x64. External UE4SS v3.0.1-1181-g83330635 and UEHelpers. Runtime mutations only on the game thread, validate object class/lifetime, fail safely. No automatic game launch, termination or hot reload without a verified cleanup mechanism.

Feature-specific identifiers and accepted observations are owned by <ModName>/docs/VERIFIED_RUNTIME.md; consult the owning mod before researching again. This is the shared host-knowledge index; no separate research repository exists.

DX11 removed stationary black flicker on rough rocks in user tests; DX12 root cause was not proved. Smooth Motion still120FPS. Local paths, raw evidence and proprietary game files stay under ignored root .local and the historical archive. Other host builds remain unverified.
