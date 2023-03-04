import numpy as np
import random
#定義目標函數
def fitness_func(x):
    return np.sum(np.power(x,2))

#定義目標函數
def fitness_func(x):
    return np.sum(np.power(x,2))
#定義基因演算法函數
def GA(num_variables, population_size, num_generations):
    # 初始化種群
    population=np.random.rand(population_size,num_variables)

    # 跌代進化
    for i in range(num_generations):
        # 計算適應度
        fitness_values=np.apply_along_axis(fitness_func,1,population)

        # 選擇優秀的個體(將每個基因透過適應度排序(索引))
        indices=np.argsort(fitness_values)
        selected_indices=indices[:int(population_size/2)]
        selected_population=population[selected_indices, :]

        # 交叉
        #創造一個跟population一樣大小的空數組，用於儲存交叉和變異
        offspring_population=np.empty_like(population)
        for j in range(int(population_size/2)):
            parent1=selected_population[j, :]
            parent2=selected_population[random.randint(0,len(selected_population)-1), :]
            crossover_point=random.randint(1,num_variables-2)
            offspring1=np.concatenate((parent1[:crossover_point],parent2[crossover_point:]))
            offspring2=np.concatenate((parent2[:crossover_point],parent1[crossover_point:]))
            #print(2*j)
            #print(2*j+1)
            offspring_population[2*j, :]=offspring1
            
            offspring_population[2*j+1, :]=offspring2
            
          

        # 變異
        for j in range(population_size):
            individual=offspring_population[j, :]
            mutation_point=random.randint(0,num_variables-1)
            individual[mutation_point]+=np.random.normal(0,0.1)
            offspring_population[j, :]=individual

        # 跟新族群
        population=offspring_population

    # 返回最優解
    fitness_values=np.apply_along_axis(fitness_func,1,population)
    best_index=np.argmin(fitness_values)
    best_individual=population[best_index, :]

    return best_individual
best_individual=GA(10,100,10000)
print(best_individual)