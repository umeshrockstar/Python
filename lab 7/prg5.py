def twdicm():
                d1={'soapbar':30,'rice':2500,'potato':20}
                d2={'soapbar':2,'rice':1,'potato':4}
                s=0
                for k in d1:
                                if k in d2:
                                                mlt = d1[k]*d2[k]
                                                s = s+mlt
                print("Total Bill =",s)
                                

twdicm()
