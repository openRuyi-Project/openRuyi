# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           signedxml
%define go_import_path  github.com/ma314smith/signedxml

Name:           go-github-ma314smith-signedxml
Version:        0+git20210628.abc5b48
Release:        %autorelease
Summary:        Transforms and validates signedxml documents
License:        MIT
URL:            https://github.com/ma314smith/signedxml
VCS:            git:https://github.com/ma314smith/signedxml.git
#!RemoteAsset:  sha256:4122d8004e3f0c4876f751fb0d634779cfbe5ddbbccbd52c7921f21f9b28c7bc
Source0:        https://github.com/ma314smith/signedxml/archive/abc5b481ae1c.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n signedxml-abc5b481ae1ce4e3076300046af90233ca18d8dd

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/beevik/etree)
BuildRequires:  go(github.com/smartystreets/goconvey)

Provides:       go(github.com/ma314smith/signedxml) = %{version}

Requires:       go(github.com/beevik/etree)

%description
This package provides the github.com/ma314smith/signedxml Go module source.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
