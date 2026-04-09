# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mem
%define go_import_path  aead.dev/mem

Name:           go-aead-dev-mem
Version:        0.2.0
Release:        %autorelease
Summary:        The mem package provides types and functions for measuring and displaying memory throughput and capacity.
License:        MIT
URL:            https://github.com/aead/mem
#!RemoteAsset
Source0:        https://github.com/aead/mem/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(aead.dev/mem) = %{version}

%description
The mem package provides types and functions for measuring and
displaying memory throughput and capacity.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
