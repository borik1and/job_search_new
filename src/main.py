from src.class_save import JsonSave
from src.user_interaction import user_interaction

# стираем фаил json из пребедущего цикла если есть
JsonSave.delete_file()
user_interaction()
