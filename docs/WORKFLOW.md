# Work and verification

Stable main initially imports exact accepted Lua bytes. Future changes feature/* or research/*, tests then exact candidate commit/hash, installation only with closed game, explicit user runtime acceptance before main. Each <ModName>/VERSION owns its mod version; increment for changed handed payload, never overwrite an old numbered artifact. Historical v1..v7 names remain historical local identities, not retrospective semantic releases. Bootstrap published no package. CombatHUD 0.2.0 is accepted stable Lua in main; its first package is verified locally, with public release publication pending explicit permission; subsequent stable promotion follows DevRules, using a component-scoped tag such as CombatHUD-v0.2.0 and the exact accepted payload. Other mods have independent acceptance and packaging gates.

Tests: Python3 + requirements-test.txt, run python tools/test.py (all available tests), or python tools/test.py SoulsEnemyHUD for one mod. The initial folder migration adapted source-path references without changing the imported Lua; later runtime changes are recorded in each mod's status and candidate history. Mock tests prove syntax, policies and API adaptation only, not real engine rendering. Local Lupa runtime is external and ignored. No new CI required to move already tested code; read CI_POLICY.md if adding it.

Installation: use local environment paths, inspect process state and installed identity; preserve current payload outside loader dirs, install only same-component files, verify hashes, record candidate and retain rollback. Never launch automatically: user's standing instruction is self-launch. Never hot-reload these widgets without cleanup. No installer is scaffolded at bootstrap.

ProfileRender and subtitle currently have accepted local payloads and historical build scripts/evidence under .local. Profile historical patch-targets.py defaults to1920×2160 and must NOT be used as a1600×1800 builder. A portable parameterized build recipe remains pending before changing/releasing those assets. No false claim of clean fully reproducible asset builds.

One active writer per checkout; new chat reads AGENTS.md, current docs, Git state and actual files. A chat is not the source of truth. GitHub synchronization provides off-machine backup of tracked source/docs only; ignored local evidence/assets need their separate local archive.


## Concurrent chats

Folder separation is product organization, not concurrency isolation. Use one writer per checkout. Before starting a second writing task, inspect live task ownership and Git status; create/reuse a separate worktree and branch for it. Each chat states its target mod and checkout. A worktree must have its own ignored environment configuration pointing to external local research/tool dependencies as needed; never copy proprietary material into Git. Shared root documentation and integration are serialized. Game installation is also serialized across worktrees and requires a closed host. Read-only investigation may run independently. Do not switch/reset another chat’s branch or claim its edits.

This folder migration was performed in the original clean checkout; the visible other active task belonged to a different repository. If a further Asterigos writer appears, establish its checkout before edits.
