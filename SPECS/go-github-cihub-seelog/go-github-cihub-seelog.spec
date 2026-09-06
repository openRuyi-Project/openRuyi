# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           seelog
%define go_import_path  github.com/cihub/seelog

Name:           go-github-cihub-seelog
Version:        2.6
Release:        %autorelease
Summary:        Logging library for Go
License:        BSD-3-Clause
URL:            https://github.com/cihub/seelog
#!RemoteAsset:  sha256:68ed377a2eba7a1558987bc1e52677295b4e703ecfc3a00708c2f68c4cb28354
Source0:        https://github.com/cihub/seelog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch1000:      1000-fix-xml-syntax-error-with-go1.6.patch
Patch1001:      1001-remove-racy-test.patch
Patch2000:      2000-support-current-go-tooling.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cihub/seelog) = %{version}

%description
Seelog is a Go logging library with configurable asynchronous dispatching,
filtering, and formatting.

%files
%doc README.markdown
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
