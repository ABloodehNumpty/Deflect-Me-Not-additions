function Combo_FindAttackInComboTable(r1, r2, b1, b2)
	local WieldingTable = Combo_GetWieldingTable()
	if WieldingTable == nil then
		return nil
	end

	local IsNormal = FALSE
	local ComboTable = nil
	if r1 == RIGHT_DASH1 or r2 == RIGHT_DASH2 or b1 == BOTH_DASH1 or b2 == BOTH_DASH2 then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_DASH_COMBO) == "table" and 0 < #WieldingTable.SUPER_DASH_COMBO then
			ComboTable = WieldingTable.SUPER_DASH_COMBO
		else
			ComboTable = WieldingTable.DASH_COMBO
		end
	elseif r1 == RIGHT_ROLL or b1 == BOTH_ROLL then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_ROLL_COMBO) == "table" and 0 < #WieldingTable.SUPER_ROLL_COMBO then
			ComboTable = WieldingTable.SUPER_ROLL_COMBO
		else
			ComboTable = WieldingTable.ROLL_COMBO
		end
	elseif r1 == RIGHT_STEP or b1 == BOTH_STEP then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_BACKSTEP_COMBO) == "table" and 0 < #WieldingTable.SUPER_BACKSTEP_COMBO then
			ComboTable = WieldingTable.SUPER_BACKSTEP_COMBO
		else
			ComboTable = WieldingTable.BACKSTEP_COMBO
		end
	elseif r1 == RIGHT_STEALTH or b1 == BOTH_STEALTH then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_STEALTH_COMBO) == "table" and 0 < #WieldingTable.SUPER_STEALTH_COMBO then
			ComboTable = WieldingTable.SUPER_STEALTH_COMBO
		else
			ComboTable = WieldingTable.STEALTH_COMBO
		end
	elseif Combo_IsGuardStance() == TRUE then
		Combo_SetGuardStance(FALSE)
		Action_SetSpecialRequest(TRUE)
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_GUARD_STANCE) == "table" and 0 < #WieldingTable.SUPER_GUARD_STANCE then
			ComboTable = WieldingTable.SUPER_GUARD_STANCE
		else
			ComboTable = WieldingTable.GUARD_STANCE
		end
		if GV_Combo.Custom == GC_MODES.MOVESETS_DEFAULT or ComboTable == nil or #ComboTable == 0 then
			ComboTable = GC_COMBO.GUARD_STANCE1
		end
	elseif Action_IsGuardCounterPossible() == TRUE then
		Action_EndGuardCounterStatus()
		ComboTable = WieldingTable.GUARD_COUNTER
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_GUARD_COUNTER) == "table" and 0 < #WieldingTable.SUPER_GUARD_COUNTER then
			ComboTable = WieldingTable.SUPER_GUARD_COUNTER
		else
			ComboTable = WieldingTable.GUARD_COUNTER
		end
		if ComboTable == nil or #ComboTable == 0 then
			if c_Style == HAND_RIGHT_BOTH or c_Style == HAND_LEFT_BOTH then
				ComboTable = GC_COMBO.GUARD_COUNTER2
			else
				ComboTable = GC_COMBO.GUARD_COUNTER1
			end
		end
	else
		IsNormal = TRUE
		if 0 < #Combo_GetComboTable() then
			ComboTable = Combo_GetComboTable()
		else
			if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_NORMAL_COMBO) == "table" and 0 < #WieldingTable.SUPER_NORMAL_COMBO then
				ComboTable = WieldingTable.SUPER_NORMAL_COMBO
			else
				ComboTable = WieldingTable.NORMAL_COMBO
			end
		end
	end

	if ComboTable == nil or #ComboTable == 0 then
		ComboTable = {}
	else
		if Combo_GetComboTable() ~= ComboTable then
			Combo_ShiftComboActions()
			Combo_SwitchComboTable(ComboTable)
		end
	end

	local AttackIndex = 0
	local CurrentActions = Combo_GetComboActions()
	local NextAttack = Combo_FindNextAttack(ComboTable)
	if NextAttack == nil and IsNormal == FALSE then
		Combo_ShiftComboActions()
		NextAttack = Combo_FindNextAttack(ComboTable)
	end

	if NextAttack == nil and WieldingTable.NORMAL_COMBO ~= nil and (1 < #CurrentActions or Action_IsGuardCounterPossible() == TRUE) then
		Combo_ShiftComboActions()
		Combo_SwitchComboTable(WieldingTable.NORMAL_COMBO)
		NextAttack = Combo_FindNextAttack(WieldingTable.NORMAL_COMBO)
	end

	return NextAttack
end