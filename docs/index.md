
## Installing uv

- 사용자 환경에 맞게 [공식 문서](https://docs.astral.sh/uv/getting-started/installation/)에 따라 설치해주세요
- Mac의 경우 아래처럼 한 후 shell을 재시작하면 됐습니다.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

## Installing Python

- `uv python install 3.11`
- `uv python pin 3.11`

## Creating Projects

- `uv init`으로 하는데 app, package, lib 3가지 형태가 있어 아래 설명을 참고하여 설정하면 좋음
- 간단한건 app, 엔터프라이즈급의 큰 규모는 pacakges로 가는게 좋아보임

<details>
<summary>uv의 3가지 init 형식에 대한 설명</summary>

<h2> Application (기본값) </h2>
<ul>
<li><code>uv init</code> 또는 <code>uv init --app</code>으로 생성</li>
<li>웹 서버, 스크립트, CLI 인터페이스에 적합한 기본 구조</li>
<li>생성되는 파일:<ul>
<li>pyproject.toml</li>
<li>hello.py</li>
<li>README.md</li>
<li>.python-version</li>
</ul>
</li>
</ul>
<h2 id="library">Library</h2>
<ul>
<li><code>uv init --lib</code>으로 생성</li>
<li>다른 프로젝트에서 임포트하여 사용할 수 있는 라이브러리 개발용</li>
<li>src 디렉토리 구조를 사용하며 <strong>init</strong>.py 파일 포함</li>
</ul>
<h2 id="package-application">Package Application</h2>
<ul>
<li><code>uv init --package</code>로 생성</li>
<li>PyPI에 배포하거나 테스트 디렉토리가 필요한 애플리케이션에 적합</li>
<li>src 디렉토리 구조를 사용하며 모듈 디렉토리와 <strong>init</strong>.py 포함</li>
</ul>
<h2 id="-">비교표</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>Application</th>
<th>Library</th>
<th>Package Application</th>
</tr>
</thead>
<tbody>
<tr>
<td>용도</td>
<td>웹서버, 스크립트, CLI</td>
<td>재사용 가능한 라이브러리</td>
<td>PyPI 배포용 애플리케이션</td>
</tr>
<tr>
<td>구조</td>
<td>플랫 구조</td>
<td>src/ 구조</td>
<td>src/ 구조</td>
</tr>
<tr>
<td>빌드시스템</td>
<td>없음</td>
<td>있음</td>
<td>있음</td>
</tr>
<tr>
<td>설치 필요성</td>
<td>환경에 설치 안됨</td>
<td>환경에 설치됨</td>
<td>환경에 설치됨</td>
</tr>
<tr>
<td>주요 특징</td>
<td>간단한 구조</td>
<td>타입 힌팅 지원</td>
<td>패키징과 배포 용이</td>
</tr>
</tbody>
</table>

</details>

## Set venv and Installing dev dependency

```sh
uv venv
uv add --dev mkdocs-material pytest pre-commit ruff pytest-cov "mkdocstrings[python]"
```
