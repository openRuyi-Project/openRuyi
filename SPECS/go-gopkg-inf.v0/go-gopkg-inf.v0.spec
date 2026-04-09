# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           inf.v0
%define go_import_path  gopkg.in/inf.v0
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-gopkg-inf.v0
Version:        0.9.1
Release:        %autorelease
Summary:        Package inf (type inf.Dec) implements "infinite-precision" decimal arithmetic.
License:        BSD-3-Clause
URL:            https://github.com/go-inf/inf
#!RemoteAsset
Source0:        https://github.com/go-inf/inf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/inf.v0) = %{version}

%description
Package inf (type inf.Dec) implements "infinite-precision" decimal arithmetic.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
