# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sacrebleu

Name:           python-%{srcname}
Version:        2.6.0
Release:        %autorelease
Summary:        Hassle-free computation of shareable, comparable, and reproducible BLEU, chrF, and TER scores
License:        Apache-2.0
URL:            https://github.com/mjpost/sacrebleu
#!RemoteAsset:  sha256:91499b6cd46138d95154fff1e863c2f9be57e82f0c719d8dd718d0006cf6c566
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SacreBLEU (Post, 2018) provides hassle-free computation of
shareable, comparable, and reproducible BLEU scores. Inspired
by Rico Sennrich's multi-bleu-detok.perl, it produces the official
WMT scores but works with plain text. It also knows all the standard
test sets and handles downloading, processing, and tokenization for you.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/sacrebleu

%changelog
%autochangelog
