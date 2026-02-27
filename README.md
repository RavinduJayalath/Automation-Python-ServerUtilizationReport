# Automation-Python-ServerUtilizationReport

## Description:
This project is an automated server monitoring solution that collects system utilization metrics (CPU, Memory, Disk) from multiple client machines and sends them to a centralized server via API. The central server aggregates the data and generates a structured weekly utilization report, which is automatically delivered via email in HTML format.

The system helps infrastructure teams monitor server health, detect abnormal usage patterns, and maintain operational stability.


## System Architecture Overview
### Client Side (Agent)
Installed on each server.<br>
It<br>
&nbsp;&nbsp;&nbsp;&nbsp;Collects system metrics:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-CPU usage %<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-RAM total / used / free<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Disk usage<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Timestamp<br>
&nbsp;&nbsp;&nbsp;&nbsp;Stores data temporarily as CSV<br>
&nbsp;&nbsp;&nbsp;&nbsp;Sends data to Central Server via REST API<br>
&nbsp;&nbsp;&nbsp;&nbsp;Can run every 20 minutes via Task Scheduler<br>

### Central Server
It<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Receives CSV files through API endpoint<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Stores them in recieved_metrics/<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Aggregates weekly data<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Generates:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-CPU daily average & peak<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Memory daily average<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Disk daily usage<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Builds professional HTML report<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Sends automated email to stakeholders<br>

### Project Structure
Server-Utilization-Monitoring/<br>
│<br>
├── Agent/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── metrics/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── Logs/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── dataTracking.py<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── apiRequest.py<br>
│<br>
├── Central/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── recieved_metrics/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── Logs/<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── weeklyReport.py<br>
│   &nbsp;&nbsp;&nbsp;&nbsp;└── api_server.py<br>
│<br>
└── README.md`

## How to Use This Project
**Step 1: Install Client Agent**<br>
On each server:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Install Python<br>
&nbsp;&nbsp;&nbsp;&nbsp;Install required libraries:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install psutil requests pandas`<br>
&nbsp;&nbsp;&nbsp;&nbsp;Configure:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Central server API URL<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Server name<br>
&nbsp;&nbsp;&nbsp;&nbsp;Schedule script using Task Scheduler:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run every 20 minutes<br>
Now client automatically pushes metrics.<br>

**Step 2: Setup Central Server**<br>
Install required packages:<br>
&nbsp;&nbsp;&nbsp;&nbsp;`pip install pandas flask`<br>
Run API service to receive metrics.<br>
Ensure folder exists:<br>
&nbsp;&nbsp;&nbsp;&nbsp;`recieved_metrics/`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`Logs/`<br>

**Step 3: Weekly Report Generation**<br>
On Central Server:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Set task in task scheduler to run *weeklyReport.py* weekly<br>
&nbsp;&nbsp;&nbsp;&nbsp;System will:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read all CSV files<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group by server<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate day-wise statistics<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create HTML report<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send email automatically<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Log status in:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Logs/automation.log`

## What the Weekly Report Includes
For Each Server:<br>
&nbsp;&nbsp;&nbsp;&nbsp;CPU<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Average CPU usage per day<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Peak CPU usage per day<br>
&nbsp;&nbsp;&nbsp;&nbsp;Memory<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total RAM<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used RAM<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Available RAM<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Memory %<br>
&nbsp;&nbsp;&nbsp;&nbsp;Disk<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total disk space<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used disk<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Free disk

    