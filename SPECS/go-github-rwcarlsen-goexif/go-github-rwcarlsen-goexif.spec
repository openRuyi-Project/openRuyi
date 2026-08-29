# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goexif
%define go_import_path  github.com/rwcarlsen/goexif
%define commit_id 9e8deecbddbd4989a3e8d003684b783412b41e7a

Name:           go-github-rwcarlsen-goexif
Version:        0+git20260717.9e8deec
Release:        %autorelease
Summary:        Provides decoding of basic exif and tiff encoded data
License:        BSD-2-Clause
URL:            https://github.com/rwcarlsen/goexif
#!RemoteAsset:  sha256:7d343e1967bf9739dc5734c3ba232fb61c35bf68436a948e1b42c70791ea95b2
Source0:        https://github.com/rwcarlsen/goexif/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rwcarlsen/goexif) = %{version}

%description
Provides decoding of basic exif and tiff encoded data. Still in alpha -
no guarantees. Suggestions and pull requests are welcome.  Functionality
is split into two packages - "exif" and "tiff" The exif package depends
on the tiff package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
