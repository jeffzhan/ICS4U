
import recipe_class_starter_code as r
import csv

def read_file(filename):
    recipeDict = {}
    
    with open(filename, encoding='utf8', errors='ignore') as fileIn:
        fileIn.readline()
        
        reader = csv.reader(fileIn)

        
        for line in reader:
            ingList = []
            tempIng = line[4].split(',')
            for ing in tempIng: 
                ingList.append(str(ing).strip())
            
            # SRNO, translatedRecipeName, translatedIngredients, prepTimeMin, cookTimeMin, totalTimeMin, servings, cuisine, course, diet, translatedInstructions, URL
            recipeObj = r.Recipe(int(line[0]), line[2].strip(), ingList, int(line[5]), int(line[6]), int(line[7]), int(line[8]), line[9].strip(), line[10].strip(), line[11].strip(), line[13].strip(), line[14].strip())
            
            if line[9] not in recipeDict:
                recipeDict[line[9]] = {}
            
            if line[10] not in recipeDict[line[9]]:
                recipeDict[line[9]][line[10]] = []
            
            recipeDict[line[9]][line[10]].append(recipeObj)
                
    return recipeDict


def generate_index_file(dataset, filename):
    
    with open(filename, "w", encoding='utf-8', newline='') as indexOut:

        writer = csv.writer(indexOut)
        
        writer.writerow(['ID','Cuisine','Course','Diet','Name','Total Time (prep & cook)','Servings'])
        
        for cuisine in dataset:
            for course in dataset[cuisine]:
                for recipe in dataset[cuisine][course]:
                    s = [recipe.ID(),recipe.cuisine(),recipe.course(),recipe.diet(),recipe.name(),recipe.totaltime(),recipe.servings()]
                    writer.writerow(s)


def generate_recipe_detail_file(dataset, filename):
    
    with open(filename, "w", encoding='utf8') as recipeOut:
        for cuisine in dataset:
            for course in dataset[cuisine]:
                for recipe in dataset[cuisine][course]:
                    s = f'{recipe.ID()}\n'
                    s += f'{recipe.name()}\n'
                    s += f'prep time: {recipe.preptime()} min | cook_time: {recipe.cooktime()} min | total_time:  {recipe.totaltime()} min\n'
                    s += f'{recipe.cuisine()} | {recipe.course()} | {recipe.diet()}\n'
                    s += f'Makes {recipe.servings()} servings\n'
                    s += f'{recipe.URL()}\n\n'
                    
                    s += 'Ingredients\n'
                    for ing in recipe.ingredients():
                        s += f'{ing}\n'
                    
                    s += '\nInstructions\n'
                    s += f'{recipe.instructions()}\n\n'
                    
                    recipeOut.write(s)
                
                       

#MAIN
dataset = read_file("IndianFood.csv")

generate_index_file(dataset, "Indian_Food_Recipe_Index.csv")

generate_recipe_detail_file(dataset, "Indian_Food_Recipe_Cards.txt")
