# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-rpmutils
%define go_import_path  github.com/sassoftware/go-rpmutils

Name:           go-github-sassoftware-go-rpmutils
Version:        0.4.0
Release:        %autorelease
Summary:        Golang implementation of parsing RPM packages
License:        Apache-2.0
URL:            https://github.com/sassoftware/go-rpmutils
#!RemoteAsset:  sha256:8a9000fcddb16b3d012f843bd3a41a2ff94da96018377c2b0db289f5b2146a8a
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/ulikunitz/xz)
BuildRequires:  go(github.com/xi2/xz)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/sassoftware/go-rpmutils) = %{version}

Requires:       go(github.com/DataDog/zstd)
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/ulikunitz/xz)
Requires:       go(github.com/xi2/xz)
Requires:       go(golang.org/x/sys)

%description
go-rpmutils is a library written in go for parsing and extracting content from RPMs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
