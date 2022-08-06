import math

inputs = [(0.0000, 0.3929), (0.5484, 0.7500), (0.0645, 0.5714), (0.5806, 0.5714),
    (0.2258, 0.8929), (0.4839, 0.2500), (0.3226, 0.2143), (0.7742, 0.8214),
    (0.4516, 0.5000), (0.4194, 0.0357), (0.4839, 0.2500), (0.3226, 0.7143),
    (0.5806, 0.5000), (0.5484, 0.1071), (0.6129, 0.6429), (0.6774, 0.1786),
    (0.2258, 0.8214), (0.7419, 0.1429), (0.6452, 1.0000), (0.8387, 0.2500),
    (0.9677, 0.3214), (0.3226, 0.4643), (0.3871, 0.5357), (0.3548, 0.1429),
    (0.3548, 0.6429), (0.1935, 0.4643), (0.4516, 0.3929), (0.4839, 0.6071),
    (0.6129, 0.6786), (0.2258, 0.6071), (0.5161, 0.3214), (0.5484, 0.6786),
    (0.3871, 0.8571), (0.6452, 0.6071), (0.1935, 0.3929), (0.6452, 0.3929),
    (0.6774, 0.4643), (0.3226, 0.2857), (0.7419, 0.7143), (0.7419, 0.3214),
    (1.0000, 0.3929), (0.8065, 0.3929), (0.1935, 0.5000), (0.1613, 0.8214),
    (0.2903, 0.9286), (0.3548, 0.0000), (0.2903, 0.6786), (0.5484, 0.9643),
    (0.4194, 0.1786), (0.2581, 0.2500), (0.3226, 0.7143), (0.5161, 0.3929),
    (0.2903, 0.6429), (0.5484, 0.9286), (0.2581, 0.3214), (0.0968, 0.5000),
    (0.6129, 0.7857), (0.0968, 0.3214), (0.6452, 0.9286), (0.8065, 0.7500)]

purple = (1, 0, 0)
orange = (0, 1, 0)
green = (0, 0, 1)

targets = [purple, orange, purple, orange, green, purple, purple, green, orange,
    purple, purple, green, orange, purple, orange, purple, green, purple, green,
    purple, purple, orange, orange, purple, orange, purple, orange, orange, orange,
    green, orange, orange, green, orange, purple, orange, orange, purple, orange,
    orange, purple, orange, green, green, green, purple, green, green, purple, purple,
    green, orange, green, green, purple, purple, green, purple, green, green]


weights = [[0.1, 0.2], [0.15, 0.25], [0.18, 0.1]]
biases = [0.3, 0.4, 0.35]
epochs = 5000
learning_rate = 0.5

def softmax(predictions):
    m = max(predictions)
    temp = [math.exp(p-m) for p in predictions]
    total = sum(temp)
    return [t / total for t in temp]

def log_loss(activations, targets):
    losses = [-t * math.log(a) - (1 - t) * math.log(1-a) for a, t in zip(activations, targets)]
    return sum(losses)

# train the network
for epoch in range(epochs):
    pred = [[sum([w * i for w, i in zip(we, inp)]) + bi for we, bi in zip(weights, biases)] for inp in inputs]
    act = [softmax(p) for p in pred]
    print(sum(act[0]))
    
    cost = sum([log_loss(ac, ta) for ac, ta in zip(act, targets)]) / len(act)
    print("epochs : {}, cost : {}".format(epoch, cost))
    
    errors_d = [[a - t for a, t in zip(ac, ta)] for ac, ta in zip(act, targets)]
    inputs_T = list(zip(*inputs))# transpose training inputs
    errors_d_T = list(zip(*errors_d)) # transpose drivates
    weights_d = [[sum([e * i for e, i in zip(er, inp)]) for er in errors_d_T] for inp in inputs_T]
    biases_d = [sum([e for e in errors]) for errors in errors_d_T]
    weights_d_T = list(zip(*weights_d)) # transpose weights_delta
    
    for y in range(len(weights_d_T[0])):
        for x in range(len(weights_d_T[0])):
            weights[y][x] -= learning_rate * weights_d_T[y][x] / len(inputs)
            biases[y] -= learning_rate * biases_d[y] / len(inputs)
            


test_inputs = [(0.0000, 0.3929), (0.0645, 0.5714), (0.0968, 0.3214),
    (0.0968, 0.5000), (0.2581, 0.3214), (0.1935, 0.4643), (0.2581, 0.2500),
    (0.1935, 0.3929), (0.3226, 0.2143), (0.4839, 0.2500), (0.3226, 0.4643),
    (0.3871, 0.5357), (0.3548, 0.6429), (0.4516, 0.5000), (0.4516, 0.3929),
    (0.5161, 0.3929), (0.5484, 0.7500), (0.6129, 0.6786), (0.5161, 0.3214),
    (0.5484, 0.6786), (0.1935, 0.5000), (0.2258, 0.6071), (0.3226, 0.7143),
    (0.2903, 0.6786), (0.3226, 0.7143), (0.2258, 0.8214), (0.2903, 0.6429),
    (0.6129, 0.7857), (0.7742, 0.8214), (0.8065, 0.7500)]

test_targets = [purple, purple, purple, purple, purple, purple, purple, purple,
    purple, purple, orange, orange, orange, orange, orange, orange, orange, orange,
    orange, orange, green, green, green, green, green, green, green, green, green, green]

# test network

pred = [[sum([w * i for w, i in zip(we, inp)]) + bi for we, bi in zip(weights, biases)] for inp in test_inputs]

act = [softmax(p) for p in pred]
correct = 0

for a, t in zip(act, test_targets):
    if a.index(max(a)) == t.index(max(t)):
        correct += 1
        
print("correct : {} / {}, ({}%)".format(correct, len(act), (correct / len(act) * 100)))
# 완전하게 맞췄다. 모든 테스트 플라워를 정확하게 맞췄다.
# 하지만 만약 non-linear 데이터를 다룰때는 어떻게 해야할까? 중간에 추가적인 레이어를 추가해서 학습률에 대한 대응을 증가시킨다.
# 히든레이어의 역할 : 데이터가 가지는 추가적인 특성을 반영해주는 레이어이다. 활성화 함수는 ReLU가 많이 쓰인다.