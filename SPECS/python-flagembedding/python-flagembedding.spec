# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flagembedding
%global pypi_name flagembedding

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        BGE one-stop retrieval toolkit for search and RAG
License:        MIT
URL:            https://github.com/FlagOpen/FlagEmbedding
#!RemoteAsset:  sha256:2079c14ecf0341d64519785e53c0401122a752e5b6a0ac497f23c02f0d21b3b9
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  FlagEmbedding
# evaluation.* needs faiss (no sdist on PyPI) and pytrec_eval (needs
# trec_eval C library) which are difficult to package.
# gemma_model fails: transformers 5.2.0 dropped GEMMA2_START_DOCSTRING.
BuildOption(check):  -e 'FlagEmbedding.evaluation' -e 'FlagEmbedding.evaluation.*' -e 'FlagEmbedding.abc.evaluation' -e 'FlagEmbedding.abc.evaluation.*' -e 'FlagEmbedding.inference.reranker.decoder_only.models.gemma_model'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(accelerate)
BuildRequires:  python3dist(sentence-transformers)
BuildRequires:  python3dist(peft)
BuildRequires:  python3dist(ir-datasets)
BuildRequires:  python3dist(sentencepiece)
BuildRequires:  python3dist(protobuf)
# Needed by top-level imports from FlagEmbedding.__init__
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(packaging)

Provides:       python3-%{srcname}= %{version}-%{release}
%python_provide python3-%{srcname}

%description
FlagEmbedding provides BGE embedding and reranking utilities for search and
retrieval-augmented generation workflows.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
