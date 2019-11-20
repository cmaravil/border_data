# Border Crossing Analysis


## Table of Contents

1. [About this Project](#About-this-Project)
1. [Getting Started](#Getting-Started])
1. [Test](#test)

## About this Project   

The purpose of this project was to obtain and analyze the data of U.S. border crossings from a CSV.  

Detail was focused on the following fields:
* <mark>Border</mark>: Designates what border was crossed
* <mark>Date</mark>: Timestamp indicating month and year of crossing
* <mark>Measure</mark>: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
* <mark>Value</mark>: Number of crossings

The data was grouped by border, month and type of entry (Pedestrian, Truck, etc.).  The monthy crossings were then summed and a counter was created to keep track of the running average for each month using the data leading up to each month.  




## Getting Started

The projects instructions were obtiined via Insight's Github repo:
<a href="https://github.com/InsightDataScience/border-crossing-analysis">Insigths Border Crossing Analysis Repo</a>

The data to create and test this project was obtained from The Bureau of Transportation Statistics.  
<a href="https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2">Border Crossing Data</a>

The file was saved in the input folder of my repo as: <i>Border_Crossing_Entry_Data.csv</i>  


### Download
The languaged used to create this program was Python 3
<a href="https://www.python.org/downloads/release/python-374/">Download Python</a>

Per Insightdata's instructions regarding this project, no external libraries where used.
   ***Due to this there are limitations*** *


Detail was focused on the following fields:
* <mark style="color:red">Border</mark>: Designates what border was crossed
* <mark  style="color:red">Date</mark>: Timestamp indicating month and year of crossing
* <mark style="color:red">Measure</mark>: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
* <mark style="color:red">Value</mark>: Number of crossings





##test 
We obtained a test from Insight's Github repo.




*<font size="2">Since Pandas and Numpy used, the program is slower and not optimal</font>.  
