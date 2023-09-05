import pickle

vaccine_details = {"Karnataka": {"Covisheild" : 5,
                                 "Covaxine" : 3,
                                 "Sputnik" : 4},
                   "Maharashtra": {"Covisheild" : 3,
                                 "Covaxine" : 1,
                                 "Sputnik" : 8},   
                    "Kashmir": {"Covisheild" : 4,
                                 "Covaxine" : 1,
                                 "Sputnik" : 4}
                  }

fh = open("vdstates", "wb")
pickle.dump(vaccine_details, fh)
fh.close()