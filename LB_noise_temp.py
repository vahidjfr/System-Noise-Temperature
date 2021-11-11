# system noise temperature
# at receiver

t_lna = float(input("Enter Low Noise Amplifier (LNA) temperature in K:"))
t_mx = float(input("Enter mixer temperature in K:"))
t_if = float(input("Enter amplifier temperature in K:"))
g_lna = float(input("Enter Low Noise Amplifier (LNA) gain in dB:"))
g_mx = float(input("Enter mixer gain in dB:"))
g_if = float(input("Enter amplifier gain in dB:"))

# general equation
# low noise amplifier gain
g_lna = (10 ** (g_lna / 10))

# mixer gain
g_mx = (10 ** (g_mx / 10))

# intermediate frequency amplifier gain
g_if = (10 ** (g_if / 10))

# compute the equivalent noise temperature at receiver
te_rx = (t_lna + (t_mx / g_lna) + (t_if / g_lna * g_mx))

print("The equivalent received temperature is:", te_rx, "K")

# enter the feeder temp and losses
tf_rx = float(input("Enter receiver feeder temperature in K:"))
lf_rx = float(input("Enter receiver feeder loss in dB:"))
lf_rx = (10 ** (lf_rx / 10))

# compute the receiver feeder temp
tf = (tf_rx * (1 - (1 / lf_rx)))
print("The receiver feeder temperature is:", tf, "[K]")

# total noise temperature
# assume a clear-sky condition ta = 50 K
ta = 50
t = ((ta / lf_rx) + (tf_rx * (1 - (1 / lf_rx)) + te_rx))
print("The total noise temperature is:", t, "[K]")
