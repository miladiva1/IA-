import os

# ----------------- CONFIGURAÇÕES -----------------
ROOT_PATH = r"C:\Users\camila\Downloads\archive\css-data"
FOLDERS = ['train', 'valid', 'test']
OLD_CLASS = '0' # Classe de oculos no dataset novo
NEW_CLASS = '10' # Nova classe de oculos no dataset combinado
# -------------------------------------------------

print("Iniciando re-mapeamento...")

for folder in FOLDERS:
    labels_dir = os.path.join(ROOT_PATH, folder, 'labels')
    if not os.path.isdir(labels_dir):
        print(f"Aviso: Pasta de labels nao encontrada: {labels_dir}")
        continue

    print(f"Processando labels em: {labels_dir}")

    for filename in os.listdir(labels_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(labels_dir, filename)

            with open(filepath, 'r') as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.split()
                if not parts:
                    continue

                class_index = parts[0]

                if class_index == OLD_CLASS:
                    new_line = NEW_CLASS + line[len(class_index):]
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)

            with open(filepath, 'w') as f:
                f.writelines(new_lines)

print("Re-mapeamento concluido.")