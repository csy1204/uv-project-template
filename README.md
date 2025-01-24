



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


## Application (기본값)

- `uv init` 또는 `uv init --app`으로 생성
- 웹 서버, 스크립트, CLI 인터페이스에 적합한 기본 구조
- 생성되는 파일:
  - pyproject.toml
  - hello.py
  - README.md
  - .python-version

## Library

- `uv init --lib`으로 생성
- 다른 프로젝트에서 임포트하여 사용할 수 있는 라이브러리 개발용
- src 디렉토리 구조를 사용하며 __init__.py 파일 포함

## Package Application

- `uv init --package`로 생성
- PyPI에 배포하거나 테스트 디렉토리가 필요한 애플리케이션에 적합
- src 디렉토리 구조를 사용하며 모듈 디렉토리와 __init__.py 포함

## 비교표

| 구분 | Application | Library | Package Application |
|------|------------|---------|-------------------|
| 용도 | 웹서버, 스크립트, CLI | 재사용 가능한 라이브러리 | PyPI 배포용 애플리케이션 |
| 구조 | 플랫 구조 | src/ 구조 | src/ 구조 |
| 빌드시스템 | 없음 | 있음 | 있음 |
| 설치 필요성 | 환경에 설치 안됨 | 환경에 설치됨 | 환경에 설치됨 |
| 주요 특징 | 간단한 구조 | 타입 힌팅 지원 | 패키징과 배포 용이 |

</details>


## Set venv and Installing dev dependency

```sh
uv venv
uv add --dev mkdocs-material pytest pre-commit ruff pytest-cov "mkdocstrings[python]"
```

