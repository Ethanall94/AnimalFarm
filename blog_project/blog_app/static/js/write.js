function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ')
            c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return '';
}

document.addEventListener('DOMContentLoaded', (event) => {
    // AI 글 자동완성
    document.getElementById('aiAutocompleteButton').addEventListener('click', function () {
        document.getElementById('loading-animation').style.display = 'block';
        document.getElementById('ai-img').style.display = 'none';

        // Django 폼에서 가져온 값을 사용
        let id_title = document.getElementById('id_title');
        let title = id_title.value;

        let csrf_token = getCookie('csrftoken');
        console.log(csrf_token);

        fetch('/autocomplete/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrf_token,
            },
            body: new URLSearchParams({
                'title': title
            })
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('loading-animation').style.display = 'none';
                document.getElementById('ai-img').style.display = 'block';

                // 기존 내용에 자동완성된 내용 추가
                let iframe = document.querySelector('iframe');
                let summer = iframe.contentWindow.document.querySelectorAll('.note-editable')[0];

                data.message = data.message.replace(/\n/g, '<br>');
                let temp = '';
                let dList = data.message.split('\n');
                console.log(dList);
                for (let text of dList) {
                    temp += `<p>${text}</p>`;
                }
                console.log(temp);
                summer.innerHTML += temp;
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('loading-animation').style.display = 'none';
            });
    });
});
