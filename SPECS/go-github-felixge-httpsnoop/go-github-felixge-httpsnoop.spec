# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpsnoop
%define go_import_path  github.com/felixge/httpsnoop

Name:           go-github-felixge-httpsnoop
Version:        1.0.4
Release:        %autorelease
Summary:        Capture HTTP response metrics from Go handlers
License:        MIT
URL:            https://github.com/felixge/httpsnoop
#!RemoteAsset:  sha256:ffb63ba081e4c2360342dea2079d08b8560c315b2f458885fd34639786a1aa3d
Source0:        https://github.com/felixge/httpsnoop/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/felixge/httpsnoop) = %{version}

%description
This package provides helpers to capture HTTP status, response size, and
timing metrics from Go http.Handler implementations.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
