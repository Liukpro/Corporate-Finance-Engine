def resolve_inputs(raw):

    return {
        # OPERATIVO
        "ric_op_mon": raw["ric_op_mon"],
        "cost_op_mon": raw["cost_op_mon"],
        "ammort": raw["ammort"],

        # TAX / FINANZA
        "tax": raw["imp"],
        "oneri_finanz": raw["of"],

        # BALANCE SHEET
        "patrimonio_netto": raw["pat_net"],
        "debiti_finanz": raw["deb_f"],
        "liquidity": raw["liq"],

        # CASH FLOW
        "ccno1": raw.get("ccno", 0),  # se non hai serie storica
        "ccno2": raw.get("ccno", 0),

        # EXTRA
        "dividendi": raw.get("div", 0),
        "quota_rimbors_capital": raw.get("rimb_cap", 0),
    }
