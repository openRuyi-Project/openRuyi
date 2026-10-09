# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pcidb
%define go_import_path  github.com/jaypipes/pcidb

Name:           go-github-jaypipes-pcidb
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for pcidb
License:        Apache-2.0
URL:            https://github.com/jaypipes/pcidb
VCS:            git:https://github.com/jaypipes/pcidb.git
#!RemoteAsset:  sha256:f66a46433a79839593905f73589c5051b6eac38d4ee1ed6e260e9290151d8084
Source0:        https://github.com/jaypipes/pcidb/archive/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n pcidb-1.0.0
# The sole test fetches the PCI ID database from the network; compile it in
# the offline build root without executing the network-dependent test.
BuildOption(check):  -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mitchellh/go-homedir)

Provides:       go(github.com/jaypipes/pcidb) = %{version}

Requires:       go(github.com/mitchellh/go-homedir)

%description
This package provides the github.com/jaypipes/pcidb Go module source.

%files
%doc README.md
%license COPYING
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
