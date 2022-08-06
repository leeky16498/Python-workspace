inputs = [(0.0000, 0.0000), (0.1600, 0.1556), (0.2400, 0.3543), (0.2800, 0.3709),
    (0.3600, 0.4702), (0.4000, 0.4868), (0.5000, 0.5530), (0.5200, 0.6026),
    (0.6000, 0.6358), (0.6200, 0.3212), (0.6600, 0.7185), (0.7000, 0.7351),
    (0.7600, 0.8013), (0.8400, 0.7848), (0.9600, 0.9669), (1.0000, 1.0000)]
# nomalization? 0과 1사이의 값으로 처리해주는 것이다. 
# nomalised age = (age - min.age) / (max.age - min.age), 넘파이 nomalised 함수 사용도 가능하다.

targets = [230, 555, 815, 860, 1140, 1085, 1200, 1330, 1290,
           870, 1545, 1480, 1750, 1845, 1790, 1955]

w1 = 0.1
w2 = 0.2
b = 0.3
epochs = 4000
learning_rate = 0.1
def predict(i1, i2):
    return w1 * i1 + w2 * i2 + b
# 가장 최적의 모델을 찾기 위해서는 에폭과 학습률, 하이퍼 파라미터의 역할이 매우 크다.

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
    
    
# 테스트 데이터로 확인해본다.
test_inputs = [(0.1600, 0.1391), (0.5600, 0.3046),
                (0.7600, 0.8013), (0.9600, 0.3046), (0.1600, 0.7185)]

test_targets = [500, 850, 1650, 950, 1375]

pred = [predict(i1, i2) for i1, i2 in test_inputs]

for p, t in zip(pred, test_targets):
    print("target : {}, predicted : {}".format(t, p))
    
# 데이터를 표준화 한 후 한 테스트는 정확도가 매우 높다.