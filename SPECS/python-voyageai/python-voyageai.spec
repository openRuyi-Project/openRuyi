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
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
# Remove langchain-text-splitters and ffmpeg-python deps to avoid deep dependency chains
Patch0:         0001-remove-langchain-and-ffmpeg-deps.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  voyageai

BuildRequires:  python3-devel
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
BuildRequires:  python3dist(langchain-text-splitters)
BuildRequires:  python3dist(ffmpeg-python)

Provides:       python3-%{srcname}
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
%{?autochangelog}
