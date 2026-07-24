# 参与贡献

[English](CONTRIBUTING.md)

贡献内容应提升公开来源逐字稿的准确性、可追溯性或覆盖范围。

## 新增或更新逐字稿

1. 仅使用公开来源，并提供原始视频链接。
2. 使用 Markdown 保存逐字稿，保留原始措辞。
3. 来源提供时间信息时必须保留时间戳。
4. 未完成说话人分离时，不要把推测写成确定归因。
5. 只有人物明确出现在来源中时，才更新 `data/featured-people.yml`。
6. 运行 `python3 -m pip install -r requirements.txt` 安装维护依赖。
7. 从本地目录导入：

```bash
python3 scripts/import_transcripts.py /path/to/transcript-directory --refresh-youtube
```

8. 提交前执行：

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## 内容修正与权利请求

修正错字时请提供文件路径、时间戳、来源链接和正确原文。权利人可以通过 Issue 提供受影响的来源链接及处理请求。请勿提交私密、付费墙、泄露或个人隐私材料。
