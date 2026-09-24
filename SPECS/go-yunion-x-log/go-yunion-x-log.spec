# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  yunion.io/x/log
%define commit_id       7cf2d6cd5a9127474da7a072880b5e38b14dfa7f

Name:           go-yunion-x-log
Version:        0+git20260922.7cf2d6c
Release:        %autorelease
Summary:        Yunion logging library for Go
License:        Apache-2.0
URL:            https://github.com/yunionio/log
#!RemoteAsset:  sha256:7cecb7abf5b6689f721a444659a80efa36de72525d8734496dd63b9e9b710594
Source0:        https://github.com/yunionio/log/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects the non-constant format string in hooks/stdio.go.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mgutz/ansi)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(yunion.io/x/log) = %{version}

Requires:       go(github.com/mgutz/ansi)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/crypto)

%description
This package provides a logrus wrapper with colored output, verbosity
levels, caller information and rotating file hooks.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
