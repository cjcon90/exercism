import re


class PhoneNumber:

    def __init__(self, number:str) -> None:
        self.number = self.cleaned_number(number)
        self.area_code = self.number[:3]
        self.prefix = self.number[3:6]
        self.line_number = self.number[6:]

    def cleaned_number(self, number: str) -> str:
        
        cleaned = re.sub("^\\+?1|\\D", '', number)

        if len(cleaned) != 10:
            raise ValueError("Invalid phone number length")
        if cleaned[0] in ['0', '1']:
            raise ValueError("Invalid Area Code")
        if cleaned[3] in ['0', '1']:
            raise ValueError("Invalid Phone Number")

        return cleaned

    def pretty(self):
        return f"({self.area_code})-{self.prefix}-{self.line_number}"

