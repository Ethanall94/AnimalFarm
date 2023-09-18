// AI 글 자동완성
document.getElementsByClassName('aiCompletion')[0].addEventListener('click', function () {
    document.getElementById('loading-animation').style.display = 'block';
    document.getElementById('ai-img').style.display = 'none';
    let contentTitle = document.getElementById('contentTitle').textContent;
    fetch('/autocomplete/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: new URLSearchParams({
            'contentTitle': contentTitle
        })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading-animation').style.display = 'none';
            document.getElementById('ai-img').style.display = 'block';

            // 기존 내용에 자동완성 된 내용 추가
            let currentContent = summernote.activeEditor.getContent();
            data.message = data.message.replace(/\n/g, '<br>');
            summernote.activeEditor.setContent(currentContent + data.message);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loading-animation').style.display = 'none';
        });
});

