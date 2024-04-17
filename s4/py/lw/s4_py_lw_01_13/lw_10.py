def kubiki(borya, anya):
    borya = set(borya)
    anya = set(anya)
    return [borya & anya, borya - anya, anya - borya]