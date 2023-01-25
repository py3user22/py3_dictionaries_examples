#!/usr/bin/python3


cySec_notes = {
    "CIS": 'Center for Internet Security',
    "NIST": 'National Institute Security Technology',
    "AICPA": 'American Institute of CPA',
    "GDPR": 'General data protection regulations',
    "HIPAA": 'Health Insurance portability & accountability act',
    "PCI-DSS": 'Payment card industry - Data standard security',
    "ISO": 'International org for standardization'
}

for kee, valu in cySec_notes.items():
    print("{} > {}".format(kee, valu))
