import glob

class Images:
    def __init__(self):
        self.Assets_dir = "All_Assets/"

        self.base_list = glob.glob(Assets_dir+'*base*')
        self.access_list = glob.glob(Assets_dir+'*access*')
        self.background_list = glob.glob(Assets_dir+'*bg*')
        self.eyes_list = glob.glob(Assets_dir+'*eyes*')
        self.eyebrows_list = glob.glob(Assets_dir+'*brows*')
        self.facialhair_list = glob.glob(Assets_dir+'*facial_hair*')
        self.hair_list = glob.glob(Assets_dir+'*app_hair*')
        self.mouth_list = glob.glob(Assets_dir+'*mouth*')
        self.outfit_list = glob.glob(Assets_dir+'*outfit*')


