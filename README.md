# Map_folding
地図折り問題を判定するプログラム  

!https://github.com/YutoToguchi/map_folding/blob/image/execution.gif
理論については修士論文を参照

1. 入出力用GUIの生成
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
* Java J2SE 6 or higher
* Perl version 5 or higher
* SATソルバ MiniSat 2.2.0
* Python 3
* pygame 1.9.4

# Setup
今回は Ubuntu 18.04.2 LTS (Bionic Beaver) を使用

## MiniSat インストール
まずは, [MiniSat](http://minisat.se/)のインストール
端末で以下を実行  
```
sudo apt-get update  
sudo apt-get install minisat  
```
適当なディレクトリにて ```minisat``` と入力  
以下のような出力が行われればMiniSatのインストールが完了 
```
WARNING: for repeatability, setting FPU to use double precision  
Reading from standard input... Use '--help' for help.  
============================[ Problem Statistics ]=============================  
|                                                                             |  
```
## Suar インストール
Sugar実行には以下の環境が必要であるため, インストールを行う
* Java J2SE 6 or higher
* Perl version 5 or higher
* A SAT Solver (今回はMiniSatを使用)

続いて, [Sugar](http://bach.istc.kobe-u.ac.jp/sugar/)からsugar-v2-2-3.zipをダウンロード
ダウンロードしたzipファイルを /home/ユーザ名 の場所で解凍する

環境設定する必要があるため、このbin内のsugarを以下のように自分の環境に合わせて編集
```
my $version = "v2-3-3";
my $java = "java";
my $jar = "/home/ユーザ名/sugar-$version/bin/sugar-$version.jar";
my $solver0 = "/usr/bin/minisat";
my $solver0_inc = "minisat-inc";
my $tmp = "/home/ユーザ名/sugar-$version/tmp";
```
* ```$version```: Sugarのバージョン
* ```$jar```: ```sugar-v2-3-3.jar```へのパス
* ```$solver0```: インストールしたMiniSat実行ファイルへのパス

その後 usr/local/binにsugarを移動させる


/home/ユーザ名/sugar-v2-3-3/examplesに移り, ```sugar nqueens-8.csp```でサンプルを実行  
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
map_folding_gui.ipynbとSugar_map_folding.pyを同じフォルダに置き, map_folding_gui.ipynbを実行


# Licence
戸口 雄斗

# References
Sugarのインストールについては[README.txt](http://bach.istc.kobe-u.ac.jp/sugar/current/docs/README.txt)を参照

参考にした情報源（サイト・論文）などの情報、リンク
