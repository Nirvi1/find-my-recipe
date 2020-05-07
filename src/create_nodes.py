import csv
class NodeCreator:

    def __init__(self, cleaned_data):
        self.recipe_data = csv.reader(open(cleaned_data, mode = 'r', encoding = 'utf8'))

    def generate_name_nodes(self):
        recipe_nodes = []
        with open('csvs/recipe_nodes.csv', 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(['recipeId:ID(Recipe)', 'recipe', ':LABEL'])
            
        for row in self.recipe_data:
            recipe_nodes.append([row[1], row[0]])
            
        with open('csvs/recipe_nodes.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.recipe_nodes)

