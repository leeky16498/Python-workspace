inputs = [(0.0000, 0.0000), (0.1600, 0.1556), (0.2400, 0.3543), (0.2800, 0.3709),
    (0.3600, 0.4702), (0.4000, 0.4868), (0.5000, 0.5530), (0.5200, 0.6026),
    (0.6000, 0.6358), (0.6200, 0.3212), (0.6600, 0.7185), (0.7000, 0.7351),
    (0.7600, 0.8013), (0.8400, 0.7848), (0.9600, 0.9669), (1.0000, 1.0000)]

targets = [230, 555, 815, 860, 1140, 1085, 1200, 1330, 1290,
           870, 1545, 1480, 1750, 1845, 1790, 1955]

weights = [0.1, 0.2]
b = 0.3
epochs = 4000
learning_rate = 0.1

def predict(inputs):
    return sum([w * i for w, i in zip(weights, inputs)]) + b

# training loop 
for epoch in range(epochs):
    pred = [predict(inp) for inp in inputs] 
    cost = sum([(p - t) ** 2 for p, t in zip(pred, targets)]) / len(targets)
    print("epoch : {}, cost : {}".format(epoch, cost))
    
    errors_d = [2 * (p-t) for p, t in zip(pred, targets)]
    weights_d = [[e * i for i in inp] for e, inp in zip(errors_d, inputs)]
    bias_d = [e * 1 for e in errors_d] 
    # 그래디언트는 숫자로 이루어진 종벡터 행렬이다.
    
    weights_d_T = list(zip(*weights_d)) # transpose weight_d
    
    for i in range(len(weights)):
        weights[i] -= learning_rate * sum(weight_d_T[i]) / len(weights_d)
        
    b -= learning_rate * sum(bias_d) / len(bias_d)
    
    
# 테스트 데이터로 확인해본다.
test_inputs = [(0.1600, 0.1391), (0.5600, 0.3046),
                (0.7600, 0.8013), (0.9600, 0.3046), (0.1600, 0.7185)]

test_targets = [500, 850, 1650, 950, 1375]

pred = [predict(inp) for inp in test_inputs]

for p, t in zip(pred, test_targets):
    print("target : {}, predicted : {}".format(t, p))
# 데이터를 표준화 한 후 한 테스트는 정확도가 매우 높다.
# 우린 이제 2개의 w데이터와 1개의 bias데이터를 얻는데 이를 그래디언트라고 부른다.
# 그래디언트를 계산하고, 하강시킨다. 통상 이러한 일반적 방법을 '배치 경사 하강법' 이라고 부른다.