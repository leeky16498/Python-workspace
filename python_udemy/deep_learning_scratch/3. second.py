inputs = [(0.2, 1600), (1.0, 11000), (1.4, 23000), (1.6, 24000), (2.0, 30000),
          (2.2, 31000), (2.7, 35000), (2.8, 38000), (3.2, 40000), (3.3, 21000), (3.5, 45000),
          (3.7, 46000), (4.0, 50000), (4.4, 49000), (5.0, 60000), (5.2, 62000)]
# 인풋 데이터에 연식과 마일리지 현황을 더 추가로 대입한다.

targets = [230, 555, 815, 860, 1140, 1085, 1200, 1330, 1290,
           870, 1545, 1480, 1750, 1845, 1790, 1955]

w1 = 0.1
w2 = 0.2
b = 0.3
epochs = 4000
learning_rate = 0.00000000005
def predict(i1, i2):
    return w1 * i1 + w2 * i2 + b

# training loop 
for epoch in range(epochs):
    pred = [predict(i1, i2) for i1, i2 in inputs] 
    cost = sum([(p - t) ** 2 for p, t in zip(pred, targets)]) / len(targets)
    print("epoch : {}, cost : {}".format(epoch, cost))
    
    error_d = [2 * (p-t) for p, t in zip(pred, targets)]
    weight_d1 = [e * i[0] for e, i in zip(error_d, inputs)]
    weight_d2 = [e * i[1] for e, i in zip(error_d, inputs)]
    bias_d = [e * 1 for e in error_d] 
    
    w1 -= learning_rate * sum(weight_d1) / len(weight_d1)
    w2 -= learning_rate * sum(weight_d2) / len(weight_d2)
    b -= learning_rate * sum(bias_d) / len(bias_d)
    
print("w1 : {}, w2 : {}, b : {}".format(weight_d1, weight_d2, bias_d))

# 항상 모델 훈련을 시작하기전 반드시 데이터 클리닝을 실천해라
# 1. 결측값을 보충하거나, 지워라.

# test networks 
print(predict(1, 20000))
# expected 750 and got 675, not bad
print(predict(1, 50000))
# expected output 1500, 1688 got, not bad
print(predict(5, 10000))
# unexpected value, 338