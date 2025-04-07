#Miguel Fernandez
#Module 4
#4/6/2025
import csv  #Import The CVS
from datetime import datetime #Imports datetime
import sys  #Import sys
from matplotlib import pyplot as plt #Imports Matplotlib

def plot_Wheather(dates, temps, title, color):

    fig, ax = plt.subplots()  #Make figures and axe
    ax.plot(dates, temps, c=color)  # Weather values vs dates
    plt.title(title, fontsize=9)  #Title Font
    plt.xlabel('', fontsize=9)  #Make x axis blank
    fig.autofmt_xdate()  #Formats the date labels
    plt.ylabel("Temp F", fontsize=9, color='red')  #Make x axis label
    plt.tick_params(axis='both', which='minor', labelsize=9 )  #Adjust the ticks
    plt.show()  #Shows Plot

def load_data(filename):
    #Load Data from file
    with open(filename) as f:
        reader = csv.reader(f)  #Make the reader
        header_row = next(reader)  #Read header row

        # Make list of dates and temps
        dates, highs, lows = [], [], []
        for row in reader:  #Make a loop
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))
        return dates, highs, lows

def main():
    #calls menu
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = load_data(filename)  #extract data

    while True:  #Make loop
        print("\nMenu:")
        print("1 View Tmax")
        print("2 View Tmin")
        print("3 OUT")

        choice = input("1,2,3")
        if choice == '1':
            plot_Wheather(dates, highs, "TMAX 2018", "orange")
        elif choice == '2':
            plot_Wheather(dates, lows, "TMIN 2018", "purple")
        elif choice == '3':
            print("Boring Company Weather Forecast Says Thanks!")
            sys.exit()
        else:
            print("Error try 1,2,3")

if __name__ == "__main__":
    main()