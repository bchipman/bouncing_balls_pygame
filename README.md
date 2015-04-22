
[Source](http://www.ics.uci.edu/~pattis/ICS-46/assignments/program1/program.html "Permalink to Program 1")

<p align="center">
<h1>
Program 1<br>
Programming using the ICS-46 Template Library (ITL):<br>
Stack, Queue, Priority Queue, Set, and Map
</h1>
</p>
#### ICS-46: Data Structure Implementation and Analysis

<h1> Program 1 </h1>

* * *
* * *
# Program 1 - Programming using the ICS-46 Template Library (ITL): Stack, Queue, Priority Queue, Set, and Map
#### ICS-46: Data Structure Implementation and Analysis


# Introduction
This programming assignment is designed to ensure that you know how to use combinations of ITL's templated classes to model and compactly write code that solves a variety of different programming problems. The kind of abstract thinking that goes into modeling solutions to these programming problems with these data types (and iteration over them) is critical to your development as computer scientists.

There are three parts to this assignment. In each you will be asked to write a program (**.cpp** file) that defines a few functions and has a **main** function, which ties these functions together to solve the problem.

You should download the [program1][1] project folder and use it to create an Eclipse project (needing only **courselib** not **googletest**). You will create each program in this project, and submit each program separately in Checkmate. The project folder contains boiler-plated files (including some **typedefs** that I found useful in my code: you may change their names) and contains all the data files you need to test/debug you program. **Important: Only one of the **.cpp** files can be active at any time.** In the download, all are active; so I suggest that you inactivate the **runoffvoting.cpp** and **fa.cpp** files and work on **reachable.cpp** first. To make a progam inactive, select it (in the editor tab), use the **Ctrl/a** command to select all its lines, and then click **Source** at the top left of the menu and choose **Toggle Comment**: every line will now appear in a comment; by using these same instructions, you can toggle back those lines to not have comments.

**Instead, you can also use a existing/working project folder: remove (but save) all the files in its **src** folder and then put all the **.cpp** files from the downloaded project's **src** folder into the existing/working project's **src** folder. Also put all the data files into the existing project folder, not in the **src** folder.**

You should work on this assignment in pairs. Try to find someone who lives near you, with similar programming skills, and work habits/schedule: e.g., talk about whether you prefer to work mornings, nights, or weekends; what kind of commitment you will make to submit program early, etc. If you believe that it is impossible for you to work with someone, because of some special reason(s), you should send me email stating them and asking for special permission to work alone (which I do grant, but not frequently).

**Only one student should submit all parts of the the assignment**, but both student's names (along with their UniqueID) should appear in the comments at the top of **each submitted .cpp** file. It should look something like

    //Romeo Montague(UniqueID from grades spreadsheet)
    //Juliet Capulet(UniqueID from grades spreadsheet)
    //We certify that we worked cooperatively on this programming
    //  assignment, according to the rules for pair programming

If you do not know what the terms **cooperatively** and/or **rules for pair programming** mean, please read about [Pair Programming][2] before starting this assignment. Please turn in each program **as you finish it**, so that I can accurately assess the progress of the class as a whole during this assignment.

Print this document and carefully read it, marking any parts that contain important detailed information that you find (for review before you turn in the files). You should familiarize yourselves with the **ics46goody.hpp** file in the **courselib/src** folder. It contains functions useful in all these programs: **split** and **join** (like their counterparts in Python, they use **std::string** and **vector<std::string>**), **prompt_string**, and **safe_open**.

This assignment has 5 parts: pairs should work on each part together, not split them up and do them separately. Parts 1-3 are 14 points each (42 points total); Part 4 is worth 10 points; Part 5 is worth 8 points. This skewing of points towards the simpler parts means students finishing the first three parts correctly will have a 70% average; those finishing the first four parts correctly will have about an 87% average; but to get an A on this assignment requires solving all parts correctly. Remember I'm going to be running MOSS on the parts of this assignment to check for program similarity.

**Important**: The [cross_reference][3] program shows an exmple of the form of code that you need to write for these programs: study and understand its code before attempting to start solving these problems. Questions about **cross_reference**? Post them on a Message Board in the Forum.

Use the array implementations supplied in the ITL for all the data types. The programs in the folder you will download has **#include** statements at the top for all the files that you need to use.

Along with the details of the functions, I've included the number of lines that I wrote in my solution. I am supplying these number of lines **not** as a requirement, but as a ballpark estimate of the amount of code you should write.  |
* * *

##Problem #1: Reachability

### Problem Summary:

* Write a program that prompts the user to enter the name of a file representing a graph.
* Read the information in the file, storing the graph in a map.
* Print the graph.
* Repeatedly prompt the user for a starting node in the graph, and compute and print all the nodes that are reachable from it by following edges in the graph: convert the algorithm for reachability, described in detail below, into C++/ITL code.

### Input and Output

Read a file of pairs of node names (representing edges) in a directed graph, building a **Map** whose key is a **std::string** source node and whose value is a **Set** of **std::string** destination nodes that are each reachable from the source node key. Although the supplied input files use 1-letter names, your code should work for any strings: use the **split** function in **ics46goody.hpp**.

Two nodes appear on each line: first the source node, then the destination node, with these node names separated by one semicolon character. For example, the input file **graph1.txt** contains the following lines (which could appear in this order, or any other): **

      c;f
      b;d
      a;c
      c;e
      d;g
      a;b
      e;d
      f;g
      f;d

which represent the graph

Print the graph, one source node per line (the source nodes are printed alphabetically) followed by the set of all the destination nodes that the source can immediately reach. The graph above would print as

      Graph: source -&gt; {destination} edges
        a -&gt; set[c,b]
        b -&gt; set[d]
        c -&gt; set[f,e]
        d -&gt; set[g]
        e -&gt; set[d]
        f -&gt; set[g,d]


Note that the source nodes are **sorted** alphabetically, but the **Set** of desintation nodes does **not have to be sorted**: in fact it makes no sense to talk about sorted **Sets**; we could talk about a sorted **Priority Queue** whose contents came from a **Set**. Note that because node **g** is not a source node (it is only a destination node), it does not appear first on any line (and appears only in the **Sets** for source nodes **d** and **f**).

Note that there are multiple data files for this program: **graph1.txt**, **graph2.txt** and **graph3.txt**; test/debug your program on the first file; when you are done, test it on the last two. Draw the graph represented by each for to ensure that your code correctly prints it and computes the nodes reachable from any source node (which you can do by eyeballing the graphs: they are small).

Repeatedly prompt the user for a starting node in the graph (until **quit** is entered) and compute and print all the nodes that are reachable from it by following edges in the graph. Reject any node not present as keys in the graph. An example interaction (processing the graph above) might be

      Enter starting node (enter quit to quit): e
      Reachable from node name e = set[e,d,g]

      Enter starting node (enter quit to quit): x
        x is not a source node name in the graph

      Enter starting node (enter quit to quit): a
      Reachable from node name a = set[a,c,b,f,e,d,g]

      Enter starting node (enter quit to quit): quit


### Functions and Program

* **read_graph** has an open (file) parameter; it returns the **Map** representing the graph (mine is 12 lines of code).
* **print_graph** has a **Map** parameter (representing the graph); it returns nothing, but it prints the graph in the appropriate form (mine is 7 lines of code).
* **reachable** has a **Map** parameter (representing the graph) and a **std::string** start node in the graph (technically a key in the **Map**); it returns a **Set** of all the nodes reachable from the start node by following edges in the graph (mine is 15 lines).
* Write a program at the bottom of this module that calls these functions to solve the problem (mine is 22 lines). To simplify the interaction, you may prompt for the file name and specify a default value (**graph1.txt**): see my **prompt_string** function in **ics46goody.hpp** in the **courselib/src** folder.

Here is the basic algorithm for computing reachability; it is simple to explain and not (very) complicated to implement. But, you have to understand these instructions and carefully translate them into C++/ITL code. You should hand-simulate this algorithm using the graph above, and verify that it produces the results you expect before coding it. You might be tempted to use recursion, but please don't: unless recursion is done very carefully, it will run forever on graphs with cycles: one of the input files is a graph with cycles.
    1. To compute all the reachable nodes in a graph, create a **Set** (initially empty) of reached nodes and a **Queue** (initially containing the parameter start node) of nodes that we are going to explore (to find nodes they can reach).

    2. While the **exploring queue** still has nodes, remove the first one and put it into the **reached set**; if it is a key in the graph (not all nodes are) then for all its destination nodes that are not already in the **reached set**, put them in the **exploring queue**.

    3. When the **exploring queue** becomes empty (can you argue that this always will happen -there is no infinite looping), return the **reached set**.

Print the set containing all these node labels. When debugging this algorithm, print the the entire **Set** and **Queue** contents (using **&lt;&lt;**, the standard insertion operator for these data types) after every interesting change, or use the debugger to observe these changes.

### Sample Interaction

The program, as specified, will have the following interaction: user-typed information appears in _italics_. Your output should "match" this one (sets will match if they have the same contents, independent of their order). You should also check that it works for other starting nodes, and a variety of starting nodes in the other graphs. **

      Enter graph file name[graph1.txt]:

      Graph: source -&gt; {destination} edges
        a -&gt; set[c,b]
        b -&gt; set[d]
        c -&gt; set[f,e]
        d -&gt; set[g]
        e -&gt; set[d]
        f -&gt; set[g,d]

      Enter starting node (enter quit to quit): e
      Reachable from node name e = set[e,d,g]

      Enter starting node (enter quit to quit): x
        x is not a source node name in the graph

      Enter starting node (enter quit to quit): a
      Reachable from node name a = set[a,c,b,f,e,d,g]

      Enter starting node (enter quit to quit): quit

* * *

# Problem #2: Instant Runoff Voting

### Problem Summary:

* Write a program that prompts the user to enter the name of a file representing the candidate preferences of a sequence of voters.
* Read the information in the file, storing it in a **Map**.
* Print the voter preferences.
* Repeatedly display the vote count for ballots (sorted both by candidate and numerically), eliminating from the election the candidate(s) receiving the fewest votes, until one candidate (the winner) or no candidates (a tie) remain.  This form of election is known as **instant runoff voting**. Every voter submits a ballot that ranks all the candidates the election, from most favorite candidate to least favorite (we will use a **Queue** for this purpose**: earlier candidates in the **Queue** are more favored than later candidates).

During the first ballot, votes are counted for each of the candidates according to the rankings of the voters. Then the candidate(s) with the fewest number of votes are removed from the election: if more than one candidate receives the least number of votes, all candidates receiving these least number of votes are removed from the election.

During the second ballot, votes are tallied for the **remaining candidates** (there are at least 1 fewer candidates); if a voter's first ranked candidate is not still in the election, then his/her second ranked candidate should receive the vote; but if his/her second ranked candidate has been removed from the election, then his/her third ranked candidate should receive the vote ...).

This ballot process continues until either 1 candidate remains, or 0 candidates remain (meaning that all the remaining candidates tallied the same number of votes). Note that the preferences **Map** never changes, but how it is intepreted does change, since the intepretation is based on which candidates remain in the election.

### Input and Output

Read a file of voters and their ranking of the candidates, separated by semicolons, building a **Map** whose key is each voter and whose value is a **Queue** of candidates ranked by that voter (they appear in the file in order, from most favorite to least favorite).

For example, the input file **votepref1.txt** contains the following lines (which could appear in this order, or any other): **

      A;X;Y;Z
      B;Y;Z;X
      C;Y;Z;X
      D;Z;Y;X
      E;Z;Y;X

The first line means, voter **A** ranks candidate **X** first, candidate **Y** second, and candidate **Z** third. The second line means, voter **B** ranks candidate **Y** first, candidate **Z** second, and candidate **X** third. Each line will have a unique voter and a permutation of all the candidates running.

Print all the associations in this **Map**, one per line (the voters are printed alphabetically) using the following form. Each line contains the voter and his/her complete ranking of the candidates. For example, the file above would produce:

      Voter Preferences
        A -&gt; queue[X,Y,Z]:rear
        B -&gt; queue[Y,Z,X]:rear
        C -&gt; queue[Y,Z,X]:rear
        D -&gt; queue[Z,Y,X]:rear
        E -&gt; queue[Z,Y,X]:rear


Note that the voter names are **sorted** alphabetically, but the **Queue** of preferences appears in the same order they appeared in the file. There are multiple data files for this program: **votepref1.txt**, **votepref2.txt**, **votepref3.txt**, and **votepref4.txt**; test/debug your program on the first file; when you are done, test it on the rest.

Start with all the candidates. Evaluate the ballot to determine how many votes each candidate received. Print this vote count two ways: sorted alphabetically and sorted numerically (in decreasing order: if more than one candidate receives the same number of votes, they should appear sorted alphabetically). Remove the candidate(s) receiving the fewest votes, and repeat this process until only one or no candidates remain. Finally, print the outcome of the election: a single candidate winner or a tie. An example interaction (processing the preferences above) might be

      Vote count on ballot #1 with candidates alphabetically: still in election = set[X,Y,Z]
        X -&gt; 1
        Y -&gt; 2
        Z -&gt; 2

      Vote count on ballot #1 with candidates numerically: still in election = set[X,Y,Z]
        Y -&gt; 2
        Z -&gt; 2
        X -&gt; 1

      Vote count on ballot #2 with candidates alphabetically: still in election = set[Y,Z]
        Y -&gt; 3
        Z -&gt; 2

      Vote count on ballot #2 with candidates numerically: still in election = set[Y,Z]
        Y -&gt; 3
        Z -&gt; 2

    Winner is Y

The first ballot consisted of all three candidates, **X**, **Y**, and **Z**. For this ballot, the votes were counted and printed; candidate **X** received the fewest number of votes so is eliminated from the next ballot. The second ballot consisted of two candidates, **Y** and **Z**. For this ballot, the votes were counted and printed; candidate **Z** received the fewest number of votes so is eliminated from the next ballot. There is only one candidate remaining so **Y** is declared the winner. An alternative outcome might be **No winner: election is a tie among all the candidates remaining on the last ballot**

### Functions and Program

* **read_voter_preferences** has an open (file) parameter; it returns the **Map** representing each voter and his/her preferences (mine is 14 lines).
* **print_voter_preferences** has a **Map** of voter preferences as a parameter and returns nothing; it prints the title followed by the **Map** whose keys are in alphabetical order (mine is 8 lines of code).
* **print_tally** has a **std::string** title, a **Map** of candidates and their number of votes, and a function pointer as parameters and returns nothing; it prints the title followed by the **Map** in the appropriate order order (specified by the function pointer) (mine is 7 lines of code).
* **evaluate_ballot** has a **Map** of voter preferences and a **Set** of the remaining candidates as parameters; it returns a tally: a **Map** whose keys are these candidates and whose values are the number of votes they received on this ballot, based on the description of **instant runnoff voting** Remember to count only one vote per voter, for his/her highest ranked candidate who is still in the election (mine is 12 lines of code).
* **remaining_candidates** has a **Map** as a parameter whose keys are candidates and whose values are the number of votes they received and returns a set containing all those candidates remaining in the election (the one(s) receiving the fewest number of votes are absent). Note that if all the candidates receive the same number of votes, then this function returns an empty **Set** (mine is 11 lines).
* Write a program at the bottom of this module the calls these functions to solve the problem (mine is 34 lines of code). To simplify the interaction, you may prompt for the file name and specify a default value (**votepref1.txt**): see my **prompt_string** function in **ics46goody.hpp** in the **courselib/src** folder.

### Sample Interaction

The program, as specified, will have the following interaction: user-typed information appears in _italics_. Your output should match this one.

    Enter voter preference file name[votepref1.txt]:

      Voter Preferences
        A -&gt; queue[X,Y,Z]:rear
        B -&gt; queue[Y,Z,X]:rear
        C -&gt; queue[Y,Z,X]:rear
        D -&gt; queue[Z,Y,X]:rear
        E -&gt; queue[Z,Y,X]:rear

      Vote count on ballot #1 with candidates alphabetically: still in election = set[X,Y,Z]
        X -&gt; 1
        Y -&gt; 2
        Z -&gt; 2

      Vote count on ballot #1 with candidates numerically: still in election = set[X,Y,Z]
        Y -&gt; 2
        Z -&gt; 2
        X -&gt; 1

      Vote count on ballot #2 with candidates alphabetically: still in election = set[Y,Z]
        Y -&gt; 3
        Z -&gt; 2

      Vote count on ballot #2 with candidates numerically: still in election = set[Y,Z]
        Y -&gt; 3
        Z -&gt; 2

      Winner is Y

You can also try processing the **votepref2.txt** file (which leads to a **No winner** result) and **votepref3.text**.
* * *

# Problem #3: Finite Automata

### Problem Summary:

* Write a program that prompts the user to enter the name of a file representing a finite automaton: indicating its **states** and **transitions** (each transition out of a state specifies the **input** and the new **state**).
* Read the information in the file, storing it in a **Map**.
* Print the finite automaton.
* Prompt the user to enter the name of a file storing the start-state and inputs to process (each line in the file contains this combination).
* Repeatedly process these lines computing the results of the finite automaton on each input, and then display a trace of the results.  A **finite automaton** (FA) is an machine that is sometimes called Deterministic Finite Automaton (DFA). An FA is described by its **states** and its **transitions**: each **transition** for a **state** specifies an **input** and what new **state** in the FA that input leads to. We can illustrate a FA as a graph with labelled edges (see below).

### Input and Output

Read a file that describes a FA: each line contains a state and an arbitrary number of input-&gt;new state **transitions**. Build a **Map** such that each key is a **std::string** state and whose associated value is another **Map** specifying of the transitions from that state: this second **Map** has keys that are **std::string** inputs and associated values that are **std::string** states. The first token on each line is the **std::string** state and the remaining tokens (always coming in pairs) are **std::string** inputs and states. All tokens are separated by one semicolon character.

For example, the input file **faparity.txt** contains the following lines (which could appear in this order, or any other):

      even;0;even;1;odd
      odd;0;odd;1;even

Here is a picture of the **parity** FA. It graphically illustrates the two **states** (**even** and **odd**) and their **transitions**, using **inputs** (**0** and **1**) that always lead back to one of these two states.

![][4]

Here, the state **even** (meaning it has seen an even number of **1** inputs so far) is a key in the main **Map**. It's value is a **Map** with two key/value pairs **0**/**even** and **1**/**odd**. It means that in the **even** state, if the input is a **0** the FA stays in the **even** state; if the input is a **1** the FA goes to the **odd** state. And similarly (the next line) means that for the **odd** state, if the input is a **0** the FA stays in the **odd** state; if the input is a **1** the FA goes back to the **even** state. So, seeing an input of **0** keeps the FA in the same state; seeing an input of **1** flips the FA into the other state.

Print the finite automaton, one state (and its transitions) per line; the states are printed alphabetically.

For example, the file above would produce:

      Finite Automaton Description
        even transitions: map[0-&gt;even,1-&gt;odd]
        odd transitions: map[0-&gt;odd,1-&gt;even]


Note that there are multiple data files for this program: **faparity.txt** and **fadivisibleby3.txt**; test/debug your program on the first file; when you are done, test it on the last file. Draw the FA represented by each for to ensure that your code correctly prints and computes with it.

Repeatedly process lines from a second input file, computing the results of the finite automaton for a start-state and its inputs; then print out all the results in a special form. Each line in the file contains a start-state followed by a sequence of inputs. The start-state will be a state in the FA (is a key in the outer **Map**) the inputs may specify legal or illegal transitions (may or may not be keys in some inner **Map**).

For example, the input file **fainputparity.txt** contains the following three lines:

      even;1;0;1;1;0;1
      odd;1;0;1;1;0;1
      even;1;0;1;1;0;x

The first line means, the start-state is **even** and the inputs are **1**, **0**, **1**, **1**, **0**, and **1**.

The result of processing each line is to print the start-state, and then each input and the new state it transitions to, and finally print the stop-state. For the **parity** FA and the first line in this file, it should print

    Start state = even
      input = 1; new state = odd
      input = 0; new state = odd
      input = 1; new state = even
      input = 1; new state = odd
      input = 0; new state = odd
      input = 1; new state = even
    Stop state = even


### Functions and Program

* **read_fa** has an open (file) parameter; it returns the **Map** representing the finite automaton (mine is 17 lines of code).
* **print_fa** has a **Map** parameter (representing the fa); it returns nothing, but it prints the fa in the appropriate form (mine is 6 lines of code).
* **process** has a **Map** parameter (representing the fa), a **std::string** parameter (representing the start-state), and a **Queue** parameter (representing a **Queue** of **std::string** inputs); it returns a **Queue** that contains **pair**s of **std::string** that show the input and resulting state after each transition (the first value on the **Queue** has an input that is an empty string and the start state). For the example shown above, **process** returns the following **Queue**. **

        queue[pair[,even],pair[1,odd],pair[0,odd],pair[1,even],pair[1,odd],pair[0,odd],pair[1,even]]:rear

Finally, if an input is illegal (is not the key in some transition for the current state), say **"x"**, then **process** should terminate with the last **pair** in the **Queue** indicating a problem: **(x, None)** (mine is 12 lines of code).
* **interpret** has a **Queue** parameter (the result produced by the **process** function described above); it returns nothing, but it prints the results of processing a fa on an input. See how it prints the **Queue** shown above in the output further above. Also see the **Sample Interaction** below to see how it prints _input errors_ (in the last example) (mine is 13 lines of code).
* Write a program at the bottom of this module that calls these functions to solve the problem. Note that the program loops over the lines in the second file (mine is 23 lines of code). To simplify the interaction, you may prompt for the file name and specify a default value (**faparity.txt** and **fainputparity.txt**): see my **prompt_string** function in **ics46goody.hpp** in the **courselib/src** folder.

### Sample Interaction

The program, as specified, will have the following interaction: user-typed information appears in _italics_. Your output should match this one.

      Enter file with finite automaton[faparity.txt]:

      Finite Automaton
        even transitions: map[0-&gt;even,1-&gt;odd]
        odd transitions: map[0-&gt;odd,1-&gt;even]

      Enter file with start-state and input[fainputparity.txt]:

      Starting new simulation with description: even;1;0;1;1;0;1
      Start state = even
        Input = 1; new state = odd
        Input = 0; new state = odd
        Input = 1; new state = even
        Input = 1; new state = odd
        Input = 0; new state = odd
        Input = 1; new state = even
      Stop state = even

      Starting new simulation with description: odd;1;0;1;1;0;1
      Start state = odd
        Input = 1; new state = even
        Input = 0; new state = even
        Input = 1; new state = odd
        Input = 1; new state = even
        Input = 0; new state = even
        Input = 1; new state = odd
      Stop state = odd

      Starting new simulation with description: even;1;0;1;1;0;x
      Start state = even
        Input = 1; new state = odd
        Input = 0; new state = odd
        Input = 1; new state = even
        Input = 1; new state = odd
        Input = 0; new state = odd
        Input = x; illegal input: terminated
      Stop state = None

You can also try the **fadivisibleby3.txt** finite automaton file, which determines whether an integer (sequence of digits) is divisible by 3: it is if the finite automaton stops in state **rem0** (which stand for **has remainder 0**). Its input file is **fainputdivisibleby3.txt**, which represents the number **12,435,711**, which is divisible by **3**, followed by the number **823**, which is not divisible by **3** (it has a remainder of **1** when divided by **3**).
* * *

# Problem #4: Non-Deterministic FA

### Problem Summary:

* Write functions and a script that solve for a Non-Deterministic Finite Automaton the same problem that was solved for a Deterministic Finite Automaton in Problem #3 (above).

A non-deterministic finite automaton (NDFA) is machine described by its **states** and its **transitions**: each **transition** for a **state** specifies an **input** and what **state** (or **states**: that what makes it non-deterministic) that input leads to. We can illustrate an NDFA as a graph with labelled edges (see below). The critical difference is that an NDFA can have multiple edges with the same label going to different states (we'll see how to handle such transitions below).

### Input and Output

Read a file that describes an NDFA: each line contains a state and an arbitrary number of input-&gt;state **transitions**. Build a **Map** such that each key is a **std::string** state and whose value is another **Map** specifying of the transitions from that state: this second **Map** has keys that are **std::string** inputs and values are **Sets** of **std::string** states: all the states a particular input can lead to. The first token on each line is the **std::string** state and the remaining tokens (always coming in pairs) are **std::string** inputs and states: here the same input can appear multiple times with different states following. All tokens are separated by one semicolon character.

For example, the input file **ndfaendin01.txt** contains the following lines (which could appear in this order, or any other):

      start;0;start;1;start;0;near
      near;1;end
      end

Here is a picture of the **endin01** NDFA. It graphically illustrates the three **states** (**start**, **near**, and **end**) and their **transitions**, using **inputs** (**0** and **1**).

![][5]

Here, the state **start** is a key in the main **Map**. It's value is a **Map** with two key/value pairs **0** mapping to the **Set** containing **start** and **near** and **1** mapping to the **Set** containing just **start**. It means that in the **start** state, if the input is a **0** the NDFA can stay in the **start** state or it can go to the **near** state; if the input is a **1** the NDFA must stay in the **start** state. And similarly the next line means that in the **near** state, if the input is a **1** the NDFA must go into the **end** state. The last line means that the **end** state has no transitions out of it.

Print the NDFA, one state (and its transitions) per line; the states are printed alphabetically and the transition **Map** for each state is printed in the form of a standard **Map**: a series in the form **input -&gt; set of states**. Note that the state **end** is a key in the main **Map**, whose associated transitions are an empty **Map**.

For example, the file above would produce:

      Non_Deterministic Finite Automaton Description
      end transitions: map[]
      near transitions: map[1-&gt;set[end]]
      start transitions: map[0-&gt;set[start,near],1-&gt;set[start]]


Note that there are multiple data files for this program: **ndfaendin01.txt**, **ndfatrain.txt.txt**, and **ndfare.txt**; test/debug your program on the first file; when you are done, test it on the last file. Draw the NDFA represented by each for to ensure that your code correctly prints and computes with it.

Repeatedly process lines from a second matching input file (**ndfainputendin01.txt** for the example above), computing the results of the non-determinisitc finite automaton for a start-state and its inputs; then print out all the results in a special form. Each line in the file contains a start-state followed by a sequence of inputs. The start-state will be a state in the DNFA (is a key in the outer **MapMap**).

For example, the input file **ndfainputendin01.txt** contains the following two lines:

      start;1;0;1;1;0;1
      start;1;0;1;1;0;0

For example, the first line means, the start-state is **start** and the inputs **1**, **0**, **1**, **1**, **0**, and **1**.

The result of processing each line is to print the start-state, and then each input and the new states (plural) it could transition to (the **could** is what makes it non-deterministic), and finally print the stop-states. For the **ndfaendin01** NDFA and the first line in this file, it should print

      Start state = set[start]
      Input = 1; new states = set[start]
      Input = 0; new states = set[start,near]
      Input = 1; new states = set[start,end]
      Input = 1; new states = set[start]
      Input = 0; new states = set[start,near]
      Input = 1; new states = set[start,end]
    Stop state(s) = set[start,end]


Note especially that in the **start** state, if the input is a **0**, then the NDFA can either remain in the **start** state or go into the **near** state. For this program, we keep track of all states that the NDFA can be in, using a **set** of **new possible states**. For the next input, **1**, we can be either in the **start** state (from the **start** state, an input of **1** allows us to stay in the **start** state) or the **end** state (from the **near** state, an input of **1** allows us to transition to the **end** state). Thus, we keep track of the **set** of states the NDFA can be in, and the new **set** of states the NDFA can be in after processing the next input for each of these states. In this example, because **'end'** is included in the stop-states, this input does end in **01**.

### Functions and Script

* **read_ndfa** has an open (file) parameter; it returns the **Map** representing the non-deterministic finite automaton; **hint**: I used a **while** loop to read lines and a nested **for** loop to construct the **Map** storing each input and the **Set** of states it can lead to (mine is 17 lines).
* **print_ndfa** has a **Map** parameter (representing the NDFA); it returns nothing, but it prints the NDFA in the appropriate form (mine is 6 lines).
* **process** has a **Map** parameter (representing the NDFA), a **std::string** parameter (representing the start-state), and a **Queue** parameter (representing the sequence of **std::string** inputs); it returns a **Queue** that contains **pair**s of inputs and the resulting states after each transition. For the example shown above, **process** returns the following **Queue**. **

          queue[pair[,set[start]],pair[1,set[start]],pair[0,set[start,near]],pair[1,set[start,end]],
            pair[1,set[start]],pair[0,set[start,near]],pair[1,set[start,end]]]:rear

Finally, if an input is illegal (is not the key in some transition for the current state), just ignore it (mine is 13 lines).
* **interpret** has a **Queue** parameter (the result produced by **process**; it returns nothing, but it prints the results of processing an NDFA on an input. See how it prints the **Queue** shown above in the output further above (mine is 10 lines).
* Write a script at the bottom of this module that calls these functions to solve the problem. Note that the script loops over the lines in the second file (mine is 23 lines).

### Sample Interaction

The program, as specified, will have the following interaction: user-typed information appears in _italics_. Your output should "match" this one (recall the order of values in sets is not important).

      Enter file name of Non-Determinstic Finite Automaton[ndfaendin01.txt]:
      Non_Deterministic Finite Automaton Description
        end transitions: map[]
        near transitions: map[1-&gt;set[end]]
        start transitions: map[0-&gt;set[start,near],1-&gt;set[start]]

      Enter file name of start-states and input[ndfainputendin01.txt]:

      Starting new simulation with description: start;1;0;1;1;0;1
      Start state = set[start]
        Input = 1; new states = set[start]
        Input = 0; new states = set[start,near]
        Input = 1; new states = set[start,end]
        Input = 1; new states = set[start]
        Input = 0; new states = set[start,near]
        Input = 1; new states = set[start,end]
      Stop state(s) = set[start,end]

      Starting new simulation with description: start;1;0;1;1;0;0
      Start state = set[start]
        Input = 1; new states = set[start]
        Input = 0; new states = set[start,near]
        Input = 1; new states = set[start,end]
        Input = 1; new states = set[start]
        Input = 0; new states = set[start,near]
        Input = 0; new states = set[start,near]
      Stop state(s) = set[start,near]


The **ndfatrain.txt** file is a non-deterministic finite automaton that determines whether an train (sequence of characters representing different kinds of cars) is a legal train according to Chapter Exercise #7 in the ENBF lecture from ICS-33.. Its input file is **ndfainputtrain.txt**, whose first input represents a legal train: ends when **done** is one possible stopping state; and second input represents an illegal train.

The **ndfare.txt** file is a non-deterministic finite automaton translation of the regular expression **((a*|b)cd)+**. Its input file is **ndfainputre.txt**, whose first input represents a matching string: ends when **last** as one possible stopping state; and input second does not match.  |
* * *

# Problem #5: Word Generator

### Problem Summary:

* Write a script that prompts the user to enter the **order statistic** (a positive number) and the name of a file of text.
* Read the file of text, storing a special **corpus** in a **Map**.
* Print the **corpus Map**.
* Prompt the user to enter the order statistic number of words, and the number of random words to generate, then print the original words followed by the words randomly generated from the **corpus**.  Your program will "learn" the word pattern of an author (based on some "order statistic" and reading a large sample of the author's writing) and then generate random text following the author's word patterns.

### Input and Output

After prompting for the order statistic, read a file of words, building a **Map**. Here the **Map**'s keys are **Queues**s of **n** words (**n** is the order statistic**) and each key's value is a **Set** of all the words in the text that ever follow these **n** words: e.g., if **n** were **2**, the **Map** would contain a keys that are **Queue**s of 2 words (for every pair of words appearing next to each other in the text) and whose values are a **Set** of all the words following the key (no matter where the pair occurs in the text; the **Set** stores no duplicate words).

The easiest way to process the words one at a time is to use an outer loop reading lines of text and an inner loop scanning all the words when the line is split using a space character. To process a new word, if the **Queue** doesn't have **n** words, just enqueue the word; if the **Queue** has **n** words, use it as a key and put the new word in its associated **Set**, then dequeue the first word and enqueue the new word (so the **Queue** will still contain **n** words).

For a simple example, the file **wginput1.txt** contains the following lines (it could have all this information on one line or more lines):

      a b c b a d c b a d
      c a a b a a d


Print all the associations in the **Map**, one per line in standard lexical order.

After printing all associations, print the size of the smallest and largest **Set** that is a value in the **Map**. Each line contains an **n** word **Queue**, followed by the **Set** of unique words that follow them in the text. In standard lexical order, the keys appear in order relative to the first word in the **Queue** (alphabetically); for all first words that are the same, they appear in order relative to the second word in the **Queue** (alphabetically); for all first and second words that are the same, they appear in order relative to the third word in the **Queue**; etc. (see the example below).

For example, the file above would produce:

      Corpus
        queue[a,a]:rear -&gt; set[b,d]
        queue[a,b]:rear -&gt; set[c,a]
        queue[a,d]:rear -&gt; set[c]
        queue[b,a]:rear -&gt; set[d,a]
        queue[b,c]:rear -&gt; set[b]
        queue[c,a]:rear -&gt; set[a]
        queue[c,b]:rear -&gt; set[a]
        queue[d,c]:rear -&gt; set[b,a]
      min/max = 1/2


For example, **queue[a,d]:end** appears three times in the text above, twice followed by **c** and once followed by nothing (at the end of the file); **queue[a,b]:end** appears twice in the file above, first followed by **c** and second followed by **a**.

Prompt the user for the words to start with (there are order statistic number of them; they must be in some **Queue** that is a key in the **corpus**) and the number of random words after that to generate. Produce the list of all words and print it.

A random 10 word list, after the words **a** and **d** might print as

    **    Random text = queue[a,d,c,a,a,b,a,d,c,b,a,d]:rear**

In the result we start with **a d** (specified by the user), we know only **c** can come next; then using **d c** we know that either **b** or **a** must come next; it randomly chooses **a**...

### Functions and Script

* **read_corpus** has an order statistic parameter and and open (file) parameter; it returns the **Map** representing the corpus of words in a file (mine is 17 lines).
* **print_corpus** has a **Map** parameter (representing the corpus); it returns nothing, but it prints the corpus in the appropriate form followed the min and max value **Set** sizes (mine is 11 lines + the **queue_gt** function).
* **produce_text** has a **Map** parameter (representing the corpus), a **Queue** parameter (representing the starting words), and an **int** parameter (representing the number of random words to generate); it returns a **Queue** that contains the the starting words followed by the generated words.

**Hint**: use two **Queue**s of words, both starting out with the starting words. The first will always contain the current **n** words to be used as a key in the **Map**); the second will contain all the generated words. Generate a random next word from the **Map** using the **random_in_set** function that I wrote in this file; then drop the first word from the **Queue** and add the generated word, so it remains a **Queue** of size **n**; repeat until you have generated the required number of words.

**Warning**: you might have to stop prematurely if you generate the last **n** words in the text, and if these words occur nowhere else. That is because in this case, there is no random word to generate following them; in this case add a **"None"** to the end of the **Queue** of words and immediately return that **Queue** (mine is 14 lines).
* Write a script at the bottom of this module that calls these functions to solve the problem. (mine is 21 lines).

### Sample Interaction

The program, as specified, will have the following interaction: user-typed information appears in _italics_. Your output should match this one.

    **  Enter order statistic[2]:
      Enter file name to process[wginput1.txt]:

      Corpus
        queue[a,a]:rear -&gt; set[b,d]
        queue[a,b]:rear -&gt; set[c,a]
        queue[a,d]:rear -&gt; set[c]
        queue[b,a]:rear -&gt; set[d,a]
        queue[b,c]:rear -&gt; set[b]
        queue[c,a]:rear -&gt; set[a]
        queue[c,b]:rear -&gt; set[a]
        queue[d,c]:rear -&gt; set[b,a]
      min/max = 1/2

      Enter 2 words to start with
      Enter word 1: a
      Enter word 2: d
      Enter # of words to generate: 10
      Random text = queue[a,d,c,a,a,b,a,d,c,b,a,d]:rear**

The **wginput2.txt** file cannot be used to generate a large number of random words for the reason explained in the **Warning** above.

With the appropriate modification, we can use this same program to read/generate music or DNA sequences or any other data made of symbols.  |

[1]: program1.zip
[2]: ../../../common/handouts/pairprogramming.html
[3]: ../../programs/cross_reference.zip
[4]: http://www.ics.uci.edu/images/parity.jpg
[5]: http://www.ics.uci.edu/images/endin01.jpg
  </std::string>
