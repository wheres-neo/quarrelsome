# Quarrelsome: A Python Tool for Semantic Versioning

Quarrelsome is a robust Python-based tool specifically designed to facilitate the management of semantic versioning. It provides a streamlined approach to version control by automatically handling version increments, ensuring your project follows the Semantic Versioning (SemVer) principles with ease and precision. 

## What Does This Entail?

- **Automated Version Management:** Quarrelsome handles the process of incrementing version numbers, ensuring consistency and adherence to SemVer.
- **Seamless Integration:** Easily integrate Quarrelsome into your existing workflows to manage versioning without hassle.

## Why Open Source?

Best of all, Quarrelsome is **100% open source**, allowing anyone to contribute, modify, and utilize it freely. This ensures a collaborative environment for development and improvement.

## "Fucking the System" - What's It About?

"Fucking the system" isn't just a tagline — it's a mindset. It's about challenging outdated systems and giving developers something clean, simple, and powerful. Quarrelsome throws out bloated pipelines and gives you a versioning tool that just works, without the BS.

## 🚀 How to Use

### Step-by-step:

```bash
# Step 1 - Make or enter your project directory
mkdir my-project && cd my-project

# Step 2 - Clone the Quarrelsome repo
git clone https://github.com/wheres-neo/quarrelsome.git

# Step 3 - Enter the Quarrelsome directory
cd quarrelsome

# Step 4 - Install required dependencies
pip install -r requirements.txt

# Step 5 - Run the tool
python quarrelsome.py
```
# A little Easter Egg : 

 ⣄⣤⣀⣀⡀⣤⡴⠶⠛⠛⠉⠉⠉⠉⠙⠓⢷⣄⢀⣀⡀
          ⠘⢯⣍⣉⣉⠁           ⠉⠉⠉⠛⠳⢦⣄⡀
          ⣠⡾⠚⠉    ⡀            ⠈⠰⡈⢿⡂
        ⣠⠞⠃     ⢀⡜      ⣠⡀       ⡱⢈⢿⣆
      ⢀⡴⠋ ⣠⠂  ⡀⣠⣾⡁   ⡀⠠⣰⠟⣷⡀  ⢣   ⠘⡦⢈⢿⣂
   ⠢⣴⠴⠋  ⣰⠃  ⣠⣾⣋⢸⡅  ⡸ ⣼⠃ ⣈⣻⣦⣄⡀⣣  ⠡⢱⡈⠤⢳⣦⡀
    ⠈⠛⠳⣶⡾⡇  ⣴⠟⠉⠉⠛⠿⡀ ⣧⢸⡏ ⠊⠉⠁⠉⠛⢿⣵⡆ ⢀⢻⢈⠆⡡⠌⠻⣶⣤
      ⢨⣟ ⣧ ⣸⠏ ⣀⣄⣀ ⠙⢦⣹⢿⡁       ⠙⢻⡀⠄⢺⠤⡙⢳⣞⠿⠃⠁
      ⠈⣿⢠⣾⣧⣿ ⣾⠋⠉⠹⣧  ⠈  ⢠⡾⠛⠛⢿⣆  ⢺⡇⢌⡏⢢⠡⡉⢿⡀
       ⠘⠻⠋⢩⡷⠈⠇   ⠻     ⢻⠁   ⣿  ⣿⢂⡾⢑⣆⣑⣌⣌⣻⣆
         ⢀⣾⠃     ⢴             ⠿⢋⢴⡟⡈⢿⣏⠉
         ⠸⣿    ⢀        ⣀⣤⣄    ⡘⢤⡾⡑⢌⢂⢻⡧
          ⠻⣦   ⠘⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⠃  ⡌⣴⡿⣑⣌⣦⣌⣦⣿⡇
     ⢀⣀    ⠙⠷⢦⡀ ⠘⢿⣿⠻⡙⢌⠓⠌⣒⡽⠋ ⢀⣲⣾⠟⠿⣯⣋    ⠁
   ⢠⣵⠋⠉⣷⡆   ⢀⣺⠟⢳⣤⣀⠈⠓⠺⠤⠼⠒⠋⣀⣤⣶⣿⡯⠟⠫⡑⠤⢛⣧⣤⠞⠺⡔
   ⠸⣷  ⢸⢇   ⠸⣯ ⡀⠺⢯⡛⣷⠶⣶⠶⣞⢻⣯⠿⠋⢉ ⡄⢣⡘⣤⣉⣿⡏  ⣿⠁   Neo ASCII Art ;3
  ⢠⣄⣿⣤⣀⠸⣞⡀ ⣠⡴⠿⣆⡁⠄⡘⠷⣿⢢⠝⣢⡽⠞⠋ ⢄⡈⣔⣥⠾⠷⠻⡟⣿⠁ ⢰⡿
⢠⡾⠋⠁  ⠙⣷⡘⣏⣮⠏ ⢀⠈⠙⢷⡶⣦⡘⢳⣾⢋⣴⢮⣤⣷⠾⠚⠍⠂⣡⠎⣧⠷⠛⠛⠛⠻⢥⡀
⢸⡇ ⠐⠛⠚⠳⣿⠠⣹⡇ ⣖⡇⠠⠁⣞⢠⠇⠛ ⠐⠋⡟⢸⡁⠂⠄⡁⢂⢡⡇ ⣿⢤⠤⠄   ⣿⠄
⢸⡇ ⠠⠄⠐⠒⣿⡄⣿  ⣿⡀⠂⠄⡿⣼⠃⡐⢈⠐⡀⡧⡽⢀⢁⠂⡐⡀⢶⡰ ⣯⣀⣀⣀⡀ ⡀⣿⠂
⠈⣿  ⢀⣀⣾⣟⣼⣿⣦⡆⡿ ⠡⠸⡧⢾⠁⡐⢀⠂⢸⣅⡗⢀⠂⡐⠠⠘⣯⡽⢸⣏⡀    ⣘⣿⠁
 ⢸⡷⣄⣈⣉⣴⢟⡼⣰⢻⣥⡗⡈⠄⡁⠛⠏⡀⠐⡀⢂⠸⣦⠏⢀⠂⠄⡁⠂⡽⣷⣿⡍⠉⠛⢁⠠⡐⢼⣻⣇
 ⠸⣥⡯⣝⣯⣖⣫⣵⠏⠄⢽⡇⠐⠠⢀⠡⠐⡀⠡⠐⠠ ⠄⡐⠠⢈⠐⠠⠑⡤⢹⡿⢿⢶⡤⠾⣃⣴⢏⡟⣯⡄
  ⢙⣆⠉⠉⠩⣅⠢⡘⠌⣸⠆⡈⠐⡀⢂⠁⡐⠠⢁⠂⡁⠂⠄⠡ ⠌⡐⠠⡑⢊⣷⠈⢷⣍⣑⣭⡶⠟⢠⣿⠇
   ⠺⢧⣈⠒⠤⠑⣈⣶⣿⡃⢀⠡⢀⠂⡐⠠⠁⠄⠂⠄⠡⠈⠄⠡⠐⢀⠡⠌⡅⠻⣦⡀⢈⠍⡰⠠⣉⣼⠏ ⢠⣰⠴⠗⣒⡶
    ⠈⠋⠛⠿⠳⠟⢓⣿ ⡲⠉⡉⠁⠒⡑⢊⠐⡈⠠⠑⠘⠚⢳⡓⠈⣇⢊⠌⡅⢻⣿⠳⠶⠶⠟⠏⢋⣠⠟⠋⡄⢊⣴⡏
          ⣾⠃⢰⠃⠄⡠⠁⢂⠐⡀⠂⠄⠡⠈⠄⠡ ⣦⠁⢹⡎⡰⢈⠍⣿⡄   ⣠⠏⡁⢆⠱⣈⣟⠁
         ⢸⣟ ⡗⠈⠐⡀⢁⠂⡐⠠⠁⠌⡀⠡⢈⠠⠁⢸⡄⢂⢿⡔⡩⢘⣸⡄⢀⣴⠟⡁⢆⠱⣈⣲⠯
          ⢿⣆⣏⠤⣁⠐⣀⠂⢄⡁⠌⡐⣀⢁⠂⡄⡡⢂⠳⣌⢂⣿⢀⣳⣏⠛⠿⢧⢂⠱⣈⠒⢰⡯⠁
          ⢸⣏⠘⡙⠒⠳⢬⡼⠤⣜⣰⣁⣆⣌⣱⣠⣑⠮⡴⡭⣒⠛⡭⢸⣇⡉⠒⡄⢊⠔⡠⢉⣿⡇
          ⠈⢻⣶⣥⣌⣀⣧ ⠂⢸ ⠄⡈⡆⡐⠠⢌⠒⣐⣣⣴⣭⣶⣿⡇⢌⣑⣬⣦⡃⠴⡁⠼⣷
           ⢸⡿⣹⠻⣟⡿⣿⢿⣿⣿⣿⢿⣿⣿⣿⢿⡿⣿⣟⣯⣟⣿⢿⢻⠯⠛⠁ ⠛⠷⣮⣤⣽⣧
