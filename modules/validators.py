
def return_model_kkt(kkt_sn_list):
    """принимает список серийных номеров ККТ и возвращает список моделей ККТ"""
    """пример номера ккт 1111110038011111, модель netpay"""
    """пример номера ккт 1111110028001111, модель payonline"""
    result = []
    for sn in kkt_sn_list:
        
        sn = str(sn.strip())
        if len(sn) == 16:
            if sn[6:12] == "003801":
                model = "netpay"
            elif sn[6:12] == "002800":
                model = "payonline"
            else:
                model = "unknown"
        else:
            model = "len not 16"
        result.append(model)
    return result
print(return_model_kkt(["1111110038011111","1111110028001111","1111110038011111","1111110028001111"]))