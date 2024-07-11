cd /home/cel/MSI_Theory/MSI_variflex/Variflex_Calculations/OH+OH/Calculation_11/nominal_B1_Energy_1_0.0 
echo Running nominal Variflex...
./variflex.exe 
echo Running perturbed Variflex...
cd /home/cel/MSI_Theory/MSI_variflex/Variflex_Calculations/OH+OH/Calculation_11/perturb_B1_Energy_1_280.0 
./variflex.exe 
cd /home/cel/MSI_Theory/MSI_variflex/Variflex_Calculations/OH+OH/Calculation_11/perturb_B1_Symmetry_1_0.8 
./variflex.exe 
