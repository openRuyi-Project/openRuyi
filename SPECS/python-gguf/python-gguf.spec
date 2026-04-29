# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gguf

Name:           python-%{srcname}
Version:        0.18.0
Release:        %autorelease
Summary:        Read and write ML models in GGUF for GGML
License:        MIT
URL:            https://ggml.ai
VCS:            git:https://github.com/ggml-org/llama.cpp.git
#!RemoteAsset:  sha256:b4659093d5d0dccdb5902a904d54b327f4052879fe5e90946ad5fce9f8018c2e
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
BuildOption(check):  -e gguf.scripts.gguf_editor_gui
BuildOption(check):  gguf

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python library to read and write GGUF model files for GGML ecosystems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/gguf-convert-endian
%{_bindir}/gguf-dump
%{_bindir}/gguf-set-metadata
%{_bindir}/gguf-new-metadata
%{_bindir}/gguf-editor-gui

%changelog
%autochangelog
