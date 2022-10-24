#include "logic.h"
#include <stdio.h>
#include <stdlib.h>

void update_log(struct Log *log, int temp, int hum, int increment)
{
    if (log->index == log->size)
    {
        log->size += increment;
        log->log = realloc(log->log, log->size * sizeof(struct Data));
        if (log->size != 0)
        {
            printf("Log Size Expanded To: %d\n", log->size);
        };
    }
    log->log[log->index].temp = temp;
    log->log[log->index].hum = hum;
    log->index++;
    printf("Received Temperature: %d\n", temp);
    printf("Received Humidity: %d\n", hum);
}

void write_average(struct Log *log)
{
    float temp = 0;
    float hum = 0;
    for (int i = 0; i < log->index; i++)
    {
        temp += log->log[i].temp;
        hum += log->log[i].hum;
    }
    printf("Average Temperature: %.2f\n", temp / log->index);
    printf("Average Humidity: %.2f\n", hum / log->index);
}

void write_min(struct Log *log)
{
    int temp = log->log[0].temp;
    int hum = log->log[0].hum;
    for (int i = 0; i < log->index; i++)
    {
        if (log->log[i].temp < temp)
        {
            temp = log->log[i].temp;
        }
        if (log->log[i].hum < hum)
        {
            hum = log->log[i].hum;
        }
    }
    printf("Minimum Temperature: %d\n", temp);
    printf("Minimum Humidity: %d\n", hum);
}

void write_max(struct Log *log)
{
    int temp = log->log[0].temp;
    int hum = log->log[0].hum;
    for (int i = 0; i < log->index; i++)
    {
        if (log->log[i].temp > temp)
        {
            temp = log->log[i].temp;
        }
        if (log->log[i].hum > hum)
        {
            hum = log->log[i].hum;
        }
    }
    printf("Maximum Temperature: %d\n", temp);
    printf("Maximum Humidity: %d\n", hum);
};

void write_log(struct Log *log)
{
    printf("Log: %d entries\n", log->index);
    for (int i = 0; i < log->index; i++)
    {
        printf("Temperature: %d; Humidity: %d\n", log->log[i].temp, log->log[i].hum);
    };
}