FileReader
==========

Reads the contents of a file.

Input signals trigger a read from a file. The contents and name of that file are placed on the notified signal as configurable attributes.

Properties
----------

-   **file** (type:expression): Location of file to read from. Can be the absolute path, relative to the nio project environment or relative block file.
-   **file_field** (type:string): New attribute name to add to Signal that contains the `file` name.
-   **file_contents_field** (type:string): New attribute name to add to the Signal that contains the contents of the file.
-   **exclude_existing** (type:bool): Whether or not to exclude the existing signal data. If this is checked, a new signal will be notified for every incoming signal. In other words, no data from the incoming signal will be included on the notified signal.
-   **results_field** (type:string): The attribute on the signal to store the results from this block. If this is empty, the results will be merged onto the incoming signal. This is the default operation. Having this field allows a block to "save" the results of an operation to a single field on an incoming signal and notify the enriched signal.

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
-  `file_field`, containing the `file` name.
-  `file_contents_field`, containing the contents of `file`.

If `exclude_exiting` is `True`, then the original Signal will be passed through and `file_field` and `file_contents_field` will be stored in `results_field`. If `results_field` is blank, then `file_field` and `file_contents_field` will be merged into the original Signal.
