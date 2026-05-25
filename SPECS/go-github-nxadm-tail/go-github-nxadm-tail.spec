# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tail
%define go_import_path  github.com/nxadm/tail

Name:           go-github-nxadm-tail
Version:        1.4.11
Release:        %autorelease
Summary:        Go package for reading from continuously updated files
License:        MIT
URL:            https://github.com/nxadm/tail
#!RemoteAsset:  sha256:f20a022655bb5acdb364382418d0481f938e761be7d4233af61b0d4659ae1812
Source0:        https://github.com/nxadm/tail/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstreamable Go 1.25 vet fix for non-constant fmt.Printf calls in examples.
# - HNO3Miracle
Patch2000:         2000-fix-example-non-constant-fmt-printf.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/tomb.v1)

Provides:       go(github.com/nxadm/tail) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/tomb.v1)

%description
nxadm/tail provides a Go library that emulates BSD tail -f behavior.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
