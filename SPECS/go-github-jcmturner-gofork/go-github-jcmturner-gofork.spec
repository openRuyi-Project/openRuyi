# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofork
%define go_import_path  github.com/jcmturner/gofork

Name:           go-github-jcmturner-gofork
Version:        1.7.6
Release:        %autorelease
Summary:        Forked Go standard-library packages
License:        BSD-3-Clause
URL:            https://github.com/jcmturner/gofork
#!RemoteAsset:  sha256:cce7c28e3a854b52a8c3b596caefd1e37fa490f0e4d7f634bac91838b201907c
Source0:        https://github.com/jcmturner/gofork/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jcmturner/gofork) = %{version}

%description
Gofork contains compatibility forks of Go standard-library packages used by
the jcmturner Kerberos libraries.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
