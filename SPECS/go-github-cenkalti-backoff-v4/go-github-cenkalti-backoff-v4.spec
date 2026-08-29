# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backoff
%define go_import_path  github.com/cenkalti/backoff/v4

Name:           go-github-cenkalti-backoff-v4
Version:        4.3.0
Release:        %autorelease
Summary:        Exponential backoff algorithm for Go
License:        MIT
URL:            https://github.com/cenkalti/backoff
#!RemoteAsset:  sha256:5006d8626ff22ad2c584b0ab09b6f20f8013b46467381519b80f9c037ad8c2b0
Source0:        https://github.com/cenkalti/backoff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Associate the context example with the exported function it demonstrates.
Patch2000:      2000-examples-associate-context-example-with-WithContext.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cenkalti/backoff/v4) = %{version}

%description
Backoff implements retry operations with configurable exponential delays and
elapsed-time limits.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
