# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           optional
%define go_import_path  github.com/antihax/optional

Name:           go-github-antihax-optional
Version:        1.0.0
Release:        %autorelease
Summary:        optional parameters for go
License:        MIT
URL:            https://github.com/antihax/optional
#!RemoteAsset
Source0:        https://github.com/antihax/optional/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/antihax/optional) = %{version}

%description
optional parameters for go

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
