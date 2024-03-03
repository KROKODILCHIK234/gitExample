from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception

class csv_reporting(reporting):
    
    def create(self, typeKey: str, output_file_path: str):
        super().create(typeKey)
        result = ""
        delimetr = ";"

        # Исходные данные
        items = self.data.get(typeKey)
        if not items:
            raise operation_exception("Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Нет данных!")
        
        # Заголовок 
        header = delimetr.join(self.fields)
        result += f"{header}\n"
        
        # Данные
        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""
                    
                row += f"{value};"
                
            result += f"{row[:-1]}\n"
        
        # Запись результата в файл CSV
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(result)
        
        return True
