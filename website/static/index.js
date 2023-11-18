function deleteNote(noteId) {
    fetch('/delete-note', {
        // will take noteID that we pass & it will send POST request to delete note end point
        method: "POST", 
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        // after getting response from delete note end point, it will reload the window aka redirect us to homepage
        window.location.href = "/";
    });
}