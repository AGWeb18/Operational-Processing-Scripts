Sub expand_rows()

Dim row_count As Integer
Dim lRow As Long
Dim new_range As Integer
Dim quantity_field as String

quantity_field = "U"


Application.ScreenUpdating = False

new_range = 0

'Find the last non-blank cell in column A(1)
lRow = Cells(Rows.Count, 1).End(xlUp).Row
i_counter = 2

While i_counter <= lRow And Not IsEmpty(Range("A" & i_counter).Value)

    
    'Store the Quantity field of the row
    row_count = Range(quantity_field & i_counter).Value
    
    'If the quantity of the row is greater than 1, insert that many number of rows above.
    If row_count > 1 Then
    
        '   Store the required values
        first_row = CStr(i_counter)
        end_row = CStr(i_counter + row_count - 1)
        next_row = CStr(i_counter + row_count)
        
        '   Insert the correct number of rows
        Rows(first_row & ":" & end_row).Select
        Selection.Insert Shift:=xlDown, CopyOrigin:=xlFormatFromLeftOrAbove
        
        '   Paste row contents Into range
        Rows(next_row).Copy
        Range("A" & first_row & ":" & "A" & end_row).Select
        ActiveSheet.Paste
        
        '   Delete the copied Rows
        Rows(next_row).Delete Shift:=xlUp
        
        ' Set the quantity back to 1
        Range(quantity_field & first_row & ":" & quantity_field & end_row).Value = 1
        
        range_count = Range("A" & first_row & ":" & "A" & end_row).Rows.Count
        new_range = new_range + range_count
        lRow = (lRow + new_range)
        i_counter = i_counter + 1 

    Else

        i_counter = i_counter + 1
    
    End If
    
    
Wend


Application.ScreenUpdating = True


End Sub
