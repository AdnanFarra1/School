Module Module1
    Dim NParticipants As Integer

    Structure Participants_Structure
        Dim ID As Integer
        Dim Full_Name As String
        Dim DOB As Date
    End Structure

    Sub Main()
        Console.WriteLine("Please enter the number of participants.")
        NParticipants = Console.ReadLine

        Dim Participants(0 To NParticipants) As Participants_Structure
        For i = 0 To NParticipants
            Console.WriteLine("Please enter participant ID")
            Participants(i).ID = Console.ReadLine
            Console.WriteLine("Please enter participant full name")
            Participants(i).Full_Name = Console.ReadLine
            Console.WriteLine("Please enter participant DOB")
            Participants(i).DOB = Console.ReadLine
        Next
        Console.WriteLine(Participants(2))









        Console.ReadLine()
    End Sub

End Module
