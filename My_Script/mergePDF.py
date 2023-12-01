import PyPDF2

# 打开第一个PDF文件
with open('ml.pdf', 'rb') as file1:
    pdf1 = PyPDF2.PdfReader(file1)

    # 打开第二个PDF文件
    with open('merge.pdf', 'rb') as file2:
        pdf2 = PyPDF2.PdfReader(file2)

        # 创建一个新的PDF文件对象来存储合并后的内容
        pdf_output = PyPDF2.PdfWriter()

        # 复制第一个PDF文件的所有页面到新文件
        for page in pdf1.pages:
            pdf_output.add_page(page)

        # 复制第二个PDF文件的所有页面到新文件
        for page in pdf2.pages:
            pdf_output.add_page(page)

        # 创建一个新的PDF文件用于保存合并后的内容
        with open('merged.pdf', 'wb') as merged_file:
            pdf_output.write(merged_file)

print("PDF文件已成功合并为 merged.pdf")
