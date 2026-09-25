# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           signedxml
%define go_import_path  github.com/ma314smith/signedxml
%define commit_id       abc5b481ae1ce4e3076300046af90233ca18d8dd

Name:           go-github-ma314smith-signedxml
Version:        0+git20260922.abc5b48
Release:        %autorelease
Summary:        XML digital signature library for Go
License:        MIT
URL:            https://github.com/ma314smith/signedxml
#!RemoteAsset:  sha256:4122d8004e3f0c4876f751fb0d634779cfbe5ddbbccbd52c7921f21f9b28c7bc
Source0:        https://github.com/ma314smith/signedxml/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/beevik/etree)
BuildRequires:  go(github.com/smartystreets/goconvey)

Provides:       go(github.com/ma314smith/signedxml) = %{version}

Requires:       go(github.com/beevik/etree)

%description
XML digital signature library for Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
