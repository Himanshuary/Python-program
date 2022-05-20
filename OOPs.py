# Create a movie class and fill out movie info

class Movie:
    def __init__(self,tital,releasedate,imbdrating):
        self.tital = tital
        self.releasedate = releasedate
        self.imbdrating = imbdrating 
        
        
    def info(self):
        print("Movie Name:        ", self.tital)
        print("Movie releasedate: ", self.releasedate)
        print("Movie imbdrating:  ", self.imbdrating)

list_of_movie = []
while True:
    tital = input("Enter Movie name: ")
    releasedate = int(input("Enter movie releasedate: "))
    imbdrating = float(input("Enter movie imbdrating: "))
    m = Movie(tital,releasedate,imbdrating)
    list_of_movie.append(m)
    print("Movie added to the list successfully")
    option = input("Do you want to add one more movie[Yes|no]")
    if option.lower() == 'no':
        break
    
print("All movie info...")
for Movie in list_of_movie:
    Movie.info()