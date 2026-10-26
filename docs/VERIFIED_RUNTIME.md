# Runtime evidence — Steam1.09/build12996889, UE4.27

Facts below come from local asset inspection, runtime logs and user tests in the legacy archive. Local evidence locations/hashes: .local/baseline.json, .local/evidence and .local/environment.json. No original game dumps are tracked. Revalidate assumptions for other host builds.

## Combat
GameGlobal:GetIsBattleState (/Script/Genesis), CDO Default__GameGlobal, requires GenesisCharacter argument obtained from owning player pawn. Earlier zero-arg/widget attempts were wrong. Targets LeftBottom_Panel, HUDSkillUMG_BP, HUDActiveSkillUMG_BP; game-thread-only operations, bounded discovery and invalid-object handling. UEHelpers is an external runtime dependency.

## Overhead bars and damage
MeterOnHead2_C:Tick under /Game/MainContent/Template/UMG/MeterOnHead2. ownAvatar validates GenesisCharacter; skip player controlled. CurVals/MaxVals/CurColorClasses real arrays use HP index2 in observed Lua runtime; adapter identifies red color class and matches HPBar.Percent, does not blindly assume full bars distinguish health. Observed max HP252/588/420 give widths90/112/102. High HP is not proof of boss status.

Actual large floating digits: /Game/MainContent/Template/UMG/HudUmg.HudUmg_C, dedicated root CanvasPanel contains20 TextBlocks DamageDigits0..19. Hide that root opacity after verified parent relationship; animations remain. MeterOnHead2.DamageText stayed9876; HUDDamageTip_BP had no observed combat instances. Hiding those alone did not solve the symptom. Production no longer scans every numeric text block.

Garamond asset /Game/Fonts/EBGaramond-SemiBold_Font.EBGaramond-SemiBold_Font is UFont, Default typeface references EBGaramond-SemiBold FontFace. FontObject/TypefaceFontName/Size/OutlineSettings set explicitly, no global font change. User accepted size12/outline1.

## Profile, subtitle, renderer
DressRoomRenderTarget and DressRoomRenderTarget_Dup under /Game/MainContent/Act/DressRoom_BP were originally960×1080; current1600×1800. Only SizeX/SizeY changed; independent CUE4Parse decoding and retoc verification passed. Both are used in the preview path; exact full capture/compositing chain not completely traced. Do not infer that two RTs mean two independent full-scene captures.

Subtitle patch resource Genesis/Content/uiresources/Hud.html. CSS-only insertion; original scripts/markup retained. Final pak is local host-derived output, not a source distributable in Git.

DX11 removed stationary black flicker on rough rocks in user tests; DX12 root cause was not proved. Smooth Motion still120FPS. a.URO.Enable=0 improved distant enemy animation per user; actual animation Hz/GPU timings were not measured. Native URO is relevant hypothesis, not universal proof for every distant stutter.
