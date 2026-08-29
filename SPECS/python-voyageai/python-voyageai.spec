# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname voyageai

Name:           python-%{srcname}
Version:        0.3.7
Release:        %autorelease
Summary:        The official Python client for the Voyage AI API
License:        MIT
URL:            https://www.voyageai.com
#!RemoteAsset:  sha256:826cd97f97223f42b5babc5c459c9c80f3a8215ce5c0e007b0b276550f790d24
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Remove langchain-text-splitters and ffmpeg-python deps to avoid deep dependency chains
Patch2000:      2000-remove-langchain-and-ffmpeg-deps.patch

BuildOption(install):  voyageai

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(tenacity)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(aiolimiter)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(tokenizers)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The official Python client for Voyage AI, providing access to cutting-edge
embedding models and rerankers for retrieval-augmented generation (RAG) and
other AI applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
