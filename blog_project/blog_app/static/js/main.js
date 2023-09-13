// 전체 포스트 목록
async function getPosts() {
    let response = await fetch("http://127.0.0.1:8000/api/posts/");
    let postListData = await response.json();
    return postListData;
  }

// author_id별 포스트 목록

// topic별 포스트 목록(필터링)

// html에 쏴주기
// 조회수 정렬