# Map_folding
地図折り問題を判定するプログラム  

![result](https://github.com/YutoToguchi/map_folding/blob/image/execution.gif)

このプログラムは以下の動作を行う

1. 入出力用GUIの生成
map_folding_gui.ipynb

2. 理論にもとづき地図折り問題を制約充足問題に変換  
Sugar_map_folding.pyを用いてcspファイルを作成

3. SAT型ソルバSugarの実行  
Sugarを用いて制約充足問題(cspファイル)の求解

4. Sugarの解をもとに平坦折り判定

(理論については修士論文を参照)

# Dependency
使用言語とバージョン, 必要なライブラリは以下の通りである
* SAT型ソルバ sugar 2.3.3
* Java J2SE 6 or higher
* Perl version 5 or higher
* SATソルバ MiniSat 2.2.0
* Python 3
* pygame 1.9.4

# Setup
今回は Ubuntu 18.04.2 LTS (Bionic Beaver) を使用

### MiniSat インストール
まずは, [MiniSat](http://minisat.se/)のインストール
端末で以下を実行  
```
sudo apt-get update  
sudo apt-get install minisat  
```
適当なディレクトリにて ```minisat``` とコマンド入力  
以下のような出力が行われればMiniSatのインストールが完了 
```
WARNING: for repeatability, setting FPU to use double precision  
Reading from standard input... Use '--help' for help.  
============================[ Problem Statistics ]=============================  
|                                                                             |  
```
### Sugar インストール
Sugar実行には以下の環境が必要であるため, インストールを行う
* Java J2SE 6 or higher
* Perl version 5 or higher
* A SAT Solver (今回はMiniSatを使用)

続いて, [Sugar](http://bach.istc.kobe-u.ac.jp/sugar/)からsugar-v2-2-3.zipをダウンロード  
ダウンロードしたzipファイルを /home/ユーザ名 の場所で解凍する

環境設定する必要があるため, このbin内のsugarを以下のように環境に合わせて編集
```
my $version = "v2-3-3";
my $java = "java";
my $jar = "/home/ユーザ名/sugar-$version/bin/sugar-$version.jar";
my $solver0 = "/usr/bin/minisat";
my $solver0_inc = "minisat-inc";
my $tmp = "/home/ユーザ名/sugar-$version/tmp";
```
* ```$version```: Sugarのバージョン
* ```$jar```: sugar-v2-3-3.jarへのパス
* ```$solver0```: インストールしたMiniSat実行ファイルへのパス

その後 usr/local/binにsugar-v2-3-3を移動させる


/home/ユーザ名/sugar-v2-3-3/examplesに移り, ```sugar nqueens-8.csp```とコマンド入力  
以下のように正しい実行結果が得られれば, Sugar, MiniSatのインストール完了
```
s SATISFIABLE
a q_1   7
a q_2   2
a q_3   4
a q_4   1
a q_5   8
a q_6   5
a q_7   3
a q_8   6
a
```


# Usage
以下の2つのプログラムを同じフォルダに置き, map_folding_gui.ipynbを実行
* map_folding_gui.ipynb : 入出力用GUI  
* Sugar_map_folding.py : 平坦折り判定プログラム  


# Licence
Copyright (c) 2019 Yuto Toguchi  
Released under [The MIT License](https://opensource.org/licenses/mit-license.php)

# References
Sugarのインストールについては[公式サイトREADME.txt](http://bach.istc.kobe-u.ac.jp/sugar/current/docs/README.txt)を参照

