from  setuptools import find_packages, setup
#from  typing import List 


#def get_requirements() ->List[str]:
 #     reuirements_list : List[str] = []

   #   return reuirements_list 

def get_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]




setup (
 name = 'sensor',
 version = "0.0.1",
 author = "prince",
 author_email = "kumarbikky8340@gmail.com",
 packages = find_packages(),
 install_requires =  get_requirements(), #["pymongo"]

)

