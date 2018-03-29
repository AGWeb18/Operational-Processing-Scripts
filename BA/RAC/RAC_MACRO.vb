Sub POSAudit_Macro()


'''''''
'Next steps
'   Split sheet by dealer
'   Sort clients within that dealer
'   Split clients by adding a blank row between them
'''''''


'Select the Data sheet, remove duplicates filtering at Client - Module - Invoice level
Dim i As Long
Dim j As Long
Dim a As Long
Dim varRow, d, n, cIn As Integer
Dim Filter As String


'Speed up macro processing, turn off prompts
Application.ScreenUpdating = False
Application.Calculation = xlCalculationAutomatic
Application.DisplayAlerts = False
Application.DisplayStatusBar = False
Application.DisplayScrollBars = False


'   Remove Duplicates with Column A, B, C, J
Sheets("PlaceDataHere").Select
Range("$A$1:$O$800000").RemoveDuplicates Columns:=Array(1, 2, 3, 10), _
        Header:=xlYes
        
'   Store the last row of the raw data
lastrow = Range("A" & Rows.Count).End(xlUp).Row

'   Input formulas into Col Q and R
Range("Q2").Formula = "=INDEX(Email!B:B,MATCH(B2,Email!A:A,0))"
Range("R2").Formula = "=Concat(A2, "" #"", J2)"

'   Extend formula to the bottom of range.
Range("Q2").AutoFill Destination:=Range("Q2", "Q" & lastrow)
Range("R2").AutoFill Destination:=Range("R2", "R" & lastrow)

'   Copy&Paste Values inplace to remove Formulas
Columns("Q:R").Copy
Sheets("PlaceDataHere").Columns("Q:R").PasteSpecial Paste:=xlPasteValues

'Refresh workbooks Pivot Table
ActiveWorkbook.RefreshAll


'Generate the number of invoices to check based on COUNT of invoices
    Sheets("Pivot").Select
    lastrow_pivot = Range("A" & Rows.Count).End(xlUp).Row

' If the module is SPIFF, STA or IR's and the count of invoice is 1, audit return the count 1.
' if CoI(count of invoice) is >5 but <=500, audit 5 invoices.
' if CoI is >500 but <=1000, audit 10% of the records
' if CoI is >1000 but <= 2000, audit 7.5%
' if CoI is >2000 but <= 5000, audit 5%
' if CoI is >5000, audit 2.5%
    Range("C6").Formula = "=IF(OR(A6=""Spiffs"",A6=""STA"",A6=""Instant Rebates""),IFS(B6<=5,B6,B6<5,B6,AND(B6>5,B6<=500),""5"",AND(B6>500,B6<=1000),B6*0.01,AND(B6>1000,B6<=2000),B6*0.0075,AND(B6>2000,B6<5001),B6*0.005,B6>=5001,B6*0.0025),"""")"
    Range("C6").AutoFill Destination:=Range("C6", "C" & lastrow_pivot)

'   Copy&Paste Values inplace to remove Formulas
    Columns("C:C").Copy
    Columns("C:C").PasteSpecial Paste:=xlPasteValues


'   Remove text formatting - into numbers
    Columns("C:C").Select
    Selection.TextToColumns Destination:=Range("C1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=False, FieldInfo _
        :=Array(1, 1), TrailingMinusNumbers:=True
'Center/middle align
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With

'Loop through rows

For i = 6 To lastrow
        Sheets("Pivot").Select
        Range("C" & i).Select
'Check whether cell is empty or not
        If IsEmpty(ActiveCell) Then
                ActiveCell.Offset(1, 0).Select
        Else
            myr = ActiveCell.Value
            Sheets("Pivot").Select
            Range("B" & i).ShowDetail = True
            Set ws = ThisWorkbook.ActiveSheet
            ltrow = Cells(Rows.Count, 2).End(xlUp).Row
            Range("I2:I" & ltrow).Formula = "=Rand()"
            

            With ThisWorkbook.ActiveSheet
            .Range("A1:O" & ltrow).AutoFilter Field:=9, Criteria1:="<>"
            .Range("I2").CurrentRegion.Sort Key1:=.Range("I2"), Order1:=xlAscending, _
            Header:=xlYes, OrderCustom:=1, DataOption1:=xlSortNormal
            End With
            
For k = 0 To myr - 1
                        tran = ws.Range("F" & ltrow - k).Value
                        Sheets("PlaceDataHere").Select
                        Range("A:O").AutoFilter Field:=6, Criteria1:=tran
                        frow = Cells(Rows.Count, 2).End(xlUp).Row
                        Range("P" & frow).Formula = "Audit"
        Next k
                        n = ThisWorkbook.Worksheets.Count
                        For d = 1 To n
                            On Error Resume Next
                            If InStr(1, Sheets(d).Name, "Sheet") Then Sheets(d).Delete
                            On Error GoTo 0
                        Next d
             End If
    Next i
    
'   Filter PlaceDataHere sheet, and insert "To be Audited" into col P.
Sheets("PlaceDataHere").Cells.AutoFilter
Sheets("PlaceDataHere").Range("P1").Formula = "To be audited"

Sheets("PlaceDataHere").Cells.AutoFilter Field:=16, Criteria1:="Audit"

Sheets("PlaceDataHere").Select
Sheets("PlaceDataHere").Columns("A:R").Copy
Sheets("To be Audited").Columns("A:R").PasteSpecial Paste:=xlPasteValues
Sheets("Merge Ref").Columns("A:R").PasteSpecial Paste:=xlPasteValues

Sheets("Merge Ref").Select
Range("A:R").RemoveDuplicates Columns:=Array(10, 17), _
        Header:=xlYes
        
Sheets("EmailPivot").Select
ActiveWorkbook.RefreshAll

lRow = Range("A" & Rows.Count).End(xlUp).Row
For a = 4 To lRow
Sheets("EmailPivot").Select
chtxt = Sheets("EmailPivot").Range("A" & a).Text
    If InStr(1, chtxt, "@") Then
    cIn = Range("B" & a).Value
    Sheets("EmailPivot").Range("A" & a, "A" & (a + cIn)).Copy
    Sheets("MERGE DOC").Select
    Range("A100000").End(xlUp).Offset(1, 0).Select
        Selection.PasteSpecial Paste:=xlPasteAll, Operation:=xlNone, SkipBlanks:= _
        False, Transpose:=True
                Else
    ActiveCell.Offset(1, 0).Select
    End If


Next a


'''''''
'Next steps
'   Split sheet by dealer
'   Sort clients within that dealer
'   Split clients by adding a blank row between them
'''''''






''''''''''''''


ActiveWorkbook.RefreshAll
Application.DisplayAlerts = True
Application.Calculation = xlCalculationAutomatic
Application.ScreenUpdating = True
Application.DisplayStatusBar = True
Application.DisplayScrollBars = True



End Sub
