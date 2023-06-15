// // window.addEventListener('load', (event) => {
    // Get search form and page links
    var searchForm = document.getElementById('searchForm')
    // console.log(searchForm)
    var pageLinks = document.getElementsByClassName('page-link')
    // console.log(pageLinks)

    // Ensure search form exists
    if (searchForm) {
        for (let i = 0; pageLinks.length > i; i++) {
            pageLinks[i].addEventListener('click', function (e) {
                e.preventDefault()

                //Get the data attribute
                let page = this.dataset.page

                //Add hidden search input to form
                searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

                //Submit form
                searchForm.submit()
            })
        }
    }

// // })
