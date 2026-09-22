# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopherjs
%define go_import_path  github.com/gopherjs/gopherjs
%define go_test_include %{shrink:
    %{go_import_path}/compiler/analysis
    %{go_import_path}/compiler/astutil
    %{go_import_path}/compiler/filter
    %{go_import_path}/compiler/gopherjspkg
    %{go_import_path}/compiler/natives
    %{go_import_path}/compiler/prelude
    %{go_import_path}/compiler/typesutil
    %{go_import_path}/js
    %{go_import_path}/nosync
}

Name:           go-github-gopherjs-gopherjs
Version:        0+git20181017.0766667
Release:        %autorelease
Summary:        GopherJS compiles Go code (go.dev) to pure JavaScript code
License:        BSD-2-Clause
URL:            https://github.com/gopherjs/gopherjs
VCS:            git:https://github.com/gopherjs/gopherjs.git
#!RemoteAsset:  sha256:4af45714be5b8822514bf6a36f12c37c733fce6712c80116f3bb30dca84d72d2
Source0:        https://github.com/gopherjs/gopherjs/archive/0766667cb4d1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gopherjs-0766667cb4d1cfb8d5fde1fe210ae41ead3cf589

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gopherjs/gopherjs) = %{version}

%description
This package provides the github.com/gopherjs/gopherjs Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
