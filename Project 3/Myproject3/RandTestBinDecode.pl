#!/usr/bin/env perl
#
#  Alex Nord
#  Datastructures, Fall 2016
#  Automated Testing (Sheer Brutality Edition)
#  No rights reserved
#
#  USAGE:  perl RandTestBinDecode.pl  <Decoder>  <Letters>  <n>
#
#  WHERE:  <Decoder>: is the name of the python script that
#                     we're testing against (i.e., your
#                     Project 3 submission file).
#
#          <Letters>: is the name of the file containing the
#                     alphabet we're working with.
#
#          <n>      : is the number of test iterations you
#                     want to work with.
#
#
######################################################


use warnings;
use strict;

sub ParseLettersFile;
sub GenRandPhrase;
sub CompareOutput;
sub PrintStatus;



################
################
##            ##
##   SCRIPT   ##
##            ##
################
################



# In case the user doesn't provide the correct
# number of arguments, stop execution and try
# to help them out.
#
if (@ARGV != 3) { die "\n  USAGE: ./RandTestBinDecode  <Decoder>  <Letters>  <n>\n\n"; }


# Grab each of the input arguments and give them sensible
# variable names.  These are:
#
#   1. The program we're testing
#   2. The alphabet we'll be constructing trees on
#   3. The number of tests we want to run
#
my $Decoder      = $ARGV[0];
my $LettersFile  = $ARGV[1];
my $NumTests     = int($ARGV[2]);


# Make sure that we can actually get a hold of the files
#
if (!(-e $Decoder))     { die "\n  ERROR: Could not locate program $Decoder\n\n";  }
if (!(-e $LettersFile)) { die "\n  ERROR: Could not locate file $LettersFile\n\n"; }


# Read in the list of characters from the letters file
#
my $lettersRef  = ParseLettersFile($LettersFile);
my @Letters     = @{$lettersRef};
my $num_letters = @Letters;


# The names of the files that we'll be bouncing around
#
my $out_file_name      = "Results.out";
my $test_file_basename = "test_decode_";
my $error_file_name    = "test_failures.err";


# Open up the output file.  We keep this open throughout
# the testing so we can transcribe the input and output
# used during our testing.
#
open(my $outf,'>',$out_file_name);


# For the specified number of test iterations, do testing.
# Note that success_percent is a counter until the end,
# where we convert it to a percentage.
#
my $i = 1;
my $success_percent = 0;
while ($i <= $NumTests) {

    
    # Test files are enumerated by the iteration of testing
    #
    my $testfile = $test_file_basename."$i.tmp";


    # Generate a random phrase from our character set to encode
    # (and hopefully decode)
    #
    my $encode_phrase = GenRandPhrase(\@Letters);

    
    # Piece together the command that we'll use to generate
    # the next test.
    #
    my $TestGenCmd = 'python3 TestGenerator.py '.$LettersFile.' "'.$encode_phrase.'"';
    $TestGenCmd    = $TestGenCmd.' 2>'.$error_file_name.' > '.$testfile;


    # Run the test-generation command.  If the command fails,
    # so do we.
    #
    if (system($TestGenCmd)) { die "\n  ERROR:  Test $i failed during tree generation\n\n"; }


    # Piece together the command that we'll use to decode the
    # phrase (this is the actual TESTING component).
    #
    my $DecodeCmd = 'python3 '.$Decoder.' '.$testfile.' |';


    # Compare the output of the testing command to the string
    # that we used to encode.
    #
    # If the strings aren't equal, the subroutine returns '1' and
    # we record this as an error.  Otherwise, increment the success
    # counter.
    #
    if (CompareOutput($encode_phrase,$DecodeCmd,$outf)) {
	open(my $errorfile,'>>',$error_file_name);
	print $errorfile "\n----------------------------------\n";
	print $errorfile "  FAILED PHRASE: $encode_phrase\n\n";
	close($errorfile);
	system("cat $testfile >> $error_file_name");
    } else {
	$success_percent++;
    }


    # Update that cute little status printout we all love
    #
    PrintStatus($NumTests,$i);


    # Clean up the test file
    #
    system("rm $testfile");


    # Increment our counter
    #
    $i++;
 
   
}


# Close up the output file, now that we're done with testing
#
close($outf);


# Compute the number of successes as a percentage with
# resolution 0.1
#
$success_percent = int(1000*($success_percent/$NumTests))/10;


# Overwrite the status bar with whitespace
#
my $garbage_str = ' ';
while (length($garbage_str) < 60) {
    $garbage_str = $garbage_str.' ';
}
print "$garbage_str\r";


# Print out the final success percentage
#
print "\n  Tests Complete -- $success_percent% Success Rate\n\n";


# If all tests were successful, remove the error file (it's empty!)
#
if ($success_percent == 100) { system("rm $error_file_name"); }


# Can I get a victory "toot toot?"
#
1;


###################
###################
##               ##
##   TOOT TOOT   ##
##               ##
###################
###################




#####################
#####################
##                 ##
##   SUBROUTINES   ##
##                 ##
#####################
#####################




#############################################
#
# FUNCTION: ParseLettersFile
#
# ABOUT: This function reads a file of newline-
#        separated characters (or strings) and
#        puts them in an array, returning the
#        array.
#
sub ParseLettersFile
{

    my $filename = shift;

    my @Letters = ();

    # Open file, read contents.  Any lines that
    # aren't blank get pushed onto the array.
    #
    open(my $inf,'<',$filename);
    while (my $line = <$inf>) {
	$line =~ s/\n|\r//g;
	if ($line) {
	    push(@Letters,$line);
	}
    }
    close($inf);

    # Return letters
    #
    return \@Letters;
    
}



#############################################
#
# FUNCTION: GenRandPhrase
#
# ABOUT: This function generates a random phrase
#        from an alphabet (provided as a character
#        array).  This phrase will be >= 15
#        characters long and randomly terminates
#        with likelihood 1/(|Letters|+1).
#
sub GenRandPhrase
{

    # Grab your alphabet
    #
    my $letters_ref = shift;
    my @Letters = @{$letters_ref};

    # Initialize phrase
    #
    my $phrase = '';

    # Iteratively add characters to the phrase
    # until (1.) the phrase is 15 characters long
    # and (2.) we draw the length of the array
    # as our random index.
    #
    my $rand_index = -1;
    while ($rand_index != @Letters || length($phrase) < 15) {
	$rand_index = int(rand(@Letters+1));
	if ($rand_index < @Letters) {
	    $phrase = $phrase.$Letters[$rand_index];
	}
    }

    # Return our phrase
    #
    return $phrase;

}




#############################################
#
# FUNCTION: CompareOutput
#
# ABOUT: Run a command to decode a phrase (in
#        the style of Project 3) and verify
#        that the output is what you wanted.
#
sub CompareOutput
{

    # Get the phrase that we want to match (the one
    # used to generate the string we're decoding)
    # and the command to perform our decoding.
    #
    my $input_phrase = shift;
    my $decode_cmd   = shift;

    # Grab the output file handle and print to
    # the file that we prepped for this input.
    #
    my $outf = shift;
    print $outf "\n\n";
    print $outf "INPUT : $input_phrase\n\n";

    # Haven't succeeded, yet.
    #
    my $failure = 1;

    # Read in the stdout from the decode command
    # and run through it until we hit a line that
    # isn't blank.
    #
    open(my $decode_output,$decode_cmd);
    while (my $line = <$decode_output>) {
	$line =~ s/\n|\r//g;
	if ($line) {

	    # Rip out the first bit of good stuff
	    # from the line (good stuff == not whitespace)
	    #
	    $line =~ /\s?(\S+)\s?/;
	    my $output_phrase = $1;

	    # Record the output, set failure to 0
	    # if we got the output we wanted.
	    #
	    print $outf "OUTPUT: $output_phrase\n\n";
	    if ($output_phrase eq $input_phrase) {
		$failure = 0;
	    }
	    last;
	}
    }
    close($decode_output);


    # Did we fail?
    #
    if ($failure) { print $outf "------> FAILURE\n\n"; }
    else          { print $outf "------> SUCCESS\n\n"; }


    # No way! (but just in case)
    #
    return $failure;
    
}




#############################################
#
#  FUNCTION: PrintStatus
#
#  ABOUT: OMG I love that little status bar!
#         Soooooooooooo adorable!
#
sub PrintStatus
{

    # How many tests are we planning on doing
    # in total? How many tests are complete?
    #
    my $total_tests = shift;
    my $completed_tests = shift;


    # The seed of the status bar.
    #
    my $full_str = "  ";

    # Figure out the length of the string needed
    # to represent the total number of tests.
    #
    my $total_tests_len = length(''.$total_tests);    

    # Add the number of completed tests to the
    # status bar, buffer with whitespace (for nice
    # incrementing effect).
    #
    my $comp_test_str = ''.$completed_tests;
    while (length($comp_test_str) < $total_tests_len) {
	$comp_test_str = $comp_test_str.' ';
    }
    $full_str = $full_str.$comp_test_str;
    $full_str = $full_str." tests (out of ".$total_tests.") complete   [";

    # Now the actual status-bar-thing.  Just splits
    # testing up into 5%-blocks and figures out how
    # far we are based on the number of completed tests.
    #
    my $i = 0.05;
    while ($i < (0.0+$completed_tests)/(0.0+$total_tests)) {
	$full_str = $full_str."#";
	$i += 0.05;
    }
    while ($i < 1) {
	$full_str = $full_str." ";
	$i += 0.05;
    }

    # Add the end cap and a carriage return (so we
    # can print over this next time).
    #
    $full_str = $full_str."]\r";

    # Do that fresh printin' business we all crave so bad.
    #
    print "$full_str";

    
}




#####################
#####################
####             ####
#### END OF FILE ####
####             ####
#####################
#####################

