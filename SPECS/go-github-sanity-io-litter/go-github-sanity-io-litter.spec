# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           litter
%define go_import_path  github.com/sanity-io/litter

Name:           go-github-sanity-io-litter
Version:        1.5.8
Release:        %autorelease
Summary:        Litter is a pretty printer library for Go data structures to aid in debugging and testing.
License:        MIT
URL:            https://github.com/sanity-io/litter
#!RemoteAsset:  sha256:aac38660151419c627d8e3d35f67f6d343f41a0b5b3566c8685ed8ad245384bc
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/sanity-io/litter) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)

%description
Litter is a pretty printer library for Go data structures to aid in debugging and testing.

Litter named for the fact that it outputs literals, which you litter your output with. As
a side benefit, all Litter output is syntactically correct Go. You can use Litter to emit
data during debug, and it's also really nice for "snapshot data" in unit tests, since it
produces consistent, sorted output. Litter was inspired by Spew, but focuses on terseness
and readability.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
