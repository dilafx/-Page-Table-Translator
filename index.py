import math

PAGE_SIZE = 1024        
MAX_PAGES = 8           
MAX_FRAMES = 6          

def main():
   
    page_table = [
        3,  
        -1, 
        0,  
        -1, 
        5,  
        2,  
        -1, 
        -1  
    ]


    logical_addresses = [100, 1050, 2500, 5000, 8500]
    
    

    print(f"{'--- Group A: Page Table Translator ---':^60}")
    print("-" * 75)
    print(f"{'Logical':<10} | {'Page#':<8} | {'Offset':<8} | {'Frame#':<8} | {'Physical':<10} | {'Status'}")
    print("-" * 75)

    for logical_addr in logical_addresses:
       
        page_number = logical_addr // PAGE_SIZE  
        offset = logical_addr % PAGE_SIZE        

        
        if page_number >= MAX_PAGES:
            print(f"{logical_addr:<10} | {'INVALID':<8} | {'-':<8} | {'-':<8} | {'-':<10} | Error: Out of Bounds")
            continue

      
        frame_number = page_table[page_number]

        if frame_number != -1:
           
            physical_addr = (frame_number * PAGE_SIZE) + offset
            status_msg = "Valid"
            print(f"{logical_addr:<10} | {page_number:<8} | {offset:<8} | {frame_number:<8} | {physical_addr:<10} | {status_msg}")
        else:
          
            status_msg = "Page Fault Occurred"
            print(f"{logical_addr:<10} | {page_number:<8} | {offset:<8} | {'-':<8} | {'-':<10} | {status_msg}")

if __name__ == "__main__":
    main()