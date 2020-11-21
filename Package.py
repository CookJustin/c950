class Package: #Group all data of a package into a package class, store package in ChainingHashTable by Delivery Address
    def __init__(self, package_ID, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight,delivery_status,special_note):
        self.Package_ID = package_ID
        self.Delivery_Address = delivery_address
        self.Delivery_Deadline = delivery_deadline
        self.Delivery_City = delivery_city
        self.Delivery_Zip_Code = delivery_zip_code
        self.Package_Weight = package_weight
        self.Delivery_Status = delivery_status
        self.Special_Note = special_note
