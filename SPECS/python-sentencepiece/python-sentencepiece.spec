# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentencepiece

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        Unsupervised text tokenizer and detokenizer
License:        Apache-2.0
URL:            https://github.com/google/sentencepiece
#!RemoteAsset:  sha256:8138cec27c2f2282f4a34d9a016e3374cd40e5c6e9cb335063db66a0a3b71fad
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  cmake
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(protobuf)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SentencePiece is an unsupervised text tokenizer and detokenizer mainly for
Neural Network-based text generation systems. SentencePiece implements
subword units (e.g., byte-pair-encoding (BPE) and unigram language model)
with the extension of direct training from raw sentences. This package
bundles the SentencePiece C++ library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
