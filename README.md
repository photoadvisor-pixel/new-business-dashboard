# SDC New Business Dashboard

## 概要
新規事業プランのMarkdownファイルを管理し、見やすいダッシュボード（HTML）を自動生成するツールです。

## セットアップ
必要なライブラリをインストールします。

```bash
pip install markdown python-frontmatter jinja2
```

## 使い方
1. `projects/` フォルダに事業プランのMarkdownファイルを作成します（テンプレート: `00_template.md`）。
2. 以下のコマンドを実行してダッシュボードを生成します。

```bash
python generate.py
```

3. 生成された `index.html` をブラウザで開いて確認します。
4. GitHubへPushすると、GitHub Pagesで公開されます（設定が必要）。

## 公開手順
1. GitHubリポジトリを作成。
2. Settings > Pages で `main` ブランチ（または `docs` フォルダ等）を公開元に設定。
