# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentence-transformers
%global pypi_name sentence_transformers

Name:           python-%{srcname}
Version:        6.2.0
Release:        %autorelease
Summary:        Embeddings, Retrieval, and Reranking
License:        Apache-2.0
URL:            https://www.sbert.net
#!RemoteAsset:  sha256:1e3cd8796ab7bcad4cfa2f51e2083d8b37b15d6b68e6fa6b91a147c67380574d
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  sentence_transformers

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(huggingface-hub)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sentence Transformers is a Python library for state-of-the-art sentence, text,
and image embeddings. It can be used to compute embeddings for sentences and
paragraphs, and to find semantically similar sentences using cosine similarity.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license NOTICE.txt

%changelog
%autochangelog
