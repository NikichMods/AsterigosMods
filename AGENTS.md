# AsterigosMods — project contract

Follow NikichMods/DevRules: start WORKING_RULES.md and action-based reading map; local work also CODEX_WORKFLOW.md. Resolve the local DevRules checkout from ignored .local/environment.json; fallback to canonical GitHub repository. Never copy personal instructions into tracked files.

Target: Asterigos: Curse of the Stars, Steam 1.09/build12996889, UE4.27, Windows x64. UE4SS integration tested with v3.0.1-1181-g83330635. Local accepted baseline uses DX11 and NVIDIA Smooth Motion. Compatibility with other builds unverified.

Read README.md, docs/CURRENT_STATE.md, relevant docs/REQUIREMENTS.md and docs/VERIFIED_RUNTIME.md before implementation. Read docs/WORKFLOW.md for test/installation rules; inspect Git status/branch/HEAD and actual installed bytes before changes. Host research is owned here in docs/VERIFIED_RUNTIME.md; no separate cross-project research repository currently exists. Bounded lookup of sibling repository names during bootstrap found no Asterigos repository.

src owns original Lua and CSS changes. Proprietary host assets, decompiled dumps, extracted fonts, tools, saves, credentials and third-party mods never enter Git. Legacy evidence remains under ignored .local plus the original archive pointer. Runtime/font rendering acceptance cannot be replaced by offline tests.

One active writer per checkout. Preserve accepted behavior; no gameplay/stat changes. Do not launch/terminate the game unless explicitly authorized. Never replace running mod files. Close-game installation must preserve previous payload outside loader paths and compare installed hashes. Do not use UE4SS hot reload without a verified cleanup mechanism.

main is stable. New behavior uses feature/* or research/*; explicit runtime acceptance required before stable promotion. Initial import preserves accepted Lua bytes exactly; no retrospective commit identities. historical-v7 is an old log label, not the new semantic version. VERSION owns future bundle versioning; initial baseline 0.1.0, no released package yet. Handoff identities must include exact commit and payload hashes; numbered artifacts immutable. Initial setup authorizes private GitHub synchronization, not public releases. Public distribution requires a separate scope/provenance review.

MPL-2.0 covers original project code only; see LICENSING.md. Keep host modifications and third-party material local. No hosted CI scaffold during bootstrap; available meaningful offline tests run locally. Before any future CI setup read CI_POLICY.md.
