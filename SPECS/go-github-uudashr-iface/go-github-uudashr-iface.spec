# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iface
%define go_import_path  github.com/uudashr/iface

Name:           go-github-uudashr-iface
Version:        1.5.3
Release:        %autorelease
Summary:        Provides analyzers designed to identify the incorrect use of interfaces, helping developers avoid interface pollution
License:        Apache-2.0
URL:            https://github.com/uudashr/iface
#!RemoteAsset:  sha256:1e4e1b5f49e92a8f149811c0363f268edc4e3a199083b153e2082140f05ccca0
Source0:        https://github.com/uudashr/iface/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/uudashr/iface) = %{version}
Provides:       go(github.com/uudashr/iface/identical) = %{version}
Provides:       go(github.com/uudashr/iface/internal/directive) = %{version}
Provides:       go(github.com/uudashr/iface/opaque) = %{version}
Provides:       go(github.com/uudashr/iface/unexported) = %{version}
Provides:       go(github.com/uudashr/iface/unused) = %{version}
Provides:       go(github.com/uudashr/iface/unusedmethod) = %{version}

Requires:       go(golang.org/x/tools)

%description
Provides analyzers designed to identify the incorrect use of interfaces, helping developers avoid interface pollution.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n iface-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/uudashr/iface

%changelog
%autochangelog
