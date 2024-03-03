import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_model import group_model


class ReportingTest(unittest.TestCase):
    
    # Тест для проверки статического метода build класса reporting
    def test_reporting_build_method(self):
        # Подготовка данных
        data = {}
        units_list = []  # Список единиц измерения
        unit = unit_model.create_gram()  # Создание экземпляра единицы измерения в граммах
        units_list.append(unit)
        data[storage.unit_key()] = units_list  # Добавление списка единиц измерения в данные
        
        # Действие
        result = reporting.build(storage.unit_key(), data)
        
        # Проверки
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
    # Тест для проверки формирования отчета в CSV формате по единицам измерения
    def test_csv_create_unit_report(self):
        # Подготовка данных
        data = {}
        units_list = []  # Список единиц измерения
        unit = unit_model.create_gram()  # Создание экземпляра единицы измерения в граммах
        units_list.append(unit)
        key = storage.unit_key()
        data[key] = units_list
        manager = settings_manager()
        report = csv_reporting(manager.settings, data)
        
        # Действие
        result = report.create(key)
        
        # Проверки
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
    # Тест для проверки формирования отчета в CSV формате по номенклатуре
    def test_csv_create_nomenclature_report(self):
        # Подготовка данных
        data = {}
        nomenclature_list = []  # Список номенклатур
        unit = unit_model.create_killogram()  # Создание экземпляра единицы измерения в килограммах
        group = group_model.create_default_group()
        item = nomenclature_model("Куриное филе", group, unit)
        nomenclature_list.append(item)
        key = storage.nomenclature_key()
        data[key] = nomenclature_list
        manager = settings_manager()
        report = csv_reporting(manager.settings, data)
        
        # Действие
        result = report.create(key)
        
        # Проверки
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
