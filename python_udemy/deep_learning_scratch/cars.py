inputs = [0.2, 1.0, 1.4, 1.6, 2.0, 2.2, 2.7, 2.8, 3.2,
          3.3, 3.5, 3.7, 4.0, 4.4, 5.0, 5.2]
targets = [230, 555, 815, 860, 1140, 1085, 1200, 1330, 1290,
           870, 1545, 1480, 1750, 1845, 1790, 1955]

w = 0.1
b = 0.3
epochs = 400
learning_rate = 0.05

def predict(i):
    return w * i + b 

# training loop 

for epoch in range(epochs):
    pred = [predict(i) for i in inputs] 
    cost = sum([(p - t) ** 2 for p, t in zip(pred, targets)]) / len(targets)
    print("w : {}, b : {}, c : {}".format(w, b, cost))
    
    error_d = [2 * (p-t) for p, t in zip(pred, targets)]
    weight_d = [e * i for e, i in zip(error_d, inputs)]
    bias_d = [e * 1 for e in error_d] 
    
    w -= learning_rate * sum(weight_d) / len(weight_d)
    b -= learning_rate * sum(bias_d) / len(bias_d)
    
# 어느순간 가중치와 편향, 비용이 모두 하나로 수렴하게 되는데 이는 모델이 더 이상 발전할 수 없음을 나타내준다.

# test network
# 다음과 같이 가장 최적의 가중치와 편향을 찾게되면 그 다음 테스트 데이터를 통해서 그 값을 예측해볼 수 있다.(선형회귀))

print(predict(4))