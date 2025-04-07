import os
import json
import shutil

results_dir = 'results'
best_score = -1
best_experiment = None

# 1. 모든 실험 폴더 순회
for folder in os.listdir(results_dir):
    folder_path = os.path.join(results_dir, folder)
    history_path = os.path.join(folder_path, 'history.json')

    if not os.path.isfile(history_path):
        continue

    with open(history_path, 'r') as f:
        history = json.load(f)

    val_acc = history.get('val_accuracy', [])
    if val_acc:
        max_val_acc = max(val_acc)
        if max_val_acc > best_score:
            best_score = max_val_acc
            best_experiment = folder_path

# 2. best 모델 복사
if best_experiment:
    best_model_dir = 'best_model'
    os.makedirs(best_model_dir, exist_ok=True)

    for fname in ['model_structure.json', 'model_weights.h5', 'config.json', 'class_names.json']:
        src = os.path.join(best_experiment, fname)
        dst = os.path.join(best_model_dir, fname)
        if os.path.exists(src):
            shutil.copyfile(src, dst)

    print(f'✅ Best model (val_acc={best_score:.4f}) copied from "{best_experiment}" to "{best_model_dir}"')
else:
    print('❌ No valid experiment with val_accuracy found.')
