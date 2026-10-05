import matplotlib.pyplot as plt
def main():
    language=["c","c++","java","python"]
    students=[30,40,35,55]

    plt.bar(
        language,           #values of x axis
        students,           #values of y axis
        width=0.6,          #width of bar
        edgecolor='black',  #border color of bar
        linewidth=1,        #border width of bar
        alpha=1.0,          #transparency of bar
        label="students",   #label for bar

    )
    plt.title("marvellous bar plot")
    plt.xlabel("language")
    plt.ylabel(" number of students")
    plt.legend()
    plt.show()
if __name__=="__main__":
    main()