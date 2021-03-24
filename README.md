# BasicPortScanner

Initial commit is just a barebones single host/port scanner with no options.

## Moving forward

- Add threading.
- Add args so we can run it from cli with less interaction needed.
- Try to move to a distributed approach? Main .

## Things to look into/keep in mind

- Can i craft packets with sockets or am i limited?
    If not i'm pretty sure scapy is the ideal module to use.
- Keep it as light as possible to keep speed up.
- Script to be server and client for distributed to keep complexity down, using args to force operating mode.