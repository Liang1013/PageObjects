import yaml,os

class Route():

    def route_yaml(self,file,url_name):
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "Data",file)
        with open(filepath) as f:
            yml = yaml.load(f,Loader=yaml.FullLoader)
        return yml[url_name]

    def route_report(self,file):
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, file)
        return filepath

if __name__ == "__main__":
    rou = Route()
    t = rou.route_yaml("login.yaml","test")
    print(t["url"])