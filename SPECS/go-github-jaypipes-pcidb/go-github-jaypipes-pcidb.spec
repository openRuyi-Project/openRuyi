# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pcidb
%define go_import_path  github.com/jaypipes/pcidb

Name:           go-github-jaypipes-pcidb
Version:        1.0.0
Release:        %autorelease
Summary:        PCI vendor, device and class database for Go
License:        Apache-2.0
URL:            https://github.com/jaypipes/pcidb
#!RemoteAsset:  sha256:f66a46433a79839593905f73589c5051b6eac38d4ee1ed6e260e9290151d8084
Source0:        https://github.com/jaypipes/pcidb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  hwdata
BuildRequires:  go(github.com/mitchellh/go-homedir)

Provides:       go(github.com/jaypipes/pcidb) = %{version}

Requires:       go(github.com/mitchellh/go-homedir)

%description
PCI vendor, device and class database for Go.

%files
%doc README.md
%license LICENSE COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
