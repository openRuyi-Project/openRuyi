# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname openai

Name:           python-%{srcname}
Version:        2.40.0
Release:        %autorelease
Summary:        The official Python library for the OpenAI API
License:        Apache-2.0
URL:            https://github.com/openai/openai-python
#!RemoteAsset:  sha256:9a756f91f274a24ad6026cbcb2042fd356c8d4a10e8f347b08d34465e585f7a2
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jiter)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(sniffio)
BuildRequires:  python3dist(sounddevice)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
openai is the official Python SDK for accessing OpenAI APIs, with both
synchronous and asynchronous clients.

%prep -a
# Upstream pins the build backend to hatchling==1.26.3. The distro build uses
# the packaged hatchling, so relax this before dependencies are calculated.
sed -i 's/hatchling==1.26.3/hatchling>=1.26.3/' pyproject.toml

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
