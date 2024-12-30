from setuptools import find_packages,setup
from typing import List


def get_requirements()-> List[str]:
    requirements:List[str]=[]
    
    try:
        with open("requirements.txt","r") as f:
            lines=f.readlines()

            for line in lines:
                require=line.strip()
                # print(require)
                if require!='' and require !="-e .":
                    requirements.append(require)
                   
    except Exception as e:
        raise e
    
    return requirements



setup(
    name="Network_Security_Project",
    version="0.0.1",
    author="Gajender",
    author_email="Iamsanju0707@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

# if __name__=="__main__":
#     print(get_requirements())