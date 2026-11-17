"""Synthetic report lookup for the Attack Hard Problems exercise."""

REPORTS = {
    ("orchard", 17): "Orchard summary",
    ("harbor", 17): "Harbor summary",
    ("harbor", 24): "Harbor inventory",
    ("orchard", 42): "Orchard forecast",
    ("harbor", 42): "Harbor forecast",
}


class ReportService:
    def __init__(self, reports):
        self.reports = reports
        self.cache = {}

    def get_report(self, workspace, report_id):
        if report_id not in self.cache:
            self.cache[report_id] = self.reports.get((workspace, report_id))
        return self.cache[report_id]


if __name__ == "__main__":
    service = ReportService(REPORTS)
    for workspace, report_id in [("orchard", 17), ("harbor", 17), ("harbor", 24)]:
        print(f"{workspace}/{report_id} -> {service.get_report(workspace, report_id)}")
