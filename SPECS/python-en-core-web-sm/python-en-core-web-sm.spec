# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname en_core_web_sm

Name:           python-en-core-web-sm
Version:        3.8.0
Release:        %autorelease
Summary:        English pipeline optimized for CPU (spaCy language model)
License:        MIT
URL:            https://spacy.io/models/en#en_core_web_sm
VCS:            git:https://github.com/explosion/spacy-models
# PyPI source not available for this version, using GitHub release
#!RemoteAsset:  sha256:14a2f31bc476af87019819ea8c9948fabdfd473a442edd6b1cba62bf0c2c0f55
Source0:        https://github.com/explosion/spacy-models/releases/download/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(spacy) >= 3.8.0

Provides:       python3-en-core-web-sm = %{version}-%{release}
%python_provide python3-en-core-web-sm

Requires:       python3dist(spacy) >= 3.8.0

%description
English pipeline optimized for CPU. Components: tok2vec, tagger, parser,
senter, ner, attribute_ruler, lemmatizer.

This is a spaCy language model for English, trained on OntoNotes 5 corpus.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md LICENSES_SOURCES
%license LICENSE

%changelog
%autochangelog
