# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastprinter
%define go_import_path  github.com/CloudyKit/fastprinter
%define commit_id 1725d2651bd4cd68eeedef7e5a3e98a2954a9e99

Name:           go-github-cloudykit-fastprinter
Version:        0+git20251202.1725d26
Release:        %autorelease
Summary:        FastPrinter supports write values in io.Writer without allocation
License:        MIT
URL:            https://github.com/CloudyKit/fastprinter
#!RemoteAsset
Source0:        https://github.com/CloudyKit/fastprinter/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/CloudyKit/fastprinter) = %{version}

%description
FastPrinter supports write values in io.Writer without allocation

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
