# PhotoFilterer
A way to filter my pictures as I scroll through them into a different folder by the number on the picture only

## The Need
I use pCloud service for my picture taking and sorting. While using pCloud and copying a picture to a different file windows explorer would refresh to upload the file to the cloud and I would lose my spot in the browse.

This little code helps me choose a source and destination folders, use a text file to write the numbers of the pictures I like, and bulk copy and paste the exact pictures I choose, leading to a more seamless and fluid filtering process.

## How to use
1. Create a text file (in the same folder for ease of use)
2. Check the image extensions are correct and apply to your photos (the jpg and raw in this case)
3. Create a folder to have your filtered pictures in (if the path to it does not exist it will create the folder)
4. Set the source_address and destination to the relevant addresses
5. Put the name of the text file in place of the PicsNames.txt
6. Make sure the naming follows DSC_XXXX, otherwise change the "DSC_" in the for loop
7. Write all the numbers you want filtered in the text file, and save it once done
8. Run the program
9. Done
