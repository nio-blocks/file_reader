FileReader
==========
Reads the contents of a file. Input signals trigger a read from a file. The contents and name of that file are placed on the notified signal as configurable attributes.

Properties
----------
- **contents_attr**: New attribute name to add to the Signal that contains the contents of the file.
- **enrich**: Options for enriching output signals. *Exclude existing:*  Whether or not to exclude the existing signal data. If this is checked, a new signal will be notified for every incoming signal. In other words, no data from the incoming signal will be included on the notified signal. *Results field:* The attribute on the signal to store the results from this block. If this is empty, the results will be merged onto the incoming signal. This is the default operation. Having this field allows a block to save the results of an operation to a single field on an incoming signal and notify the enriched signal.
- **file**: Location of file to read from. Can be the absolute path, relative to the nio project environment or relative block file.
- **file_attr**: New attribute name to add to Signal that contains the `file` name.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: The output Signals have two attributes: `file_field`, containing the `file` name and `file_contents_field`, containing the contents of `file`.

Commands
--------
None

Dependencies
------------
None
