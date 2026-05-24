import pandas as pd
import matplotlib.pyplot as plt
import os


class SalesAnalyzer:
    #df = data frame  tabulka s daty
    
    '''
    kontrola dat
    self._check_data_loaded()
        assert self.df is not None

    šlo by to i přes property: 
  @property
def data(self):

    if self.df is None:
        raise ValueError()

    return self.df
    musí se použít self.data
    '''
    

    def __init__(self, working_dir, file_name):
        self.working_dir = working_dir
        self.file_name = file_name
        self.df = None

    def _check_data_loaded(self):
        if self.df is None:
            raise ValueError("Data nejsou načtena")   

    def setup_directory(self):
        os.chdir(self.working_dir)

    def load_data(self):
        self.df = pd.read_csv(self.file_name)

    def calculate_total_price(self):
        self._check_data_loaded()
        assert self.df is not None
        self.df["total_price"] = (
            self.df["price"] * self.df["quantity"])

    def get_total_revenue(self):
        self._check_data_loaded()
        assert self.df is not None
        return self.df["total_price"].sum()

    def revenue_by_product(self):
        self._check_data_loaded()
        assert self.df is not None
        return self.df.groupby("product")["total_price"].sum()

    def revenue_by_region(self):
        self._check_data_loaded()
        assert self.df is not None
        return self.df.groupby("region")["total_price"].sum()

    def export_to_excel(self, output_file):
        self._check_data_loaded()
        assert self.df is not None
        self.df.to_excel(output_file, index=False)
        os.startfile(output_file)

    def plot_revenue_by_product(self):
        revenue = self.revenue_by_product()

        revenue.plot(kind="bar")

        plt.title("Tržby podle produktu")
        plt.xlabel("Produkt")
        plt.ylabel("Tržby (Kč)")
        plt.tight_layout()
        plt.show()


# ----------------------------
# Použití programu
# ----------------------------

analyzer = SalesAnalyzer(
    working_dir=r"C:\Users\rihab\Desktop\PROJEKT_DATOVA_ANALYZA\data",
    file_name="data.csv"
)

analyzer.setup_directory()

analyzer.load_data()

analyzer.calculate_total_price()

print(f"Celkové tržby: {analyzer.get_total_revenue()} Kč")

print("\nTržby podle produktu:")
print(analyzer.revenue_by_product())

print("\nTržby podle regionu:")
print(analyzer.revenue_by_region())

analyzer.export_to_excel("data_updated.xlsx")

analyzer.plot_revenue_by_product()