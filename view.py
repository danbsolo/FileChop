import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import control
import openpyxl as opxl



def launchView():
    def launchControllerWorker():
        control.launchController(
            excelPathVar.get(),
            wb,
            worksheetCombobox.get(),
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

        nonlocal wb
        wb = opxl.load_workbook(excelPath)

        # Update the combobox accordingly
        worksheetCombobox.config(values=wb.sheetnames)
        worksheetCombobox.set(wb.sheetnames[0])
        worksheetCombobox.event_generate("<<ComboboxSelected>>") # or just call the function directly


    def updateMaxRow(_):
        lastRowVar.set(wb[worksheetCombobox.get()].max_row)

    def closeWindow():
        # For now, just force close. Once main thread and GUI thread are separated, can go back to this.
        exit()
        # if currentState.get() == 102:
        #     exit()  # Force close
        # else:
        #     root.destroy()


    # style stuff
    fontType = "None"
    fontSize = 15
    fontGeneral = (fontType, fontSize)
    fontSmall = (fontType, int(fontSize/3*2))

    # root stuff
    root = tk.Tk()
    root.title("FileChop")
    rootWidth = 300
    rootHeight = 215
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

    # var stuff
    excelPathVar = tk.StringVar(value="~~~")
    inputColEntryVar = tk.StringVar(value="B")
    outputColEntryVar = tk.StringVar(value="E")
    firstRowVar = tk.IntVar(value=2)
    lastRowVar = tk.IntVar(value="")

    # data variables
    wb = None

    ## core UI elements stuff
    #
    browseButton = tk.Button(frame1, text="Browse to Select", command=selectExcel, font=fontGeneral, width=rootWidth)
    excelPathLabel = tk.Label(frame1, textvariable=excelPathVar, font=fontSmall, anchor="e")
    worksheetCombobox = ttk.Combobox(frame1, state="readonly")
    browseButton.pack()
    excelPathLabel.pack()
    worksheetCombobox.pack()

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

    # Bindings
    worksheetCombobox.bind("<<ComboboxSelected>>", updateMaxRow)
    root.protocol("WM_DELETE_WINDOW", closeWindow)

    root.mainloop()
