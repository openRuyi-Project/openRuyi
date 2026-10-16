# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goutils
%define go_import_path  github.com/aokoli/goutils

Name:           go-github-aokoli-goutils
Version:        1.0.1
Release:        %autorelease
Summary:        String manipulation helpers for Go
License:        Apache-2.0
URL:            https://github.com/aokoli/goutils
#!RemoteAsset:  sha256:43793e2b7a23a765769312dd11f01eb989e977510896f53b913c8564ef0d92bf
Source0:        https://github.com/aokoli/goutils/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The old string conversion and example naming trigger current Go vet checks.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aokoli/goutils) = %{version}

%description
GoUtils provides helpers for random strings, word wrapping, and other
string operations. Cloudmux uses its string utilities.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
