# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gomega
%define go_import_path  github.com/bsm/gomega

Name:           go-github-bsm-gomega
Version:        1.27.10
Release:        %autorelease
Summary:        Straight copy of the excellent Gomega library, stripped to the bare core to be free of third-party dependencies
License:        MIT
URL:            https://github.com/bsm/gomega
#!RemoteAsset
Source0:        https://github.com/bsm/gomega/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bsm/gomega) = %{version}

%description
This is a straight copy of the excellent Gomega
library, stripped to the bare core to be
free of third-party dependencies.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
