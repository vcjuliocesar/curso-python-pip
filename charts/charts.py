import matplotlib.pyplot as plt

def generate_pie_chart():
    labes = ['A','B','C']
    values = [10,300,12]
    
    
    fig,ax = plt.subplots()
    ax.pie(values,labels=labes)
    plt.savefig('pie.png')
    plt.close()