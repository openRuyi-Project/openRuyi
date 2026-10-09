# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-restful
%define go_import_path  github.com/emicklei/go-restful
%define go_test_include  %{go_import_path}

Name:           go-github-emicklei-go-restful
Version:        2.9.5
Release:        %autorelease
Summary:        REST-style web services for Go
License:        MIT
URL:            https://github.com/emicklei/go-restful
VCS:            git:https://github.com/emicklei/go-restful.git
#!RemoteAsset:  sha256:7781be0cfcc41280191ef87194d9005730fd1971625c5f205dc3f181ac988547
Source0:        https://github.com/emicklei/go-restful/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-restful-2.9.5
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/emicklei/go-restful) = %{version}

%description
This package provides the github.com/emicklei/go-restful Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
