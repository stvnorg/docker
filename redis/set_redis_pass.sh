#!/bin/bash

echo -ne '\n' | redis-server &
redis-cli AUTH PASSWORD
redis-cli CONFIG SET requirepass "0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b"
redis-cli AUTH 0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b
redis-cli -a 0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b shutdown
redis-server
