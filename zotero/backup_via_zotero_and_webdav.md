##  Built-in Backup References and Files with Zotero and WebDAV
Zotero has built-in functionality for backing up your references.
They provide a service for backing up 300MB of files for free.
If you backup full-text content (e.g. PDFs) this is easily surpassed.
However, they also provide the use of backing up files to a WebDAV.
The references will be stored in Zotero's backup service while the files are stored in the WebDAV.
Using a free service that provides the use of a WebDAV, such as box.com, allows for free remote storage of references and file content for ease of syncing up your library across multiple local Zotero libraries.
When using Zotero's service for reference and box.com's WebDAV and free account, you get 300MB of references and 10GB of files for free remote storage.

### The steps are:
1. Obtain a box.com account
2. Obtain a zotero.org account
3. Open local Zotero application
4. Go to Preferences via: Edit -> Preferences -> Sync
5. Under "Data Syncing", link your Zotero account
    - keep both "Sync automatically" and "Sync full-text content" checked, as they are by default.
6. Under File Syncing add the following into the URL: https://dav.box.com/dav
7. Add your box.com username and password and click "Verify Server"
    - A pop-up window may appear requesting to create a "zotero/" directory within your storage linked with WebDAV.
    - You may adjust the remaining settings in "File Syncing" as you see fit, leaving the defaults are fine.

Doing this with your local Zotero libraries will now sync them across machines and have file content as well.


#### Notes
You may use any WebDAV service you have available to you, including one you setup yourself or by your institution, given the username and password are all that are needed to access the WebDAV.

If you have pre-existing content in your Zotero account's remote library that is different from your local machine, you will have to manually move around the files to sync them appropriately.
Given this, I recommend doing this once where you have all the files and organization you want established on one local machine and sync those files to an empty Zotero remote library.
Then simply empty all other Zotero accounts and sync them to the library and they will download the library.

This is not the greatest solution, but given it is free and built-in it is good for starting out and unlikely that you will surpass the Zotero 300MB storage with references only.
Anecdote: A friend has over 1000 references with files in his library and still has space.

### References
- Zotero Syncing: https://www.zotero.org/support/sync
- Box WebDAV: https://support.box.com/hc/en-us/articles/360043696414-WebDAV-with-Box
