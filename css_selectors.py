def _more_button_selector(reel_idx: int) -> str:
    child_n = 2 * reel_idx + 1

    # In a personal browser tab I've seen the following selector instead of the currently in use one.
    # If we ever recreate this in selenium the following selector should be unioned with the current
    # selector so we don't ever get stuck on a reel.
    # In the meantime, leave the selector here, until we've found a conclusive answer to this discrepancy.
    # f"div.x1bhewko:nth-child({child_n}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1)"

    return f"div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div:nth-child({child_n}) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x12nagc.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x6s0dn4.x1oa3qoh.x13a6bvl.x16n37ib.x1247r65 > div:nth-child(5) > div"


selectors = {
    "more_button": _more_button_selector,
    "copy_link": "div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div > button:nth-child(4)",
}
