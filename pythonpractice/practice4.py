#関数
#長方形の面積の求め方
def rectangle(width,len):
    return width*len

result1 = rectangle(10,20)
print(result1)
result2 = rectangle(20,40)
print(result2)

#クラス
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l
#縦と横のデータを、インスタンス変数に相当する３つの関数（メソッド）に代入し、1つのカプセル化したインスタンス（オブジェクト）を生成

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())