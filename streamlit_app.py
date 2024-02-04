import streamlit as st
import pandas as pd
import base64

def main():
    st.title("Excel File Manipulation")

    # File Uploader for File A
    file_a = st.file_uploader("Upload File A (XLSX)", type=["xlsx"])
    
    # File Uploader for File B
    file_b = st.file_uploader("Upload File B (XLSX)", type=["xlsx"])

    if file_a and file_b:
        st.write("File A and File B are uploaded.")
        
        # Read the data from File A
        df_a_c = pd.read_excel(file_a, sheet_name='orang')
        df_a_d = pd.read_excel(file_a, sheet_name='kota')

        # Create new sheet names for File B
        sheet_orang_name = 'file_a_sheet_orang'
        sheet_kota_name = 'file_a_sheet_kota'

        # Write to File B with new sheet names
        with pd.ExcelWriter(file_b, engine='openpyxl', mode='a') as writer:
            df_a_c.to_excel(writer, sheet_name=sheet_orang_name, index=False)
            df_a_d.to_excel(writer, sheet_name=sheet_kota_name, index=False)

        st.success(f"Sheet C and Sheet D from File A are copied to {file_b.name} as {sheet_orang_name} and {sheet_kota_name}.")

        # Provide a button to download the updated File B
        download_button(file_b, "Download Updated File B")

def download_button(object_to_download, download_button_text, key="newFileB"):
    """Generates a download button for the given object."""
    download_obj = object_to_download.getvalue()
    b64 = base64.b64encode(download_obj).decode()
    href = f'<a href="data:file/xlsx;base64,{b64}" download="{key}.xlsx">{download_button_text}</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
