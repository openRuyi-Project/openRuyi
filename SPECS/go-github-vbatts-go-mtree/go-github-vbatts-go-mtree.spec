# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-mtree
%define go_import_path  github.com/vbatts/go-mtree

Name:           go-github-vbatts-go-mtree
Version:        0.7.0
Release:        %autorelease
Summary:        File systems verification utility and library, in likeness of mtree(8)
License:        BSD-3-Clause
URL:            https://github.com/vbatts/go-mtree
#!RemoteAsset:  sha256:ba4687f1c9d4afc761a3f05af1267754a7e5e88965c9a1d2d8700579f5a6fa12
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/urfave/cli/v2)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/vbatts/go-mtree) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/urfave/cli/v2)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

# cmd/ builds a CLI and imports github.com/urfave/cli/v2, which is not packaged yet.
%prep -a
rm -rf cmd

%description
mtree is a filesystem hierarchy validation tooling and format.
This is a library and simple cli tool for mtree(8) support.

While the traditional mtree cli utility is primarily on BSDs
(FreeBSD, openBSD, etc), even broader support for the mtree
specification format is provided with libarchive (libarchive-formats(5)).

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
