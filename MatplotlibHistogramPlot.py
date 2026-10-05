import matplotlib.pyplot as plt
def main():
    marks=[45,55,60,62,65,67,70,73,75,78,80,82,85,90,93]
    plt.hist(
        marks,              #continuous data
        bins=5,             #number of groups
        edgecolor='black',  #border color of bar
        alpha=0.8,          #transparency of bar
        rwidth=0.9,         #width of bar


    )
    plt.title("marvellous histogram plot")
    plt.xlabel("marks")
    plt.ylabel("frequency")
    plt.show()
if __name__=="__main__":
    main()