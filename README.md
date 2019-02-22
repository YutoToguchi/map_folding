# map_folding
地図折り問題を判定するプログラム  
理論については修士論文を参照 

1. 入出力用GUI  
map_folding_gui.ipynb

2. 理論にもとづき地図折り問題を制約充足問題に変換  
Sugar_map_folding.pyを用いてcspファイルを作成

3. SAT型ソルバSugarを用いて平坦折り判定を行う  
Sugarを用いて制約充足問題(cspファイル)の求解

4. Sugarの解をもとに平坦折り判定


このソフトはどんなもので、何ができるのかを書く
合わせて、簡単なデモ（使用例）などスクリーンショットやGIFアニメで表示

# Dependency(使用言語とバージョン、必要なライブラリ)  
* SAT型ソルバ sugar 2.3.3  
* SATソルバ MiniSat 2.2.0  
* Python 3  
* pygame 1.9.4

# Setup
1. 今回は Ubuntu 18.04.2 LTS (Bionic Beaver) を使用  

2. [MiniSat](http://minisat.se/)のインストール  
端末で以下を実行  
sudo apt-get update  
sudo apt-get install minisat  

適当なディレクトリにて minisat と入力  
以下のような出力が行われることを確認  

WARNING: for repeatability, setting FPU to use double precision  
Reading from standard input... Use '--help' for help.  
============================[ Problem Statistics ]=============================  
|                                                                             |  

3. [Sugar](http://bach.istc.kobe-u.ac.jp/sugar/)のインストール  

# Usage
使い方。なるべく具体的に書く。サンプルも書く

# Licence
戸口 雄斗

# References
参考にした情報源（サイト・論文）などの情報、リンク
