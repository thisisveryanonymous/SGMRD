green=`tput setaf 2`
reset=`tput sgr0`

echo ${green}==================example_10:${reset}
java -jar StreamHiCS-all-1.0.jar ../data/synthetic/example_10_data.arff > results/example_10_data_output.txt
echo ${green}==================example_20:${reset}
java -jar StreamHiCS-all-1.0.jar ../data/synthetic/example_20_data.arff > results/example_20_data_output.txt
echo ${green}==================example_50:${reset}
java -jar StreamHiCS-all-1.0.jar ../data/synthetic/example_50_data.arff > results/example_50_data_output.txt
echo ${green}==================activity:${reset}
java -jar StreamHiCS-all-1.0.jar ../data/real/activity.arff > results/activity.txt
echo ${green}==================kddcup99:${reset}
java -jar StreamHiCS-all-1.0.jar ../data/real/kddcup99.arff > results/kddcup99.txt
echo ${green}==================DONE${reset}