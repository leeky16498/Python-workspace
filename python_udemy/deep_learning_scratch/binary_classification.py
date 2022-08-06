import math

inputs = [(0.0000, 0.0000), (0.1600, 0.1556), (0.2400, 0.3543), (0.2800, 0.3709),
    (0.3600, 0.4702), (0.4000, 0.4868), (0.5000, 0.5530), (0.5200, 0.6026),
    (0.6000, 0.6358), (0.6200, 0.3212), (0.6600, 0.7185), (0.7000, 0.7351),
    (0.7600, 0.8013), (0.8400, 0.7848), (0.9600, 0.9669), (1.0000, 1.0000)]

targets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# 0 = keep, 1 = sell

weights = [0.1, 0.2]
b = 0.3
epochs = 4000
learning_rate = 0.1

def predict(inputs):
    return sum([w * i for w, i in zip(weights, inputs)]) + b

def activate(x):
    return 1 / (1 + math.exp(-x))
# 활성화 함수 : 시그모이드, 확률을 반환하는 것과도 관련이 있다. 시그모이드는 0과 1의 바이너리 분류에 매우 좋다.

def log_loss(act, target):
    return -target * math.log(act) - (1 - target) * math.log(1 - act)

# training the network
for epoch in range(epochs):
    pred = [predict(inp) for inp in inputs]
    act = [activate(p) for p in pred]
    
    cost = sum([log_loss(a, t) for a, t in zip(act, targets)]) / len(act)
    print("epoch : {}, cost : {}".format(epoch, cost))
    
    errors_d = [(a - t) for a, t in zip(act, targets)]
    weights_d = [[e * i for i in inp] for e, inp in zip(errors_d, inputs)]
    bias_d = [e * 1 for e in errors_d] 
    # 그래디언트는 숫자로 이루어진 종벡터 행렬이다.
    
    weights_d_T = list(zip(*weights_d))
    # transpose weight_d
    
    for i in range(len(weights)):
        weights[i] -= learning_rate * sum(weights_d_T[i]) / len(weights_d)
        
    b -= learning_rate * sum(bias_d) / len(bias_d)
    
    
# 테스트 데이터로 확인해본다.
test_inputs = [(0.1600, 0.1391), (0.5600, 0.3046),
                (0.7600, 0.8013), (0.9600, 0.3046), (0.1600, 0.7185)]

test_targets = [0, 0, 1, 0, 0]

pred = [predict(inp) for inp in test_inputs]
act = [activate(p) for p in pred]

for p, t in zip(act, test_targets):
    print("target : {}, predicted : {:.0f}".format(t, p))
# 완벽하게 예측을 해냈다. 적절한 에폭수와 학습률을 선택하여 최적의 모델을 구상할 수 있다.