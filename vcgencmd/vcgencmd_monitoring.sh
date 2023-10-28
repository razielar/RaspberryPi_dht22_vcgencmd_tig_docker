#!/bin/bash
set -eu -o pipefail

# In raspberry pi 4, vcgencmd is located in: /usr/bin/
vcgencmd_bin=$(/usr/bin/which vcgencmd)
output_filename="/vcgencmd_data/vcgencmd_output.tsv"

main() {
    # clock 
    cpu_clock=$($vcgencmd_bin measure_clock arm | sed -e "s/^.*=//")
    # voltages
    cpu_voltage=$($vcgencmd_bin measure_volts core | sed -e "s/volt=//" -e "s/0*V//")
    # temperatures
    soc_temp=$($vcgencmd_bin measure_temp | sed -e "s/temp=//" -e "s/'C//")
    # print vcgencmd stdout
    echo -e "$cpu_clock\t$cpu_voltage\t$soc_temp" >> "${output_filename}"
}

while true
do
    main
    sleep 30
done