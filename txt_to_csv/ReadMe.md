#  TXT_to_CSV

## Getting Started
Convert multiple "TXT" files to "CSV". Simply place all the TXT files |" or pipe delimited - in the folder you'd like and run.
This was created to work for a specific file, so slight modification may be necessary to work on a new file type. 

## Prerequisites
To get this script up and running you will need:

+ Microsoft Excel
+ [Developer Tab Enabled](https://support.office.com/en-us/article/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45)

## Setup

+ Open Excel - Select the Developer Tab
+ Select "Visual Basic"
+ Under "Insert" --> "Module"
+ Copy and Paste the following code: 

```vba 
Sub list_files()

' List all the files in a Directory
Dim objFSO As Object
Dim objFolder As Object
Dim objFile As Object
Dim file_name As String
Dim file_name_array() As String
Dim SRC_file_path As String
Dim DEST_file_path As String

'  Input user specific paths here
SRC_file_path = "C:\<PATH_TO_SOURCE_FILES>\"
DEST_file_path = "C:\<PATH_TO_DEST_FOLDER>\"


' Create an instance of the FileSelectionObject
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get the folder object
Set objFolder = objFSO.GetFolder(SRC_file_path)


For Each objFile In objFolder.Files
file_name = objFile.Name

file_name_array() = Split(file_name, ".")
name_ = file_name_array(0)

    ChDir _
        SRC_file_path
    Workbooks.OpenText Filename:= _
        SRC_file_path + file_name _
        , Origin:=xlWindows, StartRow:=1, DataType:=xlDelimited, TextQualifier _
        :=xlNone, ConsecutiveDelimiter:=False, Tab:=False, Semicolon:=False, _
        Comma:=False, Space:=False, Other:=True, OtherChar:="|", FieldInfo:= _
        Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, 1), Array(6, 1), Array(7 _
        , 1), Array(8, 1), Array(9, 1), Array(10, 1), Array(11, 1), Array(12, 1), Array(13, 1), Array _
        (14, 1), Array(15, 1), Array(16, 1), Array(17, 1), Array(18, 1), Array(19, 1), Array(20, 1), _
        Array(21, 1), Array(22, 1), Array(23, 1), Array(24, 1), Array(25, 1), Array(26, 1), Array( _
        27, 1), Array(28, 1), Array(29, 1), Array(30, 1), Array(31, 1), Array(32, 1), Array(33, 1), _
        Array(34, 1), Array(35, 1), Array(36, 1), Array(37, 1)), TrailingMinusNumbers:=True
    
    
ActiveWorkbook.SaveAs Filename:=DEST_file_path + name_ + "csv", FileFormat:=xlCSV

ActiveWorkbook.Close
    
Next objFile

End Sub
```


## Running the Script

1. Open Excel
2. Select "Macros" 
3. Find **"list_files"** and **select "Run"**
4. Open the Destination folder and ensure the files there
