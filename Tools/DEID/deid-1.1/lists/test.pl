
# # $doctor_list = "";
# open CF, "original_test90.text" or die "Cannot open";
# while ($string = <CF>){

# $doctor_list = "";
# # $string = "Drs. <PHI TYPE=\"DOCTOR\">Bo Ao</PHI>";
# print "$string\n";
# $doctor_file = "doctor_names.txt";
# open DF, ">>$doctor_file" or die "Cannot open";

# if ($string =~ /\bDoctor\s+names\s*\=\s*([a-z])/ig) {
# 	$doctor_list = ($1);
# 	print "1. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format2: 2-token-name. ex: DR. Sam Smith. both names must be intialUppercase
# elsif ($string=~ /(([dD][Rr]([Ss])?))(\.|,)* <PHI TYPE=\"DOCTOR\">(([^\Wa-z0-9_][^\WA-Z0-9_]*\b)(\s+[^\Wa-z0-9_][^\WA-Z0-9_]*\b))/){
# 	 $doctor_list = ($5);
# 	 print "2. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# 	 print DF "$doctor_list\n";
# }
# # Doctor format3: with ands ex: Dr. Antonioni and Gelman
# elsif ($string=~ /(([dD][Rr]([Ss])?))(\.|,)* <PHI TYPE=\"DOCTOR\">(\w+\s(and|AND)\s(\w+))/){
# 	$doctor_list = ($5);
# 	print "3. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format4: ex: Dr. F. Gelman.
# elsif ($string=~ /(([dD][Rr]([Ss])?))(\.)*\s<PHI TYPE=\"DOCTOR\">((\w+)(\.)*\s(\w+))/){
# 	$doctor_list = ($5);
# 	print "4. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format5: ex Dr. Antonioni
# elsif ($string=~ /(([dD][Rr]([Ss])?))(\.|,)* <PHI TYPE=\"DOCTOR\">(\w+)/){
# 	$doctor_list = ($5);
# 	print "5. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format6: 2-token-name. without '.''  ex: Dr. Fas Aas 
# elsif ($string=~ /(([dD][Rr]([Ss])?))(\.|,)* <PHI TYPE=\"DOCTOR\">((\W\w+)(\W\w+))/){
# 	$doctor_list = ($5);
# 	print "6. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format7: MD2. ex: Olivia MD. 
# elsif ($string=~ /(\w+\W\s*\w+\W*)(((M|m)(\.)*(\s*)(D|d)(\.)*))/){
# 	$doctor_list = ($1);
# 	print "7. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# # Doctor format8: Drs plural. ex: DRS. Ao Li
# elsif ($string=~ /(Drs|DRS)(\.)* <PHI TYPE=\"DOCTOR\">(.+)/){
# 	$doctor_list = ($3);
# 	print "8. $1 --- $2 ---- $3 --- $4 ---- $5 ---- $6 ---- $7 ---- $8 \n";
# }
# else{
# 	print "no match\n";
# }

# print "$doctor_list\n";
# close DF;
# }
# close CF;

# open CF, "doctor_names.txt" or die "Cannot open";
open CFS, ">doctor_names_regx.txt" or die "Cannot open";
@not_sorted = ();
$test = "hi";
push @not_sorted, "$test\n";
push @not_sorted, "what\n";
# @not_sorted = <CF>;  # read entire file in the array
# print @not_sorted;
print @not_sorted;
@sorted = sort { lc($a) cmp lc($b) } @not_sorted; # alphabetical sort
print @sorted;
foreach(@sorted) {
	print CFS "$_";
}
# print CFS join ("\n", @sorted);
# print CFS @sorted;
close CFS;
# close CF















