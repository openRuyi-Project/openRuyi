# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testing
%define go_import_path  github.com/golangplus/testing
%define commit_id       56d225dfade1dd7ba5ff9850e80c2c5a7595082e
%define bytes_commit    45c989fe545070ef7c9003cf1998bb195c61731a

Name:           go-github-golangplus-testing
Version:        0+git20260922.56d225d
Release:        %autorelease
Summary:        Testing and assertion helpers for Go
License:        BSD-3-Clause
URL:            https://github.com/golangplus/testing
#!RemoteAsset:  sha256:31607eed9f48873f8a192fdf183ff683c638f2edebf695319c3aa654da044cf0
Source0:        https://github.com/golangplus/testing/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
# bytes tests need this assertion library; unpack bytes only for our own tests.
#!RemoteAsset:  sha256:cb706b4294713f66d67baa3e202202cf69b46510f1b7144df213a08e64ed61fa
Source1:        https://github.com/golangplus/bytes/archive/%{bytes_commit}.tar.gz#/bytes-%{bytes_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golangplus/fmt)

Provides:       go(github.com/golangplus/testing) = %{version}

Requires:       go(github.com/golangplus/fmt)

%description
This library provides assertion helpers and test log writers for Go.

%check -p
%{go_common}
%{go_prep}
mkdir -p %{_builddir}/go/src/github.com/golangplus/bytes
tar -xf %{SOURCE1} --strip-components=1 -C %{_builddir}/go/src/github.com/golangplus/bytes

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
