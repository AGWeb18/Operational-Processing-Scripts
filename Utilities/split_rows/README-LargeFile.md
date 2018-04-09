### Split Large File into Chunks


```vb
Sub test()
Dim iCalc As Long, i As Long
iCalc = Application.Calculation
With Application
    .Calculation = xlManual
    .ScreenUpdating = False
    .EnableEvents = False
End With
 
With ThisWorkbook.ActiveSheet
    For i = 2 To .Range("A" & Rows.Count).End(xlUp).Row Step 1000
        Range(.Range("A1:V1").Address(0, 0) & "," & .Range(Cells(i, "A"), Cells(i, "V").Resize(1000)).Address(0, 0)).Copy
            Workbooks.Add
            Range("A1").PasteSpecial xlPasteValues
            With ActiveWorkbook
                .SaveAs Filename:="C:\Users\aridding\Documents\BA Related\Mapping - Reconciliation\ImportFiles\Non-Serialized\MO - Import - Apr9 - 2017mgr_override_PCRProf_NP" & i & ".xlsx"
                .Close
            End With
    Next i
End With
With Application
    .Calculation = iCalc
    .ScreenUpdating = True
    .EnableEvents = True
End With
End Sub

```
