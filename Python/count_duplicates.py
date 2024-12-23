class Duplicate:
    def count(self,input_string):
        number_counts={}
        character_counts={}
        for char in input_string:
            if char.isdigit():
                if char in number_counts:
                    number_counts[char]+=1
                else:
                    number_counts[char]=1
            elif char.isalpha():
                if char in character_counts:
                    character_counts[char]+=1
                else:
                    character_counts[char]=1

        print(f'''Number_counts:{number_counts}
              Charcter_counts:{character_counts}''')
        
count_duplicate=Duplicate()
input_string="abcdefacsfdjshjaacae121313"
count_duplicate.count(input_string)