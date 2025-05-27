import tkinter as tk
from tkinter.filedialog import askopenfilename
import control
import openpyxl as opxl

def view():
    def launchControllerWorker():
        control.start(
            excelPathVar.get(),
            wb,
            selectedWs.get(),
            inputColEntryVar.get(),
            outputColEntryVar.get(),
            firstRowVar.get(),
            lastRowVar.get()
        )


    def selectExcel():
        excelPath = askopenfilename(title="Select an EXCEL workbook",
                            filetypes=[("Excel files", "*.xlsx *.xlsm")])
        
        if not excelPath: return
        
        excelPathVar.set(excelPath)
        wb = opxl.load_workbook(excelPath)
        availableWorksheets = wb.sheetnames

        # Update the dropdown menu accordingly
        menu = worksheetDropdown["menu"]
        menu.delete(0, "end")  # clear existing options
        for ws in availableWorksheets:
            menu.add_command(label=ws, command=lambda value=ws: selectedWs.set(value))
        selectedWs.set(availableWorksheets[0])

    # style stuff
    fontType = "None"
    fontSize = 15
    fontGeneral = (fontType, fontSize)
    fontSmall = (fontType, int(fontSize/3*2))

    # root stuff
    root = tk.Tk()
    root.title("FileChop")
    rootWidth = 300
    rootHeight = 400
    root.geometry("{}x{}".format(rootWidth, rootHeight))
    root.resizable(0, 0)

    # frame stuff
    frame1 = tk.Frame(root)
    frame1.pack()
    frame2 = tk.Frame(root)
    frame2.pack()
    frame3 = tk.Frame(root)
    frame3.pack()
    frame4 = tk.Frame(root)
    frame4.pack()
    frame5 = tk.Frame(root)
    frame5.pack()

    # data variables
    wb = None
    availableWorksheets = [""]

    # var stuff
    excelPathVar = tk.StringVar(value="~~~")
    inputColEntryVar = tk.StringVar()
    outputColEntryVar = tk.StringVar()
    firstRowVar = tk.IntVar(value=0)
    lastRowVar = tk.IntVar(value="")
    selectedWs = tk.StringVar(value=availableWorksheets[0])


    ## core UI elements stuff
    #
    browseButton = tk.Button(frame1, text="Browse to Select", command=selectExcel, font=fontGeneral, width=rootWidth)
    excelPathLabel = tk.Label(frame1, textvariable=excelPathVar, font=fontSmall, anchor="e")
    worksheetDropdown = tk.OptionMenu(frame1, selectedWs, *availableWorksheets)
    browseButton.pack()
    excelPathLabel.pack()
    worksheetDropdown.pack()

    #
    inputColLabel = tk.Label(frame2, text="Input column: ", font=fontGeneral)
    inputColEntry = tk.Entry(frame2, textvariable=inputColEntryVar, font=fontSmall)
    inputColLabel.pack(side=tk.LEFT)
    inputColEntry.pack(side=tk.LEFT)

    #
    outputColLabel = tk.Label(frame3, text="Output column: ", font=fontGeneral)
    outputColEntry = tk.Entry(frame3, textvariable=outputColEntryVar, font=fontSmall)
    outputColLabel.pack(side=tk.LEFT)
    outputColEntry.pack(side=tk.LEFT)

    #
    rowLabel = tk.Label(frame4, text="Row Range: ", font=fontGeneral)
    firstRowEntry = tk.Entry(frame4, textvariable=firstRowVar, font=fontSmall, width=4)
    lastRowEntry = tk.Entry(frame4, textvariable=lastRowVar, font=fontSmall, width=4)
    rowLabel.pack(side=tk.LEFT)
    firstRowEntry.pack(side=tk.LEFT)
    lastRowEntry.pack(side=tk.LEFT)

    #
    executeButton = tk.Button(frame5, text="Execute", command=launchControllerWorker, font=fontGeneral)
    executeButton.pack()


    root.mainloop()

if __name__ == "__main__":
    view()