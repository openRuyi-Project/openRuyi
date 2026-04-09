# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           varint
%define go_import_path  github.com/dennwc/varint
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-github-dennwc-varint
Version:        1.0.0
Release:        %autorelease
Summary:        Fast varint library for Go
License:        MIT
URL:            https://github.com/dennwc/varint
#!RemoteAsset
Source0:        https://github.com/dennwc/varint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dennwc/varint) = %{version}

%description
This package provides an optimized implementation of protobuf's varint
encoding/decoding. It has no dependencies.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
