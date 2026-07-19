# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           licensecheck
%define go_import_path  github.com/google/licensecheck

Name:           go-github-google-licensecheck
Version:        0.3.1
Release:        %autorelease
Summary:        The licensecheck package classifies license files and heuristically determines how well they correspond to known open source licenses.
License:        BSD-3-Clause
URL:            https://github.com/google/licensecheck
#!RemoteAsset:  sha256:9f2bd0b68cee1f4bfb0cf3143575a2a78bd045a1493354e41d52da8c5a79cfb0
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/licensecheck) = %{version}

%description
The licensecheck package scans source texts for known licenses.
The design aims never to give a false positive. It also reports
matches of known license URLs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
