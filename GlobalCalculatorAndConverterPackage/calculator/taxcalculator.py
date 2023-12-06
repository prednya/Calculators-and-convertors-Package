def calc_tax_old_regime(deduc_80c,deduc_80D,deduc_80tta,salary,other):
    total_taxable_income=salary+other,(deduc_80c+deduc_80D+deduc_80tta)
    class Switch(dict):
        def __getitem__(self, item):
            for key in self.keys():                
                if item in key:                    
                    return super().__getitem__(key) 
            raise KeyError(item)                    
    switch = Switch({
    range(0,250000) :0,
         range(250000,500000) :0.05,
          range(500001,750000) :0.10,
           range(750001,1000000) :0.15,
            range(1000001,1500000) :0.20,
             range(1500000,1000000000000) :0.30,
    })
    total_taxable_income=switch[salary]*salary+other-(deduc_80c+deduc_80D+deduc_80tta)
    return total_taxable_income