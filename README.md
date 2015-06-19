FileReader
==========

Reads contents of a file.

Input signal trigger a read from a file. The contents of that file are placed on the notified signal in a configurable attribute.

Properties
----------

-   **File** (expr): Location of file to read from. Path must be absolute.
-   **File Field** (str): New attribute name to add to Signal that contains the **File**.
-   **File Contents Field** (str): New attribute name to add to Signal that contains the contents of the file.

Dependencies
------------
None

Commands
--------
None

Input
-----
Any list of signals.

Output
------
The output Signal will be the same as the input Signal but with two added attributes:
-  **File Field**, containing the **File**.
-  **Results Field**, containing the contents of **File**.
