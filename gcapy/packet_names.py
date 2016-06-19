# Generated from Scala enum by Vim macro
#   1. Remove trailing comments
#   2. Remove blank lines
#   3. Copy macro
#     kyyp0f,lDJa"ea")j
#   To load, type "<macro register>y$

# id, name, unknown (optional)
game_packet_names = [
(0, "UnknownMessage0", True),
(1, "LoginMessage"),
(2, "LoginRespMessage"),
(3, "ConnectToWorldMessage"),
(4, "ConnectToRequestWorldMessage"),
(5, "VNLWorldStatusMessage"),
(6, "UnknownMessage6", True),
(7, "UnknownMessage7", True),
(8, "PlayerStateMessage"),
(9, "HitMessage"),
(10, "HitHint"),
(11, "DamageMessage"),
(12, "DestroyMessage"),
(13, "ReloadMessage"),
(14, "MountVehicleMsg"),
(15, "DismountVehicleMsg"),
(16, "UseItemMessage"),
(17, "MoveItemMessage"),
(18, "ChatMsg"),
(19, "CharacterNoRecordMessage"),
(20, "CharacterInfoMessage"),
(21, "UnknownMessage21", True),
(22, "BindPlayerMessage"),
(23, "ObjectCreateMessage_Duplicate"),
(24, "ObjectCreateMessage"),
(25, "ObjectDeleteMessage"),
(26, "PingMsg"),
(27, "VehicleStateMessage"),
(28, "FrameVehicleStateMessage"),
(29, "GenericObjectStateMsg"),
(30, "ChildObjectStateMessage"),
(31, "ActionResultMessage"),
(32, "UnknownMessage32", True),
(33, "ActionProgressMessage"),
(34, "ActionCancelMessage"),
(35, "ActionCancelAcknowledgeMessage"),
(36, "SetEmpireMessage"),
(37, "EmoteMsg"),
(38, "UnuseItemMessage"),
(39, "ObjectDetachMessage"),
(40, "CreateShortcutMessage"),
(41, "ChangeShortcutBankMessage"),
(42, "ObjectAttachMessage"),
(43, "UnknownMessage43", True),
(44, "PlanetsideAttributeMessage"),
(45, "RequestDestroyMessage"),
(46, "UnknownMessage46", True),
(47, "CharacterCreateRequestMessage"),
(48, "CharacterRequestMessage"),
(49, "LoadMapMessage"),
(50, "SetCurrentAvatarMessage"),
(51, "ObjectHeldMessage"),
(52, "WeaponFireMessage"),
(53, "AvatarJumpMessage"),
(54, "PickupItemMessage"),
(55, "DropItemMessage"),
(56, "InventoryStateMessage"),
(57, "ChangeFireStateMessage_Duplicate"),
(58, "ChangeFireStateMessage"),
(59, "UnknownMessage59", True),
(60, "GenericCollisionMsg"),
(61, "QuantityUpdateMessage"),
(62, "ArmorChangedMessage"),
(63, "ProjectileStateMessage"),
(64, "MountVehicleCargoMsg"),
(65, "DismountVehicleCargoMsg"),
(66, "CargoMountPointStatusMessage"),
(67, "BeginZoningMessage"),
(68, "ItemTransactionMessage"),
(69, "ItemTransactionResultMessage"),
(70, "ChangeFireModeMessage"),
(71, "ChangeAmmoMessage"),
(72, "TimeOfDayMessage"),
(73, "UnknownMessage73", True),
(74, "SpawnRequestMessage"),
(75, "DeployRequestMessage"),
(76, "UnknownMessage76", True),
(77, "RepairMessage"),
(78, "ServerVehicleOverrideMsg"),
(79, "LashMessage"),
(80, "TargetingInfoMessage"),
(81, "TriggerEffectMessage"),
(82, "WeaponDryFireMessage"),
(83, "DroppodLaunchRequestMessage"),
(84, "HackMessage"),
(85, "DroppodLaunchResponseMessage"),
(86, "GenericObjectActionMessage"),
(87, "AvatarVehicleTimerMessage"),
(88, "AvatarImplantMessage"),
(89, "UnknownMessage89", True),
(90, "DelayedPathMountMsg"),
(91, "OrbitalShuttleTimeMsg"),
(92, "AIDamage"),
(93, "DeployObjectMessage"),
(94, "FavoritesRequest"),
(95, "FavoritesResponse"),
(96, "FavoritesMessage"),
(97, "ObjectDetectedMessage"),
(98, "SplashHitMessage"),
(99, "SetChatFilterMessage"),
(100, "AvatarSearchCriteriaMessage"),
(101, "AvatarSearchResponse"),
(102, "WeaponJammedMessage"),
(103, "LinkDeadAwarenessMsg"),
(104, "DroppodFreefallingMessage"),
(105, "AvatarFirstTimeEventMessage"),
(106, "AggravatedDamageMessage"),
(107, "TriggerSoundMessage"),
(108, "LootItemMessage"),
(109, "VehicleSubStateMessage"),
(110, "SquadMembershipRequest"),
(111, "SquadMembershipResponse"),
(112, "SquadMemberEvent"),
(113, "PlatoonEvent"),
(114, "FriendsRequest"),
(115, "FriendsResponse"),
(116, "TriggerEnvironmentalDamageMessage"),
(117, "TrainingZoneMessage"),
(118, "DeployableObjectsInfoMessage"),
(119, "SquadState"),
(120, "OxygenStateMessage"),
(121, "TradeMessage"),
(122, "UnknownMessage122", True),
(123, "DamageFeedbackMessage"),
(124, "DismountBuildingMsg"),
(125, "UnknownMessage125", True),
(126, "UnknownMessage126", True),
(127, "AvatarStatisticsMessage"),
(128, "GenericObjectAction2Message"),
(129, "DestroyDisplayMessage"),
(130, "TriggerBotAction"),
(131, "SquadWaypointRequest"),
(132, "SquadWaypointEvent"),
(133, "OffshoreVehicleMessage"),
(134, "ObjectDeployedMessage"),
(135, "ObjectDeployedCountMessage"),
(136, "WeaponDelayFireMessage"),
(137, "BugReportMessage"),
(138, "PlayerStasisMessage"),
(139, "UnknownMessage139", True),
(140, "OutfitMembershipRequest"),
(141, "OutfitMembershipResponse"),
(142, "OutfitRequest"),
(143, "OutfitEvent"),
(144, "OutfitMemberEvent"),
(145, "OutfitMemberUpdate"),
(146, "PlanetsideStringAttributeMessage"),
(147, "DataChallengeMessage"),
(148, "DataChallengeMessageResp"),
(149, "WeatherMessage"),
(150, "SimDataChallenge"),
(151, "SimDataChallengeResp"),
(152, "OutfitListEvent"),
(153, "EmpireIncentivesMessage"),
(154, "InvalidTerrainMessage"),
(155, "SyncMessage"),
(156, "DebugDrawMessage"),
(157, "SoulMarkMessage"),
(158, "UplinkPositionEvent"),
(159, "HotSpotUpdateMessage"),
(160, "BuildingInfoUpdateMessage"),
(161, "FireHintMessage"),
(162, "UplinkRequest"),
(163, "UplinkResponse"),
(164, "WarpgateRequest"),
(165, "WarpgateResponse"),
(166, "DamageWithPositionMessage"),
(167, "GenericActionMessage"),
(168, "ContinentalLockUpdateMessage"),
(169, "AvatarGrenadeStateMessage"),
(170, "UnknownMessage170", True),
(171, "UnknownMessage171", True),
(172, "ReleaseAvatarRequestMessage"),
(173, "AvatarDeadStateMessage"),
(174, "CSAssistMessage"),
(175, "CSAssistCommentMessage"),
(176, "VoiceHostRequest"),
(177, "VoiceHostKill"),
(178, "VoiceHostInfo"),
(179, "BattleplanMessage"),
(180, "BattleExperienceMessage"),
(181, "TargetingImplantRequest"),
(182, "ZonePopulationUpdateMessage"),
(183, "DisconnectMessage"),
(184, "ExperienceAddedMessage"),
(185, "OrbitalStrikeWaypointMessage"),
(186, "KeepAliveMessage"),
(187, "MapObjectStateBlockMessage"),
(188, "SnoopMsg"),
(189, "PlayerStateMessageUpstream"),
(190, "PlayerStateShiftMessage"),
(191, "ZipLineMessage"),
(192, "CaptureFlagUpdateMessage"),
(193, "VanuModuleUpdateMessage"),
(194, "FacilityBenefitShieldChargeRequestMessage"),
(195, "ProximityTerminalUseMessage"),
(196, "QuantityDeltaUpdateMessage"),
(197, "ChainLashMessage"),
(198, "ZoneInfoMessage"),
(199, "LongRangeProjectileInfoMessage"),
(200, "WeaponLazeTargetPositionMessage"),
(201, "ModuleLimitsMessage"),
(202, "OutfitBenefitMessage"),
(203, "EmpireChangeTimeMessage"),
(204, "ClockCalibrationMessage"),
(205, "DensityLevelUpdateMessage"),
(206, "ActOfGodMessage"),
(207, "AvatarAwardMessage"),
(208, "UnknownMessage208", True),
(209, "DisplayedAwardMessage"),
(210, "RespawnAMSInfoMessage"),
(211, "ComponentDamageMessage"),
(212, "GenericObjectActionAtPositionMessage"),
(213, "PropertyOverrideMessage"),
(214, "WarpgateLinkOverrideMessage"),
(215, "EmpireBenefitsMessage"),
(216, "ForceEmpireMessage"),
(217, "BroadcastWarpgateUpdateMessage"),
(218, "UnknownMessage218", True),
(219, "SquadMainTerminalMessage"),
(220, "SquadMainTerminalResponseMessage"),
(221, "SquadOrderMessage"),
(222, "SquadOrderResponse"),
(223, "ZoneLockInfoMessage"),
(224, "SquadBindInfoMessage"),
(225, "AudioSequenceMessage"),
(226, "SquadFacilityBindInfoMessage"),
(227, "ZoneForcedCavernConnectionsMessage"),
(228, "MissionActionMessage"),
(229, "MissionKillTriggerMessage"),
(230, "ReplicationStreamMessage"),
(231, "SquadDefinitionActionMessage"),
(232, "SquadDetailDefinitionUpdateMessage"),
(233, "TacticsMessage"),
(234, "RabbitUpdateMessage"),
(235, "SquadInvitationRequestMessage"),
(236, "CharacterKnowledgeMessage"),
(237, "GameScoreUpdateMessage"),
(238, "UnknownMessage238", True),
(239, "OrderTerminalBugMessage"),
(240, "QueueTimedHelpMessage"),
(241, "MailMessage"),
(242, "GameVarUpdate"),
(243, "ClientCheatedMessage")]

control_packet_names = [
(0, "HandleGamePacket"),
(1, "ClientStart"),
(2, "ServerStart"),
(3, "MultiPacket"),
(4, "Unknown4", True),
(5, "Unknown5", True),
(6, "Unknown6", True),
(7, "ControlSync"),
(8, "ControlSyncResp"),
(9, "SlottedMetaPacket0"),
(10, "SlottedMetaPacket1"),
(11, "SlottedMetaPacket2"),
(12, "SlottedMetaPacket3"),
(13, "SlottedMetaPacket4"),
(14, "SlottedMetaPacket5"),
(15, "SlottedMetaPacket6"),
(16, "SlottedMetaPacket7"),
(17, "RelatedA0"),
(18, "RelatedA1"),
(19, "RelatedA2"),
(20, "RelatedA3"),
(21, "RelatedB0"),
(22, "RelatedB1"),
(23, "RelatedB2"),
(24, "RelatedB3"),
(25, "MultiPacketEx"),
(26, "Unknown26", True),
(27, "Unknown27", True),
(28, "Unknown28", True),
(29, "ConnectionClose"),
(30, "Unknown30", True)
]