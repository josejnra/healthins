from app.common.data_source_abstract import DataSourceAbstract


class HealthInsuranceStatistics:

    def __init__(self, data_source: DataSourceAbstract):
        self.data_source = data_source

    def get_data(self, *args, **kwargs):
        return self.data_source.get(*args, **kwargs)
