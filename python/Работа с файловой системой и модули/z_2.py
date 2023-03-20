with open("visit_log.csv", "r", encoding = "utf-8") as f1:
    with open("funne.csv", "w", encoding = "utf-8") as f2:
        for i in f1:
            visits = i.strip().split(",")
            category = purchases.get(visits[0])
            if category != None:
                f2.write(",".join(visits.append(category)))
            else:
