for i in data["widgetcode"].keys():
    widget = data["var"][i].copy()
    exec(data["widgetcode"][i])
    data["var"][i] = widget.copy()
    del widget