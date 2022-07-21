import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


#1 – Crie um modelo de classificação de imagens, a partir da importação da base
# de dados do Sci-kit Learn. Este modelo deve ter as seguintes características:

#a) Utilize a base de dados Mnist Dataset
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title('Training: %i' % label)


#b) Divida a base de treinamento e teste em 80/20.
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

clf = svm.SVC(gamma=0.001)

X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.2, shuffle=False)

clf.fit(X_train, y_train)

predicted = clf.predict(X_test)


#c) Utilize a técnica de Cross Validation (K-fold = 5)


#d) Utilize a técnica de Random Search ou Grid Search para escolha dos melhores
# parâmetros


#e) Faça a impressão da matriz de confusão para o modelo
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')

print(f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n")





#2 – Após a etapa de treinamento, analise o modelo respondendo as questões a
#seguir:

#a) Qual a acurácia do modelo? Justifique
# A acurácia do modelo é de 96%

#b) O modelo teve uma boa performance? Justifique
# Ao final dos testes, pode-se perceber que a performance do modelo teve um bom resultado.
# isso pode ser medido pela sua acurácia que foi de 96%, um valor alto se analisada
# a simplicidade do código.


#c) Quais foram os melhores parâmetros escolhidos? Justifique
# Os melhores parametros foram: ......

#d) Quais as principais dificuldades encontradas para a criação do seu modelo
# de classificação?
# A maior dificulade para a criação do modelo foi o baixo volume de dados.
# Aumentando o numero de dados a serem analisados, podemos obter uma melhor performance.






#3 – Faça uma pesquisa para conhecer um pouco mais sobre o universo de
# Machine Learning e responda as questões a seguir:

#a) Qual é a diferença entre um parâmetro de modelo e um algoritmo de
# aprendizagem de hiperparâmetro?
# Enquanto um parâmetro é o que o modelo aprende/adapta com o seu treino, um hiperparâmetro
# é tudo que é informado para o algoritmo antes dele começar os treinos.


#b) Você pode citar quatro dos principais desafios do aprendizado de
# máquina?
# 1. Dados com viéses levam a modelos inviesados.
# 2. É necessário que tenhamos dados com qualidade sendo. 
# 3. Dificuldade de se inserir ética em decisões delicadas.
# 4. Gerar, manter e manipular uma quantidade grande de dados.
 

#c) Se o seu modelo tem um ótimo desempenho nos dados de treinamento,
# mas generaliza mal para novas instâncias, o que está acontecendo? Você
# pode citar três soluções possíveis?
# Provavelmente, os dados estão enviesados. Ou seja, o modelo está reproduzindo um
# comportamento particular para um contexto generalista. 
# Neste caso podemos:
# 1. Retreinar o modelo do zero com dados novos
# 2. Submeter o modelo a mais alguns treinamentos com novos dados
# 3. Utilizar de outras metodologias para treinar o modelo 

#d) O que é um conjunto de teste e por que você deveria usa-lo?
# O conjuntos de teste é uma parte dos dados coletados que foi separada 
# unicamente para servir como teste. Esse conjunto irá avaliar se o modelo
# consegue identificar bem os padroes desejados da maneira esperada. 
# Vale ressaltar que ele não faz parte dos dados que são utilizados para o treinamento.


#e) Qual é o propósito de um conjunto de validação?
# O conjunto de validação se faz fundamental no contexto do Machine Learing.
# É com ele que vamos validar a capacidade do modelo em identificar padrões e
# e medir indicadores importantes de performance. 


#f) O que pode dar errado se você ajustar hiperparâmetro usando o conjunto
#de teste?
# Caso o hiperparâmetro seja ajustado de maneira incorreta, pode-se obter  
# um modelo que não consegue perceber da maneira esperada padrões, o que pode
# resultar em resultados equivocados e incorretos. 