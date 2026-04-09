# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopickle
%define go_import_path  github.com/nlpodyssey/gopickle

Name:           go-github-nlpodyssey-gopickle
Version:        0.3.0
Release:        %autorelease
Summary:        Go library for loading Python's data serialized with pickle and PyTorch module files.
License:        BSD-2-Clause
URL:            https://github.com/nlpodyssey/gopickle
#!RemoteAsset
Source0:        https://github.com/nlpodyssey/gopickle/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/nlpodyssey/gopickle) = %{version}

Requires:       go(golang.org/x/text)

%description
GoPickle is a Go library for loading Python's data serialized with
pickle and PyTorch module files.

The pickle sub-package provides the core functionality for loading data
serialized with Python pickle module, from a file, string, or byte
sequence. All *pickle* protocols from 0 to 5 are supported.

The pytorch sub-package implements types and functions for loading
PyTorch module files. Both the *modern* zip-compressed format and the
*legacy* non-tar format are supported. Legacy tar-compressed files and
TorchScript archives are *not* supported.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
