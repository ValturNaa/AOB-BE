init python:
    
    class PlaceTile(object):
        def __init__(self, Name, PassN=True, PassE=True, PassS=True, PassW=True, VisibleN=True, VisibleE=True, VisibleS=True, VisibleW=True, MoveRequired=1, Void=False, VoidSight=False, SightObstructionN=False, SightObstructionE=False, SightObstructionS=False, SightObstructionW=False):
            # Type of tile, string
            self.Name = Name
            # Type of tile, string
            self.Name = Name
            # can you move north from this tile (Boolean)
            self.PassN = PassN
            # can you move east from this tile (Boolean)
            self.PassE = PassE
            # can you move south from this tile (Boolean)
            self.PassS = PassS
            # can you move west from this tile (Boolean)
            self.PassW = PassW
            # can you see north from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleN = VisibleN
            # can you see east from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleE = VisibleE
            # can you see south from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleS = VisibleS
            # can you see west from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleW = VisibleW
            # how many move points moving onto this tile will take
            self.MoveRequired = MoveRequired
            # used for absolute edges
            self.Void = Void
            self.VoidSight = VoidSight
            # Used in Underlay generator
            self.SightObstructionN = SightObstructionN
            self.SightObstructionE = SightObstructionE
            self.SightObstructionS = SightObstructionS
            self.SightObstructionW = SightObstructionW
            # used with special tiles
            self.Special = False
            
    class SpecialFeature(object):
        def __init__(self, Instance, SpecificPlacing=False, SpecificX=0, SpecificY=0, MultiPart=False, MaxQuantity=100):
            # can be a PlaceTile instance or a list of PlaceTile instances. Must have multi_part set to true if a list
            self.Instance = Instance
            # does it need to be placed somewhere specific on the map
            self.SpecificPlacing = SpecificPlacing
            self.SpecificX = SpecificX
            self.SpecificY = SpecificY
            # Is this a multi par object (building etc) Instance Must be 2d array if this is the case 
            self.MultiPart = MultiPart
            # can limit number of this specific feature, even if more features can be added in excess of this another must be chosen.
            self.MaxQuantity = MaxQuantity
            self.PlacedQuantity = 0
            
            
            
            
    blank = PlaceTile("images/Tiles/blankTile.png", Void=True, VoidSight=True)
    grass = PlaceTile("images/Tiles/grassTile.png")
    grassTree = PlaceTile("images/Tiles/grassTree.png", SightObstructionN=True, SightObstructionE=True, SightObstructionS=True, SightObstructionW=True)
    grassCampfire = PlaceTile("images/Tiles/grassCampfire.png", Void=True)
    grassStone = PlaceTile("images/Tiles/grassStone.png", MoveRequired=2, SightObstructionN=True, SightObstructionE=True, SightObstructionS=True, SightObstructionW=True)
    grassHBkade = PlaceTile("images/Tiles/HorizontalBarricade.png", Void=True)
    grassVBkade = PlaceTile("images/Tiles/VerticalBarricade.png", Void=True)
    
    
    
    
    def OverlayGenerator(map):
        return list([battletile(0, UnitPresent="Null") for x in range(0, len(map[y]))] for y in range(0, len(map)))
    
    
    # (height in accessable tiles (integer), width in accessable tiles (integer), base for map (string), specail features (list of SpecailFeature instances), 
    # number of features to go on map (integer), special features (list of SpecialFeature instances, only one will be put on the map per instance.) 
    
    def UnderlayGenerator(height, width, base_ground, features, feature_density, special_features):
        
        actual_height = height+4
        actual_width = width+4
        base = []
        return_map = []
        
        # setting internal perameters here
        if (base_ground == "grass"):
            base.append(grass)
        if (base_ground == "light forest"):
            base.append(grassTree)
            base.append(grass)
            base.append(grass)
        if (base_ground == "forest"):
            base.append(grassTree)
            base.append(grass)
        if (base_ground == "heavy forest"):
            base.append(grassTree)
            base.append(grassTree)
            base.append(grass)
            
        # make basic terrein
            
        for x in range(0, actual_height):
            temp_line = []
            for y in range(0, actual_width):
                if (x == 0 or x == 1 or x == actual_height or x == actual_height-1):
                    temp_line.append(tile(blank.Name, Void=blank.Void))
                else:
                    if (y == 0 or y == 1 or y == actual_width or y == actual_width-1):
                        temp_line.append(tile(blank.Name, Void=blank.Void))
                    else:
                        random = renpy.random.randint(0, len(base)-1)
                        temp_line.append(tile(base[random].Name, PassN=base[random].PassN, PassE=base[random].PassE, PassS=base[random].PassS, PassW=base[random].PassW, VisibleN=base[random].VisibleN, VisibleE=base[random].VisibleE, VisibleS=base[random].VisibleS, VisibleW=base[random].VisibleW, MoveRequired=base[random].MoveRequired, Void=base[random].Void, SightObstructionN=base[random].SightObstructionN, SightObstructionE=base[random].SightObstructionE, SightObstructionS=base[random].SightObstructionS, SightObstructionW=base[random].SightObstructionW))
            return_map.append(temp_line)
            
        # add standard unusual features
            
        for number in range(0, feature_density):
            x = renpy.random.randint(0, len(features)-1)
            if features[x].SpecificPlacing == True:
                if (features[x].MultiPart == False):
                    return_map[features[x].SpecificX][features[x].SpecificY] =  tile(features[x].Instance.Name, PassN=features[x].Instance.PassN, PassE=features[x].Instance.PassE, PassS=features[x].Instance.PassS, PassW=features[x].Instance.PassW, VisibleN=features[x].Instance.VisibleN, VisibleE=features[x].Instance.VisibleE, VisibleS=features[x].Instance.VisibleS, VisibleW=features[x].Instance.VisibleW, MoveRequired=features[x].Instance.MoveRequired, Void=features[x].Instance.Void, SightObstructionN=features[x].Instance.SightObstructionN, SightObstructionE=features[x].Instance.SightObstructionE, SightObstructionS=features[x].Instance.SightObstructionS, SightObstructionW=features[x].Instance.SightObstructionW)
                    return_map[features[x].SpecificX][features[x].SpecificY].Special = True
                else:
                    for z in range(0, len(features[x].Instance)):
                        for y in range(0, len(features[x].Instance[0])):
                            return_map[features[x].SpecificX+z][features[x].SpecificY+y] = tile(features[x].Instance[z][y].Name, PassN=features[x].Instance[z][y].PassN, PassE=features[x].Instance[z][y].PassE, PassS=features[x].Instance[z][y].PassS, PassW=features[x].Instance[z][y].PassW, VisibleN=features[x].Instance[z][y].VisibleN, VisibleE=features[x].Instance[z][y].VisibleE, VisibleS=features[x].Instance[z][y].VisibleS, VisibleW=features[x].Instance[z][y].VisibleW, MoveRequired=features[x].Instance[z][y].MoveRequired, Void=features[x].Instance[z][y].Void, SightObstructionN=features[x].Instance[z][y].SightObstructionN, SightObstructionE=features[x].Instance[z][y].SightObstructionE, SightObstructionS=features[x].Instance[z][y].SightObstructionS, SightObstructionW=features[x].Instance[z][y].SightObstructionW)
                            return_map[features[x].SpecificX+z][features[x].SpecificY+y].Special = True
                    
            else:
                if (features[x].MultiPart == False):
                    if (features[x].MaxQuantity != features[x].PlacedQuantity):
                        RandomX = renpy.random.randint(3, actual_height-2)
                        RandomY = renpy.random.randint(3, actual_width-2)
                        while return_map[RandomX][RandomY].Special == True:
                            RandomX = renpy.random.randint(3, actual_height-2)
                            RandomY = renpy.random.randint(3, actual_width-2)
                        return_map[RandomX][RandomY] =  tile(features[x].Instance.Name, PassN=features[x].Instance.PassN, PassE=features[x].Instance.PassE, PassS=features[x].Instance.PassS, PassW=features[x].Instance.PassW, VisibleN=features[x].Instance.VisibleN, VisibleE=features[x].Instance.VisibleE, VisibleS=features[x].Instance.VisibleS, VisibleW=features[x].Instance.VisibleW, MoveRequired=features[x].Instance.MoveRequired, Void=features[x].Instance.Void, SightObstructionN=features[x].Instance.SightObstructionN, SightObstructionE=features[x].Instance.SightObstructionE, SightObstructionS=features[x].Instance.SightObstructionS, SightObstructionW=features[x].Instance.SightObstructionW)
                        return_map[RandomX][RandomY].Special = True
                else:
                    if (features[x].MaxQuantity != features[x].PlacedQuantity):
                        RandomX = renpy.random.randint(3, actual_height-2)
                        RandomY = renpy.random.randint(3, actual_width-2)
                        PlaceCheck = PlaceCheck(RandomX, RandomY, return_map)
                        while PlaceCheck == False:
                            RandomX = renpy.random.randint(3, actual_height-2)
                            RandomY = renpy.random.randint(3, actual_width-2)
                            PlaceCheck = PlaceCheck(RandomX, RandomY, len(features[x].Instance), len(features[x].Instance[0]), return_map)
                        for z in range(0, len(features[x].Instance)):
                            for y in range(0, len(features[x].Instance[0])):
                                return_map[RandomX+z][RandomY+y] = tile(features[x].Instance[z][y].Name, PassN=features[x].Instance[z][y].PassN, PassE=features[x].Instance[z][y].PassE, PassS=features[x].Instance[z][y].PassS, PassW=features[x].Instance[z][y].PassW, VisibleN=features[x].Instance[z][y].VisibleN, VisibleE=features[x].Instance[z][y].VisibleE, VisibleS=features[x].Instance[z][y].VisibleS, VisibleW=features[x].Instance[z][y].VisibleW, MoveRequired=features[x].Instance[z][y].MoveRequired, Void=features[x].Instance[z][y].Void, SightObstructionN=features[x].Instance[z][y].SightObstructionN, SightObstructionE=features[x].Instance[z][y].SightObstructionE, SightObstructionS=features[x].Instance[z][y].SightObstructionS, SightObstructionW=features[x].Instance[z][y].SightObstructionW)
                                return_map[RandomX+z][RandomY+y].Special = True
        
        # Add special one off features that take priority
            
        for x in special_features:
            if (x.SpecificPlacing == True):
                if (x.MultiPart == False):
                    return_map[x.SpecificX][x.SpecificY] =  tile(x.Instance.Name, PassN=x.Instance.PassN, PassE=x.Instance.PassE, PassS=x.Instance.PassS, PassW=x.Instance.PassW, VisibleN=x.Instance.VisibleN, VisibleE=x.Instance.VisibleE, VisibleS=x.Instance.VisibleS, VisibleW=x.Instance.VisibleW, MoveRequired=x.Instance.MoveRequired, Void=x.Instance.Void, SightObstructionN=x.Instance.SightObstructionN, SightObstructionE=x.Instance.SightObstructionE, SightObstructionS=x.Instance.SightObstructionS, SightObstructionW=x.Instance.SightObstructionW)
                    return_map[x.SpecificX][x.SpecificY].Special = True
                else:
                    for z in range(0, len(x.Instance)):
                        for y in range(0, len(x.Instance[0])):
                            return_map[x.SpecificX+z][x.SpecificY+y] = tile(x.Instance[z][y].Name, PassN=x.Instance[z][y].PassN, PassE=x.Instance[z][y].PassE, PassS=x.Instance[z][y].PassS, PassW=x.Instance[z][y].PassW, VisibleN=x.Instance[z][y].VisibleN, VisibleE=x.Instance[z][y].VisibleE, VisibleS=x.Instance[z][y].VisibleS, VisibleW=x.Instance[z][y].VisibleW, MoveRequired=x.Instance[z][y].MoveRequired, Void=x.Instance[z][y].Void, SightObstructionN=x.Instance[z][y].SightObstructionN, SightObstructionE=x.Instance[z][y].SightObstructionE, SightObstructionS=x.Instance[z][y].SightObstructionS, SightObstructionW=x.Instance[z][y].SightObstructionW)
                            return_map[x.SpecificX+z][x.SpecificY+y].Special = True
            else:
                if (x.MultiPart == False):
                    RandomX = renpy.random.randint(3, actual_height-2)
                    RandomY = renpy.random.randint(3, actual_width-2)
                    while return_map[RandomX][RandomY].Special == True:
                        RandomX = renpy.random.randint(3, actual_height-2)
                        RandomY = renpy.random.randint(3, actual_width-2)
                    return_map[RandomX][RandomY] =  tile(x.Instance.Name, PassN=x.Instance.PassN, PassE=x.Instance.PassE, PassS=x.Instance.PassS, PassW=x.Instance.PassW, VisibleN=x.Instance.VisibleN, VisibleE=x.Instance.VisibleE, VisibleS=x.Instance.VisibleS, VisibleW=x.Instance.VisibleW, MoveRequired=x.Instance.MoveRequired, Void=x.Instance.Void, SightObstructionN=x.Instance.SightObstructionN, SightObstructionE=x.Instance.SightObstructionE, SightObstructionS=x.Instance.SightObstructionS, SightObstructionW=x.Instance.SightObstructionW)
                    return_map[RandomX][RandomY].Special = True
                else:
                    RandomX = renpy.random.randint(3, actual_height-2)
                    RandomY = renpy.random.randint(3, actual_width-2)
                    PlaceCheck = PlaceCheck(RandomX, RandomY, return_map)
                    while PlaceCheck == False:
                        RandomX = renpy.random.randint(3, actual_height-2)
                        RandomY = renpy.random.randint(3, actual_width-2)
                        PlaceCheck = PlaceCheck(RandomX, RandomY, len(features[x].Instance), len(features[x].Instance[0]), return_map)
                    for z in range(0, len(x.Instance)):
                        for y in range(0, len(x.Instance[0])):
                            return_map[RandomX+z][RandomY+y] = tile(x.Instance[z][y].Name, PassN=x.Instance[z][y].PassN, PassE=x.Instance[z][y].PassE, PassS=x.Instance[z][y].PassS, PassW=x.Instance[z][y].PassW, VisibleN=x.Instance[z][y].VisibleN, VisibleE=x.Instance[z][y].VisibleE, VisibleS=x.Instance[z][y].VisibleS, VisibleW=x.Instance[z][y].VisibleW, MoveRequired=x.Instance[z][y].MoveRequired, Void=x.Instance[z][y].Void, SightObstructionN=x.Instance[z][y].SightObstructionN, SightObstructionE=x.Instance[z][y].SightObstructionE, SightObstructionS=x.Instance[z][y].SightObstructionS, SightObstructionW=x.Instance[z][y].SightObstructionW)
                            return_map[RandomX+z][RandomY+y].Special = True
            
        # set line of sight and walk restrictions    
            
        for x in range(3, len(return_map)-2):
            for y in range(3, len(return_map[x])-2):
                if (return_map[x-1][y].Void == True):
                    return_map[x][y].PassN = False
                if (return_map[x+1][y].Void == True):
                    return_map[x][y].PassS = False 
                if (return_map[x][y-1].Void == True):
                    return_map[x][y].PassW = False
                if (return_map[x][y+1].Void == True):
                    return_map[x][y].PassE = False
                if (return_map[x-1][y].VoidSight == True):
                    return_map[x][y].VisibleN = False
                if (return_map[x+1][y].VoidSight == True):
                    return_map[x][y].VisibleS = False 
                if (return_map[x][y-1].VoidSight == True):
                    return_map[x][y].VisibleW = False
                if (return_map[x][y+1].VoidSight == True):
                    return_map[x][y].VisibleE = False
                

                if (return_map[x][y].SightObstructionN == True):
                    return_map[x-1][y].VisibleS = False
                if (return_map[x][y].SightObstructionS == True):
                    return_map[x+1][y].VisibleN = False 
                if (return_map[x][y].SightObstructionW == True):
                    return_map[x][y+1].VisibleW = False
                if (return_map[x][y].SightObstructionE == True):
                    return_map[x][y-1].VisibleE = False
        
        return return_map
                
        
                    
                

        

    def PlaceCheck(x, y, up, across, map):
        answer = True
        for updown in range(x, x+up):
            for sideside in range(y, y+across):
                if (map[updown][sideside].Special == True):
                    answer = False
                if (map[updown][sideside].Void == True):
                    answer = False
        return answer
        
        