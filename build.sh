# Variables
program_name=pomadur
program_version=v0.0.0-alpha
program_full_name=$program_name-$program_version
bin_directory=bin
main_script=scripts/main.py

# Clear directory for executable files
echo [ Clearing binary directories... ]

rm -rf $bin_directory dist
mkdir $bin_directory
mkdir $bin_directory/$program_full_name

echo [ Cleared! ]

echo .

# Building program to executable file
echo [ Compiling... ]

pyinstaller -D -F -n $program_name -c $main_script

mv dist/$program_name $bin_directory/$program_full_name/

echo [ Compiled! ]

echo .

echo [ Creating archive... ]

cd $bin_directory

zip -r -q $program_full_name.zip $program_full_name/

cd ..

echo [ Archived! ]
