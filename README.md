# VoTT2COCO
Convert VoTT annotations to COCO annotations

## 🔨 Usage
```bash
python main.py --train-ann example/train_folder/annotation/ --test-ann example/test_folder/annotation/ --output-dir output
```

`--train-ann`: Path to train annotations

`--test-ann`: Path to test annotations

`--output-dir`: Path to output directory

## 📚 Notes
- This tool does not translate segmentation annotations
- You must move your images and the output annotations (produced by this tool) to the train and test folders in the output directory after the tool has completed its task

![Output Folder Structure](folder-structure.png)

## 🎉 Contributing
If you find any bugs or potential features, feel free to write an issue or make a pull request!
