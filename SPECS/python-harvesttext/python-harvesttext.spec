# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname harvesttext

Name:           python-%{srcname}
Version:        0.8.2.1
Release:        %autorelease
Summary:        A toolkit for text mining and preprocessing
License:        MIT
URL:            https://github.com/blmoistawinde/HarvestText
#!RemoteAsset:  sha256:621bcfa334f17d5c5daf3408595506a7c224e7246c38d6742b5e927e6e9c846f
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
# The tarball from PyPI does not have requirements.txt.
#!RemoteAsset:  sha256:9ec4dd25ddefcfc5d764e7849d10a2b6c2ff22443d21bd6d6f5af3363862154a
Source1:        https://raw.githubusercontent.com/blmoistawinde/HarvestText/ba9b3d22492277c3dcdf3dc8060394e3713a5073/requirements.txt
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(jieba)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pypinyin)
BuildRequires:  python3dist(rdflib)
BuildRequires:  python3dist(python-louvain)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(w3lib)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(opencc-python-reimplemented)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HarvestText is a Python toolkit for text mining and preprocessing. It
focuses on weakly supervised methods that integrate domain knowledge
(such as types and aliases) for simple and efficient domain-specific
text processing and analysis, including entity linking, sentiment
analysis, keyword extraction, relation networks, text summarization,
and new word discovery.

%prep
%autosetup -n %{srcname}-%{version}
cp %{S:1} .

# %%pyproject_buildrequires does not work with this package.
%generate_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
