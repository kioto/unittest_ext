# unittest_ext
unittest package extension for python3

Python3のunittestを拡張し、teaDown()でテスト結果をCSVファイルに出力することができる。

## CSVログファイル
CSVのログファイルのオープンとクローズの例。

クラス名.csvでログファイルをオープンする。

```python:sample_test.py
    @classmethod
    def setUpClass(cls):
        cls.open_csv_log(cls.__name__+'.csv')

    @classmethod
    def tearDownClass(cls):
        cls.close_csv_log()
```

tearDown()から結果を出力するコード。

```python:sample_test.py
    def tearDown(self):
        self.write_csv_log((self.get_test_method_name(),
                            self.get_test_result(),
                            self.get_test_message(),))
```

CSVファイルは以下のようになる。

```csv:Sample_1.csv
test_001_OK,OK,
test_002_OK,OK,
test_003_FALSE,FAIL,False is not true
test_004_ERROR,ERROR,name 'aaa' is not defined
test_005_OK,OK,
test_006_FAIL,FAIL,False is not true
test_007_OK,OK,
```
## Python2対応について

検討中
