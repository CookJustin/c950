import Package
class ChainingHashTable:
    def __init__(self,initial_capacity=10):
        self.table = []
        for i in range(initial_capacity): #Creates 10 buckets for our packages
            self.table.append([])
        #The bucket the package goes in is calculated by bucket = hash(item)% len(self.table)
        #The indexes of the 27 buckets start at 0 and go to 26.

    def insert(self, package_ID, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight,delivery_status,special_note):
        newPackage = Package.Package(package_ID, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight,delivery_status,special_note)
        #Creates a Package to insert into our Chaining Hash Table, then decides which bucket to put it in based on the Package Address.
        #This will group packages traveling to the same address, in the same bucket.
        bucket = hash(package_ID) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(newPackage)
    def lookup(self,package_ID):
        pass
