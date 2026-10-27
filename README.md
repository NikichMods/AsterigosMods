# AsterigosMods

Interface and visual improvements for **Asterigos: Curse of the Stars**, tested locally with Steam1.09/build12996889 on Windows x64 (UE4.27).

- **CombatHUD 0.2.0:** lower HUD fades to 20% outside combat; damage reveals it immediately, and health plus all three quick-item slots stay bright while HP is incomplete. One-second transitions and native menu hiding are preserved.
- **SoulsEnemyHUD:** compact enemy health bars, a separate lock-on dot and accumulated damage numbers using EB Garamond. Native large floating damage numbers are suppressed.
- **SubtitleSoftEdges:** soft fading edges for the controllable dialogue backdrop.
- **ProfileRender:** documented1600×1800 portrait render-target settings.
- **AnimationRate:** Engine.ini setting used to improve distant enemy animation updates.
- **Immersive Interaction Prompts (research):** planned Aphes-world lettering above readable localized interaction actions.

**Current availability:** [accepted CombatHUD 0.2.0 source](https://github.com/NikichMods/AsterigosMods/tree/CombatHUD-v0.2.0/CombatHUD); its verified ZIP is prepared locally, with public package publication pending. Other components provide source/development documentation; their owned status pages record acceptance and packaging availability. CombatHUD and SoulsEnemyHUD require external UE4SS v3.0.1-1181-g83330635 and its UEHelpers module. Asset-based components currently require local game resources and do not yet have a portable build pipeline. Game assets, fonts and third-party costume/texture mods are not included.

**Boss HUD:** SoulsEnemyHUD 0.2.0 corrects duplicate boss bars and adds matching boss-bar colors and accumulated damage. See its [owned status](SoulsEnemyHUD/docs/STATUS.md) for tested identity, acceptance and promotion state.

Developer checks: Python3, dependencies from requirements-test.txt, then `python tools/test.py`. These checks cover logic and mocked API integration, not actual game rendering or compatibility with other game builds.

- [Current state](docs/CURRENT_STATE.md)
- [Adopted behavior](docs/REQUIREMENTS.md)
- [Verified runtime findings](docs/VERIFIED_RUNTIME.md)
- [Development and installation workflow](docs/WORKFLOW.md)
- [License scope](LICENSING.md) — original code under MPL-2.0.


## Independent mod folders

- [CombatHUD](CombatHUD/README.md)
- [SoulsEnemyHUD](SoulsEnemyHUD/README.md)
- [ProfileRender](ProfileRender/README.md)
- [SubtitleSoftEdges](SubtitleSoftEdges/README.md)
- [AnimationRate](AnimationRate/README.md)
- [Immersive Interaction Prompts](ImmersiveInteractionPrompts/README.md) — design and UI-owner research; no build yet.

Each folder owns its code or recipe, tests when available, requirements, status and VERSION. There is no mandatory all-in-one installation. For concurrent development use separate worktrees; see docs/WORKFLOW.md.
