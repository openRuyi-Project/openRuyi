# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rapid
%define go_import_path  pgregory.net/rapid

Name:           go-pgregory-rapid
Version:        1.3.0
Release:        %autorelease
Summary:        Property-based testing library for Go
License:        MPL-2.0
URL:            https://github.com/flyingmutant/rapid
#!RemoteAsset:  sha256:205a612d771db6c156a729d159ce6e07ff80a03537b900c8163301e414ad2f17
Source0:        https://github.com/flyingmutant/rapid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(pgregory.net/rapid) = %{version}

%description
Rapid is a property-based testing library that generates diverse test data and
automatically minimizes failing cases.

%check -p
# Go 1.26 synctest requires the modern asynchronous timer channel behavior.
export GODEBUG=asynctimerchan=0

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
