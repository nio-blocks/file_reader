FileReader
==========

Reads contents of a file.

Input signals trigger a read from a file. The contents and name of that file are placed on the notified signal as configurable attributes.

Properties
----------

-   **File** (expr): Location of file to read from. Can be absolte path, relative to nio project environment or relative block file.
-   **File Field** (str): New attribute name to add to Signal that contains the **File** name.
-   **File Contents Field** (str): New attribute name to add to Signal that contains the contents of the file.
-   **Exclude Existing** (bool): Whether or not to exclude existing data. If this is checked, a new signal will be notified for every incoming signal. In other words, no data from the incoming signal will be included on the notified signal.
-   **Results Field** (str): The attribute on the signal to store the results from this block. If this is empty, the results will be merged onto the incoming signal. This is the default operation. Having this field allows a block to "save" the results of an operation to a single field on an incoming signal and notify the enriched signal.

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
The output Signals have two attributes:
-  **File Field**, containing the **File** name.
-  **File Contents Field**, containing the contents of **File**.

If **Exclude Exiting** is True, then the original Signal will be passed through and **File Field** and **File Contents Field** will be stored in **Results Field**. If **Results Field** is blank, then **File Field** and **File Contents Field** will be merrged into the original Signal.
