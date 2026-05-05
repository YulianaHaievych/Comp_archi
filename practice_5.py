import os
import shutil
import time
import pandas as pd 

def run_comparison():
   
    source = "working_data"
    backup_dest = "external_backup_folder"
    snapshot_dest = "local_snapshot_folder"
    
    if not os.path.exists(source):
        os.makedirs(source)
        for i in range(10):
            with open(f"{source}/file_{i}.txt", "w") as f:
                f.write(f"This is some important data for AI-11 student project {i}")

    results = []

    start_b = time.perf_counter()
    if os.path.exists(backup_dest): shutil.rmtree(backup_dest)
    shutil.copytree(source, backup_dest)
    end_b = time.perf_counter()
    
    results.append({
        "Параметр": "Швидкість виконання",
        "Backup (Копія)": f"{end_b - start_b:.6f} сек",
        "Snapshot (Знімок)": "---" 
    })

    start_s = time.perf_counter()
    if os.path.exists(snapshot_dest): shutil.rmtree(snapshot_dest)
    os.system(f"cp -al {source} {snapshot_dest}")
    end_s = time.perf_counter()
    
    results[0]["Snapshot (Знімок)"] = f"{end_s - start_s:.6f} сек"
    results.append({
        "Параметр": "Локація даних",
        "Backup (Копія)": "Інший диск / Хмара",
        "Snapshot (Знімок)": "Той самий диск"
    })
    results.append({
        "Параметр": "Захист від збою диска",
        "Backup (Копія)": "ТАК (Високий)",
        "Snapshot (Знімок)": "НІ (Низький)"
    })
    results.append({
        "Параметр": "Призначення",
        "Backup (Копія)": "Катастрофостійкість",
        "Snapshot (Знімок)": "Миттєвий відкат змін"
    })

    df = pd.DataFrame(results)
    print("\nРезультат аналізу за варіантом №9 (Snapshot vs Backup):")
    print("="*70)
    print(df.to_string(index=False))
    print("="*70)

if __name__ == "__main__":
    run_comparison()