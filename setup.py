from  setuptools import find_packages, setup
#from  typing import List 


#def get_requirements() ->List[str]:
 #     reuirements_list : List[str] = []

   #   return reuirements_list 

setup (
 name = 'sensor',
 version = "0.0.1",
 author = "prince",
 author_email = "kumarbikky8340@gmail.com",
 packages = find_packages(),
 install_requires =  get_requirements(), #["pymongo"]

)

